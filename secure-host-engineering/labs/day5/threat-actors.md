# Threat Actors

## TA1 — Malicious Local User

A user with access to the Linux system attempts to abuse available privileges.

Potential objectives:
- Privilege escalation
- Persistence
- Data access
- Log manipulation

## TA2 — Compromised User Account

An attacker obtains valid credentials or access to an existing user session.

Potential objectives:
- Execute commands
- Abuse sudo
- Access sensitive files
- Establish persistence

## TA3 — Malicious or Compromised Application

A downloaded or compromised application executes unwanted activity.

Potential objectives:
- Credential theft
- Persistence
- Network communication
- Privilege escalation

## TA4 — Remote Network Attacker

An attacker attempts to interact with network-accessible services.

Potential objectives:
- Exploit vulnerable services
- Obtain unauthorized access
- Denial of service

## TA5 — Compromised Virtual Machine

A compromised guest operating system attempts to interact with or attack the host.

Potential objectives:
- Attack virtualization interfaces
- Access shared resources
- Escape the guest security boundary

## TA6 — Supply-Chain or Update Compromise

A malicious or compromised package, dependency or update introduces unwanted behavior.

Potential objectives:
- Code execution
- Persistence
- Credential theft
- Long-term access
