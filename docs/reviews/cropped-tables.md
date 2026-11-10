# Cropped kana tables: qualified factual and contract review

2026-11-08. Reviewed source commit `d141b6092c122c1a14890338ffcc01bc2f8170a3`. **Qualified PASS for content, crop geometry, data integrity and the tested update/import paths.** Accessibility wording and gallery checks remain unresolved. This report records evidence reviewed, not device actions performed by the factual reviewer.

The owner chose separate three-row figures for each reading card, retained the gold target glyph, and subsequently removed its underline. The implementation keeps the 1,000-pixel width and original font sizes, cropping to 1,080 pixels high without resampling. With eleven occupied rows (0–10), `startRow = clamp(targetRow − 1, 0, 8)` and `cropTop = startRow × 360` retain the 38-pixel top margin and complete visible kana/readings, including ん/ン. There are 92 distinct reading notes/cards/preparations, 368 cropped table PNGs (four per card), and 92 unchanged 700×500 question PNGs. Each crop contains 8, 10, 13 or 15 regions, with all other visible regions as hideAll siblings. Original script-global ordinals remain unchanged by explicit owner instruction.

The course remains 290 questions per language: 92 reading, 94 listening, 34 rules, 36 words, 12 comparisons, eight variants and 14 checkpoints. All GUIDs, native card/note identities, schemas, introduction order, Japanese mappings, answers and audio references remain stable. Only reading figure payloads change; all 198 non-reading notes are unchanged. The full renderer produces 668 assets; each combined package references 468 PNGs and 131 MP3s.

[Pixel comparison](../../../builds/cropped-tables-830-20261108/artwork-comparison.json) covers every one of the 368 table images: each equals the corresponding old-image crop except for removal of the underline. It also verifies 92 byte-identical standalone questions, unchanged non-reading figure records, and source/clean differences confined to visible pronunciation masks. The four uncompressed RGBA table images per card decrease from 64,800,000 to 17,280,000 bytes (73.33%); this is a pixel-storage calculation, not measured app memory usage.

[Final CI](../../../builds/cropped-tables-830-20261108/ci-final/result.json) and [fresh-clone CI](../../../builds/cropped-tables-830-20261108/fresh-clone-ci/result.json) pass. Their logs record 25 passing unit tests, both combined languages and all 14 components, Anki import/render/media/study/reimport checks, independent byte-identical artwork and matching package semantics. [EN update](../../../builds/cropped-tables-830-20261108/ci-final/evidence/en-edition-update.json) and [FR update](../../../builds/cropped-tables-830-20261108/ci-final/evidence/fr-edition-update.json) verify actual referenced image/audio bytes, all 92 preparation asset hashes, identities, scheduling fields including stored FSRS data, and every review-log row after old→new import. These claims apply to the tested import–study–update scenarios. New `-rows-` filenames avoid old table collisions; unused old files may remain in existing collections.

[Package records](../../../builds/cropped-tables-830-20261108/packages.json), independently checked against the actual files:

| Edition | Current bytes | Previous bytes | SHA-256 |
| --- | ---: | ---: | --- |
| EN | 15,658,223 | 48,721,793 | `8387c2acea659a6b5666c5b017a5200ac03056bffb3c14ede50c07ea4cc44786` |
| FR | 15,658,716 | 48,722,610 | `ac899ed7ee24dd55752d219293b04bba2fdca366214a1f2019156429902f57e2` |

[Native import](../../../builds/cropped-tables-830-20261108/native/import.json) records actual simulator imports of EN/iPhone and FR/Duo, each with 290 cards and all 92 cropped preparations validated against actual image hashes. The app build was PR #831 head `1f8655d`; the saved executable SHA-256 was independently verified as `99b7d58279a90a49ba329711c3ea3a7a751ef06451f8fc8e7963b6d2079bcd34`.

The live EN full-course Practice run reached 32 cards and Undo. Saved [positions 2–32](../../../builds/cropped-tables-830-20261108/native/practice/) all report the full-window canvas `[0,0,1,1]`; [Undo](../../../builds/cropped-tables-830-20261108/native/practice/iphone-undo-ax.txt) returns to 31 of 92 with that frame. All 13 saved [matrix cases](../../../builds/cropped-tables-830-20261108/native/matrix/) report full-window canvases: FR Duo closed/open in light/dark and selected EN iPhone light/dark targets. The pedagogy reviewer qualifiedly passed sampled target visibility/concealment and the correct ヨ → yo reveal. These are sampled visual/frame checks, not VoiceOver approval.

A confirmed accessibility defect requires app follow-up: the spoken summary combines cropped label counts with retained global ordinals (for example, “15 labels, the 17th masked” for ち). Preserve the source ordinals as instructed; the app should describe position within the visible crop or omit that ordinal. Canvas validation does not resolve this defect.

Gallery validation remains blocked: [metadata preflight](../../../builds/cropped-tables-830-20261108/gallery/metadata.json) correctly refuses `publication.approved=false`; [EN](../../../builds/cropped-tables-830-20261108/gallery/en.log) and [FR](../../../builds/cropped-tables-830-20261108/gallery/fr.log) Core tests stop at `GalleryDeckTests.swift:63`, whose Anki-deck-derived UUID assumption conflicts with the preserved authored book UUID. Later checks in that test are therefore not established.

**E2E replay:** the root reviewer reports the iPhone Practice/Undo replay passed all 177 steps after increasing the import wait from five to 30 seconds; the Duo canvas/reveal replay passed 32 steps. The first iPhone failure is retained and showed saving 576 of 600 files. Root follow-up: the additional iPhone matrix replay also passed all 12 steps. Do not equate replay steps with reviewed cards. The root reviewer investigated idle warnings through [saved image differences](../../../builds/cropped-tables-830-20261108/native/idle-diff/): 0.04% of pixels changed at the status clock and lit button edge, with no chart/target changes; a search warning involved the active caret and was followed by exact query/count/menu assertions. Replays reset appearance to light; dark-mode evidence comes from the saved matrix screenshots, not automated dark-appearance replay. No physical-device or memory-pressure reproduction, release, gallery pin or physical-phone installation is claimed. Native-speaker/audio listening clearance remains pending.

Reviewed source/artifact hashes:

| File | SHA-256 |
| --- | --- |
| `scripts/render_artwork.py` | `794bd9fc587e285f251efdaa2dd7f24a20e974ef32ff1c24b6b8afba42f67e00` |
| `artwork/artwork.json` | `9bf0861aba0c9be452c631f12a654abb50a2ba4a378765ebbea4c633747114b2` |
| `scripts/checks/validate-update.py` | `314b8dc8d0fc1f604c7516d64633e060d22fb1f982b907d24a8c8d7ebe4b27f4` |

The frozen manifest and all 668 final-CI artwork hashes were independently checked. No implementation or app files were edited by this reviewer.
