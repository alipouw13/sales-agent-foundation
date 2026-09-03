---
mode: agent
description: Run a full public market intelligence sweep across my book and return one ranked opportunity brief.
---

# Market intel sweep

Recommended agent: **market-intel-sweep**. Skills: `opportunity-signal-taxonomy`, `sentiment-analysis`, `sec-filings-retrieval`, `crm-data-contract`.

Run a market intelligence sweep for ${input:scope:my whole book, a segment, or a named subset}.

- Lookback window: ${input:lookback:date range or disclosure cycle to cover}
- Priority lens: ${input:priority:target bucket, solution catalog focus, or territory priority}
- Output: ${input:output:"chat" or "file in my output_dir"}
- Depth: ${input:depth:"executive brief" or "detailed evidence pack"}

What I expect you to do:

1. Resolve me and my current book from `crm`, then state the account count,
   source coverage, and date window before analysis.
2. For each account, collect public filing, earnings call, and news signals when
   available. Use public sources only.
3. Merge duplicate signals that describe the same underlying event. Keep every
   citation attached to the merged signal.
4. Reconcile conflicting sentiment scores by explaining the divergence. Do not
   average away disagreement between filings, calls, and news.
5. Cross-reference each merged signal against `crm` so open-pipeline matches
   become coaching notes and unmatched signals become whitespace.
6. Rank the final list by actionability for my role, solution catalog, target
   buckets, recency, evidence strength, and stakeholder clarity.
7. Include accounts that returned no relevant signal and state what was not
   covered, including private companies, accounts with no public disclosure,
   unresolved non-US filers, and source gaps.

No fabrication. Cite every external claim with URL, date, and verbatim excerpt. Any output that blends public signal with my book stays in my gitignored output_dir. Propose, never silently write to crm. This is sales signal detection, not investment advice. No em dashes.
