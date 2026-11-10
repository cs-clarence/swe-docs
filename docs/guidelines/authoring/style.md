# Style

## Scope

Naming, readability, and consistency. Comments are in [comments](comments.md). Formatting details belong to the repository's formatter and linter.

## Guidelines

### Defer to automated tools

Use the repository's formatter and linter and do not argue style they settle. Do not hand-format against them.

### Match surrounding code

Follow the conventions of the file and module you are in. A consistent codebase is easier to read than one locally improved.

### Name for intent

Names should say what a thing is or does in domain terms, not how it is implemented. Use one word per concept and avoid abbreviations that are not universal.

### Keep control flow shallow

Prefer early returns and guard clauses over deep nesting. Split a unit when it needs a comment to separate its parts.

### Keep units small enough to hold in mind

A function or module should fit in a reader's head. Length alone is not the test; mixed levels of abstraction are.

### Replace magic values

Give unexplained literals a name or a documented source, unless the meaning is obvious (such as 0 or 1 in a counter).

### Remove dead code

Delete unused code, commented-out code, and stale flags. Version history keeps them.

## Examples

| Avoid | Prefer |
| --- | --- |
| `d = 86400` | `secondsPerDay = 86400` |

## Exceptions

Generated code and vendored third-party code keep their original style.
