# Risk Register

## Risk Scoring

Likelihood:
- 1 = Very Low
- 2 = Low
- 3 = Medium
- 4 = High
- 5 = Very High

Impact:
- 1 = Very Low
- 2 = Low
- 3 = Medium
- 4 = High
- 5 = Critical

Risk Score = Likelihood × Impact

## Risk Register

| ID | Threat | Likelihood | Impact | Score | Priority |
|----|--------|------------|--------|-------|----------|
| R1 | Compromise of privileged user account | 3 | 5 | 15 | High |
| R2 | Abuse of sudo privileges | 3 | 5 | 15 | High |
| R3 | Unauthorized systemd persistence | 3 | 5 | 15 | High |
| R4 | Unauthorized cron persistence | 2 | 5 | 10 | High |
| R5 | Vulnerable network service exposure | 2 | 5 | 10 | High |
| R6 | Credential or secret disclosure | 3 | 5 | 15 | High |
| R7 | Host/guest virtualization attack | 2 | 5 | 10 | High |
| R8 | Log tampering or evidence destruction | 2 | 4 | 8 | Medium |
| R9 | Malicious project/script modification | 2 | 4 | 8 | Medium |
| R10 | Resource exhaustion / denial of service | 3 | 3 | 9 | Medium |

## Highest-Priority Risks

The highest-priority risks are associated with:

1. Administrative privilege compromise
2. Unauthorized persistence
3. Credential and secret exposure
4. Network service exposure
5. Host/guest virtualization boundaries

## Important Limitation

These are threat-model risk estimates. They do not mean that the corresponding attacks were observed on the system.

The Days 1–4 investigation did not establish confirmed malicious activity.
