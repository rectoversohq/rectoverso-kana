# Building the course

Install requirements.txt with Python 3.12. The shared interface is scripts/source_data.py::inputs(language), returning metadata, notes, models and deck. The builder uses Anki's backend. GUIDs, native book/card UUIDs, model IDs, field IDs, template IDs and source deck IDs stay stable. Isolated review components have separate preview identities from the combined course and the earlier phone prototype.

The reading artwork uses Noto Sans JP at weight 400 for kana and SF Pro Text Regular at 72 source pixels for romaji. Noto Serif JP and Yomogi remain limited to selected alternate-form examples. The bundled Japanese font masters retain their OFL notices.

Install SF Pro separately from https://developer.apple.com/fonts/ under Apple’s terms. The default input is /Library/Fonts/SF-Pro-Text-Regular.otf. For another location, set:

```sh
export RECTOVERSO_SF_PRO_FONT=/absolute/path/to/SF-Pro-Text-Regular.otf
```

The exact expected SHA-256 is eabf0a67833bbe3c80c800e6ce3f36b65e92f3b6ac1d6226ba2981e5cb3a74a5, recorded in artwork/fonts/provenance.json. A missing or different file fails validation; there is no font fallback. No SF Pro binary is downloaded by the build, committed, or included in the packages. The rendered mixed-font artwork is currently a local Apple-platform UI prototype; this does not claim publication clearance under Apple’s font terms.

Build and verify everything into a new external directory:

```sh
python scripts/ci.py --output /external/kana-ci
```

This checks source inventories, bilingual content, grouped listening forms, prerequisites, reverse-question spacing, unseen checkpoint words, source audio/font hashes and regression cases. It renders twice independently, compares the frozen artwork record, builds every component and both complete languages, then imports, renders, studies and reimports through Anki. Independent packages must preserve source content, schemas, source deck IDs, authored introduction order, media bytes and local study progress. APKG archive bytes may differ because Anki allocates local database timestamps/IDs; the semantic and media checks must match.

To build one component, choose reading, listening, rule, word, contrast, variant or checkpoint:

```sh
python scripts/render_artwork.py --output /external/kana-artwork
python scripts/build.py --language en --type listening --artwork /external/kana-artwork --out /external/review/Japanese-Kana-en-listening.apkg
python scripts/checks/validate-anki.py /external/review/Japanese-Kana-en-listening.apkg --output /external/review/evidence
```

Use fr for French. Omit --type and use Japanese-Kana-en.apkg or Japanese-Kana-fr.apkg for the complete course. The builder refuses paths inside the source checkout or an existing output package. No image, APKG, cache or provider-original recording is generated into source. artwork/artwork.json is the frozen, reviewed record of image names, geometry and hashes; the images themselves remain external.

Audio authoring is a separate online operation, never part of a package build:

```sh
python scripts/synthesize_audio.py --requests source/audio/requests-type-07.json --cache /external/provider-originals
```

It uses ja-JP-NanamiNeural at −20%, preserves provider originals externally, uses scripts/audio_processing.py to retain conservatively detected speech (-65 dBFS in 5 ms windows), with 40 ms lead and 75 ms tail, and applies constant gain toward -20 dBFS active RMS, capped at -3 dBFS peak and +10 dB gain. Speech is never time-stretched or pitch-shifted. The #826 preparation of the existing 131 frozen MP3s used their previous bytes, not a new synthesis: preparation826 records each previous SHA-256 and signal metadata; top-level hashes and signal fields describe the current file. Original inputs and before/after measurements are retained externally in builds/sound-player-826-20261108/audio/. Frozen input/hash disagreements fail instead of silently replacing an approved file. ffmpeg is needed only for authoring, not normal builds.

Native iPhone/Duo validation is separate from offline CI. The owner reauthorized simulator use on 2026-11-08. Respect the app repository's device locks and restore/shut down owned simulators afterward. Current coverage and limits are in docs/review.md; native evidence and replayable paths stay in the external output directory. Normal-size iPhone reveal/replay checks wait for the sheet animation before testing one ordinary answer scroll. The compact noteBody is emitted into native answer notes; body retains the full guide/reference text for documentation and descriptions. Source/build passes are not publication approval or native-speaker audio clearance.

Listening questions use a sound-only Front so RectoVerso classifies them as listening cards and applies Automatic prompt playback. Their question is Kicker; Meta is empty except for a grouped-answer hint. Anki’s existing question template renders the context and the sound. The regression and Anki checks enforce the one-sound Front and preserve comparison cards as text plus sound.

The owner-approved question player word is root playLabel: {"en": "Listen", "fr": "Écouter"}. App #826 reads it from the gallery catalog, not a standalone APKG import. Direct imports therefore retain the app’s Play / Lire fallback unless the deck already has a gallery origin. The answer player always uses the app’s Listen / Écouter.

