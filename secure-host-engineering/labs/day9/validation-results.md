# Day 9 Detection Validation

## 1. Validation Objective

The objective was to validate that the automated detection utility can
process the collected telemetry, generate investigation indicators, and
support contextual investigation without treating every root process as
malicious.

## 2. Execution Validation

The detection utility passed Python syntax validation:

    python3 -m py_compile automated-detection.py

The detector executed successfully against:

    proof/current-telemetry.json

Final execution result:

    [INFO] 13 investigation indicator(s) generated.

## 3. Detection Result

The detector generated 13 DR-01 investigation indicators.

The initial version of the rule produced a high number of root-process
alerts. The rule was subsequently tuned to filter known kernel and
expected system processes.

This reduced the output from 180 initial indicators to 13 investigation
candidates.

## 4. Contextual Validation

The 13 indicators were manually reviewed.

Expected activity included:

- Linux kernel threads
- Linux graphics/kernel threads
- ModemManager
- VirtualBox-related thread activity
- GNOME display-manager session activity
- KVM/QEMU-related activity associated with the laboratory Windows VM

PID 13037 (psimon) could not be independently verified because the
process had exited before contextual examination.

## 5. False-Positive Assessment

The remaining indicators are not interpreted as confirmed malicious
activity.

The detector intentionally produces investigation candidates rather
than declaring compromise solely from process ownership or process name.

This reduces the risk of false conclusions from legitimate root-owned
Linux processes and kernel threads.

## 6. Security Controls

The validation does not establish that the host is fully protected.

In particular, UFW was previously observed to be installed but inactive.
Therefore, the analysis does not claim that UFW provided active network
firewall protection during the investigation.

## 7. Final Assessment

The detection pipeline is operational and produces explainable
investigation candidates.

No confirmed host compromise was established from the available evidence.

Confidence: Medium-High.

Limitations include point-in-time telemetry, incomplete historical
process/network visibility, and the inability to independently verify
the already-terminated PID 13037.
