# Gentler opening: pedagogy source/build review

Qualified PASS for sequence, prerequisites, figure content and pacing design. No sequence/content blocker. Two minor copy corrections remain noted below; native rendering approval is pending separate evidence. No app or course source was edited by this reviewer.

## Directly verified

All 290 question IDs remain. Comparing question records with HEAD finds only stage, priority and batch changes, with instructions, notes, prerequisites, Japanese displays, readings, accepted answers and audio references unchanged. Every reading batch has exactly two basics; every basic listening question follows both readings in its batch. Across all 287 rolling four-question windows, at most two reading introductions occur. Every listening question is at least two positions after each required introduction: at least one intervening question, not two intervening questions.

The first eight questions are read あ, read い, listen あ, listen い, read う, read え, listen う, listen え. Word いえ and うえ follow at positions 9–10. Reading お and か occur at 11–12; あお at 13 provides eligible decoding before listen か at 14; かお follows at 15. This provides early sound-to-form recall without adding a visual choice grid. First encounter remains reveal-and-listen, not assumed prior knowledge or mastery.

The early katakana sequence places read オ at 152, read カ at 153, word-hon (ほん) at 154 and listen カ at 155. ほん uses previously introduced hiragana and is acceptable consolidation amid new-script work; it is not a previously taught complete word. Grouped お/を listening stays at 107 after readings を105/ん106; オ/ヲ stays at 239 after ヲ237/ン238. Shared ji/zu applications and their accepted alternatives are unchanged. No spelling-choice or handwriting demand is introduced.

All 92 manifest visibleKana sets and preparation regions exactly equal the current target plus earlier introduced same-script kana inside the retained three-row window. Sibling counts equal visible forms minus the target. First あ contains only あ; the second contains あ and い. The generator obtains introduction sets from full dependency order before component filtering and draws only those forms. This removes future-form cues while preserving the target and known neighbors. Snapshot figures do not represent mastery and do not gain new glyphs on subsequent reviews. Existing isolated word/variant/checkpoint questions still provide transfer beyond chart position; source figures alone do not prove learning transfer.

The supported static study preset is deckOrder / four new questions / afterReviews. There is no automatic ramp or mastery lock. Current full EN/FR learner guides match both language descriptions and metadata exactly, state four scheduled questions with both directions counted, preserve reviews-first and reduce/0 guidance, and correctly scope manual setup to file imports. Four is a starting allowance, not a promise of exactly two new kana every day or a ten-minute completion guarantee. The 46-day lower bound for the 182 basic scheduled questions is arithmetically consistent; additional exercises, pauses and reviews extend study. Existing learner choices and non-gallery imports remain outside automatic preset application.

## Minor copy qualifications

At this snapshot, source/learner-guide.json course.noteBody still says “These prototype settings are manual.” / “Ces réglages du prototype sont manuels.” The full guide correctly limits this to file imports. Make the compact answer note channel-neutral (“Check these settings”) or explicitly file-import-specific, so fresh gallery learners do not receive contradictory setup guidance.

The brief calls the moved ほん exercise “a familiar hiragana word.” Its constituent kana are familiar, but this complete word is first presented at position 154. “An already-readable hiragana word” is the precise description. Neither issue changes the verified sequence.

## Evidence and limits

Inspected ci-final/result.json: pass, both languages/all seven types, independent artwork bytes/package semantics exact and study progress preserved. Combined EN/FR Anki evidence passes import/frontBack/media/realStudy/reimport. migration-en.json preserves all states, review log, note/card/model/template identities and updated media. pixel-audit.json records 368 table comparisons, 92 unchanged standalone question images, and unchanged other artwork; changes are removal of future glyphs/readings and unused dividers, retaining existing visible pixels and mask positions. These reports were read, not rerun by this reviewer. Native phone checks are pending; prior native passes cannot automatically approve the new sparse opening. No native-speaker listening, VoiceOver, publication or complete curriculum learning-effectiveness claim is made.

## SHA-256 snapshot

