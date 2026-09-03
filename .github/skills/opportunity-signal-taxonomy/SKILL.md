---
name: opportunity-signal-taxonomy
description: buying signal, opportunity signal, signal taxonomy, revenue signal, whitespace signal, signal classification, trigger event
---

# Opportunity Signal Taxonomy

## Purpose

This skill is the controlled vocabulary for public events that may matter to a revenue team.
Every filing, call, news, portfolio, and outreach agent must classify the same event the same way.
A signal is an observed, dated, citable event, not a hunch, rumor, or account-plan opinion.
A motion family is the broad response path the seller may consider after the signal is verified.
If the source is missing, output `no signal asserted`.

## Core definitions

- **Signal:** A public event that changes likely priorities, constraints, risk, urgency, or timing.
- **Underlying event:** The real occurrence behind one or more articles, filings, or call comments.
- **Signal type:** One controlled label from this skill.
- **Signal family:** The group explaining why the event matters.
- **Strength:** The likely relevance of the verified event to sales planning.
- **Confidence:** Certainty that the event occurred and maps to the selected type.
- **Time-to-relevance:** The window in which the event may shape a business conversation.
- **Motion family:** Growth, efficiency, transformation, risk, resilience, competitive response, or partnership.

## Evidence requirements

Every signal needs a stable URL, publication date, and verbatim excerpt.
The excerpt must directly support the signal type.
Headlines, summaries, internal guesses, and uncited rumors do not qualify.
A signal corroborated by two independent public sources outranks a single-source signal of the same type.

## Signal strength scoring

| Score | Label | Evidence pattern | Use |
| --- | --- | --- | --- |
| 5 | Strong | Confirmed account-specific event, direct priority, clear current action | Rank first unless stale |
| 4 | Strong | Confirmed event with direct priority, but timing is less explicit | Rank above moderate signals |
| 3 | Moderate | Confirmed event with plausible priority connection | Use for discovery planning |
| 2 | Weak | Confirmed event with broad or generic relevance | Watchlist only |
| 1 | Weak | Thin, isolated, or early disclosure | Do not use alone |
| 0 | Withheld | No citable source, no excerpt, or unsupported inference | Output `no signal asserted` |

A negative signal can be strong without being a sales opening.

## Deduplication rules

Classify the underlying event once.
The same event reported through a filing, a call, and a news story is one signal with three citations, not three signals.
Repeating coverage of the same filing is not new momentum.
A press release copied into articles is not independent corroboration.
Create separate signals only when separate events have separate evidence and separate business implications.

## Motion family vocabulary

- **Growth:** New market, product, capacity, or revenue expansion conversation.
- **Efficiency:** Cost, margin, automation, consolidation, or productivity conversation.
- **Transformation:** Platform, data, AI, process, or operating model change.
- **Risk and compliance:** Regulatory, audit, security, legal, privacy, or governance response.
- **Resilience and support:** Stabilization, continuity, reliability, recovery, or service support.
- **Competitive response:** Differentiation, retention, win-back, or share defense.
- **Partnership:** Alliance, acquisition, divestiture, integration, or separation.

## Signal catalog

### Leadership and org change

#### LEADERSHIP_CHANGE
- Definition: A top executive, board-level, or equivalent operating role changes hands.
- Qualifying evidence: A filing, release, or transcript states the role change, effective date, and scope.
- Typical strength: Strong, because new leaders often reset priorities and review major programs.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget may pause during review, while urgency rises around the new agenda.
- Candidate motion family: Transformation or risk and compliance.
- Suggested next action: Build a neutral briefing on stated priorities and avoid assuming the prior agenda continues.

### Financial performance and pressure

#### EARNINGS_MISS
- Definition: Results or guidance fall below management expectations or market expectations cited by the source.
- Qualifying evidence: Filing, call transcript, or public report states the miss, driver, or lowered outlook.
- Typical strength: Strong and negative, because executive focus can change quickly.
- Typical time-to-relevance: Immediate.
- Budget and urgency: Discretionary budget may tighten, while urgency rises for cost, retention, and productivity.
- Candidate motion family: Efficiency or risk and compliance.
- Suggested next action: Do not celebrate the miss, instead offer a concise risk-reduction or cost-control hypothesis.

#### MARGIN_PRESSURE
- Definition: Management reports pressure on profitability, cash flow, cost, pricing, mix, supply, labor, or demand.
- Qualifying evidence: Source text links the pressure to a driver and affected business area.
- Typical strength: Strong, because margin pressure often drives efficiency programs.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget favors initiatives with clear savings, consolidation, automation, or faster cycle time.
- Candidate motion family: Efficiency.
- Suggested next action: Identify processes tied to the pressure and propose a measured discovery path.

