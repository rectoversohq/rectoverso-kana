# Type 1 factual review — basic kana → sound

Date: 8 November 2026 (Europe/Zurich). Reviewer: delegated Astra fact-checking reviewer.

## Verdict

**QUALIFIED PASS. All 92 source items reviewed; no unresolved factual or semantic blockers.** This verdict covers the current shared inventory, English/French item prose, citations, audio source-input mapping and provenance. Four supplied native screenshots were visually inspected as representative evidence. It is not blanket course, app, artwork or audio-pronunciation approval.

## Findings

- Exactly 46 basic hiragana and 46 basic katakana occur once each. All 92 item IDs, targets, kana, reading labels and audio-input mappings agree with the modern inventory. Small kana, obsolete kana and derived forms have not been accidentally substituted. Sources: [MEXT kana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf), [Bunka romanization Q&A](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/pdf/94336801_01.pdf). The consistent learner label `fu` is acceptable despite the MEXT chart's `hu` spelling.
- `read-hira-306f` / `read-kata-30cf` use `ha`; `read-hira-3078` / `read-kata-30d8` use `he`. These are correct for the isolated-kana scope. No particle-dependent example or phrase has been introduced.
- `read-hira-3092` / `read-kata-30f2` use `o` and share the お recording. The notes explicitly scope the equivalence to modern common Japanese and compare を with お and ヲ with オ respectively. This avoids an invented audible distinction and follows Bunka Q17; it does not claim universal dialectal identity.
- `read-hira-3075` / `read-kata-30d5`: the English/French lip guidance is consistent with [TUFS on ふ](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/03-06-01.php).
- `read-hira-3089`, `read-hira-308a`, `read-hira-308b`, `read-hira-308c`, `read-hira-308d`, `read-kata-30e9`, `read-kata-30ea`, `read-kata-30eb`, `read-kata-30ec`, `read-kata-30ed`: light tongue-tip contact and quick release are reasonable beginner guidance, supported by [TUFS on the r-row](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-02-01.php).
- `read-hira-3046` / `read-kata-30a6`: relaxed lips without strong rounding are supported by the newly attached [TUFS vowel reference](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-07-01.php). The e/o notes are restrained practical advice to keep the isolated vowel steady; they do not make an excessive general claim about all Japanese vowel sequences.
- `read-hira-3093` / `read-kata-30f3`: the notes correctly describe a nasal with its own timing beat and context-dependent realization. The current references now include both [TUFS consonant contexts](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-03-01.php) and [TUFS other/word-final contexts](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-04-01.php). The isolated clip is explicitly described as one example.
- All bilingual note variants were read. French now explicitly says “Lors des révisions suivantes”, preserving the distinction between initial reveal/listen and later recall. Mental recall and optional speaking are stated consistently. No inappropriate exact English/French pronunciation equivalences are introduced.
- The source instruction remains “Recall the sound of the marked kana.” / “Retrouvez le son du kana marqué.” The builder uses the shortened first-use cue “New? Reveal and listen.” / “Nouveau ? Révélez et écoutez.” for reading-card display. Both shortened cues are understandable and contain no incorrect language claim or answer leakage. They are first-use guidance; the later retrieval instruction remains in the answer note. Whether beginners reliably infer the recall task from the shortened native front requires usability observation, not a factual correction.
- All 45 copied audio files and their original source files were rehashed. Every SHA-256, declared input, original source ID, voice (`ja-JP-NanamiNeural`) and rate (`-20%`) matches the approved audition manifest. Sharing each sound across scripts and sharing `o` across お/を/オ/ヲ is consistent with this scope.

## Native evidence inspected

The supplied `en-front.png` and `fr-front.png` show the first target あ marked in gold, with its romanized reading concealed and the shortened cue visible. `fr-reveal.png` shows the matching `a` reading and the beginning of the revised French teaching note. `en-reveal-before-shortening.png` shows a matching `a` reveal and English teaching note, but explicitly represents the earlier prompt. These images support the first-item mapping and representative conceal/reveal behavior only. The French note extends beyond the visible panel; complete prose was reviewed from source.

