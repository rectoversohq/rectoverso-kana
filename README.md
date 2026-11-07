# Japanese Kana

An unpublished English/French beginner course candidate following the owner-confirmed [course brief](docs/course-brief.md). Its 290 questions were authored one type at a time, with separate Astra reviewers at high effort for facts and pedagogy.

| Type | Questions |
| --- | ---: |
| Kana → sound | 92 |
| Sound → kana | 94: 90 basic + 4 selected marked-form applications |
| Reading-rule applications | 34 |
| Short-word reading | 36 |
| Targeted comparisons | 12 |
| Alternate written forms | 8 |
| Cumulative new-word checks | 14 |

The [review record](docs/review.md) states exactly what passed and what remains unverified. The [English learner guide](docs/learner-guide-en.md) and [French learner guide](docs/learner-guide-fr.md) are also included in the package's learner-facing content: pacing on the first answer, and searchable reference tables after relevant rule answers. References add no scheduled questions.

Use Python 3.12 and the pinned requirements. All generated assets and evidence go to a new folder outside this source repository:

```sh
python -m pip install -r requirements.txt
python scripts/ci.py --output /external/kana-ci
```

The CI command validates all seven bilingual components, both combined packages, independent rendering and package rebuilds, and preservation of a genuinely studied card. [Build instructions](docs/build.md) also cover individual components and audio authoring. Builds are offline; they use frozen recordings and pinned Noto Sans JP, Noto Serif JP and Yomogi font masters.

The title, gallery copy and sample remain working candidates for owner review. Automatic initial course settings require [app issue #805](https://github.com/simonpinkas/RectoVerso/issues/805). No release, gallery pin or phone installation is authorized by these local review packages.

© Simon Pinkas. Original authored material: CC BY 4.0. Fonts: OFL-1.1, with complete notices in artwork/fonts/. The owner selected Nanami at −20% and deferred publication-rights discussion; source/audio/provenance.json retains that status. New recordings still need listening review.
