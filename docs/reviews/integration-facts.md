# Final integration — factual review

Verdict: **QUALIFIED PASS** for the integrated 290-question English/French candidate, including all four derived shared-sound listening applications. No unresolved factual/content blockers remain in the hashed snapshot. The verdict covers source content, mappings, prerequisite consistency, generated fields and supplied combined-build evidence; it does not clear native-app behavior or human listening.

Reviewed 2026-11-08 by the delegated Astra factual reviewer. This report supplements the seven per-type reports and binds their content findings to the final combined snapshot. No implementation or app files were edited, and no simulator or device was used.

## Final scope

| Type | Questions per language | Verdict |
|---|---:|---|
| Basic kana → sound | 92 | Qualified pass; all basic forms covered |
| Basic sound → kana | 90 | Qualified pass; 45 sound groups per script |
| Selected marked shared-sound listening applications | 4 | Qualified pass; reviewed below |
| Productive reading-rule applications | 34 | Qualified pass |
| Short-word decoding | 36 | Qualified pass |
| Similar-form comparisons | 12 | Qualified pass |
| Alternate-form reading | 8 | Qualified pass |
| Unseen-complete-word checkpoints | 14 | Qualified pass |
| **Total** | **290** | **Qualified factual pass** |

The added four applications do not alter the 92-form basic reading inventory or its 90 grouped listening questions. They are selected uses of already taught marked families, not an exhaustive independent reading/listening matrix. The basic inventory remains 46 forms per script, with お/を and オ/ヲ sharing their respective sound tasks.

## Shared-sound supplement — all four items

| Exact item ID | Requested script | Accepted kana | Reading / recording input | Full-source position |
|---|---|---|---|---:|
| listen-hira-ji | hiragana | じ / ぢ | ji / じ | 124 |
| listen-hira-zu | hiragana | ず / づ | zu / ず | 125 |
| listen-kata-ji | katakana | ジ / ヂ | ji / じ | 257 |
| listen-kata-zu | katakana | ズ / ヅ | zu / ず | 258 |

Each accepted set is correct for modern common Japanese. Both translations explicitly preserve that scope and explain that sound alone cannot select the spelling required by a particular word. They do not assert interchangeability in written vocabulary, nor universal homophony across dialects. Prompts ask for a matching kana and explicitly name the script. Answer fields show both accepted forms plus ji or zu. There is no kana/romaji answer in visible listening front text.

The z- and d-family prerequisite notes explicitly introduce every accepted form, including ぢ/づ and ヂ/ヅ with their ji/zu readings. The four tasks follow these notes with 4–9 intervening questions, depending on prerequisite and task. No new grapheme or pronunciation rule is introduced by these reverse applications. The katakana tasks correctly reuse the same Japanese sounds recorded from hiragana じ and ず.

[Bunka romanization Q&A, Q17](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/pdf/94336801_01.pdf) directly supports the modern-common-Japanese sound mergers. [Bunka modern kana spelling, section 5](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gendaikana/honbun_dai2.html) shows why written ぢ/づ remain word-dependent. The [MEXT chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf) independently lists the relevant voiced rows and ji/zu readings. These primary references support all four named applications.

The two new Nanami −20% files have request/input/reading agreement and verified hashes:

| File | SHA-256 | Listening status |
|---|---|---|
| rv-kana-sound-ji.mp3 | `66940715273007654abbd6d50d9ac87236f62df5200605f7f0e51bccb659ef30` | pending |
| rv-kana-sound-zu.mp3 | `8f9ee9f19d8fcf7be2239fa8024bab5b2d1da442811d6f816efb1994b348c04e` | pending |

## Whole-course consistency

All 290 identities are unique, both guidance languages are complete, all declared references resolve, every question's audio exists, and all 131 MP3s match provenance with the approved Nanami voice/rate. The source-contract check was independently executed read-only and passed. The integrated sequence resolves every prerequisite; basic listening follows all its accepted reading forms, with an intervening question. Script progression remains hiragana before katakana, followed by mixed-script checkpoints.

Types 04–07 match the exact source-file hashes in their respective factual reports. Removing only the new appendices keys from types 01 and 03 reproduces their previously reviewed source hashes exactly, confirming that their underlying question content and order are unchanged. Type 01 retains the already reviewed type-02 sequencing revision. The change to type 02 is the reviewed four-item supplement; all 94 current listening items were also checked against generated fields and supplied final-listening evidence in both languages. This report therefore supersedes the old type-02 count for the integrated build without invalidating its 90-item basic-inventory findings.

