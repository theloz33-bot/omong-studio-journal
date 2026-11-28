---
title: "The Brief Before the First Generation: A One-Page Intake for AI Video Jobs"
slug: "ai-video-client-brief-intake"
date: "2026-11-28"
category: "Short-Form Production"
excerpt: "Most wasted generations on an AI video job trace back to a question nobody asked before the first prompt. A one-page intake covering purpose, platform and format, must-show items, voice and music, references and approvals turns a loose request into something you can quote, prompt and deliver."
description: "A one-page client brief for AI video jobs: the questions to ask before generating, how to turn answers into a shot list and prompts, and what to confirm in writing."
summary: "Before the first generation, get one page of written answers on purpose, platform and format, what must appear on screen, voice and music, references, deadline and who approves, then turn that page into a shot list and confirm it with the client."
tags: ["client brief", "AI video", "pre-production", "freelance", "short-form ads", "workflow"]
tools: ["elevenlabs", "gamma"]
featured: false
---

The request arrives as one line: "A short video for our new product, something fun, for social." You generate a dozen takes, send three, and the reply says the product should have been in the first second, the video was meant for a horizontal screen in a shop window, and the voice should be a woman's, not a man's. None of that was hard to know. Nobody asked.

On an AI video job, every unasked question is paid for in generations. A traditional shoot has a pre-production meeting because the camera day is expensive; with generated footage the expensive part is spread out over dozens of small attempts, so it is easy to skip the meeting and start prompting. This post is the one-page intake that replaces that meeting, and how its answers turn into a shot list and prompts.

## Why the brief matters more with AI footage

Three things make a weak brief costlier here than on a normal edit:

- **Format decisions are baked in at generation.** A take generated in 9:16 cannot become a clean 16:9 master later without regenerating or heavy cropping.
- **Consistency depends on references.** A character, a product or a colour that has to match across shots needs reference material before the first prompt, not after the third round.
- **Every vague note becomes a new batch.** As the [revision rounds post](/omong-studio-journal/posts/ai-video-revision-rounds-feedback/) explains, a round of feedback on generated footage often means regenerating, not trimming.

A brief does not need to be long. It needs to be written down, answered by the client, and kept in the job folder.

## The one-page intake

Send the same questions every time, as a short form or a plain document. Keep it to one page so it actually gets filled in.

| Section | Questions to ask |
| --- | --- |
| Purpose | What should a viewer do or remember after watching? Who is the viewer? |
| Platform and format | Where will it run? Vertical, horizontal or square? How long? Sound on or off by default? |
| Must show | Which product, logo, text, price or offer has to appear, and by which second? |
| Must avoid | Anything off-brand, competitor references, claims that legal will not allow |
| Voice and words | Is there a voiceover? What language? Any fixed lines or slogans? Captions burned in or separate? |
| Music | Mood, tempo, any track they already own or want to avoid |
| References | Product photos, brand colours, fonts, past videos they liked and why |
| Delivery | Deadline, file formats, sizes, a clean version without captions? |
| Approvals | Who signs off, and is that person the one filling in the form? |

The last row is the one most often skipped. If the person writing the brief is not the person who approves the cut, the brief can be perfect and still be overruled at the end.

### Questions that save the most generations

From the table, four answers change the work more than the rest:

1. **The format and length.** These decide the generation settings for every shot.
2. **What must appear, and when.** A product that has to be visible in the opening seconds shapes the first shot, not a later one.
3. **Whether captions are burned in.** If the client may want other languages later, keep captions off the master, as covered in the [localisation post](/omong-studio-journal/posts/localise-vertical-ad-captions-voiceover/).
4. **Who approves.** Ask for one name, so feedback arrives from one place.

## From answers to a shot list

Once the form comes back, turn it into a shot list before you open any generation tool. Each row gets a shot number, a duration, what is on screen, the line of voiceover or caption under it, and the reference it depends on.

- Write the must-show items into the shots where they appear, so nothing is left to "somewhere in the middle".
- Mark which shots need a fixed character or product reference, and gather those files first.
- Note the generation format at the top of the sheet, so every prompt starts from the same settings.

For product spots, the [AI Product Commercial & 3D Asset Prompt Studio](https://lozzy36.gumroad.com/l/product-commercial-3d-studio) includes a 15/30/45-second shot-list builder you can fill straight from the intake answers. For music videos, the [Cinematic AI MV & Suno v6 Prompt Vault](https://lozzy36.gumroad.com/l/ai-mv-suno-prompt-vault) organises its shot prompts by section of a song, which maps neatly onto a brief that names the song's structure.

The shot numbers from this sheet become the `S03` in the file names described in the [project folder post](/omong-studio-journal/posts/ai-video-project-folder-backup-archive/), and the rows in your [generation log](/omong-studio-journal/posts/ai-generation-log-regenerate-shots/).

## Voice and script before pictures

If the job has a voiceover, lock the script before generating footage. The length of each spoken line sets how long each shot needs to be, and changing words later changes timing. Draft the lines, read them aloud against the planned durations, and send the script with the shot list.

When the voice is made with [[tool:elevenlabs|ElevenLabs]], render a short sample of the chosen voice reading one real line from the script and send it with the confirmation. A thirty-word sample settles "a warm voice" far better than a description does, and it is far cheaper than discovering the mismatch after the edit.

## Show the plan back to the client

The confirmation step is where the brief turns into an agreement. Send back:

- The shot list with durations and on-screen text
- The script and the voice sample
- Two or three reference frames or style stills, if the look is not already fixed
- The format, length and delivery list
- The revision scope from your quote

Some clients read a table; others only react to something that looks like a presentation. If you need the second kind, [[tool:gamma|Gamma]] can turn the shot list and references into a short deck without building slides by hand.

Ask for a written reply that says the plan is approved, or what to change. Changes at this stage cost an edit to a document, not a new batch of footage.

## What should an AI video brief include?

The purpose and viewer, the platform, format and length, what must appear and when, what to avoid, voice and caption details, music, references, delivery files and the name of the person who approves.

## When should the client approve the plan?

Before the first generation: after the shot list, script and voice sample are sent, and before any footage is made.

## When the client will not fill in a form

Some clients prefer a call. That is fine: run the call with the same questions in front of you, then write the answers into the one-page form yourself and send it back for a yes. The brief still exists in writing, and the job folder still starts with it.

## Checklist before the first prompt

- [ ] Intake answered in writing and saved in `00_brief`
- [ ] Format, length and generation settings noted on the shot list
- [ ] Must-show items placed in specific shots
- [ ] References for characters, products and colours collected
- [ ] Script locked and voice sample sent
- [ ] Plan approved in writing by the person who signs off

The intake takes a short conversation and one page. What it buys is a first cut that answers the question the client actually had, rather than the one you guessed.