- `rectoverso.json`: `673277774391842e07de2acc8c832a30c04a54d3d0fbe06a7bc67d3cf306751a`
- `source/learner-guide.json`: `8f71b2369646b15ba2d41794da52b2b4c0417bf26cf5119c203f0f5dc7f24fe8`
- `source/languages/en.json`: `21de9a7b30b24f001862f203eb6e2d0e61d0c5ef31691a63860fbed84a8af985`
- `source/languages/fr.json`: `a5586af7e45a13947730e592ee793353389f6dc797b1d92a30edd55d356b17da`
- `source/questions/01-reading.json`: `8710d26c08f7878e4dffce6c2b6916b6c474450e45803177353fe5ca30826612`
- `source/questions/02-listening.json`: `2adb285ace6fc833f4e01cd7fd3942b050699dd1b3225a07850b43f05ff1a931`
- `source/questions/04-words.json`: `d84f96200ea44b602572114e65e2dbc1e314e6d05fa7a624df50439beb9d12d0`
- `source/questions/05-contrasts.json`: `d59a726d521430a40c91bc973088325f191e1ccc7017ed2c10ba2138a300bc64`
- `scripts/source_data.py`: `75c2e0a70815b22d7b84e70e9b08fb0d49d59d4e65a54a05402cb48f41efea9a`
- `scripts/render_artwork.py`: `547c7535365ef8efca75c571f2895566bb6e2a94570a8ab1dbc7d942226b95d8`
- `artwork/artwork.json`: `cd3bff442039695db152776ee7f824cdb4840582121ed00dcb9ccc7e5196b8df`
- `docs/course-brief.md`: `54d3819b88805a349cde92f9978fc4e29ec34be89a6e38d264c11412e11e9ca5`

## Corrected copy and native iPhone follow-up

Both minor copy findings above are resolved in the current source: course.noteBody explicitly scopes manual setup to file imports in EN/FR, and the brief now says “an already-readable hiragana word.” These corrections supersede the outstanding-copy qualifications in the original snapshot.

Qualified native visual/pedagogy PASS for the directly inspected iPhone samples: en-a-front.png, en-i-front.png, en-u-front.png, en-sa-front.png, en-kata-a-front.png, en-a-listening.png, en-i-answer.png, fr-i-front.png and fr-kata-i-front.png.

The first front presents only complete gold あ with its concealed reading mask. The second adds prior あ in black beside gold い; French dark does the same with sufficient visual distinction. The katakana opening presents ア alone, then prior ア beside gold イ. The later う and さ samples retain a clear target and mask while showing only previously introduced neighbors. Some peripheral known glyphs extend beyond the viewport; the target remains complete and unambiguous. No future kana or romaji is visible in these samples. The listening front remains sound-only with “Which hiragana?”, preserving recall rather than a visual choice task. The ready い answer shows the correct i clearly, with the neighboring あ reading still concealed.

This evidence supports the gentler visual opening and the intended reading-to-listening transition; it does not prove mastery or transfer. The earlier blank answer capture was a failed readiness capture retained separately, not the successful final answer state. The corrected screenshot visibly shows “1 OF 1 LETTER” and i. Native replay/audio behavior and the normal recorded path are not newly approved from these still images; parent reports that path is still being finalized. No Duo check was performed for this revision. French deck text is inspected within English app chrome. Existing accessibility/spoken-ordinal limitations are not cleared by these images.

### Refreshed source hashes

- `source/learner-guide.json`: `8f71b2369646b15ba2d41794da52b2b4c0417bf26cf5119c203f0f5dc7f24fe8`
- `docs/course-brief.md`: `54d3819b88805a349cde92f9978fc4e29ec34be89a6e38d264c11412e11e9ca5`
- `scripts/source_data.py`: `75c2e0a70815b22d7b84e70e9b08fb0d49d59d4e65a54a05402cb48f41efea9a`
- `scripts/render_artwork.py`: `547c7535365ef8efca75c571f2895566bb6e2a94570a8ab1dbc7d942226b95d8`
- `rectoverso.json`: `673277774391842e07de2acc8c832a30c04a54d3d0fbe06a7bc67d3cf306751a`

### Selected native evidence hashes

- `native/en-a-front.png`: `21490a75d7040f545654801b378360066a6af742127a69c62a4ce7764624ce6b`
- `native/en-i-front.png`: `4f5d4f59cb5dbc7b457bfa4bec3147b608116098a109c51f96ed3450e67b69d6`
- `native/en-a-listening.png`: `20fb8e87d5198abf585d5b8a835dd4cd6da29b970108db77e5ef7a1d87fbf8ca`
- `native/en-i-answer.png`: `cc4ec5f47f35ea3a2b694a4ad42e881d802abdbe9ea06239675f6bb87b5a666b`
- `native/fr-i-front.png`: `aa99cea092d29b47ef748c79f6db58967fdb94d747897170c7ff565052b9434f`
- `native/fr-kata-i-front.png`: `67a2081cd90fb6effe371054c027fd9e969aaa7d3e54c6ba046b51e11a6c6817`
