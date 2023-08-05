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

u"""Marker classes for indicating which additional features gates support.

For example: some gates are reversible, some have known matrices, etc.
"""

from __future__ import absolute_import
from typing import Any, Dict, Optional, Sequence, Tuple, Iterable, TypeVar

import string
import numpy as np

from cirq import abc
from cirq.ops import op_tree
from cirq.ops import raw_types
from cirq.study import ParamResolver


class InterchangeableQubitsGate(object):
    __metaclass__ = abc.ABCMeta
    u"""Indicates operations should be equal under some qubit permutations."""

    def qubit_index_to_equivalence_group_key(self, index):
        u"""Returns a key that differs between non-interchangeable qubits."""
        return 0


class ReversibleEffect(object):
    __metaclass__ = abc.ABCMeta
    u"""A gate whose effect can be undone in a known way."""

    @abc.abstractmethod
    def inverse(self):
        u"""Returns a gate with an exactly opposite effect."""


TSelf_ExtrapolatableEffect = TypeVar(u'TSelf_ExtrapolatableEffect',
                                     bound=u'ExtrapolatableEffect')


class ExtrapolatableEffect(ReversibleEffect):
    __metaclass__ = abc.ABCMeta
    u"""A gate whose effect can be continuously scaled up/down/negated."""

    @abc.abstractmethod
    def extrapolate_effect(self, factor
                           ):
        u"""Augments, diminishes, or reverses the effect of the receiving gate.

        Args:
            factor: The amount to scale the gate's effect by.

        Returns:
            A gate equivalent to applying the receiving gate 'factor' times.
        """

    def __pow__(self, power
                ):
        u"""Extrapolates the effect of the gate.

        Note that there are cases where (G**a)**b != G**(a*b). For example,
        start with a 90 degree rotation then cube it then raise it to a
        non-integer power such as 3/2. Assuming that rotations are always
        normalized into the range (-180, 180], note that:

            ((rot 90)**3)**1.5 = (rot 270)**1.5 = (rot -90)**1.5 = rot -135

        but

            (rot 90)**(3*1.5) = (rot 90)**4.5 = rot 405 = rot 35

        Because normalization discards the winding number.

        Args:
          power: The extrapolation factor.

        Returns:
          A gate with the extrapolated effect.
        """
        return self.extrapolate_effect(power)

    def inverse(self):
        return self.extrapolate_effect(-1)


class CompositeOperation(object):
    __metaclass__ = abc.ABCMeta
    u"""An operation with a known decomposition into simpler operations."""

    @abc.abstractmethod
    def default_decompose(self):
        u"""Yields simpler operations for performing the receiving operation."""


class CompositeGate(object):
    __metaclass__ = abc.ABCMeta
    u"""A gate with a known decomposition into simpler gates."""

    @abc.abstractmethod
    def default_decompose(
            self, qubits):
        u"""Yields operations for performing this gate on the given qubits.

        Args:
            qubits: The qubits the gate should be applied to.
        """


class KnownMatrix(object):
    __metaclass__ = abc.ABCMeta
    u"""An effect that can be described by a matrix."""

    @abc.abstractmethod
    def matrix(self):
        u"""The unitary matrix of the gate/operation.

        The matrix order is implicit for both gates and operations. For a gate,
        the matrix must be in order with respect to the list of qubits that the
        gate is applied to. For an operation, the order must be with respect to
        its qubits attribute. The qubit-to-amplitude order mapping matches the
        ordering of numpy.kron(A, B), where A is a qubit earlier in the list
        than the qubit B.

        For example, when applying a CNOT gate the control qubit goes first and
        so the CNOT gate's matrix is:

            1 _ _ _
            _ 1 _ _
            _ _ _ 1
            _ _ 1 _
        """


