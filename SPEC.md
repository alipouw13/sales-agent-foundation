# SPEC: sales-agent-foundation

A reference implementation of a **team of agents** for a revenue role. It ships
no application code and no credentials. It ships the durable part: the agent
definitions, the reusable prompts, the shared skills, the project rules, and the
validation that keeps all of it honest.

Version: 1.0.0

---

## 1. Purpose

Anyone in a revenue role (Account Executive, SDR/BDR, Solution Engineer,
Solution Specialist, Customer Success or Account Manager, Sales Manager) should
be able to clone this repo, spend thirty minutes filling in one profile file,
and have a working set of agents that use *their* CRM, *their* book, and *their*
voice.

Non-goals, explicitly:

- It is not a product, a service, or a runtime. There is nothing to deploy.
- It does not ship data, customer names, quotas, or contacts.
- It does not authenticate to anything. Agents route to tools the host already
  has (MCP servers, skills, plugins).
- It is not tied to one CRM. The CRM contract is a mapping file you fill in.

## 2. Definitions

| Term | Meaning in this repo |
| --- | --- |
| **Agent** | A markdown persona in `.github/agents/<name>.agent.md`. Prose only. Defines when to activate, what it resolves, its process, its output, and its guardrails. |
| **Prompt** | A reusable, parameterized request in `.github/prompts/<name>.prompt.md`. The user-facing front door to an agent. |
| **Skill** | A shared playbook in `.github/skills/<name>/SKILL.md`. Reference material multiple agents cite: rubrics, taxonomies, formatting contracts. |
| **Runner** | The human running an agent. Every agent resolves the runner's identity, book, and role at run time. Nothing is hardcoded. |
| **Data source** | A tool the host already provides: a CRM MCP server, a workplace-data skill, a notes server, a deck skill. Declared in `config/data-sources.example.md`. |
| **Profile** | `config/profile.example.md`, copied to `config/profile.md` (gitignored). The runner's role, book shape, quota buckets, tone, and source mapping. |

## 3. Repository contract

```
.github/
  copilot-instructions.md     project rules the assistant must follow
  AGENT-CATALOG.md            the single source of truth for the agent list
  agents/*.agent.md           agent personas
  prompts/*.prompt.md         reusable prompts
  skills/<name>/SKILL.md      shared playbooks
  workflows/validate.yml      CI: runs the validator
config/
  profile.example.md          the runner profile template
  data-sources.example.md     tool/MCP mapping template
docs/
  getting-started.md          prerequisites and first run
  customize.md                how to tailor the repo to your job
  authoring-agents.md         how to add or change an agent
  data-sources.md             how to wire your own CRM and workplace data
  roles/<role>.md             per-role adoption playbooks
examples/
  worked-chain.md             an illustrative end-to-end chain, placeholders only
tools/
  validate_repo.py            the validator, Python stdlib only
```

## 4. File contracts

### 4.1 Agent

Path: `.github/agents/<name>.agent.md`, where `<name>` is lower kebab-case.

```markdown
---
name: <name>                       # MUST equal the filename stem
description: <one sentence, third person, includes trigger phrases>
---

> **Writing rule:** ... (the shared writing rule block)

You are the **<name>** agent...

## When to activate
## What it resolves (never hardcode)
## Process
## Output
## Guardrails
## Anti-patterns
```

Rules:

1. Frontmatter MUST contain `name` and `description`. `name` MUST equal the
   filename stem.
2. `description` MUST be a single line, third person, and MUST name the
   situations that should route to it. The host model uses only this text to
   decide when to call the agent, so write it as if the reader has never seen
   the file.
3. The six `##` sections above are mandatory and MUST appear in that order.
4. An agent MUST NOT name a real customer, person, email address, quota, or
   revenue number.
5. An agent MUST state which data sources it reads, using the logical names from
   `config/data-sources.example.md` (`crm`, `workplace`, `notes`, `web`,
   `decks`), never a vendor-specific tool name in the body.
6. Every non-lifecycle agent MUST have a matching prompt of the same stem.

### 4.2 Prompt

Path: `.github/prompts/<name>.prompt.md`, stem MUST match an agent.

```markdown
---
mode: agent
description: <one sentence, first person, what the runner wants>
---

# <Title>

Recommended agent: **<name>**. Skills: `<skill>`, `<skill>`.

<body, using ${input:key:hint} for every variable>
```

Rules:

