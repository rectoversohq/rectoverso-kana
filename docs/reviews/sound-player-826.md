# Sound player adaptation (#824 / #826)

The owner chose **Listen / Écouter** for Kana’s question player. Root `playLabel` carries both words. The existing 94 listening questions remain sound-only Front, their script-specific question in Kicker, and a one-form hint in Meta on exactly six grouped items per language. Twelve comparison questions retain their text and recording. All 290 notes, answers, search data, identities and authored order are unchanged from the sound-only revision.

## Audio

All 131 frozen Nanami −20% MP3s were prepared from their existing bytes, without contacting a synthesis service. `scripts/audio_processing.py` conservatively finds activity at −65 dBFS in 5 ms windows, retains a contiguous segment including internal pauses, adds 40 ms lead / 75 ms tail and applies constant gain toward −20 dBFS active RMS, with a −3 dBFS peak ceiling and +10 dB gain cap. It never stretches speech or shifts pitch. Future audio authoring uses the same helper; normal builds remain offline and require no ffmpeg.

Decoded outputs measure 35–45 ms lead, 70–90 ms tail, active RMS −20.636…−20.175 dBFS and peaks no higher than −6.767 dBFS. MP3 encoding means the target level is not exact. Very short kana still have a few flat waveform dots: the retained tail is about 75 ms, not zero. Each current hash and signal record describes the current bytes; `preparation826.inputSHA256` and `inputProvenance` retain the former hash and preparation. Original recordings, encoder version and complete before/after 22-bar measurements are external under `builds/sound-player-826-20261108/audio/` beside this checkout.

Separate high-effort Astra factual and pedagogy reviewers qualifiedly pass this source change. The factual reviewer independently decoded every original/output pair: the loudest discarded 5 ms window was −71.97 dBFS and maximum discarded energy 0.0000283%; no signal-based truncation blocker was found. These measurements and preserved TTS inputs are not human pronunciation/listening approval. Existing pending listening and publication status remain pending.

## Checks

- Seventeen source/unit cases pass, including quiet consonants, internal pauses, invalid/silent input, padding, exact owner labels and listening/contrast field rules.
- Complete bilingual CI (final run with `--previous` against the preceding editions) passes: both 290-question packages, fourteen components, independent artwork/package rebuilds, Anki media/render/preview hooks and actual study/reimport checks. Original-to-revised imports preserve every studied state and identity in both languages; the only changed package media are the 131 MP3s. All pictures and note content remain identical.
- #826’s two Python play-label validator tests and four Core PlayLabel tests pass. Its catalog generator retains the exact owner words.
- The full Core gallery package check remains blocked at `GalleryDeckTests.swift:63`: it assumes a library UUID derived from Anki’s numeric deck ID, whereas the importer preserves Kana’s authored RectoVerso book UUID. Revised EN, revised FR and the unchanged previous EN package all fail there on #826. Checks after that assertion did not run. Do not change studied identities to satisfy the assumption.
- Actual gallery metadata verification stops at `publication.approved=false`, as intended. The private, unpublished prototype has not been turned into an approved gallery source by this change. Other existing publication/schema prerequisites are outside this player adaptation.
- Anki import/render/media and all listening preview AV hooks pass. Native Anki GUI playback remains explicitly deferred by the owner; do not report it as checked.

## Anki media-update regression

An additional check exposed a real intermediate failure: unchanged contentModifiedAt let Anki keep old note sound references when the new MP3 collided with an existing filename. The source marker now advances. New `scripts/checks/validate-update.py`, wired through CI’s optional `--previous` folder, imports an older edition, studies a card, imports the current edition, verifies note/card/model/field/template IDs and every saved scheduling state (including ease, flags and FSRS data) plus all review-log rows, and compares every referenced recording’s SHA-256 against a fresh current import. Anki’s media collision aliases are allowed; the audio bytes must match. The intermediate package is retained as a negative regression and is correctly refused. Both final editions adopt the prepared recordings. Model/note modification times advance; identities and curriculum do not. All 131 filenames represent 125 distinct audio byte digests because several source recordings are identical.

Final package/CI output is `ci-final/`; earlier `ci/`, `native/packages/` and `update/packages/` are retained evidence, not final delivery paths. Native proof used the same artwork, question content and exact prepared audio bytes before this timestamp-only correction. Its playback evidence remains applicable; the final Anki migration checks cover the correction.

## Native scope

The app source was read-only. The unchanged #826 head `c5118a26e6266ebcdc52002714d9cfbadb696e85` was built into external SSD output. Native checks used English/light on **RV55 iPhone 17** and French/light plus dark on **RV55 Duo B closed**. This is representative coverage, not every card, text size or language/device combination.

The custom word comes from the gallery catalog, not standalone APKG metadata. A simulator-only copy of the built app carried an external QA catalog generated with the real packages, resolved media counts, owner words and a placeholder cover filename. This bypassed no release approval or gallery pin: it was a local test fixture. Adding/updating through the gallery persisted **Listen / Écouter** on the actual imported deck records. All 94 listening cards per tested language satisfy the native listening predicate, with Automatic as the unoverridden setting. A standalone APKG import without a gallery origin still says Play / Lire.

The large listening player and question tip fit; the smaller comparison player sits under the kana, leading-aligned; answer replay plays Back’s recording. Scoped audio logs show question playback without a tap, manual question replay, comparison playback and answer replay. A real autoplay screen recording (no `soundPlaying` capture hook) shows the gold head advancing over the recording’s waveform in about 0.3 s. Three extracted frames and full-size screenshots are retained externally. Both Astra reviewers qualify the inspected native evidence.

**Answer autoplay distinction:** dragging the answer open exposes its replay button but did not trigger automatic Back playback in this build. Confirmed-answer debug launches do play Back automatically. #826’s `ReviewScreen` triggers that on `session.isConfirmed`; do not describe this as autoplay on drag reveal. Debug reviews use `open(..., saves: false)` and do not write grades to study history.

The English and French recorded walkthroughs pass complete replay (17 and 20 directives). Cross-tree AX waits are retained raw. SoundButton has no stable native-runner identifier; plausible native labels were absent and two selector probes failed against a working tree. Sound taps therefore retain verified AX-frame coordinates, documented in each path, with playback corroborated by logs. These are fixture-specific walkthroughs, not portable structural playback regression tests. Initial empty-catalog and transient AX failures remain in external evidence.

Evidence root: `/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/sound-player-826-20261108/`. No release, gallery pin or physical-phone installation was made.
