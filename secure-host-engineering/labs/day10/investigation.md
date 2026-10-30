# Day 10 — Blind Case Investigation

## 1. Objective

The objective of this investigation is to examine a Linux host for potential indicators of compromise by reviewing:

- Authentication and system journal logs.
- Running processes and network activity.
- Persistence mechanisms.
- Security controls and configurations.
- System warnings and service failures.
- Evidence integrity and collection limitations.

## 2. Investigation Scope

The investigation was based on the collected artifacts stored in the `proof/` directory.

The evidence includes:

- System and journal information.
- Authentication-related events.
- Process and network information.
- SUID and SGID files.
- Cron jobs and autostart entries.
- Security configuration and service status.
- System warnings and boot information.

## 3. Findings

### 3.1 Security Controls

**Secure Boot**
- Secure Boot was enabled.

**AppArmor**
- AppArmor was active.
- The system reported 256 profiles:
  - 173 in enforce mode.
  - 8 in complain mode.
  - 75 unconfined.
- The status output reported 30 processes associated with profiles.
- One profile was forced into complain mode through `/etc/apparmor.d/force-complain`.

**Firewall**
- UFW was inactive at the time of collection.

**Automatic Updates**
- The unattended-upgrades service was active.

### 3.2 Authentication Analysis

The reviewed journal contained a GDM/PAM authentication failure involving the user `imene`:

`Oct 08 01:30:26`

A subsequent logind event recorded a session for the same user at approximately:

`Oct 08 01:30:33`

These events are consistent with a failed authentication followed by a later session. However, the available records do not independently establish that both events belong to the same authentication attempt.

No matching SSH authentication events were found in the reviewed journal query.

This does not prove that no SSH activity occurred, since the conclusion is limited to the available logs and their coverage.

### 3.3 Persistence Analysis

The reviewed SUID/SGID files, cron entries, and autostart items appeared consistent with ordinary system components.

No confirmed malicious persistence mechanism was identified in the reviewed artifacts.

### 3.4 Process and Network Analysis

Network listeners and active connections were observed.

The collected information alone does not establish malicious network activity.

No confirmed malicious process or network indicator was established from the available evidence.

### 3.5 System Journal and Warnings

The journal contained several warnings and service-related issues, including:

- Bluetooth firmware loading errors.
- SSSD service dependency failures.
- NetworkManager warnings.
- Repeated firmware-updater service failures.
- ModemManager port-probing issues.
- Desktop-session and DBus warnings.
- A spice-vdagent configuration warning.

These events require technical review but do not independently demonstrate malicious activity.

The MMIO Stale Data CPU warning also requires attention through supported system updates and CPU microcode verification.

### 3.6 Journal Coverage and Timeline

The reviewed boot information included:

- Boot -15: October 3, 2026, to October 5, 2026.
- Boot -14: October 7, 2026, to October 8, 2026.

The evidence collection timestamp was:

`2026-10-08T01:43:55+01:00`

The requested 24-hour journal period began before the start of the reviewed October 7 boot.

This indicates that the requested period was not fully covered by the available boot records. The timeline is consistent with the system being unavailable during part of that period, but the journal alone cannot independently establish the exact physical power state or exclude all logging gaps.

Some journal entries occurred around the collection timestamp and are consistent with collection activity.

## 4. Evidence Integrity Validation

A total of 28 evidence files were compared against the SHA-256 manifest.

| Validation | Result |
|---|---:|
| Evidence files | 28 |
| Manifest entries | 28 |
| Missing files | 0 |
| Unlisted files | 0 |
| Files passing SHA-256 verification | 27 |
| Files failing SHA-256 verification | 1 |

The file `proof/apparmor.txt` failed SHA-256 verification.

Expected hash:

`45df5ad5e0ecfa54d3226343e0e6857337494ba6e32f189d1174070665d8c659`

Actual hash:

`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

The current file size is 0 bytes, indicating that it is empty.

A shell redirection command capable of truncating the file was previously executed. However, the exact cause and time of the original content loss cannot be conclusively established.

The original SHA-256 manifest was preserved and was not regenerated to conceal the mismatch.

**Integrity conclusion:** Inventory validation passed, but complete integrity verification failed because one artifact did not match its recorded hash.

The matching hashes of the other 27 files establish consistency with the manifest, but do not independently prove the authenticity of the original evidence.

## 5. Assessment

**Conclusion:**

No confirmed evidence of host compromise was established from the available evidence.

However, this conclusion does not prove that the system is completely clean.

**Confidence:**

Moderate, limited by:

- The point-in-time nature of the investigation.
- Journal coverage limitations.
- The documented recovery of apparmor.txt and the limitations of the original evidence metadata.
- The absence of independent corroboration for some observations.

## 6. Recommendations

1. Review and enable an appropriate UFW firewall policy.
2. Install supported security updates.
3. Verify CPU microcode status and address the MMIO Stale Data warning.
4. Investigate repeated firmware-updater failures.
5. Review AppArmor profiles operating in complain mode.
6. Investigate recurring authentication failures if additional events are identified.
7. Preserve the original evidence and manifest.
8. Perform future evidence collection using separate timestamped directories and verify hashes immediately after collection.

## 7. Final Conclusion

The investigation did not establish confirmed host compromise based on the available artifacts.

Several configuration and service issues require attention, particularly the inactive firewall and system warnings.

Evidence integrity verification initially identified one SHA-256 mismatch involving `apparmor.txt`. The file was subsequently restored from a separate local copy whose SHA-256 hash matched the value in the original manifest.

Following restoration, all 28 evidence files passed SHA-256 verification (28/28). The original manifest was not modified.

This confirms byte-level agreement with the recorded hashes after recovery. It does not independently establish the authenticity of the original evidence or restore the original metadata of the recovered file.

## 8. Evidence Recovery Record – AppArmor

During final integrity verification, `proof/apparmor.txt` was found empty and did not match its expected SHA-256 hash in the original evidence manifest.

The file content was restored from a separate local working copy. The recovered content was:

`active`

The recovered file's SHA-256 hash:

`45df5ad5e0ecfa54d3226343e0e6857337494ba6e32f189d1174070665d8c659`

This hash matches the original value recorded in `proof/evidence-sha256.txt`.

After recovery, all 28 evidence files passed SHA-256 verification (28/28). The original manifest remained unchanged.

**Forensic limitations:** The recovery restored content matching the hash recorded in the manifest. It did not restore the original file metadata. The recovery source and procedure are documented to preserve transparency about the evidence history.
