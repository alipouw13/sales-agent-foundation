# Security and data handling

This repository contains **no application code, no credentials, and no customer
data**. It is a set of markdown agent definitions, prompts, and playbooks. That
shapes what "security" means here.

## What this repo will never contain

- Credentials of any kind: API keys, tokens, connection strings, certificates.
- Customer names, contact names, email addresses, phone numbers.
- Quota, revenue, attainment, or pipeline figures.
- Tenant, subscription, or record identifiers.

`tools/validate_repo.py` enforces this mechanically on every push: it fails the
build on any email address outside a placeholder domain, any bare GUID, and any
value that looks like a hardcoded credential.

## What you must keep local

When you run these agents against your own systems, the output is sensitive even
though the repo is not. Account briefs, portfolio dashboards, stakeholder maps,
and outreach drafts blend your employer's customer data with your own numbers.

- `.gitignore` already excludes `artifacts/`, `out/`, `config/profile.md`, and
  `*.local.*`. Point `output_dir` in your profile at one of those paths.
- Never commit a generated artifact, even a redacted one.
- If you fork this repo inside your company, keep the fork private unless you
  have re-run the validator and reviewed every diff for customer data.

## Reporting a vulnerability

If you find a way this repo could leak data, or a defect in the validator that
lets sensitive content through, open a **private security advisory** on the
repository rather than a public issue. Include the file, the line, and what the
validator failed to catch.

Please do not include real customer data in the report. Reproduce with a
placeholder.

## Responsible use

These agents read from systems you already have access to and produce drafts for
you to review. They do not send email, they do not write to a CRM without
confirmation, and they never claim a source they did not read. If you change an
agent in a way that removes one of those guardrails, you own the consequences.
Check your employer's policy on automated access to CRM and workplace data
before you point an agent at production systems.
