# Brush-ready Kana: factual and contract review

2026-11-08. **Qualified PASS; no blocking factual or migration issue found.** Reviewed the uncommitted candidate against source baseline `d56a75da60cf8df1a93b313c629237431a95daac`, with the exact file hashes below. This review changed no repository or app files and used no devices.

All 106 affected notes per language (94 listening, 12 comparisons) now have kana-only main answers plus their unchanged sound tags. Romaji is preserved in the appended ninth `Romaji` field and in the existing native `payload.resources` representation, labelled **Romaji** in both languages as chosen by the owner. The Anki answer template uses a genuine `input type="button"` control, labelled Explore/Explorer, opening a hidden labelled Romaji detail. The detail is conditional on a nonempty field and absent from prompts.

Exactly 100 affected answers contain one kana; six remain grouped alternatives: `listen-hira-o` お / を, `listen-kata-o` オ / ヲ, `listen-hira-ji` じ / ぢ, `listen-hira-zu` ず / づ, `listen-kata-ji` ジ / ヂ, and `listen-kata-zu` ズ / ヅ. Their script-specific prompts, one-valid-form hints, sound mappings and explanatory notes are unchanged. These are alternatives, not two-character sequences, and no preferred spelling has silently replaced either accepted form.

Independent comparison of both language expansions against the baseline verified every existing field on the other 184 notes is unchanged; their new Romaji field is empty. For the 106 affected notes, only Back, the added Romaji field and native resources change. All 290 GUIDs, native card/book/note identities, tags, due positions, prompts, answers' sound references and existing schema IDs remain stable. Source questions, audio files/provenance and artwork have no diff. No new writing, kanji or multi-character exercises were added.

The native bridge is necessary: `RectoVersoNote.card` takes resources from the native payload rather than running the generic Flags hidden-template parser. The supplied [Core import probe](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/brush-ready-832-20261108/core-probe/Sources/Probe/main.swift) uses actual `ApkgFile`/`AnkiImport.convert`; its [report](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/brush-ready-832-20261108/core-import.json) passes both packages. I independently checked every one of its 212 affected-item records against source answers, romaji and audio filenames. Each language imports 106 Romaji resources, 100 single-kana answers, six grouped answers and 94 listening cards.

The migration checker now requires the original ordered field-name/ID list to remain an exact prefix, allows only the ninth Romaji field, preserves model/template IDs, matches the fresh package's schema, and verifies actual template contents were adopted. Root modification time advances. Existing scheduling fields, stored FSRS data, all review-log rows, actual referenced audio/image bytes and preparation hashes remain checked. Removal, reordering, changed existing IDs, unexpected fields and mismatched expected schemas are covered by negative tests.

I independently ran **29 unit tests: PASS**. Supplied [full CI](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/brush-ready-832-20261108/ci/result.json) passes both 290-card editions, 14 components, independent artwork/package-semantic rebuilds and studied-card checks. [EN](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/brush-ready-832-20261108/ci/evidence/en-edition-update.json) and [FR](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/brush-ready-832-20261108/ci/evidence/fr-edition-update.json) previous-edition updates pass appended-field/template adoption, all note/card identities, scheduling state and review-log preservation. These claims apply to the tested update scenarios, not every possible edited learner collection.

This is brush-compatible answer preparation, not complete stroke coverage. The inspected DEBUG prototype only contains あ, き, ぬ, キ and 書; five course notes per language match available data: `listen-hira-a`, `listen-hira-ki`, `listen-hira-nu`, `contrast-nu-me-nu`, `listen-kata-ki`. No 書 exercise is added. Grouped answers correctly remain ordinary text with all alternatives. Native visual/interaction validation is separate and was underway at this review cutoff. Stroke-data/storage decisions, broader character support, handwriting instruction, VoiceOver approval, native-speaker listening clearance and publication are not established by this review. `publication.approved` remains false.

Reviewed source SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `scripts/source_data.py` | `b9206a67a60552d4d06bed50f6f6b9f9e77295b490a49d116709c63740642ff1` |
| `scripts/schema_update.py` | `53b1f63e70440c2c6708c174548d5b427124c104261f6abdfdbd494ed2820c29` |
| `scripts/checks/validate-update.py` | `635b58083c199237e64bdf6cb7da68fff8a4e78549ecaaa27f0ee6497830c98e` |
| `scripts/checks/validate-anki.py` | `0f3ab8cda1e57355ab8c256ec189894aeea5fb4d5fb610f52ccdbc3df127aafb` |
| `tests/test_kana_answers.py` | `a35fc55b4a5f1892051905287975b002d8d972865db9671dbcf66954eaed4b67` |
| `rectoverso.json` | `f89e38f0eef40020a55a6297caa4513d444c061cfdc05db84a7908d7435002c8` |
| `source/languages/en.json` | `6a50410c9802bed19bf8b64ce00946e9e1df0f03ae8c29f5c6d856d8ef313447` |
| `source/languages/fr.json` | `ff69dc199aaa0c668c7790d0bd74772843c7e9cd3da9302da3b4a59985a483ee` |

Evidence SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `core-import.json` | `c8176cdef4b8123e2178702b7896bc2fd50b85a4ba40129d23d93eb57c06c987` |
| `ci/result.json` | `44fcbae0939c1568643e39ffca67da0f5404412056962f00a33589df995e3d1a` |
| `ci/evidence/en-edition-update.json` | `15ec87ec26c6efef002685f272e3741ec14abb94b3023c913e7be380efbe59ae` |
| `ci/evidence/fr-edition-update.json` | `15ec87ec26c6efef002685f272e3741ec14abb94b3023c913e7be380efbe59ae` |
