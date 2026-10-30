# Day 3 — Linux Deep Host Analysis

## Objective

Perform a deeper security analysis of a Linux host by correlating:

- Processes
- Process hierarchy
- Services
- Network activity
- User privileges
- SUID/SGID executables

## Host Context

The analyzed system is an Ubuntu Linux host used for cybersecurity laboratory work and virtualization.

A Windows virtual machine was running through QEMU/KVM.

## Process Findings

The investigated high-value process was QEMU PID 42094.

The process:

- runs as user `imene`
- has PPID 3206
- uses KVM acceleration
- hosts the Windows virtual machine
- uses a Windows disk image
- uses UEFI firmware
- uses TPM support
- exposes SPICE on localhost
- uses user-mode networking

The process behavior is consistent with the known virtualization workload.

## Service Findings

36 services were running during collection.

The investigated `libvirtd.service` process:

- PID: 1829
- runs as root
- has PPID 1
- executes `/usr/sbin/libvirtd --timeout 120`

Its presence is consistent with the configured virtualization environment.

## Network Findings

The host had normal infrastructure traffic including:

- DNS
- DHCP
- mDNS
- time synchronization
- CUPS
- Firefox HTTPS connections
- libvirt networking

QEMU also had several network connections.

These connections were observed at the host level and cannot automatically be attributed to a specific application inside the Windows guest.

## Privilege Findings

The current user belongs to the `sudo` group and has:

`(ALL : ALL) ALL`

The host also contains several SUID and SGID executables.

These are security-sensitive but are not, by themselves, evidence of compromise.

## Overall Assessment

No suspicious or clearly malicious activity was identified in the collected evidence.

The observed process, service and network activity is broadly consistent with the configured Linux workstation and virtualization laboratory.

## Confidence

Confidence: Medium-High

The assessment is supported by multiple evidence sources:

- process listings
- process tree
- `/proc`
- open file descriptors
- network socket information
- running services
- privilege information
- SUID/SGID inventory

## Limitations

1. The investigation represents a point-in-time snapshot.
2. Host-side QEMU telemetry cannot provide complete visibility into the Windows guest.
3. `lsof` reported warnings for some FUSE filesystems.
4. Remote IP addresses were not independently attributed during this phase.
5. The `/proc/1829/exe` resolution did not return the expected executable path, although `ps` identified the libvirtd command.
6. No complete historical process or network timeline was constructed during this phase.

## Conclusion

The collected evidence provides a coherent baseline of the Linux host's processes, services, networking and privilege configuration.

No clear indicators of compromise were identified within the available evidence.
