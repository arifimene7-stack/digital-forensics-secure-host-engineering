# Linux Log Analysis

## Objective

Analyze recent system and authentication logs for events relevant to security investigation.

## Evidence Collected

The following evidence was collected:

- 24-hour journal
- 24-hour warning-level journal
- authentication-related events
- systemd-logind activity
- current boot journal
- current boot warnings
- boot history

## Journal Activity

The 24-hour journal contained substantial system activity.

The current timeline included normal operating-system events such as:

- system suspend/resume activity
- kernel power-management messages
- system service activity
- networking events
- user session activity

## Authentication

Authentication-related journal entries were collected using searches for:

- authentication
- sudo
- session opened
- session closed
- failed
- failure
- login

These entries provide evidence for reconstructing user sessions and privileged activity.

## Warnings

Warning-level entries were collected separately.

Warnings are not automatically indicators of compromise. They require correlation with the affected subsystem, process and timing.

## Assessment

The collected logs provide sufficient data to establish a baseline of recent system and authentication activity.

No clearly malicious event was established from the evidence reviewed so far.

## Limitations

A journal warning alone does not demonstrate malicious behavior.

Further investigation would be required for suspicious authentication events, unusual privilege escalation or unexpected service execution.
