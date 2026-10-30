# Attack Surface

## Host Attack Surface

### 1. Administrative Privileges

The user account has sudo privileges.

Potential threat:
Unauthorized use of administrative privileges after account compromise.

### 2. SUID and SGID Programs

The host contains standard SUID and SGID executables.

Potential threat:
Abuse of a vulnerable privileged executable.

### 3. Enabled Services

The system contains numerous enabled systemd units.

Potential threat:
A vulnerable or incorrectly configured service could provide persistence or unauthorized access.

### 4. Cron

Cron directories and scheduled jobs provide automatic execution mechanisms.

Potential threat:
Unauthorized modification of scheduled jobs could establish persistence.

### 5. Systemd

systemd services, timers and other units can execute programs automatically.

Potential threat:
Unauthorized unit modification could establish persistent execution.

### 6. Network Services

The host contains local and network-related listeners associated with normal system and virtualization services.

Potential threat:
An exposed vulnerable service could provide an entry point.

### 7. QEMU/KVM and libvirt

The host runs a virtualized Windows laboratory environment.

Potential threat:
A compromised guest could attempt to cross the host/guest trust boundary.

### 8. Logs

Journald provides important forensic evidence.

Potential threat:
An attacker could attempt to delete, modify or avoid generating useful logs.

### 9. User Startup Mechanisms

Shell startup files and user autostart mechanisms may execute programs automatically.

Potential threat:
Unauthorized modification could establish user-level persistence.

### 10. Security Project Files

Python scripts and collected evidence are executed or processed locally.

Potential threat:
Modified scripts or evidence could affect analysis integrity.

## Important Observation

An attack surface represents potential exposure. Its presence does not prove that exploitation or malicious activity occurred.
