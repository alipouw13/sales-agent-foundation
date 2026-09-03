# SDR / BDR

An SDR or BDR is measured on qualified meetings created and pipeline sourced at high volume, so the agent team optimizes for better account selection, faster signal research, compliant sequencing, and outreach that sounds human enough to earn a reply without pretending to know more than it does.

## What good looks like in a week

A good SDR or BDR week is high motion, but not blind motion.

Time goes into account selection, contact research, first touches, follow-up, call prep, booking handoff notes, and cleaning up the trail so the next person can continue the conversation.

The recurring pain is context switching at volume.

Without agents, the rep either researches too slowly or sends messages that sound researched but are actually generic.

The agents should remove the false choice between volume and relevance.

By the end of a good week, the rep can answer:

- Which accounts had a fresh signal worth acting on?
- Which stakeholder role is the right first contact?
- Which sequence touch adds new information?
- Which accounts should be suppressed, paused, or handed to the owner?
- Which meetings were accepted as qualified, not just booked?

The best agent use here is disciplined repetition.

The agent finds signal, resolves likely stakeholders, drafts a sequence, and the rep reviews every send.

It does not blast a list.

## Your profile settings

Start from [`config/profile.example.md`](../../config/profile.example.md), copy it to `config/profile.md`, and keep the values private.

Use bucket names only.

```yaml
role: sdr-bdr
segment: commercial
book_shape: territory
book_filter: "accounts assigned for prospecting or sourced pipeline creation"
targets:
  - name: "Qualified meetings created"
    period: fiscal-quarter
    source: crm
  - name: "Pipeline sourced"
    period: fiscal-quarter
    source: crm
  - name: "Accepted opportunities"
    period: fiscal-quarter
    source: crm
source_importance:
  matters_most:
    - crm
    - workplace
    - web
  can_live_without:
    - notes
    - decks
sources:
  crm: "<CRM source, required>"
  workplace: "<mail, calendar, and chat source, required for voice and suppression checks>"
  notes: "<notes source, optional, or unavailable>"
  web: "built-in web search"
  decks: "unavailable"
voice:
  derive_from: workplace
  sentence_length: short
  max_words_first_touch: 90
  banned_phrases:
    - "I hope this email finds you well"
    - "circling back"
    - "touch base"
  never_use_em_dashes: true
output_dir: "artifacts/"
guardrails:
  crm_writes: propose-only
  outreach: draft-only
  external_sources: public-only
  suppression_checks: required
```

Why these choices:

- `role` selects the SDR or BDR path in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).
- `segment` changes the likely buying committee and acceptable outreach style.
- `book_shape: territory` fits a high-volume patch better than a named strategic book.
- `targets` name meeting and sourced-pipeline outcomes without storing values.
- `crm` is required to avoid contacting the wrong account owner or stale contact.
- `workplace` matters more here than in most roles because sent mail shapes voice and suppression history protects the account.
- `web` is high value because fresh public signals make cold outreach less cold.
- `notes` help when the team keeps account do-not-contact context outside CRM, but agents must say when notes are unavailable.
- `decks` are usually unnecessary for week-one prospecting.
- The `outreach-voice` skill matters because it bans fake warmth, filler, and template tells.

## Week one: three agents

Use only these three until the research and draft quality are trusted.

### `prospecting-sequence`

Why it comes first: it turns a target account and reason to reach out into a multi-touch plan that adds new information each time.

First thing to ask it: "Create a compliant prospecting sequence for this account segment using only sourced signals and my voice settings."

A good first output looks like:

- A clear account trigger or reason for outreach.
- A stakeholder role for each touch.
- A different point of value in each step.
- Drafts that are short and specific.
- A suppression or compliance note before any send.

Most likely day-one disappointment: it writes a polished generic sequence.

Fix: give it a real signal from `market-news-scout` or `industry-analyst`, and confirm the profile can derive voice from `workplace`.

### `market-news-scout`

Why it comes second: high-volume prospecting needs a daily source of "why this account now" signals.

First thing to ask it: "Scan my prospecting book for public news that justifies a relevant first touch."

A good first output looks like:

- Accounts ranked by signal strength.
- A public URL and date for each claim.
- The implied opportunity signal from `opportunity-signal-taxonomy`.
- A recommendation to act, wait, or ignore.

Most likely day-one disappointment: it finds news that is interesting but not actionable.

Fix: tune the solution catalog and ask for only signals that map to a customer problem your team can credibly discuss.

### `account-intel-360`

Why it comes third: the rep needs to avoid sending a good message to the wrong role.

First thing to ask it: "Resolve the account family and rank likely buying committee roles for a first outreach motion."

A good first output looks like:

- The account entity it resolved.
- Contact roles with confidence, not certainty when evidence is thin.
- Relationship history from CRM or workplace if available.
- A first-contact recommendation with a reason.

Most likely day-one disappointment: it infers roles too broadly.

Fix: make sure CRM contact fields are mapped through `crm-data-contract`, then review the `stakeholder-mapping` assumptions before using the draft.

## Week two to four: adding depth

The catalog gives this role two depth agents. Do not add extra agents just to automate more.

### `industry-analyst`

Feed it the strongest signals from `market-news-scout` when the account deserves more than a quick first touch.

It adds public peer pressure, industry context, and a better reason the account might care.

That output feeds `prospecting-sequence` for a sharper sequence.

### `outreach-writer`

Feed it the approved stakeholder from `account-intel-360` and the sourced reason from `industry-analyst`.

It should produce the individual message the rep reviews before sending.

Use it after the sequence exists, not before, so each message fits the broader motion.

## The recurring rhythm

| Cadence | Agent | Trigger | Output |
| --- | --- | --- | --- |
| Daily | `market-news-scout` | Start of prospecting block | Ranked account signals with public source and action call |
| Daily | `prospecting-sequence` | New account selected for outreach | Review-ready sequence with compliance notes |
| Weekly | `account-intel-360` | Building or refreshing the target list | Account family, likely roles, and contact priority |
| Per-deal or per-meeting | `outreach-writer` | Before a first touch, follow-up, or meeting confirmation | Short draft in the runner's voice |
| Monthly | `industry-analyst` | Territory theme planning | Public context that explains why this segment should respond now |
| Quarterly | `prospecting-sequence` | Sequence refresh | Retired weak patterns and updated message angles |

## What this role should be careful about

- Volume tempts reps into templates, exactly what the `outreach-voice` skill is designed to prevent.
- Personalization theatre is worse than no personalization. Do not mention a fact unless the next sentence explains why it matters.
- Opt-out, suppression, and do-not-contact checks matter more here than in any other role. No signal overrides them.
- The agent will be confidently wrong about stakeholder fit unless CRM contact roles and account ownership are mapped.
- A weak first touch can burn an account for the AE or CSM. If the reason to write is thin, wait.
- Do not let `market-news-scout` turn every article into an opportunity.
- Draft-only is not optional. A human reviews before anything leaves the inbox.

## Signals you are getting value

- Fewer messages start from a blank page, but more of them cite a real account reason.
- Accepted meetings have cleaner handoff notes and fewer "why did we book this" questions.
- The same weak sequence patterns are retired instead of repeated.
- Suppression checks are visible before send, not after a complaint.
- Stop using an agent if it produces outreach that could be sent unchanged to any account in the territory.
