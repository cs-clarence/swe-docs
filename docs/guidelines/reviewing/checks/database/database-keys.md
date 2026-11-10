# Checks: database keys

Verifies [authoring/database-keys](../../../authoring/database/database-keys.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each table have a stable primary key? | [give each table or collection a primary key](../../../authoring/database/database-keys.md#give-each-table-or-collection-a-primary-key) | Medium |
| Is the primary key surrogate, with natural keys as unique constraints? | [prefer surrogate keys unless the natural key is truly stable](../../../authoring/database/database-keys.md#prefer-surrogate-keys-unless-the-natural-key-is-truly-stable) | Medium |
| Are references declared with explicit delete behavior? | [declare relationships as foreign keys](../../../authoring/database/database-keys.md#declare-relationships-as-foreign-keys) | Medium |
| Are looked-up and joined keys indexed? | [index keys that are looked up and joined](../../../authoring/database/database-keys.md#index-keys-that-are-looked-up-and-joined) | Medium |
| Are published keys left unchanged? | [do not change a key once published](../../../authoring/database/database-keys.md#do-not-change-a-key-once-published) | High |

General key checks are in [identifiers-and-keys](../identifiers-and-keys.md).

## Blocking

Blocking: changing a published key without a migration plan. Others are should fix.
