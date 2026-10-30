# Process Tree Analysis

## Objective
Analyze the Linux process hierarchy and investigate a representative high-value process.

## Evidence Collected
The process tree was collected using `pstree -p` and detailed process information using `ps`.

The investigated process was:

- PID: 42094
- Process: qemu-system-x86_64
- User: imene
- Parent PID: 3206
- State: Running
- Executable/command: `/usr/bin/qemu-system-x86_64`

## Process Investigation

PID 42094 is the QEMU process associated with the Windows virtual machine.

The process command line showed:

- Windows VM named `win11`
- KVM acceleration
- 4 GB allocated memory
- 3 virtual CPUs
- Windows disk image `win11.qcow2`
- Windows installation ISO
- OVMF UEFI firmware
- TPM socket
- SPICE server bound to localhost
- User-mode networking

The process runs under the `imene` account rather than root.

## File Descriptor Analysis

`/proc/42094/fd` and `lsof` were collected to examine files, sockets and other resources opened by the process.

The evidence included QEMU libraries, virtual machine resources and KVM-related resources.

The `lsof` command reported warnings for FUSE paths, so its output may be incomplete for those filesystems.

## Assessment

The process behavior is consistent with a locally configured virtualization workload.

No suspicious process ancestry or clearly malicious process behavior was identified in the collected evidence.

## Limitations

This is a point-in-time process snapshot. Process behavior can change over time, and the host-side QEMU process cannot by itself provide complete visibility into activity occurring inside the Windows guest.
