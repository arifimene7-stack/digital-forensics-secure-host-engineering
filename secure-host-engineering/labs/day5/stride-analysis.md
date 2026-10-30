# STRIDE Threat Analysis

## Overview

STRIDE is used to classify threats into six categories:

- Spoofing
- Tampering
- Repudiation
- Information Disclosure
- Denial of Service
- Elevation of Privilege

## S — Spoofing

### Threat

An attacker obtains valid credentials or compromises an existing user session.

### Affected Assets

- User identity
- Credentials
- Host OS

### Detection Opportunities

- Authentication logs
- sudo activity
- Unexpected login events
- Unusual process execution

---

## T — Tampering

### Threat

An attacker modifies system configuration, persistence mechanisms, project files or VM configuration.

### Affected Assets

- systemd configuration
- cron
- project files
- VM configuration
- logs

### Detection Opportunities

- File modification monitoring
- Configuration integrity checks
- Journal events
- File ownership and permission analysis

---

## R — Repudiation

### Threat

An attacker performs actions and attempts to avoid accountability by deleting or avoiding useful logs.

### Affected Assets

- Journald logs
- Authentication records
- Forensic evidence

### Detection Opportunities

- Centralized logging
- Log integrity monitoring
- Correlation of process and authentication events

---

## I — Information Disclosure

### Threat

Sensitive configuration, credentials, secrets or private data become accessible to unauthorized processes or users.

### Affected Assets

- Credentials
- VM configuration
- Host configuration
- Project evidence

### Detection Opportunities

- File permissions
- Access monitoring
- Secret scanning
- Unusual file access

---

## D — Denial of Service

### Threat

An attacker consumes CPU, memory, disk or network resources.

### Affected Assets

- Ubuntu host
- QEMU/KVM VM
- System services

### Detection Opportunities

- CPU monitoring
- Memory monitoring
- Disk monitoring
- Process monitoring
- Service availability monitoring

---

## E — Elevation of Privilege

### Threat

An attacker with limited privileges abuses sudo, SUID/SGID programs or a vulnerable service to obtain higher privileges.

### Affected Assets

- Root privileges
- Host OS
- System services

### Detection Opportunities

- sudo logs
- Process owner analysis
- SUID/SGID inventory
- Unexpected root processes
- Changes to privileged binaries

## Conclusion

The most important STRIDE categories for this host are:

1. Elevation of Privilege
2. Tampering
3. Information Disclosure
4. Spoofing
5. Denial of Service
6. Repudiation
