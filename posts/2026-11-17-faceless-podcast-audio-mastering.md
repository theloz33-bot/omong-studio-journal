---
title: "Mastering Audio for Faceless YouTube and AI Podcasts: LUFS Targets, Chain Order and a Per-Line Voiceover Workflow"
slug: "faceless-podcast-audio-mastering-lufs"
date: "2026-11-17"
category: "Audio"
excerpt: "A faceless channel is an audio product with pictures attached. Four numbers keep forty episodes at the same level, and one chain order keeps the voice sounding like the same show."
description: "Speech-audio workflow for faceless YouTube and AI podcasts: platform LUFS targets, the seven-stage voice chain, bed ducking levels, and per-line voiceover timing."
tags: ["audio mastering", "LUFS", "faceless YouTube", "podcast", "voiceover"]
tools: ["elevenlabs"]
featured: false
---

A faceless channel can survive ordinary footage. It cannot survive an episode 4 dB quieter than the last one: nobody writes a comment, they just reach for the volume knob, and the show stops feeling like a show.

Speech mastering is narrower than music mastering, and more measurable: every word understood on a phone speaker, at the same level as last week, with nothing touched. That is four numbers.

## Speech mastering is four numbers, not a tone

| What | Measured as | Why it is the goal |
| --- | --- | --- |
| Level | Integrated LUFS across the whole episode | Sits where every other show the listener hears sits |
| Headroom | True peak in dBTP, not sample peak | Nothing clips after the platform re-encodes |
| Clarity | Voice 4–8 dB above the bed, 1–4 kHz intact | Words survive a phone speaker |
| Consistency | Spread of LUFS across episodes under 1 LU | No volume knob between episodes |

Tone matters, but tone is taste. These four are the difference between a channel and a folder of files.

## The targets, by destination

| Where it plays | Integrated | True peak | LRA |
| --- | --- | --- | --- |
| YouTube, long and Shorts | −14 LUFS | −1.0 dBTP | 7–9 LU |
| Podcast, stereo (Apple, Spotify) | −16 LUFS | −1.0 dBTP | 6–8 LU |
| Podcast, mono | −19 LUFS | −1.0 dBTP | 6–8 LU |
| TikTok, Reels, Shorts | −12 to −14 LUFS | −1.0 dBTP | 5–7 LU |

Platforms normalise to their own target, so what you deliver decides how far they turn you up or down. Pick one target per destination, log the measured value, and do not move it mid-season. Verify the documented target for your platform; these are common practice, not a guarantee.

## Measure the export, not the session

- Measure the whole file, not a ten-second section — integrated loudness is an average over time.
- Measure after the limiter, on the exported master, not on the session bus.
- Use true peak: inter-sample peaks pass a sample-peak meter and clip a lossy encoder.
- Measure start, middle and end; if they disagree, take the median and look at why. Store the number beside the episode.

## The voice chain, in seven stages

Each stage exists for one problem; if it is not in this recording, skip the stage.

| # | Stage | Starting setting | What it fixes |
| --- | --- | --- | --- |
| 1 | High-pass filter | 80–100 Hz, 12 dB/oct | Rumble, handling noise, HVAC |
| 2 | Corrective EQ | −3 dB at 300–500 Hz, Q 1.0 | Small-room boxiness |
| 3 | Presence EQ | +2 dB at 3–5 kHz, Q 0.8 | Intelligibility on phone speakers |
| 4 | De-esser | 5–8 kHz, −3 to −4 dB, wide Q | Sibilance, worst on whispers |
| 5 | Compressor | 3:1, attack 10 ms, release 80 ms, 3–6 dB reduction | Level consistency and density |
| 6 | Saturation, optional | Very light, second harmonic | Presence a compressor cannot add |
| 7 | Limiter | Ceiling −1.0 dBTP, lookahead 5 ms | Peaks and final loudness |

Order matters more than settings: corrective EQ before compression, so the compressor is not reacting to a resonance you are about to remove; de-esser before compression, because compression pulls the body up around the sibilance; limiter last, and if it works harder than 3–4 dB the level problem is earlier in the chain. Two gentle stages — 2:1 at 2 dB, then 3:1 at 3 dB — sound more natural than one 4:1 doing five, because neither pumps.

