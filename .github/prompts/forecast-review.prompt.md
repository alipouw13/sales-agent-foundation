---
mode: agent
description: Prepare my forecast call by separating evidenced deals from asserted deals and showing the floor, likely case, and stretch.
---

# Forecast review

Recommended agent: **forecast-review**. Skills: `discovery-qualification`, `crm-data-contract`.

Prepare a forecast review for ${input:scope:my territory, my team, a manager roll-up, or a named account set}.

- Period: ${input:period:forecast period to inspect}
- Target source: ${input:target_source:"read from crm" or "ask me for the stated target"}
- Categories: ${input:categories:"use crm categories" or category labels to include}
- Evidence age rule: ${input:evidence_age_rule:what counts as stale evidence, or "use my profile"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve the scope and period from `crm` and my profile.
2. Group opportunities by category, including commit, best case, pipeline, and
   omitted when those labels exist.
3. For each deal, separate what is evidenced from what is asserted using
   `discovery-qualification`.
4. Compute the evidenced floor, likely case, and stretch, and show the arithmetic
   behind each call range.
5. Label every figure's source, ask for unknown targets, never mix periods or
   currencies without explicit conversion, and keep weighted and unweighted
   pipeline separate.
6. Flag category inflation per deal, especially commit deals without evidenced
   economic buyer or signed-off paper process.
7. State what fraction of the number rests on stale, missing, asserted, or
   unknown evidence.
8. Produce exactly three manager questions for the call.
9. Do not write to `crm`.

Guardrail: no fabrication, source every claim, keep sensitive output in my gitignored `output_dir`, and never write to `crm` from this workflow.