When replacing recordings, advance contentModifiedAt and check against the previous packages (a retained external folder). Anki can rename a colliding media file and keep an old note when its modification time has not advanced. This check imports the old package, studies a card, imports the new package and compares every referenced sound’s bytes to a fresh import, while preserving all note/card IDs and study states:

```sh
python scripts/ci.py --output /external/kana-update-ci --previous /external/previous-packages
```

The previous folder must hold Japanese-Kana-en.apkg and Japanese-Kana-fr.apkg. This same-inventory preflight checks the existing course; deliberate inventory changes need a separate migration check.

The shared root `study` field follows app #823: `{"newCards":"deckOrder","newPerDay":4,"newPosition":"afterReviews"}`. Both expanded language sidecars carry this same value; `studyRecommendations` is removed. Source checks reject missing or drifted settings. Anki’s authored new-queue positions are unchanged. This is a gallery preset: the catalog carries it, and a supporting app applies it only on the first gallery add, preserving learner overrides thereafter. Direct APKG imports do not activate it; their existing manual setup guidance remains applicable.


### Gold-preserving reading crops (#830)

The owner chose cropped per-card figures rather than shared neutral tables. The renderer crops the original table to three complete 360-pixel rows, retaining its 38-pixel top padding, full 1,000-pixel width, gold target and font sizes. startRow is clamp(targetRow − 1, 0, 8), cropTop is startRow × 360, and height is 1,080. There are eleven occupied rows; ん/ン remain complete at row 10. No scaling is applied. The owner removed the underline because it could read as part of the kana; the gold glyph is retained.

Each of the 92 reading notes still has its own four files, named rv-kana-<target>-rows-<light|dark>-<source|clean>.png. The new rows names avoid Anki media collisions with older full-table files. The 700 × 500 question PNGs retain their names and bytes. Preparation regions and sibling masks include every kana visible in that crop, normalized to its dimensions, with the original script-global ordinals and hideAll. Each card/note, GUID, stage, batch, priority and authored due position stays separate.

The normal CI command rebuilds and validates these figures. Reading regressions cover sparse edge rows, all target/reading/ordinal/mask mappings, separate note/card identities and label fit. Anki checks verify the actual preparation asset hashes and dimensions; the previous-edition check also compares every referenced image’s bytes, alongside sound bytes and full study-history preservation. Existing collections can retain unused old full-table media; new packages include only cropped tables. Native checks require app PR #831 and remain separately reported.


### Kana-only answers and Romaji details (#832)

The 94 listening and 12 comparison answers put only their accepted kana in Back, followed by the unchanged sound token. Romaji is appended after the original eight fields; existing field, model and template IDs never move. The answer template conditionally renders a real **Explore** / **Explorer** input button opening a hidden **Romaji** detail. Both languages use the owner-approved label **Romaji**. Other question types leave that field empty.

Native-payload notes bypass the generic Anki details parser, so the same reading is also carried by the existing resources representation in the native payload. This is an answer resource, not a new stroke-data field or brush flag. In the app's Debug prototype, resources and the answer's sound control appear after the last stroke. The six shared-sound groups retain all accepted alternatives as ordinary text; no spelling is selected to force a single-character answer.

The normal CI checks all 106 affected notes in both languages. The previous-edition command above also permits exactly this approved trailing field addition, verifies that the updated answer template was adopted, and preserves the original schema identities, note/card IDs and studied state. [Brush review](reviews/brush-ready.md) records actual importer/native checks and the prototype's limited character coverage.


### Gentler introductions

The supported study preset starts at four new questions per day, after reviews and in deck order. Existing learner options survive updates; direct file imports need the manual settings in the learner guide. No automatic pace increase or mastery lock is encoded.

The full dependency-resolved curriculum pairs basic readings before their reverse questions, with at least one intervening question for each matching reverse. Every rolling four-question window contains at most two basic introductions. The grouped お／を and オ／ヲ answers wait for both spellings; an already-readable hiragana word supplies consolidation during the early katakana exception. IDs, answer sounds and question inventory stay unchanged.

The renderer computes each reading’s introduced-token set from the complete authored sequence before component filtering. Only that target and earlier same-script kana within its existing 1,000 × 1,080 frame are drawn or registered as regions. Future glyphs and readings are absent; unused row dividers disappear. Gold, font sizes, target boxes, global ordinals, hideAll and separate note/card identities remain. These are static introduction snapshots, not a learner-state-aware reference table. The new filenames use -introduced- instead of -rows- to avoid colliding with older stored media.

CI checks the rolling density, grouped prerequisites, exact visible masks/regions, empty future glyph/reading areas in every packaged table, and actual old-edition image adoption with history preservation. The original crop specification above describes the retained frame geometry; its former all-neighbor figure contents are superseded by this progressive visibility rule.
