# SF Pro romaji, retained Noto kana

2026-11-08. Owner instruction: “keep noto sans for the kana. Use sf pro for the roman”. Only the reading-image romaji face changes, from Noto Sans JP to SF Pro Text Regular. Its previously enlarged size remains 72 source pixels; kana stays Noto Sans JP weight 400 at 91px. Color, visual centers, reading mappings, dimensions, grids and 130×70px masks remain unchanged.

SF Pro is resolved from a separately installed, SHA-256-pinned file, with RECTOVERSO_SF_PRO_FONT as the optional path override. The binary is not copied to source or APKG media. Missing files and digest mismatches fail explicitly. Mixed-font image credits identify the external Apple font and local prototype scope.

The Astra factual reviewer independently verified the SF identity/hash, glyph coverage for all 92 readings, maximum 106×55px font bounding boxes, mask clearance and unchanged Japanese content. The Astra pedagogy reviewer approved the source change and inspected native light a/tsu/mu plus dark mu revealed/concealed, with readable labels, no clipping and no front-side answer leak. The factual reviewer closed the local-font dependency documentation follow-up as PASS. Both verdicts are scoped passes, not native-speaker listening approval or publication clearance.

Complete offline CI passes: 11 source/unit cases, fourteen bilingual components, both 290-question packages, Anki import/render/study/reimport, independent byte-identical artwork and equal package semantics. Precisely 184 reading-source PNGs change; 484 other artwork assets remain byte-identical. Changed pixels stay inside pronunciation masks. Old-to-new upgrade verification compares all non-image content and geometry, permits only the intended image hashes/font metadata and newer modification timestamp, and preserves actual studied-card state and identities in both languages.

Native iPhone 17 at normal large text size: a, shi, tsu, fu, mu and yo were checked hidden and revealed in light/dark; French listening and tamago reading prompts, and the English grouped-ji prompt were also inspected. The recorded light, dark and English paths replay with 59, 42 and 6 successful steps respectively. Raw paths are retained. Polished paths use semantic identity checks and idle readiness; normalized swipes test the reveal gesture itself. Dark idle checks warn about a small changing area, while semantic checks pass and inspected content is stable. Run the French light import path before its dark path; use the appearance named by each path and restage each imported APKG in /tmp. No grades were pressed in native validation.

Evidence is external beside this checkout:
- builds/sf-pro-romaji-20261108: comparison proof, artwork-verification.json and upgrade-verification.json.
- builds/sf-pro-romaji-ci-20261108: complete offline result and both packages.
- builds/sf-pro-romaji-native-20261108: screenshots, accessibility trees, original/polished recorded paths and replay logs.

The app source was not changed. This typography update was not imported onto the physical phone. Audio remains Microsoft Nanami Neural at −20%, unchanged; new-recording listening review remains pending.

| Reviewed input | SHA-256 |
| --- | --- |
| scripts/render_artwork.py | 70b68075da964dfe650b0b8a30ffb629636ccf5850e1f00f659c6e9cfe522f93 |
| scripts/font_sources.py | 3c8ebaacd6df09ba2aff34a92bb76db9863b15296078373b468aaa09f28245b8 |
| scripts/source_data.py | d63c18906b8fcb5049904acc3ad7ed10dfc274df685b3be3b12e3463ed7bf04e |
| scripts/course_contract.py | 336eb6b3ee6e4792e61a3e68a363e6310fa18548de8bedec9af3d6c68e95c0c7 |
| artwork/fonts/provenance.json | 20a697e72d7eb10794d008615adaf318dffa9ebc3e2f5c59f147e2eb8d772c63 |
| artwork/artwork.json | ddb1cfce242678b1e06850f2bc798ce46c27e5d284f94e35b24fafaeb402c96a |
