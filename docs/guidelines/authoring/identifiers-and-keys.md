# Identifiers and keys

## Scope

Values that identify or look up things: entity identifiers, external references, cache, map, and idempotency keys, and similar values. Database keys are in [database-keys](database/database-keys.md). Cryptographic keys are in [cryptography](security/cryptography.md).

## Guidelines

### Give every entity a stable identifier

Identify each entity by a value that never changes and is never reused, even after deletion. Identifiers that change or get reused break references.

### Do not derive identity from mutable attributes

Do not use names, emails, titles, or positions as the identifier. They change, and then every reference must change too.

### Treat identifiers as opaque

Do not parse meaning out of an identifier or let consumers do so, unless the format is a published contract ([contract](../core/glossary.md)). Opaque identifiers can change format later.

### Choose the generation method deliberately

Pick between sequential, random, time-ordered, or content-derived identifiers by what you need: uniqueness across systems, ordering, unguessability, or deduplication. State the choice.

### Do not rely on guessability for access

Do not treat an unguessable identifier as authorization ([enforce authorization at the resource](security/security-and-privacy.md#enforce-authorization-at-the-resource)). Anyone who obtains it can use it.

### Do not leak information through identifiers

Avoid identifiers that expose counts, creation order, or personal data when that matters ([minimize sensitive data](security/security-and-privacy.md#minimize-sensitive-data)).

### Use one identifier form per entity across boundaries

Give an entity one external identifier and map internal ones to it at the boundary. Several forms for one thing cause mismatches.

### Define key behavior where keys are used

For any key (cache, map, lookup, idempotency, partition), state what it is made of, how it is normalized, and what happens on collision or absence ([canonicalize before checking](security/input-handling.md#canonicalize-before-checking)).

### Make cache and idempotency keys cover every input that changes the result

Include all inputs that affect the result, such as user, version, and parameters. A key missing one returns another caller's or an outdated result. For when operations need an idempotency key, see [make retried operations safe](interfaces-and-compatibility.md#make-retried-operations-safe).

## Examples

| Case | Handling |
| --- | --- |
| A cached response depends on user and language | The key includes both. A key of the path alone would serve one user another user's result. |
| A public link carries an order identifier | The server still checks the caller may see that order. |

## Exceptions

Small, private, short-lived data may use a natural key when it is stable for that lifetime; state it.
