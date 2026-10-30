# Security Telemetry Design

## 1. Objective

Security telemetry provides the information required to detect, investigate and understand suspicious activity.

The telemetry design is based on the previous investigation model:

Process + User + Privilege + Network + Persistence + Logs

---

## 2. Process Telemetry

Collect:

- PID
- PPID
- Process owner
- Executable path
- Command line
- Process start time
- CPU usage
- Memory usage

Security value:

Helps identify unexpected processes, suspicious parent-child relationships and privilege changes.

---

## 3. Identity Telemetry

Collect:

- User identity
- UID
- GID
- Group membership
- sudo activity
- Authentication events

Security value:

Helps identify unauthorized use of privileged identities.

---

## 4. Network Telemetry

Collect:

- Local address
- Local port
- Remote address
- Remote port
- Protocol
- Connection state
- Owning process

Security value:

Allows network activity to be correlated with the responsible process.

---

## 5. Persistence Telemetry

Monitor:

- systemd services
- systemd timers
- cron jobs
- user autostart
- shell startup files

Security value:

Helps detect mechanisms used to maintain access.

---

## 6. File and Configuration Telemetry

Monitor security-sensitive changes to:

- Service configuration
- Cron configuration
- Authentication configuration
- Important binaries
- Project files
- Security configuration

---

## 7. Log Telemetry

Collect:

- Authentication events
- sudo events
- Service failures
- Service starts/stops
- Kernel security events
- Relevant application errors

---

## 8. Correlation

A single event may be benign.

Detection becomes stronger when multiple events are correlated.

Example:

Unexpected process
+
new network connection
+
recent sudo activity
+
new persistence entry

This combination should receive higher investigation priority than any individual indicator.

---

## 9. Detection Quality

Good telemetry should be:

- Relevant
- Accurate
- Timely
- Consistent
- Sufficient for investigation
- Protected against unauthorized modification

---

## 10. Privacy and Data Minimization

Telemetry should collect only information required for security monitoring.

Sensitive information should be protected and unnecessary personal data should not be collected.
