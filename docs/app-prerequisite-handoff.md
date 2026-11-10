# Kana prerequisite enforcement — app handoff

Owner decision, 2026-11-10: only a kana→sound teaching encounter may introduce an unseen target. A listening, word or comparison question must wait for all the kana it requires. A reading figure’s other visible kana must also already be introduced. This is exposure gating, not a mastery lock.

The current deck contract carries authored card order and a starting study preset, not an enforced per-card prerequisite graph. Source requires/introduces tokens are authoring data; the app does not consume them. Do not emit invented native-payload fields and assume they work. A shared contract change must cover the writer, gallery validator/catalog/importer, saved model, documentation and compatibility tests before it ships.

Current app behavior permits the reported failure: direct file imports get default random new-card order; random Practice shuffles; ordered Practice follows the current page sort/filter. Even scheduled deck order filters suspended/buried introductions and prioritizes previously studied dependent cards. It does not check what a learner has actually been taught.

Required behavior:

- Define and record a form–sound teaching event when the introduction is actually revealed/provided. Do not infer it from queuing, starting an unanswered prompt, FSRS success or maturity.
- Check prerequisites immediately before presenting each question, in scheduled study, every Practice variant, filtered selections and resumed sessions.
- If an introduction is missing, defer the dependent question or offer the required teaching encounter. Do not count a listening/word answer as its missing introduction.
- Respect four new scheduled questions/day and reviews-first behavior; do not silently insert uncounted teaching cards. Decide explicitly how skipped/suspended introductions are offered.
- Preserve Practice’s current no-persistent-history contract unless the owner changes it. Track session exposure locally or provide the missing teaching again.
- Keep existing note/card IDs and histories. Do not infer historical exposure without defensible reading-teaching evidence or silently transfer progress between the isolated trial and complete course.

Acceptance examples: no あい before あ and い teaching; no listening か before か teaching; a き table cannot show unseen neighbors; suspending/omitting い must not make あい eligible; reordering, filtering, resuming or switching Practice must not bypass eligibility. A first failed recall must not itself prevent later material once the teaching event occurred.

This handoff authorizes no app-source edit or new contract fields.
