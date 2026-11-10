# Data and state

## Scope

Persistent data, schemas, migrations, and shared state. In-memory state inside a component is in [design](../structure/design.md).

## Guidelines

### Give each piece of data one owner

Let one component own writes to a piece of data; others read through its interface. Shared writers corrupt invariants.

### Make migrations safe to run and rerun

Write migrations that are idempotent or detect completion, and that fail without leaving partial results.

### Roll out in compatible steps

Order changes so old and new code both work during rollout: add, then migrate, then remove. A single-step change breaks whatever still runs the old version.

### Protect existing data

Do not delete or overwrite data without a recovery path. State how to restore.

### Enforce invariants where data lives

Express constraints in the schema or store, not only in application code. Other writers bypass the code.

### Test migrations on realistic data

Run migrations against data shaped like production before relying on them.

## Exceptions

Disposable data (caches, test fixtures) needs no recovery path.
