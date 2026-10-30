# Systemd Persistence Analysis

## Objective

Analyze systemd-enabled units and timers as potential persistence mechanisms.

## Evidence

The host reported 147 enabled unit files. These include multiple unit types:

- services
- mount units
- path units
- sockets
- timers
- targets

Therefore, the total number does not represent 147 running services.

## Enabled Services

Notable enabled services include:

- NetworkManager
- systemd-resolved
- cron
- rsyslog
- ufw
- unattended-upgrades
- libvirtd
- libvirt-guests
- qemu-kvm
- virtlockd
- virtlogd
- snapd
- apparmor
- sssd
- openvpn
- virtualbox

Several virtualization-related units are expected because this host is configured for virtualization.

## Timers

19 timers were reported.

Observed timers include:

- sysstat-collect.timer
- motd-news.timer
- anacron.timer
- fwupd-refresh.timer
- apt-daily.timer
- dpkg-db-backup.timer
- sysstat-rotate.timer
- sysstat-summary.timer
- logrotate.timer
- e2scrub_all.timer
- apt-daily-upgrade.timer
- man-db.timer
- update-notifier-download.timer
- systemd-tmpfiles-clean.timer
- fstrim.timer
- update-notifier-motd.timer
- apport-autoreport.timer
- snapd.snap-repair.timer
- ua-timer.timer

The observed schedule is consistent with periodic system maintenance and monitoring tasks.

## Assessment

No clearly suspicious systemd persistence mechanism was identified from the collected enabled-unit and timer inventory.

The virtualization-related units are consistent with the known laboratory configuration.

## Limitations

Unit names alone cannot establish whether a persistence mechanism is malicious. A complete forensic assessment would also inspect unit file contents, executable paths, ownership and modification times.
