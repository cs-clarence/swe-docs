# Choosing a type of document

## Scope

Which type of document to write. User-facing documents follow the Diátaxis model: four types, each serving one reader need. For developer-facing documents, see [developer-docs](developer-docs.md).

## Guidelines

### Choose the type by what the reader needs

Pick the type from the reader's need at that moment, not from the topic. The same feature usually needs several types.

| The reader wants to | Write a | Orientation |
| --- | --- | --- |
| Learn by doing, with no prior knowledge | [tutorial](tutorials.md) | Learning |
| Finish a specific task | [how-to guide](how-to-guides.md) | Task |
| Look up a fact | [reference](reference.md) | Information |
| Understand why or how something works | [explanation](explanation.md) | Understanding |
| Find out what a project is and where to start | [project README](project-readme.md) | Entry point |
| Learn what changed between versions | [release notes](release-notes.md) | Change |

### Keep each document to one type

A document serves one need. Mixing types, such as steps inside an explanation or background inside a how-to guide, serves neither reader. Move the other content to its own document and link to it.

### Link between types instead of mixing them

When a reader may need another type, link to it at the point where the need arises: a how-to guide links to the reference for its options and to the explanation for its reasons.

### Split a document that serves two needs

If a document's reader would skip half of it, or the named reader and purpose ([write for a named reader](documentation.md#write-for-a-named-reader)) cannot be one sentence, split it by type.

## Exceptions

A short project may combine types in a single README. Keep the sections separate and labelled so readers can find the one they need.
