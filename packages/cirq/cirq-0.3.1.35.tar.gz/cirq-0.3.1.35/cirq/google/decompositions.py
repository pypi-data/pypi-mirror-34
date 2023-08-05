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

"""Utility methods related to optimizing quantum circuits."""

import cmath
import math
from typing import List, Tuple, Optional, cast

import numpy as np

from cirq import linalg
from cirq import ops
from cirq.google.xmon_gates import ExpWGate


def is_negligible_turn(turns: float, tolerance: float) -> bool:
    return abs(_signed_mod_1(turns)) <= tolerance


def _signed_mod_1(x: float) -> float:
    return (x + 0.5) % 1 - 0.5


def _deconstruct_single_qubit_matrix_into_gate_turns(
        mat: np.ndarray) -> Tuple[float, float, float]:
    """Breaks down a 2x2 unitary into gate parameters.

    Args:
        mat: The 2x2 unitary matrix to break down.

    Returns:
       A tuple containing the amount to rotate around an XY axis, the phase of
       that axis, and the amount to phase around Z. All results will be in
       fractions of a whole turn, with values canonicalized into the range
       [-0.5, 0.5).
    """
    pre_phase, rotation, post_phase = (
        linalg.deconstruct_single_qubit_matrix_into_angles(mat))

    # Figure out parameters of the actual gates we will do.
    tau = 2 * np.pi
    xy_turn = rotation / tau
    xy_phase_turn = 0.25 - pre_phase / tau
    total_z_turn = (post_phase + pre_phase) / tau

    # Normalize turns into the range [-0.5, 0.5).
    return (_signed_mod_1(xy_turn), _signed_mod_1(xy_phase_turn),
            _signed_mod_1(total_z_turn))


def _easy_direction_partial_cz(q0: ops.QubitId, q1: ops.QubitId, t: float):
    """The actual hardware can only do CZs that phase counter-clockwise.

    This method replaces clockwise phase(t) to counter-clockwise.

    Args:
      q0: The first qubit being operated on.
      q1: The other qubit being operated on.
      t: The parameter to describe partial-CZ(CZ^t).

    Yields:
      Yields an equivalent circuit for CZ^t with counter-clock phased CZs.
    """
    if t >= 0:
        yield ops.CZ(q0, q1)**t
        return
    yield ops.Z(q0)**t
    yield ops.X(q1)
    yield ops.CZ(q0, q1)**(-t)
    yield ops.X(q1)


def single_qubit_matrix_to_native_gates(
        mat: np.ndarray, tolerance: float = 0
) -> List[ops.SingleQubitGate]:
    """Implements a single-qubit operation with few native gates.

    Args:
        mat: The 2x2 unitary matrix of the operation to implement.
        tolerance: A limit on the amount of error introduced by the
            construction.

    Returns:
        A list of gates that, when applied in order, perform the desired
            operation.
    """

    xy_turn, xy_phase_turn, total_z_turn = (
        _deconstruct_single_qubit_matrix_into_gate_turns(mat))

    # Build the intended operation out of non-negligible XY and Z rotations.
    result = [
        ExpWGate(half_turns=2*xy_turn, axis_half_turns=2*xy_phase_turn),
        ops.RotZGate(half_turns=2 * total_z_turn)
    ]
    result = [
        g for g in result
        if cast(ops.BoundedEffect, g).trace_distance_bound() > tolerance
    ]

    # Special case: XY half-turns can absorb Z rotations.
    if len(result) == 2 and abs(xy_turn) >= 0.5 - tolerance:
        return [
            ExpWGate(axis_half_turns=2*xy_phase_turn + total_z_turn)
        ]

    return result


