---
mode: agent
description: Help me write short sourced executive outreach in my own voice, with claim trace and checks before I send it myself.
---

# Outreach writer

Recommended agent: **outreach-writer**. Skills: `outreach-voice`, `stakeholder-mapping`, `solution-messaging`.

Write outreach for ${input:recipient:Contact, role, or persona from crm}.

- Account or context: ${input:account:Account name or context}
- Signal and source: ${input:signal:Signal, source, and date}
- Motion and outcome: ${input:motion:Motion, business outcome, and audience level}
- Ask: ${input:ask:One small action you want the recipient to take}
- Channel: ${input:channel:Logical channel, for example email or message}
- Voice basis: ${input:voice_basis:"derive from workplace" or "use profile fallback"}
- Output: ${input:output:"chat" or "file in my output_dir"}

What I expect you to do:

1. Resolve my profile voice settings, word cap, banned phrases, and sign-off.
2. Derive voice from my own sent mail through `workplace` when available, or use
   profile fallback and say which you used.
3. Check `crm` for opt-out, unsubscribe, suppression, contactability, and
   regional consent indicators before drafting.
4. Write one short first-touch draft with one idea, one ask, and no more than one
   link.
5. Keep citations outside the message body. Put claim trace beside the draft with
   URL, date, and excerpt for external claims, or internal record name.
6. Write the subject line last, based on the final body.
7. Run the banned-phrase and no-dash checks.
8. End with what I should check before sending.

No fabrication. Drafts only, never send or schedule. Respect opt-outs and suppression in `crm`. Any file output stays in my `output_dir`, which is gitignored. No em dashes.
