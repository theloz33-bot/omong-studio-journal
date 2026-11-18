---
title: "Suno Stems for a 60-Second Ad: Generate the Bed, Split It, Cut Picture to the Beat"
slug: "suno-stems-60-second-commercial"
date: "2026-11-18"
category: "Music Video"
excerpt: "A commercial bed is not a song with thirty seconds deleted. Generate it in sections, split it into stems, and rebuild sixty seconds whose cuts land on the beat — not near it."
description: "A practical workflow for AI music in 60-second product commercials: Suno section prompts, BPM-to-frame math, the three stem splits, rebuild moves and beat-accurate cut points."
tags: ["Suno", "stem separation", "commercial music", "beat sync", "video editing"]
tools: ["elevenlabs"]
featured: false
---

A sixty-second ad with a sixty-second generated track is a scheduling problem dressed as a music problem: the drop arrives four seconds after the product turn, the drums stop two frames before the logo, and the only fix anyone knows is to slide the song and hope.

Stems remove the hoping: with parts as separate files you rebuild sixty seconds instead of trimming a song, and the picture decides where each part goes.

## Why split the bed before editing it

An unsplit track gives you one fader and one timeline, so every fix is global: move the intro to hit the logo and the price card moves with it. Split it and four moves get cheap — mute the drums for four bars under the reveal, loop two bars to stretch a hold from 1.6 to 3.2 seconds, keep the bass while dropping the pad behind a spec card, let the tail ring 800 ms past the last frame. Those are picture edits made with music parts, which is what a commercial bed has always been.

## Step 1: brief sections, not a song

Left alone, a model writes a song: intro, verse, chorus, bridge. A spot needs events in shot-list order, so describe the sections and their job.

| Section tag | Ask for | Job in the edit |
| --- | --- | --- |
| `[Intro]` | 4 bars, filtered drums only | First frame and brand line |
| `[Build]` | 8 bars, add bass and a riser | Problem-to-solution turn |
| `[Drop]` | 8 bars, full mix, no vocal | Product on screen, loudest four seconds |
| `[Breakdown]` | 4 bars, drums out, one held note | Price or spec card |
| `[Outro]` | 2 bars, resolve, 1.5 s tail | Logo frame |

