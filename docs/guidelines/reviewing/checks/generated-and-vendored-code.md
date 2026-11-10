# Checks: generated and vendored code

Verifies [authoring/generated-and-vendored-code](../../authoring/generated-and-vendored-code.md). Tier = lowest [risk tier](../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Are changes made in the source or generator, not the output? | [do not edit generated code by hand](../../authoring/generated-and-vendored-code.md#do-not-edit-generated-code-by-hand) | Medium |
| Do generated files say that they are generated and how to regenerate them? | [mark generated files](../../authoring/generated-and-vendored-code.md#mark-generated-files) | Low |
| Does regeneration give the same output from the same inputs? | [make generation reproducible](../../authoring/generated-and-vendored-code.md#make-generation-reproducible) | Medium |
| Is it stated whether generated output is kept or built? | [state whether generated output is committed](../../authoring/generated-and-vendored-code.md#state-whether-generated-output-is-committed) | Low |
| Was the generator input reviewed, not only its output? | [review the source of generation](../../authoring/generated-and-vendored-code.md#review-the-source-of-generation) | Medium |
| Is vendored code unmodified, or its patch recorded? | [keep vendored code unmodified](../../authoring/generated-and-vendored-code.md#keep-vendored-code-unmodified) | Medium |
| Are source, version, and license of vendored code recorded? | [record the origin of vendored code](../../authoring/generated-and-vendored-code.md#record-the-origin-of-vendored-code) | Medium |
| Are vendored updates handled like dependency updates? | [update vendored code deliberately](../../authoring/generated-and-vendored-code.md#update-vendored-code-deliberately) | Medium |

## Blocking

Blocking: hand edits to generated files that will be overwritten, and vendored code with unknown origin or license. Others are should fix.
