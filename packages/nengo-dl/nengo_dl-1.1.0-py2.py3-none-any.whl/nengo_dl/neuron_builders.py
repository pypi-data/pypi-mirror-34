import logging

from nengo.builder.neurons import SimNeurons
from nengo.neurons import (RectifiedLinear, SpikingRectifiedLinear, Sigmoid,
                           LIF, LIFRate)
import numpy as np
import tensorflow as tf

from nengo_dl import utils
from nengo_dl.builder import Builder, OpBuilder
from nengo_dl.neurons import SoftLIFRate

logger = logging.getLogger(__name__)


@Builder.register(SimNeurons)
class SimNeuronsBuilder(OpBuilder):
    """Builds a group of :class:`~nengo:nengo.builder.neurons.SimNeurons`
    operators.

    Calls the appropriate sub-build class for the different neuron types.

    Attributes
    ----------
    TF_NEURON_IMPL : list of :class:`~nengo:nengo.neurons.NeuronType`
        The neuron types that have a custom implementation
    """

    TF_NEURON_IMPL = (RectifiedLinear, SpikingRectifiedLinear, Sigmoid,
                      LIF, LIFRate, SoftLIFRate)

    def __init__(self, ops, signals):
        super(SimNeuronsBuilder, self).__init__(ops, signals)

        logger.debug("J %s", [op.J for op in ops])

        neuron_type = type(ops[0].neurons)

        # if we have a custom tensorflow implementation for this neuron type,
        # then we build that. otherwise we'll just execute the neuron step
        # function externally (using `tf.py_func`), so we just need to set up
        # the inputs/outputs for that.
        if neuron_type in self.TF_NEURON_IMPL:
            # note: we do this two-step check (even though it's redundant) to
            # make sure that TF_NEURON_IMPL is kept up to date

            if neuron_type == RectifiedLinear:
                self.built_neurons = RectifiedLinearBuilder(ops, signals)
            elif neuron_type == SpikingRectifiedLinear:
                self.built_neurons = SpikingRectifiedLinearBuilder(
                    ops, signals)
            elif neuron_type == Sigmoid:
                self.built_neurons = SigmoidBuilder(ops, signals)
            elif neuron_type == LIFRate:
                self.built_neurons = LIFRateBuilder(ops, signals)
            elif neuron_type == LIF:
                self.built_neurons = LIFBuilder(ops, signals)
            elif neuron_type == SoftLIFRate:
                self.built_neurons = SoftLIFRateBuilder(ops, signals)
        else:
            self.built_neurons = GenericNeuronBuilder(ops, signals)

    def build_step(self, signals):
        self.built_neurons.build_step(signals)


