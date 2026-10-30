# Service Analysis

## Objective
Analyze running Linux services and investigate a representative security-relevant service.

## Running Services

The host had 36 running system services at the time of collection.

Examples include:

- NetworkManager
- systemd-resolved
- systemd-journald
- cron
- rsyslog
- cups
- libvirtd
- unattended-upgrades
- ssh-related components
- virtualization-related services

## Investigated Service

The selected service was:

`libvirtd.service`

Process information:

- PID: 1829
- User: root
- Parent PID: 1
- Command: `/usr/sbin/libvirtd --timeout 120`

The service is therefore managed as a system-level service and runs with root privileges.

## Security Relevance

libvirtd provides virtualization management functionality and is expected on a host running virtual machines.

The host also had a QEMU process running the Windows virtual machine.

This creates a meaningful relationship between the service layer and the process layer:

libvirtd -> virtualization management -> QEMU -> Windows guest

## Assessment

The observed libvirtd process and its relationship with the running QEMU process are consistent with the configured virtualization environment.

No suspicious service behavior was identified in the collected evidence.

## Limitation

The executable resolution using `/proc/1829/exe` did not return the expected target path during collection. However, `ps` independently identified the command as `/usr/sbin/libvirtd --timeout 120`.

Therefore, the assessment relies primarily on the process information returned by `ps`.
