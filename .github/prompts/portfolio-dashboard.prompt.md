---
mode: agent
description: Build or refresh my portfolio dashboard with overview, whitespace, stakeholder coverage, market signals, and movement.
---

# Portfolio dashboard

Recommended agent: **portfolio-dashboard**. Skills: `crm-data-contract`, `opportunity-signal-taxonomy`, `stakeholder-mapping`.

Build or refresh my portfolio dashboard for ${input:book_scope:Whole book, territory, named-account list, or filtered segment}.

- Target buckets: ${input:target_buckets:Bucket names to show, or use profile targets}
- Solution catalog: ${input:solution_catalog:Use profile solution_catalog or provide catalog source}
- Refresh mode: ${input:refresh_mode:New baseline or compare to prior refresh}
- Prior dashboard: ${input:prior_dashboard:Prior output_dir artifact or none}
- Market signal source: ${input:market_signals:Use prior market-intel artifact, fresh web evidence, or unavailable}
- Output format: ${input:output:Local dashboard format supported by the host}
- Focus questions: ${input:focus:Specific management or planning questions to answer}

What I expect you to do:

1. Resolve my identity, book, fiscal period, target bucket names, mapped sources,
   profile `solution_catalog`, and profile `output_dir`.
2. Pull the account universe and record movement from `crm`. Stop if `crm` is
   unavailable.
3. Show arithmetic for every computed figure: included records, excluded records,
   date window, bucket filter, and source.
4. Create tabs for portfolio overview, whitespace, stakeholder coverage, market
   signals, and movement since last refresh.
5. Leave any unknown target blank and label it unknown. Do not infer a target from
   pipeline, coverage, or prior output.
6. Include whitespace only when each gap has credible evidence, not just because a
   solution is missing from the catalog.
7. Flag accounts with no identified economic buyer, no recent executive contact,
   cold relationships, or low role confidence.
8. Save the dashboard and methodology note to my profile `output_dir`, then run
   QA for broken links, empty tabs, missing source labels, and figures without
   arithmetic.
9. End with prioritized next actions and a `Gaps` line naming unavailable sources
   and unsupported calculations.

No fabricated accounts, targets, contacts, roles, figures, market signals, or whitespace reasons. Any file output goes to my profile `output_dir`, which is gitignored, and is never committed. Read only against `crm`. No em dashes.
