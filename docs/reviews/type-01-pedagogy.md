# Type 01 — Kana → sound: pedagogy review

Reviewer: second Astra reviewer, pedagogy. Review date: 2026-11-08.
Decision: **Qualified PASS for this question type; proceed to type 02.**
No remaining confirmed pedagogy blocker in the reviewed source and representative native evidence. This is not approval of the complete course or exhaustive native/audio QA.

## Scope and evidence

Read the confirmed course brief, the approved 15-card prototype README and builder, all 92 type-01 question records, both basic kana inventories, all distinct bilingual note variants, both language files, and the 45 audio provenance entries. Inspected the four native screenshots listed below.

Source coverage: 46 hiragana and 46 katakana reading questions; unique target coverage and target/answer agreement checked. The source inventory is a component review; its temporary reading-only package order is not the intended interleaved course order.

## Resolved findings

- **Major — read-hira-3042, first encounter:** The original native pill truncated before the instruction telling a beginner how to start. The revised English “New? Reveal and listen.” and French “Nouveau ? Révélez et écoutez.” are fully visible in en-front.png and fr-front.png. This resolves the observed first-exposure guidance problem. Keeping longer explanations in the answer Note is appropriate.
- **Minor — all reading notes, French:** “Lors des révisions suivantes” now matches the English “On later visits” and removes the possible suggestion that a novice should immediately perform another recall attempt on the first encounter.

## Pedagogical assessment

The native front shows the selected あ in gold while concealing its phonetic label. Other visible glyphs do not disclose that label. This supports kana-to-sound retrieval and is consistent with the approved occlusion design. The course must later demonstrate recognition outside chart position, but those later question types need not exist to approve this component.

The reveal screenshots show the answer “a” and the beginning of the teaching Note. The Note explains learning through initial reveal, subsequent recall before revealing, and optional spoken production. The author reports verifying upward-drag reveal, access to the full Note and the native “Listen to the answer” control. That interaction report supports the qualified pass; the supplied static screenshots alone do not show the complete Note or the audio control.

The bilingual guidance preserves the same learning demand. Practical notes address う, steady え/お vowels, ふ, the r-row, and ん. Reading answers for を and ヲ use o and explicitly explain the shared sound without adding particle-use exercises. Mental recall is accepted; no speed criterion, compulsory handwriting, custom multiple-choice interface or automatic pronunciation grading is introduced.

All 45 provenance entries specify ja-JP-NanamiNeural at −20%; all 92 kana entries have corresponding audio filenames. These metadata checks establish declared source consistency, not an auditory pronunciation judgment.

## Remaining checks and limits

- Representative native inspection covers the first hiragana item in the shown light appearance, not all 92 targets, dark mode, every reveal fraction, text size or device.
- The English reveal screenshot predates the shorter pill. It establishes the answer/Note structure before that refinement; the revised English front and revised French reveal are directly pictured.
- Actual audio has not been listened to by this reviewer. No claim of native-listening, accent, segmentation or auditory quality approval is made.
- The native control labels in the French-content screenshots are English. This review approves the localized course guidance; it does not certify French app-interface localization.
- Final integration still requires reading exposure before listening within small batches, grouped-listening prerequisites, appropriate separation, and later word/alternate-form transfer.
- Six new scheduled questions per day includes every exercise type. Authored introduction order and study defaults remain the separate #805 launch dependency. Deck-only metadata is not evidence that those app settings work.
- No mastery gating is implied by authored order. Introductory exposure and successful first reveal are not evidence of mastery.

None of these scope limits requires delaying construction of type 02. They must remain visible in the eventual course-level readiness review.

## SHA-256 evidence snapshot

Paths below are relative to /Volumes/SSD/RectoVerso/raw/japanese-kana-course-20261107/.

| File | SHA-256 |
| --- | --- |
| source-repo/source/questions/01-reading.json | 00f988e4bba65fb476870d308643b2c31c9697afe85e82f67d59fbb5533536e0 |
| source-repo/source/kana.json | 07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4 |
| source-repo/source/audio/provenance.json | 6b0bbef765295febdc1491d503b7751d29dc7f8a5daadaba702e2ca7b41a8e94 |
| source-repo/source/languages/en.json | e1c95e4741849988a411b9b51211968573f455962f03029f57df3e24d9ddb66e |
| source-repo/source/languages/fr.json | 343ea85f71dfcadca2c4b634a5a814d4526032ae6f0fd5f9ccde41dd06df2a8c |
| builds/type-01-reading-r2/native/en-front.png | e21ed4ceccf89cb80abd956789a62be35afb5b5279365ddc35037a6bc5588c2a |
| builds/type-01-reading-r2/native/fr-front.png | 904d9f0d3aa02763b2903c1ed3eb2a56daa4ecd970bb703b1b019f2e00e26bf2 |
| builds/type-01-reading-r2/native/fr-reveal.png | ed1e0428fefb0e496dd2e55906a09eec37ffee1d02a6f5a2a7543c3090ad9d18 |
| builds/type-01-reading-r2/native/en-reveal-before-shortening.png | d9f026c07afdcbf519bb47164fb0d240b6f45f2208f2da3d62e6b1d16ee9f991 |
