---
title: "What One Workflow Run Really Costs: Run-Cost Math, Retry Budgets and Rate-Limit Guardrails in n8n, Make and Zapier"
slug: "workflow-run-cost-retry-rate-limits"
date: "2026-11-19"
category: "Automation"
excerpt: "Two workflows that do the same job can cost ten times different amounts, and both can fail at 3am without telling anyone. The billing unit each platform counts, the retry window it gives you, and the guardrails that make a run safe to leave on."
description: "What n8n, Make and Zapier each count as a billable unit, the same 12-step workflow priced three ways, real retry limits and backoff schedules, and the guardrails to add before a workflow runs unattended."
tags: ["n8n", "Make", "Zapier", "automation cost", "rate limits", "error handling"]
tools: ["elevenlabs"]
featured: false
---

Automations are chosen by how fast they can be built and kept by two numbers nobody writes down: what a run costs, and what happens when it fails at 3am. Both are knowable before the first node is connected, and both are usually discovered later, on an invoice.

The arithmetic below runs one twelve-step workflow through the three most-picked platforms. The point is not that one is cheaper: "cheap" means something different on each, and the difference decides the platform for you.

## The unit is not the same unit

| Platform | Billing unit | Counted | Not counted | Entry paid plan |
| --- | --- | --- | --- | --- |
| n8n | One execution: a single run of the whole workflow | Production runs started by a trigger or webhook | Steps inside the run | Starter, 2,500 executions, $24/mo monthly ($20 annual) |
| Make | One credit per module action | Reads, searches, writes, iterations, the trigger | Router and error-handler modules | Core, 10,000 credits, $16/mo monthly ($12 annual) |
| Zapier | One task per successful action step | Each completed action | Triggers, polling, failed actions, built-in tools such as Filter, Paths, Formatter, Delay | Professional, 750 tasks, $29.99/mo monthly ($19.99 annual) |

Prices are each vendor's November 2026 figure, monthly billing, USD; all three have changed twice this year, so check before buying.

The third column is where they stop being comparable. On n8n a twenty-node workflow and a two-node workflow cost the same per run. Elsewhere the bill is the sum of the steps, so "one big workflow or three small ones" becomes a billing question.

## The same twelve-step workflow, priced three ways

A workflow that runs 1,000 times a month: trigger, filter, lookup, normalise, one AI call, create, update, upload, notify, log. Twelve modules, eleven of them actions after the trigger.

| | Units per run | Units per month | Plan needed | Monthly cost | Cost per run |
| --- | --- | --- | --- | --- | --- |
| n8n | 1 execution | 1,000 | Starter (2,500) | $24 | $0.024 |
| Make | 12 credits | 12,000 | Core, 20,000 credits | $28 | $0.028 |
| Zapier | 11 tasks | 11,000 | Professional, 20,000 tasks | $283.50 | $0.28 |

The first two land within a few cents. The third is roughly ten times that, not because Zapier is priced badly but because 750 tasks cost $29.99 — four cents a task, eleven tasks a run.

**Depth is cheap on n8n and billable elsewhere.** Splitting one long workflow into five small ones costs five executions on n8n and nothing extra on Make or Zapier, because the modules are unchanged.

**Fan-out flips the arithmetic.** A run processing 300 rows is one execution on n8n and 300 module iterations on Make, where the cheap option becomes the expensive one. Price at the item count you expect.

The table hides a cliff: on Make, 10,000 credits is $16 and 20,000 is $28, so 12,000 costs 75% more for 20% more volume. Add 30% headroom and price the tier above.

## What the retry window actually buys

| Platform | Where it is set | Attempts | Total window |
| --- | --- | --- | --- |
| n8n | Node settings, Retry On Fail | 2 to 5 tries, default 3; wait 0 to 5,000 ms, default 1,000 ms | Seconds |
| Make | Error handler on the module | Retry handler: 3 attempts, 15 min apart by default; rate-limit, connection and timeout errors also back off 1 min, 10, 10, 30, 30, 30, then 3 h twice | Hours |
| Zapier | Autoreplay, account or per Zap | Up to 5 attempts at 5 min, 30 min, 1 h, 3 h, 6 h | About 10 h 35 min |

