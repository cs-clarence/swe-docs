# Cryptography

## Scope

Using encryption, hashing, signatures, randomness, and keys. Where secrets live and the rule to use vetted libraries are in [security-and-privacy](security-and-privacy.md). Identifier keys are in [identifiers-and-keys](../identifiers-and-keys.md).

## Guidelines

### Never design your own cryptography

Use established algorithms through vetted libraries ([use vetted libraries and protocols](security-and-privacy.md#use-vetted-libraries-and-protocols)). Custom schemes fail in ways their authors cannot see.

### Choose the primitive for the goal

Pick by purpose: hashing for integrity, a keyed MAC or signature for authenticity, authenticated encryption for confidentiality, and a password-hashing function for passwords. The wrong tool gives a false sense of safety.

### Hash passwords with a slow, salted function

Store passwords only with a purpose-built password-hashing function and a unique salt. Never store them reversibly or with a fast general hash.

### Use authenticated encryption

Use modes that also verify integrity, and verify before using decrypted data. Unauthenticated encryption can be altered undetected.

### Generate randomness from a secure source

Use the platform's cryptographically secure generator for keys, tokens, nonces, and salts. General-purpose random functions are predictable.

### Never reuse a nonce or initialization value where it must be unique

Follow the algorithm's rule for nonces and initialization vectors. Reuse can reveal plaintext or keys.

### Compare secrets in constant time

Use a constant-time comparison for MACs, tokens, and hashes. Early-exit comparison leaks information through timing.

### Manage keys through their lifecycle

Generate, store, distribute, rotate, and retire keys deliberately. Keep them in a key store or secret manager, never in code ([keep secrets out of code and history](security-and-privacy.md#keep-secrets-out-of-code-and-history)), and give each purpose its own key.

### Plan for algorithm change

Record which algorithm and version protects each piece of data, so you can migrate when one is weakened ([roll out in compatible steps](../database/data-and-state.md#roll-out-in-compatible-steps)).

### Protect data in transit and at rest by default

Use current transport security for network traffic, and encrypt stored sensitive data where the risk calls for it ([minimize sensitive data](security-and-privacy.md#minimize-sensitive-data)). Verify certificates; do not disable verification.

### Do not use encoding or obfuscation as protection

Base64, compression, and obfuscation are not encryption. Anyone can reverse them.

## Examples

| Need | Use |
| --- | --- |
| Store a user password | A password-hashing function with a per-user salt. Not a general hash, not encryption. |
| Prove a message came from a service | A keyed MAC or a signature, verified with a constant-time comparison. |
| Keep a stored document confidential | Authenticated encryption with a managed key, plus a recorded algorithm version. |
| Create a session token | Bytes from the secure generator, long enough to be unguessable. |

## Exceptions

Non-security uses, such as a hash for cache keys or a random choice for load balancing, may use fast general-purpose functions. State that the use is not security-related.
