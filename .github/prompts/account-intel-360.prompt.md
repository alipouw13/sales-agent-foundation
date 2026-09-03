---
mode: agent
description: Help me understand an account family, its buying committee, the deal team, and who I should contact first.
---

# Account intel 360

Recommended agent: **account-intel-360**. Skills: `stakeholder-mapping`, `crm-data-contract`.

Build account intelligence for ${input:account:Account or account family name}.

- Purpose: ${input:purpose:Why you need it, for example stakeholder map, QBR prep, economic buyer search, or deal team planning}
- Scope: ${input:scope:One entity, full family, or let the agent resolve the right boundary}
- Freshness window: ${input:freshness_window:How far back to treat relationship activity as fresh}
- Output: ${input:output:Chat, table, or file in my output_dir}

What I expect you to do:

1. Resolve me with `crm` `whoami`, read my profile, and resolve the account live
   this session. Do not reuse a record, contact, or account family from memory.
2. Disambiguate parent, subsidiary, sibling, duplicate, and inactive account
   records. State the primary entity and why you chose it.
3. Build the buying committee from `crm`, `workplace`, and `notes` where mapped.
   Infer roles per `stakeholder-mapping`, with role confidence and evidence.
4. Map the internal deal team, including who owns account strategy, opportunity
   execution, technical validation, commercial process, executive coverage, and
   next action.
5. Summarize open pipeline across the resolved family, not only the account name
   I typed.
6. Rank who I should contact first and explain why each ranked contact matters
   now.
7. End with `Gaps`, including unmapped sources, ambiguous records, stale
   relationships, and facts I should verify before outreach.

Guardrail: no fabrication; cite every external claim with URL, date, and verbatim excerpt; write any file output only to my gitignored `output_dir`; outreach or CRM changes are proposals only; public sources are sales signal, not investment advice; no em dashes.
