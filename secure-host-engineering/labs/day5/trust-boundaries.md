# Trust Boundaries

## Overview

A trust boundary is a point where data, privileges or control move between different security domains.

## Identified Trust Boundaries

### TB1 — User to Privileged System

The local user can obtain administrative privileges through sudo.

Risk:
- Compromise of the user account could lead to host-level compromise.

### TB2 — User Applications to System Services

Applications interact with system services and privileged background processes.

Risk:
- A vulnerable or compromised application could attempt to abuse a service.

### TB3 — Host to Network

The Ubuntu host communicates with local networks and external systems.

Risk:
- Network communication can expose services or provide an attack path.

### TB4 — Host to Virtual Machine

The Linux host provides CPU, memory, storage and virtual devices to the Windows laboratory VM through QEMU/KVM and libvirt.

Risk:
- A compromised guest could attempt to attack the virtualization boundary.

### TB5 — User to Project Files

The user executes Python analysis utilities and accesses forensic evidence.

Risk:
- Malicious or modified project files could execute unwanted code or corrupt evidence.

### TB6 — System Configuration to Execution

systemd, cron and user startup mechanisms can automatically execute programs.

Risk:
- Unauthorized configuration changes could establish persistence.

### TB7 — Applications to Credentials and Secrets

Applications and services may access configuration files, credentials or secrets.

Risk:
- Credential exposure could allow further unauthorized access.

## Security Principle

Each trust boundary should be monitored and protected because compromise on one side may allow an attacker to move into a more trusted security domain.
