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

from cirq import circuits
from cirq import ops
from cirq.contrib.jobs import DepolarizerChannel
from cirq.contrib.jobs import Job
from cirq.google import xmon_gates
from cirq.study.sweeps import Points
from cirq.value import Symbol


def test_depolarizer_no_errors():
    q1 = ops.QubitId()
    q2 = ops.QubitId()
    cnot = Job(circuits.Circuit([
        circuits.Moment([ops.CNOT(q1, q2)]),
        ]))
    noerrors = DepolarizerChannel(probability=0.0)

    assert noerrors.transform_job(cnot) == cnot


def test_depolarizer_all_errors():
    q1 = ops.QubitId()
    q2 = ops.QubitId()
    cnot = Job(circuits.Circuit([
        circuits.Moment([ops.CNOT(q1, q2)]),
        ]))
    allerrors = DepolarizerChannel(probability=1.0)
    p0 = Symbol(DepolarizerChannel._parameter_name + '0')
    p1 = Symbol(DepolarizerChannel._parameter_name + '1')

    error_sweep = Points(p0.name, [1.0]) + Points(p1.name, [1.0])

    cnot_then_z = Job(
        circuits.Circuit([
            circuits.Moment([ops.CNOT(q1, q2)]),
            circuits.Moment([xmon_gates.ExpZGate(half_turns=p0).on(q1),
                             xmon_gates.ExpZGate(half_turns=p1).on(q2)])
        ]),
        cnot.sweep * error_sweep)

    assert allerrors.transform_job(cnot) == cnot_then_z


def test_depolarizer_different_gate():
    q1 = ops.QubitId()
    q2 = ops.QubitId()
    cnot = Job(circuits.Circuit([
        circuits.Moment([ops.CNOT(q1, q2)]),
        ]))
    allerrors = DepolarizerChannel(probability=1.0, depolarizing_gates=
                                   [xmon_gates.ExpZGate(),
                                    xmon_gates.ExpWGate()])
    p0 = Symbol(DepolarizerChannel._parameter_name + '0')
    p1 = Symbol(DepolarizerChannel._parameter_name + '1')
    p2 = Symbol(DepolarizerChannel._parameter_name + '2')
    p3 = Symbol(DepolarizerChannel._parameter_name + '3')

    error_sweep = (Points(p0.name, [1.0]) + Points(p1.name, [1.0])
                   + Points(p2.name, [1.0]) + Points(p3.name, [1.0]))

    cnot_then_z = Job(
        circuits.Circuit([
            circuits.Moment([ops.CNOT(q1, q2)]),
            circuits.Moment([xmon_gates.ExpZGate(half_turns=p0).on(q1),
                             xmon_gates.ExpZGate(half_turns=p1).on(q2)]),
            circuits.Moment([xmon_gates.ExpWGate(half_turns=p2).on(q1),
                             xmon_gates.ExpWGate(half_turns=p3).on(q2)])
        ]),
        cnot.sweep * error_sweep)

    assert allerrors.transform_job(cnot) == cnot_then_z


def test_depolarizer_multiple_realizations():
    q1 = ops.QubitId()
    q2 = ops.QubitId()
    cnot = Job(circuits.Circuit([
        circuits.Moment([ops.CNOT(q1, q2)]),
        ]))
    allerrors3 = DepolarizerChannel(probability=1.0, realizations=3)
    p0 = Symbol(DepolarizerChannel._parameter_name + '0')
    p1 = Symbol(DepolarizerChannel._parameter_name + '1')

    error_sweep = (Points(p0.name, [1.0, 1.0, 1.0]) +
                   Points(p1.name, [1.0, 1.0, 1.0]))

    cnot_then_z3 = Job(
        circuits.Circuit([
            circuits.Moment([ops.CNOT(q1, q2)]),
            circuits.Moment([xmon_gates.ExpZGate(half_turns=p0).on(q1),
                             xmon_gates.ExpZGate(half_turns=p1).on(q2)])
        ]),
        cnot.sweep * error_sweep)
    assert allerrors3.transform_job(cnot) == cnot_then_z3


def test_depolarizer_parameterized_gates():
    q1 = ops.QubitId()
    q2 = ops.QubitId()
    cnot_param = Symbol('cnot_turns')
    cnot_gate = xmon_gates.Exp11Gate(half_turns=cnot_param).on(q1, q2)

    job_sweep = Points('cnot_turns', [0.5])

    cnot = Job(circuits.Circuit([circuits.Moment([cnot_gate])]), job_sweep)
    allerrors = DepolarizerChannel(probability=1.0)
    p0 = Symbol(DepolarizerChannel._parameter_name + '0')
    p1 = Symbol(DepolarizerChannel._parameter_name + '1')

    error_sweep = Points(p0.name, [1.0]) + Points(p1.name, [1.0])
    cnot_then_z = Job(
        circuits.Circuit([
            circuits.Moment([cnot_gate]),
            circuits.Moment([xmon_gates.ExpZGate(half_turns=p0).on(q1),
                             xmon_gates.ExpZGate(half_turns=p1).on(q2)])
        ]),
        job_sweep * error_sweep)
    assert allerrors.transform_job(cnot) == cnot_then_z
