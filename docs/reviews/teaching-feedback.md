# Kana 0.2.0 teaching-feedback review — 2026-11-10

## Scope and sequence

292 questions per language: 92 reading, 94 listening, 34 rule, 38 word, 12 comparison, 8 alternate-form and14 final checks. All 290 existing questions remain; only word-ai and word-kagu are new. All identifiers and all 131 previous recordings/provenance remain unchanged. Reading, listening, word and comparison feedback is shorter and specific. Rules, alternate forms and cumulative-check explanations are unchanged.

The first eight remain あ/い reading then listening, followed by う/え reading then listening. あい is#9. かぐ is#118, after the g-rule and an intervening rule question. Comparisons follow both forms’ first reverse attempts, with reciprocal questions separated. Every rolling four introduces at most two basics; reverse questions have at least one intervening item after reading. The shared study preset remains4 new questions, in deck order, after reviews. Existing settings are not overwritten; the preset applies automatically to a fresh gallery addition, not a direct file import.

## Independent reviews

Separate gpt-6-astra reviewers at high effort inspected each changed type before the next was built: factual accuracy and pedagogy. Both give qualified passes for the final source. The factual review checked the pinned Noto Sans JP glyphs and corrected と/ヒ connectivity plus き/さ wording; listening cues avoid image-specific connectivity claims because those answers are live text. New word meanings have direct primary references. These are model/source reviews, not a Japanese speaker’s listening approval or a beginner trial.

| Reviewed source | SHA-256 |
| --- | --- |
| source/questions/01-reading.json | `a027e47b2fad9c0460d7bae2e00c21850f40cdc2826374c3d18ee719c0ed0766` |
| source/questions/02-listening.json | `e189887271004de47a4774c02ee511be737eece850b2c77916952ee31ebd432a` |
| source/questions/04-words.json | `92199807364266dc2361bd896bda27dbbcebe058118112a30a8f6d44c7feaf92` |
| source/questions/05-contrasts.json | `7b54ce322b737fc8e2e9601fe2c13291a9d2634a5b170ba92f09a7c71b943819` |
| source/learner-guide.json | `060d0394a770c8ff318116f251aa2449ac0ebbc83ef85298c8471ad6d6b40b9a` |

## Build and update evidence

External evidence: builds/teaching-feedback-20261110/ in the shared course workspace. Full CI passes 39 tests, all 14 bilingual component imports and both 292-card combined packages. It checks media, actual Anki study/reimport, byte-identical independent artwork and equivalent independently built package semantics. Previous-edition imports preserve every old note/card ID, model/field/template ID, scheduling state and revlog entry; exactly two GUIDs per language are added, and reimport is idempotent. The check compares every referenced image/audio byte against a fresh import.

All 668 old artwork records and existing figure geometry match exactly. Four isolated review figures for the two new words are added; word prompts remain kana text with no front audio, meaning or romaji. The two new frozen audio files use Nanami at −20%, existing normalization, and retain pending human review.

## Native scope and remaining gates

A preinstalled RectoVerso Debug 1.1 (build 0) on RV55 Duo B imported both 292-card packages. Live observations covered the revised initial reading answer/guide on closed and open Duo, あい, and the French かぐ answer in light and dark at normal Dynamic Type. An initial AccessibilityXXXL observation is retained separately; it is not proof that the whole first guide fits without scrolling. The corrected 15-step recording replays fully: 14 actions pass, zero failed/errored/skipped. Raw AX waits remain raw because recorder and runner projections differ; this is disclosed rather than claimed as a native-hierarchy assertion. The original failed French take used a mistyped book UUID and is retained; the corrected launch and wait were recorded live and replayed. Simulator data/preferences/text size/posture are restored, and scoped Argent services/lock released. No app was rebuilt or installed.

The iPhone 17 simulator was locked by another agent, so a fresh iPhone visual pass remains pending. Full bilingual every-card/every-appearance visual coverage, VoiceOver, human Japanese listening review and a real beginner pilot remain pending. This review does not establish learning efficacy or publication approval. No release, tag, gallery pin or phone install is authorized.

Actual RectoVerso Core import/reimport against app commit `41cb6fef` passes both packages: full authored order, 92 matching occlusion preparations with exact asset hashes, 94 true listening cards, existing native card/book IDs retained and exactly two additions. See external core-import.json.

Complete CI also passes in a fresh clone of code commit `0cff139`. Its two semantic package digests exactly match the reviewed final packages: EN `4c03d1deb3005b25bddde4613ad26b24f4cf6e26209e83add4dbaf0b8ecb4c37`; FR `4d32c2b01abb321e67facecf61a120557d37140bcd7362dd77c4315f5c32afdd`. Final package hashes, sizes and paths are in external result.json.

Current gallery checks were run separately on EN and FR against app `41cb6fef`. Both stop at GalleryDeckTests.swift:63, the existing numeric-Anki-deck-to-library-UUID assumption. Later gallery assertions are therefore unverified. Native book/card IDs are preserved rather than changed to satisfy that assumption. Metadata preflight refuses publication.approved=false as intended; direct gallery study validation passes the four-question preset. These gates are not reported as passed or bypassed.
