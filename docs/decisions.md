# Decisions

- 2026-11-07 — Simon Pinkas confirmed the complete course brief after the pedagogy interview.
- 2026-11-08 — Simon Pinkas requested sequential construction of each question type, with separate Astra reviewers at high effort for factual accuracy and pedagogy.

- 2026-11-08: The owner requested the iPhone simulator immediately for Claude. Primary released its lock and services; further native checks stay pending while source/build and dual-review work continue.

- 2026-11-08: Sequential authoring completed seven types with separate high-effort Astra fact/pedagogy reviews. Four selected grouped ji/zu listening applications preserve the approved homophone treatment. Guide/reference material is unscheduled and answer-side. The candidate has 290 questions; app #805, final native inspection and new-audio listening remain outstanding before a gallery release.

- 2026-11-08: The owner reauthorized simulator use. Native checking found long answer-side guides pushed replay several screens away; compact answer-side versions retain pacing and broader reference inventories, while the complete guide remains in documentation and the full course description.

2026-11-08 — Native follow-up: shortened emitted guide/reference notes while retaining full bodies and every reference form; clarified French review-first pacing after factual review. No new scheduled questions, identity changes, artwork changes, audio changes or app-source changes. Publication and actual listening remain pending.

2026-11-08 — Owner feedback: reduce verbose listening fronts and replace cryptic exercise labels with explicit tasks. Use one task caption across the course, a short script-specific listening question, and a one-form-is-enough cue only on grouped answers. Voice remains Microsoft Nanami Neural at −20%; no audio is regenerated.

2026-11-08 — Owner reported tiny romanized text in the occlusion. Enlarge labels2.4× within unchanged masks. On the owner’s SF Pro question, clarified that the image’s Latin text currently uses pinned Noto Sans JP; native app text uses Apple’s system fonts. No typeface change was requested or made.

2026-11-08 — Owner confirmed: retain Noto Sans for kana, use SF Pro for romanized text. Reading-source romaji now uses locally installed, pinned SF Pro Text Regular at the previously enlarged 72px size. Japanese glyphs, mask geometry, content and audio are unchanged. SF Pro is external and its binary is not redistributed.

2026-11-08 — Owner named the deck Kana and authorized creating its repository, explicitly confirming that English and French belong in the same repository. Both learner-facing titles are Kana; all GUIDs, book/model/deck identities and existing package filenames stay stable. The repository starts private while this candidate is under review.

2026-11-08 — Owner decision in RectoVerso #824: fix Kana listening in the deck. All 94 listening Front fields hold only their sound; Kicker retains the script-specific question, and Meta holds only the grouped-answer hint (Recall one valid form. / Une forme suffit.). Comparisons remain text plus sound. Answers, notes, search metadata, order and all identities stay unchanged.

2026-11-08 — Owner explicitly left native Anki GUI playback pending after the successful Anki import/render/audio-hook checks and the desktop automation timeout.

