---
title: "Two Revision Rounds, Not Ten: Scoping Client Feedback on AI Video Jobs"
slug: "ai-video-revision-rounds-feedback"
date: "2026-11-26"
category: "Short-Form Production"
excerpt: "On an AI video job, every vague note costs a fresh batch of generations. A written revision scope, a timecoded feedback sheet and a clear line between a fix and a change keep a fifteen-second ad from turning into a month of rounds."
description: "How to scope revisions on AI-generated video ads: what counts as a round, a timecoded feedback sheet, fix versus change, what to lock at each stage and how to word the quote so extra rounds are billable."
tags: ["client work", "revisions", "AI video", "feedback", "freelance", "short-form ads"]
tools: ["elevenlabs"]
featured: false
---

The cut goes out on Monday. On Tuesday the client replies: "Can the character look a bit friendlier? And maybe try a warmer feel overall." On Thursday a second person on their side sends a different list. By the following week you are on version nine, nobody remembers what version four looked like, and the hours on the job have quietly doubled.

Revision creep happens on every kind of video work, but AI production makes it more expensive. In a traditional edit, "a bit friendlier" might mean a different take that already exists. With generated footage it often means a new batch of generations, new takes to review and a new colour match against the shots you kept. This post is the scope, the feedback sheet and the wording that keep revisions to a number you agreed in advance.

## Why AI jobs need a tighter revision scope

Three things make open-ended feedback costly on generated work:

- **Regeneration is not editing.** Changing a character's expression or a background usually means generating again, not trimming. Each attempt spends credits and review time, and the first attempt is rarely the keeper.
- **Changes ripple.** A new take of shot 3 may no longer match the colour or lighting of shots 2 and 4, so one note can touch three shots.
- **Late changes are the slowest.** A note on the script at the start costs a sentence. The same note after picture lock can mean new voice lines, new timings and a re-cut.

None of this is the client's fault; they rarely know which notes are cheap. The scope makes that visible before work starts.

## Define what a "round" is

Most disputes come from the word "round" meaning different things to each side. Write it down in the quote:

| Term | Definition to put in writing |
| --- | --- |
| Round | One consolidated list of notes from the client, delivered at once, answered with one new version |
| Consolidated | All reviewers on the client side agree the list before sending it |
| Included rounds | The number covered by the quoted price, per stage |
| Fix | Something that does not match the approved brief, script or storyboard |
| Change | Something that differs from what was approved |

The consolidated rule matters most. Two people sending separate notes on different days is two rounds, and often two contradictory ones. Ask for a single named reviewer on their side who collects the notes and sends one list.

## Stage the approvals and lock as you go

Revisions are cheapest when each stage is approved before the next begins. A simple ladder for a short-form ad:

1. **Script and voice line text.** Approved in writing. Changes here cost almost nothing.
2. **Storyboard and character sheet.** Stills or rough frames for each shot, plus the reference sheet for the character. Approve the look here, not in the final cut.
3. **First cut.** Generated shots, rough voice and music, captions in place.
4. **Final.** Colour matched, mixed, exported to the agreed sizes.

Include rounds per stage, for example one round on the script, one on the storyboard and two on the cut. Then state plainly that once a stage is approved, reopening it is a change, not a revision. "Make the character older" at the storyboard stage is a quick regeneration of a still. The same note on the final cut means regenerating every shot the character appears in.

## Fix or change: decide before you quote the fix

When notes arrive, sort each one before doing any work. A fix is covered without question; you did not match the approved brief. A change is a new request, and it is either inside the included rounds or billable.

| Note | Usually | Why |
| --- | --- | --- |
| "The logo is blurry in shot 5" | Fix | Approved brief said the logo must be legible |
| "The caption has a typo" | Fix | Script was approved with the correct text |
| "Make the jacket blue instead of red" | Change | The approved sheet had red |
| "Can we try a different ending?" | Change | The storyboard was approved |
| "The voice sounds rushed on line 3" | Fix or change | Fix if timing differs from the approved script read; change if they want a new read style |

Reply to each round with the list sorted into those two columns; it shows the client what they are spending without an argument.

## A timecoded feedback sheet

"A warmer feel overall" cannot be acted on. Send the client a sheet with the first cut and ask that every note lives in a row:

| Column | Example |
| --- | --- |
| `version` | v02 |
| `timecode` | 00:07–00:09 |
| `shot` | S04 |
| `note` | Hand looks wrong when it picks up the box |
| `priority` | must / nice to have |
| `reviewer` | Client role, not a personal name, e.g. "Marketing lead" |

The priority column does more work than it seems. When a round has twelve notes and three are "must", you can deliver the three first and quote the rest. The shot column ties each note to your own [generation log](/omong-studio-journal/posts/ai-generation-log-regenerate-shots/), so you know which prompt and references to reopen.

If the client replies in prose anyway, copy their email into the sheet yourself and send it back for confirmation: "Is this the full list for round one?" That single question prevents most second waves.

## Voice and caption notes are the cheap ones

Not every note needs a new generation. Voice and caption changes are usually the fastest to turn around, so steer wording notes there. If the voiceover was made with [[tool:elevenlabs|ElevenLabs]], a changed line is a new export of one line with the same saved voice and settings, then a re-cut of that line's timing. Keep the voice name and settings with the project so a pickup line in round two sounds like the rest of the ad.

## Wording for the quote

A short paragraph in the quote saves a long email later. Something like:

> The price includes one round of revisions on the script, one on the storyboard and two on the first cut. A round is one consolidated list of notes from the nominated reviewer. Fixes to match the approved brief are always included. Changes to an approved stage, or rounds beyond those included, are quoted separately before work starts.

Then give the extra-round price as a number in the same quote, so nobody has to ask. Work out your own figure from your hourly floor and the generation cost of a typical round; the [quote sheet post](/omong-studio-journal/posts/15-second-ad-cost-quote-sheet/) shows one way to build that number.

## Version files so the past stays reachable

Clients sometimes ask to go back to an earlier version. Make that possible:

- Name every delivery with its version: `P021_ad_v03_2026-11-26.mp4`.
- Never overwrite an exported version; export a new one.
- Keep a one-line change note per version: "v03: S04 hand regenerated, caption typo fixed".

When the client prefers last week's version, you can send it in a minute.

## Tools that help with the front end

Most revision rounds start because the look was not agreed early. The [AI Short-Form Character & Motion Transfer Kit](https://lozzy36.gumroad.com/l/ai-shortform-character-kit) includes three-view character prompts and an episode storyboard sheet you can send for stage-two approval. For product spots, the [AI Product Commercial & 3D Asset Prompt Studio](https://lozzy36.gumroad.com/l/product-commercial-3d-studio) has a shot-list builder that makes the storyboard stage concrete enough for a client to sign off.

## Checklist before sending the first cut

- [ ] Quote states included rounds per stage and the extra-round price
- [ ] One nominated reviewer on the client side
- [ ] Script and storyboard approved in writing
- [ ] Timecoded feedback sheet attached to the delivery
- [ ] Version number in the file name and a change note written
- [ ] Generation log and voice settings saved with the project
