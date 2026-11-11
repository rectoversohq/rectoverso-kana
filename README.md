# Kana

An English/French beginner course, at its release candidate 1.0.0-rc.4, which the owner approved for RectoVerso’s gallery in TestFlight (1.0.0 follows the listening review), following the owner-confirmed [course brief](docs/course-brief.md). Its 292 questions were authored one type at a time, with separate Astra reviewers at high effort for facts and pedagogy.

| Type | Questions |
| --- | ---: |
| Kana → sound | 92 |
| Sound → kana | 94: 90 basic + 4 selected marked-form applications |
| Reading-rule applications | 34 |
| Short-word reading | 38 |
| Targeted comparisons | 12 |
| Alternate written forms | 8 |
| Cumulative new-word checks | 14 |

The [review record](docs/review.md) states exactly what passed and what remains unverified. The [English learner guide](docs/learner-guide-en.md) and [French learner guide](docs/learner-guide-fr.md) are also included in the package's learner-facing content: pacing on the first answer, and searchable reference tables after relevant rule answers. References add no scheduled questions.

Use Python 3.12 and the pinned requirements. All generated assets and evidence go to a new folder outside this source repository:

```sh
python -m pip install -r requirements.txt
python scripts/ci.py --output /external/kana-ci
```

The CI command validates all seven bilingual components, both combined packages, independent rendering and package rebuilds, and preservation of a genuinely studied card. [Build instructions](docs/build.md) also cover individual components and audio authoring. Builds are offline; they use frozen recordings, pinned Noto Sans JP, Noto Serif JP and Yomogi font masters, and a separately installed, checksum-pinned SF Pro Text Regular. Kana stays in Noto Sans JP; SF Pro is used only for the lettering of covers 2 and 3. See the font setup in the build instructions.

A reading card asks with the big kana alone. Its answer is the reading, then its script’s whole chart (eleven columns by five rows, no romaji, no headers), the kana taught so far in ink, the others faint, the card’s kana in gold: over the course the chart fills in, and it shows only once the learner has answered. Each reading stays a separate note/card. The [progressive-figure review](docs/reviews/gentler-opening.md) records current validation and limits.

Listening and comparison answers now reveal kana alone, with **Romaji** as a labelled answer detail. This prepares single-character answers for the app’s Debug brush prototype without adding writing questions or changing the existing audio and history. [Brush review](docs/reviews/brush-ready.md) states the tested scope.

The 0.2.0 candidate adds specific shape/sound feedback to reading and listening answers, concise timing cues to word answers, and earlier, separated lookalike comparisons. あい is the ninth question; かぐ applies the voicing rule to a different member of the row. All existing question identities and recordings are retained. [Review and limits](docs/reviews/teaching-feedback.md).

The first eight questions introduce あ・い and then う・え through reading followed by listening recall. Every rolling four-question window contains at most two new basic kana, with eligible word practice in between. Early figures grow with the authored introduction sequence; an older card retains its original snapshot when reviewed.

An isolated [20-question beginner trial](docs/beginner-trial.md) is available with `--beginner-trial`. It has its own study identities and reuses the reviewed opening. Use scheduled Review with four new questions, In deck order and After reviews; the authored source checks do not implement app-side exposure gating. [App prerequisite handoff](docs/app-prerequisite-handoff.md). [Gallery cover build and remaining integration](docs/gallery-todo.md).

The owner-approved title is **Kana** in both languages. This single repository shares Japanese content and media between the English and French packages. Gallery copy and sample remain working candidates for owner review. The shared `study` preset declares deck order, four new questions per day and placement after reviews, using [app #823 / #805](https://github.com/simonpinkas/RectoVerso/pull/823). A supporting app applies it only when first adding the deck from the gallery; direct APKG imports keep their existing options. No release, gallery pin or phone installation is authorized by these local review packages.

© Simon Pinkas. Original authored material: CC BY 4.0. The bundled Japanese fonts use OFL-1.1, with complete notices in artwork/fonts/. SF Pro (Apple), for the Latin lettering of covers 2 and 3 only, outlined in their artwork; the font file isn’t included. The owner cleared it for publication under Apple’s terms (2026-11-10). The Japanese recordings (`LicenseRef-Microsoft-Azure-AI-Speech`) are Microsoft’s Nanami voice through Azure AI Speech, at −20%, under Microsoft’s Product Terms for Azure; not CC BY 4.0 and not relicensed here. The owner approved all 133 by ear (2026-11-11), not a native-speaker review; three are spoken from other text than their card shows, and provenance.json’s inputNote says why.

Gallery covers use six outlined SVG masters in the owner-selected order: brush, stroke order and reading reveal, each in light and dark. Complete builds render deterministic 2,010 × 1,340 PNGs beside the package; see [cover commands and provenance](docs/build.md#gallery-covers). The independent cover workflow attaches the six PNGs for review.

The gallery category is **Languages**. [Credits / Crédits](docs/credits.md) identifies the original course, stroke artwork, fonts, Japanese voice, authoring tool and teaching references. Both language descriptions are kept aligned with the gallery metadata.
