# Data sources

Agents in this repo never name a vendor tool. They name a **logical source**.
You map logical sources to the tools you actually have, in the `sources:` block
of `config/profile.md`.

That indirection is the whole portability story. The same `account-brief` agent
works for someone on Salesforce and someone on Dynamics, because it only ever
asks for "the `crm` source".

The full contract, with the capability list each source must satisfy and three
worked mappings, is in
[`../config/data-sources.example.md`](../config/data-sources.example.md). This
page covers how to wire yours and what breaks when you do not.

## The five logical sources

| Source | Required | Answers | Without it |
| --- | --- | --- | --- |
| `crm` | **Yes** | Accounts, opportunities, contacts, deal team, activities, targets | Nothing works. Every agent resolves the book from here |
| `workplace` | No | Mail, calendar, chat, meetings, colleagues | No relationship history, no voice derivation, weekly roll-ups see only CRM movement |
| `notes` | No | Your own prior thinking | Briefs lose your context, and agents say so |
| `web` | No | Public filings, transcripts, news | The whole market intelligence group is unavailable |
| `decks` | No | Reading and writing presentations | `enablement-deck` and `deck-editor` are unavailable |

Only `crm` is fatal. Everything else degrades: the agent says the source is
unavailable in that section and continues with what it has. That behaviour is
required by `SPEC.md` section 8 and is the reason a partial setup is still
worth having.

## Mapping yours

1. Ask your assistant to list every tool it has and what each one answers for.
2. Fill in the `sources:` block. Use the exact tool name your assistant reports.
3. Anything you do not have, write `unavailable`. Do not guess.

```yaml
sources:
  crm: "<exact tool name>"
  workplace: "<exact tool name, or unavailable>"
  notes: "<exact tool name, or unavailable>"
  web: "built-in web search"
  decks: "<exact tool name, or unavailable>"
```

**A wrong name is worse than `unavailable`.** With `unavailable`, the agent
tells you the source is not configured. With a wrong name, the tool call fails
or returns nothing and the agent may report "no history found", which reads like
an empty account rather than a broken mapping.

## Mapping your CRM properly

Naming the tool is the easy half. The hard half is the schema, and it is where
confidently wrong numbers come from.

Read the [`crm-data-contract`](../.github/skills/crm-data-contract/SKILL.md)
skill. It defines the logical entities and fields agents assume, and how to map
an arbitrary CRM onto them. Pay particular attention to:

- **Stage mapping.** Your CRM's stage list maps onto a small canonical model.
  Map it, do not rename your CRM. Custom stages need an explicit decision.
- **Staleness thresholds.** The defaults assume a particular cycle length.
  Yours are probably different. Override them.
- **Currency.** Never sum across currencies silently. If your book is
  multi-currency, this is the section that matters most.
- **What "my book" means.** It differs by `book_shape`. Named accounts, a
  territory, and a vertical resolve differently.

If a mapping is ambiguous, the contract says the agent asks rather than guesses.
Keep that rule. A wrong field mapping produces output that looks right.

## What agents may and may not do to a source

| | Read | Write |
| --- | --- | --- |
| `crm` | Freely | **Propose only.** Every change is staged as a table (record, field, current value, proposed value, reason) and applied only after you confirm |
| `workplace` | Freely | Never. No agent sends mail, posts a message, or creates a calendar event |
| `notes` | Freely | Append only, to a dated section, and only when you asked for it |
| `web` | Freely, public sources only | Never |
| `decks` | Freely | Creates and edits files in your `output_dir` |

Outreach agents produce **drafts**. They do not send, do not schedule a send,
and do not mark a contact as touched. Sending stays a human action in your own
client. That is a guardrail, not a limitation to work around.

## Access and authentication

Every source above is something **you already have access to as a human**. This
repo:

- Holds no credentials.
- Performs no authentication.
- Creates no new access.
- Adds no dependency.

Agents ask a tool your assistant already has, under your own identity, with your
own permissions. If a workflow appears to need a new credential, the correct
answer is "which existing tool already covers this", not "add auth here". That
rule is in [`../.github/copilot-instructions.md`](../.github/copilot-instructions.md)
and it is the reason this repo is safe to fork.

Before pointing an agent at production systems, check your employer's policy on
automated access to CRM and workplace data. See [`../SECURITY.md`](../SECURITY.md).

## Adding a sixth source

Do not, unless you are sure. Every logical source you add is a name every agent
has to know about, and the five here cover the workflows in the catalog.

If you genuinely need one (a support ticketing system and a product telemetry
source are the two most defensible additions):

1. Update `SPEC.md` section 2 and the source table in
   `config/data-sources.example.md` with its capability contract.
2. Add it to the `sources:` block in `config/profile.example.md`.
3. Update only the agents that need it, and make them degrade gracefully when it
   is `unavailable`.
4. Update this page and the copilot instructions.
5. Run `python tools/validate_repo.py`.
