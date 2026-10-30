# Linux Security Evidence Analyzer

## Purpose

This tool analyzes a Linux security evidence file and extracts useful indicators for host investigation.

The analyzer focuses on:

* IP addresses
* Network ports
* Process IDs
* External TCP connections
* Listening services

## Input

The tool accepts a text-based evidence file as input.

Example:

```bash
./analyzer.py ../day1/evidence.txt
```

## Output

The tool produces a structured text report containing the extracted indicators.

The output can be redirected to a file:

```bash
./analyzer.py ../day1/evidence.txt > sample-output.txt
```

## Error Handling

The tool handles:

* Missing evidence files
* Invalid file paths
* File reading errors

Errors are printed to stderr and the program returns a non-zero exit code.

Example:

```bash
./analyzer.py does-not-exist.txt
```

Expected behavior:

```text
[ERROR] Evidence file not found: does-not-exist.txt
```

## Limitations

The analyzer is a lightweight evidence-extraction utility.

It does not determine by itself whether an indicator is malicious.

An IP address, port, process, or network connection requires contextual analysis before a security conclusion can be made.

The results represent the contents of the supplied evidence file and do not prove historical activity outside the collected evidence.

## Environment

* Linux
* Python 3
* Local authorized security lab

## Evidence Source

The primary input for this exercise is the network/process evidence collected during Day 1.

## Security Scope

All analysis was performed on an authorized local laboratory environment.
