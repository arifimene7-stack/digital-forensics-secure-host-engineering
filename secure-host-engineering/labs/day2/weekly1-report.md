# Week 1 Mini Host Investigation Report

## 1. Investigation Objective

The objective was to investigate whether the collected Linux host evidence showed indicators of unusual or malicious activity.

The investigation used process information, network socket evidence, privilege information, persistence artifacts, and system logs collected during the laboratory exercises.

---

## 2. Initial Hypothesis

### Hypothesis H1

The observed host activity may contain suspicious behavior that requires investigation.

This hypothesis was treated as an investigation question rather than an assumption of compromise.

---

## 3. Evidence Reviewed

The investigation reviewed:

* Linux system inventory
* Process information
* Process parent/child relationships
* Open file descriptors
* Network sockets
* SUID/SGID information
* Sudo privileges
* Systemd services
* Timers
* Cron configuration
* System logs
* Timeline information
* Python analyzer output

---

## 4. Process Investigation

The selected process was `xdg-document-portal`, PID 3341, running under the user `imene`.

Its parent process was PID 1 (`systemd`). The process investigation did not identify an external network connection associated with this process in the collected evidence.

The process is consistent with a normal Linux desktop service used for controlled document/file access.

Therefore, the available evidence does not identify this process as suspicious.

---

## 5. Network Investigation

The collected network evidence contains several established TCP connections over HTTPS.

These connections are associated with the Firefox process.

The evidence also contains local listening services including systemd-resolved and CUPS.

The presence of external HTTPS connections alone is not sufficient to classify the activity as malicious.

The evidence must be interpreted together with the responsible process and the surrounding host context.

---

## 6. Privilege and Persistence Review

The host contains normal SUID/SGID executables and the investigated user has sudo membership.

Systemd services, timers, cron locations, and shell startup mechanisms were reviewed during the investigation.

No suspicious persistence mechanism was identified in the collected evidence.

---

## 7. Timeline Assessment

The collected journal evidence showed normal user and service activity.

The observed activity included user login/session activity and normal system service events.

Some warnings were present, but they were not sufficient on their own to demonstrate malicious activity.

---

## 8. Analysis

The available evidence does not establish a confirmed host compromise.

The observed external network connections are associated with Firefox rather than the investigated `xdg-document-portal` process.

The investigated process itself did not show an external network connection in the collected evidence.

The persistence and privilege reviews also did not identify an obvious malicious mechanism.

---

## 9. Conclusion

### Finding

No suspicious or malicious activity was identified in the collected evidence.

This conclusion is limited to the evidence collected during the laboratory investigation.

It does not prove that malicious activity could never have occurred outside the observation period or outside the collected artifacts.

---

## 10. Confidence

**Confidence: Medium-High**

The conclusion is supported by multiple evidence sources, including process, network, privilege, persistence, and log analysis.

Confidence is limited by the scope and time period of the collected evidence.

---

## 11. Limitations

The investigation cannot establish:

* Complete historical system activity
* Activity that occurred outside the collection period
* Network activity not represented in the captured evidence
* Whether an apparently normal connection had malicious content without additional application-level evidence

Therefore, conclusions are restricted to the available artifacts.

---

## 12. Final Assessment

Based on the collected laboratory evidence, no confirmed indicators of host compromise were identified.

The investigation demonstrates the importance of correlating process, network, privilege, persistence, and log evidence rather than treating an individual IP address, port, or process as malicious without context.
