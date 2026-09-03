# Agent catalog

The single source of truth for the agent team. `tools/validate_repo.py` asserts
that every agent on disk appears here, that every agent named here exists, and
that every skill cited here exists.

Each row is one agent. The prompt is the reusable front door in
[`prompts/`](prompts/); run it when you want to be asked for the inputs. The
skills are the shared playbooks in [`skills/`](skills/) that the agent reads so
its output stays consistent with the rest of the team.

## Lifecycle personas

How changes to *this repository* get made. They carry no reusable prompt because
they are process, not a revenue workflow.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `spec` | n/a | n/a | Defines or updates `SPEC.md` before any content is written. Run first when scope is fuzzy. |
| `plan` | n/a | n/a | Turns a spec change into a short ordered list of verifiable slices. |
| `build` | n/a | n/a | Executes the plan one slice at a time, validating between each. |
| `validate` | n/a | n/a | Re-checks executed work against the original request, `SPEC.md`, and the project rules. |
| `code-reviewer` | n/a | n/a | Reads the diff for guardrail violations, leaked data, and contract drift. High signal only. |

## Account intelligence

Who the account is, who to talk to, and why they should care now.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `account-brief` | [account-brief](prompts/account-brief.prompt.md) | `crm-data-contract`, `stakeholder-mapping` | An account 360 or pre-meeting brief: history, open opportunities, whitespace, stakeholders, and one next step. |
| `account-intel-360` | [account-intel-360](prompts/account-intel-360.prompt.md) | `stakeholder-mapping`, `crm-data-contract` | Resolves the account family, the buying committee, role confidence, relationship history, and who to contact first. |
| `industry-analyst` | [industry-analyst](prompts/industry-analyst.prompt.md) | `industry-context`, `opportunity-signal-taxonomy`, `sec-filings-retrieval` | Builds cited "why now" pressure: sub-vertical context, public peer evidence, and what it implies for this account. |
| `market-news-scout` | [market-news-scout](prompts/market-news-scout.prompt.md) | `opportunity-signal-taxonomy`, `sentiment-analysis`, `crm-data-contract` | Sweeps public news across the book and ranks revenue-relevant events as opportunities. |

## Market intelligence

What the account is telling the market, from public disclosure only.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `market-intel-sweep` | [market-intel-sweep](prompts/market-intel-sweep.prompt.md) | `opportunity-signal-taxonomy`, `sentiment-analysis`, `sec-filings-retrieval`, `crm-data-contract` | Orchestrates the filings, calls, and news agents across the whole book, deduplicates, and returns one ranked opportunity brief. |
| `filing-analyst` | [filing-analyst](prompts/filing-analyst.prompt.md) | `sec-filings-retrieval`, `sentiment-analysis`, `opportunity-signal-taxonomy` | Reads annual and quarterly filings for strategy, risk, spend direction, and quarter over quarter change, and extracts buying signals. |
| `earnings-call-analyst` | [earnings-call-analyst](prompts/earnings-call-analyst.prompt.md) | `sentiment-analysis`, `opportunity-signal-taxonomy`, `sec-filings-retrieval` | Analyses earnings call prepared remarks and analyst Q and A for management sentiment, commitments, and hedging. |

## Pipeline and revenue

Keeping the number honest and the pipeline clean.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `pipeline-hygiene` | [pipeline-hygiene](prompts/pipeline-hygiene.prompt.md) | `crm-data-contract`, `discovery-qualification` | Finds stale, mis-staged, and under-evidenced records, and stages every correction for confirmation. |
| `gap-analysis` | [gap-analysis](prompts/gap-analysis.prompt.md) | `crm-data-contract`, `discovery-qualification`, `opportunity-signal-taxonomy` | Maps target to pipeline per bucket, computes the gap and coverage ratio, and ranks an evidence-backed plan to close it. |
| `deal-review` | [deal-review](prompts/deal-review.prompt.md) | `discovery-qualification`, `stakeholder-mapping`, `crm-data-contract` | Inspects one opportunity against a qualification rubric, names the weakest element, and writes the next three actions. |
| `forecast-review` | [forecast-review](prompts/forecast-review.prompt.md) | `discovery-qualification`, `crm-data-contract` | Rolls a team or territory into a call by category, separates evidence from optimism, and lists what would change the call. |
| `renewal-expansion` | [renewal-expansion](prompts/renewal-expansion.prompt.md) | `crm-data-contract`, `opportunity-signal-taxonomy`, `discovery-qualification` | Scores renewal risk and expansion whitespace across the installed base, and produces a dated save-or-grow plan. |

## Prospecting and outreach

