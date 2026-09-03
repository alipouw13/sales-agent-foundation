# Sales Manager

A Sales Manager is measured on team attainment and forecast accuracy, so the agent team optimizes for cleaner roll-ups, better coaching questions, earlier risk detection, and a shared operating rhythm that helps reps improve rather than making them feel watched.

## What good looks like in a week

A good manager week is a balance of inspection, coaching, and decision making.

Time goes into forecast calls, pipeline reviews, deal strategy, one-on-ones, customer escalations, hiring or enablement work, and translating leadership asks into useful action for the team.

The recurring pain is stale inputs.

A manager can spend the whole week asking whether records are current, then still carry a forecast that rests on optimism.

The agents should reduce inspection drag so the manager can ask better coaching questions.

By the end of a good week, the manager can answer:

- Which calls changed, and what evidence changed them?
- Which reps need coaching on qualification, not just more activity?
- Which pipeline gaps are team-wide patterns?
- Which records are stale enough to distort the roll-up?
- Which deals need management help, and why?

The recurring pain the agents remove is record-by-record reconstruction.

Instead of opening every opportunity before a forecast call, the manager sees where the evidence is thin and where coaching time will matter.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: sales-manager
segment: enterprise
book_shape: territory
book_filter: "accounts, opportunities, and reps in my management span"
targets:
  - name: "Team bookings"
    period: fiscal-year
    source: crm
  - name: "Forecast accuracy"
    period: fiscal-quarter
    source: crm
  - name: "Pipeline creation"
    period: fiscal-quarter
    source: crm
source_importance:
  matters_most:
    - crm
    - workplace
    - notes
  can_live_without:
    - web
    - decks
sources:
  crm: "<CRM source, required>"
  workplace: "<mail, calendar, and chat source, high value>"
  notes: "<manager notes source, high value, or unavailable>"
  web: "built-in web search"
  decks: "<presentation source, optional, or unavailable>"
voice:
  derive_from: workplace
  sentence_length: short
  never_use_em_dashes: true
output_dir: "artifacts/"
guardrails:
  crm_writes: propose-only
  outreach: draft-only
  external_sources: public-only
  team_visibility: required
```

Why these choices:

- `role` selects the manager path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `book_shape: territory` fits a roll-up across reps, accounts, and opportunity owners.
- `targets` name team outcomes and forecast quality without storing values.
- `crm` is required because the roll-up must come from live records, not manager memory.
- `workplace` matters because deal evidence and coaching context often appear in meeting threads.
- `notes` matter more for managers because coaching commitments should not be reconstructed from memory.
- `web` is useful for context on strategic accounts, but not required for week-one forecast discipline.
- `decks` are optional unless the manager regularly prepares business-review material.
- `crm_writes: propose-only` keeps the manager from overwriting rep-owned records without review.
- `team_visibility: required` means the team should know these agents are running and what they are used for.

## Week one: three agents

Use these three to make the roll-up honest before expanding into coaching workflows.

### `forecast-review`

Why it comes first: the manager's highest leverage is separating evidence from optimism before the call is locked.

First thing to ask it: "Roll up my team's forecast by category and show what evidence would change each call."

A good first output looks like:

- Forecast categories with source records.
- Changes since the prior review if available.
- Evidence for each call.
- Risks and actions separated by owner.
- A `Gaps` line for missing CRM fields or stale inputs.

Most likely day-one disappointment: it repeats the CRM forecast without judgment.

Fix: ensure the CRM stage, forecast category, close date, activity, and qualification fields are mapped through `crm-data-contract`.

### `pipeline-hygiene`

Why it comes second: forecast review cannot improve while stale records keep polluting the roll-up.

First thing to ask it: "Find stale or mis-staged opportunities across my team's book and stage record fixes for owner review."

A good first output looks like:

- Records grouped by rep or owner.
- The hygiene issue and why it matters.
- Proposed changes that can be reviewed by the owner.
- Patterns the manager can coach to.

Most likely day-one disappointment: it feels like a compliance report.

Fix: ask for coaching themes and owner-review queues, not a wall of defects.

### `gap-analysis`

Why it comes third: once the forecast and hygiene baseline are visible, the manager needs to know whether the team has enough qualified path by bucket.

First thing to ask it: "Show team gaps by target bucket and identify where coaching or coverage action is needed."

A good first output looks like:

- Bucket gaps by team slice.
- Coverage quality separated from raw pipeline.
- Reps or accounts needing help.
- Actions that improve evidence, not just amount.

Most likely day-one disappointment: it turns into a leaderboard.

Fix: configure book filters and ask for coaching actions, not ranking for its own sake.

## Week two to four: adding depth

The catalog gives this role two depth agents. Add them after the team understands the first three are coaching aids.

### `deal-review`

Feed it the deals from `forecast-review` where the call is uncertain or the customer evidence is weak.

Use its output to coach the rep on qualification and next action.

Do not use it as a replacement for the rep's judgment in the customer conversation.

### `portfolio-dashboard`

Feed it the team-level patterns from `gap-analysis` and the hygiene themes from `pipeline-hygiene`.

It creates a broader view of where pipeline, whitespace, and risk are concentrated.

Use it for planning territory actions and enablement, not for surveillance.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `pipeline-hygiene` | Before forecast edits or rep check-ins | Owner-review queue and coaching patterns |
| Weekly | `forecast-review` | Forecast call preparation | Evidence-based roll-up and call-change list |
| Weekly | `gap-analysis` | Pipeline generation and coverage review | Bucket gaps and coaching actions |
| Per-deal or per-meeting | `deal-review` | Deal stuck, call contested, or executive help requested | Qualification gaps and next coaching questions |
| Monthly | `portfolio-dashboard` | Team operating review | Portfolio patterns, whitespace, and risk concentration |
| Quarterly | `forecast-review` | Planning reset or business review | Forecast accuracy lessons and operating changes |

## What this role should be careful about

- Do not use the agents as surveillance. Say directly to the team that they are running, what they inspect, and how outputs will be used.
- Inspecting records is not the same as coaching. Convert every finding into a question, decision, or support action.
- The agent will be confidently wrong about the roll-up if inputs are stale, unmapped, or owned by the wrong rep.
- A clean dashboard can hide weak discovery. Use `deal-review` to test evidence before accepting the call.
- Do not let `pipeline-hygiene` create shame lists. Owner-review queues and coaching themes are healthier.
- Avoid changing rep-owned CRM fields without review, even when the proposed fix looks obvious.
- The guardrail that matters most here is transparency with the team.

## Signals you are getting value

- Forecast meetings spend more time on changed evidence and less time on data cleanup.
- Reps receive better coaching questions because weak qualification patterns are visible.
- The team knows which agents are running and does not experience them as hidden monitoring.
- Pipeline gaps are addressed by coaching, coverage changes, or account action, not just pressure.
- Stop using an agent if it becomes a leaderboard that changes behavior through fear rather than better decisions.
