---
title: "AI Talking Heads That Don't Slip: Lip-Sync Timing, Jaw Artifacts and Three Failure Modes"
slug: "ai-talking-head-lip-sync"
date: "2026-11-18"
category: "Short-Form Production"
excerpt: "Lip-sync does not fail all at once. It drifts four frames over eight seconds, or the jaw walks through the teeth on the first plosive. Both are fixable before the render."
description: "A working method for AI talking-head shorts: generate voice at final speed, cut at phrase boundaries, keep clips under eight seconds, and read three specific failure modes — drift, plosive jaw, dead eyes — from a quarter-speed review."
tags: ["lip-sync", "talking head", "TTS", "AI avatar", "short-form"]
tools: ["elevenlabs", "adcreative"]
featured: false
---

A talking-head clip is judged by a viewer who cannot name what is wrong. They see a face speaking and something in the mouth region reads as false, so they scroll. Nobody comments "the jaw intersected the upper lip on the bilabial"; they just leave.

That makes lip-sync a QA problem more than a generation problem. The tools are good enough that a clean clip is achievable most of the time; the work is recognising at quarter speed which clips are not clean, and knowing which parameter caused it. Three failures account for nearly every clip that has to be thrown away.

## Generate the voice first, at the speed it will be published

Every lip-sync problem starts one step before the render. If the voice is generated at 100% and then sped up 8% to fit a 30-second cut, the mouth was animated against a rhythm that no longer exists, and the result drifts. Speed changes belong before the video model sees the audio, never after.

What the audio has to be before it can be lip-synced:

- **Final speed and pitch.** No time-stretch afterwards. If the read is too long, cut words, not milliseconds.
- **Silence trimmed at both ends**, with 80–120 ms of room at the head so the first consonant is not clipped.
- **One consistent pace**, roughly 150–165 words per minute for a vertical short. Faster reads look better in 9:16 but give the model less to work with per phoneme.
- **No overlapping music bed in the render input.** Sync against the dry voice and mix the bed in the edit; a bed inside the render makes the mouth chase a composite signal.
- **De-essed.** Sibilance that survives into the render tends to produce a small, repeating jaw flutter on every "s".

Then export per phrase, not per script. A phrase of three to eight seconds is the unit that works: long enough that the model has context, short enough that drift cannot accumulate.

## Cut at phrase boundaries, align on the plosive

The assembly order matters more than any single setting:

1. Generate voice as one file, then split at punctuation into phrase WAVs. Keep the splits on commas and full stops, never mid-word.
2. Render one clip per phrase. Do not render a 40-second monologue and hope.
3. In the edit, align each clip on its first plosive — the frame where the "p", "b" or "t" closes — and let the phrase run out.
4. Overlap clips by two frames at the joins and hide the seam under a cut or a small reframe. Hard joins between phrases are where the jaw resets visibly.
5. Add the music bed and captions after all clips are aligned, so a later fix does not move the sync.

The eight-second ceiling is not arbitrary. Drift is cumulative and roughly proportional to clip length: a clip that starts perfectly aligned can be four frames late by second eight, which is exactly where the eye starts to notice on a phone. Splitting a 24-second monologue into four phrases and joining them costs ten minutes and removes the entire class of problem.

## The three failure modes

| Symptom | What it looks like | Likely cause | Fix |
| --- | --- | --- | --- |
| Drift | Mouth closes 2–5 frames after the audio on later words | Clip too long, or speed changed after render | Re-render per phrase under 8 s, no time-stretch |
| Plosive jaw | Jaw passes through the upper teeth or lip on "m", "b", "p" | Head too small in frame, or too much head motion for the model | Enlarge the face to 45%+ of frame height, reduce motion amplitude |
| Dead eyes | Mouth moves correctly but the face reads as a mask | Single-frame source, no blink, flat lighting | Use a short video source or add blink and micro-motion; keep lighting consistent across clips |
| Hairline melt | Edges of hair blur and shift on fast turns | Motion exceeds what the model can carry at that resolution | Cut the turn, hold the frame, or reframe wider |
| Lip flap on silence | Mouth keeps moving in pauses | Voice file has room tone the model treats as speech | Gate silence in the WAV before render, or split phrases tighter |

Two of these are framing decisions rather than model settings, which is why they recur: a talking head that fills 30% of a vertical frame simply does not carry enough pixels on the mouth to survive generation, and no prompt fixes that.

## Framing and settings that hold up

- **Face height 45–55% of the frame.** Chest-up in 1080×1920. Bigger than a mid-shot, smaller than a close-up, so the mouth is 90–110 px tall after encoding.
- **Three-quarter angle, not straight-on.** A 15–25° turn hides the jaw seam and reads as more natural on a phone.
- **Camera locked.** Any push-in during a speaking clip fights the model's own motion.
- **One lighting setup per series.** Matching colour temperature and key direction across clips is what makes a series feel like one recording; a face relit between clips reads as a different person even when the model is identical.
- **Source length.** A two-to-four second source video of the subject blinking and settling produces better results than a single still, because the model has real motion to interpolate.

## The quarter-speed review

Watch every finished clip at 0.25× before it goes anywhere else. At that speed the failures separate cleanly: drift shows as the mouth finishing after the sound, the plosive fault shows as a single bad frame at a bilabial, and the dead-eye clip shows as a face that never changes between blinks.

Then watch at full speed with sound off, because that is how a large share of the audience sees it. A clip that passes quarter speed but reads as a puppet with the sound off has a motion problem, not a sync problem — usually too much head movement per phrase.

Keep the review sheet next to the batch: clip id, phrase text, pass or fail, and the reason in three words. By the tenth video the pattern is obvious, and it is almost never the model version.

## Before publishing a talking-head short

- [ ] Voice generated at final speed; no time-stretch in the edit
- [ ] Each clip under 8 seconds, split on punctuation
- [ ] Face 45%+ of frame height, three-quarter angle, camera locked
- [ ] First plosive of each phrase aligned, joins hidden under cuts
- [ ] Music bed and captions added after alignment
- [ ] Quarter-speed review passed on all clips
- [ ] Watched with sound off, once, from start to finish

A viewer forgives an imperfect voice far more readily than an imperfect mouth, because the mouth is the thing they are looking at. Treat alignment as the deliverable and the rest of the clip gets easier.
