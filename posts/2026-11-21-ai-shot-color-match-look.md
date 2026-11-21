---
title: "Matching Colour Across AI Shots: Measure Four Numbers, Grade in Two Passes, Then Apply the Look"
slug: "ai-shot-color-match-look"
date: "2026-11-21"
category: "Short-Form Production"
excerpt: "Six AI clips cut together can look like footage from six cameras. The fix is not a better LUT — it is measuring four numbers per clip and grading in the right order, so one look survives a whole series."
description: "A two-pass workflow for AI video colour: what to measure on each clip, the Rec.709 targets to hit, why the look goes last, a shot-match table, and the prompt fields that cut correction time in half."
tags: ["colour grading", "shot matching", "AI video", "DaVinci Resolve", "look development", "series consistency"]
tools: ["gamma"]
featured: false
---

Nine AI shots cut into one 45-second vertical ad, and the sequence reads as if six different cameras filmed it. One shot is blue, one is amber, one has crushed blacks and another is so flat that the caption text sits on milk. Nothing is wrong with any single clip — each is internally consistent with a camera that never existed twice.

AI video does not deliver footage, it delivers finished-looking pictures, each with white balance and contrast baked in. One LUT over the timeline cannot fix that. You fix it per clip, in a fixed order, using numbers instead of eyes.

## Why AI clips drift, and why it is not the model's fault

A text-to-video model has to invent the lighting. Give it "a woman in a grey coat, cinematic" and the words carry no colour temperature, no time of day and no contrast target, so the model fills those in from its training distribution — which is wide. Two generations of the same prompt on different days can land 500 K apart, and a re-roll of one shot inside an accepted sequence lands somewhere else again.

Three consequences follow, and each one is a decision:

- **A prompt is not a colour reference.** Words like "cinematic", "moody" or "film look" pull a different contrast curve every time. A number does not.
- **Mixing providers multiplies the drift.** A sequence that uses two or three models will always need matching; assume it and budget for it.
- **The clip arrives display-referred.** There is no log space to fall back on and no raw headroom, so aggressive corrections cost information. Small, early, per-clip moves are cheaper than one big rescue later.

## Measure four numbers before touching a slider

Grading by eye on a phone screen is how a sequence ends up three different colours. Put scopes on and read four things per clip. DaVinci Resolve's free version has all of them; Lumetri in Premiere has the same data behind a different panel.

| What to measure | Rec.709 target (legal range) | What it tells you |
| --- | --- | --- |
| Black point | 0 IRE — 16 in 8-bit | Whether the clip is milky or crushed |
| Mid-gray | about 40–45 IRE | Overall exposure of the subject |
| White point | 100 IRE — 235 in 8-bit, skin highlights below 95 | Whether highlights clip when you add contrast |
| Skin hue and chroma | skin sitting on the vectorscope's skin-tone line, roughly eleven o'clock, inside the gamut ring | White balance errors that look "warm" rather than wrong |

Pick one shot as the hero — usually the one the thumbnail will show — and neutralise *that* clip until it looks boring. The others get matched to boring, not to beautiful. And match in the order black → mid → white → saturation: jumping to saturation compensates for a contrast error and leaves a cast you will spend twenty minutes removing.

## Grade in two passes, and the look goes last

The workflow that holds up is two passes, in this order:

1. **Pass one, per clip: normalise.** White balance with the picker on something known to be neutral, then lift/gamma/gain to hit the three luminance targets, then saturation to bring skin into a plausible range. Every clip ends up looking flat and unremarkable. That is correct.
2. **Pass two, on the timeline: the look.** One node or one adjustment layer over all clips, holding the LUT, the film emulation, the split-tone. Applied after the corrections, not before.

The order is not a preference. A 3D LUT maps absolute input values to absolute output values — put it first and your clip corrections are then fighting the LUT's curve, which distorts both. Put it last and a single look survives nine clips that were each wrong in a different direction.

It also means the client's "can it be warmer" is one node instead of nine, and the tenth clip tomorrow inherits the look after a single normalisation against a saved still.

## A real match table from one 45-second cut

This is what pass one looked like on a nine-shot vertical ad in November 2026. The numbers are corrections, not absolutes; what matters is that each clip got a written target instead of a feeling.

| Shot | What the model returned | Correction in pass one | Time |
| --- | --- | --- | --- |
| 1, hero | Neutral, slightly flat | Lift −4, gain +6, saturation +8 | 4 min |
| 2, close-up | Cool, about 500 K blue | Temp +10 toward warm, tint +2 | 5 min |
| 3, hands | Warm and contrasty, blacks crushed | Lift +8, gain −5, saturation −6 | 6 min |
| 4, wide | Washed out, milky blacks | Lift −10, mid +5, saturation +12 | 5 min |
| 5, product | Green cast in the shadows | Tint +4, shadow hue −3 | 7 min |
| 6, end card | Nearly right, tiny hue shift | Tint +1 | 2 min |

About thirty minutes for pass one. Once those corrections were saved as stills, the next ad in the same format took eleven minutes for nine shots.

## The prompt fields that cut the correction time

Post is the expensive place to fix colour. Half of this work disappears if the generation is told what the light is doing, in the same terms a gaffer would use.

| Prompt field | Write this, not that | Why it works |
| --- | --- | --- |
| Light source | "single large soft window light from camera left" instead of "cinematic lighting" | A named source constrains direction and softness together |
| Colour temperature | "overcast daylight, 5600 K" instead of "natural light" | Temperature becomes a number the model can hit |
| Time of day | "late afternoon, low sun, long shadows" | Time carries its own palette and contrast |
| Contrast | "flat low-contrast grade, blacks lifted, no clipping" | Prevents the crushed look you would have to undo |
| A neutral in frame | "white painted wall behind the subject" | Gives you a white-balance picker target that is actually neutral |
| A stated look | One reference film or stock name, reused for the whole series | Consistency across generations, not just within one |

The highest-value line there is the neutral in frame: a white wall or a light grey backdrop lets you white-balance with the picker instead of guessing by eye.

## What carries across a series

- **A saved still per look.** One graded frame is the reference every new clip is matched against. Without it, "the look" is memory.
- **A .cube export.** Portable to a second editor, another app, or the next version of the project.
- **Two looks maximum per series.** Five looks are five chances to drift.
- **A written spec.** White balance, black level, mid-gray, saturation range, LUT file name — the difference between a series and a folder of clips.

For the lookup side of this, the [Color Grade & Look Lab](https://lozzy36.gumroad.com/l/color-grade-look-lab) collects 48 film looks with the grade planner and the shot-match arithmetic used above, so a new sequence starts from a written target rather than a fresh guess.

## Checklist before the export

- [ ] Hero shot neutralised first, everything matched to it
- [ ] Black point, mid-gray and white point hit on every clip, in that order
- [ ] Skin checked on the vectorscope, not by eye
- [ ] Look applied once, at the end of the chain
- [ ] Saved still and .cube exported with the project
- [ ] Exported file watched on a phone at half brightness before delivery

Colour matching is the least glamorous ten minutes in an AI edit and the one that decides whether nine clips read as one piece of work. Measure first, normalise second, apply the look once — and the next job in the same format starts from a preset instead of from zero. If the grading is the part you would rather hand off, the [hire page](/omong-studio-journal/services/) lists what a cut costs and what comes back with it.
