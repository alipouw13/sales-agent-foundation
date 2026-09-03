---
mode: agent
description: Show me my gap to target by bucket and account, with the arithmetic, evidence, and ranked actions to close it.
---

# Gap analysis

Recommended agent: **gap-analysis**. Skills: `crm-data-contract`, `discovery-qualification`, `opportunity-signal-taxonomy`.

Analyze my gap for ${input:scope:my book, territory, team, account set, or target bucket}.

- Period: ${input:period:fiscal or calendar period}
- Target source: ${input:target_source:"read from crm" or "ask me for the stated target"}
- Coverage benchmark: ${input:coverage_benchmark:coverage ratio benchmark to use, or "state a default and ask me to override"}
- Buckets: ${input:buckets:"use my profile targets" or list bucket names}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve my target buckets by name from my profile, then read actual target
   values from `crm` or ask me. Do not assume a target.
2. Resolve my current book from `crm` and compute each bucket by account.
3. For every bucket, show target, closed to date, remaining target, open weighted
   pipeline, open unweighted pipeline, coverage ratio, and gap.
4. Show arithmetic line by line, label every figure's source, and keep currencies
   and periods separate unless you explicitly convert and say how.
5. Use `discovery-qualification` to decide whether current-period opportunities
   are credible coverage.
6. Rank existing opportunities to accelerate, whitespace to open using
   `opportunity-signal-taxonomy`, and opportunities that should move out of the
   period.
7. State the coverage ratio benchmark you used and tell me to override it with
   my own benchmark.

Guardrail: no fabrication, source every claim, keep sensitive output in my gitignored `output_dir`, and stage `crm` writes for explicit confirmation before applying.
