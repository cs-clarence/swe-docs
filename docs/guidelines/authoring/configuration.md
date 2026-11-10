# Configuration

## Scope

Settings, defaults, environment differences, and feature flags.

## Guidelines

### Keep configuration out of code

Put values that vary by environment or deployment in configuration, not in code.

### Choose safe defaults

Default to the secure, least-surprising value, so omitting a setting is safe.

### Validate at startup

Check configuration when the program starts and fail with a clear message ([validate at boundaries](error-handling.md#validate-at-boundaries)).

### Keep secrets separate

Do not store secrets with ordinary configuration or in version history ([security-and-privacy](security/security-and-privacy.md)).

### Give flags an owner and an end

Name who removes each feature flag and when. Stale flags multiply code paths.

### Document each setting

State what each setting does, its default, and its allowed values.

## Exceptions

None.
