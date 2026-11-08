# Gentler opening: factual and contract review

2026-11-08. **Qualified PASS; no blocking source/content/migration issue found.** Reviewed the uncommitted candidate against `0fc12c003f637fd17f5b012b2ceb904a6b2718b8`. Exact reviewed hashes are below. No source/app files were edited and no devices were used by this reviewer.

The preset is four new scheduled questions per day, with reviews first. Both full and compact EN/FR guidance now give four, retain the approximate ten-minute budget and permission to reduce/pause new introductions, and impose no completion deadline. File-import instructions correctly remain manual; gallery settings are initial presets, not an update that overwrites learner choices. The brief's lower bound of 46 introduction days for 182 basic reading/listening questions is correct at four/day. This is not a claim that the entire course takes 46 days or that introduction establishes mastery.

Independent enumeration of the resolved 290-question curriculum confirmed:

- First eight: read あ, read い, listen あ, listen い; then read う, read え, listen う, listen え. All 287 rolling four-question windows contain at most two basic reading introductions. Each script has 23 reading pairs; original relative basic-reading order is preserved.
- Every prerequisite is available before its dependent question. Every listening requirement has a position difference of at least two from introduction (at least one intervening question). All six grouped accepted sets remain unchanged; お/を and オ/ヲ wait for both spellings, and ji/zu wait for the marked families.
- `word-hon` remains ほん / hon / book, with unchanged audio and explanation. It moves to stage 2, position 154, between `read-kata-30ab` at 153 and `listen-kata-ka` at 155. Its ほ and ん prerequisites occur at 70 and 106. It supplies familiar-script decoding while the オ/ヲ listening group remains delayed.
- All source-question differences are limited to stage, priority and batch. Both language expansions preserve all 290 GUIDs/native card/book/note identities, models/field/template IDs, prompts, main answers, romaji details and audio references. Only the first あ card's appended course-guidance Note changes in wording; other teaching explanations are unchanged. Due positions/stage tags change intentionally with the authored schedule. Audio files/provenance and the Japanese inventory are unchanged.

Every reading visible set was independently checked by walking the full resolved curriculum. The target is included, future members of its pair are excluded, and only previously introduced same-script forms inside its retained three-row frame are drawn. The first あ figure has one region; the second has あ and い. Current region counts range from one to ten. The full introduction sequence is computed before component filtering. These are fixed authored snapshots, not measurements of learner knowledge: older cards retain their earlier views on review.

The 92 separate preparations retain 1000×1080 dimensions, positions, fonts, gold target glyph, original script-global ordinals and hideAll for every drawn neighbor. Future glyphs, romaji, masks and preparation regions are absent. There are 368 newly named `-introduced-` table PNGs and 92 unchanged standalone questions. The [pixel audit](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/gentler-opening-20261108/pixel-audit.json) compares all 368 tables and allows only removal of future glyph/readings and unused dividers; known glyph/reading pixels, gold and geometry remain exact. It also records unchanged other artwork. I independently verified the current frozen manifest against final CI and all 668 generated artwork hashes.

Core's preparation contract permits a one-region figure and sparse global ordinals. Matching requires the selected ordinal's geometry to equal the target and all other regions to equal the siblings; the authored data satisfy those relationships. The existing app accessibility defect combining visible count with a global ordinal remains an app follow-up; this change is not VoiceOver approval.

I independently ran **34 unit tests: PASS**. [Final CI](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/gentler-opening-20261108/ci-final/result.json) completed during review and reports PASS for both 290-card editions, all components, independent artwork/package-semantic rebuilds and study checks. [EN](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/gentler-opening-20261108/ci-final/evidence/en-edition-update.json) and [FR](/Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/builds/gentler-opening-20261108/ci-final/evidence/fr-edition-update.json) old→new checks pass identities, schema/template adoption, referenced media bytes, all 92 preparation hashes, scheduling fields including stored FSRS data, and every review-log row in the tested scenarios. Existing learners' saved due positions/options are preserved; this does not establish automatic adoption of the new introduction order or four-card limit in an existing collection. Modification time advances and new image names avoid older-media collisions.

Native validation was underway and is not included in this verdict. No physical-device behavior, dynamic knowledge tracking, new pronunciation listening approval or publication clearance is inferred. `publication.approved` remains false. Broader gallery/accessibility limitations are not resolved by the source/Anki checks.

Reviewed file SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `rectoverso.json` | `673277774391842e07de2acc8c832a30c04a54d3d0fbe06a7bc67d3cf306751a` |
| `scripts/source_data.py` | `75c2e0a70815b22d7b84e70e9b08fb0d49d59d4e65a54a05402cb48f41efea9a` |
| `scripts/render_artwork.py` | `547c7535365ef8efca75c571f2895566bb6e2a94570a8ab1dbc7d942226b95d8` |
| `scripts/course_contract.py` | `24b32bdffd2bc9d430d16bf00d33069a4ab9f585e0ca71af2a87cc6e6f4d2f86` |
| `scripts/checks/validate-anki.py` | `a50c1785d254f498d8e538595270d888e6b5b9fa943f1327ab62db6d203d0838` |
| `artwork/artwork.json` | `cd3bff442039695db152776ee7f824cdb4840582121ed00dcb9ccc7e5196b8df` |
| `source/learner-guide.json` | `8f71b2369646b15ba2d41794da52b2b4c0417bf26cf5119c203f0f5dc7f24fe8` |
| `source/languages/en.json` | `21de9a7b30b24f001862f203eb6e2d0e61d0c5ef31691a63860fbed84a8af985` |
| `source/languages/fr.json` | `a5586af7e45a13947730e592ee793353389f6dc797b1d92a30edd55d356b17da` |
| `source/questions/01-reading.json` | `8710d26c08f7878e4dffce6c2b6916b6c474450e45803177353fe5ca30826612` |
| `source/questions/02-listening.json` | `2adb285ace6fc833f4e01cd7fd3942b050699dd1b3225a07850b43f05ff1a931` |
| `source/questions/04-words.json` | `d84f96200ea44b602572114e65e2dbc1e314e6d05fa7a624df50439beb9d12d0` |
| `source/questions/05-contrasts.json` | `d59a726d521430a40c91bc973088325f191e1ccc7017ed2c10ba2138a300bc64` |
| `tests/test_gentle_sequence.py` | `ed38c8d19c3b08ea9296482c87198e851a294b078abe3030ccd05842d5f6c946` |
| `tests/test_reading_artwork.py` | `675bca6552780b14e7a55a5863bdfeb7f30c833444e8758fc9a93d5846e33f2f` |

Evidence SHA-256 values:

| File | SHA-256 |
| --- | --- |
| `pixel-audit.json` | `96f44a8abd2ea21b7dec4230402bf1d8238a0b8613d4144ff5d730c3021c1f65` |
| `ci-final/result.json` | `44fcbae0939c1568643e39ffca67da0f5404412056962f00a33589df995e3d1a` |
| `ci-final/evidence/en-edition-update.json` | `15ec87ec26c6efef002685f272e3741ec14abb94b3023c913e7be380efbe59ae` |
| `ci-final/evidence/fr-edition-update.json` | `15ec87ec26c6efef002685f272e3741ec14abb94b3023c913e7be380efbe59ae` |
