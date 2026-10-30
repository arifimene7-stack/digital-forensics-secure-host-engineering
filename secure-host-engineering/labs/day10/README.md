# Day 10 — Blind Case Investigation

## Overview

This lab documents a Linux host security investigation focused on identifying potential indicators of compromise through system logs, authentication events, process and network analysis, persistence mechanisms, and security configurations.

The investigation also includes evidence inventory and SHA-256 integrity validation.

## Objectives

- Examine system and authentication logs.
- Review running processes and network activity.
- Inspect persistence mechanisms.
- Evaluate Linux security controls.
- Identify suspicious system warnings.
- Validate collected evidence using SHA-256 hashes.

## Repository Structure

```text
day10/
├── README.md
├── investigation.md
└── proof/
    ├── apparmor.txt
    ├── evidence-sha256.txt
    └── ...
```

## Key Findings

- No confirmed evidence of host compromise was established.
- Secure Boot was enabled.
- AppArmor and unattended-upgrades were active.
- UFW was inactive at collection time.
- A GDM/PAM authentication failure involving user `imene` was identified.
- No matching SSH authentication events were found in the reviewed journal query.
- Several system and firmware-related warnings were observed.
- The MMIO Stale Data CPU warning requires further attention.

## Evidence Integrity

A total of 28 evidence files were compared against the SHA-256 manifest.

- 27 files passed hash verification.
- 1 file failed hash verification: `proof/apparmor.txt`.
- No missing or unlisted files were identified.

The original manifest was preserved. The integrity discrepancy is documented in the investigation report.

## Final Assessment

No confirmed host compromise was established from the available evidence.

This conclusion is limited to the collected artifacts and does not prove that the host is completely clean.

## Investigation Report

See [`investigation.md`](investigation.md) for the detailed findings, technical assessment, evidence integrity results, limitations, and recommendations.

## Evidence

See the [`proof/`](proof/) directory for the collected artifacts and SHA-256 manifest.

## Status

Investigation documented. Evidence inventory validated. SHA-256 verification partially failed due to one mismatched artifact.
