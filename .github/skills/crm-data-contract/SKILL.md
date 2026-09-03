---
name: crm-data-contract
description: CRM query, field mapping, entity mapping, opportunity fields, account fields, stage mapping, CRM schema, data contract.
---

# CRM data contract

## Purpose
This skill is the translation layer between a real CRM schema and the logical model used by revenue agents.
Agents must use the logical source `crm`, not vendor-specific tool names, except in the mapping examples in this skill.
The `crm` source must expose these capabilities when available: `whoami`, `list_accounts`, `list_opportunities`, `get_contacts`, `get_deal_team`, `get_activities`, and `propose_write`.
If a capability is unavailable, the agent must name the unavailable capability and continue only with supported work.
A field mapping is a contract, not a guess.
A wrong field mapping produces confident wrong numbers, broken prioritization, and unsafe write proposals.
When a mapping is ambiguous, the agent must ask the runner to confirm the mapping before using it.

## Terms
| Term | Definition |
| --- | --- |
| Runner | The human using the agent in their own sales or revenue role. |
| Logical entity | The portable entity name an agent may use across CRM products. |
| Logical field | The portable field name an agent may request or display. |
| Source field | The concrete CRM field mapped to a logical field. |
| Required | The agent cannot perform the named workflow correctly without the field. |
| Optional | The field improves quality but must not block the workflow. |
| Conditional | Required only for workflows that compute, compare, or stage changes involving that field. |
| Absent | Missing, inaccessible, blank, redacted, or not mapped. |
| Staged change | A proposed CRM update prepared for human review, not yet applied. |

## Entity contract
Agents may use only these logical entities unless a workflow explicitly defines a local extension.
The logical entities are `account`, `opportunity`, `contact`, `deal-team member`, `activity`, and `target`.
Do not infer hidden entities from field names.
Do not merge entities without an explicit relationship field.
Do not treat workplace messages, notes, or public web content as CRM records.

## Account fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `name` | Yes | Stop account-specific output and ask for a usable account identifier. |
| `parent` | Optional | State that account family coverage is unknown and avoid hierarchy conclusions. |
| `industry` | Conditional | If industry context is needed, say industry is unmapped and use public or runner-provided context only. |
| `segment` | Optional | Omit segment filters and do not compare the account against segment peers. |
| `owner` | Conditional | If ownership matters, report owner unavailable and do not assign owner-specific actions. |
| `region` | Optional | Omit regional rollups and do not infer territory from address text. |
Account identity must preserve the source record reference.
If duplicate account names appear, disambiguate by parent, region, owner, or source record reference.

## Opportunity fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `name` | Yes | Stop opportunity-specific output and ask for a usable opportunity identifier. |
| `account` | Yes | Exclude it from account, book, and territory rollups. |
| `stage` | Yes | Mark stage unmapped and exclude it from stage-dependent forecast logic. |
| `amount` | Conditional | Do not compute coverage, gap, weighted value, or total pipeline for it. |
| `currency` | Conditional | Do not sum or compare the amount with any other amount. |
| `close date` | Conditional | Exclude it from period forecast and date-drift analysis. |
| `product or play` | Optional | Group it as unspecified product or play and do not invent a motion. |
| `probability` | Optional | Ignore probability-based weighting and use evidence rules instead. |
| `created date` | Optional | Omit age analysis and do not infer age from record ordering. |
| `last activity date` | Conditional | If staleness is evaluated, mark staleness unknown. |
| `owner` | Conditional | If task ownership is evaluated, mark owner unavailable and do not assign action. |
| `next step` | Conditional | If hygiene is evaluated, flag missing next step through a staged change only. |
| `competitor` | Optional | State competition unknown and do not fabricate competitor pressure. |
| `loss reason` | Conditional | Required only for closed-lost analysis. If absent, say loss reason is not captured. |
An amount without currency is unusable for arithmetic.
Probability is a CRM field, not qualification evidence.
A close date is a planning signal, not proof of a compelling event.

## Contact fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `name` | Yes | Do not create a contact-specific recommendation. Use role-only language if role exists. |
| `title` | Conditional | If stakeholder mapping is needed, mark title unavailable and reduce role confidence. |
| `level` | Optional | Infer no seniority and ask before labeling executive, manager, or practitioner. |
| `function` | Optional | Mark function unknown and avoid functional coverage claims. |
| `account` | Yes | Do not attach the contact to an account-specific map. |
| `last interaction date` | Optional | State relationship recency unknown. |
| `opt-out flag` | Yes for outreach | If absent, do not generate outreach to that contact. |
The `opt-out flag` wins over every other recommendation.
If the contact cannot be safely contacted, recommend internal research but not external outreach.

