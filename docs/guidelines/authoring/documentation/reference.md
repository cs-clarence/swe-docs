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

### Treat in-code descriptions as the user's reference

For some products the interface the user sees is described in the code, and that description is the reference. Write it there, to the standard of any other reference, and publish or surface it from there.

| Product | Where the user-facing reference lives |
| --- | --- |
| Library | Doc comments on the public interface, published as API docs |
| Command-line tool | Built-in help for commands, options, and arguments, plus manual pages |
| HTTP or RPC API | Annotations or definitions that generate the API description (for example OpenAPI) |
| Configuration | Schema descriptions and defaults beside the settings |
| Graphical interface | Labels, hints, and error messages in the interface itself |

Check that the surfaced form is complete: the help output, generated site, or API description must show what the code states. Write guides, tutorials, and explanations as separate documents that link to it, or, where the reference has no link target (such as a graphical interface), tell the reader where to find it.

### Keep examples short

Add a short example only where an entry's use is not clear from its description ([make examples runnable](documentation.md#make-examples-runnable)). Longer examples belong in a guide.

## Exceptions

Interfaces that are small or short-lived may be described in one page by hand. Mark it as hand-written so readers know to check the source.
