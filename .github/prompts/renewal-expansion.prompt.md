---
mode: agent
description: Score renewal risk and expansion whitespace across my installed base, then give me a dated save-or-grow plan.
---

# Renewal expansion

Recommended agent: **renewal-expansion**. Skills: `crm-data-contract`, `opportunity-signal-taxonomy`, `discovery-qualification`.

Review renewal risk and expansion whitespace for ${input:scope:my installed base, territory, account set, or renewal cohort}.

- Renewal period: ${input:renewal_period:period or date range for renewals}
- Expansion focus: ${input:expansion_focus:"use my solution_catalog" or specific catalog area}
- Risk emphasis: ${input:risk_emphasis:adoption, sponsor freshness, escalations, timing, competition, relationship health, or all}
- Target source: ${input:target_source:"read from crm" or "ask me for the stated target"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve my installed base from `crm`, including renewal dates, product
   footprint, owners, renewal opportunities, and expansion opportunities.
2. Pull adoption or consumption trend if available, support or escalation
   history, relationship recency from `workplace`, and context from `notes`.
3. Score renewal risk with an explicit rubric covering adoption trend, executive
   sponsor presence and freshness, open escalations, contract timing,
   competitive presence, and relationship recency.
4. Say which inputs were unavailable rather than scoring around them.
5. Treat quiet accounts as risk. Silence is not health.
6. Score expansion whitespace separately against my profile `solution_catalog`,
   requiring evidence per recommendation.
7. Show all renewal and expansion arithmetic, label every figure's source, ask
   for unknown targets or amounts, avoid mixing periods or currencies without
   explicit conversion, and keep weighted and unweighted pipeline separate.
8. Produce a dated save-or-grow plan sequenced by renewal date.
9. Stage any proposed `crm` write for my confirmation.

Guardrail: no fabrication, source every claim, keep sensitive output in my gitignored `output_dir`, and stage `crm` writes for explicit confirmation before applying.
