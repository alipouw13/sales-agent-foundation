---
mode: agent
description: Help me build a credible cold or lapsed account prospecting sequence where every touch adds new information.
---

# Prospecting sequence

Recommended agent: **prospecting-sequence**. Skills: `outreach-voice`, `stakeholder-mapping`, `opportunity-signal-taxonomy`, `industry-context`.

Build a prospecting sequence for ${input:account:Account name or account segment}.

- Scenario: ${input:scenario:"cold" or "lapsed"}
- Signal or reason to reach out: ${input:signal:Observed signal, source, or "find one if credible"}
- Target persona or contact: ${input:target:Known contact, role, or "rank the best targets"}
- Channels allowed: ${input:channels:Allowed logical channels, for example email, call, social, event follow-up}
- Sequence length preference: ${input:length:Maximum touches or "use your judgment"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve me, my profile, my voice settings, and the account live from `crm`.
2. Check `crm` for opt-out, unsubscribe, suppression, and regional consent
   indicators before proposing any contact.
3. Rank the target contacts or roles per `stakeholder-mapping`.
4. Confirm the signal is credible per `opportunity-signal-taxonomy` and has
   enough account or industry relevance to justify outreach.
5. Treat cold and lapsed scenarios differently. Use known history only when a
   real source supports it.
6. Design a capped sequence where each touch lists channel, timing offset in
   days, single idea, new information added, evidence, and call to action.
7. Escalate the ask slowly, starting with a low-friction response rather than a
   meeting request.
8. Define exit criteria for reply, opt-out, wrong person, non-response, and hard
   touch cap.
9. If there is no credible reason to reach out, refuse and say what evidence is
   missing.

No fabrication. Drafts only, never send or schedule. Respect opt-outs and suppression in `crm`. Any file output stays in my `output_dir`, which is gitignored. No em dashes.
