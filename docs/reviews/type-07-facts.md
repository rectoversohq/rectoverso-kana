# Type 07 — unseen-word checkpoints factual review

Verdict: **QUALIFIED PASS** for all 14 checkpoint items: readings, English/French glosses and explanations, mora counts, intended TTS mappings, source prerequisite coverage, novelty as complete words, and generated/evidenced fields. No factual blockers remain. Audio listening and native-app validation are not cleared.

Reviewed 2026-11-08 by the delegated Astra factual reviewer. All 14 records (eight hiragana, six katakana), their full bilingual notes and instructions, all 14 audio requests/provenance entries, prior question/note corpus, current source builder and supplied Anki evidence were inspected. Main app and implementation files remained read-only; no device or simulator was used.

## Complete item audit

All rows passed. Mora counts are derived from the displayed kana and taught timing rules, not from recording duration. “Input” is synthesis metadata; kanji inputs are not shown to learners.

| Item ID | Display | Reading | EN / FR context | Morae | TTS input |
|---|---|---|---|---|---|
| check-asa | あさ | asa | morning / matin | 2 | 朝 |
| check-kare | カレー | karē | curry / curry | 3 | カレー |
| check-umi | うみ | umi | sea / mer | 2 | 海 |
| check-keki | ケーキ | kēki | cake / gâteau | 3 | ケーキ |
| check-tamago | たまご | tamago | egg / œuf | 3 | 卵 |
| check-sakka | サッカー | sakkā | soccer / football | 4 | サッカー |
| check-shashin | しゃしん | shashin | photograph / photographie | 3 | 写真 |
| check-fairu | ファイル | fairu | file / fichier | 3 | ファイル |
| check-gakko | がっこう | gakkō | school / école | 4 | 学校 |
| check-chen | チェーン | chēn | chain / chaîne | 3 | チェーン |
| check-kyuri | きゅうり | kyūri | cucumber / concombre | 3 | きゅうり |
| check-dina | ディナー | dinā | dinner / dîner | 3 | ディナー |
| check-ojiisan | おじいさん | ojiisan | grandfather / grand-père | 5 | おじいさん |
| check-denwa | でんわ | denwa | telephone / téléphone | 3 | 電話 |

The notes correctly treat small ゃ/ゅ and the extensions ファ/チェ/ディ as part of one mora. `check-fairu` has three morae (ファ・イ・ル); the イ is separate. `check-sakka` and `check-gakko` preserve both a one-mora k closure and vowel length. `check-ojiisan` preserves long i and has five morae. `check-denwa` gives ん one mora without adding a separate vowel; it does not prescribe a single invariant nasal articulation. All romanizations preserve relevant vowel/consonant length and maintain the di/ji distinction.

The six kanji inputs have legitimate intended mappings in context: 朝→あさ, 海→うみ, 卵→たまご, 写真→しゃしん, 学校→がっこう, 電話→でんわ. Their lexical glosses are correct. This validates intended mapping, not the reading actually chosen by synthesis. Context glosses are not claims of exclusive meanings: for example, おじいさん can also refer to an elderly man. “Grandfather” is a valid intended sense and does not affect decoding.

## Novelty and prior coverage

All 14 are absent as complete taught words and as standalone word examples from types 01–06. A literal substring search found one deliberate qualification: あさ occurs inside おばあさん (`rule-hira-long-aa`) and おかあさん (`word-okaasan`). Neither occurrence teaches the separate word あさ or its morning sense. Thus the correct claim is new complete word, not never-seen character substring. The other 13 displays have no literal occurrence in the prior serialized question/note corpus. Kana, productive combinations and related word patterns are intentionally familiar.

The current 286-item source order places checkpoints at positions 273–286 after the previous six types. All declared prerequisites resolve. Independent feature inspection confirms coverage beyond merely trusting those declarations:

- Basic-only `check-asa` and `check-umi` use previously introduced forms.
- `check-kare` and `check-keki` use the taught katakana length bar; `check-tamago` reuses the g-row mark rule.
- `check-sakka` combines taught small ッ and length; `check-gakko` combines g voicing, small っ and long o written with う.
- `check-shashin` applies the taught し + small-y family to しゃ; `check-kyuri` applies the き family to きゅ and taught long u.
- `check-fairu`, `check-chen` and `check-dina` use explicitly introduced ファ, チェ and ディ; the latter two also use the length bar.
- `check-ojiisan` combines the taught z-row じ reading and long i; `check-denwa` combines d-row で, ん and わ.

These selected samples test transfer of taught principles. They do not independently test every one of the 92 basic forms or prove complete kana mastery. Newness applies to the first encounter; normal repeat study no longer measures an unseen first attempt.

## Primary-source checks

