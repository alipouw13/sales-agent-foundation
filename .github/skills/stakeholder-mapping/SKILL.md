---
name: stakeholder-mapping
description: Trigger for stakeholder map, buying committee, economic buyer, champion, decision maker, contact ranking, role inference, account family, who should I contact.
---
# Stakeholder Mapping Contract
## Purpose
This skill defines how agents identify, normalize, score, and rank people related to an account.
It is used when an agent must answer who is involved, who matters for a buying motion, or who should be contacted first.
The contract is vendor neutral.
Agents read logical sources only: `crm`, `workplace`, `notes`, `web`, and `decks`.
Agents must not name the host system behind those sources.
The output of this skill is a structured stakeholder map plus ranked contact guidance.
Every field must separate evidence from inference.
Every person-level finding must carry source attribution.
If evidence is missing, agents state unknown rather than guessing.
## Core terms
| Term | Definition |
| --- | --- |
| Stakeholder | A person recorded in an authorized source as related to the account, entity, opportunity, renewal, issue, meeting, note, or deck. |
| Account family | The set of parent, subsidiary, regional, business unit, and duplicate account records that plausibly belong to the same commercial customer family. |
| Entity | The specific account record, subsidiary, region, or business unit to which a fact belongs. |
| Buying committee | The set of stakeholders who influence need, budget, technical approval, risk approval, purchase process, adoption, or opposition. |
| Role inference | The process of assigning a buying-committee role from recorded evidence. |
| Warm path | A current internal relationship owner who has interacted with the stakeholder inside the freshness window and can make a relevant introduction. |
| Cold contact | A stakeholder with no recorded interaction inside the relevant freshness window. |
| Coverage gap | A missing critical role, missing current executive contact, or unclear account-family ownership that creates risk for the motion. |
## Required stakeholder record
Every agent that emits or consumes stakeholder data must use this record shape.
Use one record per person per entity when the same person appears in multiple account-family entities.
Do not merge records unless the source explicitly confirms they are the same person.
When a field is unknown, write `unknown` and cite the sources checked.
When a field is not applicable, write `not applicable`.
| Field | Required value | Source rule |
| --- | --- | --- |
| `account` | The account family display name used for the request. | Cite the source that supplied the account-family label. |
| `entity` | The specific parent, subsidiary, region, or business unit record. | Cite the entity source, never leave this implied. |
| `title_as_recorded` | The exact title string from the authorized source. | Cite the source and record context. |
| `inferred_function` | The business function inferred from title, meeting context, notes, and opportunity context. | Cite evidence. Do not infer from title alone when context conflicts. |
| `inferred_level` | One of individual contributor, manager, director, VP, C-level, board, or unknown. | Cite title evidence plus at least one context signal when available. |
| `inferred_buying_committee_role` | One primary role from the committee model, plus secondary roles when evidence supports them. | Cite the facts that map to the role. |
| `role_confidence` | high, medium, or low. | Must include the evidence class used to reach the score. |
| `role_confidence_evidence` | A short list of evidence items. | Include source name, date when available, and field or artifact name. |
| `last_interaction_date` | Most recent authorized interaction date, or unknown. | Prefer direct interaction records from `workplace`, `crm`, or `notes`. |
| `last_interaction_channel` | Meeting, message, call, note, deck review, crm activity, or unknown. | Use the channel recorded by the source. |
| `interaction_count` | Count of recorded interactions in the evaluation window. | Count only records the agent actually read. |
| `internal_relationship_owner` | The internal person or team recorded as owning the relationship, or unknown. | Cite `crm`, `workplace`, or `notes`. |
| `opt_out_or_suppression_flag` | true, false, or unknown. | If true, the stakeholder must not be recommended for outreach. |
| `field_sources` | Field-by-field source map. | Include every field name and the logical source that supplied it. |
## Field source map
The `field_sources` value must be explicit.
Use this shape for each field.
| Source item | Required fields |
| --- | --- |
| Field source | `field`, `logical_source`, `record_type`, `record_date`, `confidence_note` |
| Missing source | `field`, `logical_source_checked`, `result`, `confidence_note` |
Permitted `logical_source` values are `crm`, `workplace`, `notes`, `web`, and `decks`.
Do not include record identifiers that are not safe to commit.
Use labels such as opportunity record, contact record, meeting note, message thread, public page, or deck.
## Buying committee roles
| Role | What the role controls | Evidence that infers it |
| --- | --- | --- |
| Economic buyer | Budget authority, business case approval, priority tradeoffs, and final value acceptance. | Owns budget, approves purchase, signs business case, sponsors executive review, or is named as budget holder. |
| Champion | Internal advocacy, access to power, problem validation, and next-step momentum. | Shares internal context, introduces stakeholders, confirms pain, coaches on process, or actively advances the motion. |
| Technical evaluator | Architecture fit, integration fit, feasibility, security design input, data or workflow fit, and implementation risk. | Attends technical sessions, asks design questions, owns evaluation criteria, reviews proof output, or signs off on fit. |
| User | Day-to-day workflow need, usability feedback, adoption risk, and operational requirements. | Describes current process, pain, adoption blockers, workflow requirements, or acceptance criteria. |
| Blocker | Active or passive resistance that can slow or stop progress. | Raises unresolved objections, favors status quo, withholds access, disputes value, or blocks next steps. |
| Coach | Process guidance and stakeholder navigation without necessarily advocating. | Explains decision process, identifies roles, advises timing, or names risks while staying neutral. |
| Procurement | Commercial process, purchasing path, required forms, negotiation mechanics, and contract workflow. | Owns sourcing, request process, purchase order path, supplier onboarding, or commercial terms routing. |
| Legal | Contract terms, privacy terms, liability terms, data terms, and signature readiness. | Reviews agreements, asks legal-risk questions, supplies redlines, or controls required legal approvals. |
| Security | Security review, risk acceptance, controls, compliance evidence, and approval gates. | Owns security questionnaire, risk review, control validation, penetration test review, or compliance signoff. |
A stakeholder may hold more than one role.
When roles overlap, pick the role that controls the next decision for the current ask as primary.
List all secondary roles with separate confidence ratings.
Do not treat seniority as role evidence by itself.
## Evidence classes for role confidence
| Confidence | Required evidence |
| --- | --- |
| High | Two or more independent evidence items from authorized sources, or one explicit source statement naming the role and one corroborating behavior. |
| Medium | One direct evidence item, or two weak evidence items that agree and are not contradicted. |
| Low | Title-only evidence, stale evidence, inferred meeting attendance, or ambiguous notes. |
Independent evidence means the items come from different source records or different interaction contexts.
A copied note and the meeting it summarizes count as one evidence item.
Contradictory evidence must lower confidence by one level.
If the only evidence is title string, confidence is low.
## Level model
| Level | Definition | Typical evidence |
| --- | --- | --- |
| Individual contributor | Owns tasks, workflow knowledge, analysis, implementation work, or practitioner feedback without people-management authority. | Recorded title, task ownership, meeting role, notes describing hands-on work. |
| Manager | Leads a team or operational function and can prioritize team work. | Recorded title plus team ownership, recurring meeting lead, or approval of team tasks. |
| Director | Owns a department, program, region, or significant operating area. | Recorded title plus decision ownership, initiative ownership, or executive-facing responsibility. |
| VP | Owns a broad function, budget area, regional remit, or multi-team priority. | Recorded title plus budget, program, or strategy ownership. |
| C-level | Enterprise executive accountable for company-level function or business outcome. | Recorded title plus enterprise accountability or executive approval role. |
| Board | Governance-level stakeholder with oversight rather than operating ownership. | Public governance record or explicit source statement. |
A title string alone is weak evidence.
Title inflation, local convention, subsidiaries, and regional naming patterns vary.
Agents must use title plus behavior, ownership, meeting role, approval action, or source statement when possible.
If level is title-only, mark confidence low or medium only when the title has unambiguous authority and no contradiction exists.
## Function model
Use the function that best describes what the stakeholder owns in the account.
Allowed values are executive leadership, finance, operations, sales, marketing, product, engineering, information technology, security, legal, procurement, human resources, customer support, data and analytics, transformation, field operations, and unknown.
If the function is specialized, map it to the closest allowed value and record the specialization in evidence.
Do not create a new function value for one-off wording.
## Contact freshness thresholds
Freshness is measured from the date the agent runs.
Use calendar days.
If the source only gives a month, treat the interaction as the last day of that month and mark date precision as month.
| Relationship class | Fresh if last interaction is within | Warm if last interaction is within | Cold if older than |
| --- | --- | --- | --- |
| Active opportunity or renewal | 45 days | 90 days | 90 days |
| Account planning or executive relationship | 90 days | 180 days | 180 days |
| Customer success or adoption motion | 60 days | 120 days | 120 days |
| Cold prospecting or reactivation | No warm assumption | No warm assumption without an interaction | Any missing interaction |
A contact with no interaction inside the window is cold.
Treat cold as a status, not a defect.
Do not describe a cold contact as a warm relationship because they are senior, known by name, or listed in `crm`.
If the last interaction is unknown, freshness is unknown and ranking must penalize it as cold.
## Internal relationship strength
| Strength | Definition |
| --- | --- |
| Strong | Relationship owner interacted within the fresh window, can state current business context, and has a relevant reason to introduce. |
| Moderate | Relationship owner interacted within the warm window, or owns the account relationship but lacks recent context. |
| Weak | Relationship owner is recorded but has no current interaction, uncertain access, or only administrative ownership. |
| None | No internal owner found, or opt-out prevents contact use. |
The relationship owner can be a person, team, or role from `crm`, `workplace`, or `notes`.
Do not expose private relationship notes beyond what is necessary to explain the recommended path.
## Account family resolution
Account families often contain parent entities, subsidiaries, regional entities, retired duplicates, and near-duplicate names.
Agents must resolve the family before ranking contacts.
The primary entity is the entity that best matches the current ask.
Use this order to choose the primary entity.
| Priority | Rule |
| --- | --- |
| First | The entity explicitly named by the runner or opportunity. |
| Second | The entity that owns the active opportunity, renewal, support motion, or account plan. |
| Third | The parent entity if the ask is enterprise-wide or executive-level. |
| Fourth | The regional or subsidiary entity if the ask is local, regulated, implementation-specific, or contract-specific. |
| Fifth | The entity with the cleanest current source record when duplicates remain unresolved. |
Always state which entity each finding belongs to.
Never say a stakeholder belongs to the whole account family unless the evidence says their role spans the family.
If duplicates are likely but not resolved, create a coverage gap called unresolved duplicate account records.
If parent and subsidiary signals conflict, keep both and explain the conflict.
## Ranking algorithm for who to contact first
Ranking answers a specific ask, not a generic popularity contest.
First define the ask in one sentence.
Then score each eligible stakeholder on five dimensions.
| Dimension | Weight | Scoring rule |
| --- | --- | --- |
| Role fit | 30 | How directly the buying-committee role controls the next decision. |
| Level fit | 20 | Whether the level is appropriate for the ask and meeting type. |
| Freshness | 20 | Whether the contact is fresh, warm, cold, or unknown for this motion. |
| Relationship strength | 20 | Whether a strong, moderate, weak, or no internal path exists. |
| Access path | 10 | Whether a warmer internal path exists through another stakeholder. |
Score each dimension from 0 to 5.
Multiply each score by the weight.
Add the weighted scores and divide by 5 for a 0 to 100 rank score.
Exclude stakeholders with opt-out or suppression flag set to true.
If suppression is unknown, include only when there is a compliant authorized path and mark the risk.
The highest-ranked contact is often not the most senior person.
The best first contact is the person most likely to advance the next decision with the least trust cost.
A recent coach or champion with a strong internal owner can outrank a cold C-level contact.
A technical evaluator can outrank an economic buyer when the next ask is technical proof validation.
Procurement or legal can outrank executives when the next blocker is contract process.
## Ranking score definitions
| Score | Role fit | Level fit | Freshness | Relationship strength | Access path |
| --- | --- | --- | --- | --- | --- |
| 5 | Directly controls the next decision. | Exactly matches ask level. | Fresh. | Strong. | Warm path is available and relevant. |
| 4 | Strong influence on the decision. | One level away but appropriate. | Warm. | Moderate. | Warm path exists but needs context. |
| 3 | Useful influence but not controlling. | Usable for discovery or coaching. | Cold with known prior relationship. | Weak. | Indirect path exists. |
| 2 | Peripheral influence. | Too senior or too junior for first ask. | Cold with minimal context. | None found. | Possible path is uncertain. |
| 1 | Role is unclear. | Level is unclear. | Unknown date. | Owner unknown. | No path found. |
| 0 | Not relevant to ask. | Inappropriate for ask. | Suppressed or unavailable. | Suppressed or unavailable. | Suppressed or unavailable. |
Tie-breakers run in this order.
First prefer the stakeholder with a stronger compliant warm path.
Second prefer the stakeholder whose role controls the next decision.
Third prefer the stakeholder with more recent interaction.
Fourth prefer the stakeholder tied to the primary entity.
Fifth present the tie and ask the runner to choose.
## Coverage gap test
Run the coverage gap test after account-family resolution and before outreach guidance.
An account has a coverage gap when any of these are true.
| Gap | Condition | Required finding |
| --- | --- | --- |
| Economic buyer gap | No identified economic buyer with medium or high confidence. | State that the economic buyer is not identified and list evidence checked. |
| Executive freshness gap | No executive contact inside the freshness window for the motion. | State that executive coverage is cold or unknown. |
| Champion gap | No champion with medium or high confidence for an active motion. | State that there is no confirmed internal advocate. |
| Technical approval gap | Technical evaluator or security role is missing when the motion requires technical approval. | State which approval role is missing. |
| Process gap | Procurement or legal role is unknown when commercial process has started. | State the missing process owner. |
| Entity ambiguity gap | Parent, subsidiary, regional, or duplicate entity ownership is unresolved. | State which entity boundary is unresolved. |
| Suppression gap | The only plausible contact is suppressed or opted out. | State that compliant outreach path is unavailable. |
A coverage gap is a finding in its own right.
Do not hide it by ranking weak contacts as if coverage were complete.
## Output contract
Every stakeholder-mapping output must contain these sections.
1. Account family resolution.
2. Stakeholder records.
3. Buying committee summary.
4. Coverage gaps.
5. Ranked contact recommendation for the stated ask.
6. Evidence notes and source limits.
The ranked recommendation must say why the first contact is first.
It must also state why any more senior contact was not ranked first when that happens.
If there is no compliant contact path, say no compliant contact path found.
## Privacy boundary
Use only contact data already present in systems the runner is authorized to read.
Never scrape a personal email address or phone number.
Never infer a personal email address or phone number.
Never record personal attributes unrelated to the buying role.
Do not record personal life details.
Do not infer or record demographics.
Respect opt-out and suppression flags absolutely.
If any source indicates opt-out, suppression, do-not-contact, or equivalent status, do not recommend outreach to that person.
Never write a person's personal contact details into a committed file.
Generated stakeholder outputs that blend account data and personal data must stay in the runner's configured local output area.
Do not copy raw messages, private notes, or personal details into reusable prompts, skills, docs, examples, or committed artifacts.
## Anti-patterns
Do not rank by seniority alone.
Do not treat title as proof of authority.
Do not treat a stale executive contact as warm.
Do not merge people across duplicate entities without source confirmation.
Do not use public web guesses to fill private contact fields.
Do not invent a champion when the evidence only shows meeting attendance.
Do not ignore a coverage gap because the output would look incomplete.
