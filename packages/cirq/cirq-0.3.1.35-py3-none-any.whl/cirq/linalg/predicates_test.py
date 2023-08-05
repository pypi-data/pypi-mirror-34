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

import cmath
import numpy as np

from cirq.linalg import predicates
from cirq.linalg.tolerance import Tolerance


def test_is_diagonal():
    assert predicates.is_diagonal(np.empty((0, 0)))
    assert predicates.is_diagonal(np.empty((1, 0)))
    assert predicates.is_diagonal(np.empty((0, 1)))

    assert predicates.is_diagonal(np.array([[1]]))
    assert predicates.is_diagonal(np.array([[-1]]))
    assert predicates.is_diagonal(np.array([[5]]))
    assert predicates.is_diagonal(np.array([[3j]]))

    assert predicates.is_diagonal(np.array([[1, 0]]))
    assert predicates.is_diagonal(np.array([[1], [0]]))
    assert not predicates.is_diagonal(np.array([[1, 1]]))
    assert not predicates.is_diagonal(np.array([[1], [1]]))

    assert predicates.is_diagonal(np.array([[5j, 0], [0, 2]]))
    assert predicates.is_diagonal(np.array([[1, 0], [0, 1]]))
    assert not predicates.is_diagonal(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_diagonal(np.array([[1, 1], [0, 1]]))
    assert not predicates.is_diagonal(np.array([[1, 1], [1, 1]]))
    assert not predicates.is_diagonal(np.array([[1, 0.1], [0.1, 1]]))

    assert predicates.is_diagonal(np.array([[1, 1e-11], [1e-10, 1]]))


def test_is_diagonal_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_diagonal(np.array([[1, 0], [-0.5, 1]]), tol)
    assert not predicates.is_diagonal(np.array([[1, 0], [-0.6, 1]]), tol)

    # Error isn't accumulated across entries.
    assert predicates.is_diagonal(np.array([[1, 0.5], [-0.5, 1]]), tol)
    assert not predicates.is_diagonal(np.array([[1, 0.5], [-0.6, 1]]), tol)


def test_is_hermitian():
    assert predicates.is_hermitian(np.empty((0, 0)))
    assert not predicates.is_hermitian(np.empty((1, 0)))
    assert not predicates.is_hermitian(np.empty((0, 1)))

    assert predicates.is_hermitian(np.array([[1]]))
    assert predicates.is_hermitian(np.array([[-1]]))
    assert predicates.is_hermitian(np.array([[5]]))
    assert not predicates.is_hermitian(np.array([[3j]]))

    assert not predicates.is_hermitian(np.array([[0, 0]]))
    assert not predicates.is_hermitian(np.array([[0], [0]]))

    assert not predicates.is_hermitian(np.array([[5j, 0], [0, 2]]))
    assert predicates.is_hermitian(np.array([[5, 0], [0, 2]]))
    assert predicates.is_hermitian(np.array([[1, 0], [0, 1]]))
    assert not predicates.is_hermitian(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_hermitian(np.array([[1, 1], [0, 1]]))
    assert predicates.is_hermitian(np.array([[1, 1], [1, 1]]))
    assert predicates.is_hermitian(np.array([[1, 1j], [-1j, 1]]))
    assert predicates.is_hermitian(np.array([[1, 1j], [-1j, 1]]) * np.sqrt(0.5))
    assert not predicates.is_hermitian(np.array([[1, 1j], [1j, 1]]))
    assert not predicates.is_hermitian(np.array([[1, 0.1], [-0.1, 1]]))

    assert predicates.is_hermitian(
        np.array([[1, 1j + 1e-11], [-1j, 1 + 1j * 1e-9]]))


def test_is_hermitian_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_hermitian(np.array([[1, 0], [-0.5, 1]]), tol)
    assert predicates.is_hermitian(np.array([[1, 0.25], [-0.25, 1]]), tol)
    assert not predicates.is_hermitian(np.array([[1, 0], [-0.6, 1]]), tol)
    assert not predicates.is_hermitian(np.array([[1, 0.25], [-0.35, 1]]), tol)

    # Error isn't accumulated across entries.
    assert predicates.is_hermitian(
        np.array([[1, 0.5, 0.5], [0, 1, 0], [0, 0, 1]]), tol)
    assert not predicates.is_hermitian(
        np.array([[1, 0.5, 0.6], [0, 1, 0], [0, 0, 1]]), tol)
    assert not predicates.is_hermitian(
        np.array([[1, 0, 0.6], [0, 1, 0], [0, 0, 1]]), tol)


def test_is_unitary():
    assert predicates.is_unitary(np.empty((0, 0)))
    assert not predicates.is_unitary(np.empty((1, 0)))
    assert not predicates.is_unitary(np.empty((0, 1)))

    assert predicates.is_unitary(np.array([[1]]))
    assert predicates.is_unitary(np.array([[-1]]))
    assert predicates.is_unitary(np.array([[1j]]))
    assert not predicates.is_unitary(np.array([[5]]))
    assert not predicates.is_unitary(np.array([[3j]]))

    assert not predicates.is_unitary(np.array([[1, 0]]))
    assert not predicates.is_unitary(np.array([[1], [0]]))

    assert not predicates.is_unitary(np.array([[1, 0], [0, -2]]))
    assert predicates.is_unitary(np.array([[1, 0], [0, -1]]))
    assert predicates.is_unitary(np.array([[1j, 0], [0, 1]]))
    assert not predicates.is_unitary(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_unitary(np.array([[1, 1], [0, 1]]))
    assert not predicates.is_unitary(np.array([[1, 1], [1, 1]]))
    assert not predicates.is_unitary(np.array([[1, -1], [1, 1]]))
    assert predicates.is_unitary(np.array([[1, -1], [1, 1]]) * np.sqrt(0.5))
    assert predicates.is_unitary(np.array([[1, 1j], [1j, 1]]) * np.sqrt(0.5))
    assert not predicates.is_unitary(
        np.array([[1, -1j], [1j, 1]]) * np.sqrt(0.5))

    assert predicates.is_unitary(
        np.array([[1, 1j + 1e-11], [1j, 1 + 1j * 1e-9]]) * np.sqrt(0.5))


def test_is_unitary_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_unitary(np.array([[1, 0], [-0.5, 1]]), tol)
    assert not predicates.is_unitary(np.array([[1, 0], [-0.6, 1]]), tol)

    # Error isn't accumulated across entries.
    assert predicates.is_unitary(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1.2]]), tol)
    assert not predicates.is_unitary(
        np.array([[1.2, 0, 0], [0, 1.3, 0], [0, 0, 1.2]]), tol)


