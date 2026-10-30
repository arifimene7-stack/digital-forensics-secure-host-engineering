# Engineering Review

## 1. Security

The collector avoids shell interpretation by using shell=False.

External command failures are handled.

Timeouts are implemented for subprocess execution.

Telemetry output is protected with restrictive file permissions.

## 2. Reliability

The collector records command results and errors instead of assuming that every command will always succeed.

This supports partial collection when a command is unavailable or access is restricted.

## 3. Maintainability

The implementation is divided into separate collection functions:

- collect_host()
- collect_identity()
- collect_processes()
- collect_network()
- collect_persistence()
- collect_privileged_binaries()
- collect_security_controls()

This makes individual components easier to modify and test.

## 4. Least Privilege

The collector is designed to operate without requiring root privileges for the main collection workflow.

Some telemetry may therefore be incomplete.

The tool should not automatically escalate privileges.

## 5. Data Minimization

The collector avoids intentionally storing complete process command lines.

Only information required for the defensive telemetry objective is collected.

## 6. Main Risks

### Risk 1 — Incomplete telemetry

Some commands may require additional privileges.

### Risk 2 — Point-in-time visibility

The collector records the current state and cannot reconstruct historical events.

### Risk 3 — Remote IP attribution

A network connection does not by itself prove malicious activity.

### Risk 4 — False positives

A running service, SUID binary, timer, or network connection may be completely legitimate.

## 7. Recommended Improvements

Future versions could add:

- Structured event normalization
- Hashing of selected executable files
- Historical comparison between collections
- File modification monitoring
- Alert rules
- Centralized log storage
- Cryptographic integrity protection

## 8. Engineering Assessment

The collector is suitable as a defensive local telemetry prototype.

It should be treated as an evidence-collection component rather than a standalone intrusion detector.

