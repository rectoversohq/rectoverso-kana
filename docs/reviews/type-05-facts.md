# Type 05 — audio-to-kana comparisons factual review

Verdict: **QUALIFIED PASS** for all 12 items: target/reading mappings, bilingual shape cues and instructions, source audio mapping, prerequisites and generated fields. No factual blockers remain. Native rendering and listening are outside this verdict.

Reviewed 2026-11-08 by the delegated Astra factual reviewer. Read-only inspection of all 12 source records, the source-data builder, kana/audio provenance, six unique supplied light font proofs, and both supplied Anki evidence logs. Only this review report was written; no implementation, device or simulator was changed.

## All-item audit

Each displayed pair has distinct readings, so the prompt audio identifies exactly one available kana. The answer is the kana itself plus its reading, not a position. English and French instructions agree: Identify / Identifiez correctly describe recognition among visible alternatives, without overclaiming free recall. Reusing a hiragana-authored basic recording for the corresponding katakana sound is correct.

| Item ID | Display | Correct target | Reading | Source audio input | Full-source position (1-based) |
|---|---|---|---|---|---|
| contrast-nu-me-nu | ぬ　め | ぬ | nu | ぬ | 110 |
| contrast-nu-me-me | ぬ　め | め | me | め | 113 |
| contrast-ru-ro-ru | ろ　る | る | ru | る | 111 |
| contrast-ru-ro-ro | ろ　る | ろ | ro | ろ | 114 |
| contrast-ne-re-ne | ね　れ | ね | ne | ね | 112 |
| contrast-ne-re-re | ね　れ | れ | re | れ | 115 |
| contrast-shi-tsu-shi | ツ　シ | シ | shi | し | 234 |
| contrast-shi-tsu-tsu | ツ　シ | ツ | tsu | つ | 237 |
| contrast-so-n-so | ソ　ン | ソ | so | そ | 235 |
| contrast-so-n-n | ソ　ン | ン | n | ん | 238 |
| contrast-ku-ke-ku | ケ　ク | ク | ku | く | 236 |
| contrast-ku-ke-ke | ケ　ク | ケ | ke | け | 239 |

## Shape cues

The six unique supplied proof images were visually inspected. Their cues are accurate descriptions of the pictured print forms:

- `contrast-nu-me-{nu,me}`: the lower-right closed loop distinguishes ぬ from め. The note usefully limits the observation to the printed style.
- `contrast-ru-ro-{ru,ro}`: る has a bottom loop absent from ろ; the note also asks learners to compare the whole form.
- `contrast-ne-re-{ne,re}`: ね has a right loop; れ ends with an open sweep. French conveys the same distinction.
- `contrast-shi-tsu-{shi,tsu}`: the two short marks of シ cluster at the left; those of ツ at the top. This is a spatial cue, not a claim that every stroke has an invariant angle.
- `contrast-so-n-{so,n}`: ン sweeps more horizontally near the bottom; ソ has a steeper long stroke. Both translations explicitly distinguish the shape cue from stroke-order instruction.
- `contrast-ku-ke-{ku,ke}`: the crossing bar/extra crosswise stroke of ケ distinguishes it from ク. The supplied print forms support this practical cue.

The [MEXT hiragana/katakana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf) independently supports all 12 base character/readings and their script identities. The shape descriptions are reviewer-checked observations of the supplied proof forms, not quotations or claims of MEXT endorsement of this wording. No rule about all fonts, handwriting styles, or stroke order is inferred from the proofs.

## Sequence, fields and audio

Both candidate forms in every pair are required and introduced earlier in the current 264-item source order. Each pair's second target follows its first target with two other comparisons intervening. Across all 12 items there are six left-position and six right-position targets. Within a pair the display stays stable and both members are targeted; this avoids an always-left answer pattern. It does not establish runtime randomization or prevent familiarity with repeated displays.

All 24 generated language-specific field sets were checked. Front contains exactly the two kana and the expected prompt-audio marker; Meta contains the localized instruction. Back contains the correct kana, romanized reading and answer audio. Notes appear after reveal and teach the visible distinction without introducing a different task. No romanized answer appears in visible front text. These are self-graded recognition/comparison cards; source data does not claim a typed-answer acceptance parser.

All 12 source audio files match the corresponding basic-kana assignment and SHA-256 provenance. All are reused Nanami ja-JP-NanamiNeural recordings at −20%; no new synthesis is introduced by this type. Hiragana inputs for katakana targets preserve the same basic sounds, including ん→ン. This is file/input verification, not a new audio audition or native-speaker approval.

Both supplied Anki logs report 12 cards and passing import, front/back, media, real study and progress-preserving reimport. All 24 logged front/answer/instruction/note entries and all media hashes match current generated content. The reviewer inspected these logs but did not independently replay Anki.

Evidence-order check (en): matches the final spaced source order.

Evidence-order check (fr): matches the final spaced source order.

## Qualifications

Native app validation is pending. The supplied font proofs are not native screenshots and do not establish the app's font fallback, sizing, clipping, accessibility or audio controls. Actual font/rendering differences could require revisiting a cue. The approved course introduction order and daily limit still require runtime enforcement; an isolated component package cannot demonstrate prior basic-kana learning. No fresh listening/native-speaker clearance is claimed.

## Reviewed snapshot (SHA-256)

Audio hashes are individually checked against the hashed provenance manifest. The proof-artwork manifest binds the pictured forms used for cue review.

| File (relative to course root) | SHA-256 |
|---|---|
| source-repo/source/questions/05-contrasts.json | `efc69f8e0cc51ef40c06f10f3ee28db4d5c7acdc55d9c865fb7b2a827b02d79b` |
| source-repo/source/kana.json | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| source-repo/source/audio/provenance.json | `16d27fd23a8376f3d12827c03c64b86f361c98de23f7a15c4981eeaebf406127` |
| source-repo/source/references.json | `71caa85ddff1260b0362ebcbbe71985327274f82551d1217badf02522ead11df` |
| source-repo/scripts/source_data.py | `3a635dd9ca85c859db5ddbdcd682a6c531ca4af11ccc62a7b7419bb01694b93c` |
| source-repo/source/languages/en.json | `e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a` |
| source-repo/source/languages/fr.json | `1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b` |
| builds/type-05-contrasts/proof-artwork/artwork.json | `2457e4ffbc873ee0aff132af0ab4f0c0f0cc58783b5a5f096d9962757bbd0870` |
| source-repo/source/questions/01-reading.json | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| source-repo/source/questions/02-listening.json | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| source-repo/source/questions/03-rules.json | `3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc` |
| source-repo/source/questions/04-words.json | `d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81` |
| builds/type-05-contrasts-r2/packages/Japanese-Kana-en-contrast.apkg | `658502c423a833ae9b48b16270dcfa9d530f7e209ae5fa44617485ff88b03b20` |
| builds/type-05-contrasts-r2/packages/Japanese-Kana-fr-contrast.apkg | `6ec523a3f123b341aca9eb991f58baa5342b31b19eeb8831e23dafbdb4f9ff8b` |
| builds/type-05-contrasts-r2/evidence/en/anki-verification.json | `cea9062f1bacc4c8de8de724614f42b20d95553cd6f7a0ab15e4603fc8af9979` |
| builds/type-05-contrasts-r2/evidence/fr/anki-verification.json | `4b950f6fc329ed0a875ec9ce1385f38b49176dd48307b4e65ac58bf1ff6ef2b7` |