def test_is_orthogonal():
    assert predicates.is_orthogonal(np.empty((0, 0)))
    assert not predicates.is_orthogonal(np.empty((1, 0)))
    assert not predicates.is_orthogonal(np.empty((0, 1)))

    assert predicates.is_orthogonal(np.array([[1]]))
    assert predicates.is_orthogonal(np.array([[-1]]))
    assert not predicates.is_orthogonal(np.array([[1j]]))
    assert not predicates.is_orthogonal(np.array([[5]]))
    assert not predicates.is_orthogonal(np.array([[3j]]))

    assert not predicates.is_orthogonal(np.array([[1, 0]]))
    assert not predicates.is_orthogonal(np.array([[1], [0]]))

    assert not predicates.is_orthogonal(np.array([[1, 0], [0, -2]]))
    assert predicates.is_orthogonal(np.array([[1, 0], [0, -1]]))
    assert not predicates.is_orthogonal(np.array([[1j, 0], [0, 1]]))
    assert not predicates.is_orthogonal(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_orthogonal(np.array([[1, 1], [0, 1]]))
    assert not predicates.is_orthogonal(np.array([[1, 1], [1, 1]]))
    assert not predicates.is_orthogonal(np.array([[1, -1], [1, 1]]))
    assert predicates.is_orthogonal\
        (np.array([[1, -1], [1, 1]]) * np.sqrt(0.5))
    assert not predicates.is_orthogonal(
        np.array([[1, 1j], [1j, 1]]) * np.sqrt(0.5))
    assert not predicates.is_orthogonal(
        np.array([[1, -1j], [1j, 1]]) * np.sqrt(0.5))

    assert predicates.is_orthogonal(np.array([[1, 1e-11], [0, 1 + 1e-11]]))


def test_is_orthogonal_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_orthogonal(np.array([[1, 0], [-0.5, 1]]), tol)
    assert not predicates.is_orthogonal(np.array([[1, 0], [-0.6, 1]]), tol)

    # Error isn't accumulated across entries.
    assert predicates.is_orthogonal(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1.2]]), tol)
    assert not predicates.is_orthogonal(
        np.array([[1.2, 0, 0], [0, 1.3, 0], [0, 0, 1.2]]), tol)


