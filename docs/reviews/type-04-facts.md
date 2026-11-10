# Type 04 — short-word decoding factual review

Verdict: **QUALIFIED PASS** for the current 36-item source, bilingual factual content, prerequisite sequence, generated fields, and audio-input/provenance mapping. No factual blockers remain. This is not a listening or native-app clearance.

Reviewed 2026-11-08 by the delegated Astra factual reviewer. Scope: all 24 hiragana and 12 katakana words; all English/French glosses and notes; all 31 new synthesis requests and five reused audition clips; current source-data builder; supplied English/French Anki evidence. No implementation files were edited. No device or simulator was driven.

## Findings

All 36 readings are correct for the displayed kana and intended lexical senses. English and French glosses are appropriate context, not exhaustive dictionary definitions. The kana may have other meanings (for example はな, あお, たこ); this does not make a kana-decoding question ambiguous, because its requested reading remains the same. No pitch-accent discrimination or unique lexical meaning is claimed.

The final builder puts only the kana word on Front and leaves Meta empty. Meaning is in the answer-side Example field. This removes answer clues such as sushi, memo, and tomato from the prompt. Back contains the expected romanization and recording; the bilingual notes explicitly prioritize accurate decoding over speed and say the meaning is not for memorization. The four kanji synthesis inputs never appear in the learner-facing front or explanation.

The timing explanations are accurate: `word-byoin` has four morae (びょ・う・い・ん); `word-kyo` two (きょ・う); `word-happa` three (は・っ・ぱ); `word-jusu` three (ジュ・ー・ス); `word-poketto` four (ポ・ケ・ッ・ト). The closure explanations are specifically appropriate to p and t. `word-okaasan` preserves long a, and `word-takushi` correctly lengthens the i in シ. The romanization preserves vowel length: byōin, kyō, okaasan, takushī, jūsu. Doubled consonants in happa/poketto are correct.

The current 252-item topological sequence resolves every declared prerequisite. Inspection of the displayed words also found no required basic form or productive rule introduced too late: 18 basic hiragana words, six hiragana rule applications, five basic katakana words, seven katakana rule applications. In particular, びょ and ジュ correctly reuse previously taught small-kana and voicing principles. This establishes source-order readiness; it does not establish that an app scheduler enforces this order or the approved daily introduction limit.

## Complete item audit

Every row below passed reading, bilingual gloss, intended synthesis-input mapping, and prerequisite review. “Input” is authoring metadata, not learner-visible kanji teaching.

| Item ID | Display | Reading | English | Français | Input |
|---|---|---|---|---|---|
| word-ao | あお | ao | blue | bleu | あお |
| word-ie | いえ | ie | house | maison | いえ |
| word-ue | うえ | ue | above | au-dessus | うえ |
| word-kao | かお | kao | face | visage | かお |
| word-ike | いけ | ike | pond | étang | いけ |
| word-shio | しお | shio | salt | sel | しお |
| word-sushi | すし | sushi | sushi | sushi | すし |
| word-tako | たこ | tako | octopus | poulpe | たこ |
| word-kuchi | くち | kuchi | mouth | bouche | くち |
| word-neko | ねこ | neko | cat | chat | ねこ |
| word-inu | いぬ | inu | dog | chien | いぬ |
| word-fune | ふね | fune | boat | bateau | ふね |
| word-hana | はな | hana | flower | fleur | 花 |
| word-heya | へや | heya | room | pièce | へや |
| word-yama | やま | yama | mountain | montagne | やま |
| word-sora | そら | sora | sky | ciel | そら |
| word-yuki | ゆき | yuki | snow | neige | 雪 |
| word-hon | ほん | hon | book | livre | ほん |
| word-jikan | じかん | jikan | time | temps | じかん |
| word-sanpo | さんぽ | sanpo | walk | promenade | さんぽ |
| word-byoin | びょういん | byōin | hospital | hôpital | 病院 |
| word-kyo | きょう | kyō | today | aujourd’hui | 今日 |
| word-okaasan | おかあさん | okaasan | mother | mère | おかあさん |
| word-happa | はっぱ | happa | leaf | feuille | はっぱ |
| word-kamera | カメラ | kamera | camera | appareil photo | カメラ |
| word-memo | メモ | memo | memo | note | メモ |
| word-tomato | トマト | tomato | tomato | tomate | トマト |
| word-hoteru | ホテル | hoteru | hotel | hôtel | ホテル |
| word-miruku | ミルク | miruku | milk | lait | ミルク |
| word-basu | バス | basu | bus | bus | バス |
| word-pan | パン | pan | bread | pain | パン |
| word-terebi | テレビ | terebi | television | télévision | テレビ |
| word-takushi | タクシー | takushī | taxi | taxi | タクシー |
| word-rajio | ラジオ | rajio | radio | radio | ラジオ |
| word-jusu | ジュース | jūsu | juice | jus | ジュース |
| word-poketto | ポケット | poketto | pocket | poche | ポケット |

## Primary-source checks

