---
title: "Activation in Seven Days: The One Event, the Funnel Maths and the Churn Interview"
slug: "saas-first-seven-days-activation"
date: "2026-11-23"
category: "Product"
excerpt: "Sign-ups arrive every day and the product is empty by week three. The fix is not a longer tour: it is one activation event, a median time to value, four emails with one action each — and the maths that says how many paying customers that is worth."
description: "How to design the first seven days of a SaaS product: choosing the one activation event, the funnel arithmetic, median time to value, a 100-point health score, churn interview questions and the test sample size."
tags: ["activation", "onboarding", "SaaS", "retention", "churn", "cohort analysis"]
tools: ["elevenlabs"]
featured: false
---

A small product can collect sign-ups every day and still be empty by the third week. Nothing broke: people arrived, looked, and left before the product did the one thing they came for. The first seven days are where that is decided, and the number that decides it is not sign-ups but how many people did the thing the product exists to do, and how quickly.

Everything else in an onboarding — the tour, the checklist, the emails — either moves that number or spends the new user's patience.

## Activation is an event, not a sign-up

Activation is the earliest action that separates the people still there in a month from the people who are not. It is a claim to check against a past cohort: split last quarter's sign-ups by whether they did X within seven days, then compare day-30 retention.

| Candidate event | What it actually measures | Verdict |
| --- | --- | --- |
| Account created | Intent, and nothing else | Every product already counts it |
| Profile completed | Willingness to fill a form | Effort, not value |
| Data imported | That the product now holds their work | Strong, when import is the job |
| First invoice sent | That money is already flowing through it | The strongest kind: an outcome |
| Invited a teammate | Virality | Often a proxy for a real first use |

If the two groups retain the same, the event is a step, not activation. Keep one event, countable in the analytics you already have, reachable in a single session — a user who cannot finish the first task today will not come back tomorrow to finish it.

## The funnel maths before the redesign

Take 1,000 monthly sign-ups. Suppose activated users go on to pay at 25% and unactivated ones at 2% — plug in your own two rates, the arithmetic is the point.

| Activation rate | Activated | Paying from activated | Paying from the rest | Paying total |
| --- | --- | --- | --- | --- |
| 10% | 100 | 25 | 18 | 43 |
| 15% | 150 | 37.5 | 17 | 54.5 |
| 20% | 200 | 50 | 16 | 66 |
| 30% | 300 | 75 | 14 | 89 |

Read the first row before the last. At 10% activation, 18 of 43 paying customers — 42% — come from sign-ups who never activated: the price page is doing the onboarding. Moving 20% to 30% takes paying customers from 66 to 89 with no change to pricing, traffic or ad spend.

## Time to value, measured in hours

Log the timestamp of sign-up and of the activation event, then report the **median**. The mean is dragged upward by a few accounts that activated on day 40 for reasons of their own, and you spend a month chasing an average nobody experiences.

| Median time to value | What the first session has to do |
| --- | --- |
| Under 10 minutes | Remove steps until the first task is the only thing on the screen |
| 10 minutes to 1 hour | One guided task with a visible finish line — a progress bar with three named steps |
| 1 to 24 hours | Supply the reason to return: their data, their file, a job that runs overnight |
| Longer than a day | Sell the setup as a service, or do the first project for them |

## Four emails, one action each

A sequence is not a newsletter. Each message asks for exactly one thing, links once, and the whole sequence stops the moment activation fires.

- **Day 0 — the action.** Subject line is the task, not the product: "Send your first invoice". Body is three lines and one button.
- **Day 1 — the result.** A screenshot of what their screen should look like now. People do not need encouragement; they need to know whether it worked.
- **Day 3 — the blocker.** The one step where most accounts stop, answered before they hit it.
- **Day 7 — the question.** "What were you trying to get done when you stopped?" Replies go straight into the churn interviews below.

