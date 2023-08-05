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
import numpy as np
import pytest

import cirq
from cirq.google import Foxtail, programs
from cirq.schedules import moment_by_moment_schedule


def test_protobuf_round_trip():
    device = Foxtail
    circuit = cirq.Circuit.from_ops(
        [
            cirq.google.ExpWGate(half_turns=0.5).on(q)
            for q in device.qubits
        ],
        [
            cirq.google.Exp11Gate().on(q, q2)
            for q in [cirq.GridQubit(0, 0)]
            for q2 in device.neighbors_of(q)
        ]
    )
    s1 = moment_by_moment_schedule(device, circuit)

    protos = list(programs.schedule_to_proto(s1))
    s2 = programs.schedule_from_proto(device, protos)

    assert s2 == s1


def make_bytes(s):
    u"""Helper function to convert a string of digits into packed bytes.

    Ignores any characters other than 0 and 1, in particular whitespace. The
    bits are packed in little-endian order within each byte.
    """
    buf = []
    byte = 0
    idx = 0
    for c in s:
        if c == u'0':
            pass
        elif c == u'1':
            byte |= 1 << idx
        else:
            continue
        idx += 1
        if idx == 8:
            buf.append(byte)
            byte = 0
            idx = 0
    if idx:
        buf.append(byte)
    return bytearray(buf)


def test_pack_results():
    measurements = [
        (u'a',
         np.array([
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],])),
        (u'b',
         np.array([
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
            [0, 0],
            [0, 1],
            [1, 0],])),
    ]
    data = programs.pack_results(measurements)
    expected = make_bytes(u"""
        000 00
        001 01
        010 10
        011 11
        100 00
        101 01
        110 10

        000 00 -- padding
    """)
    assert data == expected


def test_pack_results_no_measurements():
    assert programs.pack_results([]) == ''


def test_pack_results_incompatible_shapes():
    def bools(*shape):
        return np.zeros(shape, dtype=bool)

    with pytest.raises(ValueError):
        programs.pack_results([(u'a', bools(10))])

    with pytest.raises(ValueError):
        programs.pack_results([(u'a', bools(7, 3)), (u'b', bools(8, 2))])


def test_unpack_results():
    data = make_bytes(u"""
        000 00
        001 01
        010 10
        011 11
        100 00
        101 01
        110 10
    """)
    assert len(data) == 5  # 35 data bits + 5 padding bits
    results = programs.unpack_results(data, 7, [(u'a', 3), (u'b', 2)])
    assert u'a' in results
    assert results[u'a'].shape == (7, 3)
    assert results[u'a'].dtype == bool
    np.testing.assert_array_equal(
        results[u'a'],
        [[0, 0, 0],
         [0, 0, 1],
         [0, 1, 0],
         [0, 1, 1],
         [1, 0, 0],
         [1, 0, 1],
         [1, 1, 0],])

    assert u'b' in results
    assert results[u'b'].shape == (7, 2)
    assert results[u'b'].dtype == bool
    np.testing.assert_array_equal(
        results[u'b'],
        [[0, 0],
         [0, 1],
         [1, 0],
         [1, 1],
         [0, 0],
         [0, 1],
         [1, 0],])
