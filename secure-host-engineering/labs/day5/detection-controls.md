# Detection and Security Controls

## Existing Controls

### UFW

UFW is installed on the host, but the collected evidence shows that the firewall is currently inactive.

Purpose:
- UFW can reduce unnecessary network exposure when enabled.

Security Observation:
- UFW should not be considered an active preventive control in the current state.
- Network exposure should therefore be assessed using the actual listening services and firewall configuration.


### AppArmor

AppArmor provides mandatory access-control profiles for supported applications.

Purpose:
- Restrict application behavior.

### Journald

systemd-journald provides system and security-related logging.

Purpose:
- Support detection and forensic investigation.

### Sudo

Administrative operations are controlled through sudo.

Purpose:
- Provide controlled administrative execution and auditing.

### Unattended Updates

Automatic update mechanisms help maintain the security state of installed software.

Purpose:
- Reduce exposure to known vulnerabilities.

### Secure Boot

Secure Boot is enabled on the host.

Purpose:
- Help protect the boot chain against unauthorized modifications.

## Detection Opportunities

| Threat | Detection Source |
|--------|------------------|
| Privilege escalation | sudo logs + process ownership |
| Persistence | systemd + cron + autostart |
| Network compromise | ss + process/network correlation |
| Suspicious process | ps + /proc |
| Authentication abuse | journald/authentication logs |
| Log tampering | log integrity monitoring |
| Resource exhaustion | CPU/memory/process monitoring |
| VM-related activity | QEMU/libvirt logs and process analysis |

## Recommended Improvements

1. Monitor changes to systemd and cron configuration.
2. Monitor privileged command execution.
3. Maintain centralized or protected logging.
4. Periodically review SUID/SGID binaries.
5. Monitor network listeners and correlate them with processes.
6. Protect credentials and virtualization secrets.
7. Maintain a baseline of normal processes and services.
