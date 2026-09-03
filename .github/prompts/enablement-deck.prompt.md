---
mode: agent
description: Build me a new cited deck from scratch for a specific audience, message, and time slot.
---

# Enablement deck

Recommended agent: **enablement-deck**. Skills: `deck-visual-system`, `solution-messaging`, `industry-context`.

Build a new presentation file for ${input:audience:Audience and deck type, for example internal enablement, customer-facing, or personal walking deck}.

- Topic: ${input:topic:The topic or point of view}
- Single message to land: ${input:message:The one sentence the audience must remember}
- Time slot: ${input:time_slot:Presentation time in minutes}
- Desired output: ${input:output:Presentation file or slide script in output_dir}
- Source material: ${input:sources:Source files, links, records, notes, or none}
- Must include: ${input:must_include:Required sections, claims, visuals, or constraints}
- Must avoid: ${input:must_avoid:Claims, examples, assets, or topics to omit}

What I expect you to do:

1. Resolve my profile, mapped sources, `solution_catalog`, and profile
   `output_dir` before drafting.
2. Classify the deck type first, because internal enablement, customer-facing,
   and personal walking decks require different tone and evidence.
3. Use one slide for every two minutes of presentation time, reserving one title
   slide and one close slide, then state the resulting slide cap.
4. Build a slide-title outline first, with one sentence explaining why each slide
   belongs, and get agreement before generating slides when interaction is
   available.
5. Ground every factual claim in `web`, `crm`, `workplace`, `notes`, or `decks`.
   Keep citations in speaker notes, not cluttering the slide.
6. Enforce one idea per slide, no noun-only bullet slides, and no chart without a
   takeaway title.
7. Apply `deck-visual-system`, then render and run visual QA for overflow,
   contrast, type consistency, and orphaned text.
8. End with a `Gaps` line naming sources unavailable and claims removed because
   they lacked evidence.

No fabricated claims, proof points, quotes, logos, contacts, or numbers. Any file output goes to my profile `output_dir`, which is gitignored, and is never committed. Read only against `crm`. No em dashes.
