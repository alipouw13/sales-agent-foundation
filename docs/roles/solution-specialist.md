# Solution Specialist

A Solution Specialist is measured on one solution area's revenue or consumption across many accounts they do not own, so the agent team optimizes for evidence-backed whitespace, account-team relevance, motion clarity, and outreach that helps the owner rather than colliding with them.

## What good looks like in a week

A good specialist week is a portfolio exercise followed by precise account-team engagement.

The specialist scans many accounts, finds where the solution motion is truly relevant, earns time with account owners, helps progress a small set of opportunities, and avoids becoming a broadcast channel for product news.

The recurring pain is getting attention without ownership.

The specialist sees patterns across the book, but the account owner controls customer context and timing.

The agents should turn a broad solution mandate into a ranked, evidence-backed set of account conversations.

By the end of a good week, the specialist can answer:

- Which accounts have the strongest evidence for this solution area?
- Which target bucket is most exposed?
- Which account owner should be engaged first and why?
- Which market signal supports the motion?
- Which outreach should come from the specialist, and which should come from the owner?

The recurring pain the agents remove is unsupported whitespace.

Instead of a long list of accounts that have not bought the product, the specialist gets a shorter list of accounts with evidence, motion, and a respectful handoff path.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: solution-specialist
segment: enterprise
book_shape: vertical
book_filter: "accounts in my solution-area coverage where I am owner or specialist support"
targets:
  - name: "Solution-area bookings"
    period: fiscal-year
    source: crm
  - name: "Consumption growth"
    period: fiscal-quarter
    source: crm
  - name: "Qualified solution pipeline"
    period: fiscal-quarter
    source: crm
source_importance:
  matters_most:
    - crm
    - web
    - workplace
  can_live_without:
    - notes
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
  never_use_em_dashes: true
output_dir: "artifacts/"
guardrails:
  crm_writes: propose-only
  outreach: draft-only
  external_sources: public-only
```

Why these choices:

- `role` selects the specialist path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `book_shape: vertical` often fits a role that spans many accounts through a solution lens.
- `targets` name the specialist's solution buckets without storing values.
- `crm` is required to see pipeline, ownership, products, stages, and account-team roles.
- `web` matters because external signals help the specialist earn relevance with account teams.
- `workplace` matters because the specialist must see recent account-team coordination before engaging.
- `notes` help capture informal account-owner guidance, but the agent must say when notes are missing.
- `decks` are optional unless the specialist frequently ships enablement material.
- The `solution-messaging` skill matters because product fit is not the same as customer problem fit.
- Draft-only outreach protects the relationship between specialist, owner, and customer.

## Week one: three agents

Use these three to build evidence before asking account teams for time.

### `gap-analysis`

Why it comes first: the specialist needs to know where the solution-area target is unsupported by real pipeline.

First thing to ask it: "Show my solution-area gaps by account and bucket, with evidence quality separated from coverage."

A good first output looks like:

- Target bucket names that match the specialist profile.
- Accounts ranked by gap and evidence.
- Existing opportunities separated from whitespace.
- A proposed action that names the account owner or next internal step.

Most likely day-one disappointment: it ranks accounts only by missing product.

Fix: update `solution_catalog` and ask for evidence from `opportunity-signal-taxonomy`, not just white space.

### `portfolio-dashboard`

Why it comes second: the specialist needs a portfolio view to explain where focus belongs.

First thing to ask it: "Build a portfolio view for my solution area across my covered accounts."

A good first output looks like:

- Accounts grouped by current adoption, pipeline, and whitespace.
- Evidence columns, not just scoring.
- Stakeholder or account-owner context where available.
- A clear top-priority list for the next operating cycle.

Most likely day-one disappointment: it creates a beautiful list that account teams do not trust.

Fix: make sure CRM ownership, product fields, and stage fields are mapped through `crm-data-contract`.

### `motion-strategist`

Why it comes third: the specialist must translate a signal into a motion the account team can recognize.

First thing to ask it: "Map this account signal to the right solution motion and talk track for the account owner and customer executive."

A good first output looks like:

- The signal it is using.
- The motion it recommends.
- The role-level message.
- Traps to avoid.
- A clear next internal or customer action.

Most likely day-one disappointment: it sounds like product marketing.

Fix: feed it the customer problem from `gap-analysis` or `portfolio-dashboard`, not just the product area.

## Week two to four: adding depth

The catalog gives this role two depth agents. They compound only if the portfolio view is already trusted.

### `market-intel-sweep`

Feed it the account list and gaps surfaced by `portfolio-dashboard`.

It finds public signals that explain why the solution motion matters now.

High-confidence signals feed `motion-strategist` for message shaping.

### `outreach-orchestrator`

Feed it the account priority from `portfolio-dashboard`, the motion from `motion-strategist`, and the signal from `market-intel-sweep`.

Use it to draft internal account-owner outreach first when ownership is sensitive.

Only move to customer-facing drafts when the owner agrees or the engagement model allows it.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `motion-strategist` | New signal, objection, or account-team ask | Motion, talk track, and trap list |
| Weekly | `gap-analysis` | Solution-area pipeline review | Bucket gaps and evidence-backed account actions |
| Weekly | `portfolio-dashboard` | Prioritizing account-team engagement | Ranked coverage and whitespace view |
| Per-deal or per-meeting | `outreach-orchestrator` | Asking an account owner or customer for action | Draft aligned to signal, role, and owner context |
| Monthly | `market-intel-sweep` | Refreshing why-now evidence | Public signals mapped to accounts and motions |
| Quarterly | `portfolio-dashboard` | Business review or territory reset | Portfolio story, focus accounts, and stale assumptions |

## What this role should be careful about

- Whitespace lists with no evidence behind them will damage trust with account teams.
- Colliding with the account owner is a specialist-specific risk. Ask who owns the next conversation before drafting customer outreach.
- The agent will be confidently wrong about fit if it sees product absence as customer need.
- Do not mistake a product motion for a customer problem. The `solution-messaging` skill should translate, not decorate.
- Public signals need dates and citations, or they should not change account priority.
- If the CRM product taxonomy is poorly mapped, every portfolio view will look more precise than it is.
- The guardrail that matters most here is owner alignment before customer activation.

## Signals you are getting value

- Account owners accept the specialist's recommendations because each one has evidence and a next action.
- The specialist spends less time explaining the product and more time shaping customer-specific motions.
- Portfolio reviews identify a smaller set of accounts with better reasons to act.
- Outreach drafts start with internal alignment when ownership is sensitive.
- Stop using an agent if it ranks whitespace without showing the evidence behind each account.
