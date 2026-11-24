---
title: "One Vertical Ad, Two Languages: Localising Captions and Voiceover Without Re-Cutting the Picture"
slug: "localise-vertical-ad-captions-voiceover"
date: "2026-11-24"
category: "Short-Form Production"
excerpt: "A client approves the Korean cut and then asks for English. The picture should not move. A per-line sheet, a reading-speed budget for each language and a delivery package built around a silent master keep it that way."
description: "How to localise a 9:16 AI ad into a second language: lock picture, a per-line sheet, Netflix reading-speed ceilings for Korean and English, per-line voiceover, SRT files and a silent master."
tags: ["localisation", "subtitles", "SRT", "voiceover", "9:16", "Korean", "English"]
tools: ["elevenlabs"]
featured: false
---

The cut is approved in Korean. Two days later the client asks for an English version "with the same edit". Then the problems arrive in order: the English line for shot three runs half a second past the cut, the caption on shot five is now two lines and sits on the product, and the end card has Korean text baked into the generated frame.

None of this is a translation problem. It is a production-order problem. A second language is cheap when the project was built to accept one, and expensive when the language was welded into the picture.

## Lock picture first, then localise per line

The rule that saves the most time: **the picture does not change for a language.** Shot order, shot length and every cut point stay where the approved version put them. What changes is the text layer, the voiceover and the mix.

That only works if you localise per line, not per script. Translating the script as a paragraph produces good prose and lines that no longer fit their shots. Translating line by line, against the time each line has on screen, produces lines that fit every time.

## The line sheet

One row per caption or voiceover line. It lives next to the project and it is the only place a line is edited.

| Column | Example | Why it exists |
| --- | --- | --- |
| `id` | `L03` | Matches the voiceover file name and the SRT block |
| `shot` | `S03` | The shot the line must fit inside |
| `in` / `out` | `00:00:04,200` / `00:00:06,000` | The time the line owns, copied from the locked cut |
| `slot` | `1.8 s` | out minus in; the budget for both languages |
| `ko` | source line | What was approved |
| `en` | target line | Written to fit the slot, not to mirror the source |
| `ko_vo` / `en_vo` | measured seconds | Duration of the exported voiceover take |
| `fix` | `shorter` / `ok` / `move cut` | The decision, in one word |

The `fix` column is where the discipline is. "Move cut" should be rare and needs the client to agree, because it changes the approved picture.

## A reading-speed budget for each language

Captions in a feed are not cinema subtitles, but streaming style guides are useful as a ceiling — a number beyond which the line is definitely too long. Netflix publishes per-language guides, and for adult programmes they set:

| Language | Characters per line | Reading speed ceiling | Counting note |
| --- | --- | --- | --- |
| English (USA) | 42 | up to 20 characters per second | — |
| Korean | 16 | up to 12 characters per second | Latin letters, spaces and punctuation count as half |

Multiply the slot by the ceiling and you get the maximum length of the line on screen. A 1.8-second slot allows at most 36 English characters and about 21 Korean characters — which in Korean already means two lines at 16 per line. For a 9:16 feed, where captions are usually two to four words and sit inside a safe band, aim well under the ceiling. The ceiling just tells you when to stop arguing and rewrite.

The two languages fail in different places. English tends to break the per-second ceiling on short slots; Korean tends to break the per-line count and spill to a second line. Check both columns, not just the one you are writing.

## Per-line voiceover, measured not guessed

Voiceover follows the same rule as captions: one file per line, named by `id`. Generate each line in the target language with one saved voice per language, so the narrator does not change character between lines. [[tool:elevenlabs|ElevenLabs]] works for this because a saved voice can be reused across both language versions and every line exports as its own file, which makes the duration column a measurement instead of an estimate.

Then compare each take against its slot:

1. **Fits with room.** Place it on the line's `in` point and move on.
2. **Slightly long.** Trim leading and trailing silence first; most overruns are breath, not words.
3. **Clearly long.** Rewrite the line shorter and regenerate. Time-stretching a voice by more than a few percent is audible, and squeezing a sentence to fit a cut makes the narrator sound rushed in exactly one place, which is worse than sounding slower everywhere.
4. **Much shorter.** Leave the gap. A breath of music is fine; padding the line with filler words is not.

Mix every language to the same target. This studio's delivery spec is −14 LUFS integrated with peaks at −3 dBFS, and each language version is measured separately, because a different voice track changes the integrated number even when the music bed is identical.

## SRT: one file per language, same timings

The SRT format is plain text: a block number, a time range with commas before the milliseconds, one or two lines of text, and a blank line.

```
3
00:00:04,200 --> 00:00:06,000
Same box. Half the shelf space.

4
00:00:06,000 --> 00:00:08,400
Ships folded, opens in one pull.
```

Keep block numbers and time ranges identical across `ad_ko.srt` and `ad_en.srt`. When the timings match, a reviewer can open both files side by side and check one line against the other, and a later re-time is done once and copied, not done twice.

## Build the picture to accept a second language

Most localisation pain is created at the generation stage, weeks before anyone asks for English.

- **No text inside generated frames.** Signs, labels and end-card copy produced by the image or video model are part of the pixels and cannot be translated. Prompt for clean surfaces and add text as a graphics layer in the edit.
- **Leave caption room in the composition.** The longer language decides how much room that is. If the frame only works with one short line, it will fail the moment a two-line Korean caption arrives.
- **Choose a font with both scripts.** A caption preset that renders English beautifully can turn Hangul into empty boxes. Test a Korean line in the preset before the first export, not on delivery day.
- **Keep the music bed separate.** A bed that was mixed with the voice baked in has to be rebuilt for every language.

## The delivery package

The version that survives a third language request is built around a silent master.

| File | Contents |
| --- | --- |
| Silent master | Picture and music bed, no captions, no voiceover |
| Voiceover per language | One WAV per language, or one per line with the sheet |
| SRT per language | Identical timings, one file each |
| Burned-in versions | One MP4 per language, for platforms where uploading an SRT is not practical |
| Line sheet | The final text of every line, both languages |

One public piece on the studio's hire page shipped this way: captions burned in, six separate narration tracks in Korean and English, and a silent master alongside. Another language would mean new voiceover files and one more SRT, not a new edit.

If a series is headed for more than one market, the [AI Short-Form Character & Motion Transfer Kit](https://lozzy36.gumroad.com/l/ai-shortform-character-kit) covers the storyboard and shot side, and the [Podcast & Faceless YouTube Audio Production Kit](https://lozzy36.gumroad.com/l/podcast-faceless-audio-kit) covers the per-line voiceover and loudness side.

## Checklist before the second language ships

- [ ] Picture locked; no cut moved without the client agreeing
- [ ] Every line in the sheet with a measured slot
- [ ] Both languages under their reading-speed ceiling for every slot
- [ ] One voiceover file per line, named by line id
- [ ] Each language mix measured on its own
- [ ] SRT files share block numbers and timings
- [ ] Korean caption checked in the actual font preset
- [ ] Silent master exported and kept with the project

A second language should cost a voiceover session, a sheet of rewrites and an afternoon of checks — not a rebuilt edit. Decide that before the first shot is generated. If you would rather hand the whole bilingual package off, the [hire page](/omong-studio-journal/services/) lists what a cut costs and what comes back with it.
