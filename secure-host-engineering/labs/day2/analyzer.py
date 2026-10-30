#!/usr/bin/env python3

import argparse
import re
import sys
from pathlib import Path


IP_PATTERN = re.compile(
    r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
)

PORT_PATTERN = re.compile(
    r':(\d{1,5})\b'
)

PID_PATTERN = re.compile(
    r'\bpid=(\d+)\b'
)


def validate_ip(ip):
    parts = ip.split(".")
    return (
        len(parts) == 4
        and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
    )


def analyze_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Evidence file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a regular file: {file_path}")

    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        raise OSError(f"Unable to read evidence file: {exc}")

    ips = sorted({
        ip for ip in IP_PATTERN.findall(content)
        if validate_ip(ip)
    })

    ports = sorted({
        int(port)
        for port in PORT_PATTERN.findall(content)
        if int(port) <= 65535
    })

    pids = sorted({
        int(pid)
        for pid in PID_PATTERN.findall(content)
    })

    external_connections = []

    for line in content.splitlines():
        if "tcp   ESTAB" in line:
            external_connections.append(line.strip())

    listening_services = []

    for line in content.splitlines():
        if "LISTEN" in line:
            listening_services.append(line.strip())

    return {
        "ips": ips,
        "ports": ports,
        "pids": pids,
        "external_connections": external_connections,
        "listening_services": listening_services,
    }


def print_report(results):
    print("=" * 60)
    print("Linux Security Evidence Analyzer")
    print("=" * 60)

    print("\n[+] IP Addresses")
    for ip in results["ips"]:
        print(f"    - {ip}")

    print("\n[+] Ports")
    for port in results["ports"]:
        print(f"    - {port}")

    print("\n[+] PIDs")
    for pid in results["pids"]:
        print(f"    - {pid}")

    print("\n[+] External TCP Connections")
    if results["external_connections"]:
        for connection in results["external_connections"]:
            print(f"    - {connection}")
    else:
        print("    - None found")

    print("\n[+] Listening Services")
    if results["listening_services"]:
        for service in results["listening_services"]:
            print(f"    - {service}")
    else:
        print("    - None found")

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze Linux security evidence."
    )

    parser.add_argument(
        "evidence",
        help="Path to evidence file"
    )

    args = parser.parse_args()

    try:
        results = analyze_file(args.evidence)
        print_report(results)

    except (FileNotFoundError, ValueError, OSError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
