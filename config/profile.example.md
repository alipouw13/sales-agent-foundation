# Runner profile (template)

Copy this file to `config/profile.md` and fill it in. `config/profile.md` is
gitignored. Every agent in this repo reads it to tailor its output to you.

Keep this file free of actual numbers. Name your quota buckets, do not record
their values. Agents pull live figures from your CRM at run time, which is the
only way the numbers stay right.

```yaml
# ---------------------------------------------------------------------------
# Who you are
# ---------------------------------------------------------------------------
role: account-executive        # one of: account-executive | sdr-bdr |
                               # solution-engineer | solution-specialist |
                               # customer-success-manager | sales-manager
role_title: "Account Executive, Enterprise Financial Services"

segment: enterprise            # enterprise | commercial | smb | public-sector
region: "North America"

# How your book is defined. Drives how every agent resolves "my accounts".
book_shape: named-accounts     # named-accounts | territory | vertical | patch
book_filter: "accounts where I am the owner or on the deal team"

# ---------------------------------------------------------------------------
# What you are measured on
# ---------------------------------------------------------------------------
# Bucket names only. Agents read the values from the CRM or your quota system.
targets:
  - name: "New business bookings"
    period: fiscal-year
    source: crm
  - name: "Consumption / usage growth"
    period: fiscal-quarter
    source: crm
  - name: "Renewal retention"
    period: fiscal-year
    source: crm

fiscal_year_start: "07-01"     # MM-DD, so agents compute the right period

# ---------------------------------------------------------------------------
# What you sell
# ---------------------------------------------------------------------------
# Used to compute whitespace: what an account has not bought yet.
solution_catalog:
  - "Data platform and analytics"
  - "AI and agent platform"
  - "Cloud migration and modernization"
  - "Security and governance"
  - "Business applications"

# Competitors agents should recognize in filings, calls, and news.
competitors:
  - "Competitor A"
  - "Competitor B"

# ---------------------------------------------------------------------------
# Where your data comes from
# ---------------------------------------------------------------------------
# Logical source name to the tool that answers it. See
# config/data-sources.example.md for the full contract and worked examples.
# Set a source to `unavailable` and agents will say so rather than invent.
sources:
  crm: "<your CRM MCP server name>"
  workplace: "<your mail / calendar / chat skill name>"
  notes: "<your notes MCP server name, or unavailable>"
  web: "built-in web search"
  decks: "<your presentation skill name, or unavailable>"

# Optional. Declares which sources this role actually depends on, so an agent
# can tell the difference between a source that is missing and a source that was
# never going to matter for you. Agents degrade quietly on anything listed under
# can_live_without, and say so loudly for anything under matters_most.
source_importance:
  matters_most:
    - crm
    - workplace
  can_live_without:
    - decks

# ---------------------------------------------------------------------------
# How you sound
# ---------------------------------------------------------------------------
voice:
  derive_from: workplace       # workplace | manual
  # Used when derive_from is manual, or as a floor when there is not enough
  # sent mail to derive a profile from.
  greeting: "Hi <first name>,"
  sign_off: "Thanks,\n<your first name>"
  sentence_length: short
  max_words_first_touch: 120
  banned_phrases:
    - "I hope this email finds you well"
    - "circling back"
    - "synergies"
    - "touch base"
  never_use_em_dashes: true

# ---------------------------------------------------------------------------
# Where output goes
# ---------------------------------------------------------------------------
# Must be a gitignored path. Agent output blends customer data with your book.
output_dir: "artifacts/"

# ---------------------------------------------------------------------------
# Guardrail overrides (tighten only, never loosen)
# ---------------------------------------------------------------------------
guardrails:
  crm_writes: propose-only     # propose-only | disabled
  outreach: draft-only         # draft-only | disabled
  external_sources: public-only
```

## Filling it in

| Field | How to decide |
| --- | --- |
| `role` | Pick the closest match. It selects which agents lead and which are supporting. See [docs/roles/](../docs/roles/). |
| `book_shape` | If you have a named account list, use `named-accounts`. If you own everything in a geography or size band, use `territory`. |
| `targets` | Copy the bucket names off your comp plan. Names only. |
| `solution_catalog` | The product or play names your CRM uses, so whitespace math lines up with your opportunity records. |
| `sources` | Run your assistant's tool list and paste the actual names. Anything you do not have, set to `unavailable`. |
| `source_importance` | Optional. Which sources your role genuinely depends on, so agents know which absences to flag loudly. Your role playbook in `docs/roles/` suggests a starting split. |
| `voice.derive_from` | `workplace` gives a much better result, because the agent reads how you actually write. Use `manual` if you cannot expose sent mail. |
| `output_dir` | Leave it as `artifacts/` unless you have a reason. It is already gitignored. |

## What agents do when a field is missing

They say so and continue. An agent that cannot resolve `notes` writes "no notes
source configured" in that section rather than inventing history. An agent that
cannot resolve `crm` stops and tells you, because everything downstream would be
fabrication.
