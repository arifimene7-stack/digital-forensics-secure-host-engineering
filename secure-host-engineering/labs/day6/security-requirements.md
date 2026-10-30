# Security Requirements

## Authentication

SR-01: Administrative functionality must require authentication.

SR-02: Authentication secrets must not be stored in source code.

## Authorization

SR-03: The service must operate using least privilege.

SR-04: Administrative operations must be restricted to authorized identities.

## Confidentiality

SR-05: Sensitive information must be protected from unauthorized access.

SR-06: Secrets must not be exposed through logs.

## Integrity

SR-07: Important configuration files must have restricted write access.

SR-08: Security-relevant evidence should support integrity verification.

## Input Security

SR-09: All external input must be validated.

SR-10: Input size and format must be restricted.

## Availability

SR-11: Resource consumption should be limited.

SR-12: Invalid requests should not crash the service.

## Logging

SR-13: Security-relevant events must be logged.

SR-14: Authentication and authorization failures must be detectable.

## Isolation

SR-15: The service should use a dedicated low-privilege account.

SR-16: Unnecessary filesystem and network access should be restricted.

## Cryptography

SR-17: Secure cryptographic protocols should be used for protected communications.

SR-18: Cryptographic keys must be protected separately from application source code.
