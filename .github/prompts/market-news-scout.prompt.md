---
mode: agent
description: Run a public news sweep across my book and tell me which account events are worth action.
---

# Market news scout

Recommended agent: **market-news-scout**. Skills: `opportunity-signal-taxonomy`, `sentiment-analysis`, `crm-data-contract`.

Run a market news sweep across ${input:scope:My full book, a named account list, or a segment from my book}.

- Window: ${input:window:News publication window to search}
- Event types: ${input:event_types:Use default revenue-relevant events, or specify a subset}
- Action lens: ${input:action_lens:Pipeline, prospecting, renewal risk, expansion, executive prep, or all}
- Output: ${input:output:Chat digest, table, or file in my output_dir}

What I expect you to do:

1. Resolve me with `crm` `whoami`, read my profile, and resolve the account list
   live this session. Do not use cached territory or account records.
2. Search public `web` news for each account and known aliases within the window.
3. Keep only revenue-relevant events: leadership change, funding, M and A,
   earnings surprise, regulatory action, outage or incident, expansion,
   restructuring, or technology announcement.
4. Classify each surviving event with `opportunity-signal-taxonomy` and score
   tone with `sentiment-analysis` so results are comparable.
5. Deduplicate the same event reported by multiple outlets and choose the
   strongest primary source.
6. Rank actionability for me based on my solution catalog, open pipeline or
   account context, timing, and evidence quality.
7. Handle negative signals with care. Explain the changed motion and what not to
   say.
8. List accounts with no material news in the window instead of padding with weak
   mentions.
9. End with `Gaps`, including unmapped sources, ambiguous aliases, excluded weak
   hits, and accounts needing manual verification.

Guardrail: no fabrication; cite every external claim with URL, date, and verbatim excerpt; write any file output only to my gitignored `output_dir`; outreach or CRM changes are proposals only; public sources are sales signal, not investment advice; no em dashes.