class GenericNeuronBuilder(OpBuilder):
    """Builds all neuron types for which there is no custom Tensorflow
    implementation.

    Notes
    -----
    These will be executed as native Python functions, requiring execution to
    move in and out of TensorFlow.  This can significantly slow down the
    simulation, so any performance-critical neuron models should consider
    adding a custom TensorFlow implementation for their neuron type instead.
    """

    def __init__(self, ops, signals):
        super(GenericNeuronBuilder, self).__init__(ops, signals)

        self.J_data = signals.combine([op.J for op in ops])
        self.output_data = signals.combine([op.output for op in ops])
        self.state_data = [signals.combine([op.states[i] for op in ops])
                           for i in range(len(ops[0].states))]

        self.prev_result = []

        def neuron_step_math(dt, J, *states):  # pragma: no cover
            output = None
            J_offset = 0
            state_offset = [0 for _ in states]
            for op in ops:
                # slice out the individual state vectors from the overall
                # array
                op_J = J[J_offset:J_offset + op.J.shape[0]]
                J_offset += op.J.shape[0]

                op_states = []
                for j, s in enumerate(op.states):
                    op_states += [states[j][state_offset[j]:
                                  state_offset[j] + s.shape[0]]]
                    state_offset[j] += s.shape[0]

                # call step_math function
                # note: `op_states` are views into `states`, which will
                # be updated in-place
                mini_out = []
                for j in range(signals.minibatch_size):
                    # blank output variable
                    neuron_output = np.zeros(
                        op.output.shape, self.output_data.dtype)
                    op.neurons.step_math(dt, op_J[..., j], neuron_output,
                                         *[s[..., j] for s in op_states])
                    mini_out += [neuron_output]
                neuron_output = np.stack(mini_out, axis=-1)

                # concatenate outputs
                if output is None:
                    output = neuron_output
                else:
                    output = np.concatenate((output, neuron_output),
                                            axis=0)

            return (output,) + states

        self.neuron_step_math = neuron_step_math
        self.neuron_step_math.__name__ = utils.sanitize_name(
            "_".join([repr(op.neurons) for op in ops]))

    def build_step(self, signals):
        J = signals.gather(self.J_data)
        states = [signals.gather(x) for x in self.state_data]
        states_dtype = [x.dtype for x in self.state_data]

        # note: we need to make sure that the previous call to this function
        # has completed before the next starts, since we don't know that the
        # functions are thread safe
        with tf.control_dependencies(self.prev_result), tf.device("/cpu:0"):
            ret = tf.py_func(
                self.neuron_step_math, [signals.dt, J] + states,
                [self.output_data.dtype] + states_dtype,
                name=self.neuron_step_math.__name__)
            neuron_out, state_out = ret[0], ret[1:]
        self.prev_result = [neuron_out]

        neuron_out.set_shape(
            self.output_data.shape + (signals.minibatch_size,))
        signals.scatter(self.output_data, neuron_out)

        for i, s in enumerate(self.state_data):
            state_out[i].set_shape(s.shape + (signals.minibatch_size,))
            signals.scatter(s, state_out[i])


class RectifiedLinearBuilder(OpBuilder):
    """Build a group of :class:`~nengo:nengo.RectifiedLinear`
    neuron operators."""

    def __init__(self, ops, signals):
        super(RectifiedLinearBuilder, self).__init__(ops, signals)

        self.J_data = signals.combine([op.J for op in ops])
        self.output_data = signals.combine([op.output for op in ops])

        if all(op.neurons.amplitude == 1 for op in ops):
            self.amplitude = None
        else:
            self.amplitude = signals.op_constant(
                [op.neurons for op in ops], [op.J.shape[0] for op in ops],
                "amplitude", signals.dtype)

    def build_step(self, signals):
        J = signals.gather(self.J_data)
        out = tf.nn.relu(J)
        if self.amplitude is not None:
            out *= self.amplitude
        signals.scatter(self.output_data, out)


class SpikingRectifiedLinearBuilder(RectifiedLinearBuilder):
    """Build a group of :class:`~nengo:nengo.SpikingRectifiedLinear` neuron
       operators."""

    def __init__(self, ops, signals):
        super(SpikingRectifiedLinearBuilder, self).__init__(ops, signals)

        self.voltage_data = signals.combine([op.states[0] for op in ops])

        self.alpha = 1 if self.amplitude is None else self.amplitude
        self.alpha /= signals.dt

    def build_step(self, signals):
        J = signals.gather(self.J_data)
        voltage = signals.gather(self.voltage_data)

        voltage += tf.nn.relu(J) * signals.dt
        n_spikes = tf.floor(voltage)

        signals.scatter(self.output_data, self.alpha * n_spikes)

        voltage -= n_spikes
        signals.scatter(self.voltage_data, voltage)


class SigmoidBuilder(OpBuilder):
    """Build a group of :class:`~nengo:nengo.Sigmoid` neuron operators."""

    def __init__(self, ops, signals):
        super(SigmoidBuilder, self).__init__(ops, signals)

        self.J_data = signals.combine([op.J for op in ops])
        self.output_data = signals.combine([op.output for op in ops])

        self.tau_ref = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "tau_ref", signals.dtype)

    def build_step(self, signals):
        J = signals.gather(self.J_data)
        signals.scatter(self.output_data, tf.nn.sigmoid(J) / self.tau_ref)


