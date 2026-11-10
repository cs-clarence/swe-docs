# Checks: identifiers and keys

Verifies [authoring/identifiers-and-keys](../../authoring/identifiers-and-keys.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each entity have a stable, never-reused identifier? | [give every entity a stable identifier](../../authoring/identifiers-and-keys.md#give-every-entity-a-stable-identifier) | Medium |
| Is identity independent of attributes that can change? | [do not derive identity from mutable attributes](../../authoring/identifiers-and-keys.md#do-not-derive-identity-from-mutable-attributes) | Medium |
| Do callers treat identifiers as opaque? | [treat identifiers as opaque](../../authoring/identifiers-and-keys.md#treat-identifiers-as-opaque) | Medium |
| Is the generation method chosen and stated for a reason? | [choose the generation method deliberately](../../authoring/identifiers-and-keys.md#choose-the-generation-method-deliberately) | Medium |
| Is access checked rather than assumed from an unguessable identifier? | [do not rely on guessability for access](../../authoring/identifiers-and-keys.md#do-not-rely-on-guessability-for-access) | High |
| Do identifiers avoid exposing counts, order, or personal data? | [do not leak information through identifiers](../../authoring/identifiers-and-keys.md#do-not-leak-information-through-identifiers) | Medium |
| Is there one external identifier per entity? | [use one identifier form per entity across boundaries](../../authoring/identifiers-and-keys.md#use-one-identifier-form-per-entity-across-boundaries) | Medium |
| Are key composition, normalization, and collisions defined? | [define key behavior where keys are used](../../authoring/identifiers-and-keys.md#define-key-behavior-where-keys-are-used) | Medium |
| Does the key include every input that changes the result? | [make cache and idempotency keys cover every input that changes the result](../../authoring/identifiers-and-keys.md#make-cache-and-idempotency-keys-cover-every-input-that-changes-the-result) | High |

## Blocking

Blocking: reused or changing identifiers that others reference, access granted by an unguessable identifier alone, and cache or idempotency keys that omit an input affecting the result. Others are should fix.
