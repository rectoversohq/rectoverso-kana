# Question type reviews

All seven types received qualified source/build passes from separate Astra reviewers at high effort. Reports bind their findings to item IDs, source hashes and the supplied evidence; later integration reports cover the final snapshot and the four additional shared-sound applications.

| Type | Count | Fact review | Pedagogy review |
| --- | ---: | --- | --- |
| Reading | 92 | [Report](reviews/type-01-facts.md) | [Report](reviews/type-01-pedagogy.md) |
| Listening | 94 | [Basic 90](reviews/type-02-facts.md); supplement in integration | [Basic 90](reviews/type-02-pedagogy.md); supplement in integration |
| Rules | 34 | [Report](reviews/type-03-facts.md) | [Report](reviews/type-03-pedagogy.md) |
| Words | 36 | [Report](reviews/type-04-facts.md) | [Report](reviews/type-04-pedagogy.md) |
| Comparisons | 12 | [Report](reviews/type-05-facts.md) | [Report](reviews/type-05-pedagogy.md) |
| Alternate forms | 8 | [Report](reviews/type-06-facts.md) | [Report](reviews/type-06-pedagogy.md) |
| Final checks | 14 | [Report](reviews/type-07-facts.md) | [Report](reviews/type-07-pedagogy.md) |

The final inventory is 290 questions: 182 basic core directions, four selected derived listening applications and 104 other targeted applications. Comparisons are supplementary recognition tasks, not evidence of unaided recall. The fourteen final words were not previously taught as complete words; a substring inside another word does not count as prior word teaching.

Learner pacing and reference material is shared in source/learner-guide.json. The first reading answer includes the course guide; relevant rule answers include compact contracted-form and katakana-extension references; full basic/marked inventories remain in the full guide and teaching notes. Searchable Reference/Référence fields expose these answers. They add no scheduled questions. Ten minutes and six new questions are recommendations; app issue #805 remains a gallery-launch requirement for automatic settings. The local prototype gives explicit manual settings and a reduce/0 pause procedure.

The owner reauthorized simulator use on 2026-11-08. Representative fronts and reveals for all seven types, plus grouped ji listening, were checked in English/light and French/dark on RV55 iPhone 17. Answers stayed concealed before reveal. The first course guide and the two long rule references were shortened after native testing showed that the replay control was buried; their full bodies remain in the guides and deck descriptions. On the tested normal-size iPhone layouts, replay is reachable with one ordinary answer scroll after the reveal animation finishes. Both compact-note recorded paths replayed end to end; recorded AX waits remain raw because the runner's UIView projection differs. A failed early replay lacked animation readiness between reveal and scrolling; it passed after readiness gates were added, without weakening the replay-access check.

RV55 Duo B's first reading front was inspected in book pose and its answer was revealed by opening to 180°. Its picture answer also repeats the revealed plate inside the answer sheet, so reaching replay needs additional scrolling. This is a limited Duo check, not approval of every type or pose. A French word answer was inspected at the largest accessibility text size: the kana and answer remained legible, the explanation scrolls, and grading buttons remain reachable. Full VoiceOver, all text sizes, all 290 native presentations and actual device pronunciation/listening remain unverified. Native evidence and recorded paths are external in builds/native-final-20261108 beside this checkout.

All recordings use Nanami at −20%. Fifty source files reuse the approved audition; eighty-one newly authored files retain listeningReview=pending. Signal checks, correct input mappings and reviewer approval of written facts do not constitute human listening or native-speaker clearance. The owner deferred publication-rights discussion; that decision remains recorded without a claim of unrestricted redistribution.

No remote repository, pull request, release, gallery pin or phone import has been created for this candidate. Copy, names and sample remain unapproved. Generated packages/evidence are external on the SSD. The app and existing deck sources were not edited by this work.

Offline validation passed in both the working checkout and a fresh clone of commit 6ae5e9acfe33c81fad59c2810392218d1c301bc3. Both languages and all fourteen components passed Anki import/render/study/reimport checks; two independent renders were byte-identical, independent package semantics and authored order matched, and actual study progress survived reimport. Cross-checkout semantic digests also matched. The external evidence index is builds/validation-summary.json beside this source checkout.


After these content refinements, the complete offline CI passed again into builds/native-final-ci: both languages, all fourteen components, two independent artwork renders, package semantic equality and preserved study progress. The refined source at d1e3e40 also passed complete CI from a fresh clone into builds/native-final-fresh-ci; cross-checkout semantic digests match for both languages. Six polished iPhone paths passed end to end. The refined evidence index is builds/native-validation-summary.json beside this source checkout. Separate Astra factual and pedagogy follow-ups qualifiedly passed the compact notes and inspected native samples; see reviews/native-facts.md and reviews/native-pedagogy.md.


2026-11-08 prompt-clarity follow-up: the owner’s screenshots prompted a concise task-caption system in EN/FR. Both Astra reviewers approved it; both rebuilt packages and delivered-to-revised progress preservation pass. The earlier native screenshots concern the prior wording; current prompt fit remains unverified while the simulators are held by other work. See reviews/prompt-clarity.md and external builds/prompt-clarity-20261108.


2026-11-08 romaji-size follow-up: reading labels grow30→72px in the existing Noto Sans JP font. All mask/capsule source-fit checks and complete offline CI pass; actual native scaling remains unverified while simulators are held by others. See reviews/romaji-size.md and external builds/romaji-size-ci-20261108.
