# Sound-only listening questions

The owner’s decision in RectoVerso #824 is implemented in the deck. Each of the 94 listening questions in each language has exactly one sound tag in Front, its original script-specific question in Kicker, and an empty Meta except for the six grouped questions. Their hints are “Recall one valid form.” and “Une forme suffit.”. The redundant listening instruction is removed. Comparisons retain their text and sound.

Back, answer audio, Note, search metadata, GUIDs, card/book/model/field/template/deck identities, ordering, media bytes and every other question remain unchanged. Only contentModifiedAt advances in the package metadata. Anki’s existing template continues to render the question context and its audio.

## Evidence

- All 13 source/unit cases and complete CI pass: both 290-question packages, all fourteen review components, independent identical artwork renders, matching independent package semantics and actual study/reimport checks.
- An old-to-new upgrade studies an actual listening card and verifies every card’s identity and study state in each language. Precisely 94 notes change, only in Front/Kicker/Meta; the other 196 are identical. Every recording and picture remains byte-identical.
- All 94 imported listening-component cards per language satisfy RectoVerso’s listening predicate. Their saved settings contain no override, so Automatic applies. Audio diagnostics record recto playback without a play-button tap.
- The unmodified instruction-tip app branch at bc749279ed2a40bff59ba81e2b4ca4fd05d9f0e9 was built into an external folder. iPhone 17 at normal text size shows the 56pt primary button and the task on the tip, with the grouped hint only when appropriate. English/light and French/dark basic and grouped examples were inspected. The two recorded preview paths pass uninterrupted replay, eight and ten steps; their already-imported fixture requirement is explicit.
- Separate high-effort Astra factual and pedagogy reviews pass their source scopes. The pedagogy reviewer also approves the four inspected native presentations; this is not a pronunciation-quality claim.
- Anki backend preview rendering resolves one question AV tag for all 94 questions per language, and the English package imported as 290 notes in a separate native Anki QA profile. The owner explicitly left GUI playback pending after desktop automation could not reliably activate the preview; no manual listening claim is made. The isolated Kana listening QA profile remains available; the original User 1 collection was not edited.

## Gallery blocker

RectoVerso’s GalleryDeckTests fails at GalleryDeckTests.swift:63. It requires a library UUID derived from the numeric Anki deck ID, while AnkiImport preserves these packages’ unambiguous authored RectoVerso book UUID. The previously delivered English package fails at exactly the same assertion. This is a pre-existing mismatch between the test assumption and the importer’s payload-preservation behavior, not a listening-field regression. Identities remain unchanged. The test’s later checks did not execute; the gallery check is not reported as passing.

## Reproduce

Run python scripts/ci.py --output <new external folder>. External evidence is beside this checkout in builds/listening-sound-only-20261108: ci/result.json, source-delta.json, upgrade-verification.json, verify-upgrade.py, gallery-core.log, gallery-baseline.log, gallery-result.json and native/. Native README.txt documents fixture books and the two replayable paths. The raw walkthrough retains early failed import waits; it is not a passing replay.

The native build initially hit the full internal disk. Its temporary files and build output were placed on the SSD, and verified duplicate APKG staging files created by this work were removed from /tmp. Build and import proofs were then completed. No app source or other deck was edited. No release, gallery pin or physical-phone reimport is included.

| Input | SHA-256 |
| --- | --- |
| scripts/source_data.py | 4835142ae277d93532f502bbcfedf4ee2b64c121b75e4f433f9f563c8c2ae92f |
| source/languages/en.json | c279d80446ba9436b9128458b840f1d729baf3065a9b2d97e0b89302c53c71dc |
| source/languages/fr.json | b353b2ef4bbadfbed7faf921434151211a4020478208defd76bbc30140ec3ca1 |
| tests/test_course_contract.py | d37e3cea8855516c6f2ac105e73df23fc6fe860f87ab408c2732e69e31138a49 |
| scripts/checks/validate-anki.py | 99b2f9b38fdce4d67200897849214a284c02c7c378564df49bd21c8c51ccef0c |
| rectoverso.json | 39c755caf2009ff5742afba2f2b3fd53bff029d348aa5d02e54e6a623870ef52 |
