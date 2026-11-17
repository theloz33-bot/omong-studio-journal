---
title: "Thirty Vertical Videos a Month From One Spreadsheet: a Batch Pipeline That Survives Week Three"
slug: "batch-vertical-video-pipeline"
date: "2026-11-18"
category: "Automation"
excerpt: "Daily uploads do not fail on day one. They fail on day nineteen, when the script, the voice file and the shot folder stop matching. One spreadsheet column fixes that."
description: "A batch production system for vertical video: the spreadsheet schema that acts as the source of truth, the folder contract, a weekly rhythm that batches by stage instead of by video, and the four failure modes that appear around week three."
tags: ["batch production", "pipeline", "spreadsheet", "AI video", "workflow"]
tools: ["browseai"]
featured: false
---

Anyone can produce three vertical videos in a burst. Thirty a month is a different problem: the work arrives faster than the decisions that make it consistent, and the thing that breaks is never the renderer. It is the file name.

Three weeks in, the script in the document says one hook, the voice file says another, the shot folder is numbered differently from both, and nobody can tell which caption file belongs to which cut. That is not a discipline failure. It is the predictable result of keeping the source of truth in four places at once.

## One row per video, one sheet per month

The system that holds up is unglamorous: a spreadsheet where one row is one video and every downstream file is addressed from that row. Not a content calendar, not a Kanban board with twenty cards — a table with a fixed column contract.

| Column | Holds | Contract |
| --- | --- | --- |
| `id` | `2026-11-18-a` | Never changes after creation; every file name starts with it |
| `slug` | `hook-frame-test` | Readable, lowercase, no spaces |
| `hook` | The first spoken line | Six words or fewer |
| `promise` | What the viewer gets | One sentence, written before the script |
| `script` | Link to the script file | Lives in the row's folder, not in the sheet |
| `vo` | `done` or blank | Only flips when the WAV is exported and measured |
| `shots` | Count of approved clips | A number, not "in progress" |
| `captions` | `auto` / `fixed` / blank | Blank means not checked by a human |
| `status` | `script` → `vo` → `shots` → `assembly` → `qa` → `published` | Exactly one value, never two |
| `blocked` | One short reason, or blank | Anything in this column is not being worked on |
| `keep` | `keep` / `cut` / `redo` | Written after publishing, before the next batch |

The `blocked` column is the one people skip, and it is the one that keeps a batch honest. A row that is stuck for four days has a name for why: missing voice speed, a prompt that produces melted hands, a client note pending. A row with no reason and no progress is an invisible cost, and there are usually six of them by week three.

## The folder contract

Every row gets a folder named from `id` and `slug`, with the same four subfolders in the same order:

```
2026-11-18-a_hook-frame-test/
  01_script.md        final script, dated in the file header
  02_vo/              master.wav, plus per-line exports if the workflow needs them
  03_shots/           approved clips only, named s001, s002, …
  04_edit/            project file, caption .srt, export
```

Two rules make this survive contact with reality. Rejected clips live in `03_shots/_rejected/` rather than being deleted, because the fourth-best take is often the one that gets used after a re-script. And nothing is renamed once it is exported — a version change becomes `_v2`, not a new name.

The point of the contract is that any question about any video is answerable with one path. That is what has to be true at video twenty-six, when the reference video from week one is the only record of how the hook was phrased.

## Batch by stage, not by video

The instinct is to finish one video, then the next. That switches the brain between writing, listening, prompting and cutting every 40 minutes, and each switch has a warm-up cost that lands on a different kind of decision each time.

Batching by stage keeps one mode of attention for a whole block:

| Day | Stage | What happens | Typical block |
| --- | --- | --- | --- |
| Monday | Script | Write seven scripts against the month's promise list; no rendering | 3 h |
| Tuesday | Voice | Generate and measure every WAV for the week; lock speed and voice | 2 h |
| Wednesday | Shots | Prompt, review and approve clips for three videos | 4 h |
| Thursday | Assembly | Cut three videos back to back with the same caption and export settings | 4 h |
| Friday | QA and publish | Watch finished cuts, fix captions, schedule | 2 h |

The gain is not speed on any single step. It is that every video in a batch gets the same voice, the same caption preset and the same loudness target, because those decisions are made once per block instead of once per video. A month produced this way sounds like one channel; a month produced one video at a time sounds like four nervous weeks.

## Automate the plumbing, not the edit

The steps worth scripting are the ones with no judgement in them: creating the folder tree from a row, renaming the exported voice files to the id, splitting a script into caption lines at the punctuation, generating a contact sheet of approved clips, and writing the status back to the sheet. Each of those takes an afternoon once and saves minutes on every video, which is the only arithmetic that matters at thirty a month.

The steps not worth automating are caption timing, hook wording and the choice of which take is good. Every attempt to automate those produces output that needs to be reviewed more carefully than it would have taken to do, and the review is the expensive part.

## The four failures that show up around week three

1. **Drift across the batch.** The character's jaw or wardrobe changes between video 12 and video 18 because the descriptor block was edited in one script. Fix: the descriptor lives in one file, copied into each script by the folder script, never retyped.
2. **Loudness creep.** Each voice export is normalised to its own peak, so episode 20 is 3 dB louder than episode 2. Fix: one target per destination, measured on the export, logged in a column next to `vo`.
3. **Caption overflow.** A four-word line becomes six after a re-script, and now runs into the platform's UI. Fix: a caption length check in QA, before scheduling, not after publishing.
4. **Stale status.** A row says `shots` while the cut is already published, so the next batch re-uses the slot. Fix: status is written by the person who did the work, in the same minute, not at the end of the week.

Every one of them is a data problem, and every one of them is caught by a single column that is actually maintained.

## The monthly review that keeps it alive

Once a month, before writing the next batch, read the `keep` column. Three questions, in order: which hooks held past two seconds, which format took under an hour to assemble, and which rows were blocked most often.

Rows that took more than two hours of attention and did not hold get cut from the format list, not improved. Rows that held and assembled fast get three variations in the next batch. That is the whole planning process — there is no separate strategy document, because the sheet already holds the evidence.

A batch pipeline is not a way to make more videos for the same effort. It is a way to make the same video thirty times without the quality drifting, which is what a series actually is.

## Before the first batch

- [ ] One row per video, with `id`, `slug`, `hook`, `promise` filled before any work starts
- [ ] Folder tree generated from the row, not typed by hand
- [ ] Descriptor block in one file, included by every script
- [ ] One loudness target per destination, measured on the export
- [ ] `status` written in the same minute the stage finishes
- [ ] `blocked` used every single time something waits
- [ ] Monthly review reads the `keep` column before planning
