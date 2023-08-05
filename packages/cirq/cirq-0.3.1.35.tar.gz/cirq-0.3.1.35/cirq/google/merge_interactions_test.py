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

import cirq
import cirq.google as cg


def assert_optimizes(before: cirq.Circuit, expected: cirq.Circuit):
    actual = cirq.Circuit(before)
    opt = cg.MergeInteractions()
    opt.optimize_circuit(actual)

    # Ignore differences that would be caught by follow-up optimizations.
    followup_optimizations = [
        cg.MergeRotations(),
        cg.EjectFullW(),
        cg.EjectZ(),
        cirq.DropNegligible(),
        cirq.DropEmptyMoments()
    ]
    for post in followup_optimizations:
        post.optimize_circuit(actual)
        post.optimize_circuit(expected)

    if actual != expected:
        # coverage: ignore
        print('ACTUAL')
        print(actual)
        print('EXPECTED')
        print(expected)
    assert actual == expected


def assert_optimization_not_broken(circuit):
    """Check that the unitary matrix for the input circuit is the same (up to
    global phase and rounding error) as the unitary matrix of the optimized
    circuit."""
    u_before = circuit.to_unitary_matrix()
    cg.MergeInteractions().optimize_circuit(circuit)
    u_after = circuit.to_unitary_matrix()

    cirq.testing.assert_allclose_up_to_global_phase(
        u_before, u_after, atol=1e-8)


def test_clears_paired_cnot():
    a, b = cirq.LineQubit.range(2)
    assert_optimizes(
        before=cirq.Circuit([
            cirq.Moment([cirq.CNOT(a, b)]),
            cirq.Moment([cirq.CNOT(a, b)]),
        ]),
        expected=cirq.Circuit())


def test_ignores_czs_separated_by_parameterized():
    a, b = cirq.LineQubit.range(2)
    assert_optimizes(
        before=cirq.Circuit([
            cirq.Moment([cirq.CZ(a, b)]),
            cirq.Moment([cg.ExpZGate(
                half_turns=cirq.Symbol('boo'))(a)]),
            cirq.Moment([cirq.CZ(a, b)]),
        ]),
        expected=cirq.Circuit([
            cirq.Moment([cirq.CZ(a, b)]),
            cirq.Moment([cg.ExpZGate(
                half_turns=cirq.Symbol('boo'))(a)]),
            cirq.Moment([cirq.CZ(a, b)]),
        ]))


def test_ignores_czs_separated_by_outer_cz():
    q00 = cirq.GridQubit(0, 0)
    q01 = cirq.GridQubit(0, 1)
    q10 = cirq.GridQubit(1, 0)
    assert_optimizes(
        before=cirq.Circuit([
            cirq.Moment([cirq.CZ(q00, q01)]),
            cirq.Moment([cirq.CZ(q00, q10)]),
            cirq.Moment([cirq.CZ(q00, q01)]),
        ]),
        expected=cirq.Circuit([
            cirq.Moment([cirq.CZ(q00, q01)]),
            cirq.Moment([cirq.CZ(q00, q10)]),
            cirq.Moment([cirq.CZ(q00, q01)]),
        ]))


def test_cnots_separated_by_single_gates_correct():
    a, b = cirq.LineQubit.range(2)
    assert_optimization_not_broken(
        cirq.Circuit.from_ops(
            cirq.CNOT(a, b),
            cirq.H(b),
            cirq.CNOT(a, b),
        ))


def test_czs_separated_by_single_gates_correct():
    a, b = cirq.LineQubit.range(2)
    assert_optimization_not_broken(
        cirq.Circuit.from_ops(
            cirq.CZ(a, b),
            cirq.X(b),
            cirq.X(b),
            cirq.X(b),
            cirq.CZ(a, b),
        ))


def test_inefficient_circuit_correct():
    t = 0.1
    v = 0.11
    a, b = cirq.LineQubit.range(2)
    assert_optimization_not_broken(
        cirq.Circuit.from_ops(
            cirq.H(b),
            cirq.CNOT(a, b),
            cirq.H(b),
            cirq.CNOT(a, b),
            cirq.CNOT(b, a),
            cirq.H(a),
            cirq.CNOT(a, b),
            cirq.Z(a)**t, cirq.Z(b)**-t,
            cirq.CNOT(a, b),
            cirq.H(a), cirq.Z(b)**v,
            cirq.CNOT(a, b),
            cirq.Z(a)**-v, cirq.Z(b)**-v,
        ))


def test_optimizes_single_iswap():
    a, b = cirq.LineQubit.range(2)
    c = cirq.Circuit.from_ops(cirq.ISWAP(a, b))
    assert_optimization_not_broken(c)
    cg.MergeInteractions().optimize_circuit(c)
    assert len([1 for op in c.all_operations() if len(op.qubits) == 2]) == 2
    assert all(cg.XmonGate.is_xmon_op(op)
               for op in c.all_operations())