## Deal-team member fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `person` | Yes | Do not assign or attribute work to the member. |
| `role` | Yes | List the member as role unknown and ask for role confirmation. |
| `related record` | Yes | Do not attach the member to an account or opportunity. |
A deal-team member is an internal participant, not a customer contact.
If the same person appears with multiple roles, keep each role tied to its related record.
Do not collapse roles across records.

## Activity fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `type` | Optional | Label as activity with type unknown. |
| `date` | Yes | Exclude from recency, staleness, and timeline logic. |
| `subject` | Optional | Display as untitled activity and do not infer outcome. |
| `participants` | Optional | Do not infer stakeholder engagement or buyer access. |
| `related record` | Yes | Exclude from account or opportunity timelines. |
Activities prove that something happened.
Activities do not prove qualification unless their content or linked notes identify the evidence.
Do not infer meeting content from a title alone.

## Target fields
| Logical field | Required | What the agent must do when absent |
| --- | --- | --- |
| `bucket name` | Yes | Do not group targets by bucket. Ask the runner to map the bucket. |
| `period` | Yes | Do not compare target to pipeline for any period. |
| `value` | Yes | Do not compute attainment, gap, or coverage. |
| `source` | Yes | State target source unknown and do not call it authoritative. |
Targets may represent quota, goal, plan, or capacity.
Preserve the source label and do not treat an informal goal as authoritative.
A target value must follow the amount and currency rule when it is monetary.

## Canonical stage model
All CRM stage lists must map to this ordered stage model.
| Order | Canonical stage | Meaning | Open or closed |
| --- | --- | --- | --- |
| 1 | `Identified` | A potential opportunity exists, but qualification evidence is incomplete. | Open |
| 2 | `Qualified` | Need, account fit, owner, and next discovery action are established. | Open |
| 3 | `Solution Fit` | The buying problem, decision criteria, and proposed approach are being validated. | Open |
| 4 | `Selected` | The customer has indicated a preferred path and commercial or paper process is active. | Open |
| 5 | `Closed` | The opportunity ended as won, lost, no decision, or cancelled. | Closed |
The canonical stage is the only stage value used for cross-agent reasoning.
The original CRM stage must be preserved for display and write proposals.
Never sort stages alphabetically.
Never use probability alone to assign canonical stage.

## Stage mapping method
Map each source CRM stage to the earliest canonical stage whose meaning is fully satisfied.
Use stage label, CRM status, required exit evidence, and close status together.
If a stage is closed in CRM, map it to `Closed` regardless of label.
If a custom stage is a pre-qualification holding area, map it to `Identified`.
If a custom stage means internal review before customer validation, map it to `Qualified` at most.
If a custom stage means customer validation of technical, business, or value fit, map it to `Solution Fit`.
If a custom stage means selected vendor, legal, procurement, contracting, or purchase process, map it to `Selected`.
If a custom stage mixes meanings, map it to the earlier stage and flag it for runner confirmation.
If no mapping can be defended, set canonical stage to `Unknown` and exclude the record from stage rollups.

## Default staleness thresholds
These are defaults the runner should override in their profile.
| Canonical stage | Stale when no logged activity for | Required agent action |
| --- | --- | --- |
| `Identified` | 14 calendar days | Flag as stale if still open with no next step. |
| `Qualified` | 21 calendar days | Flag as stale and request a dated discovery next step. |
| `Solution Fit` | 30 calendar days | Flag as stalled unless evidence explains the delay. |
| `Selected` | 7 calendar days | Flag as urgent because late-stage inactivity changes forecast confidence. |
| `Closed` | Not applicable | Do not apply activity staleness. |
| `Unknown` | 14 calendar days | Flag as stage unmapped and stale only if last activity is also old. |
Use calendar days unless the runner profile defines business days.
If `last activity date` is absent, say staleness is unknown rather than stale.
If `next step` has a future date but no recent activity, report both facts separately.

## Amount and currency rule
Every displayed monetary amount must include its currency label.
Never sum across currencies silently.
Never compare monetary values across currencies unless they are explicitly converted.
A converted value must state source currency, target currency, conversion rate, and rate date.
If the rate date is unknown, the conversion cannot be used for forecast, gap, or target comparison.
If a CRM provides corporate converted amount and transaction amount, keep both labels.
Use transaction amount for deal inspection unless the runner asks for corporate reporting.
Use corporate converted amount for rollups only when the source identifies it as converted.
Do not infer currency from account country, region, owner, or user locale.

## Book shape contract
`my book` means the accounts, opportunities, contacts, and targets in scope for the runner.
The runner profile value `book_shape` controls how scope is resolved.
| `book_shape` value | Meaning of `my book` | Required CRM basis |
| --- | --- | --- |
| `named-accounts` | A named account list owned by or assigned to the runner. | Account ownership, account team, or explicit named-account list. |
| `territory` | Records in a geographic, segment, product, or sales territory assigned to the runner. | Territory membership or territory account list. |
| `vertical` | Records in one or more industries or sub-industries assigned to the runner. | Industry field plus runner assignment. |
| `patch` | A flexible coverage set defined by manager, overlay, partner, or temporary assignment. | Explicit patch membership, team role, or runner-provided list. |
If `book_shape` is absent, default to records where the runner is owner or deal-team member.
If multiple scope rules disagree, use the narrower scope and report the conflict.
Do not include an account in `my book` because it appears in notes, mail, or public web alone.

