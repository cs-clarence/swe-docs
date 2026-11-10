# Checks: cryptography

Verifies [authoring/cryptography](../../../authoring/security/cryptography.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Is cryptography done only with vetted libraries and standard algorithms? | [never design your own cryptography](../../../authoring/security/cryptography.md#never-design-your-own-cryptography) | High |
| Does each use match its goal (integrity, authenticity, confidentiality, passwords)? | [choose the primitive for the goal](../../../authoring/security/cryptography.md#choose-the-primitive-for-the-goal) | High |
| Are passwords stored with a slow, salted password hash? | [hash passwords with a slow, salted function](../../../authoring/security/cryptography.md#hash-passwords-with-a-slow-salted-function) | High |
| Is encryption authenticated and verified before use? | [use authenticated encryption](../../../authoring/security/cryptography.md#use-authenticated-encryption) | High |
| Is a cryptographically secure generator used for security values? | [generate randomness from a secure source](../../../authoring/security/cryptography.md#generate-randomness-from-a-secure-source) | High |
| Are nonces and initialization values used as the algorithm requires? | [never reuse a nonce or initialization value where it must be unique](../../../authoring/security/cryptography.md#never-reuse-a-nonce-or-initialization-value-where-it-must-be-unique) | High |
| Are secret values compared in constant time? | [compare secrets in constant time](../../../authoring/security/cryptography.md#compare-secrets-in-constant-time) | Medium |
| Do keys have a defined lifecycle, storage, and separate purposes? | [manage keys through their lifecycle](../../../authoring/security/cryptography.md#manage-keys-through-their-lifecycle) | High |
| Can the algorithm be replaced without breaking existing data? | [plan for algorithm change](../../../authoring/security/cryptography.md#plan-for-algorithm-change) | Medium |
| Is traffic protected with certificate verification enabled, and sensitive data encrypted where needed? | [protect data in transit and at rest by default](../../../authoring/security/cryptography.md#protect-data-in-transit-and-at-rest-by-default) | High |
| Is anything treated as protected that is only encoded or obfuscated? | [do not use encoding or obfuscation as protection](../../../authoring/security/cryptography.md#do-not-use-encoding-or-obfuscation-as-protection) | Medium |

## Blocking

Blocking: custom cryptography, reversible or fast-hashed passwords, predictable randomness for security values, disabled certificate verification, and keys in code. Others are should fix. Cryptography changes are High risk unless clearly non-security.
