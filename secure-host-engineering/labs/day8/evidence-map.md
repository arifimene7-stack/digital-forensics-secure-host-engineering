# Evidence Map

## Investigation Objective

The objective is to determine whether the collected Linux host evidence indicates a confirmed security compromise, suspicious persistence, unauthorized privilege use, or abnormal network activity.

---

## Evidence Categories

| Evidence ID | Category | Source | Purpose | Reliability |
|---|---|---|---|---|
| E01 | Host identity | Day 1 / Day 3 | Establish host baseline | High |
| E02 | Process activity | Day 1 / Day 3 | Identify running processes | High |
| E03 | Process tree | Day 3 | Understand parent-child relationships | High |
| E04 | Network state | Day 3 / Day 7 | Correlate processes and connections | Medium-High |
| E05 | Privileges | Day 1 / Day 3 | Identify privileged accounts and binaries | High |
| E06 | Systemd persistence | Day 4 | Identify enabled persistence mechanisms | High |
| E07 | Cron persistence | Day 4 | Identify scheduled execution | High |
| E08 | Logs | Day 4 | Identify security-relevant events | Medium-High |
| E09 | Timeline | Day 4 | Establish event sequence | Medium |
| E10 | Threat model | Day 5 | Prioritize security risks | Medium |
| E11 | Security controls | Day 5 / Day 6 | Determine defensive controls | High |
| E12 | Cryptographic posture | Day 6 | Assess security mechanisms | High |
| E13 | Automated telemetry | Day 7 | Produce repeatable host snapshot | High |

---

## Evidence Interpretation

Evidence should not be interpreted in isolation.

A process may be legitimate even when it has network activity.

A network connection does not by itself prove malicious activity.

A SUID binary does not by itself prove privilege abuse.

An enabled systemd unit or cron job does not by itself prove malicious persistence.

Multiple independent indicators should be correlated before reaching a compromise conclusion.

---

## Key Evidence Relationships

### Process + Network

A network connection should be correlated with the responsible process where possible.

### Process + Privilege

The process owner and effective privileges should be considered.

### Persistence + Executable

A persistence mechanism should be investigated together with the executable or command it launches.

### Logs + Timeline

Log events should be interpreted according to their chronological sequence.

### Threat Model + Evidence

Threat-model risks are hypotheses or expected attack paths, not proof that an attack occurred.

---

## Evidence Limitations

The collected evidence represents snapshots and selected logs.

It does not provide complete historical visibility.

Host-side QEMU network activity cannot automatically be attributed to a specific guest application.

Remote IP addresses alone are insufficient to classify an endpoint as malicious.

Some command output may be incomplete when elevated privileges are required.

Therefore conclusions must explicitly include confidence and limitations.
