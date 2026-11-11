# Reference

## Scope

Documents that describe facts for lookup: interfaces, commands, settings, formats, and errors. For instructions, see [how-to-guides](how-to-guides.md).

## Guidelines

### Describe, do not instruct

State what things are and do, neutrally and completely. Leave steps to [how-to guides](how-to-guides.md) and reasons to [explanation](explanation.md).

### Follow the structure of the thing described

Order and group entries as the interface itself is laid out, with the same names, so readers can find an entry by knowing the product.

### State the facts a caller needs

For each entry give its purpose, types or formats, defaults, limits, errors, and side effects. Mark what is required.

### Be complete and consistent

Cover every public entry in the same format. A gap makes readers doubt the rest.

### Generate from the source where possible

Build reference from the doc comments or definitions that already describe the interface ([link to facts instead of copying them](documentation.md#link-to-facts-instead-of-copying-them), [developer-docs](developer-docs.md#write-reference-material-in-the-code)). Hand-written copies drift.

### Keep examples short

Add a short example only where an entry's use is not clear from its description ([make examples runnable](documentation.md#make-examples-runnable)). Longer examples belong in a guide.

## Exceptions

Interfaces that are small or short-lived may be described in one page by hand. Mark it as hand-written so readers know to check the source.