def test_is_special_orthogonal():
    assert predicates.is_special_orthogonal(np.empty((0, 0)))
    assert not predicates.is_special_orthogonal(np.empty((1, 0)))
    assert not predicates.is_special_orthogonal(np.empty((0, 1)))

    assert predicates.is_special_orthogonal(np.array([[1]]))
    assert not predicates.is_special_orthogonal(np.array([[-1]]))
    assert not predicates.is_special_orthogonal(np.array([[1j]]))
    assert not predicates.is_special_orthogonal(np.array([[5]]))
    assert not predicates.is_special_orthogonal(np.array([[3j]]))

    assert not predicates.is_special_orthogonal(np.array([[1, 0]]))
    assert not predicates.is_special_orthogonal(np.array([[1], [0]]))

    assert not predicates.is_special_orthogonal(np.array([[1, 0], [0, -2]]))
    assert not predicates.is_special_orthogonal(np.array([[1, 0], [0, -1]]))
    assert predicates.is_special_orthogonal(np.array([[-1, 0], [0, -1]]))
    assert not predicates.is_special_orthogonal(np.array([[1j, 0], [0, 1]]))
    assert not predicates.is_special_orthogonal(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_special_orthogonal(np.array([[1, 1], [0, 1]]))
    assert not predicates.is_special_orthogonal(np.array([[1, 1], [1, 1]]))
    assert not predicates.is_special_orthogonal(np.array([[1, -1], [1, 1]]))
    assert predicates.is_special_orthogonal(
        np.array([[1, -1], [1, 1]]) * np.sqrt(0.5))
    assert not predicates.is_special_orthogonal(
        np.array([[1, 1], [1, -1]]) * np.sqrt(0.5))
    assert not predicates.is_special_orthogonal(
        np.array([[1, 1j], [1j, 1]]) * np.sqrt(0.5))
    assert not predicates.is_special_orthogonal(
        np.array([[1, -1j], [1j, 1]]) * np.sqrt(0.5))

    assert predicates.is_special_orthogonal(
        np.array([[1, 1e-11], [0, 1 + 1e-11]]))


def test_is_special_orthogonal_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_special_orthogonal(
        np.array([[1, 0], [-0.5, 1]]), tol)
    assert not predicates.is_special_orthogonal(
        np.array([[1, 0], [-0.6, 1]]), tol)

    # Error isn't accumulated across entries, except for determinant factors.
    assert predicates.is_special_orthogonal(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1 / 1.2]]), tol)
    assert not predicates.is_special_orthogonal(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1.2]]), tol)
    assert not predicates.is_special_orthogonal(
        np.array([[1.2, 0, 0], [0, 1.3, 0], [0, 0, 1 / 1.2]]), tol)


def test_is_special_unitary():
    assert predicates.is_special_unitary(np.empty((0, 0)))
    assert not predicates.is_special_unitary(np.empty((1, 0)))
    assert not predicates.is_special_unitary(np.empty((0, 1)))

    assert predicates.is_special_unitary(np.array([[1]]))
    assert not predicates.is_special_unitary(np.array([[-1]]))
    assert not predicates.is_special_unitary(np.array([[5]]))
    assert not predicates.is_special_unitary(np.array([[3j]]))

    assert not predicates.is_special_unitary(np.array([[1, 0], [0, -2]]))
    assert not predicates.is_special_unitary(np.array([[1, 0], [0, -1]]))
    assert predicates.is_special_unitary(np.array([[-1, 0], [0, -1]]))
    assert not predicates.is_special_unitary(np.array([[1j, 0], [0, 1]]))
    assert predicates.is_special_unitary(np.array([[1j, 0], [0, -1j]]))
    assert not predicates.is_special_unitary(np.array([[1, 0], [1, 1]]))
    assert not predicates.is_special_unitary(np.array([[1, 1], [0, 1]]))
    assert not predicates.is_special_unitary(np.array([[1, 1], [1, 1]]))
    assert not predicates.is_special_unitary(np.array([[1, -1], [1, 1]]))
    assert predicates.is_special_unitary(
        np.array([[1, -1], [1, 1]]) * np.sqrt(0.5))
    assert predicates.is_special_unitary(
        np.array([[1, 1j], [1j, 1]]) * np.sqrt(0.5))
    assert not predicates.is_special_unitary(
        np.array([[1, -1j], [1j, 1]]) * np.sqrt(0.5))

    assert predicates.is_special_unitary(
        np.array([[1, 1j + 1e-11], [1j, 1 + 1j * 1e-9]]) * np.sqrt(0.5))


