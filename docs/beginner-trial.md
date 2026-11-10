# Beginner trial

The English and French trial packages contain the exact first 20 questions of the 0.2.0 course: eight hiragana readings, seven listening questions and five word-reading questions. Their GUIDs, book/card/deck/model/field/template identities are separate from the complete course and earlier previews. Existing media and question content are reused; the first-answer appendix and deck description describe this trial rather than promising the full course.

Build outside the checkout:

```sh
python scripts/build.py --language en --beginner-trial --out /external/Japanese-Kana-en-beginner-trial.apkg
python scripts/build.py --language fr --beginner-trial --out /external/Japanese-Kana-fr-beginner-trial.apkg
```

The normal CI checks both trial packages as well as the full course and type previews. The two selectors --type and --beginner-trial cannot be used together. No new pictures or recordings are authored for the trial.

## How to run it

Use **Review** on this trial’s deck page. In Deck options, select four new cards a day, In deck order, After reviews. Direct file imports do not receive the gallery’s study preset. Random Practice shuffles; ordered Practice follows the page’s current sort and filter, which need not be curriculum order. Neither is a dependable first-course entry point.

Aim for about ten minutes including due reviews; pause new introductions if reviews fill that time. Four-question groups are not guaranteed calendar days. New kana may be learned by revealing and listening; later questions retrieve the connection. Accurate decoding counts even when slow. Continue spaced reviews after all 20 have been introduced.

| Introduction group | Questions | New kana |
| --- | --- | --- |
| 1 | Read あ/い, then listen あ/い | あい |
| 2 | Read う/え, then listen う/え | うえ |
| 3 | Read あい, いえ, うえ; introduce お | お |
| 4 | Introduce か; read あお, listen か, read かお | か |
| 5 | Introduce き/く; listen き/く | きく |

Word transfer in this opening covers あいうえおか; き/く have individual reading/listening only. Listening お remains deferred because its grouped alternative を has not been introduced.

After each session, record only what is useful: time spent, unclear prompts, sounds that were hard to distinguish, whether a word could be decoded without the table, and any dependent question that appeared before its kana. Someone already familiar with these forms can test usability, but cannot stand in for a genuinely new learner’s learning trial. No automatic study-history export is needed.

## Prerequisites and current app limit

The owner’s rule is strict: a basic kana→sound teaching encounter may introduce its own target. Every other kana required by a listening answer, word, comparison, or reading figure context must already have had its form–sound connection introduced. Introduction is exposure, not mastery; simply occupying an earlier queue position is insufficient when that encounter was skipped.

The trial builder independently checks actual prompt/accepted glyphs and reading-figure visibleKana, rather than trusting declared requires. Regression cases for an undeclared new word kana and a future table neighbor were first observed failing, then passed with the guard. This checks authored order, not runtime eligibility.

The phone initially showed Random and 20 new cards/day. These settings were changed and directly observed as In deck order and 4, with After reviews retained. Automation later overran its accessibility watchdog; the recording retains its failures and is not claimed as a passing end-to-end replay or complete learner-history verification. No question was graded, no history was reset/exported, and the full Kana deck’s settings were not changed by this correction.

Existing history can still put an already-studied dependent card in the due queue. Changing new-card order does not undo that or implement prerequisite checks. This trial is not proof of a fully enforced beginner course; [the app handoff](app-prerequisite-handoff.md) describes the remaining requirement.
