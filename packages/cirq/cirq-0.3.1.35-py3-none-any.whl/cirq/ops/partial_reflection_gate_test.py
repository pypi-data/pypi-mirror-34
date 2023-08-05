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

from typing import Union

import numpy as np

import cirq
from cirq.ops.partial_reflection_gate import PartialReflectionGate
from cirq.study import ParamResolver
from cirq.testing import EqualsTester
from cirq.value import Symbol


class DummyGate(PartialReflectionGate):

    def _with_half_turns(self, half_turns: Union[Symbol, float] = 1.0):
        return DummyGate(half_turns=half_turns)

    def _reflection_matrix(self):
        return np.diag([1, -1])


def test_partial_reflection_gate_init():
    assert DummyGate(half_turns=0.5).half_turns == 0.5
    assert DummyGate(half_turns=5).half_turns == 1


def test_partial_reflection_gate_eq():
    eq = EqualsTester()
    eq.add_equality_group(DummyGate(), DummyGate(half_turns=1))
    eq.add_equality_group(DummyGate(half_turns=3.5), DummyGate(half_turns=-0.5))
    eq.make_equality_group(lambda: DummyGate(half_turns=Symbol('a')))
    eq.make_equality_group(lambda: DummyGate(half_turns=Symbol('b')))
    eq.make_equality_group(lambda: DummyGate(half_turns=0))
    eq.add_equality_group(DummyGate(half_turns=0.5),
                          DummyGate(rads=np.pi / 2),
                          DummyGate(degs=90))


def test_partial_reflection_gate_extrapolate():
    assert (DummyGate(half_turns=1).extrapolate_effect(0.5) ==
            DummyGate(half_turns=0.5))
    assert DummyGate()**-0.25 == DummyGate(half_turns=1.75)


def test_partial_reflection_gate_inverse():
    assert DummyGate().inverse() == DummyGate(half_turns=-1)
    assert DummyGate(half_turns=0.25).inverse() == DummyGate(half_turns=-0.25)


def test_partial_reflection_as_self_inverse():
    ex = cirq.Extensions()

    h0 = DummyGate(half_turns=0)
    h1 = DummyGate(half_turns=1)
    ha = DummyGate(half_turns=cirq.Symbol('a'))
    assert ex.try_cast(cirq.ReversibleEffect, h0) is h0
    assert ex.try_cast(cirq.ReversibleEffect, h1) is h1
    assert ex.try_cast(cirq.ReversibleEffect, ha) is None


def test_partial_reflection_gate_trace_bound():
    assert DummyGate(half_turns=.001).trace_distance_bound() < 0.01
    assert DummyGate(half_turns=cirq.Symbol('a')).trace_distance_bound() >= 1


def test_partial_reflection_gate_with_parameters_resolved_by():
    gate = DummyGate(half_turns=Symbol('a'))
    resolver = ParamResolver({'a': 0.1})
    resolved_gate = gate.with_parameters_resolved_by(resolver)
    assert resolved_gate.half_turns == 0.1


def test_partial_reflection_gate_matrix():
    np.testing.assert_allclose(DummyGate(half_turns=1).matrix(),
                               np.diag([1, -1]),
                               atol=1e-8)

    np.testing.assert_allclose(DummyGate(half_turns=0.5).matrix(),
                               np.diag([1, 1j]),
                               atol=1e-8)

    np.testing.assert_allclose(DummyGate(half_turns=-0.5).matrix(),
                               np.diag([1, -1j]),
                               atol=1e-8)
