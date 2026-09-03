---
mode: agent
description: Read a public filing for an account and show me what changed, what matters, and which sales signals are supported.
---

# Filing analyst

Recommended agent: **filing-analyst**. Skills: `sec-filings-retrieval`, `sentiment-analysis`, `opportunity-signal-taxonomy`.

Analyze filings for ${input:account:Account or filer name}.

- Filing scope: ${input:filing_scope:"latest annual", "latest quarterly", "current report", or "specific period"}
- Comparison: ${input:comparison:"prior quarter", "prior year", or specific comparison period}
- Jurisdiction hint: ${input:jurisdiction:"US", "non-US", or "unknown"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve the right filer entity and the exact document before analysis. State
   the filing type, fiscal period, filing date, URL, and comparison filing.
2. For US filers, handle 10-K, 10-Q, and 8-K. For non-US filers, find the
   equivalent annual, interim, or current disclosure instead of failing on form
   name differences.
3. Extract stated strategy, risk factor changes, MD and A spend direction,
   technology and transformation commitments, capital allocation language, and
   new disclosures.
4. Compare quarter over quarter and year over year where the documents support
   it. Mark missing comparison documents as gaps.
5. Distinguish boilerplate from signal. Elevate newly added or materially changed
   risk language above persistent language.
6. Score management tone with `sentiment-analysis` and map every finding to
   `opportunity-signal-taxonomy`.
7. Quote numbers exactly as written, including units, period, and basis.

No fabrication. Cite every finding with filing type, filing date, section, URL, access date, and verbatim excerpt. Any output blended with my book stays in my gitignored output_dir. Propose, never silently write to crm. This is sales signal detection, not investment advice. No em dashes.
