# Customer Success Manager

A Customer Success Manager is measured on retention, adoption, and expansion in an installed base, so the agent team optimizes for renewal risk visibility, customer outcome tracking, relationship context, and expansion timing that follows proven value instead of racing ahead of it.

## What good looks like in a week

A good CSM week is part relationship management, part operating discipline.

Time goes into adoption reviews, risk follow-up, renewal planning, stakeholder check-ins, support coordination, value documentation, and internal account-team alignment.

The recurring pain is reading the account through too few signals.

Silence can look like health.

A renewal date can become the only reason to talk.

Expansion can arrive before the customer believes the last purchase worked.

The agents should make quiet risk visible and keep the conversation anchored to outcomes.

By the end of a good week, the CSM can answer:

- Which installed-base accounts are healthy, at risk, or unknown?
- Which renewal conversations need action before the date becomes urgent?
- Which adoption gaps require customer or internal follow-up?
- Which expansion ideas are justified by proven value?
- Which relationship changes should the team know about?

The recurring pain the agents remove is renewal scramble.

Instead of reconstructing history when a renewal is close, the CSM keeps a steady view of value, adoption, risk, and next steps.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: customer-success-manager
segment: enterprise
book_shape: named-accounts
book_filter: "installed-base accounts where I own success, renewal, or expansion coordination"
targets:
  - name: "Renewal retention"
    period: fiscal-year
    source: crm
  - name: "Adoption health"
    period: fiscal-quarter
    source: crm
  - name: "Expansion pipeline"
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
  notes: "<notes source, high value, or unavailable>"
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
```

Why these choices:

- `role` selects the CSM path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `book_shape: named-accounts` fits an installed base where relationship history matters.
- `targets` name retention, adoption, and expansion outcomes without recording values.
- `crm` is required for renewal dates, products, opportunities, account ownership, and risk fields.
- `workplace` matters because sentiment and risk often appear in meetings before CRM is updated.
- `notes` matter because success plans and value observations may live outside formal records.
- `web` is useful for account changes, but internal signals matter more week one.
- `decks` are optional unless QBR or value-review material is central to the role.
- The `discovery-qualification` skill matters when expansion is being tested against real customer outcomes.
- `outreach: draft-only` protects customer trust in sensitive renewal or risk moments.

## Week one: three agents

Use these three to establish the installed-base truth before pursuing expansion.

### `renewal-expansion`

Why it comes first: it sees the book through retention risk and expansion readiness together.

First thing to ask it: "Score renewal risk and expansion whitespace across my installed-base accounts, with evidence and next actions."

A good first output looks like:

- Accounts grouped by renewal risk, adoption health, and expansion readiness.
- Evidence for each risk or expansion recommendation.
- Save actions separated from grow actions.
- Dates and owners for follow-up.
- A `Gaps` line for missing adoption, renewal, or relationship data.

Most likely day-one disappointment: it treats renewal proximity as the same thing as risk.

Fix: map adoption, support, meeting, and success-plan fields where they exist, then ask it to separate date urgency from health.

### `account-brief`

Why it comes second: the CSM needs a full account view before a renewal, value review, or stakeholder check-in.

First thing to ask it: "Brief me on this installed-base account with renewal risk, adoption history, stakeholders, and one next step."

A good first output looks like:

- Account and account-family resolution.
- Current products, open opportunities, and renewal context.
- Relationship history from CRM, workplace, or notes.
- Stakeholders ranked by role and confidence.
- One next action tied to customer value.

Most likely day-one disappointment: it lists opportunities but misses health.

Fix: make sure adoption and renewal fields are mapped in the CRM source and include notes where health is tracked outside CRM.

### `weekly-impact`

Why it comes third: success work compounds only if value and risk actions are captured over time.

First thing to ask it: "Roll up my week into renewal saves, adoption progress, expansion evidence, risks, and next-week actions."

A good first output looks like:

- Dated customer outcome entries.
- Risk movement separated from expansion activity.
- Follow-ups with owners.
- Missing sources called out plainly.

Most likely day-one disappointment: it records meetings but not outcomes.

Fix: keep short notes on customer outcomes and make sure `notes` or `workplace` is mapped.

## Week two to four: adding depth

The catalog gives this role two depth agents. Add them after the renewal and impact baseline is working.

### `market-news-scout`

Feed it accounts that `renewal-expansion` marks as at risk, unknown, or expansion-ready.

It finds public events that may change customer priorities or stakeholder urgency.

Those signals feed `account-brief` before the next customer conversation.

### `portfolio-dashboard`

Feed it the risk and expansion categories from `renewal-expansion` and the weekly movement from `weekly-impact`.

It creates a book-level view of installed-base health.

Use it to plan where the CSM spends time, not to replace customer conversations.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `account-brief` | Before renewal, value, or stakeholder meeting | Account context, relationship history, and next action |
| Weekly | `renewal-expansion` | Start of success planning block | Risk, adoption, expansion readiness, and dated actions |
| Weekly | `weekly-impact` | End of week | Value delivered, risks moved, expansion evidence, and tasks |
| Per-deal or per-meeting | `market-news-scout` | Before sensitive renewal or expansion conversation | Public account signal that may affect timing or tone |
| Monthly | `portfolio-dashboard` | Installed-base health review | Book-level health, risk, and expansion view |
| Quarterly | `renewal-expansion` | Renewal planning and QBR cycle | Save-or-grow plan grounded in evidence |

## What this role should be careful about

- Silence is not health. An account with no complaints and no engagement may be unknown, not safe.
- Letting the renewal date drive the conversation can make the customer feel managed instead of helped.
- Expansion pitches that land before value is proven can damage trust.
- The agent will be confidently wrong about health unless adoption, support, relationship, and renewal sources are mapped or explicitly unavailable.
- Do not use public news to manufacture urgency in a relationship that needs value proof.
- If `weekly-impact` cannot find outcomes, it will summarize activity. That is a warning, not a success.
- The guardrail that matters most here is value before expansion.

## Signals you are getting value

- Renewal conversations start earlier because risk is visible before urgency spikes.
- Expansion ideas are tied to adoption evidence and customer outcomes.
- Quiet accounts are labelled unknown instead of healthy.
- Weekly summaries show movement in value, risk, and next steps, not just meetings attended.
- Stop using an agent if it recommends expansion without naming the value proof already achieved.