A tour that explains every feature on day one competes with the task. One 40-second recording, voiced once with a saved [[tool:elevenlabs|ElevenLabs]] voice, can be re-cut when the copy changes without booking anyone — and the tour is the first thing to go stale.

## A health score whose weights add to 100

A health score is only useful if each band triggers a different action. Weights are a judgement call; write them down so months compare.

| Factor | Weight | How it is measured |
| --- | --- | --- |
| Activated within 7 days | 30 | Activation event inside the window |
| Used on 3 separate days in the first 14 | 20 | Distinct active days, not sessions |
| Core action repeated in week 2 | 20 | A second invoice, a second export |
| More than one user or object created | 10 | Seats, projects, files |
| Integration or import connected | 10 | Data of theirs now in the product |

Bands and the one action each band gets:

| Score | Band | Action |
| --- | --- | --- |
| 70–100 | Healthy | Nothing automated; ask for a testimonial |
| 40–69 | Watch | One personal email naming the unfinished step |
| Under 40 | At risk | A human offer — a call, a setup, a pause on billing |

A score of 55 is a watch account: activated, but never repeated the core action in week 2. The email that follows names that one gap, not features.

## Retention compounds, so week one outweighs week twelve

Weekly retention multiplies. A cohort that keeps 60% of itself each week is 0.22% of its original size at week 12; at 75% it is 3.2% — fourteen times larger from a fifteen-point difference in a single week.

| Weekly retention | Week 4 | Week 8 | Week 12 |
| --- | --- | --- | --- |
| 60% | 13.0% | 1.68% | 0.22% |
| 65% | 17.9% | 3.19% | 0.57% |
| 70% | 24.0% | 5.76% | 1.38% |
| 75% | 31.6% | 10.0% | 3.17% |
| 80% | 41.0% | 16.8% | 6.87% |

The same arithmetic runs on churn: 5% a month leaves 54% of a cohort after a year, 3% leaves 69%.

## The churn interview: five questions, no pitching

Split every cancellation by whether the account ever activated. A never-activated account has an onboarding problem; an activated account that left has a product or price problem. Mixing them produces advice that fixes neither.

- What were you trying to get done the week you stopped?
- What did you use instead?
- Where did it stop making sense — the screen, or the idea?
- What would have had to be true for you to keep paying?
- Who else did you ask before deciding?

Do not ask "why did you cancel": the polite answer — "budget", "we're not ready" — is what people say to end a conversation. Do not offer a discount either, or you learn what they think of the price instead of the product. Ten interviews, coded into three reasons, name the gap no dashboard shows.

## Testing activation changes without a big sample

Activation tests are two-proportion tests. At 95% confidence and 80% power, users per arm:

> n ≈ 7.84 × (p₁(1−p₁) + p₂(1−p₂)) ÷ (p₂ − p₁)²

| Baseline | Target | Users per arm |
| --- | --- | --- |
| 15% | 20% | 902 |
| 20% | 24% | 1,678 |
| 20% | 25% | 1,090 |
| 25% | 30% | 1,247 |
| 30% | 35% | 1,372 |

A 20% relative lift needs 1,678 users per side; a 25% lift needs 1,090. Small differences are expensive to prove. With 200 activations a month, no onboarding test reports anything inside a quarter — ship the first-session fixes that are obviously right and track median time to value weekly.

## Checklist before the seventh day

- [ ] One activation event, defined in the analytics tool, not in a document
- [ ] A past cohort split by activation, with day-30 retention compared
- [ ] Median time to value measured and visible to the team
- [ ] Four emails, one action each, stopping on activation
- [ ] Health score with fixed weights and one action per band
- [ ] Cancellations separated by activation before the interview
- [ ] First-session screen reviewed once on a phone, as a new user

For $19, the [SaaS Onboarding & Retention OS](https://lozzy36.gumroad.com/l/saas-onboarding-retention-os) carries the 36 activation levers, the twelve formulas, 24 churn reasons with interview scripts, eight onboarding emails and the eight-factor health model used here, as Markdown, JSON and one offline HTML page.