Turning a signal into a credible, sourced message that a human sends.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `prospecting-sequence` | [prospecting-sequence](prompts/prospecting-sequence.prompt.md) | `outreach-voice`, `stakeholder-mapping`, `opportunity-signal-taxonomy`, `industry-context` | Builds a multi-touch, multi-channel sequence for cold or lapsed accounts, each touch carrying new information. |
| `outreach-orchestrator` | [outreach-orchestrator](prompts/outreach-orchestrator.prompt.md) | `stakeholder-mapping`, `industry-context`, `solution-messaging`, `outreach-voice`, `opportunity-signal-taxonomy` | Chains who, why now, what, and how into ranked, review-ready drafts. Drafts only, never sends. |
| `motion-strategist` | [motion-strategist](prompts/motion-strategist.prompt.md) | `solution-messaging`, `opportunity-signal-taxonomy`, `stakeholder-mapping` | Maps a signal to the right motion and the executive-level talk track for the level you are writing to. |
| `outreach-writer` | [outreach-writer](prompts/outreach-writer.prompt.md) | `outreach-voice`, `stakeholder-mapping`, `solution-messaging` | Writes short, sourced executive outreach in the runner's own derived voice. |

## Enablement and reporting

Communicating the work: decks, the weekly roll-up, and the portfolio view.

| Agent | Prompt | Skills | What it does |
| --- | --- | --- | --- |
| `enablement-deck` | [enablement-deck](prompts/enablement-deck.prompt.md) | `deck-visual-system`, `solution-messaging`, `industry-context` | Builds a new deck from scratch, grounded in cited sources, with a restrained visual system. |
| `deck-editor` | [deck-editor](prompts/deck-editor.prompt.md) | `deck-visual-system` | Surgically updates an existing deck to reflect source changes while preserving its formatting. |
| `weekly-impact` | [weekly-impact](prompts/weekly-impact.prompt.md) | `crm-data-contract`, `discovery-qualification` | Rolls up the week from every signal source into dated impact entries and the next week's tasks. |
| `portfolio-dashboard` | [portfolio-dashboard](prompts/portfolio-dashboard.prompt.md) | `crm-data-contract`, `opportunity-signal-taxonomy`, `stakeholder-mapping` | Builds or refreshes a multi-tab portfolio and whitespace view across the whole book. |

## Skills library

| Skill | Read by | Contract it owns |
| --- | --- | --- |
| [`crm-data-contract`](skills/crm-data-contract/SKILL.md) | every CRM-touching agent | The logical entity and field names agents may use, and how to map them onto a real CRM. |
| [`discovery-qualification`](skills/discovery-qualification/SKILL.md) | `deal-review`, `gap-analysis`, `pipeline-hygiene`, `forecast-review` | The qualification rubric and what counts as evidence for each element. |
| [`opportunity-signal-taxonomy`](skills/opportunity-signal-taxonomy/SKILL.md) | market intelligence, outreach | The controlled vocabulary of buying signals and what each one implies. |
| [`sentiment-analysis`](skills/sentiment-analysis/SKILL.md) | filings, calls, news | The shared tone rubric, so scores are comparable across sources. |
| [`sec-filings-retrieval`](skills/sec-filings-retrieval/SKILL.md) | filings, calls, industry | How to resolve a company to a public filing and cite it correctly. |
| [`stakeholder-mapping`](skills/stakeholder-mapping/SKILL.md) | account intel, outreach | The stakeholder record shape, role inference, and contact ranking. |
| [`industry-context`](skills/industry-context/SKILL.md) | industry, outreach | Peer evidence thresholds and public-source citation rules. |
| [`solution-messaging`](skills/solution-messaging/SKILL.md) | motion, outreach, decks | Per-motion, per-level framing, proof points, and traps to avoid. |
| [`outreach-voice`](skills/outreach-voice/SKILL.md) | outreach, prospecting | Deriving the runner's voice from their own sent mail, and anti-template rules. |
| [`deck-visual-system`](skills/deck-visual-system/SKILL.md) | decks | Typography, colour, layout, and visual QA. |

## Which agents lead, by role

Every agent works for every role. These are the ones that earn their keep first.
Full adoption paths are in [`docs/roles/`](../docs/roles/).

| Role | Start with | Then add |
| --- | --- | --- |
| [Account Executive](../docs/roles/account-executive.md) | `gap-analysis`, `pipeline-hygiene`, `account-brief` | `deal-review`, `outreach-orchestrator`, `market-intel-sweep` |
| [SDR / BDR](../docs/roles/sdr-bdr.md) | `prospecting-sequence`, `market-news-scout`, `account-intel-360` | `industry-analyst`, `outreach-writer` |
| [Solution Engineer](../docs/roles/solution-engineer.md) | `account-brief`, `enablement-deck`, `weekly-impact` | `deck-editor`, `deal-review` |
| [Solution Specialist](../docs/roles/solution-specialist.md) | `gap-analysis`, `portfolio-dashboard`, `motion-strategist` | `market-intel-sweep`, `outreach-orchestrator` |
| [Customer Success / Account Manager](../docs/roles/customer-success-manager.md) | `renewal-expansion`, `account-brief`, `weekly-impact` | `market-news-scout`, `portfolio-dashboard` |
| [Sales Manager](../docs/roles/sales-manager.md) | `forecast-review`, `pipeline-hygiene`, `gap-analysis` | `deal-review`, `portfolio-dashboard` |
