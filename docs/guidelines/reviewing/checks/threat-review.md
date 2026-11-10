# Checks: threat review

For [high-tier](../../core/risk-tiers.md) changes that touch input, identity, access, secrets, or sensitive data. It adds a questioning pass on top of [security-and-privacy](security/security-and-privacy.md); it adds no rules. Tier = lowest risk tier at which to ask.

| Question | Rule | Tier |
| --- | --- | --- |
| What crosses a trust boundary, and who controls each input? | [identify trust boundaries](../../authoring/security/security-and-privacy.md#identify-trust-boundaries) | High |
| What is the worst an attacker can do with each input they control? | [keep data separate from commands](../../authoring/security/input-handling.md#keep-data-separate-from-commands) | High |
| Is authorization checked at the resource, for each action? | [enforce authorization at the resource](../../authoring/security/security-and-privacy.md#enforce-authorization-at-the-resource) | High |
| Is identity proven by a vetted mechanism, and can sessions be ended? | [expire and revoke sessions](../../authoring/security/authentication-and-sessions.md#expire-and-revoke-sessions) | High |
| Does each component hold only the access it needs? | [grant least privilege](../../authoring/security/security-and-privacy.md#grant-least-privilege) | High |
| Where are secrets and keys stored, rotated, and kept out of output? | [manage keys through their lifecycle](../../authoring/security/cryptography.md#manage-keys-through-their-lifecycle) | High |
| Which sensitive data is collected, how long is it kept, and how is it deleted? | [decide how long each kind of data is kept](../../authoring/security/data-retention-and-deletion.md#decide-how-long-each-kind-of-data-is-kept) | High |
| What happens when a dependency fails or is slow? Does it fail closed? | [degrade deliberately](../../authoring/resilience.md#degrade-deliberately) | High |
| Can an attacker exhaust resources through size, count, or rate? | [enforce limits on size depth and rate](../../authoring/security/input-handling.md#enforce-limits-on-size-depth-and-rate) | Medium |
| Would an operator see an attack in progress, without sensitive data in the logs? | [keep sensitive data out of telemetry](../../authoring/observability.md#keep-sensitive-data-out-of-telemetry) | Medium |
| Is anything unclear about security, and has it been surfaced rather than assumed safe? | [surface security uncertainty](../../authoring/security/security-and-privacy.md#surface-security-uncertainty) | High |

## Blocking

A question the author cannot answer is a blocking question, not a pass. Findings follow the classes in [process](../process.md#classify-each-finding).
