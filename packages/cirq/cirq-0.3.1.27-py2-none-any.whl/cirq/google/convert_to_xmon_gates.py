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

from __future__ import absolute_import
from cirq import ops
from cirq.circuits.optimization_pass import (
    PointOptimizationSummary,
    PointOptimizer,
)
from cirq.extension import Extensions
from cirq.google.decompositions import (
    single_qubit_matrix_to_native_gates,
    two_qubit_matrix_to_native_gates,
)
from cirq.google.xmon_gate_extensions import xmon_gate_ext
from cirq.google.xmon_gates import XmonGate


class ConvertToXmonGates(PointOptimizer):
    u"""Attempts to convert strange gates into XmonGates.

    First, checks if the given extensions are able to cast the gate into an
        XmonGate instance.

    Second, checks if the given extensions are able to cast the operation into a
        KnownMatrix. If so, and the gate is a 1-qubit or 2-qubit gate, then
        performs circuit synthesis of the operation.

    Third, checks if the given extensions are able to cast the operation into a
        CompositeOperation. If so, recurses on the decomposition.

    Fourth, if ignore_failures is set, gives up and returns the gate unchanged.
        Otherwise raises a TypeError.
    """

    def __init__(self,
                 extensions=None,
                 ignore_failures=False):
        u"""
        Args:
            extensions: The extensions instance to use when trying to
                cast gates to known types. Defaults to the standard xmon
                gate extension.
            ignore_failures: If set, gates that fail to convert are forwarded
                unchanged. If not set, conversion failures raise a TypeError.
        """
        self.extensions = extensions or xmon_gate_ext
        self.ignore_failures = ignore_failures

    def _convert_one(self, op):
        # Already supported?
        if isinstance(op, ops.GateOperation) and isinstance(op.gate, XmonGate):
            return op

        # Maybe we know how to wrap it?
        if isinstance(op, ops.GateOperation):
            xmon = self.extensions.try_cast(XmonGate, op.gate)
            if xmon is not None:
                return xmon.on(*op.qubits)

        # Known matrix?
        mat = self.extensions.try_cast(ops.KnownMatrix, op)
        if mat is not None and len(op.qubits) == 1:
            gates = single_qubit_matrix_to_native_gates(mat.matrix())
            return [g.on(op.qubits[0]) for g in gates]
        if mat is not None and len(op.qubits) == 2:
            return two_qubit_matrix_to_native_gates(
                op.qubits[0],
                op.qubits[1],
                mat.matrix(),
                allow_partial_czs=True)

        # Provides a decomposition?
        composite_op = self.extensions.try_cast(ops.CompositeOperation, op)
        if composite_op is not None:
            return composite_op.default_decompose()

        # Just let it be?
        if self.ignore_failures:
            return op

        raise TypeError(u"Don't know how to work with {!r}. "
                        u"It isn't a GateOperation with an XmonGate, "
                        u"a 1-qubit KnownMatrix, "
                        u"a 2-qubit KnownMatrix, "
                        u"or a CompositeOperation.".format(op))

    def convert(self, op):
        converted = self._convert_one(op)
        if converted is op:
            return converted
        return [self.convert(e) for e in ops.flatten_op_tree(converted)]

    def optimization_at(self, circuit, index, op):
        converted = self.convert(op)
        if converted is op:
            return None

        return PointOptimizationSummary(
            clear_span=1,
            new_operations=converted,
            clear_qubits=op.qubits)
