# Type 06 — alternate kana forms factual review

Verdict: **QUALIFIED PASS** for all eight alternate-form items, bilingual prose, font attribution/provenance, image and audio mapping, prerequisites and generated/evidenced content. No factual blockers remain in this snapshot. This is not native-app or audio-listening clearance.

Reviewed 2026-11-08 by the delegated Astra factual reviewer. All eight shipped dark glyph plates were visually inspected, not merely checked by filename. All English/French notes and prompts were read. The implementation and main app remained read-only; no simulator or physical device was used. Only this report was written.

## Complete item review

| Item ID | Glyph | Reading | Actual font | Source-order position |
|---|---|---|---|---|
| variant-hira-3055 | さ | sa | Yomogi | 138 |
| variant-hira-304d | き | ki | Yomogi | 139 |
| variant-hira-308a | り | ri | Yomogi | 140 |
| variant-hira-3075 | ふ | fu | Yomogi | 141 |
| variant-hira-305d | そ | so | Noto Serif JP | 142 |
| variant-kata-30b7 | シ | shi | Noto Serif JP | 270 |
| variant-kata-30c4 | ツ | tsu | Noto Serif JP | 271 |
| variant-kata-30f3 | ン | n | Noto Serif JP | 272 |

All eight images show the intended, recognizable character without clipping or another kana replacing it. The separated lower portions of Yomogi さ and き and its two-part り are legitimate shape variation. Its ふ is recognizable despite its distinctive connecting treatment. The serif そ, シ, ツ and ン retain their character identities; the シ/ツ orientation and one-mark ン distinction remain clear.

English and French accurately identify Yomogi as a handwritten-style typeface, not a handwritten sample or stroke-order demonstration. The internal `handwritten` flag is a font-selection switch, not evidence of human pen production. Noto Serif JP is correctly described as a printed serif style whose stroke endings/contrast differ. Neither version requires learners to copy the style or implies a new sound. The French wording is semantically consistent with English. These are recognition/reading examples, not a comprehensive handwriting course or an exhaustive alternate-form inventory.

## Primary references and font provenance