The parent reports successful import/study/reimport in both languages for the earlier build and a rebuild after shortening. That report is recorded as supplied evidence, not an independently replayed test by this reviewer. Package hashes below identify the current artifacts; this reviewer did not decode and verify every packaged card or independently replay their imports.

## Remaining limitations

- No audio listening assessment or native-speaker clearance was performed or claimed. Matching metadata, hashes and source input does not prove the synthesized spoken output is correct.
- These four screenshots do not prove all 92 image masks, all reveal fractions, katakana rendering, dark appearance, accessibility or every audio-playback placement. The current shortened English reveal is not among the supplied screenshots.
- All reading items have empty `requires` arrays. Isolated reading content has no word prerequisites, and stage/priority values provide hiragana-before-katakana authoring structure. This component review does not establish final-course interleaving, grouped-listening prerequisites or actual app introduction order. Those require later integration review, including the app dependency described in the approved brief.
- No grouped listening, derived rules, word reading, visual comparison, alternate-form or final cumulative items are approved by this Type 1 verdict.
- This review does not assert publication readiness or audio licensing clearance.

## Reviewed artifacts and SHA-256

| Artifact (relative to course workspace) | SHA-256 |
| --- | --- |
| `source-repo/source/questions/01-reading.json` | `00f988e4bba65fb476870d308643b2c31c9697afe85e82f67d59fbb5533536e0` |
| `source-repo/source/kana.json` | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| `source-repo/source/audio/provenance.json` | `6b0bbef765295febdc1491d503b7751d29dc7f8a5daadaba702e2ca7b41a8e94` |
| `source-repo/source/references.json` | `ff509ee6efce6370d165869ff2debee1b6de92dcfd3b9ee2c2d71924691c4590` |
| `source-repo/source/languages/en.json` | `e1c95e4741849988a411b9b51211968573f455962f03029f57df3e24d9ddb66e` |
| `source-repo/source/languages/fr.json` | `343ea85f71dfcadca2c4b634a5a814d4526032ae6f0fd5f9ccde41dd06df2a8c` |
| `source-repo/scripts/source_data.py` | `3c882b0e93a75ea0a274f017d7bd4a596cb2f2ac6067f3c3236b586fae9f69bc` |
| `builds/type-01-reading-r2/packages/Japanese-Kana-en-reading.apkg` | `92a4354adda3f55866afadfe953d593cfc50cf212e93f6c06f9315062002cc38` |
| `builds/type-01-reading-r2/packages/Japanese-Kana-fr-reading.apkg` | `beaba5a16e05ec5831d38c2e42c685560f40b625078270b8985e1a0e66bf8e89` |
| `builds/type-01-reading-r2/native/en-front.png` | `e21ed4ceccf89cb80abd956789a62be35afb5b5279365ddc35037a6bc5588c2a` |
| `builds/type-01-reading-r2/native/fr-front.png` | `904d9f0d3aa02763b2903c1ed3eb2a56daa4ecd970bb703b1b019f2e00e26bf2` |
| `builds/type-01-reading-r2/native/fr-reveal.png` | `ed1e0428fefb0e496dd2e55906a09eec37ffee1d02a6f5a2a7543c3090ad9d18` |
| `builds/type-01-reading-r2/native/en-reveal-before-shortening.png` | `d9f026c07afdcbf519bb47164fb0d240b6f45f2208f2da3d62e6b1d16ee9f991` |

## Complete reviewed item inventory

