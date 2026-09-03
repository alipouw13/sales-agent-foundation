---
name: discovery-qualification
description: qualification, MEDDPICC, BANT, discovery, deal inspection, qualification rubric, evidence, exit criteria.
---

# Discovery qualification

## Purpose
This skill defines the shared qualification rubric for revenue agents.
`deal-review`, `gap-analysis`, `pipeline-hygiene`, and `forecast-review` must score qualification identically.
The rubric is evidence-first.
It is not a form-completion exercise.
It is not a numeric score.
It is not a substitute for human judgment.
The rubric exists to find the single weakest condition that can kill a deal.

## Core terms
| Term | Definition |
| --- | --- |
| Deal | A CRM opportunity inspected for quality, stage, next action, or forecast category. |
| Qualification element | One required buying condition from the rubric. |
| Evidence | A specific artifact or CRM record the agent can point at. |
| Artifact | A CRM field, CRM activity, meeting note, customer message, call recap, signed document, public source, or approved internal note. |
| Assertion | A belief held by the team but not tied to a pointable artifact. |
| Unknown | Missing, contradictory, inaccessible, or not yet asked. |
| Canonical stage | The shared stage model from `crm-data-contract`: `Identified`, `Qualified`, `Solution Fit`, `Selected`, `Closed`. |
| Forecast category | A human-facing call about likelihood and timing, based on evidence rather than optimism. |
Evidence must name the artifact type and the record or note where it lives.
A statement without a pointable artifact is asserted, even when the team believes it.
Contradictory artifacts make the element asserted unless the contradiction is resolved.
A stale artifact can still be evidence, but the agent must flag the date risk.

## Three-value scale
Every qualification element has exactly one value: `Evidenced`, `Asserted`, or `Unknown`.
Do not use numeric scores.
Do not use percentages.
Do not average elements.
Do not create half states such as mostly evidenced or almost known.
| Value | Meaning | Allowed use |
| --- | --- | --- |
| `Evidenced` | A pointable artifact directly supports the element. | Use for stage exit, forecast support, and next-step planning. |
| `Asserted` | The team believes it, but the agent cannot point to a supporting artifact. | Use as a risk and convert it into a question. |
| `Unknown` | The element is absent, contradictory, or not inspected. | Use as a blocker for stage or forecast confidence. |
The overall deal qualification state is the weakest element.
The order from strongest to weakest is `Evidenced`, then `Asserted`, then `Unknown`.
A deal with any `Unknown` element is overall `Unknown` for qualification.
A deal with no `Unknown` elements but at least one `Asserted` element is overall `Asserted`.
A deal is overall `Evidenced` only when every required element for its stage is evidenced.
Averaging hides the thing that kills the deal.
One unevidenced paper process can block a selected deal even if every other element looks strong.
One absent economic buyer can make a forecast call unsafe even when activity is high.

## Qualification elements
Use these elements for every deal unless a prompt explicitly narrows scope.
The element names are stable and must not be renamed by individual agents.
| Element | Meaning |
| --- | --- |
| Metrics | The measurable business result the customer wants and the baseline or direction of change. |
| Economic buyer | The person or buying body with final authority over funds, priority, or commercial approval. |
| Decision criteria | The explicit requirements the customer will use to choose a path. |
| Decision process | The sequence of customer decisions, approvals, meetings, and participants needed to choose. |
| Paper process | The contracting, procurement, legal, security, or order path required after selection. |
| Identified pain | The business problem, consequence, or risk that makes action necessary. |
| Champion | A stakeholder who has power, influence, and active commitment to help the seller win. |
| Competition | The customer's credible alternatives, including doing nothing, internal build, incumbent, or another vendor. |
| Compelling event | A dated business reason that makes timing matter. |