1. Frontmatter MUST contain `mode: agent` and `description`.
2. The body MUST name the recommended agent in bold on its own line.
3. Every runner-supplied value MUST use `${input:key:hint}` so the prompt is
   reusable, never a hardcoded account or number.
4. The body MUST end with the guardrail line for that workflow (no fabrication,
   output stays local, drafts only where applicable).

### 4.3 Skill

Path: `.github/skills/<name>/SKILL.md`, directory name MUST equal `name`.

```markdown
---
name: <name>                       # MUST equal the directory name
description: <one sentence, includes the trigger keywords>
---

# <Title>
...
```

Rules:

1. Skills are prose. A skill MUST NOT require a dependency, a credential, or a
   network call to be useful.
2. A skill is shared reference. If only one agent will ever read it, it belongs
   in the agent.
3. Any scoring rubric, taxonomy, or output schema used by more than one agent
   MUST live in a skill so the agents stay comparable.

## 5. Guardrails every agent inherits

These are non-negotiable and are asserted by the validator where mechanically
checkable, and by the `validate` and `code-reviewer` agents otherwise.

1. **No fabrication.** If a source returns nothing, the agent says so. Never
   invent a person, title, email address, quota, revenue figure, attainment
   percentage, customer quote, or proof point.
2. **Cite the source per claim.** External claims carry a URL plus a date plus a
   verbatim excerpt. Internal claims name the record they came from.
3. **Portable, never hardcoded.** Identity, book, role, and targets are resolved
   at run time from the runner's own seat. No account name, record ID, or
   territory is carried from a previous run.
4. **Sensitive output stays local.** Anything that blends customer data with the
   runner's book is written to a gitignored path and is never committed.
5. **Drafts only.** Outreach agents produce drafts. Sending is a human action in
   the human's own mail client.
6. **Propose, do not silently write.** Any CRM write is staged and shown for
   confirmation first.
7. **No new authentication.** If a workflow appears to need a new credential,
   the answer is to ask which existing tool already covers it.
8. **Public sources are public.** Filings, transcripts, and news come from public
   endpoints, are attributed, and are treated as sales signal, not investment
   advice.
9. **No em dashes or en dashes** anywhere in the repo.

## 6. The agent team

Groups, and what each group is for. The authoritative list, with prompts and
skills, is `.github/AGENT-CATALOG.md`; the validator asserts the two agree.

| Group | Agents | Purpose |
| --- | --- | --- |
| Lifecycle | `spec`, `plan`, `build`, `validate`, `code-reviewer` | How changes to this repo get made: spec, plan, build, validate, review. |
| Account intelligence | `account-brief`, `account-intel-360`, `industry-analyst`, `market-news-scout` | Who the account is, who to talk to, and why now. |
| Market intelligence | `market-intel-sweep`, `filing-analyst`, `earnings-call-analyst` | What the account is telling the market, from public disclosure. |
| Pipeline and revenue | `pipeline-hygiene`, `gap-analysis`, `deal-review`, `forecast-review`, `renewal-expansion` | Keeping the number honest and the pipeline clean. |
| Prospecting and outreach | `prospecting-sequence`, `outreach-orchestrator`, `motion-strategist`, `outreach-writer` | Turning a signal into a credible, sourced, human-sent message. |
| Enablement and reporting | `enablement-deck`, `deck-editor`, `weekly-impact`, `portfolio-dashboard` | Communicating the work: decks, weekly roll-up, portfolio view. |

## 7. Skills library

| Skill | Used by | Contract it owns |
| --- | --- | --- |
| `crm-data-contract` | every CRM-touching agent | The logical entity and field names agents may use, and how to map them to a real CRM. |
| `discovery-qualification` | `deal-review`, `gap-analysis`, `pipeline-hygiene`, `forecast-review` | The qualification rubric (MEDDPICC-style) and what counts as evidence per element. |
| `opportunity-signal-taxonomy` | market intelligence, outreach | The controlled vocabulary of buying signals and what each maps to. |
| `sentiment-analysis` | `filing-analyst`, `earnings-call-analyst`, `market-news-scout` | The shared 1 to 5 tone rubric so scores are comparable across sources. |
| `sec-filings-retrieval` | `filing-analyst`, `earnings-call-analyst`, `industry-analyst` | How to resolve a company to a public filing and cite it. |
| `stakeholder-mapping` | `account-intel-360`, outreach | The stakeholder record shape, role inference, and contact ranking. |
| `industry-context` | `industry-analyst`, outreach | Peer evidence thresholds and public-source citation rules. |
| `solution-messaging` | `motion-strategist`, outreach, `enablement-deck` | Per-motion, per-level executive framing, proof points, and traps. |
| `outreach-voice` | `outreach-writer`, `prospecting-sequence` | Voice derivation from the runner's own sent mail, and anti-template rules. |
| `deck-visual-system` | `enablement-deck`, `deck-editor` | Typography, colour, layout, and visual QA for decks. |

