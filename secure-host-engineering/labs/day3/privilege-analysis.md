# Privilege Analysis

## Objective
Analyze user identity, group membership, sudo privileges and SUID/SGID executables.

## Current User

The current account is:

- Username: imene
- UID: 1000
- Primary group: imene
- Supplementary groups include:
  - sudo
  - adm
  - cdrom
  - plugdev
  - users
  - lpadmin
  - lxd
  - libvirt
  - cyberlab

## Sudo Privileges

The `sudo -l` output shows:

`(ALL : ALL) ALL`

This means the user is permitted to execute commands through sudo as any user, including root, subject to normal authentication and sudo policy.

This represents a highly privileged administrative account.

## SUID Files

The collected SUID list included:

- `/usr/bin/pkexec`
- `/usr/bin/mount`
- `/usr/bin/su`
- `/usr/bin/fusermount3`
- `/usr/bin/passwd`
- `/usr/bin/chfn`
- `/usr/bin/sudo.ws`
- `/usr/bin/gpasswd`
- `/usr/bin/umount`
- `/usr/bin/ntfs-3g`
- `/usr/sbin/pppd`

## SGID Files

The collected SGID list included:

- `/usr/bin/ssh-agent`
- `/usr/bin/crontab`
- `/usr/bin/expiry`
- `/usr/bin/chage`
- `/usr/sbin/unix_chkpwd`
- `/usr/sbin/pam_extrausers_chkpwd`

## Important Observation

SUID and SGID permissions are security-sensitive because they can allow programs to execute with elevated or group privileges.

However, the existence of a SUID/SGID file does not by itself demonstrate malicious activity or exploitation.

The collected list represents the host state at the time of investigation.

## Assessment

The user account has administrative privileges through the sudo group and the configured sudo policy.

No evidence collected during this phase demonstrated unauthorized privilege escalation.

The SUID/SGID inventory should be retained as a baseline for future comparison.