## Element evidence contract
Use the table below to classify each element.
The best question is the single highest-leverage question to move an asserted element to evidenced.
| Element | Evidenced | Asserted | Unknown | Best question |
| --- | --- | --- | --- | --- |
| Metrics | A CRM note, discovery summary, customer message, or business case states the desired metric and baseline or desired change. | The team says there is value, but no artifact states the metric. | No measurable outcome is named. | What measurable result will the customer use to say this was worth doing? |
| Economic buyer | A CRM stakeholder record, meeting note, customer message, or approval artifact identifies who can approve funds or priority. | The team believes a stakeholder is the buyer, but authority is not documented. | No authority path is known. | Who can say yes when every other stakeholder says yes? |
| Decision criteria | A customer artifact, discovery note, evaluation matrix, success plan, or recap lists requirements used to choose. | The team believes the criteria, but only internal assumptions exist. | No selection requirements are known. | What criteria will the customer use to compare options? |
| Decision process | A mutual plan, CRM note, recap, or customer-confirmed timeline identifies steps, owners, and sequence. | The team has a rough path, but it is not customer-confirmed. | No path to decision is known. | What happens between this conversation and a formal decision? |
| Paper process | A procurement note, legal checklist, security review record, order path, or customer confirmation identifies post-selection steps. | The team assumes standard procurement or contracting will apply. | No commercial or approval path after selection is known. | After selection, what paperwork or approvals must happen before the order is complete? |
| Identified pain | A discovery artifact states the problem and consequence of inaction in customer language. | The team describes a problem, but the customer has not confirmed it in an artifact. | No business pain is documented. | What happens if the customer does nothing? |
| Champion | A stakeholder record plus activity evidence shows influence, access, and active selling help inside the account. | The team likes a contact, but there is no proof of influence or action. | No internal advocate is identified. | Who is actively helping us navigate and why would they spend political capital? |
| Competition | A CRM field, discovery note, customer message, or evaluation artifact names credible alternatives or confirms no active alternative. | The team thinks there is no competitor or knows one informally. | Alternatives are not discussed. | What options is the customer comparing, including doing nothing? |
| Compelling event | A dated customer artifact ties action to a business event, deadline, risk, launch, renewal, compliance date, or executive commitment. | The team has a desired close date, but no customer event supports it. | No timing driver is known. | Why does this need to happen by the proposed date? |
If the answer to the best question is already assumed, the element is likely asserted, not evidenced.
If an artifact exists but does not answer the element's meaning, it is not evidence for that element.

## Stage exit criteria
A deal may sit in a canonical stage only when the required elements for that stage meet the minimum state below.
| Canonical stage | Minimum required qualification state | Required evidenced elements before entering or remaining |
| --- | --- | --- |
| `Identified` | At least one element is asserted or evidenced. | None. The record may exist while discovery begins. |
| `Qualified` | No required element for this stage is unknown. | Identified pain, initial metrics, account fit, next discovery action. |
| `Solution Fit` | Required elements for this stage are evidenced. | Identified pain, metrics, decision criteria, decision process, competition. |
| `Selected` | Required elements for this stage are evidenced. | Economic buyer, decision criteria, decision process, paper process, champion, compelling event, competition. |
| `Closed` | Outcome evidence exists. | Closed outcome, close date, amount and currency when monetary, loss reason when lost. |
`account fit` means the account is in scope for the runner's book and the opportunity aligns to an allowed product, play, service, or motion.
`next discovery action` means a dated action that can produce missing qualification evidence.
A late-stage deal with an unevidenced economic buyer is mis-staged, not merely under-documented.
A late-stage deal with an unevidenced paper process is mis-staged, not merely under-documented.
Late-stage means `Selected` or any CRM stage mapped to `Selected`.
If stage evidence and CRM stage disagree, report the evidence-based stage and stage a correction only through the CRM propose-only write contract.
Do not move a deal forward because time has passed, probability increased, or the seller wants it in forecast.

## Forecast category rules
Forecast category follows qualification and stage evidence.
It must not override missing evidence.
| Category | Required evidence |
| --- | --- |
| `Omitted` | The deal is closed, out of period, duplicate, not in the runner's book, or lacks required CRM fields for forecast use. |
| `Pipeline` | The deal is open and in scope, but one or more required elements for its current stage are unknown. |
| `Best Case` | The deal is open, in period, in scope, no required late-stage element is unknown, and at least one required element is asserted. |
| `Commit` | The deal is in `Selected`, all `Selected` elements are evidenced, amount and currency are usable, close date is supported by a compelling event, paper process is known, and the human owner confirms the call. |
| `Closed` | CRM close status is closed and outcome evidence exists. |
A commit is a commit only when selection, authority, paper process, timing, and owner confirmation all exist.
A verbal positive signal without paper process evidence is not commit.
A dated close target without a compelling event is not commit.
A strong champion without economic buyer access is not commit.
If forecast category and qualification conflict, lower the forecast category or mark it for human review.
Stage any CRM forecast-category change as a proposed write, never apply it directly.

