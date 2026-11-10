# Agents

## Scope

Additional rules for AI or automated agents authoring changes. Agents also follow every other authoring guideline and [precedence](../core/precedence.md), including [check local rules first](approach.md#check-local-rules-first) and [define the scope](approach.md#define-the-scope) (ask or state assumptions).

## Guidelines

### Stay within the request

Do only what was asked. Note out-of-scope problems; do not fix them uninvited ([separate unrelated work](approach.md#separate-unrelated-work)).

### Preserve unrelated work

Do not revert, overwrite, or reformat changes you did not make. Treat unfamiliar files and uncommitted changes as someone's work, and investigate before touching them.

### Get authorization for destructive or irreversible actions

Deleting data, rewriting history, running costly or external operations, or changing shared systems requires explicit approval. A general task request is not approval.

### Do not bypass safeguards

Do not disable tests, linters, hooks, or permissions to get a result. If a safeguard blocks you, report it.

### Verify, then claim

Run the checks that apply ([approach](approach.md#verify-the-result)) and base claims on their results. Never state that something works, passes, or exists without having observed it.

### Do not fabricate

Do not invent APIs, files, results, or sources. If you cannot confirm something, say so.

### Report limitations

Close with the [result explanation](approach.md#explain-the-result), including what was not done or is uncertain. Add any conflict between instructions and which you followed.

### Keep secrets out of reach

Do not copy secrets or personal data into code, logs, outputs, or external services ([security-and-privacy](security/security-and-privacy.md)).

## Exceptions

If the user explicitly authorizes an action a rule here restricts, follow the user and state what you did.
