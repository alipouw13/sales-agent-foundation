---
mode: agent
description: Build or refresh my weekly impact roll-up from actual activity, record movement, and open tasks.
---

# Weekly impact

Recommended agent: **weekly-impact**. Skills: `crm-data-contract`, `discovery-qualification`.

Build or refresh my weekly impact roll-up for ${input:week_scope:Week, date range, or list of weeks to backfill}.

- Destination: ${input:destination:Existing roll-up artifact or new file in output_dir}
- Refresh mode: ${input:refresh_mode:Additive new section or proposed replacement for a dated section}
- Sources to use: ${input:sources:Use all mapped sources or list exclusions}
- Focus areas: ${input:focus:Accounts, opportunities, outcomes, or task types to emphasize}
- Output depth: ${input:depth:Executive summary, full evidence roll-up, or both}

What I expect you to do:

1. Resolve my identity, profile, calendar settings, mapped sources, and profile
   `output_dir`.
2. State the exact week boundaries before gathering evidence. If I ask for
   backfill, keep each week in its own dated section.
3. Pull record movement from `crm`: stage changes, new records, closed records,
   completed tasks, overdue items cleared, and next-step changes.
4. Pull corroborating signal from `workplace`: sent and received items, chats,
   channel posts, meetings, recaps, and follow-ups.
5. Pull context from `notes`, with dates and note titles.
6. Separate activity from impact. Promote only outcomes with evidence of movement,
   decision, risk reduction, customer progress, or completed work.
7. Group the write-up by outcome, not by day, and keep thin weeks short.
8. Write additively to the destination under `output_dir`. If refreshing an
   existing dated section, provide a proposed replacement diff.
9. Produce next week's open tasks with owner, due date, source, and rationale.
10. End with a `Gaps` line naming unavailable sources and what the roll-up could
    not see.

No fabricated meetings, messages, tasks, owners, dates, numbers, or impact. Any file output goes to my profile `output_dir`, which is gitignored, and is never committed. Propose only against `crm`. No em dashes.
