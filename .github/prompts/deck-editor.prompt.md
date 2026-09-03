---
mode: agent
description: Update my existing deck with specific changes while preserving formatting, protection, and narrative intent.
---

# Deck editor

Recommended agent: **deck-editor**. Skills: `deck-visual-system`.

Update the existing presentation file at ${input:deck:Local deck path or decks source reference}.

- Requested changes: ${input:changes:Exact changes to make, by slide if known}
- Source of truth: ${input:sources:Records, notes, workplace items, web citations, or source deck references}
- Slides in scope: ${input:slides:Specific slides or sections, or "infer from requested changes"}
- Formatting expectation: ${input:formatting:Preserve current formatting or explicitly redesign}
- Output preference: ${input:output:Edited copy in output_dir or another gitignored local path}
- Known constraints: ${input:constraints:Protection, classification, approval, or narrative constraints}

What I expect you to do:

1. Open the file through `decks` read only first and record slide count, theme,
   masters, fonts, protection, and classification when available.
2. Convert my request into an atomic slide-by-slide edit plan with the source for
   each change.
3. Change only what I asked for. Do not redesign unless my formatting expectation
   explicitly asks for redesign, in which case apply `deck-visual-system`.
4. Preserve theme, master layouts, fonts, notes, file-level protection, and
   classification. Warn before saving if any property cannot be preserved.
5. For each changed slide, report what changed, from what, to what, why, and the
   source that justified it.
6. Warn if a requested change breaks narrative flow or contradicts another slide.
7. Save an edited copy to my profile `output_dir`, then re-read the file and
   render changed slides to verify persistence, overflow, contrast, and orphaned
   text.
8. End with a `Gaps` line naming unavailable sources, blocked edits, and any file
   properties that could not be verified.

No fabricated metrics, proof points, quotes, logos, contacts, or numbers. Any file output goes to my profile `output_dir`, which is gitignored, and is never committed. Read only against `crm`. No em dashes.