class TextDiagramInfoArgs(object):
    u"""
    Attributes:
        known_qubits: The qubits the gate is being applied to. None means this
            information is not known by the caller.
        known_qubit_count: The number of qubits the gate is being applied to
            None means this information is not known by the caller.
        use_unicode_characters: If true, the wire symbols are permitted to
            include unicode characters (as long as they work well in fixed
            width fonts). If false, use only ascii characters. ASCII is
            preferred in cases where UTF8 support is done poorly, or where
            the fixed-width font being used to show the diagrams does not
            properly handle unicode characters.
        precision: The number of digits after the decimal to show for numbers in
            the text diagram. None means use full precision.
    """

    UNINFORMED_DEFAULT = None  # type: TextDiagramInfoArgs

    def __init__(self,
                 known_qubits,
                 known_qubit_count,
                 use_unicode_characters,
                 precision):
        self.known_qubits = known_qubits
        self.known_qubit_count = known_qubit_count
        self.use_unicode_characters = use_unicode_characters
        self.precision = precision


TextDiagramInfoArgs.UNINFORMED_DEFAULT = TextDiagramInfoArgs(
    known_qubits=None,
    known_qubit_count=None,
    use_unicode_characters=True,
    precision=3)


class TextDiagramInfo(object):
    def __init__(self,
                 wire_symbols,
                 exponent = 1):
        u"""
        Args:
            wire_symbols: The symbols that should be shown on the qubits
                affected by this operation. Must match the number of qubits that
                the operation is applied to.
            exponent: An optional convenience value that will be appended onto
                an operation's final gate symbol with a caret in front
                (unless it's equal to 1). For example, the square root of X gate
                has a text diagram exponent of 0.5 and symbol of 'X' so it is
                drawn as 'X^0.5'.
        """
        self.wire_symbols = wire_symbols
        self.exponent = exponent

    def _eq_tuple(self):
        return TextDiagramInfo, self.wire_symbols, self.exponent

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._eq_tuple() == other._eq_tuple()

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._eq_tuple())

    def __repr__(self):
        return u'TextDiagramInfo(wire_symbols={!r}, exponent={!r})'.format(
            self.wire_symbols, self.exponent)


class TextDiagrammable(object):
    __metaclass__ = abc.ABCMeta
    u"""A thing which can be printed in a text diagram."""

    @abc.abstractmethod
    def text_diagram_info(self, args):
        u"""Describes how to draw something in a text diagram.

        Args:
            args: A TextDiagramInfoArgs instance encapsulating various pieces of
                information (e.g. how many qubits are we being applied to) as
                well as user options (e.g. whether to avoid unicode characters).

        Returns:
             A TextDiagramInfo instance describing what to print.
        """


TSelf_PhaseableEffect = TypeVar(u'TSelf_PhaseableEffect',
                                bound=u'PhaseableEffect')


class PhaseableEffect(object):
    __metaclass__ = abc.ABCMeta
    u"""An effect that can be phased around the Z axis of target qubits."""

    @abc.abstractmethod
    def phase_by(self,
                 phase_turns,
                 qubit_index):
        u"""Returns a phased version of the effect.

        For example, an X gate phased by 90 degrees would be a Y gate.

        Args:
            phase_turns: The amount to phase the gate, in fractions of a whole
                turn.
            qubit_index: The index of the target qubit the phasing applies to.

        Returns:
            The phased gate or operation.
        """


class BoundedEffect(object):
    __metaclass__ = abc.ABCMeta
    u"""An effect with known bounds on how easy it is to detect.

    Used when deciding whether or not an operation is negligible. For example,
    the trace distance between the states before and after a Z**0.00000001
    operation is very close to 0, so it would typically be considered
    negligible.
    """

    @abc.abstractmethod
    def trace_distance_bound(self):
        u"""A maximum on the trace distance between this effect's input/output.

        Generally this method is used when deciding whether to keep gates, so
        only the behavior near 0 is important. Approximations that overestimate
        the maximum trace distance are permitted. Even ones that exceed 1.
        Underestimates are not permitted.
        """


