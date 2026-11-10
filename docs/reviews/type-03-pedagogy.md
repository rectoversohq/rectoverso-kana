# Type 03 — Selected reading-rule applications: pedagogy review

Reviewer: second Astra reviewer, pedagogy. Review date: 2026-11-08.
Decision: **Qualified SOURCE/BUILD PASS; proceed to the next question type.**
No remaining confirmed source-level pedagogy blocker. Native UI verification is pending because the owner handed the simulator to another agent; this reviewer did not drive or reacquire it. No audio-listening approval is claimed.

## Scope

Reviewed every record in 03-rules.json: 16 hiragana and 18 katakana questions, 34 total. The set covers five marked families per script, three selected contracted-sound examples per script, small tsu, seven hiragana long-vowel applications, the katakana length bar, and eight selected extensions.

Executed the current inputs() expansion for English and French and inspected the Anki verification reports. The combined current curriculum has 216 scheduled questions: 91 hiragana basic questions, 16 hiragana rule questions, 91 katakana basic questions and 18 katakana rule questions. This is not the final course inventory.

## Findings resolved before this verdict

- **Major teaching-clarity issue — rule-hira-long-ou:** The original note referred to literal おう “in this word” although the displayed word is とうふ. The revised note identifies と + う, explains とう → tō, and states the productive o-vowel-kana + う pattern. English and French now connect the rule to the actual visible spelling.
- **Related transfer/scope issue — rule-hira-long-oo:** The revised note explains an o-vowel kana followed by お or う, explicitly maps こお → kō, and asks learners to keep the kana as written. It no longer introduces a demand to memorize each word's spelling.
- **Minor presentation issue — rule-hira-long-ei.meaning.fr:** The literal backslash-u202f escape was replaced with the intended narrow nonbreaking space in “horloge ; montre”.

These corrections align the long-vowel explanation with the teaching pattern described by [Tokyo University of Foreign Studies](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-02-01.php) and the o-column-plus-お spelling examples in [Bunka's modern kana spelling guidance](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gendaikana/honbun_dai2.html).

## Retrieval, instruction and feedback

Every emitted rule front contains only its displayed kana or word, plus the generic new-rule instruction. Answer romaji, target audio and context meaning appear on the answer side. There is no phonetic prompt leak or meaning-recall demand.

A beginner encountering a rule can reveal and listen, then use the productive explanation. The marked-family notes supply the full row and its exceptional ji/zu mappings. Contracted-sound notes distinguish small from full-size kana and one timing beat from two, consistent with [TUFS's contracted-sound guidance](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-11-01.php). Sokuon notes describe a held consonant closure in the selected examples, rather than an extra tsu.

Long-vowel notes distinguish written kana from the modeled sound. The とけい note explicitly explains why its spelling-oriented romaji “tokei” can accompany a commonly long-e pronunciation; it does not ask learners to rewrite い as え. The katakana extension notes model Japanese readings, with useful ti/chi and di/ji distinctions. English and French preserve the same learning objective.

All words remain isolated decoding material. Meanings are answer-side context. There are no particle-use readings, phrase lessons, grammar exercises, vocabulary-recall tasks, speed thresholds or compulsory writing demands.

## Prerequisites and manageable scope

In the actual combined order, all basic kana of the relevant script precede the rule block. The extra marked kana needed by おばあさん and ベッド are introduced before those applications. The katakana length-bar question precedes extension words that contain ー. No current target depends on an additional rule that has not yet been presented.

A rule may introduce its own new feature on first reveal; requiring that feature to have been learned beforehand would contradict the approved guided-question design. Source prerequisites and authored order establish exposure, not mastery.

The selected 34 applications are a reasonable bounded component; an exhaustive two-direction matrix is unnecessary under the brief. They use the same six-new-question allowance as other tasks. The current 216-question inventory alone requires at least 36 days of introductions at that cap; that arithmetic is not a duration or mastery promise. The ten-minute budget still needs real study-session evaluation with reviews prioritized.

## Transfer obligations carried into later types

These cards teach general principles but repeatedly retrieve fixed examples. Correctly answering が, きゃ or とうふ alone does not establish that the learner can decode a new marked form, contracted sound or long-vowel word.

Later word and cumulative-reading types should therefore sample new applications across the taught rule families, including beyond the selected a-vowel marked examples and the three contracted-sound examples. This is already part of the approved course design; it is not a demand to finish those future types before accepting this component.

Likewise, newly introduced ji/zu families eventually need the brief's grouped listening treatment where exercised; do not infer unique spelling from their sound. No new exhaustive inventory is required here.

## Verification and limitations

- Both EN and FR inputs() expansions were executed. For all 34 items, the front matched display exactly; the back matched answer romaji plus its target audio; the note matched the localized source.
- Current Anki verification JSON reports 34 cards and passes for import, front/back, media, real study and reimport preservation in both languages. These reports were inspected; this reviewer did not independently rerun the import suite.
- All 34 rule audio references have provenance declaring ja-JP-NanamiNeural at −20%, with provider input matching the displayed target.
- Audio was not listened to by this reviewer. Provider metadata, hashes and successful playback mechanics do not establish pronunciation quality.
- Native EN/FR first-rule instruction visibility, small-kana sizing, complete Note access, long-note scrolling, context placement and answer-audio access remain pending. Anki success does not substitute for those checks.
- Native claim/check and reveal grading remain the intended flow. This review does not authorize custom multiple-choice or automatic speech/handwriting grading.
- Final course ordering, future transfer coverage and supported app defaults remain separate integration checks; #805 is not fulfilled by source/deck ordering metadata.

## SHA-256 evidence snapshot

Source paths are relative to source-repo/. Build paths are relative to the parent course directory.

| File | SHA-256 |
| --- | --- |
| source/questions/03-rules.json | 3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc |
| source/questions/01-reading.json | f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767 |
| source/questions/02-listening.json | 1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51 |
| source/kana.json | 07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4 |
| source/audio/provenance.json | 91cf7bae5d5c39d54d405f4face552bbd4852d0742936332ff70d1258335e833 |
| source/references.json | 9f142ffe402f3950fefc35bbf474200849c658dc4ab7995611f1a1873aec8f1b |
| source/languages/en.json | e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a |
| source/languages/fr.json | 1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b |
| scripts/source_data.py | 93824b10fa775aa287ca1899f93d6b50dce4eb468fa160fe4b2eab83a1c05a10 |
| builds/type-03-rules/packages/Japanese-Kana-en-rule.apkg | 061aa3ffbcfd8fb25bcfa69e3299a9713de243f5206e7d70522daba8307938ab |
| builds/type-03-rules/packages/Japanese-Kana-fr-rule.apkg | 4d2e143d2208440e9ee7961aa26ffcebcd44015dea229912dd350f3dd341ab5f |
| builds/type-03-rules/evidence/en/anki-verification.json | 7c2a51b24ea481da9e335afe0dc61c02a3fbc0170ce68a6b1cc7bd9c6e716431 |
| builds/type-03-rules/evidence/fr/anki-verification.json | d59e16831cc11f8583f2002edb4a3a8075d0b0f94a92be02ee0b9ff6760dae00 |
