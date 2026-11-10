# Type 3 factual review — selected reading-rule applications

Date: 8 November 2026 (Europe/Zurich). Reviewer: delegated Astra fact-checking reviewer.

## Verdict

**QUALIFIED PASS. All 34 current items reviewed: 16 hiragana and 18 katakana. No unresolved factual or semantic blockers in this snapshot.** The verdict covers readings, English/French explanations and lexical glosses, prerequisites, current generated fields, and new audio request/provenance/file correspondence. Audio listening and native behavior remain pending.

## Corrections verified

`rule-hira-long-ou` now explains the actual sequence とう in とうふ: う lengthens the o vowel of と, and とう occupies two timing beats. It no longer incorrectly points to a literal おう sequence inside that word. `rule-hira-long-oo` now describes an o-vowel kana followed by う or お and illustrates こお → kō. Both languages preserve the distinction between pronunciation and lexical spelling. `rule-kata-extension-fi` now specifies “photographic film” / “pellicule photographique”, resolving the former broad gloss “film”.

## Content findings and primary sources

- All ten mark-family items (`rule-hira-marks-g/z/d/b/p` and `rule-kata-marks-g/z/d/b/p`) give correct complete rows. The d-row explicitly maps ぢ/ヂ to ji and づ/ヅ to zu; the notes correctly state the modern-common-Japanese mergers with じ/ジ and ず/ズ without claiming that spelling is interchangeable. The h→b/p wording describes the h-row family, and the supplied rows correctly include bu/pu. Sources: [MEXT kana inventory](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf), [Bunka romanization Q&A, Q17](https://www.bunka.go.jp/seisaku/kokugo_nihongo/kokugo_shisaku/pdf/94336801_01.pdf), [Bunka modern kana spelling](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gendaikana/honbun_dai2.html).
- The six contracted-sound examples (`rule-hira-kya`, `rule-hira-shu`, `rule-hira-cho`, `rule-kata-kya`, `rule-kata-shu`, `rule-kata-cho`) correctly distinguish small ゃ/ゅ/ょ or ャ/ュ/ョ from full-size forms. Each example is one mora, without an additional separate i. The French term “more” is appropriate. [TUFS contracted sounds](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/01-11-01.php)
- `rule-hira-small-tsu` correctly reads きって as kitte and contrasts it with きて. `rule-kata-small-tsu` correctly reads ベッド as beddo. Both words have three morae; the displayed ki·(t)·te and be·(d)·do are timing guides, not instructions to insert a vowel. Closure guidance is appropriate to these stop-consonant examples; it should not be generalized to fricative examples where the consonant is sustained rather than replaced by silence. [TUFS small っ](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-01-01.php)
- All seven hiragana length items (`rule-hira-long-aa/ii/uu/ee/ou/oo/ei`) give correct readings. A long vowel spans two morae; the added duration is one mora. The おばあさん/おばさん comparison is valid. The revised tōfu/kōri explanations preserve their different kana spellings. `rule-hira-long-ei` appropriately says とけい commonly has long e, retains the orthographic label tokei and does not require every e+i sequence to merge. [TUFS vowel length](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-02-01.php), [Bunka spelling exceptions and えい note](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gendaikana/honbun_dai2.html)
- `rule-kata-long-bar` correctly reads コーヒー as kōhī. The two long vowels each span two morae; the whole word has four. The bar extends the preceding vowel and is not a separately pronounced syllable. The dot between kō and hī groups syllables, while the prose explicitly states each long vowel's two-beat duration. [TUFS vowel length](https://www.coelang.tufs.ac.jp/mt/ja/pmod/practical/02-02-01.php)
- All eight extension items (`rule-kata-extension-fa/fi/fe/fo/ti/che/she/di`) use the correct small vowel and reading. ティ differs from チ, and ディ differs from ジ. The wording presents selected applications rather than claiming an exhaustive foreign-sound inventory or an exact reproduction of the source language. These forms are present in Bunka's first loanword table. [Bunka loanword spelling, first table and detailed notes](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/pdf/94380801_03.pdf)
- Every EN/FR lexical gloss in the inventory below was reviewed and is acceptable as one contextual sense, not an exhaustive dictionary definition. Family words may also have other address/reference uses; no grammar lesson is implied. フィルム is now explicitly film stock. Primary teaching examples distinguishing that sense are available in [TUFS film vocabulary](https://www.coelang.tufs.ac.jp/mt/my/vmod/v_search_detail.php?id=1792&ls=%E1%80%96&rf=3). Sources listed for spelling are not claimed to independently certify every English/French gloss.

## Prerequisite and builder checks

The current authoring order contains 216 items. Running the actual `ordered()` function confirmed that all declared prerequisites exist and precede use. All hiragana basics/reverses precede the hiragana rules, followed by katakana basics/reverses and katakana rules. Word examples use known base forms plus the rule being introduced; additional marked forms in おばあさん and ベッド have earlier mark-family instruction. Long-bar instruction precedes フェリー, フォーク and ティー. ディスク follows d-row instruction. References to earlier rule explanations are safe in the current stage/priority order, even when not redundantly listed as individual prerequisite tokens. Conservative extra requirements on some extension items do not introduce unknown forms.

Actual `inputs()` expansion was checked for all 34 items in both languages (68 notes). Front is exactly the Japanese display string, with no sound tag or romaji. Back is the correct romanized reading plus its recording. The bilingual explanation and meaning are answer-side fields. These checks establish authored fields, not installed rendering or playback.

## Audio provenance

All 34 request entries have unique corresponding item purposes and correct input/display, reading and output filename mappings. Every new provenance record declares `ja-JP-NanamiNeural` at `-20%`; every copied file matches its recorded SHA-256. The provenance file now contains 79 recordings in total, including the earlier 45 basic sounds. Every new record explicitly retains `listeningReview: pending`.

No recording was listened to or cleared by this reviewer. Hash equality, intended input, duration and activity metadata do not prove spoken realization, vowel length, gemination, lexical pronunciation or native-speaker approval. In particular, とけい and the long-vowel/geminate examples still need listening review against their notes.

## Supplied Anki verification evidence

Both language logs report 34 cards, 34 audio files, zero images, and passing import, front/back, media, real-study and progress-preserving reimport checks. This reviewer cross-checked all 68 logged item fronts, answers, instructions and notes against the current source, including the revised long-o prose, and all logged media hashes against provenance. The logs are supplied test evidence; their execution was not independently replayed by this reviewer. They do not constitute native iPhone or human listening approval.

## Remaining limitations

- No simulator or physical-device control was performed. Native Type 3 validation remains pending; no native screenshot, import/reimport, truncation, text contrast, reveal behavior or playback signoff is given.
- This is a selected rule/application set. It does not certify complete later coverage or whether the final teaching/reference materials provide every broader marked/contracted form promised by the brief.
- The order result concerns the current source and algorithm, not launch-ready app introduction settings, actual study pacing or mastery. Standalone component previews omit prerequisite lessons and are review artifacts.
- Package hashes, if listed below, identify artifacts present at review time; no independent package import or full archive-content certification is claimed. Publication rights remain outside scope.

## Reviewed snapshot and SHA-256

| Artifact (relative to course workspace) | SHA-256 |
| --- | --- |
| `source-repo/source/questions/03-rules.json` | `3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc` |
| `source-repo/source/audio/requests-type-03.json` | `da3a21a1b56e36bfe0a4bbe4ff0370ba0f36850662c0aa826b04a1a6305a15bc` |
| `source-repo/source/audio/provenance.json` | `91cf7bae5d5c39d54d405f4face552bbd4852d0742936332ff70d1258335e833` |
| `source-repo/source/references.json` | `9f142ffe402f3950fefc35bbf474200849c658dc4ab7995611f1a1873aec8f1b` |
| `source-repo/scripts/source_data.py` | `93824b10fa775aa287ca1899f93d6b50dce4eb468fa160fe4b2eab83a1c05a10` |
| `source-repo/source/questions/01-reading.json` | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| `source-repo/source/questions/02-listening.json` | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| `builds/type-03-rules/packages/Japanese-Kana-en-rule.apkg` | `061aa3ffbcfd8fb25bcfa69e3299a9713de243f5206e7d70522daba8307938ab` |
| `builds/type-03-rules/packages/Japanese-Kana-fr-rule.apkg` | `4d2e143d2208440e9ee7961aa26ffcebcd44015dea229912dd350f3dd341ab5f` |
| `builds/type-03-rules/evidence/en/anki-verification.json` | `7c2a51b24ea481da9e335afe0dc61c02a3fbc0170ce68a6b1cc7bd9c6e716431` |
| `builds/type-03-rules/evidence/fr/anki-verification.json` | `d59e16831cc11f8583f2002edb4a3a8075d0b0f94a92be02ee0b9ff6760dae00` |

## Complete reviewed inventory

| Item ID | Display | Reading | English context | French context |
| --- | --- | --- | --- | --- |
| `rule-hira-marks-g` | が | ga | — | — |
| `rule-hira-marks-z` | ざ | za | — | — |
| `rule-hira-marks-d` | だ | da | — | — |
| `rule-hira-marks-b` | ば | ba | — | — |
| `rule-hira-marks-p` | ぱ | pa | — | — |
| `rule-hira-kya` | きゃ | kya | — | — |
| `rule-hira-shu` | しゅ | shu | — | — |
| `rule-hira-cho` | ちょ | cho | — | — |
| `rule-hira-small-tsu` | きって | kitte | postage stamp | timbre-poste |
| `rule-hira-long-aa` | おばあさん | obaasan | grandmother | grand-mère |
| `rule-hira-long-ii` | おにいさん | oniisan | older brother | grand frère |
| `rule-hira-long-uu` | くうき | kuuki | air | air |
| `rule-hira-long-ee` | おねえさん | oneesan | older sister | grande sœur |
| `rule-hira-long-ou` | とうふ | tōfu | tofu | tofu |
| `rule-hira-long-oo` | こおり | kōri | ice | glace |
| `rule-hira-long-ei` | とけい | tokei | clock; watch | horloge ; montre |
| `rule-kata-marks-g` | ガ | ga | — | — |
| `rule-kata-marks-z` | ザ | za | — | — |
| `rule-kata-marks-d` | ダ | da | — | — |
| `rule-kata-marks-b` | バ | ba | — | — |
| `rule-kata-marks-p` | パ | pa | — | — |
| `rule-kata-kya` | キャ | kya | — | — |
| `rule-kata-shu` | シュ | shu | — | — |
| `rule-kata-cho` | チョ | cho | — | — |
| `rule-kata-long-bar` | コーヒー | kōhī | coffee | café |
| `rule-kata-small-tsu` | ベッド | beddo | bed | lit |
| `rule-kata-extension-fa` | ファン | fan | fan | fan |
| `rule-kata-extension-fi` | フィルム | firumu | photographic film | pellicule photographique |
| `rule-kata-extension-fe` | フェリー | ferī | ferry | ferry |
| `rule-kata-extension-fo` | フォーク | fōku | fork | fourchette |
| `rule-kata-extension-ti` | ティー | tī | tea | thé |
| `rule-kata-extension-che` | チェス | chesu | chess | échecs |
| `rule-kata-extension-she` | シェフ | shefu | chef | chef cuisinier |
| `rule-kata-extension-di` | ディスク | disuku | disc | disque |
