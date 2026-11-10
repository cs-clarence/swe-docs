# Example override file

A sample of what a consuming repository might write in its own files. It is not shipped. Use the actions from [precedence](../../guidelines/core/precedence.md#overriding-rules).

```markdown
## Guideline overrides

- Tighten: `authoring/testing/testing.md#test-at-the-lowest-level-that-gives-confidence`. Every bug fix also needs an integration test.
- Relax: `authoring/comments.md#give-todos-a-handle`. We do not require an owner on TODOs. Reason: the issue tracker is the owner.
- Disable: `authoring/ui/accessibility-and-i18n.md`. Reason: command-line tool only.
- Add: all changes to `billing/` are High risk.
```
