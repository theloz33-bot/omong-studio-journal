---
title: "How to Keep AI Characters Consistent Across 9:16 Short-Form Episodes (3-View Sheets & Motion Transfer)"
slug: "consistent-ai-characters-9-16-short-form"
date: "2026-11-16"
category: "Character Consistency"
excerpt: "The face starts drifting by episode three. A three-view character sheet, a frozen descriptor block, and one action per clip are what held a nine-episode vertical series together."
description: "A practical pipeline for keeping one AI character recognisable across a 9:16 episode series: three-view character sheets, locked descriptors, first-frame anchoring, and motion transfer that does not melt the face."
tags: ["AI character", "9:16", "motion transfer", "short-form series"]
tools: ["gamma", "adcreative"]
featured: true
---

An episodic vertical series has one job before it has any other: the person has to be the same person. Not similar — the same. Viewers forgive a stiff arm or a background that repeats. They do not forgive a character whose nose changes width between episode two and episode three, because the moment that happens the series stops being a story and becomes a slideshow of strangers.

This is the workflow that kept one character stable across a nine-episode run, the parts that broke, and the order I now do them in so they stop breaking.

## Why faces drift in the first place

Every generation is a fresh roll of the dice. A text prompt describes a *type* — "woman, late twenties, dark hair, soft features" — and the model fills the type with a new face each time. The prompt has no memory, so the only thing holding identity together is whatever you attach to it.

Three things make that worse in short-form:

- **The crop.** A 9:16 frame slices off shoulders and body language, which are half of what makes a person recognisable on screen.
- **Motion interpolation.** Image-to-video models generate plausible in-between frames. "Plausible" pulls toward the average face, so the longer the clip, the more your character becomes everybody.
- **Prompt edits.** Every word you change between shots is a small instruction to re-draw the face. People tighten a motion prompt and quietly rewrite the character.

Fix those three and most of the drift goes away.

## Step 1 — Make the three-view sheet before animating anything

A character sheet is three or four stills of the same person from different angles, generated once and then treated as a contract. Make it at 1:1 or 2:3, never at 9:16 — the vertical crop cuts the shoulders and the model loses the body cues it needs.

Start with one hero frame: full face, even light, neutral expression, no strong makeup, no shadows across the eyes. Then use that frame as a reference image to produce:

1. **Front view**, eyes to camera.
2. **Three-quarter view**, turned about 45 degrees.
3. **Profile**, so the nose bridge and jaw line are on record.
4. **Two detail crops**: eyes and brow, then hairline and neck. These settle arguments later.

Label the sheet and keep a palette strip beside it — three or four exact colours for skin, hair, wardrobe and background. When a shot comes back with a face that is right but a jacket that is two shades off, the palette strip tells you whether to fix the shot or accept it.

## Step 2 — Freeze the descriptor block

The sheet is the picture. The descriptor block is the sentence that travels with every prompt. Write it once, save it as a text file next to the sheet, and paste it unchanged into every shot:

```
CHARACTER: MIRA (locked — do not edit)
AGE RANGE: late 20s
FACE: round-oval, soft jaw, straight brows, wide-set eyes
HAIR: dark brown, blunt shoulder-length cut, side part left
SKIN: warm mid tone, matte, no freckles
WARDROBE: charcoal overshirt, cream tee, thin silver chain
LIGHT: soft window light from camera left, low contrast
```

Two rules keep this block useful. First, it never changes mid-season — not for a better adjective, not for a mood. Mood goes in the shot description, not in the character. Second, it says what is *absent* as well as what is present. "No freckles, no beard shadow, no earrings" is worth as much as any positive detail, because models add texture when they are unsure.

If you storyboard for clients or collaborators, [[tool:gamma|Gamma]] will turn the shot list and the sheet into a deck you can show without opening a slide app, which matters more than it sounds when someone else has to approve a look.

## Step 3 — One action per clip, and describe the camera separately

Motion transfer fails when the prompt asks for two things at once. "She turns, smiles, and walks toward the window" is three actions in five seconds, and the model resolves the conflict by generating a new person halfway through.

Write motion prompts in three blocks and keep them short:

- **Subject:** the descriptor block, trimmed to face and wardrobe.
- **Action:** one verb. *Lifts the cup. Turns her head. Steps back.*
- **Camera:** separate sentence. *Slow push in. Static. Slight handheld drift.*

Four to six seconds per clip is the sweet spot for vertical. Longer clips drift more, and you rarely need more than six seconds for one beat in a short.

## Step 4 — Anchor every shot to an approved still

Generate the first frame first, as an image. Approve it. Then animate from that frame. If the still is wrong, regenerate the still — not the video clip. Re-rolling video to fix a face is how a project burns a day.

| Stage | What you produce | What must be locked | How it usually fails |
| --- | --- | --- | --- |
| Sheet | 3 views + 2 detail crops | Face, hair length, wardrobe | Views generated in different lighting |
| Descriptor | One text block | Never edited mid-season | "Improving" wording between shots |
| Keyframe | One approved still per shot | Composition, eyeline, costume | Approving a still that needs a fix later |
| Motion | 4–6 s clip per still | One action, separate camera note | Two verbs in one prompt |
| Assembly | Cut, captions, sound | Safe areas, subtitle band | Face pushed under platform UI |

## Step 5 — Compose for 9:16 from the beginning

A vertical frame is unforgiving. Keep the face in the upper third, leave the bottom fifth for captions and the platform's own interface, and resist the urge to fill the frame with the character. The tighter the crop, the less the model has to anchor identity to, and the more the viewer notices drift.

Generate at full vertical resolution rather than cropping a landscape image. A centre-cropped landscape frame loses the shoulders, crops the hands at the wrist, and leaves you with a face floating in a slot.

## Step 6 — Reuse the sheet instead of remaking it

Keep one folder per character:

```
mira/
  sheet_v01.png
  descriptor.txt
  palette.png
  episode_01/  episode_02/  ...
```

When episode four needs a new angle, generate it *from* the sheet, approve it, and add it to the folder as `sheet_v02.png` with a note on what changed. Do not regenerate the whole sheet because one shot came out odd. A sheet that is regenerated every episode is not a contract, it is a new character each time — and that is exactly the drift you were trying to prevent.

## The episode loop

The order that finally stopped costing me reshoots:

1. Eight to twelve beats, written as sentences.
2. A shot list of twelve to eighteen shots, each mapped to one beat.
3. One approved still per shot — batch them, but approve before animating.
4. Four to six second clips, one action each.
5. Assembly with captions, then a pass at full size on a phone screen, not a monitor.

If the stills are approved, the clips almost always behave. If a clip misbehaves, the fault is usually in the still or in a motion prompt that grew a second verb.

## Checklist before you render episode one

- [ ] Three-view sheet exists at 1:1 or 2:3, labelled, with a palette strip
- [ ] Descriptor block saved as a file, pasted unedited into every prompt
- [ ] Two detail crops approved (eyes, hairline)
- [ ] Motion prompt template split into subject / action / camera
- [ ] Every shot has an approved first frame before video generation
- [ ] Face sits in the upper third; bottom fifth clear for captions
- [ ] Character folder holds sheet, descriptor, palette and episode subfolders

One more thing worth writing down: the sheet is also the cheapest piece of marketing you will make. When a character holds together across nine episodes, the same sheet drives thumbnail variants and ad creatives without a new shoot — which is why a folder of approved angles is worth more than another prompt revision.
