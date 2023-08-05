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

u"""An optimization pass that removes operations with tiny effects."""

from __future__ import absolute_import
from typing import TYPE_CHECKING

from cirq import ops, extension
from cirq.circuits import optimization_pass, circuit as _circuit

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from typing import List, Tuple


class DropNegligible(optimization_pass.OptimizationPass):
    u"""An optimization pass that removes operations with tiny effects."""

    def __init__(self,
                 tolerance = 1e-8,
                 extensions = None):
        self.tolerance = tolerance
        self.extensions = extensions or extension.Extensions()

    def optimize_circuit(self, circuit):
        deletions = []  # type: List[Tuple[int, ops.Operation]]
        for moment_index, moment in enumerate(circuit):
            for op in moment.operations:
                bounded = self.extensions.try_cast(ops.BoundedEffect, op)
                if (bounded is not None and
                        bounded.trace_distance_bound() <= self.tolerance):
                    deletions.append((moment_index, op))
        circuit.batch_remove(deletions)
