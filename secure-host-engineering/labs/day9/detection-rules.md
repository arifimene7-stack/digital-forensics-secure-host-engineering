# Day 9 - Detection Rules

## 1. Objective

The objective of this document is to define defensive detection rules for Linux host security monitoring.

The rules are based on the threat model, telemetry design, persistence analysis, privilege analysis, network analysis, and investigation work completed during Days 1-8.

A detection indicator does not automatically prove malicious activity. Each alert requires contextual validation.

---

## 2. Detection Rule DR-01 - Privileged Process Anomaly

### Purpose
Identify processes running with elevated privileges that require investigation.

### Telemetry
- PID
- PPID
- User
- Executable
- Command line
- Process state
- Process start time

### Detection Logic
Generate an alert when:
- a process runs as root and has an unexpected executable or command line, or
- a privileged process has an unusual parent-child relationship.

### Validation
The process must be correlated with:
- installed software
- system services
- expected administrative activity
- parent process
- executable path

### Severity
Medium initially.

---

## 3. Detection Rule DR-02 - Persistence Anomaly

### Purpose
Identify potentially suspicious persistence mechanisms.

### Telemetry
- systemd enabled units
- systemd timers
- cron jobs
- user crontab
- user autostart entries
- shell startup files

### Detection Logic
Generate an alert when persistence contains:
- unexpected executable paths
- commands using temporary directories
- suspicious download utilities
- unexpected scripting interpreters
- unusual user-created startup entries

### Validation
Correlate the entry with:
- package ownership
- known system functionality
- creation/modification context
- expected administrative configuration

### Severity
High if unexplained.

---

## 4. Detection Rule DR-03 - Suspicious Network Listener

### Purpose
Identify unexpected network services listening on the host.

### Telemetry
- Local address
- Local port
- Protocol
- PID
- Process
- User

### Detection Logic
Generate an alert when:
- a previously unknown process opens a listening socket, or
- a listener is bound to a broad interface without an identified business or laboratory purpose.

### Validation
Determine:
- owning process
- executable
- service
- configuration
- expected purpose

### Severity
Medium to High depending on exposure.

---

## 5. Detection Rule DR-04 - Suspicious Network Connection

### Purpose
Identify network connections requiring investigation.

### Telemetry
- Process
- PID
- User
- Local address
- Remote address
- Remote port
- Connection state

### Detection Logic
Generate an investigation alert when:
- an unexpected process establishes an external connection,
- a process connects to an unusual destination,
- or network activity cannot be explained by the host role.

### Validation
IP addresses alone must not be treated as proof of malicious activity.

The process, destination, timing, protocol, and host context must be correlated.

### Severity
Medium initially.

---

## 6. Detection Rule DR-05 - Security Control Degradation

### Purpose
Detect disabled or degraded security controls.

### Telemetry
- AppArmor status
- Secure Boot status
- UFW status
- unattended-upgrades
- journald

### Detection Logic
Generate an alert when an expected security control becomes disabled or inactive.

### Important Context

UFW is installed on the analyzed host but was observed to be inactive.

Therefore, the existing state must not be interpreted as evidence that UFW was previously active or that it currently provides firewall protection.

### Severity
Medium.

---

## 7. Detection Rule DR-06 - Privilege Escalation Indicators

### Purpose
Identify changes or activity associated with privilege escalation.

### Telemetry
- sudo configuration
- SUID/SGID binaries
- privileged groups
- authentication events
- process identity

### Detection Logic
Generate an investigation alert when:
- unexpected privilege changes occur,
- unusual sudo activity appears,
- suspicious SUID/SGID files are introduced,
- or a non-expected account obtains elevated privileges.

### Severity
High if unexplained.

---

## 8. Detection Philosophy

The detection system follows a correlation-based approach.

A single indicator should not automatically be classified as malicious.

The investigation should correlate:

Process + Identity + Privilege + Network + Persistence + Files + Logs

The final classification should distinguish between:

- Normal
- Requires Investigation
- Suspicious
- Confirmed Malicious

The available evidence from Days 1-8 did not establish confirmed compromise.
