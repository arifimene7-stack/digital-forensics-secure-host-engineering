#!/usr/bin/env python3

import argparse
import json
import os
import platform
import socket
import subprocess
import sys
from datetime import datetime, timezone


def redact_text(text):
    """
    Redact common secret-like values before storing command output.
    """
    import re

    patterns = [
        (r'(?i)(password\s*[=:]\s*)\S+', r'\1[REDACTED]'),
        (r'(?i)(token\s*[=:]\s*)\S+', r'\1[REDACTED]'),
        (r'(?i)(secret\s*[=:]\s*)\S+', r'\1[REDACTED]'),
        (r'(?i)(api[_-]?key\s*[=:]\s*)\S+', r'\1[REDACTED]'),
    ]

    result = text

    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result)

    return result


def run_command(command, timeout=10):
    """
    Execute a local command safely without shell interpretation.
    """
    try:
        result = subprocess.run(
            command,
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )

        return {
            "command": command,
            "return_code": result.returncode,
            "stdout": redact_text(result.stdout),
            "stderr": redact_text(result.stderr)
        }

    except subprocess.TimeoutExpired:
        return {
            "command": command,
            "return_code": None,
            "stdout": "",
            "stderr": "Command timed out"
        }

    except Exception as exc:
        return {
            "command": command,
            "return_code": None,
            "stdout": "",
            "stderr": f"{type(exc).__name__}: {exc}"
        }


def collect_host():
    return {
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "kernel": platform.version(),
        "architecture": platform.machine(),
    }


def collect_identity():
    result = run_command(["id"])

    return {
        "id": result
    }


def collect_processes():
    result = run_command(
        [
            "ps",
            "-eo",
            "pid=,ppid=,user=,stat=,comm=,etimes="
        ]
    )

    processes = []

    if result["return_code"] == 0:
        for line in result["stdout"].splitlines():
            parts = line.split(None, 5)

            if len(parts) == 6:
                pid, ppid, user, state, command, elapsed = parts

                processes.append({
                    "pid": pid,
                    "ppid": ppid,
                    "user": user,
                    "state": state,
                    "command": command,
                    "elapsed_seconds": elapsed
                })

    return {
        "count": len(processes),
        "processes": processes,
        "collection": result
    }


def collect_network():
    listening = run_command(
        ["ss", "-H", "-lntup"]
    )

    connections = run_command(
        ["ss", "-H", "-antup"]
    )

    return {
        "listening": listening,
        "connections": connections
    }


def collect_persistence():
    enabled_units = run_command(
        [
            "systemctl",
            "list-unit-files",
            "--state=enabled"
        ]
    )

    timers = run_command(
        [
            "systemctl",
            "list-timers",
            "--all"
        ]
    )

    cron_directories = {}

    for directory in [
        "/etc/cron.d",
        "/etc/cron.daily",
        "/etc/cron.hourly",
        "/etc/cron.weekly",
        "/etc/cron.monthly"
    ]:
        try:
            cron_directories[directory] = sorted(
                os.listdir(directory)
            )
        except Exception as exc:
            cron_directories[directory] = {
                "error": f"{type(exc).__name__}: {exc}"
            }

    user_crontab = run_command(
        ["crontab", "-l"]
    )

    return {
        "enabled_units": enabled_units,
        "timers": timers,
        "cron_directories": cron_directories,
        "user_crontab": user_crontab
    }


def collect_privileged_binaries():
    directories = [
        "/usr/bin",
        "/usr/sbin",
        "/bin",
        "/sbin"
    ]

    findings = []

    for directory in directories:
        result = run_command(
            [
                "find",
                directory,
                "-xdev",
                "-type",
                "f",
                "-perm",
                "/6000",
                "-printf",
                "%m %u:%g %p\\n"
            ],
            timeout=20
        )

        if result["return_code"] == 0:
            findings.extend(
                line
                for line in result["stdout"].splitlines()
                if line.strip()
            )

    return {
        "count": len(findings),
        "files": sorted(set(findings))
    }


def collect_security_controls():
    apparmor = run_command(
        ["systemctl", "is-active", "apparmor"]
    )

    journald = run_command(
        ["systemctl", "is-active", "systemd-journald"]
    )

    unattended = run_command(
        ["systemctl", "is-active", "unattended-upgrades"]
    )

    secure_boot = run_command(
        ["mokutil", "--sb-state"]
    )

    ufw = run_command(
        ["ufw", "status"]
    )

    return {
        "apparmor": apparmor,
        "systemd_journald": journald,
        "unattended_upgrades": unattended,
        "secure_boot": secure_boot,
        "ufw": ufw
    }


def collect():
    return {
        "metadata": {
            "collector": "security_collector.py",
            "version": "1.0",
            "timestamp_utc": datetime.now(
                timezone.utc
            ).isoformat()
        },

        "host": collect_host(),
        "identity": collect_identity(),
        "processes": collect_processes(),
        "network": collect_network(),
        "persistence": collect_persistence(),
        "privileged_binaries": collect_privileged_binaries(),
        "security_controls": collect_security_controls()
    }


def main():
    parser = argparse.ArgumentParser(
        description="Local Linux security telemetry collector"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="proof/security-telemetry.json",
        help="Output JSON file"
    )

    parser.add_argument(
        "--pretty",
        action="store_true",
        help="Pretty-print JSON output"
    )

    args = parser.parse_args()

    try:
        data = collect()

        output_directory = os.path.dirname(
            os.path.abspath(args.output)
        )

        os.makedirs(
            output_directory,
            exist_ok=True
        )

        with open(
            args.output,
            "w",
            encoding="utf-8"
        ) as output_file:

            json.dump(
                data,
                output_file,
                indent=2 if args.pretty else None
            )

        # Telemetry can contain sensitive host information.
        try:
            os.chmod(args.output, 0o600)
        except OSError:
            pass

        print(
            f"[+] Collection completed: {args.output}"
        )

    except Exception as exc:
        print(
            f"[!] Collection failed: {type(exc).__name__}: {exc}",
            file=sys.stderr
        )

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
