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


## 2026-11-10 — The prompts and the prerequisites, in one edition

The script-specific reading prompts and the prerequisite payload were written on two branches, each advancing contentModifiedAt for its own change. Together they make notes that neither branch's packages hold, so contentModifiedAt advances once more (2026-11-10T18:16:07Z): an update over either earlier build then replaces every note, where the later of the two times alone left Anki keeping the older ones (the update check refused it). No question, identity, answer, order or media changes.


## 2026-11-10 — The first gallery edition: 1.0.0-rc.1, on the deck kit’s contract

The owner decided, for the 1.1 gallery:

- **Version:** a release candidate first, 1.0.0-rc.1, tried in the app; then 1.0.0, approved for publication on the owner’s go for that release. Until then publication.approved stays false: the kit’s check passes, RectoVerso’s gallery (which takes approved editions only) does not yet.
- **Kana joins the 1.1 gallery,** its two languages delivered together in one of the gallery’s asset packs (the gallery’s grouping; the deck still builds and releases one package a language).
- **SF Pro is cleared:** the pictures that draw romaji in SF Pro Text are published with the deck. The font’s binary stays out of the repository and the packages.
- **The recordings ship as they are.** They are Microsoft’s Nanami voice (ja-JP-NanamiNeural, −20%), made through edge-tts, an unofficial client of Edge’s read-aloud service; their publication rights were never established. The owner accepts that risk. The source records them as LicenseRef-Microsoft-Read-Aloud-Not-Relicensed: they are not CC BY 4.0, and nothing here presents them as licensed or cleared.
- **Listening review:** eighty-three recordings have not been listened to by a person. The review happens before 1.0.0, not before the candidate.
- **The sample** is the first reading, あ; **the gallery copy** (headline and description, both languages) is approved as written.
- **The repository is public,** and its metadata now says so.

The deck now follows the deck kit (kit/, pinned at v1.0.1), which replaced the app’s own copy of the contract: rectoverso.json states the count of pictures and a credit for each of the 468 (each an original composition, CC-BY-4.0, its fonts named in its source), lists the six covers, and is held to what the course makes by scripts/metadata.py and the kit’s check; scripts/source_data.py gives the kit its inputs(language) beside the course’s own course(language, …); the complete course’s sidecar is the kit’s. No question, identity, answer, order, picture or sound changes.


## 2026-11-10 — The book is the id RectoVerso gives the package’s Anki deck

RectoVerso’s gallery knows a deck on the shelf by the id it derives from the package’s Anki deck (UUID(stableFrom: "anki/deck/<id>"), two FNV-1a passes). This course’s payload named a book of its own (a UUID from the GUID prefix and the language), so the app filed the deck under that one, and the gallery would have offered **Get** for a deck already there: the app’s gallery round trip refused both packages. The owner chose to fix it here rather than in the app’s catalog. Each package’s book is now that derived id (scripts/source_data.py, library_id), the complete course’s, the trial’s and each component’s alike; a test holds it to literals computed with the app’s own function. Card ids, GUIDs, note types and Anki ids are unchanged. Nothing was published under the earlier book; a build already imported into RectoVerso stays a deck of its own beside the new one. contentModifiedAt advances with the payload.


## 2026-11-10 — 1.0.0-rc.2, approved for the gallery in TestFlight

The owner tests the course through RectoVerso’s gallery in TestFlight, and the gallery pins approved editions only. 1.0.0-rc.2 is 1.0.0-rc.1 with publication.approved true: the same questions, identities, answers, order, pictures and sounds, and the same contentModifiedAt. It is still a candidate by its number: 1.0.0 follows the owner’s test and the listening review of the eighty-three recordings. The workflow now runs the kit’s check as RectoVerso’s gallery takes a deck.


## 2026-11-10 — 1.0.0-rc.3: the Anki check reads RectoVerso’s export

RectoVerso’s gallery checks a deck in Anki twice: its package, then the app’s own export of it. A deck whose notes carry a payload comes out of the app as the app’s notes (its own note type, each note named by its card’s id, no tags, no Romaji field), which scripts/checks/validate-anki.py took for a broken package: the gallery’s check stopped there on 1.0.0-rc.2. The check now recognizes that export and holds it to the source: every note once, by the noteID in its payload; its fields (an occlusion’s front is the app’s own drawing over the same pictures, another front keeps its words and pictures); its kind, what it requires and introduces, its card and book ids; every picture and sound byte for byte; then real study and a reimport that keeps progress. The gallery reads the check from the pinned tag, so this is a new candidate; the packages’ notes, identities, media and contentModifiedAt are those of 1.0.0-rc.2.
