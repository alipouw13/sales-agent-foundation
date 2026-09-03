---
name: sec-filings-retrieval
description: 10-K, 10-Q, 8-K, SEC filing, EDGAR, annual report, quarterly report, CIK lookup, filing retrieval, investor relations
---

# SEC Filings Retrieval

## Purpose

This skill tells agents how to resolve a company to public filings and cite them correctly.
It uses public disclosure only.
It does not require repo credentials, private data, or a network call to understand the contract.
When retrieval is available, use public endpoints and public investor relations pages.
When retrieval is not available, state that the filing could not be retrieved.
Never substitute news coverage for a filing when the task asks for a filing.
News may provide context, but it is not the filing record.

## Source hierarchy

Use the most direct public source available.
Prefer the filed document over an exhibit summary.
Prefer the regulator page over an aggregator page.
Prefer the company investor relations page only when the regulator filing is unavailable, non-US, or the company is private.
Use public news only to locate possible filing events, not to quote filing content.
Every claim from a filing must carry a filing citation.
Every quoted figure must retain its units and period.

## Filer resolution principle

Resolve the company name to the correct filer entity before retrieving documents.
The sales account name may be a brand, subsidiary, product line, acquired company, or parent family.
The filer entity is the legal registrant that files the disclosure.
Do not assume the brand name equals the filer name.
Do not assume a ticker maps to the current filer without checking.
Do not assume a subsidiary files separately.
Do not assume a recently acquired company still files.
Do not assume a private company has public filings.
When the correct filer is uncertain, report the ambiguity and withhold filing conclusions.

## Common resolution traps

- A subsidiary may file separately, may be consolidated into a parent filing, or may not file at all.
- A brand name may differ from the legal filer name.
- A recently acquired company may stop filing after the transaction closes.
- A ticker can be reassigned, changed, retired, or associated with a different security.
- A parent may file under a name that does not match the account's go-to-market brand.
- Foreign issuers may file different forms or rely on home-country disclosure.
- Investor relations pages may keep old documents after the filing obligation changed.
- Search results may include unrelated companies with similar names.
- Shell entities and predecessor entities can make period comparison misleading.
- Amendments may supersede or correct an earlier filing.

## CIK lookup path

Use the Central Index Key, or CIK, as the stable SEC filer identifier.
The lookup path is:

1. Start with the account name, ticker if supplied, and any known parent or subsidiary context.
2. Search the SEC company ticker lookup file at https://www.sec.gov/files/company_tickers.json when a ticker is available.
3. Search EDGAR company name results when the name is available but ticker is absent.
4. Confirm the filer by matching legal name, ticker, state or country if available, and business description.
5. Convert the CIK to the zero-padded format required by submissions URLs.
6. Retrieve the submissions index at `https://data.sec.gov/submissions/CIK<zero-padded-cik>.json`.
7. Select the filing accession and primary document for the needed form and period.
8. Record the filer entity used, not just the sales account name.

Do not paste a real CIK into committed examples.
Use `<zero-padded-cik>` as the placeholder.
If the CIK match is uncertain, do not proceed as if it is certain.

## EDGAR full-text search

Use EDGAR full-text search when the task is topic-driven or when the filer is unclear.
The public search interface is https://www.sec.gov/edgar/search/.
Search by company name, ticker, form type, filing date range, and topic terms.
Use full-text search to locate sections or exhibits, then cite the actual filing document.
Do not cite the search result snippet as the source of truth.
If multiple similar filers appear, compare filer details before selecting one.
If full-text search finds only an exhibit, check whether the exhibit is part of the desired filing.
If the filing is amended, cite the version actually used.

## Submissions endpoint

Use the submissions endpoint to list a filer's recent forms and primary documents.
The pattern is `https://data.sec.gov/submissions/CIK<zero-padded-cik>.json`.
The endpoint helps identify form type, accession number, filing date, reporting date, and primary document.
Use the primary document URL for quotations whenever possible.
If the desired filing is older than the recent submissions list, use archive access from the filing page or EDGAR search.
Record both filing date and period covered.
Do not treat filing date as period end date.
Do not treat period end date as freshness date.
Freshness is based on filing date unless the task asks about the reporting period.

