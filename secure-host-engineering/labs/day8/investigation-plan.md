# Investigation Plan

## 1. Investigation Question

Does the available Linux evidence support a conclusion of host compromise or suspicious activity?

---

## 2. Scope

The investigation covers:

- Running processes
- Process relationships
- User identity and privileges
- Network connections
- Listening services
- Systemd persistence
- Timers
- Cron persistence
- User autostart
- Security logs
- Security controls
- SUID/SGID binaries
- Automated telemetry

The investigation is limited to the collected local Linux evidence.

---

## 3. Investigation Phases

### Phase 1 — Establish Baseline

Determine:

- Host identity
- Kernel
- Current user
- Groups
- Running services
- Expected virtualization components

### Phase 2 — Process Investigation

Review:

- Process ownership
- Parent-child relationships
- Executable paths
- Long-running processes
- Unusual process states

### Phase 3 — Network Investigation

Review:

- Listening sockets
- Established connections
- Process/network correlation
- Local-only services
- Remote endpoints

### Phase 4 — Persistence Investigation

Review:

- Enabled systemd units
- Timers
- Cron directories
- User crontab
- User autostart
- Shell startup files

### Phase 5 — Privilege Investigation

Review:

- sudo configuration
- User groups
- SUID binaries
- SGID binaries
- Root-owned security-sensitive components

### Phase 6 — Log Investigation

Review:

- Authentication events
- Warnings
- Current boot
- Recent journal events
- Logind activity
- Boot history

### Phase 7 — Correlation

Compare evidence between:

- Processes
- Network
- Privileges
- Persistence
- Logs
- Timeline

### Phase 8 — Conclusion

Classify findings as:

- Confirmed evidence
- Suspicious indicator
- Benign/expected activity
- Unknown
- Insufficient evidence

The conclusion must include confidence and limitations.
