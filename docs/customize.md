# Customizing this repo for your job

This repo is a starting point that expects to be edited. Fork it, change it, and
keep the guardrails.

There are four levels of customization. Work up from the cheapest, because most
people never need level three.

| Level | What you change | Effort | Blast radius |
| --- | --- | --- | --- |
| 1 | `config/profile.md` | 30 minutes | Everything, tailored to you |
| 2 | A skill in `.github/skills/` | An hour | Every agent that reads it, at once |
| 3 | One agent in `.github/agents/` | An hour | That agent only |
| 4 | A new agent, prompt, and catalog row | Half a day | A new workflow |

---

## Level 1: the profile

Covered in [`getting-started.md`](getting-started.md). Do this first and do not
skip it. Nothing else works properly until the source mapping is right.

Revisit it when: you change role, your comp plan changes, your company adds a
product line, or you gain access to a new data source.

---

## Level 2: the skills, where the leverage is

A skill is a contract that multiple agents read. Editing one changes all of them
consistently, which is exactly what you want, because inconsistent agents cannot
be compared to each other.

### `crm-data-contract`, edit this second

This is the translation layer between your CRM's real schema and what agents
assume. Edit it when:

- Your stage names differ from the canonical model. Map them, do not rename your
  CRM.
- You have custom fields agents should use (a segment field, a play field, a
  renewal date).
- Your staleness thresholds differ. A ninety day enterprise cycle and a
  fourteen day transactional cycle need different numbers, and the defaults in
  the skill are only defaults.
- You operate in multiple currencies. The currency rules matter more than
  anything else in the file.

### `discovery-qualification`, the highest-leverage edit in the repo

If your company already has a qualification method, replace the rubric with
yours. Keep the three-value scoring (evidenced, asserted, unknown) and keep the
rule that a deal scores as its weakest element, because those two are what stop
the rubric from becoming a form-filling exercise.

Changing this file updates `deal-review`, `gap-analysis`, `pipeline-hygiene`,
and `forecast-review` simultaneously, and they stay consistent with each other.
That is the single best hour you can spend in this repo.

### `opportunity-signal-taxonomy`

Add the signals that matter in your industry and delete the ones that do not.
Public sector, financial services, and manufacturing care about visibly
different trigger events. Keep the evidence requirement and the negative-signal
rule.

### `solution-messaging`

Replace the generic motion families with your actual portfolio's motions. This
is the file that most needs your company's language in it. Keep the level
framing contract and the rule that every proof point must be sourced or omitted.

### `sentiment-analysis`, `sec-filings-retrieval`, `industry-context`

These are usually fine as shipped. Edit `sec-filings-retrieval` if your book is
mostly non-US or mostly private companies, because the default path assumes a
US public filer and you will want the fallbacks promoted.

### `outreach-voice`

Add your company's compliance requirements and your own banned phrases. If your
legal team requires specific disclosure language on cold outreach, it goes here,
not in the individual agents.

### `stakeholder-mapping`

Adjust the freshness windows to your sales cycle, and adjust the buying
committee roles if your market has a role this repo does not name (a clinical
sponsor, a regulator liaison, a works council).

### `deck-visual-system`

Replace the generic type and colour system with your employer's approved brand
assets. This skill deliberately ships none. Check your brand policy first,
including on customer logos.

---

## Level 3: editing an agent

Open `.github/agents/<name>.agent.md`. The structure is fixed and the validator
enforces it:

```
## When to activate
## What it resolves (never hardcode)
## Process
## Output
## Guardrails
## Anti-patterns
```

Safe to change freely:

- **`## Process`.** This is the agent's method. Reorder it, add a step, change a
  threshold. Most role-specific customization belongs here.
- **`## Output`.** Change the shape of what you get back.
- **`## When to activate`.** Add the phrases you actually say.

Change carefully:

- **`description:` in the frontmatter.** This is the routing contract. The host
  model sees only this line when deciding whether to call the agent. If you make
  it vague, the agent stops being invoked and you will not know why. Keep the
  trigger phrases in it.
- **`## Anti-patterns`.** These usually encode a real failure someone hit.

Do not remove:

- **`## Guardrails`.** No fabrication, cite per claim, propose never write,
  drafts only, output stays local. Removing one of these is how a helpful agent
  becomes a liability. Tighten them if you like. Do not loosen them.

After any edit:

```bash
python tools/validate_repo.py
```

---

## Level 4: adding an agent

Full guide in [`authoring-agents.md`](authoring-agents.md). Before you start,
apply this test: **if only one agent will ever need this knowledge, it belongs
inside that agent. If two or more will, it belongs in a skill.** Most new-agent
ideas are actually new-skill ideas.

---

## Adapting to a role that is not here

The six role playbooks in [`roles/`](roles/) cover the most common revenue
seats. If yours is not one of them:

1. Read the closest match on **what you are measured on**, not on your title.
2. Keep the profile structure and every guardrail.
3. Change the adoption order and the cadence table, which is the only part that
   is genuinely role-specific.

Worked examples:

| Role | Closest match | What changes |
| --- | --- | --- |
| Revenue operations | Sales manager | `forecast-review` and `pipeline-hygiene` run across the whole org rather than one team, and the output is a data-quality report rather than a coaching plan |
| Partner or channel manager | Account executive | The "account" is a partner, the book is a partner portfolio, and `renewal-expansion` becomes partner-sourced pipeline health |
| Sales leader above first line | Sales manager | `forecast-review` consumes team roll-ups rather than deals, and `portfolio-dashboard` becomes the primary artifact |
| Customer-facing technical lead | Solution engineer | `enablement-deck` and `weekly-impact` matter more, `deal-review` matters less |
| Renewals specialist | Customer success manager | `renewal-expansion` is the whole job, and the cadence tightens to weekly |

---

## Keeping your fork current

If you fork this to your company:

- Keep `tools/validate_repo.py` and the CI workflow. They are what stop customer
  data leaking into a repo that started clean.
- Keep the fork private if anyone will edit skills to include internal method
  names, competitor intelligence, or pricing language.
- Record your level 2 edits in your fork's `SPEC.md` so the next person knows
  which rubrics are yours and which are upstream.