def single_qubit_op_to_framed_phase_form(
        mat: np.ndarray) -> Tuple[np.ndarray, complex, complex]:
    """Decomposes a 2x2 unitary M into U^-1 * diag(1, r) * U * diag(g, g).

    U translates the rotation axis of M to the Z axis.
    g fixes a global phase factor difference caused by the translation.
    r's phase is the amount of rotation around M's rotation axis.

    This decomposition can be used to decompose controlled single-qubit
    rotations into controlled-Z operations bordered by single-qubit operations.

    Args:
      mat:  The qubit operation as a 2x2 unitary matrix.

    Returns:
        A 2x2 unitary U, the complex relative phase factor r, and the complex
        global phase factor g. Applying M is equivalent (up to global phase) to
        applying U, rotating around the Z axis to apply r, then un-applying U.
        When M is controlled, the control must be rotated around the Z axis to
        apply g.
    """
    vals, vecs = np.linalg.eig(mat)
    u = np.conj(vecs).T
    r = vals[1] / vals[0]
    g = vals[0]
    return u, r, g


def controlled_op_to_native_gates(
        control: ops.QubitId,
        target: ops.QubitId,
        operation: np.ndarray,
        tolerance: float = 0.0) -> List[ops.Operation]:
    """Decomposes a controlled single-qubit operation into Z/XY/CZ gates.

    Args:
        control: The control qubit.
        target: The qubit to apply an operation to, when the control is on.
        operation: The single-qubit operation being controlled.
        tolerance: A limit on the amount of error introduced by the
            construction.

    Returns:
        A list of Operations that apply the controlled operation.
    """
    u, z_phase, global_phase = single_qubit_op_to_framed_phase_form(operation)
    if abs(z_phase - 1) <= tolerance:
        return []

    u_gates = single_qubit_matrix_to_native_gates(u, tolerance)
    if u_gates and isinstance(u_gates[-1], ops.RotZGate):
        # Don't keep border operations that commute with CZ.
        del u_gates[-1]

    ops_before = [gate(target) for gate in u_gates]
    ops_after = ops.inverse(ops_before)
    effect = ops.CZ(control, target) ** (cmath.phase(z_phase) / math.pi)
    kickback = ops.Z(control) ** (cmath.phase(global_phase) / math.pi)

    return list(ops.flatten_op_tree((
        ops_before,
        effect,
        kickback if abs(global_phase - 1) > tolerance else [],
        ops_after)))


def _xx_interaction_via_full_czs(q0: ops.QubitId,
                                 q1: ops.QubitId,
                                 x: float):
    a = x * -2 / np.pi
    yield ops.H(q1)
    yield ops.CZ(q0, q1)
    yield ops.X(q0)**a
    yield ops.CZ(q0, q1)
    yield ops.H(q1)


def _xx_yy_interaction_via_full_czs(q0: ops.QubitId,
                                    q1: ops.QubitId,
                                    x: float,
                                    y: float):
    a = x * -2 / np.pi
    b = y * -2 / np.pi
    yield ops.X(q0)**0.5
    yield ops.H(q1)
    yield ops.CZ(q0, q1)
    yield ops.H(q1)
    yield ops.X(q0)**a
    yield ops.Y(q1)**b
    yield ops.H(q1)
    yield ops.CZ(q0, q1)
    yield ops.H(q1)
    yield ops.X(q0)**-0.5


def _xx_yy_zz_interaction_via_full_czs(q0: ops.QubitId,
                                       q1: ops.QubitId,
                                       x: float,
                                       y: float,
                                       z: float):
    a = x * -2 / np.pi + 0.5
    b = y * -2 / np.pi + 0.5
    c = z * -2 / np.pi + 0.5
    yield ops.X(q0)**0.5
    yield ops.H(q1)
    yield ops.CZ(q0, q1)
    yield ops.H(q1)
    yield ops.X(q0)**a
    yield ops.Y(q1)**b
    yield ops.H.on(q0)
    yield ops.CZ(q1, q0)
    yield ops.H(q0)
    yield ops.X(q1)**-0.5
    yield ops.Z(q1)**c
    yield ops.H(q1)
    yield ops.CZ(q0, q1)
    yield ops.H(q1)


