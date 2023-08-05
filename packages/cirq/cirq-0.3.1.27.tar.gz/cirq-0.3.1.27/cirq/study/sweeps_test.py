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
import pytest

from cirq.study.sweeps import Linspace, Points, Unit
from cirq.testing import EqualsTester
from cirq.value import Symbol


def test_product_duplicate_keys():
    with pytest.raises(ValueError):
        _ = Linspace(u'a', 0, 9, 10) * Linspace(u'a', 0, 10, 11)


def test_zip_duplicate_keys():
    with pytest.raises(ValueError):
        _ = Linspace(u'a', 0, 9, 10) * Linspace(u'a', 0, 10, 11)


def test_linspace():
    sweep = Linspace(u'a', 0.34, 9.16, 7)
    assert len(sweep) == 7
    params = list(sweep.param_tuples())
    assert len(params) == 7
    assert params[0] == ((u'a', 0.34),)
    assert params[-1] == ((u'a', 9.16),)


def test_linspace_one_point():
    sweep = Linspace(u'a', 0.34, 9.16, 1)
    assert len(sweep) == 1
    params = list(sweep.param_tuples())
    assert len(params) == 1
    assert params[0] == ((u'a', 0.34),)


def test_points():
    sweep = Points(u'a', [1, 2, 3, 4])
    assert len(sweep) == 4
    params = list(sweep)
    assert len(params) == 4


def test_zip():
    sweep = Points(u'a', [1, 2, 3]) + Points(u'b', [4, 5, 6, 7])
    assert len(sweep) == 3
    assert _values(sweep, u'a') == [1, 2, 3]
    assert _values(sweep, u'b') == [4, 5, 6]


def test_product():
    sweep = Points(u'a', [1, 2, 3]) * Points(u'b', [4, 5, 6, 7])
    assert len(sweep) == 12
    assert _values(sweep, u'a') == [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    assert _values(sweep, u'b') == [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7]


def _values(sweep, key):
    p = Symbol(key)
    return [resolver.value_of(p) for resolver in sweep]


def test_equality():
    et = EqualsTester()

    et.add_equality_group(Unit, Unit)

    # Simple sweeps with the same key are equal to themselves, but different
    # from each other even if they happen to contain the same points.
    et.make_equality_group(lambda: Linspace(u'a', 0, 10, 11))
    et.make_equality_group(lambda: Linspace(u'b', 0, 10, 11))
    et.make_equality_group(lambda: Points(u'a', range(11)))
    et.make_equality_group(lambda: Points(u'b', range(11)))

    # Product and Zip sweeps can also be equated.
    et.make_equality_group(
        lambda: Linspace(u'a', 0, 5, 6) * Linspace(u'b', 10, 15, 6))
    et.make_equality_group(
        lambda: Linspace(u'a', 0, 5, 6) + Linspace(u'b', 10, 15, 6))
    et.make_equality_group(
        lambda: Points(u'a', [1, 2]) *
                     (Linspace(u'b', 0, 5, 6) + Linspace(u'c', 10, 15, 6)))
