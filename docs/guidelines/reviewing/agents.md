# Reviewing agents

## Scope

Reviewing changes made by agents, and agents acting as reviewers. Also apply [process](process.md).

## Guidelines

### Verify, do not trust, agent claims

Check that stated results (tests pass, behavior works, files exist) are true. Agent summaries can be confidently wrong.

### Check scope

Confirm the change touches only what was requested and does not revert or reformat others' work ([authoring/agents](../authoring/agents.md#stay-within-the-request)).

### Check for fabrication

Verify that referenced APIs, functions, options, and sources exist and behave as described.

### Check that safeguards are intact

Look for disabled, deleted, or weakened tests, checks, and permissions ([never weaken a test](../authoring/testing/testing.md#never-weaken-a-test-to-pass)).

### Confirm limitations are reported

The change should state what was not done or verified. Treat missing limitations in a non-trivial change as a finding.

### Agent reviewers: state coverage

Say what you examined and what you did not. Never approve on the basis of the description alone.

### Agent reviewers: do not act beyond review

Report findings; do not modify the change or take other actions unless asked.

### Agent reviewers: cite evidence

Support each finding with the location and the rule or observed behavior. Mark uncertain findings as questions.