def test_is_special_unitary_tolerance():
    tol = Tolerance(atol=0.5)

    # Pays attention to specified tolerance.
    assert predicates.is_special_unitary(np.array([[1, 0], [-0.5, 1]]), tol)
    assert not predicates.is_special_unitary(np.array([[1, 0], [-0.6, 1]]), tol)
    assert predicates.is_special_unitary(
        np.array([[1, 0], [0, 1]]) * cmath.exp(1j * 0.1), tol)
    assert not predicates.is_special_unitary(
        np.array([[1, 0], [0, 1]]) * cmath.exp(1j * 0.3), tol)

    # Error isn't accumulated across entries, except for determinant factors.
    assert predicates.is_special_unitary(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1 / 1.2]]), tol)
    assert not predicates.is_special_unitary(
        np.array([[1.2, 0, 0], [0, 1.2, 0], [0, 0, 1.2]]), tol)
    assert not predicates.is_special_unitary(
        np.array([[1.2, 0, 0], [0, 1.3, 0], [0, 0, 1 / 1.2]]), tol)


def test_commutes():
    assert predicates.commutes(
        np.empty((0, 0)),
        np.empty((0, 0)))
    assert not predicates.commutes(
        np.empty((1, 0)),
        np.empty((0, 1)))
    assert not predicates.commutes(
        np.empty((0, 1)),
        np.empty((1, 0)))
    assert not predicates.commutes(
        np.empty((1, 0)),
        np.empty((1, 0)))
    assert not predicates.commutes(
        np.empty((0, 1)),
        np.empty((0, 1)))

    assert predicates.commutes(np.array([[1]]), np.array([[2]]))
    assert predicates.commutes(np.array([[1]]), np.array([[0]]))

    x = np.array([[0, 1], [1, 0]])
    y = np.array([[0, -1j], [1j, 0]])
    z = np.array([[1, 0], [0, -1]])
    xx = np.kron(x, x)
    zz = np.kron(z, z)

    assert predicates.commutes(x, x)
    assert predicates.commutes(y, y)
    assert predicates.commutes(z, z)
    assert not predicates.commutes(x, y)
    assert not predicates.commutes(x, z)
    assert not predicates.commutes(y, z)

    assert predicates.commutes(xx, zz)
    assert predicates.commutes(xx, np.diag([1, -1, -1, 1 + 1e-9]))


def test_commutes_tolerance():
    tol = Tolerance(atol=0.5)

    x = np.array([[0, 1], [1, 0]])
    z = np.array([[1, 0], [0, -1]])

    # Pays attention to specified tolerance.
    assert predicates.commutes(x, x + z * 0.1, tol)
    assert not predicates.commutes(x, x + z * 0.5, tol)


def test_allclose_up_to_global_phase():
    assert predicates.allclose_up_to_global_phase(
        np.array([1]),
        np.array([1j]))

    assert predicates.allclose_up_to_global_phase(
        np.array([[1]]),
        np.array([[1]]))
    assert predicates.allclose_up_to_global_phase(
        np.array([[1]]),
        np.array([[-1]]))

    assert predicates.allclose_up_to_global_phase(
        np.array([[0]]),
        np.array([[0]]))

    assert predicates.allclose_up_to_global_phase(
        np.array([[1, 2]]),
        np.array([[1j, 2j]]))

    assert predicates.allclose_up_to_global_phase(
        np.array([[1, 2.0000000001]]),
        np.array([[1j, 2j]]))

    assert not predicates.allclose_up_to_global_phase(
        np.array([[1]]),
        np.array([[1, 0]]))
    assert not predicates.allclose_up_to_global_phase(
        np.array([[1]]),
        np.array([[2]]))
    assert not predicates.allclose_up_to_global_phase(
        np.array([[1]]),
        np.array([[2]]))
