# Larger romaji in occlusion

2026-11-08. The owner reported that romanized reading labels inside the occlusion lens were too small. They increase from 30 to 72 source pixels (2.4×). The same pinned Noto Sans JP font at weight400 is used for the romaji and kana; this does not change the romaji to SF Pro. Kana size remains91. Font, color, centers, grid, 130×70 masks, source dimensions and reading labels are otherwise unchanged.

| Severity | Location | Before | After | Why |
| --- | --- | --- | --- | --- |
| Medium | scripts/render_artwork.py reading-label draw | 30px romaji versus91px kana | 72px romaji | Makes the reading answer legible at a more comparable visual scale. |

All labels fit the current rectangles: maximum text bounds are110px wide (mu) and60px high (fu), leaving at least10px horizontal and5px vertical padding. A separate actual-ink test passes even against a conservative130×70 rounded capsule. Old-to-new comparisons for every source image place all changed pixels within the original pronunciation masks. Exactly184 light/dark source images changed; all484 other artwork assets remain byte-identical, including clean backgrounds, standalone kana and alternate forms. Occlusion and preparation geometry is unchanged.

Separate Astra fact and pedagogy reviewers at high effort qualifiedly approved the larger type. The factual reviewer independently verified every label in both palettes and confirmed mask fit; the pedagogy reviewer found the labels substantially easier to read, with no learning-objective change. The rounded-capsule test addresses the conservative source geometry concern, but actual native lens scaling, concealment and border clearance have not been rechecked while both allowed simulator locks are held by others. In particular, inspect mu, shi, tsu, fu and yo when a device is available.

Complete offline CI passed both languages and all fourteen components, with two independent identical artwork renders, matching independent package semantics and preserved actual study progress. The prompt-clarity-to-larger-romaji upgrade also preserves card identities and actual study progress; prompts, answers, notes, audio, order and all geometry remain unchanged. The packages also include the preceding concise-prompt update. No phone import was performed by this artwork follow-up.

Evidence: external builds/romaji-size-20261108/artwork-verification.json, upgrade-verification.json, romaji-before-after.png, and builds/romaji-size-ci-20261108/result.json. Approve the source typography and offline package checks; native fit remains not verified.

```json
{
  "scripts/render_artwork.py": "1f16b561e26a766c11aa2b4c8ea9f06e1286c4e30aa2bb07ec5a812e24a6dcb8",
  "artwork/artwork.json": "7598b306ad0313e5a20315cdf9ab0b59c73ff51e9a99296a1908b9cec5c31284"
}
```
