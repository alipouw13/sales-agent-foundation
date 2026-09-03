# Getting started

Thirty minutes, most of it spent on one file. This walkthrough assumes you have
already cloned the repo and have an agentic assistant that reads
`.github/agents/`.

## 0. Check the prerequisites

You need exactly two things to get value on day one:

1. An assistant that can see this folder's `.github/agents/` and
   `.github/prompts/`.
2. A CRM your assistant can query.

Everything else is optional and additive. See the prerequisites table in
[`../README.md`](../README.md).

Verify the repo itself is intact:

```bash
python tools/validate_repo.py
```

You should see `All checks passed.` If not, something got edited. Fix that
before going further, because the validator is the only thing standing between
this repo and slow drift.

## 1. Find out what your assistant actually has

Before you map anything, ask your assistant:

> List every tool, skill, and MCP server you currently have available. For each,
> say in one line what kind of data it answers questions about.

Write down which ones answer for: your CRM, your mail and calendar and chat,
your notes, web search, and presentations. Those are the five logical sources
this repo uses.

If you have no CRM tool, stop here and solve that first. Every agent that
matters resolves your book from `crm`, and without it there is nothing to
ground on.

## 2. Create your profile

```bash
cp config/profile.example.md config/profile.md    # Windows: copy
```

Open it and fill it in. It is gitignored, so it never leaves your machine.

Work through it in this order, because later answers depend on earlier ones:

| Step | Field | How to decide |
| --- | --- | --- |
| 1 | `sources` | Paste the actual tool names you found in step 1. Anything you do not have, write `unavailable`. Do not guess a name, a wrong name is worse than `unavailable` |
| 2 | `role` | Match on **what you are measured on**, not your job title. See [`roles/README.md`](roles/README.md) |
| 3 | `book_shape` | `named-accounts` if you have a list, `territory` if you own a geography or size band, `vertical` if you own an industry |
| 4 | `targets` | Copy the bucket **names** off your comp plan. Names only. Never put the numbers in this file |
| 5 | `solution_catalog` | Use the product or play names your CRM actually uses, so whitespace math lines up with your opportunity records |
| 6 | `voice` | Leave `derive_from: workplace` if you have a mail source. It reads how you actually write, which beats any style setting |
| 7 | `output_dir` | Leave it as `artifacts/`. It is already gitignored |

Two things people get wrong here:

- **Putting real numbers in `targets`.** Do not. Agents read live figures from
  your CRM at run time, which is the only way they stay correct. A number typed
  into this file is stale the day you type it.
- **Mapping a source you do not really have.** If you map `notes` to a tool that
  cannot search your notes, agents will report "no notes found" as though your
  notes were empty rather than unreachable.

## 3. Pick your role playbook

Open [`roles/`](roles/) and read the file that matches what you are measured on.
Each one names the three agents to start with, in the order that compounds, and
tells you what a good first output looks like.

If your role is not one of the six, read the closest match. The profile and the
guardrails are the same, only the adoption order changes.

## 4. Run your first agent

Run the reusable prompt rather than typing a request from scratch, because the
prompt asks you for the inputs the agent needs.

In VS Code, open the `.prompt.md` file from `.github/prompts/` and run it. In a
CLI host, invoke the agent by name and paste the prompt body.

A good first run is `account-brief` on an account you know well. You will be
able to tell immediately whether the output is true, which is the fastest way to
calibrate trust.

## 5. Read the output critically, once

On your first few runs, do all three of these:

1. **Check the `Gaps` line.** Every agent reports what it could not resolve.
   That is your source mapping telling you where it is thin.
2. **Verify two citations.** Click the URLs. Confirm the dates. External claims
   are supposed to carry a URL, a date, and a verbatim excerpt.
3. **Look for anything confident and unsourced.** If you find one, that is a
   bug in the agent definition, and it is worth fixing in the agent file before
   you run it again.

## 6. Establish a rhythm

Single impressive runs are not the point. Your role playbook has a cadence table
covering daily, weekly, per-deal, monthly, and quarterly. Pick the weekly one
and actually do it for three weeks before adding more agents.

The compounding comes from chaining. Once the first three agents are habitual,
the handoffs listed in your role playbook are where the leverage is.

## Troubleshooting the first run

| Symptom | Almost always |
| --- | --- |
| "I could not resolve your identity" | The `crm` source name in your profile does not match a tool your assistant has |
| Output is generic and mentions no real accounts | Same as above, or your CRM tool cannot filter to your own records |
| "No meeting or note history available" on every account | `workplace` or `notes` is unmapped, or mapped to the wrong tool name |
| Whitespace suggestions do not match your products | `solution_catalog` in your profile does not use the same names as your CRM's product field |
| Numbers look wrong | Check whether the agent labelled the source of each figure. If it did not, the agent file is broken. If it did, follow the label back: the field mapping in `crm-data-contract` is almost certainly pointing at the wrong CRM field |
| Drafts sound nothing like you | `voice.derive_from` is `workplace` but the mail source cannot read your **sent** mail. Switch to `manual` and fill the voice block |
| The agent invented something | Stop using it and open an issue. That is a defect in the agent definition, not a prompt problem |

## Next

- Tailor the rubrics to your company: [`customize.md`](customize.md)
- Add your own agent: [`authoring-agents.md`](authoring-agents.md)
- Understand the source contract: [`data-sources.md`](data-sources.md)
