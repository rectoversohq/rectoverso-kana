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

The previous folder must hold Japanese-Kana-en.apkg and Japanese-Kana-fr.apkg. The update preflight permits authored additions while requiring every existing GUID, note/card ID, study state and review-log entry to survive. The imported inventory must exactly match a fresh import of the new package, with one card per note. A second import must be idempotent. Version 0.2.0 checks the studied 290-question edition against the 292-question edition, adding exactly word-ai and word-kagu in each language. Existing Anki new-card queue positions are preserved; this does not reset a learner’s queue or options. RectoVerso’s reimport separately adopts the authored card order.

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


### 0.2.0 word recordings

The two new frozen sources are authored with the existing voice and processing settings:

```sh
python scripts/synthesize_audio.py --requests source/audio/requests-v02.json --cache /external/kana-provider-originals
```

Normal builds never synthesize audio. The 131 existing recordings and their provenance are unchanged; the two new files retain pending human listening review. All 668 existing rendered image records and geometry remain identical; only the two new words’ light/dark isolated figures are added to the artwork manifest. Those isolated word figures are review renders, not packaged word prompts.


### Isolated beginner trial

Use --beginner-trial to build the exact reviewed first 20 questions with separate study identities; see [trial setup and limits](beginner-trial.md). Both languages are checked by scripts/ci.py. The source guard checks actual kana in word/listening prompts and reading figures, but cannot override shuffled app entry points or enforce learner exposure.


### Gallery covers

The three compositions follow the owner’s selected order: **brush**, **stroke order**, then **reading reveal** (workshop studies 1–3–2). Each has a distinct light and dark version, shared by English and French: the kana, reading `i` and step numerals are teaching symbols rather than localized prose. The cover has no deck title.

Render the six self-contained masters, independently of any package or locally installed fonts:

```sh
python scripts/covers.py --output /external/kana-covers
python scripts/checks/verify-covers.py --output /external/kana-covers
```

Masters live in `artwork/covers/`, named `rv-kana[-<en|fr>]-cover[-<light|dark>]-<n>.svg`; the renderer writes the matching `.png` names. Omit a language when the artwork is shared by every shipped language. Omit an appearance only when the same artwork serves both modes. A localized cover needs every shipped language at the same number and appearance. Shared/localized numbers and shared/explicit appearances must not overlap.

The complete-package builder renders all six covers beside the APKG and its sidecar. Covers stay outside Anki’s card media and out of the repository; component previews and the isolated trial do not generate gallery covers. `scripts/ci.py` checks the two complete builds’ cover bytes independently, alongside the existing deck checks. The **Gallery covers** GitHub workflow runs the cover regressions without proprietary font inputs and attaches the six PNGs as `kana-covers`.

Every PNG is exactly 2,010 × 1,340 pixels, optimized below 400 KB for this set. CI checks filenames, language/appearance coverage, matching localized variants, unambiguous scopes and the language-pill corner (`x ≥ 1608`, `y ≤ 335`, within 4 per RGBA channel of that corner’s dominant color). Masters reject live text, external image/style references and a non-3:2 viewport. Their subject stays within the central crop safe area.

To regenerate the editable vector masters after an intentional design change, use the pinned font and authoring dependencies, render into a new external folder, review the results and then explicitly promote the SVGs and update the provenance hashes:

```sh
python scripts/make_cover_masters.py --output /external/kana-cover-master-candidates
```

Normal builds do not run this authoring command. No absolute workshop paths, app-checkout files, network requests or installed fonts are used by the production cover renderer. `artwork/cover-provenance.json` records all master hashes and inputs.

The brush artwork adapts **KanjiVG r20260714**, © Ulrich Apel, CC BY-SA 3.0: the source centerlines and stroke order for あ are frozen in `artwork/sources/kanjivg/a.json`, with the full attribution and license beside it. Covers 1 and 2 retain CC BY-SA 3.0 for those adaptations; their layout and brush treatment are original. Cover 3’s composition is © Simon Pinkas, CC BY 4.0. Its kana and the step/readout lettering are outlined from the checksum-pinned Noto Sans JP and SF Pro inputs described above; font software retains its own terms. No font binary is embedded in a cover.

The covers and build support do not approve a release or gallery pin. `rectoverso.json`, including publication status and gallery cover selection, remains unchanged by this work. The gallery/importer release gates already recorded in the review remain separate.

| Master | SHA-256 |
|---|---|
| [rv-kana-cover-dark-1.svg](../artwork/covers/rv-kana-cover-dark-1.svg) | `3447e0a19189ec4b98aadbfce22724bc40a57001fc9a32726e2066bd5da290f6` |
| [rv-kana-cover-dark-2.svg](../artwork/covers/rv-kana-cover-dark-2.svg) | `6101ff5ab3312a626497396411dcd7d940d02c4e97b56ecee2e32b04a400df21` |
| [rv-kana-cover-dark-3.svg](../artwork/covers/rv-kana-cover-dark-3.svg) | `61e75a450ec127c68f4531174ff05ce9ae2183db87314777342baa3240dae9bb` |
| [rv-kana-cover-light-1.svg](../artwork/covers/rv-kana-cover-light-1.svg) | `bafb930bd7d32e3baeb854e30e3e957b626093c28cb4383470aa71640a4cdd8e` |
| [rv-kana-cover-light-2.svg](../artwork/covers/rv-kana-cover-light-2.svg) | `246837af18d4220721265ffb73d5639f84c12a018dc3edc9306e0b0c1670a3e0` |
| [rv-kana-cover-light-3.svg](../artwork/covers/rv-kana-cover-light-3.svg) | `947dc93d3264b0caa47c42489c36f5f138993b8e643c65bd4e3f722dac2c381f` |
