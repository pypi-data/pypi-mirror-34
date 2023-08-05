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
import numpy as np
import pytest

import cirq


def test_gate_operation_init():
    q = cirq.QubitId()
    g = cirq.Gate()
    v = cirq.GateOperation(g, (q,))
    assert v.gate == g
    assert v.qubits == (q,)


def test_gate_operation_eq():
    g1 = cirq.Gate()
    g2 = cirq.Gate()
    r1 = [cirq.QubitId()]
    r2 = [cirq.QubitId()]
    r12 = r1 + r2
    r21 = r2 + r1

    eq = cirq.testing.EqualsTester()
    eq.make_equality_group(lambda: cirq.GateOperation(g1, r1))
    eq.make_equality_group(lambda: cirq.GateOperation(g2, r1))
    eq.make_equality_group(lambda: cirq.GateOperation(g1, r2))
    eq.make_equality_group(lambda: cirq.GateOperation(g1, r12))
    eq.make_equality_group(lambda: cirq.GateOperation(g1, r21))
    eq.add_equality_group(cirq.GateOperation(cirq.CZ, r21),
                          cirq.GateOperation(cirq.CZ, r12))

    # Interchangeable subsets.

    class PairGate(cirq.Gate, cirq.InterchangeableQubitsGate):
        def qubit_index_to_equivalence_group_key(self, index: int):
            return index // 2

    p = PairGate()
    a0, a1, b0, b1, c0 = cirq.LineQubit.range(5)
    eq.add_equality_group(p(a0, a1, b0, b1), p(a1, a0, b1, b0))
    eq.add_equality_group(p(b0, b1, a0, a1))
    eq.add_equality_group(p(a0, a1, b0, b1, c0), p(a1, a0, b1, b0, c0))
    eq.add_equality_group(p(a0, b0, a1, b1, c0))
    eq.add_equality_group(p(a0, c0, b0, b1, a1))
    eq.add_equality_group(p(b0, a1, a0, b1, c0))


def test_gate_operation_pow():
    Y = cirq.Y
    qubit = cirq.QubitId()
    assert (Y ** 0.5)(qubit) == Y(qubit) ** 0.5


def test_with_qubits_and_transform_qubits():
    g = cirq.Gate()
    op = cirq.GateOperation(g, cirq.LineQubit.range(3))
    assert op.with_qubits(*cirq.LineQubit.range(2)
                          ) == cirq.GateOperation(g, cirq.LineQubit.range(2))
    assert op.transform_qubits(lambda e: cirq.LineQubit(-e.x)
                               ) == cirq.GateOperation(g, [cirq.LineQubit(0),
                                                           cirq.LineQubit(-1),
                                                           cirq.LineQubit(-2)])

    # The gate's constraints should be applied when changing the qubits.
    with pytest.raises(ValueError):
        _ = cirq.Y(cirq.LineQubit(0)).with_qubits(cirq.LineQubit(0),
                                                  cirq.LineQubit(1))


def test_extrapolate():
    q = cirq.NamedQubit('q')

    # If the gate isn't extrapolatable, you get a type error.
    op0 = cirq.GateOperation(cirq.Gate(), [q])
    assert not cirq.can_cast(cirq.ExtrapolatableEffect, op0)
    with pytest.raises(TypeError):
        _ = op0.extrapolate_effect(0.5)
    with pytest.raises(TypeError):
        _ = op0**0.5

    op1 = cirq.GateOperation(cirq.Y, [q])
    assert cirq.can_cast(cirq.ExtrapolatableEffect, op1)
    assert op1**0.5 == op1.extrapolate_effect(0.5) == cirq.GateOperation(
        cirq.Y**0.5, [q])
    assert (cirq.Y**0.5).on(q) == cirq.Y(q)**0.5


def test_inverse():
    q = cirq.NamedQubit('q')

    # If the gate isn't reversible, you get a type error.
    op0 = cirq.GateOperation(cirq.Gate(), [q])
    assert not cirq.can_cast(cirq.ReversibleEffect, op0)
    with pytest.raises(TypeError):
        _ = op0.inverse()

    op1 = cirq.GateOperation(cirq.S, [q])
    assert cirq.can_cast(cirq.ReversibleEffect, op1)
    assert op1.inverse() == cirq.GateOperation(cirq.S.inverse(), [q])
    assert cirq.S.inverse().on(q) == cirq.S.on(q).inverse()


def test_text_diagrammable():
    q = cirq.NamedQubit('q')

    # If the gate isn't diagrammable, you get a type error.
    op0 = cirq.GateOperation(cirq.Gate(), [q])
    assert not cirq.can_cast(cirq.TextDiagrammable, op0)
    with pytest.raises(TypeError):
        _ = op0.text_diagram_info(cirq.TextDiagramInfoArgs.UNINFORMED_DEFAULT)

    op1 = cirq.GateOperation(cirq.S, [q])
    assert cirq.can_cast(cirq.TextDiagrammable, op1)
    actual = op1.text_diagram_info(cirq.TextDiagramInfoArgs.UNINFORMED_DEFAULT)
    expected = cirq.S.text_diagram_info(
        cirq.TextDiagramInfoArgs.UNINFORMED_DEFAULT)
    assert actual == expected


def test_bounded_effect():
    q = cirq.NamedQubit('q')

    # If the gate isn't bounded, you get a type error.
    op0 = cirq.GateOperation(cirq.Gate(), [q])
    assert not cirq.can_cast(cirq.BoundedEffect, op0)
    with pytest.raises(TypeError):
        _ = op0.trace_distance_bound()

    op1 = cirq.GateOperation(cirq.Z**0.000001, [q])
    assert cirq.can_cast(cirq.BoundedEffect, op1)
    assert op1.trace_distance_bound() == (cirq.Z**0.000001
                                          ).trace_distance_bound()


def test_parameterizable_effect():
    q = cirq.NamedQubit('q')
    r = cirq.ParamResolver({'a': 0.5})

    # If the gate isn't parameterizable, you get a type error.
    op0 = cirq.GateOperation(cirq.Gate(), [q])
    assert not cirq.can_cast(cirq.ParameterizableEffect, op0)
    with pytest.raises(TypeError):
        _ = op0.is_parameterized()
    with pytest.raises(TypeError):
        _ = op0.with_parameters_resolved_by(r)

    op1 = cirq.GateOperation(cirq.RotZGate(half_turns=cirq.Symbol('a')), [q])
    assert cirq.can_cast(cirq.ParameterizableEffect, op1)
    assert op1.is_parameterized()
    op2 = op1.with_parameters_resolved_by(r)
    assert not op2.is_parameterized()
    assert op2 == cirq.S.on(q)


def test_known_matrix():
    a = cirq.NamedQubit('a')
    b = cirq.NamedQubit('b')

    # If the gate has no matrix, you get a type error.
    op0 = cirq.measure(a)
    assert not cirq.can_cast(cirq.KnownMatrix, op0)
    with pytest.raises(TypeError):
        _ = op0.matrix()

    op1 = cirq.X(a)
    assert cirq.can_cast(cirq.KnownMatrix, op1)
    np.testing.assert_allclose(op1.matrix(),
                               np.array([[0, 1], [1, 0]]))
    op2 = cirq.CNOT(a, b)
    op3 = cirq.CNOT(a, b)
    np.testing.assert_allclose(op2.matrix(), cirq.CNOT.matrix())
    np.testing.assert_allclose(op3.matrix(), cirq.CNOT.matrix())
