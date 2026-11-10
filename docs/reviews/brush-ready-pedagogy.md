# Brush-ready Kana: pedagogy source/build review

Verdict: qualified PASS; no source-level pedagogy blocker. Native interaction/rendering approval is pending the supplied supported, unsupported and grouped-case evidence. This review makes no human-listening or stroke-data accuracy claim.

The 94 listening and 12 comparison questions now reveal kana as their main answer, retaining answer audio. Romaji remains available as labelled feedback, with the owner-approved label “Romaji” in both languages. This supports the existing sound-to-form and visual-recognition objectives; it adds no writing task or handwriting assessment.

Direct comparison of all 290 expanded records in each language against the prior generator found no change to Front, Kicker, Meta, Example, Note, search fields, GUIDs, authored due positions or tags. All 106 affected answers exactly match their accepted kana plus original sound token and their original reading in the new Romaji field/resource. Other answer fields remain unchanged. The eight existing field IDs are preserved; Romaji is appended ninth.

All six grouped listening questions retain both alternatives: listen-hira-o, listen-hira-ji, listen-hira-zu, listen-kata-o, listen-kata-ji and listen-kata-zu. Their one-valid-form hints and spelling-ambiguity explanations remain intact. Comparison answers and shape feedback remain intact, including contrast-nu-me-nu. There is no new prompt-side romaji cue.

The Anki answer template contains a real Explore/Explorer button with aria-expanded/aria-controls and a hidden Romaji container; its question template does not include the field. Native payloads expose the same reading as an answer resource. The existing native convention displays resources inline after the last brush stroke: this is acceptable answer-side feedback and is not represented as an explicitly opened disclosure. Native final-glyph legibility, resource timing and unsupported/grouped fallback remain to be inspected. The Anki verification establishes emitted markup and AV tags; it does not by itself prove GUI button interaction or accessibility behavior.

Reviewed evidence: ci/result.json passes both languages and all components; combined EN/FR Anki reports pass import/frontBack/media/realStudy/reimport. EN/FR edition-update reports preserve card/note/model/template IDs, all studied states and review logs, with appended fields and updated templates validated. core-import.json records supported and unsupported imported answers, resources and audio. Existing history is not reset to demonstrate the prototype.

Limits: no simulator actions or repository edits; no approval of all 290 native screens, VoiceOver, provider pronunciation, handwriting grading or publication. The app prototype's limited character support must not be described as a complete stroke-order curriculum.

## SHA-256 snapshot

- `scripts/source_data.py`: `b9206a67a60552d4d06bed50f6f6b9f9e77295b490a49d116709c63740642ff1`
- `source/languages/en.json`: `6a50410c9802bed19bf8b64ce00946e9e1df0f03ae8c29f5c6d856d8ef313447`
- `source/languages/fr.json`: `ff69dc199aaa0c668c7790d0bd74772843c7e9cd3da9302da3b4a59985a483ee`
- `source/questions/02-listening.json`: `9cd50a0193d4ce0461da4bd7cbfcea9fda3ad1598889bb067924ccdda76d3fca`
- `source/questions/05-contrasts.json`: `158957b09d826c97e3303c30cf39833e20ba4d1536b8a2ef35fccaa8e89cae16`
- `rectoverso.json`: `f89e38f0eef40020a55a6297caa4513d444c061cfdc05db84a7908d7435002c8`
