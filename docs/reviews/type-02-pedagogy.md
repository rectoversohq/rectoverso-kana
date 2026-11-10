# Type 02 — Sound → kana: pedagogy review

Reviewer: second Astra reviewer, pedagogy. Review date: 2026-11-08.
Decision: **Qualified PASS for this question type; proceed to the next type.**
No remaining confirmed source or English-native pedagogy blocker. This is component approval, not approval of the complete course, every native rendering, or the pronunciation of the audio.

## Reviewed scope

Reviewed all 90 listening records, both script inventories, all distinct bilingual prompts and notes, audio references, and the actual expansion/order from source_data.inputs() for English and French. Inspected the revised English native front and reveal screenshots. The complete current two-type expansion contains 182 questions; the listening-only preview contains 90 and is an inspection artifact, not the beginner introduction sequence.

## Resolved findings

- **Major brief-conformance issue — all listen-* IDs:** Initial emitted answers omitted romaji despite having answerReading in source. The current expansion displays accepted kana plus answerReading and audio, for example “あ · a” and “お / を · o”. Verified this on every emitted listening answer in both languages. The English native reveal visibly confirms “あ · a”.
- **Ambiguity clarification — especially listen-hira-o and listen-kata-o:** The revised prompt asks for “a matching hiragana/katakana” and “un hiragana/katakana correspondant à ce son”. It requests one acceptable form without implying that sound determines unique spelling or that every accepted spelling must be recalled.

## Retrieval objective and feedback

The front is the script-labelled listening instruction plus its audio recording. No kana, answer romaji, grid, positional clue or multiple-choice option appears in the emitted front. The English native screenshot confirms that presentation and shows a question-audio replay control.

The task therefore elicits a matching written form from sound. Mental recall is sufficient; optional handwriting is clearly explained in the answer feedback. The English native reveal displays the full feedback and an answer-audio Listen control. It does not introduce automatic handwriting/speech scoring or a speed threshold.

English and French prompts preserve the same learning demand. Feedback asks the learner to compare the recalled shape with the revealed form and treats the recording as the sound model. The two o-group notes explicitly accept either form and explain that the exercise does not test a word's required spelling.

The accepted sets and audio references match every declared prerequisite form. All 45 underlying sound files retain declared Nanami −20% provenance. These are metadata and reference checks, not auditory quality judgments.

## Actual introduction order

Executed ordered(questions()) and inputs() for both languages against the real artwork record. The emitted sequence matches the ordered source and has sequential due values from 1 to 182.

- Every listening question follows introduction of every form in its accepted set.
- Every reverse has at least one intervening scheduled question after each required reading item; the minimum is one.
- All reading introductions within each normalized row-family batch precede its listening questions.
- listen-hira-o is position 90, after お at 8 and を at 87; listen-kata-o is position 181, after オ at 99 and ヲ at 178.
- The first six questions are reading あ/い/う followed by listening a/i/u: six scheduled questions introducing three characters, not six characters.
- A short intervening gap satisfies the requested separation check. It is not evidence of durable mastery; spaced review remains necessary within the approved course design.

The delayed initial o listening exercise follows the owner's explicit grouped-sound and prerequisite decisions. It is not grounds for silently adding an earlier duplicate listening question.

## Limits and course-level dependencies

- Direct native visual inspection covers the revised English first item only. French source copy is reviewed; French native screenshots were not yet supplied at this evidence snapshot.
- Grouped-o, katakana, dark appearance, all devices/text sizes and every reveal state are not exhaustively verified here.
- This reviewer did not listen to the audio. No native-listener pronunciation, segmentation or accent approval is claimed.
- Parent author reports successful import, rendering, media, study and reimport checks for both 90-card Anki packages; this reviewer independently checked generated fields and curriculum order, not those complete import runs.
- New-card ordering, six new scheduled questions/day and placement after reviews remain the #805 app dependency. Source order and deck due values do not prove the app applies those defaults.
- Hiragana rules, marked-form sound groups, word applications and later cumulative reading are not yet authored. Their absence does not block this component; they require their own review and the eventual combined-course sequencing audit.
- Authored introduction order does not impose or demonstrate mastery gating.

## SHA-256 evidence snapshot

Source paths below are relative to source-repo/. Build paths are relative to its parent course directory.

| File | SHA-256 |
| --- | --- |
| source/questions/01-reading.json | f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767 |
| source/questions/02-listening.json | 1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51 |
| source/kana.json | 07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4 |
| source/audio/provenance.json | 6b0bbef765295febdc1491d503b7751d29dc7f8a5daadaba702e2ca7b41a8e94 |
| source/languages/en.json | e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a |
| source/languages/fr.json | 1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b |
| scripts/source_data.py | 01068ba6cd7171b74deaa79e0310c818f48785b80407360f722e1edab795aabb |
| builds/type-02-listening-r2/native/en-front.png | 15acdabaf7477fe4f626709bb8ea29dbce9f9bebaa0fddd4cf5037f4b2b94533 |
| builds/type-02-listening-r2/native/en-reveal.png | 63ccc488b1444e55eb77a5a196da449ac995924397df0798de21f92cc5a6567c |
| builds/type-02-listening-r2/packages/Japanese-Kana-en-listening.apkg | c98d40e61a1c567a9d0b97839aef6d921f7fcbad94322a8c3bc799a0f9337fbd |
| builds/type-02-listening-r2/packages/Japanese-Kana-fr-listening.apkg | 0894a00511ca06d2a1e0de3f6b04cd7c3bde9dbba1643b7c6b8b3272fde762ba |

## Addendum — French native evidence

Directly inspected fr-front.png and fr-reveal.png on 2026-11-08. The complete French matching-hiragana prompt is readable, its question replay control is visible, and no answer kana or romaji appears before reveal. The revealed “あ · a”, complete French feedback, and answer Listen control visibly fit. The earlier French-native-pending limitation is therefore resolved for this representative first item. The qualified PASS remains unchanged; exhaustive item/device coverage and actual listening quality remain outside this review.

| Additional evidence | SHA-256 |
| --- | --- |
| builds/type-02-listening-r2/native/fr-front.png | 8d8c782f5ed5ba6cc43b6b6f0d105557b8cc328e0a4dc5e6e2805bec3175b046 |
| builds/type-02-listening-r2/native/fr-reveal.png | 2be2947728308b874f0b9ac7bf9deeb30f5c7e3d4e9c3934a73883c55fa2112a |
