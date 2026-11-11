# Developer docs

## Scope

Documents for people who change the code: contracts, structure, and reasons. Most of them live in the code. For user-facing documents, see [choosing-a-type](choosing-a-type.md).

## Guidelines

### Keep developer docs with the code

Put each document next to what it describes: doc comments on the element, a README in the module, decision records in the repository. Documents that live elsewhere are not updated with the code ([update docs in the same change as behavior](documentation.md#update-docs-in-the-same-change-as-behavior)).

### Write contracts as doc comments

Document public elements with doc comments, as in [document public contracts](../comments.md#document-public-contracts). The comment is the contract: it states purpose, inputs, outputs, errors, and guarantees.

### Write reference material in the code

Make doc comments and definitions the source for API reference, and generate user-facing [reference](reference.md) from them where possible. Writing a fact in the code and again in a document creates two sources. For products whose users see this material directly, see [treat in-code descriptions as the user's reference](reference.md#treat-in-code-descriptions-as-the-users-reference).

### Record why in decisions and design docs

Put reasons and rejected alternatives in a [decision record](../../core/decision-records.md) or [design doc](../../planning/design-docs.md), not in comments or scattered notes. Link to them from the code they explain.

### Give contributors a way in

Keep a short contributor document with how to set up, build, test, and follow conventions. Link to it from the [project README](project-readme.md), and keep its commands runnable ([make examples runnable](documentation.md#make-examples-runnable)).

### Describe structure for newcomers

Where a project has several modules, keep a short overview of what each does and how they relate, kept with the code and linking to module docs ([architecture](../structure/architecture.md)).

## Exceptions

Small projects may hold the contributor document and structure overview in the README.
