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

from __future__ import with_statement
from __future__ import absolute_import
from typing import Union

import numpy as np
import pytest

import cirq


class CExpZinGate(cirq.EigenGate, cirq.TwoQubitGate):
    u"""Two-qubit gate for the following matrix:
        [1  0  0  0]
        [0  1  0  0]
        [0  0  i  0]
        [0  0  0 -i]
    """
    def __init__(self, quarter_turns):
        super(CExpZinGate, self).__init__(exponent=quarter_turns)

    @property
    def exponent(self):
        return self._exponent

    def _with_exponent(self, exponent):
        return CExpZinGate(exponent)

    def _eigen_components(self):
        return [
            (0, np.diag([1, 1, 0, 0])),
            (0.5, np.diag([0, 0, 1, 0])),
            (-0.5, np.diag([0, 0, 0, 1])),
        ]

    def _canonical_exponent_period(self):
        return 4


def test_init():
    assert CExpZinGate(1).exponent == 1
    assert CExpZinGate(0.5).exponent == 0.5
    assert CExpZinGate(4.5).exponent == 0.5
    assert CExpZinGate(1.5).exponent == 1.5
    assert CExpZinGate(3.5).exponent == -0.5
    assert CExpZinGate(cirq.Symbol(u'a')).exponent == cirq.Symbol(u'a')


def test_eq():
    eq = cirq.testing.EqualsTester()
    eq.make_equality_group(lambda: CExpZinGate(quarter_turns=0.1))
    eq.add_equality_group(CExpZinGate(0), CExpZinGate(4), CExpZinGate(-4))
    eq.add_equality_group(CExpZinGate(1.5), CExpZinGate(41.5))
    eq.add_equality_group(CExpZinGate(3.5), CExpZinGate(-0.5))
    eq.add_equality_group(CExpZinGate(2.5))
    eq.add_equality_group(CExpZinGate(2.25))
    eq.make_equality_group(lambda: cirq.Symbol(u'a'))
    eq.add_equality_group(cirq.Symbol(u'b'))


def test_pow():
    assert CExpZinGate(0.25)**2 == CExpZinGate(0.5)
    assert CExpZinGate(0.25)**-1 == CExpZinGate(-0.25)
    assert CExpZinGate(0.25)**0 == CExpZinGate(0)
    with pytest.raises(ValueError):
        _ = CExpZinGate(cirq.Symbol(u'a'))**1.5


def test_extrapolate_effect():
    assert CExpZinGate(0.25).extrapolate_effect(2) == CExpZinGate(0.5)
    assert CExpZinGate(0.25).extrapolate_effect(-1) == CExpZinGate(-0.25)
    assert CExpZinGate(0.25).extrapolate_effect(0) == CExpZinGate(0)
    assert CExpZinGate(0).extrapolate_effect(0) == CExpZinGate(0)
    with pytest.raises(ValueError):
        _ = CExpZinGate(cirq.Symbol(u'a')).extrapolate_effect(1.5)


def test_inverse():
    assert CExpZinGate(0.25).inverse() == CExpZinGate(-0.25)
    with pytest.raises(ValueError):
        _ = CExpZinGate(cirq.Symbol(u'a')).inverse()


def test_trace_distance_bound():
    assert CExpZinGate(0.001).trace_distance_bound() < 0.01
    assert CExpZinGate(cirq.Symbol(u'a')).trace_distance_bound() >= 1


def test_try_cast_to():
    ext = cirq.Extensions()

    h = CExpZinGate(2)
    assert h.try_cast_to(cirq.ExtrapolatableEffect, ext) is h
    assert h.try_cast_to(cirq.ReversibleEffect, ext) is h
    assert h.try_cast_to(cirq.KnownMatrix, ext) is h
    assert h.try_cast_to(cirq.SingleQubitGate, ext) is None

    p = CExpZinGate(0.1)
    assert p.try_cast_to(cirq.ExtrapolatableEffect, ext) is p
    assert p.try_cast_to(cirq.ReversibleEffect, ext) is p
    assert p.try_cast_to(cirq.KnownMatrix, ext) is p
    assert p.try_cast_to(cirq.SingleQubitGate, ext) is None

    s = CExpZinGate(cirq.Symbol(u'a'))
    assert s.try_cast_to(cirq.ExtrapolatableEffect, ext) is None
    assert s.try_cast_to(cirq.ReversibleEffect, ext) is None
    assert s.try_cast_to(cirq.KnownMatrix, ext) is None
    assert s.try_cast_to(cirq.SingleQubitGate, ext) is None


def test_matrix():
    np.testing.assert_allclose(
        CExpZinGate(1).matrix(),
        np.diag([1, 1, 1j, -1j]),
        atol=1e-8)

    np.testing.assert_allclose(
        CExpZinGate(2).matrix(),
        np.diag([1, 1, -1, -1]),
        atol=1e-8)

    np.testing.assert_allclose(
        CExpZinGate(3).matrix(),
        np.diag([1, 1, -1j, 1j]),
        atol=1e-8)

    np.testing.assert_allclose(
        CExpZinGate(4).matrix(),
        np.diag([1, 1, 1, 1]),
        atol=1e-8)

    np.testing.assert_allclose(
        CExpZinGate(0.00001).matrix(),
        CExpZinGate(3.99999).matrix(),
        atol=1e-4)

    assert not np.allclose(
        CExpZinGate(0.00001).matrix(),
        CExpZinGate(1.99999).matrix(),
        atol=1e-4)

    with pytest.raises(ValueError):
        _ = CExpZinGate(cirq.Symbol(u'a')).matrix()


def test_matrix_is_exact_for_quarter_turn():
    print CExpZinGate(1).matrix()
    np.testing.assert_equal(
        CExpZinGate(1).matrix(),
        np.diag([1, 1, 1j, -1j]))


def test_is_parameterized():
    assert not CExpZinGate(0).is_parameterized()
    assert not CExpZinGate(1).is_parameterized()
    assert not CExpZinGate(3).is_parameterized()
    assert CExpZinGate(cirq.Symbol(u'a')).is_parameterized()


def test_with_parameters_resolved_by():
    assert CExpZinGate(cirq.Symbol(u'a')).with_parameters_resolved_by(
        cirq.ParamResolver({u'a': 0.5})) == CExpZinGate(0.5)

    assert CExpZinGate(0.25).with_parameters_resolved_by(
        cirq.ParamResolver({})) == CExpZinGate(0.25)
