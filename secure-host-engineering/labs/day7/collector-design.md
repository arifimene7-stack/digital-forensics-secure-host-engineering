# Security Telemetry Collector Design

## 1. Purpose

The purpose of this tool is to automate the collection of defensive Linux security telemetry.

The collector combines information from the previous security analysis tasks into one structured JSON output.

## 2. Collected Telemetry

The collector gathers:

- Host and kernel information
- Current identity information
- Running processes
- Listening and active network connections
- Systemd enabled units
- Systemd timers
- Cron persistence locations
- SUID and SGID binaries
- Security control status

## 3. Output Format

The collector produces a structured JSON document.

Main sections:

- metadata
- host
- identity
- processes
- network
- persistence
- privileged_binaries
- security_controls

## 4. Security Design

The collector uses subprocess execution with shell=False.

This avoids shell interpretation and reduces command injection risk.

Command execution includes:

- timeout handling
- return-code collection
- stderr collection
- exception handling

The collector does not intentionally collect full process command lines.

## 5. Sensitive Data Protection

Common secret-like values are redacted before command output is stored.

The JSON output is written with restrictive permissions when supported.

## 6. Reliability

The collector records command failures instead of immediately terminating the entire collection process.

This allows partial telemetry to remain available when a command is unavailable or requires additional privileges.

## 7. Limitations

The collector is a point-in-time snapshot.

It does not provide historical process or network activity.

Some network information may require elevated privileges.

SUID/SGID collection is limited to standard system binary directories.

The collector does not determine whether an observed remote IP address is malicious.

The collector provides telemetry and evidence, not a complete compromise verdict.