Name tempo and key explicitly ("120 BPM, A minor") so takes stay in one world, say "instrumental, no vocals" because stacked vocals split worst, and generate four to six takes at two lengths — the long one usually has the better drop. Section-tag wording is collected in the [Cinematic AI MV & Suno Prompt Vault](https://lozzy36.gumroad.com/l/ai-mv-suno-prompt-vault).

## Step 2: pick a tempo your frame rate likes

Sixty seconds is fixed, so tempo decides how many bars you have. In 4/4, one bar is 240 ÷ BPM seconds.

| BPM | One bar | Whole bars in 60 s |
| --- | --- | --- |
| 90 | 2.667 s | 22.5 |
| 100 | 2.400 s | 25 |
| 120 | 2.000 s | 30 |
| 125 | 1.920 s | 31.25 |
| 128 | 1.875 s | 32 |

At 120 BPM a bar is exactly two seconds, so thirty bars fill the spot and every eighth bar lands on a 15-second cutdown. That arithmetic, not taste, is why advertising lives near 120.

The frame rate closes the decision, because a beat between frames can only land near the cut.

| Frame rate | Beat at 120 BPM | Tempos giving whole-frame beats |
| --- | --- | --- |
| 24 fps | 12 frames | 120, 90, 144 |
| 25 fps | 12.5 frames — drifts | 125 (12), 100 (15) |
| 30 fps | 15 frames | 120, 100, 90 (20) |

At 25 fps a 120 BPM take sits half a frame off every cut. Retime 4% (120 → 125) rather than fixing it by eye at each point.

## Step 3: choose the split for the edit you have

Suno's extraction has three modes and they answer different questions; check labels and credit cost in your own account before a batch, because this moves. As of this writing: Auto Split (Pro and Premier) returns up to 12 category stems — vocals, drums, bass, guitar, keys — for 50 credits per extraction; Split from Mix pulls one chosen part plus the mix without it for 10 credits per stem; Advanced Split (Premier only) names instruments from a list of nearly 100. Free plans get none of it.

| Mode | What you get | Use in an ad |
| --- | --- | --- |
| Auto Split | Up to 12 category stems | Rebalance: drums up 2 dB, pad down under dialogue |
| Split from Mix | One part plus its complement | Remove one muddy element or a vocal |
| Advanced Split | Named instruments | Keep the cello, cut the violin under a card |

Two cautions that cost credits. Separation reconstructs parts from a finished stereo mix, so a stem is an estimate: check the busiest four bars for kick holes before building on it. And requesting an instrument the song lacks still spends credits and returns nothing usable. An open-source separator (Demucs) does the same job more cheaply; what matters either way is 48 kHz 24-bit WAVs with identical start times, so parts stay sample-aligned.

## Step 4: rebuild sixty seconds from parts

Build in picture order with the original mix muted underneath as a reference.

1. **Top and tail first.** In on a downbeat, out on the last beat you want, and let the tail ring past the final frame rather than fading inside the picture.
2. **Stretch with a loop, not a slide.** Duplicate the two bars before the drop and crossfade the seam at a zero crossing with 10–20 ms fades. Longer smears the kick, shorter clicks.
3. **Cut parts, not volume.** Under dialogue, mute the pad and keep drums, bass and one held note — quieter without sounding ducked.
4. **Carry one element throughout.** A bass line or hi-hat that never drops out is what makes a rebuilt bed feel like one piece.
5. **Re-enter one beat early.** Hitting the logo with the full mix on the beat feels reactive; one beat before, it feels causal.

## Step 5: place cuts on the transients

Mark a bar every two seconds at 120 BPM, then cut on beats 1 and 3 for a calm spot, every beat for a launch. Cut **one to two frames before** the beat so the transient blooms just after the cut.

| Moment | Cut on | Offset |
| --- | --- | --- |
| Logo reveal | Outro downbeat | 2 frames early |
| Product turn | Drop, beat 1 | 1 frame early |
| Price card | Breakdown, beat 3 | On the frame |
| Final button | Last beat, hold 8 frames | 2 frames early |

## Step 6: voice, then loudness

Cut the read against the finished picture, not the raw track, so line endings can be nudged to the beat instead of stretching the music to the read. One saved voice per brand keeps a campaign consistent across fifteen spots — [[tool:elevenlabs|ElevenLabs]] with per-line exports lets you slide one sentence three frames.

Social delivery sits near −14 LUFS integrated with true peak at −1.0 dBTP; broadcast specs differ by destination, so read the delivery sheet. Music 12–16 dB under the voice, lifted only in the gaps, and check on a phone speaker before the client does.

## What goes wrong

| Symptom | First check |
| --- | --- |
| Hollow kick after the split | It bled into the bass stem and was cut twice — solo both over one bar |
| Loop seam clicks | Edit landed mid-waveform — nearest zero crossing, 10–20 ms fade |
| Cuts feel late | Hit sits on the cut frame — move 1–2 frames earlier |
| Take drifts out of tempo | Two takes stitched — use one, or retime, never both |

## Checklist before export

- [ ] One take, end to end, tempo and key written down
- [ ] Bar line lands on the 15-second cutdown
- [ ] Stems exported 48 kHz, same start time, sample-aligned
- [ ] Loop seams faded at zero crossings, checked on headphones
- [ ] Every cut 1–2 frames before its transient
- [ ] Voice 12–16 dB above the bed, bed lifted only in gaps
- [ ] Loudness and true peak measured on the exported file

The point is not purity. A client will ask for the drop a second earlier, and with stems that is one edit — with a stereo file it is a new generation and a new round of notes.

The picture side of the same job — 30-second structure, lighting and material prompts — is in the [AI Product Commercial & 3D Asset Prompt Studio](https://lozzy36.gumroad.com/l/product-commercial-3d-studio); the loudness planner and bed prompts are in the [Podcast & Faceless YouTube Audio Production Kit](https://lozzy36.gumroad.com/l/podcast-faceless-audio-kit). If the whole spot needs building, the studio takes [commissions](https://theloz33-bot.github.io/omong-studio-journal/services/).
