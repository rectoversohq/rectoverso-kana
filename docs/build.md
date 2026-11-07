# Building the course

Install requirements.txt with Python 3.12. The shared interface is scripts/source_data.py::inputs(language), returning metadata, notes, models and deck. The builder uses Anki's backend. GUIDs, native book/card UUIDs, model IDs, field IDs, template IDs and source deck IDs stay stable. Isolated review components have separate preview identities from the combined course and the earlier phone prototype.

Build and verify everything into a new external directory:

```sh
python scripts/ci.py --output /external/kana-ci
```

This checks source inventories, bilingual content, grouped listening forms, prerequisites, reverse-question spacing, unseen checkpoint words, source audio/font hashes and regression cases. It renders twice independently, compares the frozen artwork record, builds every component and both complete languages, then imports, renders, studies and reimports through Anki. Independent packages must preserve source content, schemas, source deck IDs, authored introduction order, media bytes and local study progress. APKG archive bytes may differ because Anki allocates local database timestamps/IDs; the semantic and media checks must match.

To build one component, choose reading, listening, rule, word, contrast, variant or checkpoint:

```sh
python scripts/render_artwork.py --output /external/kana-artwork
python scripts/build.py --language en --type listening --artwork /external/kana-artwork --out /external/review/Japanese-Kana-en-listening.apkg
python scripts/checks/validate-anki.py /external/review/Japanese-Kana-en-listening.apkg --output /external/review/evidence
```

Use fr for French. Omit --type and use Japanese-Kana-en.apkg or Japanese-Kana-fr.apkg for the complete course. The builder refuses paths inside the source checkout or an existing output package. No image, APKG, cache or provider-original recording is generated into source. artwork/artwork.json is the frozen, reviewed record of image names, geometry and hashes; the images themselves remain external.

Audio authoring is a separate online operation, never part of a package build:

```sh
python scripts/synthesize_audio.py --requests source/audio/requests-type-07.json --cache /external/provider-originals
```

It uses ja-JP-NanamiNeural at −20%, preserves provider originals externally, retains all detected speech with 100 ms lead and 250 ms tail, and applies constant gain without time stretching or pitch shifting. Frozen input/hash disagreements fail instead of silently replacing an approved file. ffmpeg is needed only for authoring, not normal builds.

Native iPhone/Duo validation is separate from offline CI. Earlier reading/listening presentations have native evidence. The owner released the simulator to another agent before later types and the final long guide/reference notes could be checked. Do not reclaim it during this work. Source/build passes are not publication approval or native-speaker audio clearance.