2026-11-08 — Owner chose Listen / Écouter for Kana’s question sound buttons (playLabel, app #824 / PR #826). Requested compact silence padding and consistent loudness. Keep Nanami −20%, sound-only listening fronts and text-plus-sound comparisons; no release, gallery pin or phone install authorized.

2026-11-08 — Media update verification found that Anki retained old audio when the content marker had not advanced. Advance contentModifiedAt while keeping all identities. Add an optional previous-edition CI preflight that checks the actual referenced audio bytes after update as well as every studied state; retain the rejected intermediate package externally as negative evidence.

2026-11-08 — Owner requested conformance to the implemented study field. Replace advisory studyRecommendations with the agreed shared study preset: newCards=deckOrder, newPerDay=6, newPosition=afterReviews. This metadata migration changes no question, identity, authored position or media. App #823 applies it only on first gallery addition; do not overwrite existing learner options or treat a direct file import as a gallery add.


## 2026-11-08 — Keep gold; crop the reading figures (#830)

The owner selected « Keep gold; use cropped per-card figures » instead of neutral shared tables. Each reading keeps its gold kana and underline, its separate note/card identities and authored place. Figures retain three complete neighboring rows, at 1,000 × 1,080 pixels, with the original fonts, colors and pixels. Top and bottom crops clamp to occupied rows 0–10, including ん/ン. All visible pronunciation labels remain covered with hideAll; the target retains its global ordinal. The whole-table canvas is intentionally no longer present. There are still 368 per-card table PNGs and 92 preparations, not eight shared PNGs and two preparations. No release, gallery pin or phone install is authorized.


## 2026-11-08 — Gold glyph without an underline

The owner retained the cropped figures and gold kana, and explicitly removed the underline because it looked like part of the symbol. The gold character itself is now the only baked target highlight. Font sizes, glyph shapes, crop geometry, masks, identities and course order remain as above.


## 2026-11-08 — Kana-only answers for the brush prototype (#832)

The owner authorized preparing the existing 94 listening and 12 comparison answers for the app’s Debug stroke-reveal prototype and chose **Romaji** as the labelled detail in both English and French. Their main answers contain kana only, retaining each existing answer recording. All six grouped listening answers keep every accepted spelling as alternatives and ordinary text reveal. Other question types continue to answer with romaji. The new Romaji field is appended after all eight existing fields, preserving existing identities and course order. Genuine Anki button/hidden-field details and the existing native payload’s resources carry the same reading. Stroke storage, new writing questions and multi-character drawing remain undecided; this change adds none of them. No release, gallery pin or phone installation is authorized.


## 2026-11-08 — Gentler Kana introductions

The owner approved the proposed gentler start: up to two new basic kana and four new scheduled questions per day, reading exposure before reverse listening, and early figures showing only already-introduced kana. The supported static starting preset changes from six to four; no automatic ramp or mastery gate is added. All existing learner options, IDs and history remain stable. The first あ figure contains only あ, then the い figure adds い, within the existing gold-preserving frame. Older figures remain introduction-time snapshots. Existing eligible word questions supply consolidation without adding new questions or recordings. No release, gallery pin or phone installation is authorized.


## 2026-11-10 — More useful feedback and earlier application (0.2.0 candidate)

The owner approved creating the proposed next version: concise kana-specific answer feedback, earlier lookalike comparisons, earlier tiny-word practice and a productive voicing application. Keep the first eight questions and the gentle four-new-question starting preset. Add あい as question9 and かぐ after the g-rule with another question intervening; retain all 290 existing questions, identities and recordings. Move existing comparisons nearer their completed reading/listening pair cycles and separate reciprocal questions. Reading, listening, word and comparison feedback is revised; rules, alternate forms and final checks retain their established content. The two new recordings use Nanami at −20% and await human review. The owner’s approval creates a review candidate, not a release, gallery pin or phone install.


## 2026-11-10 — Isolated beginner trial and strict introduction prerequisite

The owner requested a phone trial of the first 20 course questions, and noted that gallery covers remain to be made. The trial is built in both languages; English is installed for testing, under identities separate from the complete course. No original question, artwork or recording changes.

After the owner reported words preceding their kana, the authored sequence was independently audited by actual glyphs and passed; the phone’s trial was observed still configured as Random with 20 new cards/day. It was changed to In deck order and four/day, retaining After reviews. The owner’s rule is that only a kana→sound teaching encounter may introduce a target; all other required kana must already be introduced. Add actual-glyph source regressions and an app handoff. Source order and settings alone do not establish runtime prerequisite enforcement, especially with skipped introductions, Practice or pre-existing dependent-card history. Do not reset learner history to conceal the failure.


## 2026-11-10 — Gallery cover builder

The owner selected workshop order 1–3–2 (brush, stroke order, reading reveal) and requested the same cover build workflow as the other authored decks. Six self-contained outlined SVG masters retain separate light/dark artwork and share teaching symbols across English and French. Complete builds render covers externally; checks enforce dimensions, naming, appearance/language coverage, localization, unambiguous scopes and language-pill clearance, with independent-byte comparison. KanjiVG attribution and share-alike terms accompany the frozen stroke source and its derived covers. No study content or identities, publication status, gallery pin or phone installation changes.


## 2026-11-10 — Gallery description, Languages and credits

The owner requested the gallery description, confirmed the Languages category and asked for credits. The English/French gallery and package descriptions now concisely describe sound ↔ kana recall, stroke-by-stroke answers, reading rules and short-word practice; import-setup details remain in the learner guide. The source list separately credits the original course, KanjiVG, the pinned Japanese/SF fonts, Microsoft Nanami, edge-tts and the teaching reference index. Original-material licensing is normalized to the equivalent CC-BY-4.0 identifier; each third-party contribution keeps its own recorded terms, including deferred audio rights. This is metadata/copy work, with no question/media/identity changes and no publication approval.


## 2026-11-10 — Prerequisites in the package

The owner had the app enforce prerequisites (RectoVerso #876, Lesson mode) and included this source’s writer in that work. Each note’s native payload now carries requires and introduces: the source’s tokens, plus, for a reading, the other kana its figure shows, so a figure never shows an untaught neighbor. The complete course and the beginner trial carry them; a type preview declares nothing, since it cannot teach what it requires. Question identities, artwork, audio and study state are unchanged; only the payload gains keys, which earlier app versions ignore. contentModifiedAt advances with the payload (2026-11-10T15:46:16Z): Anki updates a note only when it is newer, and with the earlier marker an existing learner kept the notes without the keys, which the previous-edition update check caught. With it advanced, the full CI passes against the gallery-metadata edition: content updated, every study state and review preserved, in both languages. Publication and gallery pinning remain separate owner decisions.


## 2026-11-10 — Name the script in reading prompts

The owner approved replacing “Read this kana.” with “Read this hiragana.” or “Read this katakana.” The 92 basic reading questions and eight alternate-form questions name their actual script in English and French. French keeps the existing question wording, using « Comment se lit ce hiragana ? » and « Comment se lit ce katakana ? ». Word, rule, listening, comparison and final-check prompts stay unchanged. Advance contentModifiedAt so existing Anki notes receive the revised instructions; retain all question identities, answers, ordering and media. No release, gallery pin or phone installation is authorized.
