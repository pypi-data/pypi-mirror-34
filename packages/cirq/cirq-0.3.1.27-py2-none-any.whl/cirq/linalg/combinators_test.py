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

from cirq.linalg import combinators


def test_kron_multiplies_sizes():
    assert np.allclose(combinators.kron(), np.eye(1))
    assert np.allclose(combinators.kron(np.eye(1)), np.eye(1))
    assert np.allclose(combinators.kron(np.eye(2)), np.eye(2))
    assert np.allclose(combinators.kron(np.eye(1), np.eye(1)), np.eye(1))
    assert np.allclose(combinators.kron(np.eye(1), np.eye(2)), np.eye(2))
    assert np.allclose(combinators.kron(np.eye(2), np.eye(3)), np.eye(6))
    assert np.allclose(combinators.kron(np.eye(2), np.eye(3), np.eye(4)),
                       np.eye(24))


def test_kron_spreads_values():
    u = np.array([[2, 3], [5, 7]])

    assert np.allclose(
        combinators.kron(np.eye(2), u),
        np.array([[2, 3, 0, 0], [5, 7, 0, 0], [0, 0, 2, 3], [0, 0, 5, 7]]))

    assert np.allclose(
        combinators.kron(u, np.eye(2)),
        np.array([[2, 0, 3, 0], [0, 2, 0, 3], [5, 0, 7, 0], [0, 5, 0, 7]]))

    assert np.allclose(
        combinators.kron(u, u),
        np.array([[4, 6, 6, 9], [10, 14, 15, 21], [10, 15, 14, 21],
                [25, 35, 35, 49]]))


def test_acts_like_kron_multiplies_sizes():
    assert np.allclose(combinators.kron_with_controls(), np.eye(1))
    assert np.allclose(
        combinators.kron_with_controls(np.eye(2), np.eye(3), np.eye(4)),
        np.eye(24))

    u = np.array([[2, 3], [5, 7]])
    assert np.allclose(
        combinators.kron_with_controls(u, u),
        np.array([[4, 6, 6, 9], [10, 14, 15, 21], [10, 15, 14, 21],
                [25, 35, 35, 49]]))


def test_supports_controls():
    u = np.array([[2, 3], [5, 7]])
    assert np.allclose(
        combinators.kron_with_controls(combinators.CONTROL_TAG),
        np.array([[1, 0], [0, 1]]))
    assert np.allclose(
        combinators.kron_with_controls(combinators.CONTROL_TAG, u),
        np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 2, 3], [0, 0, 5, 7]]))
    assert np.allclose(
        combinators.kron_with_controls(u, combinators.CONTROL_TAG),
        np.array([[1, 0, 0, 0], [0, 2, 0, 3], [0, 0, 1, 0], [0, 5, 0, 7]]))


def test_block_diag():
    assert np.allclose(
        combinators.block_diag(),
        np.zeros((0, 0)))

    assert np.allclose(
        combinators.block_diag(
            np.array([[1, 2],
                    [3, 4]])),
        np.array([[1, 2],
                [3, 4]]))

    assert np.allclose(
        combinators.block_diag(
            np.array([[1, 2],
                    [3, 4]]),
            np.array([[4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])),
        np.array([[1, 2, 0, 0, 0],
                [3, 4, 0, 0, 0],
                [0, 0, 4, 5, 6],
                [0, 0, 7, 8, 9],
                [0, 0, 10, 11, 12]]))


def test_block_diag_dtype():
    assert combinators.block_diag().dtype == np.complex128

    assert (combinators.block_diag(np.array([[1]], dtype=np.int8)).dtype ==
            np.int8)

    assert combinators.block_diag(
            np.array([[1]], dtype=np.float32),
            np.array([[2]], dtype=np.float32)).dtype == np.float32

    assert combinators.block_diag(
            np.array([[1]], dtype=np.float64),
            np.array([[2]], dtype=np.float64)).dtype == np.float64

    assert combinators.block_diag(
            np.array([[1]], dtype=np.float32),
            np.array([[2]], dtype=np.float64)).dtype == np.float64

    assert combinators.block_diag(
            np.array([[1]], dtype=np.float32),
            np.array([[2]], dtype=np.complex64)).dtype == np.complex64

    assert combinators.block_diag(
            np.array([[1]], dtype=np.int),
            np.array([[2]], dtype=np.complex128)).dtype == np.complex128