The table answers the question every failure asks: hiccup or outage? n8n's retries cover a dropped request or a rate limit, not a vendor down for twenty minutes; that needs Loop Over Items with a Wait, or a scheduled re-check. Zapier's autoreplay suits the other case and is slow by design.

n8n's retries carry a condition: they only run when the node's On Error stays at Stop Workflow. Set it to Continue or Continue (using error output) and the retry settings are ignored, so the item goes down the error branch on the first failure.

## Retry only what is safe to run twice

Some actions must not happen twice: charging a card, posting to a live account, emailing a customer. Keep those out of retry and put a check in front of them.

- Reads, lookups, uploads to a named path and updates that set a value are safe to repeat.
- Creates, sends and charges are not. Give them an idempotency key, or write an "already done" flag first and check it on the second attempt.
- If a step can half-succeed, log before the call and after it so a retry can tell the difference.

Retries are priced differently. On n8n a retry stays inside the same execution; on Make the failing bundle reruns from the failing module, spending credits on each attempt, though error-handler modules are free; on Zapier failed actions are not counted at all. That settles the setting rather than the platform: stop giving five retries to a step failing for a reason retries will not fix.

The most retry-prone call in a content pipeline is the narration step: [[tool:elevenlabs|ElevenLabs]] returns one file per line, so a timeout on line 14 of 40 can be re-fetched alone instead of regenerating forty.

## Rate limits are a scheduling problem

A rate limit says the schedule is wrong; retrying faster cannot fix it. On n8n it literally cannot: Wait Between Tries is capped at 5,000 ms and the HTTP Request node ignores `Retry-After`, so the limit has to be handled in the design.

- **Batch before you call.** One request for twenty records beats twenty requests, everywhere.
- **Space the batch.** Loop Over Items with a Wait on n8n, an iterator with a sleep or a 15-minute schedule on Make, Delay or Looping on Zapier.
- **Filter before you fetch.** A trigger filter costs nothing and removes a whole call.
- **Respect the concurrency ceiling.** n8n Starter runs 5 executions at once and caps a run at 5 minutes; Pro raises those to 20 and 40.

## Guardrails that make a workflow safe to leave on

- [ ] Anything irreversible is prepared, not completed: a draft, a proposal, a review queue, an internal note
- [ ] One log row per run: timestamp, item count, duration, result
- [ ] An item cap per run, which stops rather than truncating silently
- [ ] A dry-run first week: read, log, skip the writes
- [ ] Failures land in one inbox a human reads, not a vendor's history page
- [ ] A pause flag checked at the first node, so the kill switch is one edit
- [ ] A named owner and a review date

The cap and the log pay first. Without a cap, one bad query becomes 40,000 runs and a bill; without a log row, "it stopped working last Tuesday" is an anecdote, not a record.

## Deleting a workflow is a cost decision

A run costing 3 cents and saving three minutes at $30 an hour returns about $1.50, a good trade if it runs on real items. If one run in twenty produces something usable, the cost per useful outcome is twenty times that.

The workflows worth deleting are rarely the expensive ones. They fail quietly, get checked by a person every morning, and take fifteen minutes a week. One that saves twenty minutes and costs fifteen in supervision is a second job with a subscription.

The 32 blueprints in the [AI Automation Blueprint Pack](https://lozzy36.gumroad.com/l/automation-blueprint-pack) were built around this arithmetic: the trigger, the ordered steps, the guardrail, the common failure and a cost per run, plus a studio that calculates break-even volume.

## Three numbers before the first node

Steps per run, runs per month, and what happens on failure. Write those three down and the choice mostly makes itself. Anything that must happen on time needs a retry window shorter than its deadline; the rest is preference, and preferences are fine as long as the invoice was expected.
