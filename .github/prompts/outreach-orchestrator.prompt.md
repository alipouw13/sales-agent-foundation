---
mode: agent
description: Help me turn an account or signal into ranked, review-ready outreach drafts with the reasoning and source trace shown beside each draft.
---

# Outreach orchestrator

Recommended agent: **outreach-orchestrator**. Skills: `stakeholder-mapping`, `industry-context`, `solution-messaging`, `outreach-voice`, `opportunity-signal-taxonomy`.

Turn ${input:target:Account name, account segment, or signal} into ranked outreach drafts.

- Trigger or signal: ${input:signal:Observed signal, source, date, or "research why now"}
- Intended audience: ${input:audience:Known contact, buying role, level, or "rank the best people"}
- Business motion: ${input:motion:Preferred motion or "choose the right motion"}
- Draft count: ${input:draft_count:"two", "three", "four", or "use the evidence to decide"}
- Tone constraint: ${input:tone:Tone requirement, risk note, or "use my derived voice"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve me, my profile, my solution catalog, and the account or signal live.
2. Check `crm` for opt-out, unsubscribe, suppression, contactability, and
   regional consent indicators before drafting.
3. Answer WHO with ranked stakeholder logic.
4. Answer WHY NOW with cited industry, account, or internal evidence.
5. Answer WHAT with the right motion, level framing, small first step, and traps
   to avoid.
6. Answer HOW with drafts in my derived voice, or profile voice if sample is
   insufficient.
7. Produce no more than two to four drafts, and fewer if evidence supports fewer.
8. Put the claim trace beside each draft: URL, date, and excerpt for external
   claims, or internal record name for internal claims.
9. If the signal is negative, use a support or risk frame and avoid opportunism.
10. List what I should verify before sending.

No fabrication. Drafts only, never send or schedule. Respect opt-outs and suppression in `crm`. Any file output stays in my `output_dir`, which is gitignored. No em dashes.
