# Account Executive

An Account Executive is measured on booked revenue against quota in named accounts or a territory, so the agent team optimizes for a cleaner number, fewer surprise deal slips, better executive context, and customer conversations that move real opportunities instead of creating activity for its own sake.

## What good looks like in a week

A good AE week is not a wall of meetings.

It is a small number of customer conversations that advance qualified deals, a pipeline view that is honest enough to act on, and enough account context to know where to spend scarce attention.

Most AE time disappears into three recurring pains:

- Updating records after calls, often late and from memory.
- Rebuilding account context before every important conversation.
- Explaining the same forecast story in several different ways.

The agents should remove the rework around those pains.

By the end of a good week, the AE can answer:

- Which target buckets are ahead, exposed, or unsupported by evidence?
- Which open opportunities need a human decision this week?
- Which accounts deserve new outreach because something changed?
- Which forecast movement is backed by customer action?
- Which records are too stale to trust?

The recurring pain the agents remove is pipeline archaeology.

Instead of hunting through notes, CRM fields, meeting history, and public news before every call, the AE gets a short ranked view of what matters and what is missing.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: account-executive
segment: enterprise
book_shape: named-accounts
book_filter: "accounts where I am the owner or on the deal team"
targets:
  - name: "New business bookings"
    period: fiscal-year
    source: crm
  - name: "Expansion bookings"
    period: fiscal-year
    source: crm
  - name: "Renewal influenced bookings"
    period: fiscal-year
    source: crm
source_importance:
  matters_most:
    - crm
    - workplace
    - notes
    - web
  can_live_without:
    - decks
sources:
  crm: "<CRM source, required>"
  workplace: "<mail, calendar, and chat source, high value>"
  notes: "<notes source, helpful, or unavailable>"
  web: "built-in web search"
  decks: "<presentation source, optional, or unavailable>"
voice:
  derive_from: workplace
  sentence_length: short
  max_words_first_touch: 120
  never_use_em_dashes: true
output_dir: "artifacts/"
guardrails:
  crm_writes: propose-only
  outreach: draft-only
  external_sources: public-only
```

Why these choices:

- `role` selects the AE adoption path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `segment` changes the level of detail expected in briefs and deal reviews.
- `book_shape` tells agents whether to reason account by account or across a territory.
- `targets` should mirror the comp-plan bucket names, but never include values.
- `crm` is required because gaps, pipeline, stage, close dates, and ownership live there.
- `workplace` matters because actual customer intent often appears in meetings and messages before it appears in the CRM.
- `notes` help when the AE keeps informal account history that never became a record.
- `web` matters because public signals can change the priority order of the book.
- `decks` are optional for an AE unless deck updates are a major part of the selling motion.
- `voice.derive_from: workplace` keeps outreach from sounding like a template.
- `crm_writes: propose-only` matters because the AE owns the record and should approve changes.

## Week one: three agents

Use only these three until their outputs are reliable.

### `gap-analysis`

Why it comes first: it tells you whether the number is actually supported by pipeline in each named bucket.

First thing to ask it: "Compare my target buckets to my current pipeline and show the biggest gaps with evidence."

A good first output looks like:
- Bucket names that match your profile.
- A ranked list of gaps by account or territory slice.
- Coverage separated from customer evidence.
- A short close-the-gap plan that names the next account action.
- A `Gaps` line that says which targets or CRM fields were unavailable.

Most likely day-one disappointment: it treats the wrong target names as your buckets.

Fix: update `targets` in `config/profile.md` so the names match your real measurement language.

### `pipeline-hygiene`

Why it comes second: the gap view is only useful if the records behind it are clean enough to trust.

First thing to ask it: "Find stale, mis-staged, or under-evidenced opportunities in my book and stage fixes for my approval."

A good first output looks like:
- A short list of records that need attention.
- The field or evidence problem for each record.
- A proposed update, not an automatic write.
- A reason the update matters to forecast or account execution.

Most likely day-one disappointment: it flags too many records as stale.

Fix: map the CRM activity fields correctly through the source contract and confirm the stale threshold used by `crm-data-contract`.

### `account-brief`

Why it comes third: once the number and records are grounded, the AE needs account context before the next customer conversation.

First thing to ask it: "Brief me on the account for my next executive or buying committee meeting."

A good first output looks like:
- The resolved account entity and account family.
- Open opportunities with source records.
- Stakeholders ranked by role and confidence.
- Whitespace only when evidence supports it.
- One next step, not a long menu.

Most likely day-one disappointment: it has CRM facts but no relationship history.

Fix: map `workplace` or `notes`, or accept that the brief is CRM and public sources only.

## Week two to four: adding depth

Add agents in the order below, because each one uses output from the week-one trio.

### `deal-review`

Feed it the opportunities surfaced by `gap-analysis` and cleaned by `pipeline-hygiene`.

Its job is to name the weakest qualification element and the next actions that improve the deal, not to make the deal sound better.

### `outreach-orchestrator`

Feed it account context from `account-brief` and the specific gap or next action from `gap-analysis`.

It chains who to write, why now, what motion fits, and how to draft, with every draft still human-reviewed.

### `market-intel-sweep`

Run it across the book after the first two depth agents are working.

It finds public signals that should change account priority.

Feed high-confidence signals into `account-brief`, then into `outreach-orchestrator` only when the signal maps to a real customer problem.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `pipeline-hygiene` | Before customer follow-up or forecast edits | Records needing attention, staged changes, and missing evidence |
| Daily | `account-brief` | Before priority meetings | A short account readout and one next step |
| Weekly | `gap-analysis` | Start of territory review | Bucket gaps, coverage quality, and ranked close-the-gap actions |
| Per-deal or per-meeting | `deal-review` | A deal advances, stalls, or needs executive attention | Weakest qualification element and next actions |
| Monthly | `market-intel-sweep` | Reprioritizing the book | Public signals ranked by account and motion |
| Quarterly | `outreach-orchestrator` | Executive outreach cycle or territory reset | Review-ready drafts tied to sourced account signals |

## What this role should be careful about

- Pipeline coverage is not progress. Treat coverage as inventory until customer evidence proves movement.
- The agent will be confidently wrong about quota attainment unless the target bucket names are mapped and the values come from `crm` at run time.
- Forecast inflation is easy when `deal-review` is asked to justify a commit instead of test the commit.
- Do not let `outreach-orchestrator` write to a stakeholder just because the account has whitespace. It needs a reason the customer would recognize.
- If `pipeline-hygiene` stages updates, review them. The AE owns the record.
- If public news sounds exciting but does not connect to an open problem, leave it as context.
- The guardrail that matters most here is evidence before forecast movement.

## Signals you are getting value

- Forecast calls spend less time arguing about record hygiene and more time deciding next actions.
- The same accounts keep appearing at the top of gap, deal, and outreach outputs for clear reasons.
- Customer meetings start with a sharper hypothesis than "catch up."
- CRM updates happen closer to the customer conversation because the proposed changes are specific.
- Stop using an agent if it reports numbers without naming the source record or bucket.