#### COST_REDUCTION_PROGRAM
- Definition: The company announces or expands a cost reduction, restructuring, productivity, or simplification program.
- Qualifying evidence: Source states the program scope, business reason, timing, or affected cost categories.
- Typical strength: Strong and negative when tied to layoffs or closures, moderate when routine.
- Typical time-to-relevance: Immediate.
- Budget and urgency: New spend faces scrutiny, but funded work may exist for automation and support.
- Candidate motion family: Efficiency or resilience and support.
- Suggested next action: Keep messaging respectful, focus on helping teams do more with less, and avoid opportunism.

### Growth and expansion

#### MARKET_EXPANSION
- Definition: The company enters a new geography, segment, route to market, or customer category.
- Qualifying evidence: Public source states the expansion target, timing, and rationale.
- Typical strength: Moderate, because expansion requires execution but may move in stages.
- Typical time-to-relevance: This year.
- Budget and urgency: Budget may attach to localization, compliance, operations, analytics, and acquisition.
- Candidate motion family: Growth.
- Suggested next action: Identify operational bottlenecks that could slow the expansion.

#### PRODUCT_LAUNCH
- Definition: The company launches or materially expands a product, service, or platform.
- Qualifying evidence: Source states the offering, launch timing, customer target, or operational requirement.
- Typical strength: Moderate, because launches create enablement, support, data, and reliability needs.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget may exist for launch readiness, but urgency depends on public commitments.
- Candidate motion family: Growth or transformation.
- Suggested next action: Ask what systems, support model, and adoption metrics must be ready for launch.

### Technology and transformation

#### DIGITAL_TRANSFORMATION_PROGRAM
- Definition: The company names a digital, operating model, automation, or customer experience transformation.
- Qualifying evidence: Source states an initiative, sponsor area, objective, or measurable outcome.
- Typical strength: Strong, because the account has framed change as strategic.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget may exist, but scope and partner choice may be contested.
- Candidate motion family: Transformation.
- Suggested next action: Map the stated objective to outcomes, stakeholders, and proof requirements.

#### AI_DATA_INITIATIVE
- Definition: The company describes AI, analytics, automation, data platform, or decision intelligence investment.
- Qualifying evidence: Source states a use case, business process, governance need, or deployment goal.
- Typical strength: Strong when tied to named use cases, moderate when aspirational.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget may exist for pilots, data readiness, governance, and adoption.
- Candidate motion family: Transformation.
- Suggested next action: Separate production use cases from experimentation before proposing technology.

#### SECURITY_MODERNIZATION
- Definition: The company names cyber risk, identity, privacy, resilience, or security modernization as a priority.
- Qualifying evidence: Source states risk, program, incident response, control gap, or compliance driver.
- Typical strength: Strong when tied to incident or regulation, moderate when generic.
- Typical time-to-relevance: Immediate or this quarter.
- Budget and urgency: Budget is often defensive and time sensitive when risk is visible.
- Candidate motion family: Risk and compliance.
- Suggested next action: Use a risk language frame and ask what controls are already in motion.

### Risk regulatory and compliance

#### REGULATORY_ACTION
- Definition: A regulator, court, or public authority takes action requiring remediation, reporting, or controls.
- Qualifying evidence: Public source states the authority, action, issue area, and affected activity.
- Typical strength: Strong and negative, because deadlines and scrutiny can change priorities fast.
- Typical time-to-relevance: Immediate.
- Budget and urgency: Budget may move toward remediation, auditability, governance, and risk reduction.
- Candidate motion family: Risk and compliance.
- Suggested next action: Keep outreach factual, never punitive, and align only to relevant remediation support.

#### COMPLIANCE_DEADLINE
- Definition: A legal, industry, reporting, privacy, security, or operational compliance date affects the account.
- Qualifying evidence: Source states the requirement, deadline, affected process, or readiness gap.
- Typical strength: Moderate, strong when the deadline is near and the gap is specific.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Urgency is date-driven, and budget may attach to controls and reporting.
- Candidate motion family: Risk and compliance.
- Suggested next action: Confirm applicability and timing before suggesting a readiness workshop.

### Operational disruption

