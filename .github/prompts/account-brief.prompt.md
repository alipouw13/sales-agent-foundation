---
mode: agent
description: Give me a grounded 360 or pre-meeting brief on one account from my book, with every claim traced to a source.
---

# Account brief

Recommended agent: **account-brief**. Skills: `crm-data-contract`, `stakeholder-mapping`.

Brief me on ${input:account:Account name}.

- Purpose: ${input:purpose:Why you need it, for example "first meeting tomorrow", "QBR prep", "who owns what"}
- Depth: ${input:depth:"ninety second read" or "full 360"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve me with `crm` `whoami`, then resolve the account live this session.
   Do not reuse an account, a record ID, or a relationship from a prior run.
2. State up front what you resolved: entity covered, open opportunity count,
   internal team size, and which of my sources actually answered.
3. Build each section from a real source and name the source in the section:
   - History and context from `workplace` activity plus my `notes`, with dates.
   - Open opportunities from `crm`, with stage, amount, close date, last
     activity, and a link to each record. Flag stale and past-due records.
   - Whitespace against the `solution_catalog` in my profile, with one piece of
     evidence per gap.
   - Stakeholders ranked per `stakeholder-mapping`, with inferred role, role
     confidence, and last contact date. Mark anyone cold past ninety days.
   - Exactly one next step I can take today.
4. End with a `Gaps` line naming what you could not resolve and why.

If a source is unmapped or returns nothing, say so plainly in that section. No
fabricated history, contacts, titles, or numbers. Read only, never write to my
CRM. Any file output goes to my `output_dir`, which is gitignored. No em dashes.