The prior factual qualifications remain: isolated は/へ use ha/he; modern を/ヲ use o; vocabulary spelling is not inferred from homophone audio; length and mora explanations are restricted to the actual examples; alternate glyphs are fonts rather than handwriting instruction. Word/checkpoint meanings remain answer-side context. All 14 checkpoint words remain new as complete taught words, with the documented あさ substring inside earlier longer words. Checkpoints are selected transfer samples, not proof that every basic character is mastered. Specific details and primary references are in the seven per-type reports.

The source metadata count has been corrected to 290 for both languages and the combined candidate. Generated package counts agree. The reviewed source is an unpublished candidate; this factual review does not authorize publication or make an audio-rights determination.

## Learner guide and unscheduled references

All English/French course-guide and reference prose was reviewed. The guide treats ten minutes and six new questions/day as adjustable starting recommendations, includes due reviews in the time budget, permits pausing new introductions, and promises no fixed completion date. It correctly says directions count separately and recommendations do not automatically change app settings. All six quoted EN/FR settings labels match the read-only app Localizable.xcstrings; DeckSettingsView.swift supports a zero new-card limit. This verifies current source strings and available configuration, not execution on a device.

The hiragana and katakana reference tables each have 46 basic mappings, 25 marked mappings, 33 principal contracted combinations and three separately identified ja/ju/jo alternate spellings. Every mapping was checked, and the EN/FR tables are identical. The 33 count excludes those three additional spellings explicitly rather than pretending they do not exist. The one-mora small-ya/yu/yo statement is correct. [MEXT's kana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf) and [Bunka's modern sound-merger explanation](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/pdf/94336801_01.pdf) support these readings.

The 13 Table 1 extended spellings (シェ, チェ, ツァ, ツェ, ツォ, ティ, ファ, フィ, フェ, フォ, ジェ, ディ, デュ) and their learner labels are correct. The 20 Table 2 written forms exactly match the official list. Their description as closer renderings of foreign sounds/spellings, with word-specific conventions and alternatives, accurately reflects [Bunka loanword spelling tables](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/pdf/94380801_03.pdf). Neither list claims universal or exhaustive phonetic coverage, and the guide does not require memorizing all entries.

The four appendices attach only after reveal to read-hira-3042 (course guide), rule-hira-kya (hiragana reference), rule-kata-kya (katakana reference), and rule-kata-extension-ti (extensions reference). No extra scheduled cards are created. Generated Note HTML preserves line breaks; the structured search Reference field names the corresponding reference. These reading tables do not contain any checkpoint word as a complete word example.

## Build evidence

The 94-item final-listening component evidence was cross-checked: all 188 language-specific front/answer/instruction/note entries and media hashes match current generation. The supplied logs report passing import, front/back, media, real study and progress-preserving reimport.

For the combined course, all 580 language-specific generated field sets were compared with supplied Anki evidence. Front, answer, instruction and note fields match for every item; every logged media hash matches current source audio or artwork bytes. Both logs report passing import, front/back, media, real study and progress-preserving reimport. This is inspection/cross-check of supplied evidence, not an independent replay by the factual reviewer. Images inspected in prior type-specific reviews retain those visual-review limits; hash equality does not amount to all-screen native inspection.

All 14 final component evidence sets (seven types × two languages) were also compared with current generated fields and report passing checks. The independent rebuild has identical artwork manifests and image bytes, verified directly. Its supplied comparison reports confirm source identities/content, authored order, media semantics, and preservation of real studied-card progress in place. Package ZIP bytes are allowed to differ; the claim is semantic equality, not byte-identical archives. The fresh-clone portability run is outside this snapshot and not claimed here.

## Remaining limitations

- All 131 audio file identities were verified, but there is no native-speaker audio clearance. Provenance has 50 reused audition-source files (45 basic entries lack a per-entry listeningReview field; five explicitly record approved audition source, not native review) and 81 new files marked listeningReview=pending. Correct TTS strings and hashes do not establish the actual spoken reading or quality.
- Native RectoVerso validation of the full course remains pending. Earlier limited type-01 iPhone evidence cannot be generalized to all seven types or all 290 questions. No simulator use was substituted.
- Authored source order and deck study recommendations do not prove runtime enforcement. App issue #805 remains relevant to curriculum-order introduction and the approved six-new-questions/day, after-reviews defaults.
- Per-type reports are historical snapshots. This report binds the final integrated snapshot and supplement; it does not retroactively claim that earlier evidence tested later changes.

## Reviewed snapshot (SHA-256)

