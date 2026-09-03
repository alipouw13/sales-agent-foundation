---
mode: agent
description: Analyze a public earnings call transcript for me, covering prepared remarks, Q and A, tone shift, and sales signals.
---

# Earnings call analyst

Recommended agent: **earnings-call-analyst**. Skills: `sentiment-analysis`, `opportunity-signal-taxonomy`, `sec-filings-retrieval`.

Analyze the earnings call for ${input:account:Account or public company name}.

- Fiscal period: ${input:fiscal_period:Fiscal quarter or year to analyze}
- Comparison call: ${input:comparison_call:"prior comparable call" or specific period}
- Focus: ${input:focus:strategy, guidance, technology, risk, cost actions, or all}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve the exact public transcript before analysis. State the company,
   fiscal period, call date, transcript URL, source, and comparison call.
2. Treat prepared remarks and analyst Q and A as different evidence classes.
   Label every finding by segment.
3. Track stated priorities and their ordering, explicit commitments with
   timelines, hedging language, non-answers, repeated analyst pressure points,
   guidance changes, and tone shift versus the prior call.
4. Attribute excerpts by speaker role only, such as CEO, CFO, other officer,
   analyst, or operator. Do not use personal names.
5. Score tone with `sentiment-analysis` and map every supported finding to
   `opportunity-signal-taxonomy`.
6. Explain the delta between prepared remarks and Q and A, even if the answer is
   that no material divergence was found.
7. Quote numbers exactly as written, including units, period, and basis.

No fabrication. Cite every finding with transcript URL, call date, access date, segment, speaker role, and verbatim excerpt. Any output blended with my book stays in my gitignored output_dir. Propose, never silently write to crm. This is sales signal detection, not investment advice. No em dashes.
