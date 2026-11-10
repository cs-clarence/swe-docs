# Output handling

## Scope

Data a component sends out: to users, other systems, files, and logs. Counterpart of [input handling](input-handling.md).

## Guidelines

### Encode for the destination

Escape or encode data for the context it enters (markup, queries, shells, paths, logs), using the destination's own mechanism. One encoding does not fit all contexts.

### Encode at the point of output

Encode when writing, not when storing, so stored data stays raw and each output gets the right encoding.

### Do not echo untrusted data unmodified

Do not return input to a user or system without encoding it ([treat external input as untrusted](security-and-privacy.md#treat-external-input-as-untrusted)).

### Send only what the consumer needs

Limit output to the fields the consumer is entitled to and needs ([minimize sensitive data](security-and-privacy.md#minimize-sensitive-data)).

### Keep output format stable and declared

State the format, encoding, and character set of output, and keep them consistent ([interfaces](../interfaces-and-compatibility.md#keep-names-shapes-and-errors-consistent)).

## Exceptions

Output to a trusted, single-purpose destination may use its native format directly.
