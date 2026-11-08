# Japanese Kana Course Brief

Confirmed by the owner on 7 November 2026. This is the agreed pedagogy, sequencing and scope for the gallery course. It defines the learning design; the complete lesson and card inventory is the next authoring step.

## Learning promise

A complete beginner can use this course without external lessons to learn hiragana and katakana and accurately decode unfamiliar short words built from the characters and rules taught. Success means unaided reading without romaji or hints, respecting vowel length and doubled consonants. There is no speed requirement.

Reading and sound-to-kana recall are the core skills. Mental recall is sufficient; handwriting is encouraged as optional practice. The exercises must test connections between sounds and written forms, rather than memorisation of positions in a kana table. Reading figures show the target and only kana already introduced at that point in the authored sequence, within the retained three-row frame. Every drawn reading is concealed with hideAll. The first figure contains only あ and the second adds い; later cards grow the visible set. These are authored snapshots: an older card retains its earlier view on review, without a claim of measuring mastery.

The shared Japanese curriculum has English and French guidance. Word meanings provide context, rather than a separate vocabulary-recall objective.

## Course sequence

1. **Hiragana basics:** vowels, followed by sound families in small batches.
2. **Hiragana reading rules:** sound marks, contracted sounds, small っ, and long vowels, taught through principles and selected applications.
3. **Katakana:** familiar sounds with new written forms, followed by applicable reading conventions and selected common extensions such as ファ, ティ and チェ.
4. **Cumulative reading:** a final block mixing hiragana and katakana words not previously used as teaching examples, containing only characters and rules already introduced.

Basic characters are introduced in pairs. The first four questions are reading あ, reading い, listening あ, listening い; the next four do the same for う and え. Every rolling window of four authored questions introduces at most two new basic kana. Existing eligible word questions provide consolidation, including an already-readable hiragana word during early katakana while its grouped オ／ヲ listening question remains delayed. Within each pair, reading exposure comes before listening recall. Matching questions are separated by other material. A grouped listening question appears only after all the forms in its accepted answer have been introduced.

Authored order controls new introductions. Earlier material continues through spaced reviews while the learner progresses. Checkpoints provide practice and feedback; they do not lock access to later material.

## Scheduled practice

The basic characters receive two core directions:

- See a kana and recall its sound.
- Hear a sound, with the requested script stated, and recall a matching written form.

Listening questions are grouped by sound and script where multiple forms share a pronunciation. Their answers list accepted forms, including the relevant お／を, じ／ぢ and ず／づ groups when those forms are covered. Separate reading exercises and examples explain the forms and spelling conventions. A sound-only question must not demand a uniquely determined spelling when the recording cannot distinguish it.

Derived forms are taught as productive rules and exercised through selected words and contrasts. There is no requirement to create a separate two-direction question for every marked or contracted combination. Broader forms remain available in teaching or reference material. Common katakana extensions receive selected applications; the broader inventory is reference material.

Add targeted word-reading, lookalike-comparison and alternate-form questions where they serve a learning need. Occlusion can implement a core question where useful; it need not create an additional scheduled task for every character.

The basic inventory accounts for approximately **182 scheduled questions**: 92 reading questions and 90 listening questions after grouping お／を within each script. Selected rule, word, comparison and variant-form exercises are additional. The final total remains to be determined from the complete inventory.

## Teaching and feedback

New material uses the existing guided-question flow. Learners can consult a hint or reveal the answer to learn a new sound and form, then practise retrieval on later encounters. A separate, first-time unscored teaching phase is not required.

Romaji accompanies audio in teaching, hints and answers, but is absent from recall prompts. Provide brief practical sound guidance and examples, including useful distinctions involving ふ, the r-row, ん, and sound length. Formal phonetic notation and a systematic pitch-accent curriculum are outside scope.

Use short shape-based memory cues where useful, especially for confusing characters, rather than requiring an illustrated or story mnemonic for every kana. Keep the initial teaching style visually consistent. Later, introduce selected alternate printed and handwritten forms to support recognition beyond one typeface. A separate card set for every typeface is not required.

## Audio

Use **Microsoft Nanami (`ja-JP-NanamiNeural`) at −20% throughout**. This applies to individual kana, word examples and final reading checks. Normal-rate recordings are not part of this version.

The approved voice and pacing reference is the Microsoft listening audition under `/Volumes/SSD/RectoVerso/raw/japanese-microsoft-kana-test-20261107/`. Its provider inputs, processing and hashes are recorded in `manifest.json`. The owner chose to defer the publication-rights discussion; that decision is not a record of an unrestricted audio licence.

## Scope boundaries

The course covers modern kana, standard reading rules, selected common katakana extensions, short-word decoding, practical sound notes and targeted visual distinctions. It stays with isolated kana and words.

Particle-use readings, phrase or sentence lessons, grammar, kanji, vocabulary memorisation, systematic pitch-accent training and compulsory handwriting are deferred. Word selection must respect those boundaries, including avoiding examples that depend on untaught particle-derived readings.

## Pacing and app dependency

The study target is **ten minutes per day, including reviews**. Start with **four new scheduled questions per day**. Word and comparison questions use that same allowance. Due reviews take priority; learners should be shown how to reduce or pause new introductions when reviews fill the time budget.

Four questions is a starting preset to check against real study sessions. The course has no fixed completion deadline. The basic inventory alone requires at least 46 days of introductions at that cap; additional exercises and pauses extend the course. Introducing every question is not itself proof of mastery, and spaced reviews continue afterward.

Automatic authored introduction order is a launch requirement. The source declares `study: {"newCards": "deckOrder", "newPerDay": 4, "newPosition": "afterReviews"}` for both languages, using the contract implemented in **[app #823 / #805](https://github.com/simonpinkas/RectoVerso/pull/823)**. A supporting app applies these options when first adding a new deck from the gallery. Updates, restored decks and saved learner choices retain their options; direct APKG imports receive no gallery preset. Existing learner changes and study history must survive reimports and updates.

## Working references

- [Approved Microsoft audition and provenance](/Volumes/SSD/RectoVerso/raw/japanese-microsoft-kana-test-20261107/manifest.json)
- [Existing 15-card prototype](/Volumes/SSD/RectoVerso/raw/japanese-kana-15-card-prototype-20261107/README.md)
- [Deck structure audit](/Volumes/SSD/RectoVerso/raw/japanese-deck-structure-audit-20261107/report.json)
- [MEXT kana inventory](https://tsunagarujp.mext.go.jp/assets/download/hiragana_katakana_ver202404.pdf)
- [Bunka loanword spelling tables](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/gairai/pdf/94380801_03.pdf)