## Request etiquette

Public SEC access has rules and expectations.
Use a descriptive user agent that identifies the requester or application context.
Do not use generic or misleading user agent text.
Do not commit contact details into this repository.
Respect the SEC published rate limit, commonly stated as no more than ten requests per second.
Use backoff when responses indicate throttling or access limits.
Avoid bulk scraping when a small number of targeted filings answers the task.
Cache within the current run when the host allows it, but do not add cached filing data to the repo.
Do not bypass access controls, blocks, or robots guidance.
If access fails, report the failure and ask the runner to retry through an approved host tool.

## Form types for sales signal detection

| Form type | What it is good for | Sales signal use |
| --- | --- | --- |
| 10-K | Annual report with business, risk factors, MD&A, financial statements, controls, and long-form strategy | Strategy, risk, major initiatives, operating model, customer concentration, capital priorities |
| 10-Q | Quarterly report with interim results, updated risks, liquidity, and quarter-specific change | Recent pressure, demand shifts, margin movement, cost actions, litigation updates |
| 8-K | Current report for material events between periodic filings | Trigger events, leadership changes, transactions, incidents, restructurings, guidance updates |
| DEF 14A | Proxy statement for governance, executive priorities, compensation-linked metrics, and board matters | Priority indicators, measured outcomes, risk oversight, leadership incentives |
| S-1 | Registration statement for a pre-IPO company | Business model, growth strategy, risks, use of proceeds, customer and market narrative |
| 20-F | Annual report for many non-US private issuers listed in the United States | Annual strategy and risks when the issuer is foreign |
| 40-F | Annual report for certain Canadian issuers listed in the United States | Annual disclosure bridge for eligible issuers |


## 8-K item numbers that often matter

| Item | Typical meaning | Signal relevance |
| --- | --- | --- |
| 1.01 | Material definitive agreement | Partnerships, major customers, financing, supplier or commercial commitments |
| 1.03 | Bankruptcy or receivership | Severe risk, support posture only |
| 2.01 | Completion of acquisition or disposition | M and A integration or separation |
| 2.02 | Results of operations and financial condition | Earnings update, guidance context, performance pressure |
| 2.05 | Costs associated with exit or disposal activities | Restructuring, layoffs, facility exit, efficiency pressure |
| 2.06 | Material impairments | Asset pressure, strategic reset, demand or valuation concerns |
| 5.02 | Departure, election, or appointment of directors or certain officers | Leadership and governance change |
| 7.01 | Regulation FD disclosure | Investor update, strategic or financial communication |
| 8.01 | Other events | Company-defined material update, review carefully |
| 9.01 | Financial statements and exhibits | Transaction support documents and exhibits |

Item numbers guide triage only.
Always read the item text before classifying a signal.
Do not infer a signal from an item number alone.

## Finding the right section inside a long filing

Start with the form type and question.
Use the document table of contents when available.
Search within the filing for exact section labels and topic terms.
Use these common section targets:

| Question | Likely section |
| --- | --- |
| What does the company do and where is it focused | Business |
| What could go wrong | Risk Factors |
| What changed in the period | Management's Discussion and Analysis |
| Why did results change | Results of Operations |
| Can it fund operations | Liquidity and Capital Resources |
| What major legal issues exist | Legal Proceedings or Contingencies |
| What controls or audit issues matter | Controls and Procedures |
| What priorities affect executives | DEF 14A compensation discussion |
| What event just happened | 8-K item text and exhibits |

When searching, use both plain language and filing language.
For example, search `restructuring`, `exit costs`, `impairment`, `liquidity`, `cybersecurity`, `supply`, `customer`, `competition`, and `regulation`.
After locating a section, read surrounding paragraphs to avoid quoting out of context.
If a table contains the key figure, cite the table title and retain units and period.
If the filing uses inline XBRL, quote the visible document text, not extracted fragments that lose context.

## Non-US companies

