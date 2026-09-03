# Authoring an agent

Read [`../SPEC.md`](../SPEC.md) section 4 first. It holds the contracts. This
page is the practical walkthrough.

Before you write anything, apply the test that saves the most time:

> If only one agent will ever need this knowledge, it belongs inside that agent.
> If two or more will, it belongs in a **skill**.

Most new-agent ideas are actually new-skill ideas, or a `## Process` edit to an
agent that already exists.

## The lifecycle

Follow it. It is short and it catches the expensive mistakes early.

1. **Spec.** If you are adding a group or changing a contract, update `SPEC.md`
   first. Run the `spec` agent if the scope is fuzzy.
2. **Plan.** List the files you will touch and the verification step, before you
   edit. Run the `plan` agent.
3. **Build.** One file at a time. Run the validator after each.
4. **Validate.** Run the `validate` agent against the original request.
5. **Review.** Run the `code-reviewer` agent over the diff.
6. **Ship.** One focused commit.

## Step 1: the agent file

Create `.github/agents/<name>.agent.md`. Lower kebab-case, and the stem must
match the frontmatter `name`.

```markdown
---
name: deal-review
description: Inspect one opportunity against the qualification rubric, name the weakest element, and write the next three actions. Use for "review this deal", "is this deal real", "what am I missing on <opportunity>", "deal inspection", "should I forecast this".
---

> **Writing rule:** never use an em dash (U+2014) or an en dash (U+2013). Use a
> comma, a colon, parentheses, or a second sentence.

You are the **deal-review** agent. <one or two paragraphs on what it does and,
more importantly, what it refuses to do>

## When to activate
## What it resolves (never hardcode)
## Process
## Output
## Guardrails
## Anti-patterns
```

All six sections, in that order. The validator checks it.

### The description is the routing contract

This is the part people get wrong. The host model sees **only** the
`description` line when deciding whether to invoke your agent. It has not read
the body.

So write it as if the reader has never seen the file, and put the phrases a
human would actually say into it.

| | |
| --- | --- |
| Bad | `description: Helps with deals.` |
| Bad | `description: A sophisticated multi-step agent leveraging qualification methodology.` |
| Good | `description: Inspect one opportunity against the qualification rubric, name the weakest element, and write the next three actions. Use for "review this deal", "is this deal real", "what am I missing on <opportunity>".` |

The good one is third person, says what it produces, and contains the literal
phrases that should route to it.

### Writing each section

**`## When to activate`.** Four to six bullets of things a person actually says,
plus the situations where it should fire even if nobody asks (before a forecast
call, before a first meeting).

**`## What it resolves (never hardcode)`.** Numbered. What the agent looks up
live, every run: the runner's identity, the record in question, which sources
are mapped. State explicitly that nothing carries over from a prior run. This
section is what makes the agent portable, so a teammate running it gets their
own data.

**`## Process`.** The method, numbered. Be specific about thresholds, ordering,
and what to do when a step returns nothing. This is the section you will edit
most often, and it is where your company's way of working goes.

**`## Output`.** The shape of what comes back, including a `Gaps` line naming
what could not be resolved. Every agent reports its own blind spots.

**`## Guardrails`.** Restate the inherited guardrails, adapted to this agent.
Not a copy-paste, adapted. `deal-review` needs "read only, never writes to
`crm`". `outreach-writer` needs "drafts only, never sends". Both need "no
fabrication".

**`## Anti-patterns`.** The failure modes. Write these from real failures, not
imagined ones. They are the most useful section when someone edits the agent
later.

### Logical sources, not vendor names

Agents name `crm`, `workplace`, `notes`, `web`, and `decks`. Never a product
name. This is what lets the same agent work for someone on Salesforce and
someone on Dynamics.

Vendor names are allowed in `docs/` and in `config/*.example.md` as worked
examples, and inside the `crm-data-contract` skill, which is explicitly the
mapping layer.

## Step 2: the prompt file

Create `.github/prompts/<name>.prompt.md`. Same stem.

```markdown
---
mode: agent
description: Review one of my opportunities against the qualification rubric and tell me what is actually missing.
---

# Deal review

Recommended agent: **deal-review**. Skills: `discovery-qualification`, `stakeholder-mapping`.

Review ${input:opportunity:Opportunity name or record}.

- Context: ${input:context:Why now, for example "forecast call tomorrow"}
- Depth: ${input:depth:"quick check" or "full inspection"}

<what you expect it to do, numbered>

<the guardrail line for this workflow>
```

Rules the validator enforces: `mode: agent` and a `description` in frontmatter,
a `Recommended agent: **<name>**.` line whose name matches the stem and exists,
and every skill you cite must exist as a directory.

Every runner-supplied value uses `${input:key:hint}`. A prompt with a hardcoded
account name is not reusable, it is a one-off request.

The prompt is written in **first person** (what the runner wants). The agent is
written in **third person** (what it does). That split is deliberate: one is the
request, the other is the contract.

## Step 3: the catalog

Add a row to [`../.github/AGENT-CATALOG.md`](../.github/AGENT-CATALOG.md) in the
right group, with the prompt link and the skills it reads. The validator asserts
that every agent appears here and every agent named here exists.

If the agent belongs to a new group, update `SPEC.md` section 6 as well.

## Step 4: validate

```bash
python tools/validate_repo.py
```

Zero errors. The checks are listed in `SPEC.md` section 9. The ones that catch
new agents most often:

| Error | Cause |
| --- | --- |
| `agent-frontmatter` | `name` does not match the filename stem |
| `agent-description` | Description under 40 characters, so it cannot route |
| `agent-sections` | A section missing, or out of order |
| `agent-prompt-parity` | You wrote the agent and forgot the prompt |
| `prompt-agent-link` | The `Recommended agent:` line does not match the stem |
| `catalog` | You forgot the catalog row |
| `skill-reference` | You cited a skill that does not exist |
| `dashes` | An em dash slipped in |
| `links` | A relative link to a file that is not there |
| `pii` | An email address or a GUID in your example text |

## Step 5: run it for real

Validation proves the file is well formed. It cannot prove the agent is any
good. Run it end to end in a real session, against real data, before you commit.

Specifically check:

1. Did it resolve the runner and the record live, or did it assume something?
2. Does every claim carry a source?
3. Does the `Gaps` line honestly report what was missing?
4. When you deliberately unmap a source, does it degrade gracefully instead of
   inventing?

That last one is the test most new agents fail.

## Authoring a skill instead

1. `.github/skills/<name>/SKILL.md`, frontmatter `name` matching the directory.
2. The `description` must carry the trigger keywords, because that is how a
   skill gets loaded.
3. Write it as a **contract**, not an essay. Another agent has to apply it
   identically without asking you questions. Define every term, every score,
   every threshold.
4. Prose only. No dependency, no credential, no network call required.
5. Add it to the skills table in the catalog, and cite it from the agents that
   read it.
