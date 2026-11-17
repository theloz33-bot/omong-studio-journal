---
title: "Packaging a Digital Kit for Gumroad: File Structure, a Price Ladder and Delivery That Refunds Itself"
slug: "gumroad-digital-kit-packaging"
date: "2026-11-18"
category: "Product"
excerpt: "A prompt pack is not a product until a stranger can open the ZIP and know what to do in ninety seconds. The structure, the price steps and the listing copy that does the selling."
description: "How to package and price a digital kit for Gumroad: the ZIP layout that removes support questions, a three-step price ladder with real numbers, listing copy that states what is inside, and a delivery standard that prevents most refunds."
tags: ["Gumroad", "digital products", "packaging", "pricing", "prompt packs"]
tools: ["gamma"]
featured: false
---

A digital kit is bought in about eight seconds and judged in about ninety. In those ninety seconds the buyer opens a ZIP, works out whether the file names make sense, and decides whether they got what the preview promised. Everything that happens after that is either the product working or a support conversation.

The packaging decisions below come from shipping prompt packs and templates to a shop that sells them for $12 to $19. None of them are about marketing. They are about removing the reasons a buyer feels unsure after paying.

## What the buyer is actually paying for

Not information. Almost everything in a prompt pack is discoverable for free, scattered across videos and threads, in a form that took weeks to assemble. What a buyer pays for is a decision already made: this prompt, in this order, for this shot, at this aspect ratio, with the part that failed removed.

That definition sets the packaging. A pack that is a list of prompts is a folder of text. A pack that is a list of prompts plus the sheet that shows which ones to use first, in what order, on what kind of footage, is a tool. The difference costs an afternoon and shows up in the refund rate, not the conversion rate.

## The ZIP layout that removes support questions

Keep one archive, one top folder, no nested archives, and a numbered order that matches the order of use.

```
kit-name-v1.2/
  README.pdf            what this is, what to do first, version and date
  01_start-here.md      the 15-minute path for someone who opens it and freezes
  02_prompts/           01_character.md, 02_shots.md, 03_audio.md
  03_templates/         storyboard.xlsx, shot-budget.csv
  04_examples/          before/after frames, one per technique
  LICENSE.txt           what the buyer may do with the output
```

Three rules do most of the work:

- **Number the folders.** The number is the instruction. A buyer who does not read the README still follows 01 → 02 → 03.
- **Name files after the action, not the topic.** `02_shots.md` beats `notes_final2.md`, and `03_audio.md` beats `audio (copy).md`.
- **No nested ZIPs.** Every extra unpack is a place where someone stops, and a stopped buyer writes an email.

A single README.pdf is worth the ten minutes it takes. It should answer four questions in one page: what this is, what to open first, what tool version it was tested on, and how to get an update.

## The price ladder, with real numbers

Price follows what the buyer has to do with the kit, not how long it took to make. A useful ladder has three rungs, and the middle one is where most sales land.

| Rung | Price | What is inside | Who it is for |
| --- | --- | --- | --- |
| Entry | $9–12 | Prompts plus one template | Someone testing whether the workflow fits |
| Core | $15–19 | Prompts, 2–3 templates, examples, README | The buyer who wants to finish a project this week |
| Studio | $29–39 | Core plus a fill-in plan, a review checklist and update access | Someone selling the output to a client |

Two observations from running this ladder. First, $12 and $15 do not behave differently; the jump that changes behaviour is the one from "text" to "text plus a working file". Second, a $29 tier only sells when it contains something that saves an hour — a plan, a checklist, a sheet that calculates. Bundling two more prompt lists into it does nothing.

Avoid the discount reflex on the way in. A launch price that undercuts the ladder teaches the first buyers that the real price is lower, and it is difficult to raise afterwards. If a launch offer is needed, make it time-bound and say so in the listing.

## Listing copy that does the selling

The product page has one job: let the buyer confirm that what they guessed from the title is what is inside. Four blocks, in this order.

1. **A title with the outcome and the tool.** "Cinematic AI MV Prompt Vault — 60 shot prompts for Suno and image-to-video" tells the buyer the format, the count and the tools. "The Ultimate AI Bundle" tells them nothing and reads like a course.
2. **The first 120 characters as the promise.** Search results and previews truncate there. If the promise is in the third paragraph, most people never read it.
3. **What is included, as a list with counts.** "62 prompts split by shot type · 1 storyboard sheet · voiceover timing sheet · 8 before/after frames". Counts are checkable, and checkable claims reduce hesitation.
4. **What it does not do.** One honest line — "no footage is included; you bring your own model access" — prevents the most common refund reason before it exists.

Three screenshots beat ten. One of the inside of a real file, one of the output it produces, one of the table of contents. A buyer who has seen the actual file structure has already done the unpacking in their head.

## Delivery that prevents most refunds

Refunds happen for three reasons: the file did not arrive, the contents did not match the preview, or the buyer could not use it with the tool they already pay for. Each has a packaging answer.

- **Delivery:** state the format in the listing (PDF, Markdown, XLSX, MP4) and the file size. A 300 MB "template" on a phone is a refund, not a download.
- **Match:** put the table of contents in the preview, and keep the listing copy generated from the same source as the README so the two cannot drift.
- **Tool compatibility:** name the version tested, and what happens on other versions. "Tested in Runway Gen-3, prompts are model-agnostic" is a sentence that saves an argument.

Gumroad handles receipts, taxes and the refund mechanics; none of that is yours to build. What is yours is the version number in the folder name, because it is the only way to answer "did I buy the version with the audio sheet" a month later.

## A QA pass before it goes live

- [ ] ZIP opens to one top-level folder, no nested archives
- [ ] Folders numbered in the order of use; file names describe an action
- [ ] README.pdf answers: what, first step, tested version, updates
- [ ] Listing copy matches the README line for line
- [ ] Table of contents included in the preview images
- [ ] Price sits on the ladder, and the tier above it contains an hour-saving artifact
- [ ] Version number in the folder name and the listing
- [ ] Licence states what the buyer may sell, and what they may not resell

A kit sold this way does not need a bigger audience to do better. It needs the buyer's ninety seconds after checkout to go the way the preview promised, and that is a design problem, not a marketing one.
