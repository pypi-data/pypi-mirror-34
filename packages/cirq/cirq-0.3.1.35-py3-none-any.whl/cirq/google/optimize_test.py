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

import pytest

import cirq
import cirq.google as cg

from cirq.testing import (
    assert_circuits_with_terminal_measurements_are_equivalent,
)


@pytest.mark.parametrize('n,d', [
    (3, 2),
    (4, 3),
    (4, 4),
    (5, 4),
    (22, 4),
])
def test_swap_field(n: int, d: int):
    before = cirq.Circuit.from_ops(
        cirq.ISWAP(cirq.LineQubit(j), cirq.LineQubit(j + 1))
        for i in range(d)
        for j in range(i % 2, n - 1, 2)
    )
    before.append(cirq.measure(*before.all_qubits()))

    after = cg.optimized_for_xmon(before)

    assert len(after) == d*4 + 2
    if n <= 5:
        assert_circuits_with_terminal_measurements_are_equivalent(
            before, after, atol=1e-4)


def test_ccz():
    before = cirq.Circuit.from_ops(
        cirq.CCZ(cirq.GridQubit(5, 5),
                 cirq.GridQubit(5, 6),
                 cirq.GridQubit(5, 7)))

    after = cg.optimized_for_xmon(before)

    assert len(after) <= 22
    assert_circuits_with_terminal_measurements_are_equivalent(
        before, after, atol=1e-4)


def test_adjacent_cz_get_split_apart():
    before = cirq.Circuit([cirq.Moment([
        cirq.CZ(cirq.GridQubit(0, 0), cirq.GridQubit(0, 1)),
        cirq.CZ(cirq.GridQubit(1, 0), cirq.GridQubit(1, 1))])])

    after = cg.optimized_for_xmon(before,
                                  new_device=cg.Foxtail)

    assert after == cirq.Circuit([
        cirq.Moment([
            cg.Exp11Gate().on(cirq.GridQubit(0, 0), cirq.GridQubit(0, 1))]),
        cirq.Moment([
            cg.Exp11Gate().on(cirq.GridQubit(1, 0), cirq.GridQubit(1, 1))])],
        device=cg.Foxtail)


def test_remap_qubits():
    before = cirq.Circuit([cirq.Moment([
        cirq.CZ(cirq.LineQubit(0), cirq.LineQubit(1))])])

    after = cg.optimized_for_xmon(before,
                                  new_device=cg.Foxtail,
                                  qubit_map=lambda q: cirq.GridQubit(q.x, 0))

    assert after == cirq.Circuit([
        cirq.Moment([
            cg.Exp11Gate().on(cirq.GridQubit(0, 0), cirq.GridQubit(1, 0))])],
        device=cg.Foxtail)
