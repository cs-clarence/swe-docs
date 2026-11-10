# Database and queries

## Scope

Designing, writing, and changing queries and the storage behind them. Migrations and invariants are in [data-and-state](data-and-state.md).

## Guidelines

### Select only what you need

Name the columns or fields and the rows required instead of fetching everything and filtering in code. Over-fetching wastes memory and breaks when columns are added.

### Avoid per-item queries

Fetch related data in bulk or by join instead of one query per item ([avoid known accidental costs](../performance.md#avoid-known-accidental-costs)). The cost grows with data and hides in tests.

### Back each query pattern with an index

Check that frequent and large-table queries use an index, using the query plan. Add an index for a pattern, not by guess, because indexes cost writes and space.

### Bound result sizes

Paginate or limit every query that can return many rows, and use stable ordering for pagination ([bound resource use](../performance.md#bound-resource-use)).

### Keep transactions short and scoped

Group what must succeed together, and keep out network calls and slow work. Long transactions hold locks and block others.

### Handle concurrent writes explicitly

Use constraints, optimistic version checks, or locks for read-modify-write, and handle the conflict ([shared state](../concurrency.md)).

### Pass values as parameters

Never build queries by concatenating input ([keep data separate from commands](../security/input-handling.md#keep-data-separate-from-commands)).

### Test queries against a real engine

Run them on the same database engine and realistic volume, not a fake that accepts different syntax ([check a fake against the real thing](../testing/test-doubles-and-data.md#check-a-fake-against-the-real-thing)).

### Make deletes and updates targeted and checkable

Scope them by key, check the affected count, and prefer a trial select first for bulk changes ([protect existing data](data-and-state.md#protect-existing-data)).

## Exceptions

Small, fixed-size tables may skip indexes and pagination. State the bound.