| Item ID | Kana | Reading |
| --- | --- | --- |
| `read-hira-3042` | あ | a |
| `read-hira-3044` | い | i |
| `read-hira-3046` | う | u |
| `read-hira-3048` | え | e |
| `read-hira-304a` | お | o |
| `read-hira-304b` | か | ka |
| `read-hira-304d` | き | ki |
| `read-hira-304f` | く | ku |
| `read-hira-3051` | け | ke |
| `read-hira-3053` | こ | ko |
| `read-hira-3055` | さ | sa |
| `read-hira-3057` | し | shi |
| `read-hira-3059` | す | su |
| `read-hira-305b` | せ | se |
| `read-hira-305d` | そ | so |
| `read-hira-305f` | た | ta |
| `read-hira-3061` | ち | chi |
| `read-hira-3064` | つ | tsu |
| `read-hira-3066` | て | te |
| `read-hira-3068` | と | to |
| `read-hira-306a` | な | na |
| `read-hira-306b` | に | ni |
| `read-hira-306c` | ぬ | nu |
| `read-hira-306d` | ね | ne |
| `read-hira-306e` | の | no |
| `read-hira-306f` | は | ha |
| `read-hira-3072` | ひ | hi |
| `read-hira-3075` | ふ | fu |
| `read-hira-3078` | へ | he |
| `read-hira-307b` | ほ | ho |
| `read-hira-307e` | ま | ma |
| `read-hira-307f` | み | mi |
| `read-hira-3080` | む | mu |
| `read-hira-3081` | め | me |
| `read-hira-3082` | も | mo |
| `read-hira-3084` | や | ya |
| `read-hira-3086` | ゆ | yu |
| `read-hira-3088` | よ | yo |
| `read-hira-3089` | ら | ra |
| `read-hira-308a` | り | ri |
| `read-hira-308b` | る | ru |
| `read-hira-308c` | れ | re |
| `read-hira-308d` | ろ | ro |
| `read-hira-308f` | わ | wa |
| `read-hira-3092` | を | o |
| `read-hira-3093` | ん | n |
| `read-kata-30a2` | ア | a |
| `read-kata-30a4` | イ | i |
| `read-kata-30a6` | ウ | u |
| `read-kata-30a8` | エ | e |
| `read-kata-30aa` | オ | o |
| `read-kata-30ab` | カ | ka |
| `read-kata-30ad` | キ | ki |
| `read-kata-30af` | ク | ku |
| `read-kata-30b1` | ケ | ke |
| `read-kata-30b3` | コ | ko |
| `read-kata-30b5` | サ | sa |
| `read-kata-30b7` | シ | shi |
| `read-kata-30b9` | ス | su |
| `read-kata-30bb` | セ | se |
| `read-kata-30bd` | ソ | so |
| `read-kata-30bf` | タ | ta |
| `read-kata-30c1` | チ | chi |
| `read-kata-30c4` | ツ | tsu |
| `read-kata-30c6` | テ | te |
| `read-kata-30c8` | ト | to |
| `read-kata-30ca` | ナ | na |
| `read-kata-30cb` | ニ | ni |
| `read-kata-30cc` | ヌ | nu |
| `read-kata-30cd` | ネ | ne |
| `read-kata-30ce` | ノ | no |
| `read-kata-30cf` | ハ | ha |
| `read-kata-30d2` | ヒ | hi |
| `read-kata-30d5` | フ | fu |
| `read-kata-30d8` | ヘ | he |
| `read-kata-30db` | ホ | ho |
| `read-kata-30de` | マ | ma |
| `read-kata-30df` | ミ | mi |
| `read-kata-30e0` | ム | mu |
| `read-kata-30e1` | メ | me |
| `read-kata-30e2` | モ | mo |
| `read-kata-30e4` | ヤ | ya |
| `read-kata-30e6` | ユ | yu |
| `read-kata-30e8` | ヨ | yo |
| `read-kata-30e9` | ラ | ra |
| `read-kata-30ea` | リ | ri |
| `read-kata-30eb` | ル | ru |
| `read-kata-30ec` | レ | re |
| `read-kata-30ed` | ロ | ro |
| `read-kata-30ef` | ワ | wa |
| `read-kata-30f2` | ヲ | o |
| `read-kata-30f3` | ン | n |
