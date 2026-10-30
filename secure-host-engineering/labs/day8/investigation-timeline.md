# Investigation Timeline

## Timeline Purpose

The timeline provides a chronological view of selected security-relevant observations.

It is not a complete forensic timeline.

---

## Timeline Sources

The timeline is based on:

- Journal entries
- Process observations
- Network observations
- Persistence observations
- Security-control observations
- Automated telemetry

---

## Chronological Analysis

### Initial Host State

The investigation established the Linux host identity, kernel, user identity, groups, processes, and security controls.

### Process and Service State

Running processes and services were reviewed.

Virtualization-related processes were expected because the laboratory Windows VM was configured using QEMU/KVM.

### Network State

Network listeners and active connections were reviewed.

Local services such as DNS, mDNS, printing, and virtualization-related services were identified.

Network connections were not automatically classified as malicious based only on remote addresses.

### Persistence State

Systemd units, timers, cron locations, user autostart, and shell startup configuration were reviewed.

No clearly suspicious persistence mechanism was established.

### Log State

Recent journal data and authentication-related events were reviewed.

Warnings were treated as events requiring context rather than automatically treating them as malicious.

---

## Timeline Assessment

The available timeline does not demonstrate a clear sequence of compromise.

No reliable chain of:

Initial Access → Execution → Persistence → Privilege Abuse → Command and Control

was established.

---

## Confidence

Medium.

The timeline provides useful evidence for the investigated period but is not a complete forensic reconstruction.
