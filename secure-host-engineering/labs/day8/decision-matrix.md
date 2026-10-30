# Investigation Decision Matrix

| Indicator | Evidence | Interpretation | Status |
|---|---|---|---|
| Unknown process | Process inventory | Requires process validation | Not confirmed |
| QEMU process | Day 3 process analysis | Expected laboratory virtualization | Benign/Expected |
| External network connection | Network evidence | Requires process/context correlation | Not confirmed malicious |
| SUID binaries | Privilege analysis | Normal Linux security mechanism unless abused | Not evidence of abuse |
| Enabled systemd units | Persistence analysis | Mostly expected system components | No suspicious persistence established |
| Timers | Day 4 | Maintenance/update/monitoring activity | Expected |
| Cron | Day 4 | Standard scheduled tasks | No suspicious persistence established |
| Authentication events | Logs | Requires contextual review | No confirmed compromise |
| AppArmor | Day 5/6 | Active security control | Positive control |
| Secure Boot | Day 6 | Enabled | Positive control |
| UFW | Day 5/6 | Installed but inactive | Hardening gap |
| Automated telemetry | Day 7 | Repeatable collection | Positive capability |

## Decision Rule

An indicator is not treated as malicious solely because it is unusual.

A stronger conclusion requires multiple correlated indicators or direct evidence.

Final classifications should be:

- Confirmed
- Suspicious
- Expected
- Unknown
- Not established
