---
mode: agent
description: Review one opportunity in depth, score the evidence, name the weakest element, and give me exactly three next actions.
---

# Deal review

Recommended agent: **deal-review**. Skills: `discovery-qualification`, `stakeholder-mapping`, `crm-data-contract`.

Review this opportunity: ${input:opportunity:opportunity name or link from crm}.

- Review date: ${input:review_date:date for the deal inspection}
- Purpose: ${input:purpose:forecast inspection, coaching, executive review, or close plan}
- Close period to test: ${input:close_period:period the opportunity is expected to close}
- Time tradeoff: ${input:time_tradeoff:what other book priority this deal competes with}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve exactly one opportunity in `crm`. If there are multiple matches, ask
   me to choose rather than guessing.
2. Pull its history, buying committee, competitive situation, paper process,
   amount, close date, and recent activity from mapped sources.
3. Score each `discovery-qualification` element as evidenced, asserted, or
   unknown, and cite evidence for anything scored evidenced.
4. Name the single weakest element, then explain why it is the highest leverage
   issue to fix now.
5. Test the close date against the customer's paper process and procurement
   reality, not seller hope.
6. Show any money arithmetic, label each figure's source, ask for unknown targets
   or amounts, avoid mixing periods or currencies without explicit conversion,
   and keep weighted and unweighted values separate.
7. Produce exactly three next actions with owner, date, and desired proof.
8. Ask whether this deal is worth the time relative to the rest of my book.

Guardrail: no fabrication, source every claim, keep sensitive output in my gitignored `output_dir`, and stage `crm` writes for explicit confirmation before applying.