- [MEXT kana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf): base and voiced kana mappings and small-y combinations.
- [TUFS small-kana combinations](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-11-01.php), [long vowels](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-02-01.php), [small っ timing](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-01-01.php), and [nasal in other contexts](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-04-01.php): support the relevant one-mora combinations, extra length/closure morae, and ん timing. Counts above are this reviewer's application to the actual words.
- [Bunka loanword spelling guidance](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/pdf/94380801_03.pdf): the selected ファ/チェ/ディ spellings and long-vowel notation; no claim that this course exhausts loanword variation.
- [Japan Foundation Irodori Starter word list](https://www.irodori.jpf.go.jp/assets/data/wordlist_X.pdf): direct lexical support including 海/うみ, 写真/しゃしん, 学校/がっこう, 電話/でんわ and ディナー. The list also gives 朝's あさ reading in compounds. Its doubled-vowel romanization and this course's macrons represent the same intended length.
- [Japan Foundation Marugoto Elementary 1 vocabulary index](https://marugoto.jpf.go.jp/assets/docs/download/elementary1_a/MarugotoElementary1ActivitiesVocabularyIndex2_EN.pdf): direct support for 卵/たまご, きゅうり, and おじいさん with the selected senses.

The generic Irodori landing-page reference is supplementary context, not evidence that every item appears on that page. All 14 readings and bilingual glosses were individually reviewed; primary references were used for the relevant rules and selected lexical checks.

## Fields, audio and supplied build evidence

All 28 language-specific generated field sets have only the displayed kana on Front and an empty Meta. Romaji, recording, contextual meaning and explanatory notes appear after reveal. No kanji authoring input, English/French meaning, prompt audio or romanization is visible before reveal. Both versions prioritize accurate unaided decoding without a speed target and explicitly exclude a vocabulary test.

All 14 new MP3s match source provenance hashes. Requests and provenance agree on file, intended reading and input, with Nanami ja-JP-NanamiNeural at −20%. Their listening review remains pending; no signal or hash result is treated as an audition.

Both supplied Anki logs report 14-card import, front/back, media, real study and progress-preserving reimport passing. Every logged front/answer/instruction/note field and audio hash matches current generated content. These logs were inspected and cross-checked, not independently replayed by this reviewer.

## Remaining limitations

Native RectoVerso validation remains pending. This report does not certify runtime layout, audio controls, answer reveal, accessibility or scheduler enforcement of the authored sequence/daily limit. Human listening must still establish pronunciation, intended readings and absence of TTS artifacts. Source correctness and supplied integration evidence justify the qualified factual pass; they do not replace those separate checks.

## Reviewed snapshot (SHA-256)

Audio files were individually checked against the hashed provenance. All prior source-question files are hashed to bind the novelty/prerequisite review.

| File (relative to course root) | SHA-256 |
|---|---|
| source-repo/source/questions/01-reading.json | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| source-repo/source/questions/02-listening.json | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| source-repo/source/questions/03-rules.json | `3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc` |
| source-repo/source/questions/04-words.json | `d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81` |
| source-repo/source/questions/05-contrasts.json | `efc69f8e0cc51ef40c06f10f3ee28db4d5c7acdc55d9c865fb7b2a827b02d79b` |
| source-repo/source/questions/06-variants.json | `a0aeff50ab3157947506f1d98014a7d03d88cefd34dac73ddd3b996fe088426c` |
| source-repo/source/questions/07-checkpoints.json | `733c54bad3644143d311d33cf6f0eb8440774a00c13632a6543cec183996238c` |
| source-repo/source/audio/requests-type-07.json | `fabc7def001a4862c26d2cf04fe6ae7f316dbe4d86879af6c63aa64dc81c8308` |
| source-repo/source/audio/provenance.json | `faf1d7ff49cf8f80b806cb8e4d53fcd7eb4f6f2f45f2275e789c931a47d3cdef` |
| source-repo/source/kana.json | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| source-repo/source/references.json | `e878b9a4749bcfbc881091d9b03350a74bf4ac4b18970fe10a1644a9c8a1b305` |
| source-repo/scripts/source_data.py | `9c59199cf71c76a55f8889236b64a4b97e5343f7f666deb8192e476c50522134` |
| source-repo/source/languages/en.json | `e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a` |
| source-repo/source/languages/fr.json | `1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b` |
| builds/type-07-checkpoints/packages/Japanese-Kana-en-checkpoint.apkg | `875cdaa333f5c44f55bc461c62e67f06037d1c40dbbd217b81036195172757b7` |
| builds/type-07-checkpoints/packages/Japanese-Kana-fr-checkpoint.apkg | `48f5433e60c0df69f7c620c29a2fa3636510e60c818dff4801a1444f4f4135e8` |
| builds/type-07-checkpoints/evidence/en/anki-verification.json | `952987841e5eeafae9cbb30cd482b73bfda55b6c7f2c16714d113b862adefc39` |
| builds/type-07-checkpoints/evidence/fr/anki-verification.json | `77d18ec00127ab1946da276561402b53c529ebe9279defd02cd8f82a3bbe96d3` |
