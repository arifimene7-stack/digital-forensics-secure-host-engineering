# Day 4 — Linux Persistence, Logs and Timeline Analysis

## Objective

Investigate Linux persistence mechanisms and correlate them with recent system and authentication logs.

## Persistence Findings

The host reported 147 enabled systemd unit files across several unit types.

The enabled configuration included:

- system services
- sockets
- mount units
- path units
- timers
- targets

19 timers were reported.

The observed timers primarily corresponded to:

- system maintenance
- package updates
- filesystem maintenance
- logging
- system statistics
- firmware updates
- housekeeping

Virtualization-related units were also enabled, including libvirt and QEMU-related components. These are consistent with the known laboratory environment.

## Cron Findings

System cron directories and the user crontab were examined.

A targeted search was performed for commands and paths commonly associated with suspicious persistence.

No clearly suspicious cron persistence mechanism was established from the collected evidence.

## User Persistence

User autostart and shell startup files were examined.

No clearly suspicious user-level persistence mechanism was established from the collected evidence.

## Log Findings

The investigation collected:

- 24-hour journal
- warning-level journal
- authentication events
- systemd-logind activity
- current boot journal
- boot history

The logs contained normal system activity including power-management, networking, service and session events.

Warnings were treated as investigation leads rather than automatic indicators of compromise.

## Timeline

A 24-hour working timeline was generated from journal events.

The observed events include normal system power-management activity and service operations.

The timeline is useful for correlating persistence mechanisms with execution and authentication events.

## Overall Assessment

No clearly malicious persistence mechanism or malicious event was established from the collected evidence.

The host's persistence configuration is broadly consistent with a Linux workstation used for virtualization and cybersecurity laboratory work.

## Confidence

Confidence: Medium

The assessment is supported by multiple persistence and logging sources.

However, this was a point-in-time analysis and does not reconstruct the complete historical state of the system.

## Limitations

1. Unit names alone do not establish whether a persistence mechanism is malicious.
2. Historical modifications to persistence mechanisms were not reconstructed.
3. The timeline represents a working 24-hour journal view and is not a complete forensic timeline.
4. Warning-level log entries require contextual investigation.
5. No complete file-integrity or historical metadata analysis was performed.

## Conclusion

The collected evidence establishes a useful Linux persistence and logging baseline.

No clear indicator of compromise was identified within the evidence reviewed for this phase.
