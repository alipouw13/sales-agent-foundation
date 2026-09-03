---
name: industry-context
description: Trigger for industry context, why now, peer evidence, sub-vertical, competitive pressure, industry pressure, peer benchmark, market context.
---
# Industry Context Contract
## Purpose
This skill defines how agents build credible market and industry context for revenue work.
It answers why now without inventing urgency.
It is a sourcing and inference contract, not a message-writing style guide.
Agents use public company and market information from `web`, plus internal context from `crm`, `notes`, `workplace`, and `decks` only to frame the account ask.
Agents must not name vendor-specific tools.
Agents must not use private personal information to support public market claims.
Every claim must be sourced or clearly labeled as unsupported.
If evidence is too thin, the correct output is not yet supportable.
## Core terms
| Term | Definition |
| --- | --- |
| Industry | A broad market category that groups organizations by the type of work they do. |
| Sub-vertical | A narrower segment inside an industry with distinct buyers, regulations, operating model, economics, and technology pressures. |
| Peer | An organization comparable enough that its public disclosure can evidence a pressure that may be relevant to the target account. |
| Peer datapoint | One sourced public fact about one qualifying peer, read by the agent, with citation and excerpt. |
| Independent datapoints | Datapoints that do not merely repeat the same original source or syndicated article. |
| Why-now claim | A concise statement that a market, regulatory, operational, financial, or technology pressure makes action timely. |
| Account-specific claim | A statement that the named account has a specific pressure, need, program, risk, or priority. |
| Analogy | A bounded comparison showing that a pressure exists among peers, not proof that the account has the same pressure. |
| Not yet supportable | The required threshold is not met, so the agent must not assert the claim. |
## Sub-vertical rule
The broad industry is too coarse to be useful.
Agents must resolve the sub-vertical before making a why-now claim.
A sub-vertical must be specific enough that peer choice and pressure logic change.
Use the account's own description first when available.
Then use public business descriptions, product lines, service model, region, buyer type, and regulatory context.
If the sub-vertical cannot be resolved, state unknown and do not assert a tailored why-now claim.
Broad labels such as healthcare, financial services, manufacturing, retail, public sector, and technology are starting points only.
They are not sufficient final context.
## Sub-vertical worked illustration
Use generic illustrations only.
Inside a broad industry such as healthcare, pressures differ sharply.
A hospital operator may face staffing constraints, patient throughput, care quality reporting, and system interoperability pressure.
A life sciences manufacturer may face clinical trial cycle time, quality documentation, regulatory submissions, and supply continuity pressure.
A payer may face claims accuracy, member service cost, fraud detection, and compliance reporting pressure.
The broad industry label is the same.
The economic buyer, peer set, proof points, and risk vocabulary are different.
Therefore an agent must not reuse one healthcare why-now claim across all three sub-verticals.
The same rule applies to any industry.
## Peer qualification rule
A peer must match the account on enough dimensions to make the comparison useful.
Use these dimensions.
| Dimension | Required comparison |
| --- | --- |
| Sub-vertical | Same sub-vertical or a directly adjacent operating model. |
| Size band | Similar scale band, such as emerging, mid-market, enterprise, regional leader, or global operator. |
| Regulatory regime | Similar legal, reporting, privacy, safety, or public-sector obligations. |
| Business model | Similar revenue model, delivery model, customer base, and margin pressure. |
| Geography | Same region when regulation, labor, infrastructure, or market maturity matters. |
| Technology pattern | Similar digital channel, data intensity, operational footprint, or platform dependency. |
A peer does not need to match every dimension.
A peer must match sub-vertical plus at least two other dimensions.
If regulation is central to the claim, regulatory regime must match.
If geography is central to the claim, geography must match.
If business model is central to the claim, business model must match.
Document which dimensions matched and which did not.
## Peer evidence threshold
A why-now claim based on peer evidence requires at least three independent peer datapoints.
Those datapoints must come from at least two different qualifying peer organizations.
At least two datapoints must come from sources ranked peer public disclosure or stronger in the source hierarchy.
A single trade article naming multiple peers counts as one datapoint unless the article quotes separate original sources that the agent read.
A vendor case study counts only as vendor-published material and cannot satisfy the independent evidence threshold by itself.
If the threshold is not met, the agent must say not yet supportable.
Do not stretch by using weakly related peers.
Do not treat the account's broad industry as enough to qualify a peer.
Do not turn one public quote into an industry trend.
## Source hierarchy
Use the strongest available source for each claim.
| Rank | Source type | Strength | Use rule |
| --- | --- | --- | --- |
| 1 | Account's own public disclosure | Strongest | Can support an account-specific claim when the excerpt directly says it. |
| 2 | Peer's public disclosure | Strong | Can support a pressure analogy when the peer qualifies. |
| 3 | Regulator or standards body | Strong | Can support regulatory or standards pressure. |
| 4 | Quality trade press | Moderate | Can support market activity when independently reported and dated. |
| 5 | Industry analyst report | Moderate | Can support structured market framing when source, date, and excerpt are available. |
| 6 | Vendor-published material | Weakest | May provide examples, but must always be labeled vendor-published. |
Vendor-published material must always be labeled vendor-published.
Vendor-published material must never be presented as independent evidence.
When stronger and weaker sources conflict, prefer the stronger source and state the conflict if material.
When all available evidence is vendor-published, say the claim is vendor-supported only, not independently supported.
## Citation shape
Every external claim must include a citation with this shape.
| Citation field | Required value |
| --- | --- |
| Source name | The public name of the source or publisher. |
| Source type | One value from the source hierarchy. |
| Publication date | Date shown by the source, or unknown if absent. |
| URL | `<source URL>` or the URL read by the agent. |
| Verbatim excerpt | Exact source wording that supports the claim. |
A citation is not complete without a verbatim excerpt.
Do not cite a source that the agent has not actually read.
Do not cite a search result snippet as if it were source text.
If a source is behind access limits and the agent cannot read it, do not use it as evidence.
If the date is missing, mark publication date as unknown and apply the most conservative freshness window.
## Freshness windows by claim type
Freshness depends on claim type.
Use the date the agent runs as the reference date.
| Claim type | Fresh window | Stale after | Rule |
| --- | --- | --- | --- |
| Regulatory deadline | Until the deadline passes, then 90 days for aftermath. | 90 days after the deadline unless enforcement is continuing. | A future deadline remains fresh if still active. |
| Regulation or standard change | 24 months. | 24 months unless explicitly still in force and relevant. | Cite the effective date and current status. |
| Account strategic priority | 12 months. | 12 months unless repeated in newer disclosure. | Prefer account's own public disclosure. |
| Peer investment or program | 12 months. | 12 months unless there is a later update. | Use as pressure analogy only. |
| Technology trend | 9 months. | 9 months unless supported by newer adoption or standards evidence. | Avoid generic hype. |
| Operational disruption | 6 months. | 6 months unless still reported as active. | Include region and scope. |
| Financial or margin pressure | 12 months. | 12 months unless repeated in newer reporting. | Cite account or peer disclosure. |
| Security threat pattern | 6 months. | 6 months unless a regulator, standard, or recent incident keeps it current. | Avoid fear-based unsupported claims. |
| Labor or skills pressure | 12 months. | 12 months unless updated by newer market data. | Match geography when material. |
| Supply chain pressure | 9 months. | 9 months unless active disruption continues. | Include geography and category. |
If a claim uses multiple sources, the claim freshness is the age of the source that directly supports the claim.
Do not refresh an old claim by citing a newer article that merely repeats it.
## Claim support levels
Use these labels in outputs.
| Support level | Definition | Allowed language |
| --- | --- | --- |
| Account-confirmed | Account's own public disclosure directly supports the claim. | The account says or discloses. |
| Peer-supported | Peer threshold is met and citations qualify. | Peers in the same sub-vertical are reporting. |
| Regulator-supported | Current regulator or standards source supports the timing. | Regulation or standard creates pressure. |
| Market-indicated | Trade press or analyst evidence suggests a market pattern but peer threshold is incomplete. | Market signals suggest. |
| Vendor-supported only | Only vendor-published sources support the claim. | Vendor-published examples suggest, independent support not found. |
| Not yet supportable | Threshold is not met or sources are stale. | Not yet supportable from sources read. |
Never upgrade support level because the claim would be useful for outreach.
Never present market-indicated evidence as account-confirmed.
## Analogy rule
A peer example is evidence that a pressure exists.
A peer example is not evidence that the target account has that pressure.
Agents must state the inference explicitly.
Use this structure.
| Element | Required wording |
| --- | --- |
| Peer fact | A qualifying peer publicly reported the pressure. |
| Similarity basis | The peer qualifies because of listed dimensions. |
| Bounded inference | This suggests the pressure may be relevant to `<account name>`, not that `<account name>` has confirmed it. |
| Account check | State what account-specific source would confirm or refute it. |
Do not elide the difference between pressure exists and account has pressure.
Do not write as if peer action proves account urgency.
## No-fabrication rules
Never invent a statistic.
Never cite a number without its source and publication date.
Never present an aggregated industry average without naming who aggregated it.
Never reuse a claim whose source the agent has not actually read.
Never fill missing publication dates with guessed dates.
Never paraphrase a source so aggressively that the excerpt no longer supports the claim.
Never turn vendor-published material into independent evidence.
Never claim an account has a priority unless the account's own public disclosure or authorized internal source supports it.
Never cite private internal belief as market fact.
## Output contract
Every industry-context output must include these sections.
1. Resolved sub-vertical.
2. Why-now claims by support level.
3. Peer evidence table.
4. Source hierarchy notes.
5. Freshness assessment.
6. Analogy and inference statement.
7. Unsupported or not yet supportable claims.
8. Privacy boundary.
The peer evidence table must include peer qualification dimensions.
The why-now section must separate account-confirmed claims from peer-supported analogies.
Unsupported claims are useful.
They prevent the outreach agent from overstating the case.
## Privacy boundary
Use public company and market information only for industry context.
Do not include any individual's personal information.
Do not infer anything about a named individual from public sources.
Do not combine public sources with private personal attributes to create a profile.
Do not scrape personal social profiles, personal contact details, or personal activity.
Do not cite private messages, private notes, or private meetings as public industry evidence.
Internal sources may identify the target account and current sales context, but they do not become public citations.
If an industry claim would require personal information to support it, do not make the claim.
Generated outputs that combine account context with industry claims must stay in the runner's configured local output area.
Never commit generated account-specific research or personal data.
## Anti-patterns
Do not start with a broad industry and stop there.
Do not use a famous company as a generic customer example.
Do not use a vendor case study as independent proof.
Do not assert urgency because a topic is trendy.
Do not cite a number without date and source.
Do not ignore stale dates.
Do not imply the account has a pressure when only a peer has disclosed it.
Do not use private personal data to strengthen a public market claim.