## 8. Configuration contract

`config/profile.example.md` is copied to `config/profile.md` (gitignored) and
declares:

| Key | Meaning |
| --- | --- |
| `role` | One of the roles in `docs/roles/`. Drives which agents lead. |
| `segment` | Enterprise, commercial, SMB, public sector. Changes tone and cycle assumptions. |
| `book_shape` | Named-account, territory, or vertical. Changes how the book is resolved. |
| `targets` | The quota buckets the runner is measured on, by name only. Never actual numbers in a committed file. |
| `solution_catalog` | The list of plays/products the runner sells, used to compute whitespace. |
| `sources` | Logical source to actual tool mapping (see `config/data-sources.example.md`). |
| `voice` | Tone constraints for drafts. |
| `output_dir` | Where generated artifacts go. Must be a gitignored path. |

Agents MUST degrade gracefully: if a source is unmapped, the agent says the
source is unavailable and continues with what it has, rather than failing or
inventing.

## 9. Validation contract

`python tools/validate_repo.py` exits non-zero on any violation. It is the
verification step for every change and runs in CI on push and pull request.

Checks:

| # | Check | Failure mode |
| --- | --- | --- |
| 1 | Agent frontmatter present, `name` matches filename stem | error |
| 2 | Agent `description` present, single line, at least 40 characters | error |
| 3 | Required agent sections present and in order | error |
| 4 | Prompt frontmatter present with `mode: agent` and `description` | error |
| 5 | Agent to prompt parity, both directions, lifecycle agents exempt | error |
| 6 | Prompt names the recommended agent, and that agent exists | error |
| 7 | Skill frontmatter present, `name` matches directory name | error |
| 8 | Every agent appears in `AGENT-CATALOG.md`, every catalog row exists on disk | error |
| 9 | Every catalog skill reference exists on disk | error |
| 10 | No em dash (U+2014) or en dash (U+2013) in any tracked text file | error |
| 11 | Relative markdown links resolve to an existing path | error |
| 12 | No email address outside a placeholder domain (including obfuscated forms), no GUID or long hex string, no credential pattern (assignment, bearer, PEM, JWT, connection string, vendor token prefix), including a credential split across a line break | error |
| 13 | Every skill referenced by an agent or prompt exists | error |
| 14 | `SPEC.md` section 6 and `AGENT-CATALOG.md` name the same agents | error |
| 15 | Agent `description` is third person, not imperative and not first person outside quoted trigger phrases | error |
| 16 | No file over 60 KB in `.github/` (keeps agents readable and cheap) | warning |

Notes on scope:

- Files are enumerated from `git ls-files`, falling back to a full tree walk
  when the index is empty or git is unavailable. An empty file list is never
  treated as a pass.
- Every text file is scanned regardless of extension. Only known binary formats
  are skipped, so a new file type is checked by default.
- Required section headings inside fenced code blocks do not count, so an
  example cannot satisfy the structural contract.
- The validator does not exempt itself.

What the validator **cannot** check, and therefore what review must catch:

- A customer or person's name written as ordinary prose. No pattern
  distinguishes a real account name from an illustrative one.
- A phone number, a street address, or any other identifier that looks like
  ordinary text.
- A real revenue, quota, or attainment figure. A number is just a number.
- A credential deliberately obfuscated beyond the patterns above, or split
  across more than two lines.
- Whether an agent's process actually contradicts its own guardrails.

Check 12 catches structured identifiers, not natural language. That gap is the
reason the `code-reviewer` agent reads every diff, and the reason
`CONTRIBUTING.md` puts the burden for customer data on the contributor. Treat a
green validator as "the structure is intact", never as "this is safe to
publish".

## 10. Definition of done for a change

1. `SPEC.md` updated if the contract moved.
2. `python tools/validate_repo.py` passes with zero errors.
3. The `validate` agent has re-checked the work against the original request and
   this spec.
4. The `code-reviewer` agent has read the diff.
5. No customer data, no credentials, no personal identifiers added.