class SingleQubitGate(raw_types.Gate):
    __metaclass__ = abc.ABCMeta
    u"""A gate that must be applied to exactly one qubit."""

    def validate_args(self, qubits):
        if len(qubits) != 1:
            raise ValueError(
                u'Single-qubit gate applied to multiple qubits: {}({})'.
                format(self, qubits))

    def on_each(self, targets):
        u"""Returns a list of operations apply this gate to each of the targets.

        Args:
            targets: The qubits to apply this gate to.

        Returns:
            Operations applying this gate to the target qubits.
        """
        return [self.on(target) for target in targets]


class TwoQubitGate(raw_types.Gate):
    __metaclass__ = abc.ABCMeta
    u"""A gate that must be applied to exactly two qubits."""

    def validate_args(self, qubits):
        if len(qubits) != 2:
            raise ValueError(
                u'Two-qubit gate not applied to two qubits: {}({})'.
                format(self, qubits))


class ThreeQubitGate(raw_types.Gate):
    __metaclass__ = abc.ABCMeta
    u"""A gate that must be applied to exactly three qubits."""

    def validate_args(self, qubits):
        if len(qubits) != 3:
            raise ValueError(
                u'Three-qubit gate not applied to three qubits: {}({})'.
                format(self, qubits))


TSelf_ParameterizableEffect = TypeVar(u'TSelf_ParameterizableEffect',
                                      bound=u'ParameterizableEffect')


class ParameterizableEffect(object):
    __metaclass__ = abc.ABCMeta
    u"""An effect that can be parameterized by Symbols."""

    @abc.abstractmethod
    def is_parameterized(self):
        u"""Whether the effect is parameterized.

        Returns True if the gate has any unresolved Symbols and False otherwise.
        """

    @abc.abstractmethod
    def with_parameters_resolved_by(self,
                                    param_resolver
                                    ):
        u"""Resolve the parameters in the effect.

        Returns a gate or operation of the same type, but with all Symbols
        replaced with floats according to the given ParamResolver.
        """


class QasmOutputArgs(string.Formatter):
    u"""
    Attributes:
        precision: The number of digits after the decimal to show for numbers in
            the text diagram.
        version: The QASM version to output.  QasmConvertableGate/Operation may
            return different text depending on version.
        qubit_id_map: A dictionary mapping qubits to qreg QASM identifiers.
        meas_key_id_map: A dictionary mapping measurement keys to creg QASM
            identifiers.
    """
    def __init__(self,
                 precision = 10,
                 version = u'2.0',
                 qubit_id_map = None,
                 meas_key_id_map = None,
                 ):
        self.precision = precision
        self.version = version
        self.qubit_id_map = {} if qubit_id_map is None else qubit_id_map
        self.meas_key_id_map = ({} if meas_key_id_map is None
                                   else meas_key_id_map)

    def format_field(self, value, spec):
        u"""Method of string.Formatter that specifies the output of format()."""
        if isinstance(value, float):
            value = round(value, self.precision)
            if spec == u'half_turns':
                value = u'pi*{}'.format(value) if value != 0 else u'0'
                spec = u''
        elif isinstance(value, raw_types.QubitId):
            value = self.qubit_id_map[value]
        elif isinstance(value, unicode) and spec == u'meas':
            value = self.meas_key_id_map[value]
            spec = u''
        return super(QasmOutputArgs, self).format_field(value, spec)

    def validate_version(self, *supported_versions):
        if self.version not in supported_versions:
            raise ValueError(u'QASM version {} output is not supported.'.format(
                                self.version))


class QasmConvertableGate(object):
    __metaclass__ = abc.ABCMeta
    u"""A gate that knows its representation in QASM."""
    @abc.abstractmethod
    def known_qasm_output(self,
                          qubits,
                          args):
        u"""Returns lines of QASM output representing the gate on the given
        qubits or None if a simple conversion is not possible.
        """


class QasmConvertableOperation(object):
    __metaclass__ = abc.ABCMeta
    u"""An operation that knows its representation in QASM."""
    @abc.abstractmethod
    def known_qasm_output(self, args):
        u"""Returns lines of QASM output representing the operation or None if a
        simple conversion is not possible."""