- [MEXT kana chart](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf): kana identities and sound mapping. The course's fu spelling is its established pedagogical romanization for ふ; the chart's hu spelling does not imply a different Japanese kana.
- [Japan Foundation, teaching kana writing, pp. 12–13](https://www.jpf.go.jp/j/project/japanese/teach/tsushin/bn/dw_pdfs/tushin45_p12-13.pdf): directly explains differences between printed and handwritten kana forms, including connected parts and examples such as さ, ふ and り. This supports the general explanatory claim, without claiming that the Foundation endorses either chosen font. All eight source items now cite this direct reference.
- [Pinned Yomogi license](https://raw.githubusercontent.com/google/fonts/008f47aa68a60f07e4f6adc926ab78e19a88d92f/ofl/yomogi/OFL.txt) and [pinned Noto Serif JP license](https://raw.githubusercontent.com/google/fonts/8b0a1d0f5983c89bc2b93f1b5fb55f9e252744b5/ofl/notoserifjp/OFL.txt): the bundled texts identify SIL OFL 1.1, with Yomogi Project Authors and Google copyright notices respectively. This is a provenance/attribution check, not a general legal opinion.

The local Yomogi-Regular.ttf, yomogi-OFL.txt, NotoSerifJP.ttf and notoserifjp-OFL.txt hashes match the font-provenance manifest. The reviewer independently retrieved all four files from their pinned official Google Fonts URLs in memory and verified the same SHA-256 values. Rendering code selects Yomogi for the four `hand` items and Noto Serif JP for the four `serif` items at the selected regular weight. The corrected generated and packaged imageCredits now name those actual font files, replacing the earlier incorrect blanket NotoSansJP attribution.

## Mapping, fields and evidence

All eight readings/audio assignments match the previously reviewed basic kana source; each item's prerequisite is its corresponding already-introduced basic character. The current 272-item source order resolves every prerequisite. All eight reused basic MP3s match provenance hashes. No new synthesis or listening claim is introduced.

The shipped plates are the `*-dark.png` assets: light glyphs on a dark paper-colored rectangle. Their use in both appearances is a build choice, not proof of native appearance behavior. All image bytes match the artwork manifest. The builder places the alternate glyph image on Front, uses a generic localized alt label, and puts romaji plus recording and explanation after reveal. The alt label does not expose the kana or its reading. A generic label is not an equivalent nonvisual reading exercise, so this review does not certify accessibility.

Both r2 Anki evidence logs report eight cards and passing import, front/back, media, real study and progress-preserving reimport. All 16 logged front/answer/instruction/note entries match the current generated fields, and every logged image/audio hash matches the source assets. Actual package metadata was checked for correct per-image font credits. The reviewer inspected supplied logs and metadata; no Anki or native flow was independently replayed.

## Limitations

Native RectoVerso validation remains pending. Source images are not app screenshots, and this report does not certify runtime scaling, presentation, appearance switching, audio controls, or scheduler enforcement. Reused recordings inherit their previous review status; hash matching is not listening/native-speaker approval. Isolated component packages do not demonstrate that learners have actually completed prerequisites.

## Reviewed snapshot (SHA-256)

| File (relative to course root) | SHA-256 |
|---|---|
| source-repo/source/questions/06-variants.json | `a0aeff50ab3157947506f1d98014a7d03d88cefd34dac73ddd3b996fe088426c` |
| source-repo/source/kana.json | `07111a9cc20bf6e00474992ca2a38fbfa2631495002925e0b2b886fd056e98a4` |
| source-repo/source/audio/provenance.json | `16d27fd23a8376f3d12827c03c64b86f361c98de23f7a15c4981eeaebf406127` |
| source-repo/source/references.json | `e0bbd008b47dd9a08c938b2fe8747a1b0547689656c5d192e4ebc5be464d217f` |
| source-repo/scripts/source_data.py | `9c59199cf71c76a55f8889236b64a4b97e5343f7f666deb8192e476c50522134` |
| source-repo/scripts/render_artwork.py | `2a5372133c66f8f8d5ff9c83fcd0d7f171c646945df84dd566c36368cafb970c` |
| source-repo/source/languages/en.json | `e23bec669a3376e9f4d23585f7b1fc99fba59ab5ebe45c79d2da75e60d4ccf5a` |
| source-repo/source/languages/fr.json | `1cf709400fed8087c6c70241c64b6ee921a8d7ae4acf62aff4a512c68a30fb8b` |
| source-repo/artwork/fonts/provenance.json | `72ebcd4e989f48dd3542bee00f044281ccf071999499c1ac82314e7c8c50bbc8` |
| builds/type-06-variants-r2/artwork/artwork.json | `8db80e55b607722cee8e4682c64354fb72bef77103a7ee303a7a4f8ea41afce6` |
| source-repo/artwork/fonts/Yomogi-Regular.ttf | `ec280f473a03187292905618f24fdb08a6dcbf8620b52637e3b589fe745259b9` |
| source-repo/artwork/fonts/yomogi-OFL.txt | `bc0330d5973ab1f200553f51b4cb4ef11b81187fdcd0249f7f83992726c02a48` |
| source-repo/artwork/fonts/NotoSerifJP.ttf | `2fd527ba12b6a44ec30d796d633360da0aeba6c5d4af1304ce12bb4dc15a7dfc` |
| source-repo/artwork/fonts/notoserifjp-OFL.txt | `5e0da210fb04058a8c0087985d2d456b931c2579811a49655721d3cf0c36b6d6` |
| source-repo/source/questions/01-reading.json | `f6363a37b1624e2e0a66f0eac91d589aab5adc3ccb4c92882fee31c3e5103767` |
| source-repo/source/questions/02-listening.json | `1744ab00a6d8a4360d5b6ec2c06711ef3ecfc6dc761c45d5e6cdbe268ff32b51` |
| source-repo/source/questions/03-rules.json | `3bf1c59488ca0c7462d24dd5e7edacf15a2872211cccdda4efe783141350eddc` |
| source-repo/source/questions/04-words.json | `d8e3d4d5e703ab7fcae84d79add7e67be3a19d8308d218e08416cc9405f2bc81` |
| source-repo/source/questions/05-contrasts.json | `efc69f8e0cc51ef40c06f10f3ee28db4d5c7acdc55d9c865fb7b2a827b02d79b` |
| builds/type-06-variants-r2/packages/Japanese-Kana-en-variant.apkg | `2d49f9fa5b6213342cc349808aab4681f8b9b5b3d7b5d2cad5f0dfd59d479c7d` |
| builds/type-06-variants-r2/packages/Japanese-Kana-en-variant.rectoverso.json | `6c1771fcc28b76c37741c564b176ed0a7618f632857385b4ad7edff886a3dc9d` |
| builds/type-06-variants-r2/packages/Japanese-Kana-fr-variant.apkg | `80ba34fdbc0b48e33d1e4815cfb9c702d6e2e89e536cee99ecbfce6939c3aeb6` |
| builds/type-06-variants-r2/packages/Japanese-Kana-fr-variant.rectoverso.json | `dcdd768bf42c50dfa3090dc19a11f08a73eec864a52ea82ba74ae071051180c9` |
| builds/type-06-variants-r2/evidence/en/anki-verification.json | `0bfbbbf85dcaadab70d8a3a48c8631259dfefa0e7140abf536e396370d6a754f` |
| builds/type-06-variants-r2/evidence/fr/anki-verification.json | `fe983ada6f3eeb07899db044607dce4d424958e73c4dab5b4ccdc109a07f80e8` |
