# Persistence Investigation Report

## What is Persistence?
Persistence means ways to make a program run automatically.
It can be used by the system (normal) or by attackers (malicious).

## 1. Systemd Services
Command: `systemctl list-unit-files --state=enabled`
Result: Found 123 enabled services like `ssh.service`, `cron.service`, `NetworkManager.service`.
These are normal system services that start at boot.

## 2. Systemd Timers
Command: `systemctl list-timers --all`
Result: Found 19 timers like `apt-daily.timer`, `logrotate.timer`, `fwupd-refresh.timer`.
These run scheduled tasks automatically.

## 3. Cron Jobs
Commands:
- `ls -la /etc/cron.d/`
- `ls -la /etc/cron.daily/`
- `ls -la /etc/cron.hourly/`
- `crontab -l`

Result:
- `/etc/cron.d/` has files: `anacron`, `e2scrub_all`, `placeholder`
- `/etc/cron.daily/` has: `anacron`, `apport`, `apt-compat`, `dpkg`, `logrotate`, `man-db`
- `/etc/cron.hourly/` has only `placeholder`
- User `imene` has no personal crontab ("no crontab for imene")

## 4. Startup Files
Command: `ls -la ~/.config/autostart/ 2>/dev/null`
Result: No autostart folder for user imene (empty output).

Command: `grep -n "" ~/.bashrc | head -50`
Result: `.bashrc` contains normal settings for history, prompt, and shell options. Nothing suspicious.

## Conclusion
We checked common persistence methods: systemd services, timers, cron jobs, and startup files.
All findings are normal system behavior. No suspicious persistence was found.
Evidence saved in the `proof/` folder.
