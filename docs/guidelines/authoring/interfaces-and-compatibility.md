# Interfaces and compatibility

## Scope

Changing anything others depend on: APIs, protocols, file formats, configuration, command-line interfaces. Includes network API design.

## Guidelines

### Treat published interfaces as promises

Assume consumers you cannot see depend on every observable behavior. Change it deliberately.

### Prefer additive changes

Add optional fields, parameters, or operations instead of changing existing ones. Existing consumers keep working.

### Mark breaking changes and give a migration path

Identify any change that breaks consumers, announce it, and say how to migrate. Surprise breakage costs consumers their time.

### Deprecate before removing

Mark the old form deprecated, say what replaces it and when it ends, then remove it. Consumers need time to move.

### Version what consumers pin

Give interfaces that consumers pin or negotiate a version, and keep supported versions working.

### Keep names, shapes, and errors consistent

Follow one convention for naming, pagination, identifiers, and error shapes across an interface ([contract](../core/glossary.md)).

### Make retried operations safe

Design operations that clients may retry so that repeating them gives the same result, or provide an idempotency key ([make cache and idempotency keys cover every input that changes the result](identifiers-and-keys.md#make-cache-and-idempotency-keys-cover-every-input-that-changes-the-result)).

## Exceptions

Interfaces with one known consumer, changed together, may skip deprecation; state this.