class LIFRateBuilder(OpBuilder):
    """Build a group of :class:`~nengo:nengo.LIFRate` neuron operators."""

    def __init__(self, ops, signals):
        super(LIFRateBuilder, self).__init__(ops, signals)

        self.tau_ref = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "tau_ref", signals.dtype)
        self.tau_rc = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "tau_rc", signals.dtype)
        self.amplitude = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "amplitude", signals.dtype)

        self.J_data = signals.combine([op.J for op in ops])
        self.output_data = signals.combine([op.output for op in ops])
        self.zeros = tf.zeros(self.J_data.shape + (signals.minibatch_size,),
                              signals.dtype)

        self.zero = tf.constant(0, dtype=signals.dtype)
        self.one = tf.constant(1, dtype=signals.dtype)
        self.epsilon = tf.constant(1e-15, dtype=signals.dtype)

    def build_step(self, signals):
        j = signals.gather(self.J_data)
        j -= self.one

        # note: we convert all the j to be positive before this calculation
        # (even though we'll only use the values that are already positive),
        # otherwise we can end up with nans in the gradient
        rates = self.amplitude / (
            self.tau_ref + self.tau_rc * tf.log1p(tf.reciprocal(
                tf.maximum(j, self.epsilon))))

        signals.scatter(self.output_data, tf.where(j > self.zero, rates,
                                                   self.zeros))


class LIFBuilder(LIFRateBuilder):
    """Build a group of :class:`~nengo:nengo.LIF` neuron operators."""

    def __init__(self, ops, signals):
        super(LIFBuilder, self).__init__(ops, signals)

        self.min_voltage = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "min_voltage", signals.dtype)
        self.amplitude /= signals.dt

        self.voltage_data = signals.combine([op.states[0] for op in ops])
        self.refractory_data = signals.combine([op.states[1] for op in ops])

    def build_step(self, signals):
        J = signals.gather(self.J_data)
        voltage = signals.gather(self.voltage_data)
        refractory = signals.gather(self.refractory_data)

        delta_t = tf.clip_by_value(signals.dt - refractory, self.zero,
                                   signals.dt)

        dV = (voltage - J) * tf.expm1(-delta_t / self.tau_rc)
        voltage += dV

        spiked = voltage > self.one
        spikes = tf.cast(spiked, signals.dtype) * self.amplitude
        signals.scatter(self.output_data, spikes)

        partial_ref = -self.tau_rc * tf.log1p((self.one - voltage) /
                                              (J - self.one))
        # FastLIF version (linearly approximate spike time when calculating
        # remaining refractory period)
        # partial_ref = signals.dt * (voltage - self.one) / dV

        refractory = tf.where(spiked, self.tau_ref - partial_ref,
                              refractory - signals.dt)

        signals.mark_gather(self.J_data)
        signals.scatter(self.refractory_data, refractory)

        voltage = tf.where(spiked, self.zeros,
                           tf.maximum(voltage, self.min_voltage))
        signals.scatter(self.voltage_data, voltage)


class SoftLIFRateBuilder(LIFRateBuilder):
    """Build a group of :class:`.SoftLIFRate` neuron operators."""

    def __init__(self, ops, signals):
        super(SoftLIFRateBuilder, self).__init__(ops, signals)

        self.sigma = signals.op_constant(
            [op.neurons for op in ops], [op.J.shape[0] for op in ops],
            "sigma", signals.dtype)

    def build_step(self, signals):
        j = signals.gather(self.J_data)

        j -= self.one

        js = j / self.sigma
        j_valid = js > -20
        js_safe = tf.where(j_valid, js, self.zeros)

        # softplus(js) = log(1 + e^js)
        z = tf.nn.softplus(js_safe) * self.sigma

        # as z->0
        #   z = s*log(1 + e^js) = s*e^js
        #   log(1 + 1/z) = log(1/z) = -log(s*e^js) = -js - log(s)
        q = tf.where(j_valid,
                     tf.log1p(tf.reciprocal(z)),
                     -js - tf.log(self.sigma))

        rates = self.amplitude / (self.tau_ref + self.tau_rc * q)

        signals.scatter(self.output_data, rates)
