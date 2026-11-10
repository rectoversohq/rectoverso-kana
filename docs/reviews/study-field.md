# Shared study preset

The owner requested migration to the contract implemented in app #823 / #805. Root rectoverso.json now declares the same `study` object for both languages:

```json
{"newCards":"deckOrder","newPerDay":6,"newPosition":"afterReviews"}
```

The former advisory studyRecommendations field is removed. Both language expansions and generated sidecars retain the supported field. Source checks refuse a missing/drifted preset, a non-integer daily limit or a leftover legacy field. All question content, note/model/field/template/deck identities, authored positions, pictures and audio remain unchanged from 5060cf4. The existing source dependency order still controls new introductions; due reviews retain FSRS scheduling. Six is a new-question limit across exercise types, not six new kana or a ten-minute guarantee.

## Validation

- Twenty source/unit cases pass, including three new metadata regressions.
- The actual Kana value passes app `scripts/gallery/decks.py::verify_study` at 082066ff80b4b0433f051de42cf6d8aa5434794f. Three production Python tests pass: valid/invalid study values, agreement with Core enums/ranges, and unchanged propagation to the catalog.
- All nine Core StudyPresetTests pass on that app branch, covering catalog reading, first-add application, learner-override preservation, saved records, authored import order, daily limits and reviews-first behavior. These are the app's tests; no app source was edited.
- Complete bilingual CI passes for both 290-question packages and fourteen components, including independent rendering/rebuilds and previous-edition import checks. Both final sidecars contain the exact study value and no legacy field. Semantic digests match the preceding editions: note/model/deck identities, question content, authored order and media are unchanged. The tested scheduling states and review logs survive update.

Separate Astra factual and pedagogy reviewers at high effort pass the source/contract change. The factual reviewer independently checked the exact app validator, both expansions and unchanged 290-note/model/deck/order data against 5060cf4. The pedagogy reviewer confirms the preset matches the approved plan without adding mastery gates or changing the completion goal. These are scoped source/contract reviews, not new native UI or publication approval.

## Application boundary

A supporting app takes these defaults on a fresh gallery addition and only where no learner options exist. Updates or putting a deck back retain saved options. Deleting a deck and its options, then adding it afresh, can apply the preset again. Direct APKG imports do not receive a gallery preset; the package currently on the owner's phone therefore keeps its existing options.

The prototype's manual setup copy remains applicable to direct file imports. Before gallery publication, its learner-facing wording needs owner review so the same guide is accurate after automatic setup. No headline, description or card guidance was changed in this metadata task.

Full gallery publication remains blocked by the already documented source/publication prerequisites and the existing library UUID assumption; targeted study checks passing does not make the complete gallery pipeline green. Existing native content evidence remains in the sound-player review; no new native preset walkthrough or phone import was performed here.

External evidence and rebuilt packages: `/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/study-field-20261108/`. No release, merge, gallery pin or phone setting was changed.
