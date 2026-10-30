# Linux Persistence Analysis

## Objective

Identify common Linux persistence mechanisms and correlate them with available evidence.

## Persistence Sources Examined

The investigation covered:

1. systemd enabled units
2. systemd timers
3. cron directories
4. user crontab
5. cron spool
6. user autostart
7. shell startup files
8. recent journal activity

## Systemd

147 enabled unit files were identified across different unit types.

The observed virtualization units are consistent with the Windows VM laboratory environment.

19 timers were identified and primarily corresponded to system maintenance, monitoring, updates and housekeeping.

## Cron

System cron directories and the current user's crontab were collected.

Additional keyword searching was performed for commonly suspicious execution mechanisms and temporary paths.

## User Autostart

The user's `~/.config/autostart` directory was examined.

No clear suspicious autostart mechanism was established from the collected evidence.

## Shell Persistence

The user's `.bashrc` and `.profile` were collected.

A targeted search was performed for commands and paths commonly associated with suspicious startup execution.

## Assessment

No clearly suspicious persistence mechanism was identified within the collected evidence.

The results provide a useful Linux persistence baseline for future investigations.

## Limitations

This analysis does not prove that the system has never contained malicious persistence.

Persistence mechanisms can be hidden in less common locations or disguised as legitimate components.

Historical file changes were not reconstructed during this phase.
