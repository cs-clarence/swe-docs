# Checks: ui behavior

Verifies [authoring/ui-behavior](../../../authoring/ui/ui-behavior.md). Tier = lowest [risk tier](../../../core/risk-tiers.md) at which to check.

| Check | Rule | Tier |
| --- | --- | --- |
| Does each view handle loading, empty, error, and offline states? | [design every state, not only the loaded one](../../../authoring/ui/ui-behavior.md#design-every-state-not-only-the-loaded-one) | Medium |
| Does each action show progress and outcome? | [give feedback for every action](../../../authoring/ui/ui-behavior.md#give-feedback-for-every-action) | Medium |
| Can a repeated trigger cause a duplicate action? | [prevent duplicate submission](../../../authoring/ui/ui-behavior.md#prevent-duplicate-submission) | Medium |
| Does an error explain itself and keep the user's input? | [make failures recoverable](../../../authoring/ui/ui-behavior.md#make-failures-recoverable) | Medium |
| Are destructive actions undoable or confirmed? | [confirm destructive actions or make them undoable](../../../authoring/ui/ui-behavior.md#confirm-destructive-actions-or-make-them-undoable) | High |
| Does displayed data stay consistent after changes and concurrent edits? | [keep the screen consistent with the data](../../../authoring/ui/ui-behavior.md#keep-the-screen-consistent-with-the-data) | Medium |
| Is input validated early for the user and again at the boundary? | [validate input where the user can fix it](../../../authoring/ui/ui-behavior.md#validate-input-where-the-user-can-fix-it) | Medium |
| Does slow work avoid blocking interaction? | [keep the interface responsive](../../../authoring/ui/ui-behavior.md#keep-the-interface-responsive) | Medium |
| Is unsaved user input preserved or warned about? | [do not lose user work](../../../authoring/ui/ui-behavior.md#do-not-lose-user-work) | Medium |

## Blocking

Blocking: duplicate submission of a harmful action, silent loss of user data, and destructive actions with no undo or confirmation. Others are should fix.
