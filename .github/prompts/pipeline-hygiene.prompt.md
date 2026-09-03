---
mode: agent
description: Clean my pipeline by finding stale, wrong, duplicate, or under-evidenced records and staging exact corrections for me to approve.
---

# Pipeline hygiene

Recommended agent: **pipeline-hygiene**. Skills: `crm-data-contract`, `discovery-qualification`.

Run a pipeline hygiene pass for ${input:scope:my book, a territory, a team, or a named account set}.

- Review date: ${input:review_date:date to evaluate staleness and past-due close dates}
- Period: ${input:period:fiscal period or calendar period to inspect}
- Defect focus: ${input:defect_focus:all defect classes or a narrower class}
- Stale rule: ${input:stale_rule:stage-specific stale threshold, or "use my profile"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve me and my book from `crm`, then read my profile for target bucket
   names, source mappings, stale rules, and `solution_catalog`.
2. Inspect active records for past-due close dates, stage mismatch against
   `discovery-qualification`, no activity, missing next step or owner, missing
   or stale amount, stalled records, duplicates, and missing economic buyer.
3. Distinguish "the record is wrong" from "the deal is in trouble". Route deal
   trouble to `deal-review` instead of hiding it in hygiene.
4. For every proposed `crm` change, stage a table row with record, field, current
   value, proposed value, evidence, reason, and batch approval key.
5. Batch corrections by defect class so I can approve a class at once.
6. Show all money arithmetic, label every figure's source, ask for an unknown
   target or amount, keep periods and currencies separate unless explicitly
   converted, and label weighted pipeline separately from unweighted pipeline.
7. Do not apply any change unless I explicitly confirm the staged row or batch.

Guardrail: no fabrication, source every claim, keep sensitive output in my gitignored `output_dir`, and stage `crm` writes for explicit confirmation before applying.
