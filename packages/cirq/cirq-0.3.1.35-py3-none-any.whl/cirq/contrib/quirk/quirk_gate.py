# Copyright 2018 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, Any, Union

import numpy as np

from cirq import ops, Symbol
from cirq.extension import Extensions
from cirq.google.xmon_gates import ExpZGate, Exp11Gate, ExpWGate


class QuirkOp:
    """An operation as understood by Quirk's parser.

    Basically just a series of text identifiers for each qubit, and some rules
    for how things can be combined.
    """

    def __init__(self, *keys: Any, can_merge: bool=True) -> None:
        """
        Args:
            *keys: The JSON object(s) that each qubit is turned into when
                explaining a gate to Quirk. For example, a CNOT is turned into
                the keys ["•", "X"].

                Note that, when keys terminates early, it is implied that later
                qubits should use the same key as the last key.
            can_merge: Whether or not it is safe to merge a column containing
                this operation into a column containing other operations. For
                example, this is not safe if the column contains a control
                because the control would also apply to the other column's
                gates.
        """
        self.keys = keys
        self.can_merge = can_merge


UNKNOWN_GATE = QuirkOp('UNKNOWN', can_merge=False)


def same_half_turns(a1: float, a2: float, atol=0.0001) -> bool:
    d = (a1 - a2 + 1) % 2 - 1
    return abs(d) < atol


def angle_to_exponent_key(t: Union[float, Symbol]) -> Optional[str]:
    if isinstance(t, Symbol):
        return '^t'

    if same_half_turns(t, 1):
        return ''

    if same_half_turns(t, 0.5):
        return '^½'

    if same_half_turns(t, -0.5):
        return '^-½'

    if same_half_turns(t, 0.25):
        return '^¼'

    if same_half_turns(t, -0.25):
        return '^-¼'

    return None


def z_to_known(gate: Union[ExpZGate, ops.RotZGate]) -> Optional[QuirkOp]:
    e = angle_to_exponent_key(gate.half_turns)
    if e is None:
        return None
    return QuirkOp('Z' + e)


def x_to_known(gate: Union[ops.RotXGate, ExpWGate]) -> Optional[QuirkOp]:
    e = angle_to_exponent_key(gate.half_turns)
    if e is None:
        return None
    return QuirkOp('X' + e)


def y_to_known(gate: Union[ops.RotYGate, ExpWGate]) -> Optional[QuirkOp]:
    e = angle_to_exponent_key(gate.half_turns)
    if e is None:
        return None
    return QuirkOp('Y' + e)


def cz_to_known(gate: Union[ops.Rot11Gate, Exp11Gate]) -> Optional[QuirkOp]:
    e = angle_to_exponent_key(gate.half_turns)
    if e is None:
        return None
    return QuirkOp('•', 'Z' + e, can_merge=False)


def w_to_known(gate: ExpWGate) -> Optional[QuirkOp]:
    if isinstance(gate.axis_half_turns, Symbol):
        return None
    p = (gate.axis_half_turns + 1) % 2 - 1
    if same_half_turns(p, 0):
        return x_to_known(gate)
    if same_half_turns(p, 0.5):
        return y_to_known(gate)
    return None


def single_qubit_matrix_gate(gate: ops.KnownMatrix) -> Optional[QuirkOp]:
    matrix = gate.matrix()
    if matrix.shape[0] != 2:
        return None

    matrix = matrix.round(6)
    matrix_repr = '{{%s+%si,%s+%si},{%s+%si,%s+%si}}' % (
        np.real(matrix[0, 0]), np.imag(matrix[0, 0]),
        np.real(matrix[1, 0]), np.imag(matrix[1, 0]),
        np.real(matrix[0, 1]), np.imag(matrix[0, 1]),
        np.real(matrix[1, 1]), np.imag(matrix[1, 1]))

    # Clean up.
    matrix_repr = matrix_repr.replace('+-', '-')
    matrix_repr = matrix_repr.replace('+0.0i', '')
    matrix_repr = matrix_repr.replace('.0,', ',')
    matrix_repr = matrix_repr.replace('.0}', '}')
    matrix_repr = matrix_repr.replace('.0+', '+')
    matrix_repr = matrix_repr.replace('.0-', '-')

    return QuirkOp({
        'id': '?',
        'matrix': matrix_repr
    })


quirk_gate_ext = Extensions()
quirk_gate_ext.add_recursive_cast(
    QuirkOp,
    ops.GateOperation,
    lambda ext, op: ext.try_cast(QuirkOp, op.gate))
quirk_gate_ext.add_cast(QuirkOp, ops.RotXGate, x_to_known)
quirk_gate_ext.add_cast(QuirkOp, ops.RotYGate, y_to_known)
quirk_gate_ext.add_cast(QuirkOp, ops.RotZGate, z_to_known)
quirk_gate_ext.add_cast(QuirkOp, ExpZGate, z_to_known)
quirk_gate_ext.add_cast(QuirkOp, ExpWGate, w_to_known)
quirk_gate_ext.add_cast(QuirkOp, ops.Rot11Gate, cz_to_known)
quirk_gate_ext.add_cast(QuirkOp, Exp11Gate, cz_to_known)
quirk_gate_ext.add_cast(QuirkOp,
                        ops.CNotGate,
                        lambda e: QuirkOp('•', 'X',
                                          can_merge=False))
quirk_gate_ext.add_cast(QuirkOp,
                        ops.SwapGate,
                        lambda e: QuirkOp('Swap', 'Swap'))
quirk_gate_ext.add_cast(QuirkOp,
                        ops.HGate,
                        lambda e: QuirkOp('H'))
quirk_gate_ext.add_cast(QuirkOp,
                        ops.MeasurementGate,
                        lambda e: QuirkOp('Measure'))