Not every public company files 10-K or 10-Q forms.
For foreign issuers that file with the SEC, check 20-F, 40-F, 6-K, and related exhibits.
For companies listed outside the United States, look for home-country regulator filings and annual reports.
Use the investor relations site when it hosts official annual reports, interim reports, or exchange filings.
State the regulator or source used.
Do not force a US form taxonomy onto a non-US filer.
When comparing periods, compare equivalent source types when possible.
If only an annual report is available, state that quarterly filing evidence is unavailable.

## Private companies

Private companies may have no public filing record.
Some private companies publish annual reports, bond offering documents, sustainability reports, or regulator disclosures.
Use only documents that are public and attributable to the company or regulator.
If no public disclosure exists, say `no public filing found for <company>`.
Do not substitute news articles for filings.
Do not infer private financial performance from peer filings.
Do not invent a parent filer unless the source establishes the ownership relationship.
If a private company was recently acquired, check whether the parent filing discusses it.
If the parent filing does not discuss it, say so.

## Citation shape

Every filing citation must include:

| Field | Required value |
| --- | --- |
| company | Account placeholder or resolved account name |
| filer_entity | Legal filer name used for retrieval |
| form_type | Form such as 10-K, 10-Q, 8-K, DEF 14A, S-1, 20-F, or 40-F |
| period_covered | Reporting period, fiscal year, event date, or proxy year stated by the filing |
| filing_date | Date the document was filed or published |
| section | Section name, item number, exhibit, table, or page label |
| verbatim_excerpt | Exact filing text supporting the claim |
| document_url | Public URL to the filing document or official report |

The citation must be close enough for another agent to find the same text.
If the document URL is unavailable but the filing page is available, cite the filing page and state the limitation.
If the section name is unavailable, cite the item number or table label.
Never cite only the company home page.

## Freshness rule

Always state the filing date and how stale the filing is.
Freshness language must be explicit, such as `filed <date>, approximately <age> old as of <current date>`.
A signal from an eleven month old filing is not current unless a newer source confirms it remains relevant.
A current 8-K can supersede an older 10-K on the same event.
A recent 10-Q can update risk, liquidity, and performance language from an older 10-K.
A DEF 14A may be fresh for executive incentives but stale for operational status.
When staleness affects confidence, lower confidence or mark the signal as historical context.
Do not hide stale evidence behind present-tense wording.

## Figure and metric handling

Never quote a number without units and period.
Never paraphrase a figure.
Use the exact figure as written in the filing, including scale words, units, and table context.
If the filing gives a range, preserve the range and the period.
If the filing compares periods, preserve both periods.
If a table has footnotes, read the relevant footnote before using the figure.
If the unit is unclear, do not use the figure.
If the period is unclear, do not use the figure.
Do not convert currencies, units, percentages, or time periods unless the filing itself provides the conversion.

## Retrieval workflow contract

Follow this sequence for every filing request:

1. Capture the requested company, suspected parent, ticker if supplied, geography, and filing type.
2. Resolve the filer entity and record the resolution confidence.
3. Choose SEC EDGAR, home-country regulator, investor relations, or `no public filing found`.
4. Retrieve the document or identify why it cannot be retrieved.
5. Identify form type, period covered, filing date, and document URL.
6. Navigate to the relevant section using table of contents, item number, or targeted terms.
7. Extract a verbatim excerpt with enough surrounding context.
8. Apply freshness language.
9. Return the citation shape exactly.
10. If extracting a sales signal, pass the cited excerpt to the signal taxonomy rather than inventing a signal.

Do not skip filer resolution because a search result looks obvious.
Do not skip freshness because a filing is official.

## Refusal and guardrails

Refuse to present an aggregator's summary as the filing.
Refuse to infer a disclosure that is not in the document.
Refuse to quote a number without units and period.
Refuse to paraphrase a figure.
Refuse to fabricate filer entities, CIKs, dates, URLs, sections, excerpts, or figures.
Refuse to treat private-company news as a filing.
Refuse to bypass public endpoint etiquette or access limits.
Refuse to provide investment advice, trading conclusions, or valuation recommendations.
Use placeholders such as `<company>` and `<zero-padded-cik>` in examples.
When the evidence is missing, say exactly what is missing and stop at that boundary.
