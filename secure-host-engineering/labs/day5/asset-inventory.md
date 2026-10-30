# Asset Inventory

## Purpose

This document identifies the main assets that must be protected on the analyzed Linux host and its local virtualization environment.

## Assets

| ID | Asset | Description | Security Importance |
|----|-------|-------------|---------------------|
| A1 | Ubuntu Host OS | Main operating system hosting applications and services | Critical |
| A2 | User Identity | Local user account and associated privileges | Critical |
| A3 | Sudo Privileges | Administrative capability available to the user | Critical |
| A4 | System Services | systemd-managed services and background processes | High |
| A5 | Network Interfaces | Host network connectivity and communication paths | High |
| A6 | Logs and Evidence | Journald logs and collected forensic evidence | High |
| A7 | QEMU/KVM Environment | Virtualization layer used to run the Windows laboratory VM | High |
| A8 | Windows VM Disk and Configuration | Guest operating system, virtual disk and VM configuration | High |
| A9 | Credentials and Secrets | Authentication information and configuration secrets | Critical |
| A10 | Security Tools and Controls | UFW, AppArmor, logging and update mechanisms | High |
| A11 | Project Files | Security analysis scripts, reports and evidence | Medium |
| A12 | System Configuration | systemd, cron, user startup and other configuration | High |

## Security Priorities

The highest-priority assets are:

1. Ubuntu host integrity
2. User identity and administrative privileges
3. Credentials and secrets
4. System configuration and persistence mechanisms
5. Logs and forensic evidence
6. Virtualization infrastructure
