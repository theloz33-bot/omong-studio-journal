---
title: "One Folder per Job: Project Structure, Backups and a Handover Archive for AI Video Work"
slug: "ai-video-project-folder-backup-archive"
date: "2026-11-27"
category: "Short-Form Production"
excerpt: "AI video jobs scatter files across generation sites, download folders and editors. One fixed folder per job, a naming rule, a backup routine with an off-site copy and a closing archive keep every shot, voice line and delivery findable long after the invoice is paid."
description: "How to organise AI video projects: a fixed folder structure per job, file naming, what to keep from generation sites, a 3-2-1 style backup routine and a handover archive when the job closes."
summary: "Give every AI video job one fixed folder with the same subfolders, name files by project, shot and version, keep at least one copy off the working machine, and close each job with a small archive that holds the brief, the generation log, the voice settings and the final exports."
tags: ["project management", "backups", "AI video", "file naming", "freelance", "archiving"]
tools: ["elevenlabs"]
featured: false
---

A client writes back four months after delivery: "Can we get the version without the price caption?" The ad is somewhere. The generated shots are in a downloads folder, the voice lines are in another app, the edit project points at files that were moved, and the export with captions is the only one you can find.

AI production makes this worse than ordinary video work because the raw material comes from many places: generation sites, a voice tool, a music tool, reference images, your editor. Each one has its own download folder and its own idea of a file name. This post is the folder structure, naming rule, backup routine and closing archive that keep one job in one place.

## Why AI jobs scatter

Three habits cause most of the mess:

- **Downloads land wherever the browser puts them.** A day of generating leaves dozens of files with machine-made names in one shared folder, mixed with every other job.
- **The generation site is treated as storage.** Histories on hosted tools can be trimmed, reorganised or tied to a plan you later cancel. If a take matters, it needs to live on your own disk.
- **The editor references files instead of holding them.** Move or rename a source file and the timeline shows media offline.

The fix is not a clever tool. It is the same folder every time, created before the first generation.

## A fixed folder for every job

Create the folder from a template, not by hand, so the structure never drifts. One layout that works for short-form ads and music-video shots:

| Folder | What goes in it |
| --- | --- |
| `00_brief` | Brief, approved script, quote, feedback sheets |
| `01_refs` | Character sheets, product photos, style frames, mood references |
| `02_gen` | Generated stills and video takes, one subfolder per shot |
| `03_audio` | Voice lines, music bed, stems, sound effects |
| `04_edit` | Editor project files and autosaves |
| `05_exports` | Every delivered version, never overwritten |
| `99_archive` | The closing archive, made at the end of the job |

Numbered prefixes keep the order stable in any file browser. Keep the template folder somewhere obvious and copy it at the start of each job with the project code in the name, for example `P024_snack-brand-ad`.

## A naming rule you can follow at speed

Rename files as they come in, not at the end of the job, when nobody remembers which take was which. A pattern that sorts well:

`P024_S03_t02_v01.mp4`

- `P024` is the project code.
- `S03` is the shot number from the storyboard.
- `t02` is the take, meaning the second generation for that shot.
- `v01` is the version, which only changes when a kept take is edited or regenerated after feedback.

Exports get a date as well: `P024_ad_9x16_v03_2026-11-27.mp4`. The same codes go into your [generation log](/omong-studio-journal/posts/ai-generation-log-regenerate-shots/), so the file name points straight at the row that holds the prompt, seed and references.

### What to keep from the generation site

Not every take deserves disk space, but deleting too early is the more common regret. A workable rule:

- Keep every take that reached review, even the rejected ones, until the job closes.
- Keep the prompt and settings for every kept take in the log, not only on the site.
- Download the highest quality the site offers for kept takes; a preview file is not a master.

## Voice and music belong in the job folder

Voice lines are easy to lose because they are small and quick to regenerate. Regenerating is exactly what you want to avoid in a pickup session, though, because a new render can differ in pacing. If the voiceover is made with [[tool:elevenlabs|ElevenLabs]], save each line as its own file named by shot and line number, and write the voice name and settings into a text file in `03_audio`. When the client asks for one changed word, you export one line with the same settings instead of re-recording the whole script.

Music works the same way: keep the bed, any stems you split, and a note of where the track came from and what licence or plan it was made under.

## A backup routine you will actually run

The well-known 3-2-1 rule is a good shape for this: three copies of the data, on two different kinds of storage, with one copy somewhere other than your desk. For a solo studio, that can be as plain as:

1. **Working copy** on the machine you edit on.
2. **Local backup** on an external drive, updated at the end of each working day.
3. **Off-site copy** in cloud storage or a drive kept at another address, updated at least when a version goes to the client.

Two habits make the routine survive a busy week:

- **Back up before delivery, not after.** The moment a version is exported and sent is the moment it becomes something you may be asked to reproduce.
- **Test a restore once in a while.** Open a backed-up project on another machine and see whether the edit relinks. A backup you have never opened is a guess.

## The closing archive

When the final invoice is paid, spend a short session closing the job:

- [ ] Copy the brief, approved script and final feedback sheet into `99_archive`
- [ ] Export the generation log for this project as a file
- [ ] Save the voice settings note and music source note
- [ ] Keep the final exports in every delivered size, plus a clean version without captions if one exists
- [ ] Use the editor's collect or consolidate feature so the project holds copies of the media it uses
- [ ] Delete rejected takes that never reached review, if disk space matters
- [ ] Copy the finished archive to the off-site location and note the date in your job list

The clean version without captions is the one clients ask for most often later, for a new language or a new price. The [localisation post](/omong-studio-journal/posts/localise-vertical-ad-captions-voiceover/) explains why keeping captions off the master saves a re-cut.

## Kits that slot into the structure

Templates make the folder routine faster. The [AI Short-Form Character & Motion Transfer Kit](https://lozzy36.gumroad.com/l/ai-shortform-character-kit) includes three-view character prompts and an episode storyboard sheet, which become the first files in `01_refs` and give you the shot numbers for the naming rule. For product spots, the [AI Product Commercial & 3D Asset Prompt Studio](https://lozzy36.gumroad.com/l/product-commercial-3d-studio) has a shot-list builder whose shot numbers can carry straight into `02_gen`.

## Where should AI-generated takes be stored?

On your own disk, inside the job folder, with the prompt and settings recorded in a log. The generation site's history is a convenience, not storage you control.

## What should a handover archive contain?

The brief and approved script, the final feedback sheet, the generation log, the voice and music notes, the final exports in every delivered size, a clean version without captions if one exists, and an editor project that holds its own media.

## What the folder buys you

The structure costs a few minutes at the start of a job and a short session at the end. In return, a request months later becomes a search for one project code instead of an afternoon of digging, and a lost laptop becomes an inconvenience rather than a lost client.
