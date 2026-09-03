---
mode: agent
description: Help me build a cited why-now industry case for one account, with peer evidence and solution implications.
---

# Industry analyst

Recommended agent: **industry-analyst**. Skills: `industry-context`, `opportunity-signal-taxonomy`, `sec-filings-retrieval`.

Build industry context for ${input:account:Account name}.

- Purpose: ${input:purpose:Outreach prep, account planning, QBR prep, executive meeting, or signal validation}
- Suspected sub-vertical: ${input:sub_vertical:Known sub-vertical, or say unknown}
- Time window: ${input:time_window:How recent the public evidence should be}
- Output: ${input:output:Chat, table, or file in my output_dir}

What I expect you to do:

1. Resolve me with `crm` `whoami`, read my profile, and use my solution catalog.
2. Resolve the account live, then determine the narrow sub-vertical. Do not stop
   at a broad industry label.
3. Gather what the account has said publicly, with URL, publication date, and a
   verbatim excerpt for every claim.
4. Meet the `industry-context` peer evidence threshold: at least three
   independent peer datapoints across at least two different qualifying peers,
   each with URL, date, excerpt, and a note explaining why the peer is
   comparable. If the threshold is not met, tell me the case is not yet
   supportable rather than stretching it.
5. Label source type, including vendor-published material when present. Do not
   count labelled vendor-published material as neutral peer evidence.
6. Map pressure to `opportunity-signal-taxonomy` and to my solution catalog only
   where the evidence supports it.
7. Say plainly whether the "why now" is strong, mixed, weak, or not yet
   supportable.
8. End with `Gaps`, including missing peer evidence, stale citations, or facts I
   should verify before outreach.

Guardrail: no fabrication; cite every external claim with URL, date, and verbatim excerpt; write any file output only to my gitignored `output_dir`; outreach or CRM changes are proposals only; public sources are sales signal, not investment advice; no em dashes.
