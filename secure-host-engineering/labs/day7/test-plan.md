# Security Collector Test Plan

## Test 1 — Python Syntax

Command:

python3 -m py_compile security_collector.py

Expected result:

No syntax errors and exit code 0.

## Test 2 — CLI Help

Command:

python3 security_collector.py --help

Expected result:

The command displays usage information and exits successfully.

## Test 3 — Live Collection

Command:

python3 security_collector.py --pretty

Expected result:

A JSON telemetry file is created.

## Test 4 — JSON Validation

Command:

python3 -m json.tool proof/security-telemetry.json

Expected result:

The JSON document is valid.

## Test 5 — Secret Scan

Command:

grep -Ein "password|passwd|token|secret|api[_-]?key" proof/security-telemetry.json

Expected result:

No actual credentials or secrets are stored.

## Test 6 — Unit Tests

Command:

python3 -m unittest -v test_collector.py

Expected result:

All tests pass.

## Test 7 — Output Permissions

Command:

stat -c '%A %a %U:%G %n' proof/security-telemetry.json

Expected result:

The output is restricted to the owner where supported.

## Test 8 — Repeated Collection

Command:

python3 security_collector.py --pretty -o proof/security-telemetry-second.json

Expected result:

A second valid JSON telemetry file is created without modifying the Python source.
