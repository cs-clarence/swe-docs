# Observability

## Scope

Logs, metrics, and traces that let operators see what a running system does. Failure behavior is in [error-handling](error-handling.md).

## Guidelines

### Emit what operators need to diagnose

Record significant events, failures, and decisions with enough context to trace one request or job.

### Use levels consistently

Use one meaning for each level, and reserve the highest for conditions that need action. Noisy logs hide real problems.

### Keep sensitive data out of telemetry

Do not log secrets or personal data ([security-and-privacy](security/security-and-privacy.md#keep-sensitive-data-out-of-output)).

### Use structured, correlatable output

Use fields and a correlation identifier rather than free text only, so events can be queried and joined.

### Do not let telemetry break the system

Bound volume and cost, and make telemetry failures non-fatal.

## Exceptions

Short-lived scripts may log to standard output only.
