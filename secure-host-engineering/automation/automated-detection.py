#!/usr/bin/env python3

import argparse
import json
from pathlib import Path


KNOWN_ROOT_PROCESSES = {
    "systemd",
    "systemd-journal",
    "systemd-udevd",
    "systemd-logind",
    "systemd-machine",
    "kthreadd",
    "ksoftirqd",
    "rcu_preempt",
    "rcu_exp_par_gp_",
    "rcu_exp_gp_kthr",
    "migration",
    "cpuhp",
    "idle_inject",
    "kworker",
    "kdevtmpfs",
    "kauditd",
    "khungtaskd",
    "oom_reaper",
    "kcompactd0",
    "ksmd",
    "khugepaged",
    "watchdogd",
    "jbd2",
    "scsi_eh",
    "irq",
    "hwrng",
    "NetworkManager",
    "wpa_supplicant",
    "bluetoothd",
    "chronyd-starter",
    "networkd-dispat",
    "snapd",
    "accounts-daemon",
    "switcheroo-cont",
    "thermald",
    "udisksd",
    "virtlockd",
    "virtlogd",
    "cupsd",
    "unattended-upgr",
    "cron",
    "libvirtd",
    "gdm3",
    "dnsmasq",
    "upowerd",
    "power-profiles-",
    "fusermount3",
    "fwupd",
}


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[ERROR] Cannot read {path}: {exc}")
        return None


def detect_security_controls(data):
    alerts = []

    controls = data.get("security_controls", {})

    if not isinstance(controls, dict):
        return alerts

    ufw = str(controls.get("ufw", "")).lower()

    if "inactive" in ufw:
        alerts.append(
            "DR-05: UFW is installed but currently inactive."
        )

    return alerts


def is_known_root_process(command):
    for known in KNOWN_ROOT_PROCESSES:
        if command == known or command.startswith(known):
            return True

    return False


def detect_processes(data):
    alerts = []

    process_section = data.get("processes", {})

    if not isinstance(process_section, dict):
        return alerts

    processes = process_section.get("processes", [])

    if not isinstance(processes, list):
        return alerts

    for proc in processes:

        if not isinstance(proc, dict):
            continue

        user = str(proc.get("user", ""))
        command = str(proc.get("command", ""))
        pid = str(proc.get("pid", ""))

        if user != "root" or not command:
            continue

        # Ignore expected kernel threads.
        if command.startswith(
            (
                "kworker",
                "ksoftirqd",
                "migration",
                "cpuhp",
                "rcu",
                "idle_inject",
                "irq/",
            )
        ):
            continue

        # Ignore known system processes.
        if is_known_root_process(command):
            continue

        alerts.append(
            f"DR-01: Unclassified root process: PID={pid}, command={command}"
        )

    return alerts


def detect_network(data):
    alerts = []

    network = data.get("network", {})

    entries = []

    if isinstance(network, dict):
        for value in network.values():
            if isinstance(value, list):
                entries.extend(value)

    elif isinstance(network, list):
        entries = network

    for entry in entries:

        if not isinstance(entry, dict):
            continue

        state = str(entry.get("state", "")).upper()

        if state == "LISTEN":
            alerts.append(
                f"DR-03: Listening socket observed: {entry}"
            )

    return alerts


def main():
    parser = argparse.ArgumentParser(
        description="Defensive Linux telemetry detection utility"
    )

    parser.add_argument(
        "telemetry",
        help="Path to security telemetry JSON"
    )

    args = parser.parse_args()

    telemetry_path = Path(args.telemetry)

    data = load_json(telemetry_path)

    if data is None:
        return 1

    alerts = []

    alerts.extend(detect_security_controls(data))
    alerts.extend(detect_processes(data))
    alerts.extend(detect_network(data))

    print("=== Day 9 Detection Results ===")
    print()

    if not alerts:
        print("[OK] No detection indicators generated.")
    else:
        print(
            f"[INFO] {len(alerts)} investigation indicator(s) generated."
        )
        print()

        for alert in alerts:
            print(f"[ALERT] {alert}")

    print()
    print("Classification note:")
    print("Detection indicators are investigation candidates.")
    print("Expected system and kernel processes are filtered.")
    print("They do not independently prove malicious activity.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