## Champion versus coach
A coach provides information.
A champion changes the deal.
A champion has influence, understands the customer's power path, wants the outcome, and takes action that helps the seller win.
Evidence of a champion may include introducing the team to authority, correcting the mutual plan, sharing decision criteria, advocating internally, or confirming competitive risk.
A friendly contact is not a champion by default.
A frequent meeting attendee is not a champion by default.
A technical evaluator is not a champion unless they influence the buying decision and act on that influence.
If influence or active advocacy is missing, classify the element as asserted or unknown.
The best next action is to ask what the person has done that changed access, criteria, urgency, or decision path.

## Pain versus interest
Interest is curiosity about a product, service, idea, or meeting.
Pain is a business consequence that makes inaction costly.
Interest can create discovery.
Pain creates qualification.
Evidence of pain uses customer language and states consequence.
Consequence types include cost, risk, delay, compliance exposure, customer impact, employee burden, missed market window, or operational fragility.
Do not treat attendance, enthusiasm, downloads, demos, or generic strategic language as pain.
If the customer cannot explain what breaks or worsens without action, pain is asserted at best.
If the pain has no owner or affected process, it is incomplete evidence.
The best next action is to ask what happens if nothing changes and who is accountable for that outcome.

## Inspection process
Inspect the CRM record first for stage, amount, currency, close date, owner, account, next step, and last activity date.
Inspect qualification artifacts second.
Classify every element as `Evidenced`, `Asserted`, or `Unknown`.
Name the weakest element.
Name the canonical stage supported by evidence.
Compare evidence-based stage to CRM stage.
Compare qualification state to forecast category.
Return the smallest safe next action that can create or verify evidence.
For late-stage deals, prioritize economic buyer, paper process, identified pain, and compelling event in that order.
For early-stage deals, prioritize identified pain, metrics, decision criteria, and next discovery action.

## Output contract
Every deal inspection must include these fields in plain language.
| Output field | Requirement |
| --- | --- |
| `Overall qualification` | The weakest state among required elements. |
| `Weakest element` | One element name, with tie broken by stage risk. |
| `Evidence cited` | The artifact types used, without exposing sensitive content unnecessarily. |
| `Mis-stage assessment` | `Aligned`, `Possibly mis-staged`, or `Mis-staged`. |
| `Forecast implication` | The safest category or review flag. |
| `Next action` | One action, owner type, and date if available. |
| `Proposed CRM changes` | Staged changes only, following `crm-data-contract`. |
Do not hide unknowns in a narrative summary.
Do not substitute activity volume for evidence quality.
Do not call a deal healthy if the weakest element can still kill it.

## Anti-patterns
Rubric theatre is filling every field so the record looks complete while answers remain unverified.
Field completion is not qualification.
A copied note is not evidence unless it answers the specific element.
A seller belief is not evidence because it appears in a CRM field.
Treating the rubric as a form creates false confidence.
Treating the rubric as questions creates useful pressure.
Do not mark every element evidenced from one meeting recap unless the recap directly answers every element.
Do not reward vague language such as strategic priority, strong interest, aligned, likely, or verbal yes without the artifact that proves what it means.
Do not create a numeric score to make weak evidence look precise.
Do not average away a blocker.
Do not inspect only the fields that make the deal look good.

## Guardrails and refusals
Refuse to certify `Commit` when economic buyer, paper process, or compelling event is not evidenced.
Refuse to advance the evidence-based stage when required exit criteria are missing.
Refuse to invent missing qualification evidence from account size, brand, activity volume, or seller confidence.
Refuse to treat a close date as a compelling event without a customer business reason.
Refuse to treat a coach as a champion without influence and advocacy evidence.
Refuse to treat interest as pain without consequence of inaction.
Refuse to apply CRM updates directly.
When refusing, state the missing element, why it matters, and the single best question or action to obtain evidence.
If a prompt asks for a forecast call that conflicts with this rubric, follow this rubric and mark the conflict for human review.
If evidence is unavailable because a source is unavailable, classify affected elements as unknown rather than guessed.
