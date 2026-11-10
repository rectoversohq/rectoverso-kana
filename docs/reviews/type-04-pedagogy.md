# Type 04 — Word reading: pedagogy review

Reviewer: second Astra reviewer, pedagogy. Review date: 2026-11-08.
Decision: **Qualified SOURCE/BUILD PASS; proceed to the next question type.**
No remaining confirmed source-level pedagogy blocker. Native rendering and actual audio listening are pending.

## Scope and resolved blocker

Reviewed all 36 word records: 24 hiragana and 12 katakana. Executed English and French inputs() expansions against the actual artwork record, audited the combined introduction sequence and inspected both Anki verification reports.

**Major answer-leak blocker, resolved:** Initially the meaning appeared in question-side Meta. This displayed the exact requested romaji for word-sushi in both languages and word-memo/word-tomato in English. Such prompts could be answered without decoding the kana.

The revised expansion has a reading instruction in Kicker, Japanese-only Front and empty Meta. Meaning remains in answer-side Example. Checked this arrangement for all 36 words in both languages, including every leaking case. This preserves the owner's context-only meaning requirement and removes the inadvertent translation/romaji cue. The same policy was applied in the builder to future checkpoints; no checkpoint content is approved by this review.

## Objective and difficulty

The current task requires the learner to decode the visible word before revealing its reading and audio. Context meaning is not tested. English and French notes explicitly accept accurate slow reading and explain that meaning need not be memorized. No time limit, grammar objective, compulsory handwriting or automatic pronunciation scoring is added.

The early inventory begins with two-kana combinations using only introduced forms. Later examples combine marks, contracted sounds, length and consonant doubling. Useful targeted feedback identifies the four beats and long vowel in びょういん, the long vowel in きょう and おかあさん, the held consonant in はっぱ and ポケット, and the contracted sound plus length in ジュース. This is more useful for checking decoding than a meaning-only answer.

The new words provide transfer beyond the rule cards' fixed examples and beyond chart positions. Words such as じかん, さんぽ, びょういん and ジュース exercise members or combinations beyond the selected initial row examples. Familiar cognates may still be known to learners, but their meanings no longer supply a question-side shortcut. These scheduled practice examples are not themselves an unseen-word mastery assessment.

## Dependencies and order

The current combined expansion contains 252 scheduled questions. Every word's explicit prerequisites precede it. Independently checked the visible basic glyphs against prior introductions and manually checked the derived combinations against their rule prerequisites.

- Basic-word stages contain 18 hiragana and 5 katakana words; post-rule stages contain 6 hiragana and 7 katakana words.
- びょういん follows the b-family, contracted-sound and long-o rules; きょう follows the contracted-sound and long-o rules.
- はっぱ and ポケット follow the relevant p-family and small-tsu rules.
- ジュース follows the z-family, contracted-sound and katakana length-bar rules.
- All prior core listening reverses still have at least one intervening scheduled question after each prerequisite reading form. Adding words has not broken that separation.
- English and French inputs() emit the same ordered item sequence. Existing rule exposure precedes later applications; exposure is not mastery gating.

The 36 additions consume the same six-new-question allowance as other types. The present 252-question inventory has a minimum of 42 introduction days at that cap, before review-driven pauses and future additions. It does not establish ten-minute session feasibility; reviews still take priority.

## Audio and source/build evidence

Every word references audio with declared ja-JP-NanamiNeural at −20%. Some provider inputs use kanji for lexical disambiguation, including 花, 雪, 病院 and 今日; the learner-visible prompts remain はな, ゆき, びょういん and きょう. Hidden synthesis input does not turn these into kanji-learning questions.

For both languages, independently checked all 36 emitted Front, Kicker, empty Meta, answer-side Example and answer reading/audio fields. Both Anki verification reports state 36 cards and pass import, front/back, media, real study and reimport preservation. The reports were inspected, not independently rerun by this reviewer.

## Remaining limits

- Native English/French rendering has not been reviewed for type 04. The owner handed the simulator to another agent; this reviewer did not drive or reacquire it.
- Native target readability, answer-side context, complete feedback and answer-audio access remain to be verified.
- No actual word audio was listened to by this reviewer. Provenance and import checks are not pronunciation-quality approval.
- Later cumulative checks should use words absent from earlier teaching examples and only introduced forms/rules; repeated successful reading of this practice inventory does not prove that transfer.
- Supported introduction order and study defaults remain the separate #805 app dependency. Source order and due fields do not establish that app behavior.

## SHA-256 evidence snapshot

Source paths are relative to source-repo/. Build paths are relative to its parent course directory.

| File | SHA-256 |
| --- | --- |
| source/questions/04-words.json | d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81 |
| source/questions/01-reading.json | f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767 |
| source/questions/02-listening.json | 1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51 |
| source/questions/03-rules.json | 3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc |
| source/kana.json | 07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4 |
| source/audio/provenance.json | 16d27fd23a8376f3d12827c03c64b86f361c98de23f7a15c4981eeaebf406127 |
| scripts/source_data.py | ce1df07437875ed97199b911164de57b79ca26583421b7eda7ee648a6a814a67 |
| builds/type-04-words/packages/Japanese-Kana-en-word.apkg | 93717a0b89f90940a9ab08a650c8a0b2fd152e89570d4a0025d3fe3e4c4efe50 |
| builds/type-04-words/packages/Japanese-Kana-fr-word.apkg | 26f694d63264f9d23e56fa663f981d2f64c64555a35a7a7691760ad851c052d1 |
| builds/type-04-words/evidence/en/anki-verification.json | f0e3e4d360bab49775736a870d93daef36614837720fd8820269d601ec3fe501 |
| builds/type-04-words/evidence/fr/anki-verification.json | a1dcda03f880d10cb73868356185f62e9efe85f8ac3e7f2c23df31c879ea1743 |
