# Final Investigation Report

## 1. Executive Summary

A Linux host security investigation was performed using evidence
collected during Days 1-9 of the security engineering training.

The investigation covered host inventory, processes, privileges, identity,
persistence, systemd, cron, logs, network activity, security controls,
cryptographic configuration, telemetry collection, automated detection,
and contextual validation.

No confirmed host compromise was established from the available evidence.

## 2. Scope

The investigation focused on the Linux host and its local security
configuration.

The environment also contained a Windows laboratory VM running through
QEMU/KVM.

All observations were interpreted within this authorized laboratory
context.

## 3. Evidence Integrity

Evidence was collected into the project laboratory structure and
integrity checks were performed during the investigation.

The Day 9 detection process used:

    proof/current-telemetry.json

The detector executed successfully and generated investigation
indicators.

## 4. Process Analysis

Process analysis identified normal Linux kernel threads, system
services, desktop components, virtualization processes, and user
processes.

The QEMU process associated with the laboratory Windows VM was identified
as PID 42094 and executed as user imene.

Its associated KVM thread PID 42103 was also identified.

No process was established as malicious from the available evidence.

## 5. Privilege and Identity

The investigation confirmed that user imene has sudo privileges.

SUID and SGID binaries were inventoried.

These findings represent security-relevant attack surface but do not
independently demonstrate privilege abuse or compromise.

## 6. Persistence

Systemd units, timers, cron directories, user cron configuration,
autostart locations, and shell startup files were reviewed.

No clearly malicious persistence mechanism was established.

## 7. Network Analysis

Network listeners and connections were correlated with processes.

Expected local services included DNS resolution, Avahi, chrony,
NetworkManager, CUPS, libvirt/dnsmasq, and virtualization-related
networking.

QEMU generated network activity associated with the laboratory Windows
VM.

Host-side QEMU network activity cannot be attributed to a specific guest
application without guest-side telemetry.

Remote IP addresses alone were not treated as evidence of maliciousness.

## 8. Security Controls

AppArmor was observed to be active.

Secure Boot was enabled.

systemd-journald and unattended-upgrades were active.

UFW was installed but inactive and therefore was not treated as an active
firewall control.

## 9. Automated Detection

The automated detection pipeline successfully processed the collected
telemetry.

The initial root-process detection produced 180 indicators.

After contextual tuning, the detector generated 13 investigation
indicators.

The remaining indicators were reviewed and were largely attributable to
expected Linux kernel, graphics, desktop, system-service, VirtualBox,
and KVM/QEMU activity.

PID 13037 could not be independently verified because it had terminated
before contextual examination.

The indicators therefore do not establish malicious activity.

## 10. Investigation Conclusion

No confirmed host compromise was established from the available
evidence.

The investigation provides a defensible baseline of host processes,
privileges, persistence, network activity, security controls, telemetry,
and detection logic.

Confidence: Medium-High.

## 11. Limitations

The investigation has several limitations:

- Evidence is primarily point-in-time telemetry.
- Complete historical process and network telemetry was not available.
- Guest-side Windows telemetry was not used for attributing activity
  inside the VM.
- Remote IP ownership/reputation was not independently established.
- One detected process (PID 13037) had terminated before contextual
  verification.
- Detection rules depend on expected-process baselines and may require
  further tuning in a production environment.

## 12. Final Security Statement

Based on the evidence collected and analyzed during Days 1-9, no
confirmed compromise was established.

The appropriate security conclusion is therefore:

"No confirmed host compromise was established from the available
evidence; the observed indicators were either explained by expected
system activity or remained insufficient for a malicious determination."