- [MEXT hiragana/katakana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf): base kana inventory and readings. This course consistently uses shi/chi/tsu/fu-style pedagogical romanization.
- [TUFS small-kana combinations](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-11-01.php): joined small ゃ/ゅ/ょ form one mora; especially relevant to `word-byoin`, `word-kyo`, and `word-jusu`. TUFS explicitly contrasts びょういん and びよういん.
- [TUFS long vowels](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-02-01.php): vowel length adds a mora; supports `word-byoin`, `word-kyo`, `word-okaasan`, `word-takushi`, and `word-jusu`.
- [TUFS small っ](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-01-01.php): the timing and closure explanation used for `word-happa` and `word-poketto`.
- [Japan Foundation Irodori direct word list](https://www.irodori.jpf.go.jp/assets/data/wordlist_Y.pdf): selected lexical reading/meaning checks, including 花/はな, 雪/ゆき, 病院/びょういん. The source now names this direct reference for those three items. It is not presented as a line-by-line source for every word.
- [Japan Foundation Irodori lesson 4](https://www.irodori.jpf.go.jp/assets/data/elementary01/pdf/Y_L04_au.pdf): 今日/きょう with the intended “today” sense for `word-kyo`.

The generic Irodori landing-page citation is supplementary teaching context; it does not independently verify all 36 glosses. Common-word readings and bilingual glosses were individually reviewed, rather than inferred from that citation.

## Audio and build evidence

All 36 source MP3 hashes match provenance. All entries specify ja-JP-NanamiNeural at −20%. New requests match provenance exactly, including 花→はな, 雪→ゆき, 病院→びょういん, 今日→きょう. These are legitimate intended readings; metadata cannot establish that synthesis actually selected them. 今日 has other readings in other contexts, so `word-kyo` especially needs listening confirmation.

The five reused clips are `word-shio`, `word-fune`, `word-heya`, `word-hon`, and `word-sanpo`. Their bytes, source inputs, and original audition-manifest hashes match. Their provenance says approved audition source, explicitly not native-speaker review. The other 31 clips retain listeningReview=pending.

Read-only execution of the builder verified all 72 language-specific field sets: exact kana Front, blank Meta, exact romanization/audio Back, localized answer-side meaning, and complete localized Note. No kanji or audio leaked into a word front. All 72 supplied Anki evidence entries match current Front, Back, instruction and Note, and all media hashes match current source. Both supplied logs report 36-card import, front/back, media, real study and progress-preserving reimport passing. These logs were inspected and cross-checked, not independently replayed by this reviewer.

## Remaining limitations

- No listening or native-speaker audio clearance is given. Neither file hashes, source strings, signal checks nor successful playback establish pronunciation quality, chosen reading, or absence of TTS artifacts.
- Native RectoVerso validation remains pending by owner request. This review does not certify visual layout, reveal behavior, accessibility, or runtime scheduling.
- Isolated 36-card component packages demonstrate this question type; they are not a substitute for the full course prerequisite sequence.
- No systematic pitch-accent instruction or vocabulary-memorization outcome is approved or implied.

## Reviewed snapshot (SHA-256)

Hashes bind this verdict to the reviewed source and supplied evidence. Audio-level hashes are in the hashed provenance file and were individually checked.

| File (relative to course root) | SHA-256 |
|---|---|
| source-repo/source/questions/04-words.json | `d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81` |
| source-repo/source/audio/requests-type-04.json | `ba6ffba05c2cc3a464f253d1ebf87f51b5e5f55c41cebd7f0f8bc283c8cabb3f` |
| source-repo/source/audio/provenance.json | `16d27fd23a8376f3d12827c03c64b86f361c98de23f7a15c4981eeaebf406127` |
| source-repo/source/references.json | `71caa85ddff1260b0362ebcbbe71985327274f82551d1217badf02522ead11df` |
| source-repo/scripts/source_data.py | `ce1df07437875ed97199b911164de57b79ca26583421b7eda7ee648a6a814a67` |
| source-repo/source/languages/en.json | `e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a` |
| source-repo/source/languages/fr.json | `1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b` |
| source-repo/source/kana.json | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| source-repo/source/questions/01-reading.json | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| source-repo/source/questions/02-listening.json | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| source-repo/source/questions/03-rules.json | `3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc` |
| builds/type-04-words/packages/Japanese-Kana-en-word.apkg | `93717a0b89f90940a9ab08a650c8a0b2fd152e89570d4a0025d3fe3e4c4efe50` |
| builds/type-04-words/packages/Japanese-Kana-fr-word.apkg | `26f694d63264f9d23e56fa663f981d2f64c64555a35a7a7691760ad851c052d1` |
| builds/type-04-words/evidence/en/anki-verification.json | `f0e3e4d360bab49775736a870d93daef36614837720fd8820269d601ec3fe501` |
| builds/type-04-words/evidence/fr/anki-verification.json | `a1dcda03f880d10cb73868356185f62e9efe85f8ac3e7f2c23df31c879ea1743` |
