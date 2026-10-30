# Hypothesis Log

## H1 — Host Compromise

### Hypothesis

The Linux host may have been compromised.

### Supporting Indicators

No single confirmed indicator of compromise was identified in the collected evidence.

### Evidence Reviewed

- Processes
- Network connections
- Persistence
- Logs
- Privileges
- Security controls

### Test

Correlate independent indicators across the collected evidence.

### Result

Not confirmed.

### Confidence

Medium-High that no compromise was demonstrated by the available evidence.

### Limitation

Absence of evidence in a point-in-time collection does not prove that compromise never occurred.

---

## H2 — Suspicious Persistence

### Hypothesis

An unauthorized persistence mechanism may exist.

### Evidence Reviewed

- Systemd enabled units
- Systemd timers
- Cron directories
- User crontab
- Autostart configuration
- Shell startup files

### Test

Review persistence mechanisms and identify commands, executables, ownership, and unusual locations.

### Result

No clearly suspicious persistence mechanism was established from the collected evidence.

### Confidence

Medium.

### Limitation

Unit names and schedules alone are insufficient for complete forensic validation.

---

## H3 — Unauthorized Privilege Abuse

### Hypothesis

A process or user may have abused elevated privileges.

### Evidence Reviewed

- sudo configuration
- User groups
- SUID binaries
- SGID binaries
- Process ownership
- Authentication logs

### Test

Correlate privileged identities and processes with security-relevant events.

### Result

No confirmed privilege abuse was established.

### Confidence

Medium.

### Limitation

The available evidence does not reconstruct every historical privileged action.

---

## H4 — Suspicious Network Activity

### Hypothesis

The host may contain an unauthorized network connection.

### Evidence Reviewed

- Listening sockets
- Established connections
- Process/network correlation
- QEMU networking
- System services

### Test

Correlate network endpoints with responsible processes and expected system or lab activity.

### Result

No confirmed malicious network activity was established.

Several connections were associated with normal applications or virtualization-related activity.

### Confidence

Medium.

### Limitation

An IP address alone does not establish maliciousness, and host-side virtualization traffic cannot always be attributed to a guest application.

---

## H5 — Security Control Failure

### Hypothesis

A disabled or ineffective security control may increase host risk.

### Evidence Reviewed

- AppArmor
- Secure Boot
- unattended-upgrades
- journald
- UFW

### Result

AppArmor and other selected controls were active in the collected evidence.

Secure Boot was enabled.

UFW was installed but inactive.

### Interpretation

UFW should not be considered an active preventive firewall control in this assessment.

The inactive state represents a security hardening gap rather than evidence of compromise.
