# Type 2 factual review — sound → kana

Date: 8 November 2026 (Europe/Zurich). Reviewer: delegated Astra fact-checking reviewer.

## Verdict

**QUALIFIED PASS. All 90 current items inspected; no unresolved factual or semantic blockers.** This covers the shared listening source, English/French instructions and notes, accepted sets, source audio mappings, authored prerequisite order, and the actual builder's generated listening fields in both languages. Native Type 2 evidence was not available during this review.

## Corrections verified

The initial snapshot discarded `answerReading` and used definite singular prompts even for grouped sounds. Both issues are resolved in the snapshot identified below. Every generated answer now includes the accepted kana, romaji and audio; every English prompt requests “a matching” form and every French prompt requests “un ... correspondant à ce son”. This allows one valid form rather than implying a unique spelling. No answer label was added to a recall front.

## Findings and primary-source checks

- Exactly 90 unique items: 45 sounds per script, covering the 46 basic characters per script after grouping お/を and オ/ヲ. Every accepted set, reading label, requested script and declared audio input was checked. No incorrect mapping, missing basic form or duplicate sound task was found. [MEXT kana inventory](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf)
- `listen-hira-o` accepts exactly お and を; `listen-kata-o` accepts exactly オ and ヲ. Both use the approved お clip. Both explanatory notes correctly limit the equivalence to modern common Japanese and distinguish this sound task from word spelling. Either accepted form suffices. [Bunka romanization Q&A, Q17](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/pdf/94336801_01.pdf)
- `listen-hira-ha` / `listen-kata-ha` accept は / ハ, and `listen-hira-he` / `listen-kata-he` accept へ / ヘ, using ordinary isolated readings. Particle readings remain outside scope. じ/ぢ and ず/づ belong to later marked-form coverage; they are not omissions from this basic 90-item inventory. Their grouped-answer policy still applies if corresponding listening tasks are authored later.
- All bilingual prompt variants and explanatory-note variants were reviewed. Mental shape recall suffices and writing is optional. The source does not add a vocabulary objective, grammatical task or exaggerated pronunciation claim. For `listen-hira-n` / `listen-kata-n`, the reused isolated nasal is only the current recording example; this verdict does not imply that ん/ン always has one invariant phonetic realization. [TUFS nasal contexts](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-03-01.php), [TUFS other/word-final contexts](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-04-01.php)
- All 90 `requires` sets exactly equal the IDs of their accepted forms. Running the actual `ordered()` function on current reading/listening data confirmed that every accepted form's reading task comes before listening, with at least one intervening item. All reading tasks within a batch precede that batch's listening tasks. The 18 batches per script use row-family chunks of 3+2, three y-row forms, and a final wa/o/n group. Grouped o listening is correctly delayed until お and を, or オ and ヲ, have both been introduced.
- Running actual `inputs()` expansion for both languages checked all 180 generated fields: Front contains precisely the script-specific prompt plus sound tag, with no displayed kana or romaji answer; Back contains every accepted form, the correct romaji label and the same sound tag. Examples are `お / を · o` and `シ · shi`. The audio filename contains its sound label internally, but the authored template does not display that filename; native rendering remains to be checked.
- All tasks reuse the same 45 Nanami −20% files whose source inputs and provenance were approved in Type 1. Their current copied-file hashes were rechecked against `source/audio/provenance.json`; no changed file, new voice, speed or synthesized input was introduced by Type 2.

## Scope and remaining limitations

- No native Type 2 screenshots, playback behavior or import/reimport were independently reviewed here. Package hashes below identify artifacts available at review time; their 180 packaged cards were not independently decoded. Source expansion checks are not a substitute for proving that those artifacts contain the same content or that the installed app displays it correctly.
- No audio listening assessment or native-speaker clearance is claimed. Correct filenames, source inputs, hashes and signal metadata do not establish the correctness of synthesized speech.
- The order check proves authoring behavior, not actual app scheduling, spaced-review placement or learner mastery. The standalone listening preview filters out reading tasks after ordering and is an audition component, not a self-contained beginner sequence. The complete-course authored-order app dependency remains a launch requirement.
- No later rule, word, comparison, alternate-form or cumulative-reading items are approved by this verdict. Publication readiness and audio rights are outside its scope.

## Reviewed snapshot and SHA-256

| Artifact (relative to course workspace) | SHA-256 |
| --- | --- |
| `source-repo/source/questions/02-listening.json` | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| `source-repo/source/questions/01-reading.json` | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| `source-repo/source/kana.json` | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| `source-repo/source/audio/provenance.json` | `6b0bbef765295febdc1491d503b7751d29dc7f8a5daadaba702e2ca7b41a8e94` |
| `source-repo/source/references.json` | `ff509ee6efce6370d165869ff2debee1b6de92dcfd3b9ee2c2d71924691c4590` |
| `source-repo/scripts/source_data.py` | `01068ba6cd7171b74deaa79e0310c818f48785b80407360f722e1edab795aabb` |
| `builds/type-02-listening/packages/Japanese-Kana-en-listening.apkg` | `0efc5798fdbe7dd6f5a5c088567d420429c6f0685e623c60e7df3276996cd79f` |
| `builds/type-02-listening/packages/Japanese-Kana-fr-listening.apkg` | `a306062bed30e9ff825f365457afea00c922c1e3413787d77dad6213a0209f0b` |

