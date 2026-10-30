# Linux Security Engineering Lab

## Environment
- **OS:** Ubuntu 26.04 LTS
- **Kernel:** 7.0.0-31-generic
- **Hostname:** imene-Aspire-A515-54
- **User:** imene

## Objectives
- System inventory
- Process investigation
- Privilege analysis
- Persistence investigation
- Timeline analysis

## Deliverables
- lab-inventory.md
- process-investigation.md
- evidence.txt
- privilege-lab.md
- proof/
- persistence-investigation.md
- timeline.csv
- analysis.md

## Scope
All investigation activities were performed on an authorized local Linux environment.
Target: imene-Aspire-A515-54 (Ubuntu 26.04 LTS)
Date: 2026-09-25 and 2026-09-30

## Status
Day 1 completed 
Day 2 completed 
Day 3 completed 
Day 4 completed 
Day 5 completed
Day 6 completed 

## Summary of Findings
- **System Inventory:** Collected OS, kernel, user, groups, disks, network, and services information.
- **Process Investigation:** Analyzed PID 3341 (xdg-document-portal). No network connections found.
- **Privilege Analysis:** Verified permissions, ownership, SUID/SGID files, and sudo access.
- **Persistence Investigation:** Checked systemd services, timers, cron jobs, and startup files. All normal.
- **Logs + Timeline:** Built a timeline of today's events using journalctl. No suspicious activity found.

## Conclusion
All lab tasks were completed successfully.No suspicious or malicious activity was identified in the collected evidence.
