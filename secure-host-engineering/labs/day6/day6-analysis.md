# Day 6 — Cryptography, Secrets and Secure Service Design

## 1. Objective

Day 6 translates the Day 5 threat model into concrete security engineering requirements.

The focus is:

- Cryptography
- Secrets management
- Secure service design
- Security requirements
- Security telemetry

---

## 2. Cryptography

Cryptography provides mechanisms for:

- Confidentiality
- Integrity
- Authentication
- Digital signatures where required

The design distinguishes encryption from hashing.

Encryption primarily protects confidentiality.

Hashing primarily supports integrity verification.

---

## 3. Secrets

Sensitive credentials and cryptographic keys require special protection.

The design prohibits:

- Hard-coded credentials
- Secrets in source code
- Secrets in public repositories
- Secrets in normal logs

Least privilege and appropriate access controls should be applied to secret storage.

---

## 4. Secure Service Design

The proposed telemetry service should:

- Run with least privilege.
- Validate input.
- Protect configuration.
- Restrict filesystem access.
- Restrict unnecessary network access.
- Log security-relevant events.
- Avoid exposing secrets.
- Limit resource consumption.
- Fail safely.

---

## 5. Security Telemetry

The telemetry architecture correlates:

Process
+
Identity
+
Privilege
+
Network
+
Persistence
+
Logs

This provides a stronger basis for detection than isolated indicators.

---

## 6. Security Architecture

The conceptual architecture is:

Client
  |
  v
Authentication
  |
  v
Authorization
  |
  v
Input Validation
  |
  v
Service Logic
  |
  +---- Protected Storage
  |
  +---- Security Logging

The host security layer additionally provides:

- AppArmor
- systemd
- journald
- Secure Boot
- Least privilege
- Network controls

---

## 7. Validation

The host provides real security mechanisms that can support the design.

AppArmor is active.

systemd-journald is active.

Automatic update mechanisms are active.

Secure Boot is enabled.

OpenSSL is available for cryptographic operations.

The current UFW state remains inactive, so network protection should not be assumed from UFW alone.

---

## 8. Relationship to Day 5

Day 5 identified the main threats:

- Privilege compromise
- Persistence
- Credential disclosure
- Network exposure
- Host/guest boundary attacks

Day 6 translates these threats into engineering controls:

| Day 5 Threat | Day 6 Response |
|--------------|----------------|
| Privilege compromise | Least privilege |
| Persistence | Configuration monitoring |
| Credential disclosure | Secrets management |
| Network exposure | Secure communication + restricted access |
| Tampering | Integrity monitoring |
| Information disclosure | Encryption + access control |
| DoS | Resource limits |
| Poor detection | Security telemetry |

---

## 9. Limitations

This day focuses on security architecture and design.

It does not prove that a proposed service is secure in production.

A real implementation would require:

- Secure coding
- Automated tests
- Configuration testing
- Dependency analysis
- Runtime testing
- Security review

These activities will be addressed in later tasks.

---

## 10. Final Assessment

The threat model from Day 5 can be converted into concrete engineering requirements.

The most important principles are:

1. Least privilege
2. Strong authentication and authorization
3. Protected secrets
4. Secure cryptography
5. Input validation
6. Process isolation
7. Security logging
8. Telemetry correlation
9. Resource protection
10. Defense in depth

## Status

Day 6: COMPLETED
