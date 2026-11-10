# Checks: data and state

Verifies [authoring/data-and-state](../../../authoring/database/data-and-state.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does one component own writes to each piece of data? | [give each piece of data one owner](../../../authoring/database/data-and-state.md#give-each-piece-of-data-one-owner) | Medium |
| Is the migration idempotent or detectable, and free of partial results? | [make migrations safe to run and rerun](../../../authoring/database/data-and-state.md#make-migrations-safe-to-run-and-rerun) | High |
| Do old and new code both work during rollout? | [roll out in compatible steps](../../../authoring/database/data-and-state.md#roll-out-in-compatible-steps) | High |
| Is there a recovery path for deleted or overwritten data? | [protect existing data](../../../authoring/database/data-and-state.md#protect-existing-data) | High |
| Are invariants enforced in the store? | [enforce invariants where data lives](../../../authoring/database/data-and-state.md#enforce-invariants-where-data-lives) | Medium |
| Was the migration tried on realistic data? | [test migrations on realistic data](../../../authoring/database/data-and-state.md#test-migrations-on-realistic-data) | High |

## Blocking

Blocking: irreversible data loss without recovery, and migrations that break running versions. Others are should fix.
