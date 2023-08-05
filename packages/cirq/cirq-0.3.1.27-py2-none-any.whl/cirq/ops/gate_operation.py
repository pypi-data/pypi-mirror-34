# coding=utf-8
# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

u"""Basic types defining qubits, gates, and operations."""

from __future__ import absolute_import
from typing import (
    Optional, Sequence, FrozenSet, Tuple, Union, TYPE_CHECKING, cast
)

import numpy as np

from cirq import extension
from cirq.ops import raw_types, gate_features

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from cirq import study
    from typing import Dict, List


LIFTED_POTENTIAL_TYPES = dict((t, t) for t in [
    gate_features.BoundedEffect,
    gate_features.ExtrapolatableEffect,
    gate_features.KnownMatrix,
    gate_features.ParameterizableEffect,
    gate_features.PhaseableEffect,
    gate_features.ReversibleEffect,
    gate_features.TextDiagrammable,
])

LIFTED_POTENTIAL_TYPES[
    gate_features.CompositeOperation] = gate_features.CompositeGate
LIFTED_POTENTIAL_TYPES[
    gate_features.QasmConvertableOperation] = gate_features.QasmConvertableGate


class GateOperation(raw_types.Operation,
                    extension.PotentialImplementation[Union[
                        gate_features.BoundedEffect,
                        gate_features.CompositeOperation,
                        gate_features.ExtrapolatableEffect,
                        gate_features.KnownMatrix,
                        gate_features.ParameterizableEffect,
                        gate_features.PhaseableEffect,
                        gate_features.ReversibleEffect,
                        gate_features.TextDiagrammable,
                        gate_features.QasmConvertableOperation,
                    ]]):
    u"""An application of a gate to a collection of qubits.

    Attributes:
        gate: The applied gate.
        qubits: A sequence of the qubits on which the gate is applied.
    """

    def __init__(self,
                 gate,
                 qubits):
        self._gate = gate
        self._qubits = tuple(qubits)

    @property
    def gate(self):
        return self._gate

    @property
    def qubits(self):
        return self._qubits

    def with_qubits(self, *new_qubits):
        return self.gate.on(*new_qubits)

    def with_gate(self, new_gate):
        return new_gate.on(*self.qubits)

    def __repr__(self):
        return u'GateOperation({!r}, {!r})'.format(self.gate, self.qubits)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __unicode__(self):
        return u'{}({})'.format(self.gate,
                               u', '.join(unicode(e) for e in self.qubits))

    def _group_interchangeable_qubits(self):

        cast_gate = extension.try_cast(gate_features.InterchangeableQubitsGate,
                                       self.gate)
        if cast_gate is None:
            return self.qubits

        groups = {}  # type: Dict[int, List[raw_types.QubitId]]
        for i, q in enumerate(self.qubits):
            k = cast_gate.qubit_index_to_equivalence_group_key(i)
            if k not in groups:
                groups[k] = []
            groups[k].append(q)
        return tuple(sorted((k, frozenset(v)) for k, v in groups.items()))

    def _eq_tuple(self):
        grouped_qubits = self._group_interchangeable_qubits()
        return raw_types.Operation, self.gate, grouped_qubits

    def __hash__(self):
        return hash(self._eq_tuple())

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._eq_tuple() == other._eq_tuple()

    def __ne__(self, other):
        return not self == other

    def try_cast_to(self, desired_type, extensions):
        desired_gate_type = LIFTED_POTENTIAL_TYPES.get(desired_type)
        if desired_gate_type is not None:
            cast_gate = extensions.try_cast(desired_gate_type, self.gate)
            if cast_gate is not None:
                return self.with_gate(cast_gate)
        return None

    def default_decompose(self):
        cast_gate = extension.cast(gate_features.CompositeGate, self.gate)
        return cast_gate.default_decompose(self.qubits)

    def matrix(self):
        cast_gate = extension.cast(gate_features.KnownMatrix, self.gate)
        return cast_gate.matrix()

    def text_diagram_info(self, args
                          ):
        cast_gate = extension.cast(gate_features.TextDiagrammable, self.gate)
        return cast_gate.text_diagram_info(args)

    def trace_distance_bound(self):
        cast_gate = extension.cast(gate_features.BoundedEffect, self.gate)
        return cast_gate.trace_distance_bound()

    def inverse(self):
        cast_gate = extension.cast(gate_features.ReversibleEffect, self.gate)
        return self.with_gate(cast(raw_types.Gate, cast_gate.inverse()))

    def extrapolate_effect(self, factor):
        cast_gate = extension.cast(gate_features.ExtrapolatableEffect,
                                   self.gate)
        return self.with_gate(cast(raw_types.Gate,
                                   cast_gate.extrapolate_effect(factor)))

    def phase_by(self, phase_turns, qubit_index):
        cast_gate = extension.cast(gate_features.PhaseableEffect,
                                   self.gate)
        return self.with_gate(cast(raw_types.Gate,
                                   cast_gate.phase_by(phase_turns,
                                                      qubit_index)))

    def __pow__(self, power):
        u"""Raise gate to a power, then reapply to the same qubits.

        Only works if the gate implements cirq.ExtrapolatableEffect.
        For extrapolatable gate G this means the following two are equivalent:

            (G ** 1.5)(qubit)  or  G(qubit) ** 1.5

        Args:
            power: The amount to scale the gate's effect by.

        Returns:
            A new operation on the same qubits with the scaled gate.
        """
        return self.extrapolate_effect(power)

    def is_parameterized(self):
        cast_gate = extension.cast(gate_features.ParameterizableEffect,
                                   self.gate)
        return cast_gate.is_parameterized()

    def with_parameters_resolved_by(self,
                                    param_resolver,
                                    ):
        cast_gate = extension.cast(gate_features.ParameterizableEffect,
                                   self.gate)
        new_gate = cast_gate.with_parameters_resolved_by(param_resolver)
        return self.with_gate(cast(raw_types.Gate, new_gate))

    def known_qasm_output(self,
                          args):
        cast_gate = extension.cast(gate_features.QasmConvertableGate,
                                   self.gate)
        return cast_gate.known_qasm_output(self.qubits, args)
