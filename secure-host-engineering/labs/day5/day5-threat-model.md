# Day 5 — Linux Host Threat Model

## 1. Executive Summary

This threat model evaluates the security risks associated with the analyzed Ubuntu Linux host and its local virtualization environment.

The model is based on the observations collected during Days 1–4, including processes, services, privileges, network activity, persistence mechanisms and system logs.

No confirmed malicious activity was established during the previous investigation.

The objective of this threat model is therefore to identify realistic attack paths and determine how they could be prevented or detected.

---

## 2. Protected Assets

The most important assets are:

- Ubuntu host integrity
- User identity and administrative privileges
- Credentials and secrets
- System services and configurations
- Logs and forensic evidence
- QEMU/KVM and libvirt infrastructure
- Windows laboratory VM
- Security project files

---

## 3. Main Trust Boundaries

The major trust boundaries are:

1. User to privileged system
2. Host to network
3. Host to virtual machine
4. Applications to system services
5. Configuration to automatic execution
6. User to project files
7. Applications to credentials and secrets

---

## 4. Main Threat Actors

Relevant threat actors include:

- Malicious local user
- Compromised user account
- Malicious or compromised application
- Remote network attacker
- Compromised virtual machine
- Supply-chain or update compromise

---

## 5. Main Attack Surface

The main attack surfaces are:

- sudo privileges
- SUID/SGID programs
- systemd services and timers
- cron
- network services
- QEMU/KVM and libvirt
- user startup mechanisms
- credentials and secrets
- logs
- security project files

The presence of an attack surface does not prove that it has been exploited.

---

## 6. STRIDE Summary

| STRIDE Category | Main Threat |
|-----------------|-------------|
| Spoofing | Credential/session compromise |
| Tampering | Modification of system configuration |
| Repudiation | Avoiding or manipulating forensic evidence |
| Information Disclosure | Exposure of credentials or sensitive configuration |
| Denial of Service | Resource exhaustion |
| Elevation of Privilege | Abuse of sudo, SUID/SGID or vulnerable services |

---

## 7. Highest-Priority Risks

The most important risks are:

### R1 — Privileged Account Compromise

A compromised privileged user account could provide broad control over the host.

### R2 — Unauthorized Persistence

Attackers could attempt to use systemd, cron or startup mechanisms to maintain access.

### R3 — Credential or Secret Exposure

Sensitive credentials or configuration secrets could allow additional unauthorized access.

### R4 — Network Service Exposure

A vulnerable network-accessible service could provide an initial attack path.

### R5 — Host/Guest Boundary Attack

A compromised virtual machine could attempt to interact with the host through the virtualization boundary.

---

## 8. Existing Security Controls

The investigation identified several security mechanisms:

- AppArmor is active and enforcing multiple profiles.
- systemd-journald provides system and security-related logging.
- sudo provides controlled administrative execution and auditing.
- Automatic update mechanisms are present.
- Secure Boot is enabled.
- UFW is installed, but the collected evidence shows that it is currently inactive.

These controls reduce risk, but their effectiveness depends on their actual configuration and operational state.

---

## 9. Detection Strategy

A useful detection strategy should correlate:

Process + User + Privilege + Network + Persistence + Logs

For example:

An unexpected process running as root should be correlated with:

- its parent process
- executable path
- command line
- network connections
- recent sudo activity
- systemd or cron changes
- relevant journal events

This correlation provides stronger evidence than any single indicator.

---

## 10. Security Baseline

The previous investigation provides a baseline of normal host behavior.

Important baseline observations include:

- Normal system services were observed.
- Standard persistence mechanisms were present.
- QEMU/KVM activity was associated with the laboratory VM.
- Network connections were observed from expected applications and services.
- No clearly malicious persistence was established.
- No confirmed host compromise was established.

---

## 11. Confidence and Limitations

Confidence:

Medium.

Limitations:

- The investigation represents a point-in-time view.
- IP addresses alone cannot establish malicious intent.
- Host-side virtualization traffic cannot always be attributed to a specific guest application.
- Some filesystem inspection commands may have incomplete results.
- A complete historical process/network timeline was not available.
- Threat modeling identifies potential risks and does not prove exploitation.

---

## 12. Final Assessment

The Linux host has a meaningful security attack surface because it provides administrative privileges, system services, persistence mechanisms, network connectivity and virtualization capabilities.

The highest-value defensive approach is continuous correlation of processes, privileges, network activity, persistence mechanisms and logs.

The threat model does not identify a confirmed compromise. Instead, it establishes a structured baseline for future detection and incident investigation.

## Status

Day 5 Threat Modeling: COMPLETED