## Everything else is placed against the voice

Set the voice at the target first. Music, effects and room tone are then placed relative to it, never the other way round.

| Element | Level | Note |
| --- | --- | --- |
| Voice | The target, e.g. −16 LUFS | The reference everything else is set against |
| Bed under voice | −14 to −18 dB below voice | Around −30 to −34 LUFS in a −16 LUFS mix |
| Bed in gaps | +6 dB above its ducked level | Rises only when nobody is speaking |
| SFX accent | −10 to −14 dB below voice | Loud enough to feel, quiet enough not to mask |
| Room tone | −55 to −50 dBFS | Continuous, never digital silence |

Four ducking settings worth keeping: sidechain the bed from the voice, not by hand-drawn automation; attack 100–150 ms so the first consonant is not clipped; release 300–500 ms; 4–6 dB of depth, because more and the listener hears the music move. Carve a 2–3 dB dip at 1–4 kHz in the bed itself, and fade out over 1.5 seconds, not 0.2.

## Voiceover: generate per line, time it after the picture

For a faceless video the narrator is the only performer, so consistency is a technical problem, not an acting one. A saved voice per show, generated and exported per line, solves most of it. [[tool:elevenlabs|ElevenLabs]] with one saved voice is the difference between a narrator who sounds the same in the outro as the intro and one who changes accent at the bridge.

1. Lock the script and mark where each line starts against the cut picture.
2. Generate one file per line, not one long take — separate files let you slide a line three frames without regenerating the rest.
3. Pace narration at 150–160 words per minute, slower for anything calm. If a read rushes, shorten the sentence; adjectives rarely fix pacing.
4. Fit the voice to the cut once there is more than one hook line, nudging the picture so the last word lands on a beat.
5. Leave the first two seconds clean — platforms fade in and clip a line starting at 0:00. Keep narration near −3 dBFS with music ducked 3–6 dB, and check on a phone speaker.

## Normalise with one gain change, then limit

Normalisation is a measurement plus a fixed gain, not compression and not limiting. If the result pumps, the pumping was created earlier.

1. Export a reference mix near −18 dBFS average, peaks below −6 dBFS.
2. Measure integrated LUFS over the whole file and write it down.
3. Apply the difference to the target as a single gain change.
4. Set the limiter ceiling to −1.0 dBTP; more than 3 dB of limiting sends you back to the compressor.
5. Measure again — the limiter moves integrated loudness by 0.3–1.0 LU — and keep two files: a −16 LUFS archive master and a −14 LUFS copy for a video-first upload.

## The episode log is what keeps a series level

Consistency is a process: one line per export, four columns, and drift becomes visible before a viewer mentions it.

| Episode | LUFS | dBTP | Bed | Notes |
| --- | --- | --- | --- | --- |
| EP-041 | −16.1 | −1.2 | lo-fi, 72 BPM | new mic position, +1 dB presence |

A spread wider than 1 LU across a season is the most common reason a series feels amateur, and no listener can tell you why. Four things stay fixed while a season runs: microphone distance and interface gain, the chain preset, the bed library and its level, and the delivery target. Change them between seasons, not between episodes.

## Checklist before an export leaves the machine

- [ ] Voice at the target LUFS, measured on the exported file
- [ ] True peak at or below −1.0 dBTP after the limiter
- [ ] Bed 14–18 dB under the voice, sidechained, ducking 4–6 dB
- [ ] Room tone under every gap; no digital silence between sentences
- [ ] Measurement written into the episode log

## What the order actually buys

Not speed on any stage — the stages take the same time either way. It buys the second pass: an episode mixed against a measured target and a log gets one assembly and one fix, while one mixed by ear gets re-mastered later, when the previous episode suddenly sounds louder.

The chain builder, the 40 bed, SFX and narrator prompts and the 13-chapter playbook behind these numbers are packaged as the [Podcast & Faceless YouTube Audio Production Kit](https://lozzy36.gumroad.com/l/podcast-faceless-audio-kit) if you would rather not rebuild the sheet. Either way, keep the order: voice first at a measured level, chain in a fixed sequence, everything else placed under the voice, and a number in the log at the end.
