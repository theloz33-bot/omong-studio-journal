---
title: "Regenerating an AI Shot Six Months Later: A Generation Log, a Naming Rule and What to Record"
slug: "ai-generation-log-regenerate-shots"
date: "2026-11-25"
category: "Short-Form Production"
excerpt: "A client asks for the same shot with a different product colour, and nobody knows which prompt, model or reference made it. A one-row-per-take generation log and a file name that points back to it turn that from a guessing game into a ten-minute job."
description: "How to log AI image and video generations so any shot can be found and redone later: a naming rule, the columns that matter, reference folders, voice settings and an archive routine."
tags: ["prompt log", "file naming", "AI video", "asset management", "reproducibility", "workflow"]
tools: ["elevenlabs"]
featured: false
---

The ad shipped in spring. In autumn the client comes back: same shot, same character, but the jacket is now green. You open the project folder and find `final_v3_REAL.mp4`, `final_v3_REAL2.mp4` and forty clips named by the generator's random string. The prompt is somewhere in a browser history that no longer exists. The reference image was a screenshot on a phone.

The shot was not hard to make. It is hard to make *again*, because nothing connected the file to the decisions behind it. This post is the small system that fixes that: a naming rule, a generation log with one row per take, and a short archive routine at the end of each job.

## What "the same shot" actually depends on

A generated shot is the output of more inputs than the prompt. If any of these is missing, you are not regenerating; you are starting over with a hint.

| Input | Why it matters later |
| --- | --- |
| Tool and model name, with version if shown | Hosted models are updated; the same prompt on a newer version can look different |
| Full prompt and negative prompt | Paraphrased prompts drift; copy the exact text |
| Reference images | Character sheets, product shots and style frames often carry more of the look than the words do |
| Settings | Aspect ratio, duration, resolution, motion strength, guidance, anything the interface exposed |
| Seed, if the tool shows one | Fixes one source of randomness; it does not guarantee an identical result |
| The take you kept, and why | Out of eight takes, the reason you picked take five is the brief for the next round |

Be honest about the seed. On many tools the same seed, prompt and settings land close to the earlier result, but a model update, a different queue or a changed default can still move it. The log is not a promise of pixel-perfect repeats. It is the shortest path back to a shot that matches.

## A naming rule that points back to the log

The file name has one job: let you find the log row in one search. Everything else lives in the log.

```
2026-11-25_P014_S03_T05_char-walk.mp4
```

| Part | Meaning |
| --- | --- |
| `2026-11-25` | Generation date, year first, so files sort in time order |
| `P014` | Project number |
| `S03` | Shot number from the storyboard |
| `T05` | Take number for that shot |
| `char-walk` | Two or three words a human can read |

Rules that keep it working:

- **Year-month-day, always.** `25-11-26` and `11/25` sort wrongly and mean different things in different countries.
- **Zero-padded numbers.** `S03` sorts before `S10`; `S3` does not.
- **No spaces, no "final".** A file called final is never the last one.
- **Rename on download.** The generator's random string goes into the log as a column, not into your folder.

## The generation log

One row per take, including the takes you rejected. A spreadsheet is enough; a CSV next to the project is better, because it travels with the folder.

| Column | Example |
| --- | --- |
| `file` | `2026-11-25_P014_S03_T05_char-walk.mp4` |
| `tool` / `model` | Video generator name, model label as shown in the interface |
| `mode` | text-to-video / image-to-video / edit |
| `prompt` | Exact text, pasted |
| `negative` | Exact text, or blank |
| `refs` | `refs/char_front.png; refs/jacket_red.png` |
| `settings` | `9:16, 5 s, 1080p, motion 0.6` |
| `seed` | Number, or `n/a` |
| `source_id` | The generator's own job or file ID, if it has one |
| `status` | keep / reject / alt |
| `note` | "hands fine, background warps at 3 s" |

Two habits make the log useful instead of decorative.

First, **write the row at generation time, not afterwards.** Reconstructing prompts at the end of a job means copying the last version of each prompt, which is rarely the one that produced the kept take.

Second, **log rejections with a reason.** "Face drifts after 2 s" on four rejected takes tells you that the problem is the reference, not the wording. That note saves more credits on the next job than any prompt trick.

## Keep references as files, not links

References are the part most often lost. A link to a chat, a gallery page or a shared drive folder may not open in six months; a file in the project does.

```
P014_client-jacket/
  refs/
    char_front.png
    char_side.png
    jacket_red.png
    style_frame_01.png
  gen/
  edit/
  delivery/
  log.csv
```

Name reference files by role, not by source. `char_front.png` will still make sense next year; `IMG_4471.png` will not. When a character sheet changes, save a new file (`char_front_v2.png`) and log which takes used which version. A series that switches sheets mid-season without a record is where consistency quietly breaks.

## Voice and audio belong in the same log

Short-form ads usually carry a voice line, and voiceover drifts for the same reasons pictures do. Log the voice name, the model, the stability and similarity settings, and the exact line text, one row per exported line. With [[tool:elevenlabs|ElevenLabs]] a saved voice keeps the narrator consistent across jobs, but the settings you used on the day still need writing down, because a changed slider changes the read.

For music beds, log the generator, the prompt and the version you mixed, and keep the stems in the project rather than only the bounce. A pickup edit with the bed at a new length is quick with stems and slow without them.

## The end-of-job archive routine

Fifteen minutes when a job is delivered, before the folder is forgotten:

1. Delete nothing yet. Mark every take in the log as keep, reject or alt.
2. Move rejected clips into `gen/_rejected/`. Keep them until the client has signed off; then decide by storage cost, not by mood.
3. Check that every `keep` row has its prompt, references and settings filled in.
4. Export the log as CSV into the project root, even if you also keep a spreadsheet online.
5. Copy the whole project folder to a second drive or storage location.
6. Write one line in a studio-wide index: project number, client label, date, what was made.

The index line is what lets you find `P014` when the client writes "the jacket ad from spring" and nothing more.

## Regenerating, step by step

When the request comes back:

1. Find the project in the index, then the shot in `log.csv`.
2. Open the kept take and its reference files side by side.
3. Check whether the tool still offers the same model. If not, note the new model in a new row; expect a match, not a copy.
4. Change one thing only: the jacket reference, or the one line of prompt that mentions colour.
5. Generate a small batch, log every take, and compare against the old keep on the same screen.

If the old keep and the new take sit in the same cut, colour-match them before delivery rather than hoping the generator did it.

## Starting points

The [AI Short-Form Character & Motion Transfer Kit](https://lozzy36.gumroad.com/l/ai-shortform-character-kit) includes three-view character prompts and an episode storyboard sheet that map directly onto the `S` and `refs` columns above. For music-video work, the [Cinematic AI MV & Suno v6 Prompt Vault](https://lozzy36.gumroad.com/l/ai-mv-suno-prompt-vault) organises prompts by shot type, which makes a prompt column easier to fill with text you can reuse.

## Checklist before closing a job

- [ ] Every delivered shot has a log row marked keep
- [ ] Prompts are pasted, not paraphrased
- [ ] Reference images saved as files inside the project
- [ ] Model name and settings recorded for each keep
- [ ] Voice settings and line text logged per exported line
- [ ] Log exported as CSV into the project root
- [ ] Project copied to a second location
- [ ] One line added to the studio index

A generation log costs a minute per take. It is the difference between telling a client "we can do that this afternoon" and quoting the shot again from scratch.
