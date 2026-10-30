# Cryptography Analysis

## 1. Purpose

Cryptography protects information against unauthorized disclosure and manipulation.

A secure system should use cryptography to provide:

- Confidentiality
- Integrity
- Authentication
- Non-repudiation where required

---

## 2. Confidentiality

Confidentiality prevents unauthorized users from reading sensitive information.

Examples:

- Encrypted network communication
- Encrypted storage
- Protected credentials
- Encrypted backups

For network communication, secure protocols such as TLS should be preferred over plaintext protocols.

---

## 3. Integrity

Integrity ensures that information has not been modified without authorization.

Examples:

- Cryptographic hashes
- Message authentication codes
- Digital signatures
- File integrity monitoring

A hash can be used to detect changes to evidence or configuration files.

---

## 4. Authentication

Cryptographic mechanisms can help verify the identity of users, systems and services.

Examples include:

- Certificates
- Public/private key authentication
- Digital signatures

---

## 5. Hashing vs Encryption

Hashing and encryption have different purposes.

### Hashing

A cryptographic hash is designed to produce a fixed-size representation of data.

Main use:

- Integrity verification

Hashing is not intended to be reversed into the original data.

### Encryption

Encryption transforms plaintext into ciphertext using a cryptographic key.

Main use:

- Confidentiality

Encrypted information can be decrypted by an authorized party with the appropriate key.

---

## 6. Key Management

Cryptographic security depends strongly on protecting keys.

Important principles:

1. Keys should not be hard-coded into source code.
2. Keys should not be stored in public repositories.
3. Access to keys should be limited.
4. Keys should be rotated when appropriate.
5. Key storage should be protected by appropriate access controls.

---

## 7. Cryptographic Requirements for the Project

The security engineering project should:

- Protect sensitive configuration.
- Protect credentials and secrets.
- Use secure network protocols.
- Verify the integrity of important evidence.
- Avoid storing cryptographic keys directly in source code.
- Protect private keys using appropriate permissions.

---

## 8. Security Principle

Cryptography should support the security architecture rather than replace access control, authentication, logging or monitoring.

A system can use strong encryption and still be insecure if keys or credentials are poorly protected.
