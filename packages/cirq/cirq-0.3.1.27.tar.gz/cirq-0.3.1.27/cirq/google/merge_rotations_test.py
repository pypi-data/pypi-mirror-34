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
import numpy as np

import cirq


def assert_optimizes(before, after, optimizer=None):
    if optimizer is None:
        optimizer = cirq.google.MergeRotations()
    optimizer.optimize_circuit(before)

    # Ignore differences that would be caught by follow-up optimizations.
    followup_optimizations = [
        cirq.DropNegligible(),
        cirq.DropEmptyMoments()
    ]
    for post in followup_optimizations:
        post.optimize_circuit(before)
        post.optimize_circuit(after)

    if before != after:
        # coverage: ignore
        print u"before:", before
        print u"after:", after
    assert before == after


def test_leaves_singleton():
    m = cirq.google.MergeRotations(0.000001)
    q = cirq.QubitId()
    c = cirq.Circuit([cirq.Moment([cirq.X(q)])])

    m.optimization_at(c, 0, c.operation_at(q, 0))

    assert c == cirq.Circuit([cirq.Moment([cirq.X(q)])])


def test_combines_sequence():
    m = cirq.google.MergeRotations(0.000001)
    q = cirq.QubitId()
    c = cirq.Circuit([
        cirq.Moment([cirq.X(q)**0.5]),
        cirq.Moment([cirq.Z(q)**0.5]),
        cirq.Moment([cirq.X(q)**-0.5]),
    ])

    assert (m.optimization_at(c, 0, c.operation_at(q, 0)) ==
            cirq.PointOptimizationSummary(clear_span=3,
                                          clear_qubits=[q],
                                          new_operations=cirq.Y(q)**0.5))


def test_removes_identity_sequence():
    q = cirq.QubitId()
    assert_optimizes(
        before=cirq.Circuit([
            cirq.Moment([cirq.Z(q)]),
            cirq.Moment([cirq.H(q)]),
            cirq.Moment([cirq.X(q)]),
            cirq.Moment([cirq.H(q)]),
        ]),
        after=cirq.Circuit())


def test_stopped_at_2qubit():
    m = cirq.google.MergeRotations(0.000001)
    q = cirq.QubitId()
    q2 = cirq.QubitId()
    c = cirq.Circuit([
        cirq.Moment([cirq.Z(q)]),
        cirq.Moment([cirq.H(q)]),
        cirq.Moment([cirq.X(q)]),
        cirq.Moment([cirq.H(q)]),
        cirq.Moment([cirq.CZ(q, q2)]),
        cirq.Moment([cirq.H(q)]),
    ])

    assert (m.optimization_at(c, 0, c.operation_at(q, 0)) ==
            cirq.PointOptimizationSummary(clear_span=4,
                                          clear_qubits=[q],
                                          new_operations=[]))


def test_ignores_2qubit_target():
    m = cirq.google.MergeRotations(0.000001)
    q = cirq.QubitId()
    q2 = cirq.QubitId()
    c = cirq.Circuit([
        cirq.Moment([cirq.CZ(q, q2)]),
    ])

    m.optimization_at(c, 0, c.operation_at(q, 0))

    assert c == cirq.Circuit([cirq.Moment([cirq.CZ(q, q2)])])


def test_extension():
    class DummyGate(cirq.Gate):
        pass

    ext = cirq.Extensions()
    ext.add_cast(cirq.KnownMatrix,
                 DummyGate,
                 lambda _: cirq.SingleQubitMatrixGate(
                     np.array([[0, 1], [1, 0]])))
    optimizer = cirq.google.MergeRotations(extensions=ext)

    q = cirq.QubitId()
    c = cirq.Circuit([
        cirq.Moment([DummyGate().on(q)]),
    ])
    assert_optimizes(
        before=c,
        after=cirq.Circuit([cirq.Moment([cirq.X(q)])]),
        optimizer=optimizer)