| File (relative to course root) | SHA-256 |
|---|---|
| source-repo/source/questions/01-reading.json | `91b55b8d8b9039c163faf76bbf416e77d652a0f3ce2e6102fde4a8b36ccd2bf5` |
| source-repo/source/questions/02-listening.json | `7b2c3fa379bf53b6a376fd0740958814164099ce6e8b4da151c7816eb146fb2c` |
| source-repo/source/questions/03-rules.json | `3fcb8d495311dada9226da8bd7897b2d732cf3834376df7fe8605bd7de4d935d` |
| source-repo/source/questions/04-words.json | `d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81` |
| source-repo/source/questions/05-contrasts.json | `efc69f8e0cc51ef40c06f10f3ee28db4d5c7acdc55d9c865fb7b2a827b02d79b` |
| source-repo/source/questions/06-variants.json | `a0aeff50ab3157947506f1d98014a7d03d88cefd34dac73ddd3b996fe088426c` |
| source-repo/source/questions/07-checkpoints.json | `733c54bad3644143d311d33cf6f0eb8440774a00c13632a6543cec183996238c` |
| source-repo/source/kana.json | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| source-repo/source/learner-guide.json | `e71f46ad201b333790a29a656756b9320302ba851bdb60302dbc840b3a836124` |
| source-repo/docs/learner-guide-en.md | `add607237448e2d3d484cde0f95c7396fbd19331fc20e814058f796cb3498428` |
| source-repo/docs/learner-guide-fr.md | `abf6cc37254cba9594f534fcca6fed99af4505d85d016be0be3be408e4c4809b` |
| source-repo/source/references.json | `e878b9a4749bcfbc881091d9b03350a74bf4ac4b18970fe10a1644a9c8a1b305` |
| source-repo/source/audio/provenance.json | `eb63e97bd59e73fa0efc08c5f2db412f6a9289c67164ef996b6620dd48ce24dd` |
| source-repo/source/audio/requests-type-02-applications.json | `592f26c26ddbc3bde7c8cc933047f5801c379c3a5860b7235dbbbbe704864321` |
| source-repo/scripts/source_data.py | `5226034450fa55f1bb07ef10c606d217c1214b70ed39e7eda637de3d2791c84c` |
| source-repo/scripts/course_contract.py | `d66069ae2d0adfbd53a068e0ebddbeeb5b7f6bea437339cbe98e9afcc3addc73` |
| source-repo/rectoverso.json | `1deb0449e7bce3011b8871ae9c929375dbbbb2efff6ba5c72498574cf6f71f59` |
| source-repo/source/languages/en.json | `533a50a5427b757e98d98c2db93ef60868f9d5c4d190a66b1ba32ccf9051fe93` |
| source-repo/source/languages/fr.json | `2be1769ad42a0695b4a56f80884c493e5ac6db8bcab615a328ecd1c03608e396` |
| source-repo/README.md | `cb10609bceea8f66b66b1db0dadeef224bc5b6887cad4bff07cbc6086b49e564` |
| source-repo/docs/review.md | `74c089916a3f255fea3d808ddad9a6d0859fdbd73cd0bd98875a3b30c8b2d447` |
| builds/final-ci-working/first/artwork/artwork.json | `f5b28dd7d37a18958620024c2bec2f898cf10d4e8695fd3a3eb22488f7dd81d8` |
| builds/final-ci-working/first/packages/Japanese-Kana-en.apkg | `90d854d71377a8f17045d5482311e39fe848a56150abddd3ec21edf3f6b50abc` |
| builds/final-ci-working/first/packages/Japanese-Kana-fr.apkg | `2d596ef7517a9137813256c859683cee80fafc99eca439c118f81f72e4497ce1` |
| builds/final-ci-working/evidence/en/anki-verification.json | `e241ef81db42af532dc634cc9fde3577fee9c8dd66681c6940e5b527429db5cc` |
| builds/final-ci-working/evidence/fr/anki-verification.json | `60ec81910584058f7308eed63cde186484f9939f3561e1c7fe3a7ac65f484f70` |
| builds/final-ci-working/result.json | `44fcbae0939c1568643e39ffca67da0f5404412056962f00a33589df995e3d1a` |
| builds/final-ci-working/source.json | `5898e4c3673fd387a786b70b1bc6617ff8587710d2a4c46a4f35c3c217b12d96` |
| builds/final-ci-working/second/artwork/artwork.json | `f5b28dd7d37a18958620024c2bec2f898cf10d4e8695fd3a3eb22488f7dd81d8` |
| builds/final-ci-working/evidence/en-rebuild.json | `a3c01b6ec2a4f90f4ec96a7c46040206b9b1480902a3a50b523c4e802aeae0c6` |
| builds/final-ci-working/evidence/fr-rebuild.json | `b2be795ed270e5bb968c47b519c55bd953ebefb59fae304eabe56389e9c9d705` |
| builds/final-ci-working/second/packages/Japanese-Kana-en.apkg | `72bc30af84a179c835288368d698fdef6b83de9db01ca694ec0a028154d1d786` |
| builds/final-ci-working/second/packages/Japanese-Kana-fr.apkg | `6e802c4b8dd01588b6188ba15208e0da91cb4407570aef23d4cd685bf7cb4fe4` |
| builds/final-ci-working/evidence/en-reading/anki-verification.json | `667b5374111059104d081c39654fb096317a685072ee6d6699dfb109db08fdb3` |
| builds/final-ci-working/evidence/en-listening/anki-verification.json | `8dcafab429ac924dfac2497f1d17db534d030adee54bbe2ba27ebbd6e093b599` |
| builds/final-ci-working/evidence/en-rule/anki-verification.json | `c9e3c1622687ac0ed349c5e8965be63dac3c13996957c8ff6b34d05d70dbdfd0` |
| builds/final-ci-working/evidence/en-word/anki-verification.json | `f0e3e4d360bab49775736a870d93daef36614837720fd8820269d601ec3fe501` |
| builds/final-ci-working/evidence/en-contrast/anki-verification.json | `cea9062f1bacc4c8de8de724614f42b20d95553cd6f7a0ab15e4603fc8af9979` |
| builds/final-ci-working/evidence/en-variant/anki-verification.json | `0bfbbbf85dcaadab70d8a3a48c8631259dfefa0e7140abf536e396370d6a754f` |
| builds/final-ci-working/evidence/en-checkpoint/anki-verification.json | `952987841e5eeafae9cbb30cd482b73bfda55b6c7f2c16714d113b862adefc39` |
| builds/final-ci-working/evidence/fr-reading/anki-verification.json | `2f30fd63945249031175dad3e27ef7fe247e8382e722dccd9870feafba21e5b6` |
| builds/final-ci-working/evidence/fr-listening/anki-verification.json | `8d10f17cd22dfe0c0de009c782ccc5dc790372bc871b3627e7cdbe740402fe9a` |
| builds/final-ci-working/evidence/fr-rule/anki-verification.json | `fbfc498c0b103ffa573eef1753eb537623ac9a7d4e69bcf958c5aa2c21abd6b6` |
| builds/final-ci-working/evidence/fr-word/anki-verification.json | `a1dcda03f880d10cb73868356185f62e9efe85f8ac3e7f2c23df31c879ea1743` |
| builds/final-ci-working/evidence/fr-contrast/anki-verification.json | `4b950f6fc329ed0a875ec9ce1385f38b49176dd48307b4e65ac58bf1ff6ef2b7` |
| builds/final-ci-working/evidence/fr-variant/anki-verification.json | `fe983ada6f3eeb07899db044607dce4d424958e73c4dab5b4ccdc109a07f80e8` |
| builds/final-ci-working/evidence/fr-checkpoint/anki-verification.json | `77d18ec00127ab1946da276561402b53c529ebe9279defd02cd8f82a3bbe96d3` |
| builds/type-02-listening-final/evidence/en/anki-verification.json | `8dcafab429ac924dfac2497f1d17db534d030adee54bbe2ba27ebbd6e093b599` |
| builds/type-02-listening-final/evidence/fr/anki-verification.json | `8d10f17cd22dfe0c0de009c782ccc5dc790372bc871b3627e7cdbe740402fe9a` |
| source-repo/docs/reviews/type-01-facts.md | `38ee4292dc22e9cf830ba7f1c93bb1fccd3572cf45165f99684e52ac8713e9dd` |
| source-repo/docs/reviews/type-02-facts.md | `650baaadb051df8c3f4f43c8c240a82da99e3dfb56ccea4cf3a9b25c385f372c` |
| source-repo/docs/reviews/type-03-facts.md | `1a0d577d927df7a8a7efb07fb0943f7d3f2c1c2bc0cb1fe1f47c5fbffe42ce9c` |
| source-repo/docs/reviews/type-04-facts.md | `0a6ae0d8a528766c6277e7f1bbdf5b658f4d18a09c8b55010bdc8804703fdbe3` |
| source-repo/docs/reviews/type-05-facts.md | `09e857ac025ce4f4be8e25fa001dc28ba722cf8a3f72ab88b79e389118c0ac8e` |
| source-repo/docs/reviews/type-06-facts.md | `9dd2a9642998919608b81b3156248c6835d9b13e0c13b0df57de785e42e766e3` |
| source-repo/docs/reviews/type-07-facts.md | `ea6dde3309dfa05dcdd0dcd0b391451d9017840cbb56aaf8527436b0a468e13e` |
