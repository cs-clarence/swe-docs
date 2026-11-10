# Database keys

## Scope

Primary, natural, and foreign keys in a database. General rules for identifiers and keys are in [identifiers-and-keys](../identifiers-and-keys.md) and apply here too.

## Guidelines

### Give each table or collection a primary key

Define a primary key that is unique, non-null, and stable ([give every entity a stable identifier](../identifiers-and-keys.md#give-every-entity-a-stable-identifier)).

### Prefer surrogate keys unless the natural key is truly stable

Use a generated key as the primary key, and keep natural keys as unique constraints. Natural keys such as emails and codes change in practice.

### Declare relationships as foreign keys

Express references with foreign keys where the store supports them, and decide delete behavior (restrict, cascade, or set null) explicitly ([enforce invariants where data lives](data-and-state.md#enforce-invariants-where-data-lives)).

### Index keys that are looked up and joined

Index foreign keys and lookup columns, and confirm with measurement ([measure before optimizing](../performance.md#measure-before-optimizing)).

### Do not change a key once published

Treat primary keys referenced elsewhere as promises. Changing them is a breaking migration ([roll out in compatible steps](data-and-state.md#roll-out-in-compatible-steps)).

## Examples

| Case | Handling |
| --- | --- |
| A user is looked up by email | Email is a unique constraint. The primary key is a generated identifier, so changing the email changes nothing else. |

## Exceptions

Small, private, short-lived data may use a natural key when it is stable for that lifetime; state it.
