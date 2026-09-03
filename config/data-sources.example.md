# Data sources (template)

Agents in this repo never name a vendor tool in their body text. They name a
**logical source**. This file is where logical sources become the real tools you
have. Copy it to `config/data-sources.md` (gitignored) if you want to keep notes
about your own wiring, or just fill in the `sources:` block in
`config/profile.md`.

## The five logical sources

| Logical source | Answers | Typical backing tool |
| --- | --- | --- |
| `crm` | Accounts, opportunities, contacts, deal team, activities, quota, close dates | A CRM MCP server (Salesforce, Dynamics 365, HubSpot, or your company's internal one) |
| `workplace` | Your email, calendar, chat, meetings, files, colleagues | A workplace-data skill or MCP server for Microsoft 365 or Google Workspace |
| `notes` | Your own notes, prior thinking, meeting notes, demo ideas | A notes MCP server pointed at Obsidian, Notion, or a folder of markdown |
| `web` | Public filings, transcripts, news, company sites | Built-in web search and fetch |
| `decks` | Reading and writing presentations | A presentation skill such as `pptx` |

Only `crm` is required. Everything else degrades: the agent says the source is
unavailable and continues with what it has.

## Contract each source must satisfy

An agent asks a source for a **capability**, not a tool name. If your tool can
answer the questions below, the agent works. If it cannot, map the source to
`unavailable`.

### `crm`

| Capability | The agent will ask for |
| --- | --- |
| `whoami` | The runner's own user record, so the book resolves to their seat |
| `list_accounts` | Accounts the runner owns or is on the team for |
| `list_opportunities` | Open and closed opportunities, with stage, amount, close date, product |
| `get_contacts` | Contacts on an account, with title and role |
| `get_deal_team` | Internal people attached to an account or opportunity, with role |
| `get_activities` | Logged calls, meetings, tasks, and their dates |
| `propose_write` | A staged change the runner confirms before it is applied |

Field names are normalized by the [`crm-data-contract`](../.github/skills/crm-data-contract/SKILL.md)
skill. Read that before you map anything, it is the translation layer between
your CRM's schema and what agents assume.

### `workplace`

| Capability | The agent will ask for |
| --- | --- |
| `search_mail` | Sent and received mail, filtered by person, account, or date |
| `search_chat` | Chat and channel messages |
| `list_meetings` | Calendar events, attendees, and recaps or transcripts if available |
| `find_people` | Colleagues, their titles, and their org relationship |

`search_mail` over **your own sent mail** is what the
[`outreach-voice`](../.github/skills/outreach-voice/SKILL.md) skill derives your
writing style from. Without it, drafts fall back to the manual voice settings in
your profile.

### `notes`

| Capability | The agent will ask for |
| --- | --- |
| `search` | Full text or semantic search across your notes |
| `read` | Read one note, or one section of a note |
| `append` | Add a dated section to an existing note |

### `web`

| Capability | The agent will ask for |
| --- | --- |
| `search` | A natural language question, answered with citations |
| `fetch` | Retrieve a specific URL, including SEC EDGAR and investor relations pages |

### `decks`

| Capability | The agent will ask for |
| --- | --- |
| `read` | Extract text and structure from an existing presentation |
| `write` | Create or edit slides |
| `render` | Rasterize slides to images for visual QA |

## Worked example: full coverage

Every source mapped. This is what an enterprise seller with a well-equipped
assistant looks like.

```yaml
sources:
  crm: "<your-crm-mcp-server>"
  workplace: "<your-workplace-data-skill>"
  notes: "<your-notes-mcp-server>"
  web: "built-in web search"
  decks: "<your-presentation-skill>"
```

Replace each placeholder with the exact tool name your assistant reports. If
your employer provides an internal CRM or workplace connector, its name goes
here, in your own gitignored `config/profile.md`, not in a committed file.

## Worked example: Salesforce seller with Google Workspace

```yaml
sources:
  crm: "salesforce-mcp"
  workplace: "google-workspace-mcp"
  notes: unavailable
  web: "built-in web search"
  decks: "google-slides-mcp"
```

## Worked example: minimum viable

```yaml
sources:
  crm: "hubspot-mcp"
  workplace: unavailable
  notes: unavailable
  web: "built-in web search"
  decks: unavailable
```

With this mapping, `account-brief` still produces a grounded brief from CRM plus
public web, and says plainly that it has no meeting or mail history. That is the
correct behaviour: less coverage, zero fabrication.

## A note on access

Every source above is something **you already have access to as a human**. These
agents do not create new access, do not hold credentials, and do not
authenticate. They ask a tool your assistant already has. If a workflow seems to
need a new credential, the answer is to find the tool that already covers it,
not to add authentication here. See
[`.github/copilot-instructions.md`](../.github/copilot-instructions.md).
