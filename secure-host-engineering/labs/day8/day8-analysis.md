# Day 8 — Investigation Planning and Evidence Analysis

## Objective

The objective of Day 8 was to transform the collected Linux security telemetry into a structured investigation methodology.

## Work Completed

The investigation now includes:

1. Evidence inventory
2. Evidence map
3. Investigation plan
4. Hypothesis log
5. Investigation timeline
6. Decision matrix

## Investigation Method

The investigation follows:

Evidence → Correlation → Hypothesis → Test → Result → Confidence → Limitation

## Major Findings

The available evidence does not demonstrate a confirmed host compromise.

No clearly suspicious persistence mechanism was established.

No confirmed privilege abuse was identified.

No confirmed malicious network activity was established.

Virtualization-related QEMU activity is consistent with the laboratory environment.

## Security Control Finding

Secure Boot was enabled.

AppArmor was active.

Selected security services were active.

UFW was installed but inactive and therefore should not be treated as an active firewall control.

## Important Analytical Principle

Threat-model risks are not equivalent to observed incidents.

Likewise, individual processes, connections, SUID binaries, or persistence mechanisms should not be classified as malicious without contextual correlation.

## Confidence

Overall confidence is medium.

The evidence is sufficient to document the investigated state and to state that no compromise was demonstrated.

It is not sufficient to prove that compromise never occurred.

## Limitations

- Point-in-time observations
- Incomplete historical process visibility
- Limited historical network visibility
- Some commands may require elevated privileges
- Remote IP addresses were not independently attributed
- Guest activity cannot always be attributed from host-side QEMU evidence
- Timeline is not a complete forensic timeline

## Conclusion

Day 8 established a structured investigation workflow that can be reused for future host-compromise investigations.

The next phase should use this workflow to define detection logic, validate findings, automate selected detections, and produce the final investigation report.
