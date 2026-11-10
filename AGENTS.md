# Japanese kana source

Read README.md, rectoverso.json, docs/course-brief.md and docs/review.md before authoring. This is an unpublished multilingual gallery-source candidate. The owner authorized sequential construction of question types with two Astra reviewers at high effort: factual accuracy and pedagogy. The app repository is read-only.

## Authoring and review

Build one question type, validate its packages and rendered behavior, and address both reviewers before starting the next type. Record each review against item IDs and file hashes in docs/review.md and external evidence. Primary Japanese teaching sources substantiate facts. A content or signal check is not native-speaker listening approval.

The confirmed course brief owns pedagogy and scope. The owner decides final names, copy, sample, categories, coverage changes, covers and releases. Working metadata remains unapproved until reviewed. Add dated owner decisions to docs/decisions.md, preserving earlier entries.

Each language is complete. English is American English. French is France’s French: « guillemets », narrow no-break spaces before ; : ! ? and %, typographic apostrophes and …; a deck is « un deck ». Shared Japanese content and media have one source. Original prose/compositions are © Simon Pinkas, CC BY 4.0; font and audio terms retain their own provenance. The owner deferred publication-rights discussion for the Microsoft audition audio; do not represent it as cleared for unrestricted redistribution.

## Source and contract

Source records live in source/, font masters in artwork/fonts/, tooling in scripts/, checks in scripts/checks/, and guides in docs/. Use the existing shared interface scripts/source_data.py::inputs(language), returning metadata, notes, models and deck. Build with scripts/build.py --language <code> --out <new external package>, optionally --type for separate review components and --artwork for retained external renders.

All generated packages, pictures, caches and evidence stay outside this source checkout on the SSD, with paths passed as arguments. The tracked artwork record contains filenames, geometry and hashes, not rendered PNGs. Rebuilds use pinned fonts and dependencies. Every image and sound has provenance, credits and hashes.

Keep GUIDs, model/field/template/deck IDs and package identities stable once studied. GUIDs follow <guidPrefix>-<language>-<item>. Isolated component packages have distinct preview identities; they do not replace the earlier 15-card prototype or the final course. Stages affect introduction order only; reviews remain with FSRS. Custom metadata does not create app behavior; initial presets require app issue #805.

Prerequisites are part of the contract (app #876, the Library page’s “Prerequisites”): each note’s “RectoVerso” payload says what its card requires and what it introduces, as lists of this course’s own tokens (lowercase words and digits with hyphens: hira-3042, hira-marks-g). Only a card that teaches introduces: a reading introduces its kana, a rule its rule. A card requires everything it shows or asks that another card teaches: a listening, word, comparison, variant or checkpoint question its kana and rules, and a reading the other kana its figure shows (visibleKana). The app’s Lesson mode holds a card back until the cards that introduce what it requires have been answered. scripts/source_data.py writes both keys from the source’s requires/introduces and the artwork record; the complete course and the beginner trial carry them, a type preview declares nothing (it could not teach what it requires). The gallery’s check refuses a token no card of the package introduces, a card that could never come, and a deck’s order that asks before it teaches; tests/test_prerequisite_payload.py holds the packages to the same rules.

The authoritative app contract is agents/decks.md, docs/app/library.md and docs/app/languages.md in RectoVerso. Changes to shared schema require coordinated app/pipeline work. This source’s publication.approved remains false; contract preflight cannot be reported as release approval.

## Validation and Git

Before presenting each type, check inventory, prerequisites, bilingual copy, sound/reveal placement, mask preservation and media integrity, then import/render/study/reimport with Anki. Inspect native iPhone/Duo light/dark behavior when the simulator is available and say exactly which checks remain unverified. The owner released the iPhone to Claude, then explicitly reauthorized simulator use on 2026-11-08. Respect current simulator locks. Pending native checks do not prevent sequential source/build work and dual content review. Keep failed evidence. Final combined sequencing is checked after every type exists.

Work on a codex/ branch in this source repository. Commit only owned files explicitly by name. App and other deck sources remain untouched. Source changes ultimately reach the owner by pull request; creating a remote repository, pushing, merging, tagging, publishing, changing gallery pins or editing the owner’s phone requires the applicable user instruction. Local review packages authorize none of those actions.
