# Security and privacy

## Scope

Any change that handles external input, identity, access, secrets, or personal or sensitive data. Usually [high risk](../../core/risk-tiers.md).

## Guidelines

### Identify trust boundaries

Know where data and control cross between parties of different trust ([glossary](../../core/glossary.md)). Security decisions belong at those boundaries.

### Treat external input as untrusted

Validate it ([error-handling](../error-handling.md#validate-at-boundaries)) and encode or parameterize it for the context where it is used (queries, commands, markup, paths). Never build executable text from raw input.

### Enforce authorization at the resource

Check that the caller may perform this action on this resource, in the layer that owns the resource. Hiding an option in a client is not enforcement. Authentication does not imply authorization.

### Grant least privilege

Give code, services, and users only the access they need, for only as long as needed.

### Keep secrets out of code and history

Never commit credentials, keys, or tokens. Load them from a secure source at runtime. Treat an exposed secret as compromised and rotate it.

### Minimize sensitive data

Collect, store, and retain only what is needed. Prefer not holding it at all; protect what you must hold in transit and at rest.

### Keep sensitive data out of output

Do not put secrets or personal data in logs, errors, URLs, or analytics.

### Default to secure and closed

Defaults should be the safe option. On error or missing permission, deny.

### Use vetted libraries and protocols

Use established libraries and protocols for cryptography, authentication, and session handling. Do not invent your own.

### Surface security uncertainty

If you are unsure whether a change is safe, say so and treat it as high risk rather than assuming it is fine.

## Examples

| Avoid | Prefer |
| --- | --- |
| Concatenating input into a query | Parameterized query. |
| Checking only that the user is logged in | Checking the user may access this record. |
| Logging a full request including credentials | Logging identifiers and outcome only. |

## Exceptions

Local-only or throwaway code may relax hardening, but still must not contain real secrets or real personal data. State the assumption.