def two_qubit_matrix_to_native_gates(q0: ops.QubitId,
                                     q1: ops.QubitId,
                                     mat: np.ndarray,
                                     allow_partial_czs: bool,
                                     tolerance: float = 1e-8
                                     ) -> List[ops.Operation]:
    """Decomposes a two-qubit operation into Z/XY/CZ gates.

    Args:
        q0: The first qubit being operated on.
        q1: The other qubit being operated on.
        mat: Defines the operation to apply to the pair of qubits.
        allow_partial_czs: Enables the use of Partial-CZ gates.
        tolerance: A limit on the amount of error introduced by the
            construction.

    Returns:
        A list of operations implementing the matrix.
    """
    _, (a0, a1), (x, y, z), (b0, b1) = linalg.kak_decomposition(
        mat,
        linalg.Tolerance(atol=tolerance))
    return _kak_decomposition_to_native_gates(q0, q1,
                                              a0, a1, x, y, z, b0, b1,
                                              allow_partial_czs, tolerance)


def _kak_decomposition_to_native_gates(q0: ops.QubitId,
                                       q1: ops.QubitId,
                                       a0: np.ndarray,
                                       a1: np.ndarray,
                                       x: float,
                                       y: float,
                                       z: float,
                                       b0: np.ndarray,
                                       b1: np.ndarray,
                                       allow_partial_czs: bool,
                                       tolerance: float = 1e-8
                                       ) -> List[ops.Operation]:
    """Assumes that the decomposition is canonical."""
    pre = [_do_single_on(b0, q0, tolerance), _do_single_on(b1, q1, tolerance)]
    post = [_do_single_on(a0, q0, tolerance), _do_single_on(a1, q1, tolerance)]

    return list(ops.flatten_op_tree([
        pre,
        _non_local_part(q0, q1, x, y, z, allow_partial_czs, tolerance),
        post,
    ]))


def _is_trivial_angle(rad: float, tolerance: float) -> bool:
    """Tests if a circuit for an operator exp(i*rad*XX) (or YY, or ZZ) can
    be performed with a whole CZ.

    Args:
        rad: The angle in radians, assumed to be in the range [-pi/4, pi/4]
    """
    return abs(rad) < tolerance or abs(abs(rad) - np.pi / 4) < tolerance


def _parity_interaction(q0: ops.QubitId,
                        q1: ops.QubitId,
                        rads: float,
                        tolerance: float,
                        gate: Optional[ops.ReversibleEffect] = None):
    """Yields a ZZ interaction framed by the given operation."""
    if abs(rads) < tolerance:
        return

    h = rads * -2 / np.pi
    if gate is not None:
        g = cast(ops.Gate, gate)
        yield g.on(q0), g.on(q1)

    # If rads is ±pi/4 radians within tolerance, single full-CZ suffices.
    if _is_trivial_angle(rads, tolerance):
        yield ops.CZ.on(q0, q1)
    else:
        yield _easy_direction_partial_cz(q0, q1, -2 * h)

    yield ops.Z(q0)**h
    yield ops.Z(q1)**h
    if gate is not None:
        g = cast(ops.Gate, gate.inverse())
        yield g.on(q0), g.on(q1)


def _do_single_on(u: np.ndarray, q: ops.QubitId, tolerance: float=1e-8):
    for gate in single_qubit_matrix_to_native_gates(u, tolerance):
        yield gate(q)


def _non_local_part(q0: ops.QubitId,
                    q1: ops.QubitId,
                    x: float,
                    y: float,
                    z: float,
                    allow_partial_czs: bool,
                    tolerance: float = 1e-8):
    """Yields non-local operation of KAK decomposition."""

    if (allow_partial_czs or
        all(_is_trivial_angle(e, tolerance) for e in [x, y, z])):
        return [
            _parity_interaction(q0, q1, x, tolerance,
                                cast(ops.ReversibleEffect, ops.Y**-0.5)),
            _parity_interaction(q0, q1, y, tolerance,
                                cast(ops.ReversibleEffect, ops.X**0.5)),
            _parity_interaction(q0, q1, z, tolerance)
        ]

    if abs(z) >= tolerance:
        return _xx_yy_zz_interaction_via_full_czs(q0, q1, x, y, z)

    if y >= tolerance:
        return _xx_yy_interaction_via_full_czs(q0, q1, x, y)

    return _xx_interaction_via_full_czs(q0, q1, x)
