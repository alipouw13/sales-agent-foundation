> **Global writing rule: never use em dashes.** Do not use the em dash character
> (U+2014) in anything you produce: prose, slides, documents, tables, captions,
> code comments, or commit messages. Use a comma, a colon, parentheses, or a
> second sentence instead. En dashes (U+2013) are also disallowed, use a hyphen
> or reword. This is enforced by `tools/validate_repo.py`.

# Project rules

This repository is a **foundation for a team of agents that help someone in a
revenue role do their job**. It ships agent definitions, reusable prompts, and
shared skills. It ships no application code, no credentials, and no data.

Read [`SPEC.md`](../SPEC.md) before changing anything. It holds the contracts
these rules enforce.

## Workflow, never skip a phase

1. **Spec.** Update `SPEC.md` first if the contract moves.
2. **Plan.** List the files you will touch and the verification step, before
   editing.
3. **Build.** One small, verifiable slice at a time.
4. **Test.** Run `python tools/validate_repo.py` after every slice. Zero errors.
5. **Validate.** Run the `validate` agent: re-check the executed work against the
   original request, `SPEC.md`, and these rules. Fix gaps before review.
6. **Review.** Run the `code-reviewer` agent over the diff.
7. **Ship.** One focused commit, push, open a pull request.

The five lifecycle personas that carry those phases live in
[`agents/`](agents/): `spec`, `plan`, `build`, `validate`, `code-reviewer`.

## Architecture rules, read before adding anything

- **Agents are prose, not code.** An agent is a markdown persona. If you find
  yourself wanting to write a script inside an agent, the work belongs in the
  host's existing tools instead.
- **No new authentication, ever.** This repo holds no credentials and performs
  no auth. Agents ask tools the host already has. If a workflow appears to need
  a new credential, the correct answer is "which existing tool already covers
  this", not "add auth here".
- **No vendor tool names in agent bodies.** Agents name **logical sources**:
  `crm`, `workplace`, `notes`, `web`, `decks`. The runner maps those to their
  real tools in `config/profile.md`. This is what makes the repo portable across
  Salesforce, Dynamics, HubSpot, Microsoft 365, and Google Workspace.
  Vendor names may appear in `docs/` and in `config/*.example.md` as worked
  examples, never in `.github/agents/*.agent.md`.
- **Skills are shared, agents are specific.** Anything two or more agents both
  need (a rubric, a taxonomy, an output schema, a citation rule) goes in a skill
  so their output stays comparable. Anything only one agent needs stays in that
  agent.
- **Degrade, never fabricate.** If a source is unmapped or returns nothing, the
  agent says so in that section and continues. Only an unavailable `crm` is
  fatal, because everything downstream would be invented.

## Content rules, the ones that keep this publishable

Every one of these is checked by `tools/validate_repo.py` where a machine can
check it. The rest are on you.

- **No customer data.** No company names as examples of *your* customers, no
  contact names, no titles attached to real people.
- **No personal identifiers.** No email addresses outside placeholder domains
  (`example.com`, `yourcompany.com`), no phone numbers, no record IDs, no GUIDs.
- **No numbers from a real book.** No quota, revenue, attainment, pipeline, or
  consumption figures. Ever. Not even "anonymized" ones.
- **No credentials.** No keys, tokens, connection strings, or bearer values.
- **Placeholders look like placeholders.** Use `<account name>`, `<first name>`,
  `${input:account:Account name}`. Never a plausible-looking fake that a reader
  could mistake for real data.

The validator enforces the mechanically checkable ones: email addresses, GUIDs
and long hex strings, credential patterns, dashes, links, and every structural
contract. It cannot detect a customer name, a phone number, or a real revenue
figure written as ordinary prose. Those are on you and on review, which is why
`code-reviewer` reads every diff for them.

## Authoring an agent

Follow [`docs/authoring-agents.md`](../docs/authoring-agents.md). The short
version:

1. Update `SPEC.md` if you are adding a group or changing a contract.
2. Create `.github/agents/<name>.agent.md` with frontmatter `name` (matching the
   filename stem) and a `description` that names the situations that should
   route to it. **The description is the routing contract.** The host model sees
   only that line when deciding whether to call your agent, so write it as if
   the reader has never seen the file, and include the phrases a human would
   actually say.
3. Include all six sections, in order: `## When to activate`,
   `## What it resolves (never hardcode)`, `## Process`, `## Output`,
   `## Guardrails`, `## Anti-patterns`.
4. Create the matching `.github/prompts/<name>.prompt.md`. Every runner-supplied
   value uses `${input:key:hint}`.
5. Add a row to [`AGENT-CATALOG.md`](AGENT-CATALOG.md).
6. Run `python tools/validate_repo.py`. Zero errors.
7. Run it end to end in a real session before you commit.

## Authoring a skill

1. `.github/skills/<name>/SKILL.md`, frontmatter `name` matching the directory.
2. The `description` must carry the trigger keywords, because that is how a
   skill gets loaded.
3. Prose only. No dependency, no credential, no network call required.
4. If only one agent will ever read it, put it in the agent instead.

## Guardrails every agent inherits

Restate these in each agent's `## Guardrails` section, adapted to what that
agent does. They are the reason this is safe to run against real systems.

1. **No fabrication.** Never invent a person, title, email address, quota,
   revenue figure, attainment percentage, quote, or proof point.
2. **Cite per claim.** External claims carry a URL, a date, and a verbatim
   excerpt. Internal claims name the record.
3. **Portable, never hardcoded.** Resolve identity, book, role, and targets at
   run time. Never carry an account, record ID, or number from a prior run.
4. **Sensitive output stays local.** Write to the profile's `output_dir`, which
   is gitignored. Never commit generated output.
5. **Drafts only.** Outreach agents draft. A human sends, from their own client.
6. **Propose, do not write.** Stage every CRM change for confirmation first.
7. **Public sources stay public.** Filings, transcripts, and news only, always
   attributed, and treated as sales signal rather than investment advice.
8. **No em dashes or en dashes.**

## Dependencies

There are none, and that is the point. `tools/validate_repo.py` is Python
standard library only. Do not add a package, a lockfile, or a build step.

## Boundaries

- **Always:** run `python tools/validate_repo.py` before committing.
- **Ask first:** adding an agent group, changing a logical source name, or
  loosening a guardrail.
- **Never:** commit customer data, credentials, real names, real numbers, or a
  filled-in `config/profile.md`.
