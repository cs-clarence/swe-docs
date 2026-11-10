# Checks: database and queries

Verifies [authoring/database-and-queries](../../../authoring/database/database-and-queries.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Do queries fetch only the needed fields and rows? | [select only what you need](../../../authoring/database/database-and-queries.md#select-only-what-you-need) | Medium |
| Is there a query per item in a loop? | [avoid per-item queries](../../../authoring/database/database-and-queries.md#avoid-per-item-queries) | Medium |
| Does the query plan show index use for frequent or large queries? | [back each query pattern with an index](../../../authoring/database/database-and-queries.md#back-each-query-pattern-with-an-index) | Medium |
| Is every potentially large result limited and stably ordered? | [bound result sizes](../../../authoring/database/database-and-queries.md#bound-result-sizes) | High |
| Are transactions scoped to what must be atomic and free of slow work? | [keep transactions short and scoped](../../../authoring/database/database-and-queries.md#keep-transactions-short-and-scoped) | High |
| Is read-modify-write protected against concurrent change? | [handle concurrent writes explicitly](../../../authoring/database/database-and-queries.md#handle-concurrent-writes-explicitly) | High |
| Are all values parameterized? | [pass values as parameters](../../../authoring/database/database-and-queries.md#pass-values-as-parameters) | High |
| Are queries tested on the real engine with realistic data? | [test queries against a real engine](../../../authoring/database/database-and-queries.md#test-queries-against-a-real-engine) | Medium |
| Is the scope of bulk updates and deletes checked? | [make deletes and updates targeted and checkable](../../../authoring/database/database-and-queries.md#make-deletes-and-updates-targeted-and-checkable) | High |

## Blocking

Blocking: unparameterized input, unbounded results on growing data, and unscoped bulk deletes or updates. Others are should fix.
