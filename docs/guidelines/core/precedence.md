# Precedence and overrides

## Scope

Who decides when instructions differ, and how a repository customizes these guidelines.

## Order of precedence

Highest first:

1. Explicit instructions from the user or owner of the task.
2. The repository's own documentation and [overrides](#overriding-rules).
3. These guidelines.

Higher sources win. A higher source that is silent leaves lower ones in force.

## Overriding rules

This folder may be read-only for the consuming repository, so overrides live in the repository's own files, at a path it chooses and references from its existing instruction file. Overrides are optional; without them the baseline applies.

Each override names the rule (file and heading), an action, and a reason.

| Action | Effect |
| --- | --- |
| tighten | Stricter than baseline. |
| relax | Weaker than baseline (for example, must to should, or narrower scope). |
| replace | Different rule with the same intent. |
| disable | Rule does not apply in this repository. |
| add | Repository-specific rule; keep it in the repository's own docs. |

Example entry:

```
- rule: authoring/testing/testing.md#cover-regressions
  action: relax
  scope: generated/**                   # optional: paths or areas
  reason: generated code is verified by its generator's tests
  expires: when the generator is replaced   # optional
```

Constraints:

- An override states a reason. Silently ignoring a rule is a violation, not an override.
- Overrides change rule text only, not [glossary](glossary.md) terms or [tier](risk-tiers.md) definitions. Repositories may add tier criteria.
- State a one-off deviation for a single change in that change's description, with a reason. It needs no override.
- If an override links to a heading that no longer exists, treat it as stale and ask the repository owner to update it.

## Effective rules

Authors and agents follow the effective rule. Reviewers check against it. A disabled rule produces no findings.

## Conflicts

If two sources conflict and the right choice is unclear, do not pick silently. State the conflict and the choice made in the change description, or ask the user.

Repository docs should link to these guidelines rather than copy them.