## Propose-only write contract
Agents must never apply CRM changes directly.
All CRM updates must be staged through `propose_write` for explicit human confirmation.
A staged change must contain exactly these fields.
| Field | Required content |
| --- | --- |
| `record` | Logical entity, source record reference, and safe display label. |
| `field` | Logical field name and mapped source field name. |
| `current value` | Current CRM value, or `blank`, `unmapped`, or `unavailable`. |
| `proposed value` | Replacement value or append value, expressed in the CRM field's allowed format. |
| `reason` | Evidence-based reason for the proposed change. |
| `confidence` | `high`, `medium`, or `low`, based on mapping certainty and evidence quality. |
`high` confidence means the mapping is confirmed and evidence directly supports the value.
`medium` confidence means the mapping is confirmed but evidence is indirect or partial.
`low` confidence means the proposal is a question for review.
No staged change may be applied unless the human explicitly confirms that exact change.
Bulk changes require one staged change per record and per field.

## Worked field mapping examples
These examples show how to build a mapping for common CRM products.
They are not a guarantee that every tenant uses the same names.
| Logical entity | Logical field | Salesforce common field | Dynamics 365 common field | HubSpot common field | Pipedrive common field |
| --- | --- | --- | --- | --- | --- |
| account | `name` | `Account.Name` | `account.name` | `companies.name` | `organization.name` |
| account | `parent` | `Account.ParentId` | `account.parentaccountid` | `companies.hs_parent_company_id` | custom relationship field |
| account | `industry` | `Account.Industry` | `account.industrycode` | `companies.industry` | `organization.category` or custom field |
| account | `owner` | `Account.OwnerId` | `account.ownerid` | `companies.hubspot_owner_id` | `organization.owner_id` |
| opportunity | `name` | `Opportunity.Name` | `opportunity.name` | `deals.dealname` | `deal.title` |
| opportunity | `account` | `Opportunity.AccountId` | `opportunity.parentaccountid` | `deals.associatedcompanyid` | `deal.org_id` |
| opportunity | `stage` | `Opportunity.StageName` | `opportunity.salesstage` or `opportunity.stepname` | `deals.dealstage` | `deal.stage_id` |
| opportunity | `amount` | `Opportunity.Amount` | `opportunity.estimatedvalue` | `deals.amount` | `deal.value` |
| opportunity | `currency` | `Opportunity.CurrencyIsoCode` | `transactioncurrencyid` | `deals.deal_currency_code` | `deal.currency` |
| opportunity | `close date` | `Opportunity.CloseDate` | `opportunity.estimatedclosedate` | `deals.closedate` | `deal.expected_close_date` |
| opportunity | `probability` | `Opportunity.Probability` | `opportunity.closeprobability` | `deals.hs_deal_stage_probability` | `deal.probability` |
| contact | `title` | `Contact.Title` | `contact.jobtitle` | `contacts.jobtitle` | `person.job_title` |
| contact | `opt-out flag` | `Contact.HasOptedOutOfEmail` | `contact.donotemail` | `contacts.hs_email_optout` | custom privacy field |
| activity | `date` | `Task.ActivityDate` or `Event.ActivityDate` | `activitypointer.scheduledend` | `engagements.timestamp` | `activity.due_date` |
| target | `period` | forecast or quota period field | forecast or goal period field | goal period field | goal period field |
If a product uses custom objects, map them only after confirming they satisfy the logical entity definition.
Do not map similarly named fields when their semantics differ.
For example, a field named status may mean lifecycle state, approval state, or forecast category.
Inspect allowed values before using a field as `stage`.

## Guardrails and refusals
Refuse to calculate rollups when required monetary fields or currencies are absent.
Refuse to label a record as in scope when the book rule cannot justify it.
Refuse to stage a write when the source record reference is missing.
Refuse to generate outreach to a contact when the opt-out flag is absent or true.
Refuse to use notes, workplace records, or public web pages as a substitute for CRM field mapping.
Refuse to treat a custom field as authoritative until the runner confirms its meaning.
Refuse to hide mapping uncertainty in a footnote.
When refusing, state the missing field or mapping, affected workflow, and safest next action.

## When in doubt
Ask rather than guess.
Use `Unknown`, `unmapped`, or `unavailable` explicitly.
Prefer a smaller, correct rollup over a broader, questionable one.
A CRM mapping is reusable only after the runner confirms it or the profile declares it.
If a future agent disagrees with a mapping, stop and ask for reconciliation before using either mapping.