## Complete reviewed item inventory

| Item ID | Accepted forms | Sound label |
| --- | --- | --- |
| `listen-hira-a` | あ | a |
| `listen-hira-i` | い | i |
| `listen-hira-u` | う | u |
| `listen-hira-e` | え | e |
| `listen-hira-o` | お / を | o |
| `listen-hira-ka` | か | ka |
| `listen-hira-ki` | き | ki |
| `listen-hira-ku` | く | ku |
| `listen-hira-ke` | け | ke |
| `listen-hira-ko` | こ | ko |
| `listen-hira-sa` | さ | sa |
| `listen-hira-shi` | し | shi |
| `listen-hira-su` | す | su |
| `listen-hira-se` | せ | se |
| `listen-hira-so` | そ | so |
| `listen-hira-ta` | た | ta |
| `listen-hira-chi` | ち | chi |
| `listen-hira-tsu` | つ | tsu |
| `listen-hira-te` | て | te |
| `listen-hira-to` | と | to |
| `listen-hira-na` | な | na |
| `listen-hira-ni` | に | ni |
| `listen-hira-nu` | ぬ | nu |
| `listen-hira-ne` | ね | ne |
| `listen-hira-no` | の | no |
| `listen-hira-ha` | は | ha |
| `listen-hira-hi` | ひ | hi |
| `listen-hira-fu` | ふ | fu |
| `listen-hira-he` | へ | he |
| `listen-hira-ho` | ほ | ho |
| `listen-hira-ma` | ま | ma |
| `listen-hira-mi` | み | mi |
| `listen-hira-mu` | む | mu |
| `listen-hira-me` | め | me |
| `listen-hira-mo` | も | mo |
| `listen-hira-ya` | や | ya |
| `listen-hira-yu` | ゆ | yu |
| `listen-hira-yo` | よ | yo |
| `listen-hira-ra` | ら | ra |
| `listen-hira-ri` | り | ri |
| `listen-hira-ru` | る | ru |
| `listen-hira-re` | れ | re |
| `listen-hira-ro` | ろ | ro |
| `listen-hira-wa` | わ | wa |
| `listen-hira-n` | ん | n |
| `listen-kata-a` | ア | a |
| `listen-kata-i` | イ | i |
| `listen-kata-u` | ウ | u |
| `listen-kata-e` | エ | e |
| `listen-kata-o` | オ / ヲ | o |
| `listen-kata-ka` | カ | ka |
| `listen-kata-ki` | キ | ki |
| `listen-kata-ku` | ク | ku |
| `listen-kata-ke` | ケ | ke |
| `listen-kata-ko` | コ | ko |
| `listen-kata-sa` | サ | sa |
| `listen-kata-shi` | シ | shi |
| `listen-kata-su` | ス | su |
| `listen-kata-se` | セ | se |
| `listen-kata-so` | ソ | so |
| `listen-kata-ta` | タ | ta |
| `listen-kata-chi` | チ | chi |
| `listen-kata-tsu` | ツ | tsu |
| `listen-kata-te` | テ | te |
| `listen-kata-to` | ト | to |
| `listen-kata-na` | ナ | na |
| `listen-kata-ni` | ニ | ni |
| `listen-kata-nu` | ヌ | nu |
| `listen-kata-ne` | ネ | ne |
| `listen-kata-no` | ノ | no |
| `listen-kata-ha` | ハ | ha |
| `listen-kata-hi` | ヒ | hi |
| `listen-kata-fu` | フ | fu |
| `listen-kata-he` | ヘ | he |
| `listen-kata-ho` | ホ | ho |
| `listen-kata-ma` | マ | ma |
| `listen-kata-mi` | ミ | mi |
| `listen-kata-mu` | ム | mu |
| `listen-kata-me` | メ | me |
| `listen-kata-mo` | モ | mo |
| `listen-kata-ya` | ヤ | ya |
| `listen-kata-yu` | ユ | yu |
| `listen-kata-yo` | ヨ | yo |
| `listen-kata-ra` | ラ | ra |
| `listen-kata-ri` | リ | ri |
| `listen-kata-ru` | ル | ru |
| `listen-kata-re` | レ | re |
| `listen-kata-ro` | ロ | ro |
| `listen-kata-wa` | ワ | wa |
| `listen-kata-n` | ン | n |
