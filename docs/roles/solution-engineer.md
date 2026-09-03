# Solution Engineer

A Solution Engineer is measured on technical win rate, deal influence, and enabling the account team, not quota directly, so the agent team optimizes for sharper account preparation, reusable proof assets, visible impact, and enough qualification discipline to keep technical effort on deals that deserve it.

## What good looks like in a week

A good SE week mixes customer-facing work with invisible preparation.

There are discovery calls, demos, proof planning, follow-up notes, account team huddles, deck changes, technical objections, and internal questions that arrive with little context.

The recurring pain is that the highest-value work often becomes invisible.

If the SE does not capture impact, a week of unblocking deals can look like a calendar full of random support.

The agents should make the work easier to prepare, easier to reuse, and easier to explain.

By the end of a good week, the SE can answer:

- Which customer conversations need technical preparation?
- Which decks or proof assets can be reused instead of rebuilt?
- Which deals are asking for technical effort before qualification is strong enough?
- Which blockers did the SE remove this week?
- Which account-team enablement artifact should exist because the same question keeps returning?

The recurring pain the agents remove is prep fragmentation.

Instead of reading scattered notes, CRM records, and old slides, the SE gets enough account context to tailor the technical conversation and enough weekly roll-up to show influence.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: solution-engineer
segment: enterprise
book_shape: patch
book_filter: "accounts and opportunities where I am assigned for technical support"
targets:
  - name: "Technical win influence"
    period: fiscal-quarter
    source: crm
  - name: "Proof progression"
    period: fiscal-quarter
    source: crm
  - name: "Account team enablement"
    period: fiscal-quarter
    source: workplace
source_importance:
  matters_most:
    - crm
    - workplace
    - decks
    - notes
  can_live_without:
    - web
sources:
  crm: "<CRM source, required>"
  workplace: "<mail, calendar, and chat source, high value>"
  notes: "<notes source, high value, or unavailable>"
  web: "built-in web search"
  decks: "<presentation source, high value>"
voice:
  derive_from: workplace
  sentence_length: short
  never_use_em_dashes: true
output_dir: "artifacts/"
guardrails:
  crm_writes: propose-only
  outreach: draft-only
  external_sources: public-only
```

Why these choices:

- `role` selects the SE path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `book_shape: patch` fits a role that supports many sellers or solution motions without owning every account.
- `targets` name influence and enablement outcomes without pretending they are booked revenue.
- `crm` is required to know which opportunities exist and whether they are qualified.
- `workplace` matters because technical asks often arrive through meeting threads and team messages.
- `decks` matter more here than for most roles because deck reuse and edits are a major time sink.
- `notes` are high value when the SE keeps demo, architecture, or objection handling notes privately.
- `web` is useful for industry context, but most week-one SE leverage is internal and account-specific.
- The `deck-visual-system` skill helps deck agents keep artifacts usable without turning every request into redesign.
- `output_dir` protects customer-specific artifacts from being committed.

## Week one: three agents

Use these three to make the work visible before adding more automation.

### `account-brief`

Why it comes first: the SE needs account and opportunity context before choosing a demo, proof path, or technical angle.

First thing to ask it: "Brief me on the account and open opportunities before my technical discovery or demo."

A good first output looks like:

- The resolved account and open opportunities.
- The current customer problem in plain language.
- Stakeholders and likely technical evaluators when evidence exists.
- Whitespace only when supported by account evidence.
- One next technical question to ask.

Most likely day-one disappointment: it reads like a seller brief and misses the technical angle.

Fix: add solution catalog terms that match your SE coverage and ask for technical unknowns explicitly.

### `enablement-deck`

Why it comes second: SEs repeatedly explain the same concepts, and a reusable deck prevents starting over every time.

First thing to ask it: "Build a short enablement deck for this solution motion using sourced customer problem framing and reusable visuals."

A good first output looks like:

- A clear audience and outcome.
- Slides tied to a customer problem, not a product tour.
- Citations for external claims.
- Visual restraint from `deck-visual-system`.
- Speaker notes that help the account team reuse it.

Most likely day-one disappointment: the deck is too broad.

Fix: narrow the motion, audience, and meeting objective before asking for slides.

### `weekly-impact`

Why it comes third: technical work has to be captured while it is fresh or it disappears.

First thing to ask it: "Roll up my week into customer impact, deal influence, blockers removed, and next-week actions."

A good first output looks like:

- Dated entries tied to meetings, opportunities, or artifacts.
- Internal enablement separated from customer-facing impact.
- Follow-up tasks the SE can actually do.
- A `Gaps` line for missing workplace, CRM, or notes sources.

Most likely day-one disappointment: it misses work that happened outside CRM.

Fix: map `workplace` and `notes`, then keep short notes for proof work that never becomes a CRM activity.

## Week two to four: adding depth

The catalog gives this role two depth agents. Add them only after the week-one trio is useful.

### `deck-editor`

Feed it decks created by `enablement-deck` or existing customer decks that need updates.

Use it for surgical changes, not total reinvention.

It compounds when `account-brief` identifies the customer problem and `deck-editor` updates only the slides that need to change.

### `deal-review`

Feed it opportunities where the account team is asking for a demo, proof, workshop, or executive technical support.

It tests whether the deal is qualified enough for the requested technical effort.

Use its output to decide what the SE should build, defer, or ask before committing time.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `account-brief` | Before technical discovery, demo, or proof call | Account context, open questions, and one next technical action |
| Weekly | `weekly-impact` | End of week or before manager check-in | Deal influence, blockers removed, artifacts shipped, and next actions |
| Weekly | `enablement-deck` | Repeated account-team question or upcoming workshop | Reusable deck grounded in the motion and audience |
| Per-deal or per-meeting | `deal-review` | Requested proof, demo, or technical escalation | Qualification gaps and effort recommendation |
| Monthly | `deck-editor` | Refreshing core talk tracks or customer decks | Updated deck without unnecessary redesign |
| Quarterly | `weekly-impact` | Business review or performance narrative | Evidence-backed summary of technical influence |

## What this role should be careful about

- The biggest SE failure mode is making impact invisible. That is why `weekly-impact` belongs in week one.
- Demo and proof effort spent on unqualified deals steals time from deals that can actually move.
- The agent will be confidently wrong about what to prove unless `deal-review` has the customer outcome and decision criteria.
- Do not over-engineer a proof because the agent produced a beautiful plan. Ask what the smallest customer-valid proof is.
- Deck agents can make artifacts look more finished than the story deserves. Evidence still matters.
- If `account-brief` lacks workplace and notes history, it may miss the real objection even when CRM looks clean.
- The guardrail that matters most here is effort gating before technical build time.

## Signals you are getting value

- Account teams ask for fewer last-minute custom decks because reusable assets exist.
- Technical calls start with known unknowns instead of a product tour.
- Proof requests become smaller, clearer, and better tied to decision criteria.
- Weekly summaries show customer impact and account-team enablement without hours of reconstruction.
- Stop using an agent if it turns every technical ask into a proof or deck instead of asking whether the deal is qualified.