#### OUTAGE_INCIDENT
- Definition: The company experiences a material service, production, logistics, cyber, or customer-impacting outage.
- Qualifying evidence: Public source states the incident, impact area, timing, and recovery status.
- Typical strength: Strong and negative, because reliability and trust become immediate concerns.
- Typical time-to-relevance: Immediate.
- Budget and urgency: Budget may shift to stabilization, resilience, monitoring, continuity, and support.
- Candidate motion family: Resilience and support.
- Suggested next action: Lead with empathy and support, never a pitch, and offer help only if the relationship permits it.

### Competitive and market

#### COMPETITOR_PRESSURE
- Definition: The company names pressure from competitors, pricing, substitution, market share loss, or disruptive entrants.
- Qualifying evidence: Filing, transcript, or source states the pressure and affected segment or product.
- Typical strength: Moderate, because it signals urgency but may not point to a specific project.
- Typical time-to-relevance: This quarter.
- Budget and urgency: Budget may favor differentiation, customer experience, sales productivity, analytics, or retention.
- Candidate motion family: Competitive response.
- Suggested next action: Build a hypothesis around speed, differentiation, service quality, or retention.

#### CUSTOMER_CHURN_PRESSURE
- Definition: Public language indicates retention pressure, churn, lower renewal, reduced usage, or satisfaction decline.
- Qualifying evidence: Source states churn, renewal pressure, retention direction, or customer experience issue.
- Typical strength: Strong when explicit, moderate when inferred from demand weakness.
- Typical time-to-relevance: Immediate.
- Budget and urgency: Budget may shift toward customer experience, success operations, analytics, and support.
- Candidate motion family: Competitive response or resilience and support.
- Suggested next action: Focus on customer outcomes and retention operations, not new-logo selling.

### Partnership and M and A

#### ACQUISITION_ANNOUNCED
- Definition: The company announces an acquisition, merger, or pending integration.
- Qualifying evidence: Public source states the parties, rationale, expected timing, and integration scope if available.
- Typical strength: Strong, because integration creates systems, process, data, and governance work.
- Typical time-to-relevance: This quarter or this year.
- Budget and urgency: Budget may be controlled by integration governance and synergy targets.
- Candidate motion family: Partnership or transformation.
- Suggested next action: Map integration risks, duplicate systems, data migration, and continuity needs.

#### DIVESTITURE_SPIN
- Definition: The company announces a sale, separation, spinout, or business exit.
- Qualifying evidence: Source states the asset, scope, rationale, timing, and transition obligations if available.
- Typical strength: Strong, because separation creates urgent operational and data boundary needs.
- Typical time-to-relevance: Immediate or this quarter.
- Budget and urgency: Budget may exist for transition services, disentanglement, compliance, and continuity.
- Candidate motion family: Partnership, efficiency, or risk and compliance.
- Suggested next action: Ask what must be separated, kept running, secured, or reported by the transaction date.

## Negative signal handling

Negative signals include EARNINGS_MISS, COST_REDUCTION_PROGRAM, REGULATORY_ACTION, OUTAGE_INCIDENT, and any signal involving layoffs, customer harm, safety, breach, investigation, or public failure.
A negative signal changes the motion to efficiency, risk, resilience, or support rather than creating a sales opening.
Opportunism on bad news is the fastest way to lose an account.
If outreach is appropriate, it must be empathetic, factual, low pressure, and tied to a relationship or explicit need.
When in doubt, record the signal for planning and withhold outreach.

## Required evidence record

| Field | Required value |
| --- | --- |
| signal_id | One short id from this taxonomy |
| account | Placeholder or resolved account from the runner's authorized source |
| source_type | Filing, transcript, release, regulator notice, public news, or investor relations page |
| source_url | Stable public URL |
| publication_date | Date the source was published or filed |
| verbatim_excerpt | Exact text supporting the signal |
| strength | Strong, moderate, weak, or withheld |
| confidence | High, medium, or low |
| mapped_motion_family | One motion family from this skill |
| suggested_action | One concrete next action |

## Refusal and guardrails

No signal without a citable source, ever.
Refuse to classify rumors, unattributed summaries, unsourced social posts, or internal guesses as signals.
Refuse to invent source URLs, dates, excerpts, people, titles, budget, quota, revenue, or customer proof points.
Refuse to convert bad news into aggressive outreach.
Refuse to merge separate accounts, filer entities, or brands unless the source explicitly connects them.
State `insufficient evidence` when the event cannot be verified.
Use placeholders for accounts in examples, such as `<company>`.
Keep public-source analysis separate from internal CRM facts.
Treat every signal as a planning input, not a guarantee of intent, budget, or timing.
