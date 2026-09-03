# Contributing

Thanks for improving this. The bar here is unusual: this repo ships prose that
an AI agent executes against real customer data, so a sloppy sentence is a bug.

## Before you start

Read [`SPEC.md`](SPEC.md) and
[`.github/copilot-instructions.md`](.github/copilot-instructions.md). They hold
the contracts. Everything below assumes you have.

## The lifecycle, never skip a phase

1. **Spec.** Update `SPEC.md` first if the contract moves.
2. **Plan.** List the files you will touch and the verification step, before
   editing.
3. **Build.** One small, verifiable slice at a time.
4. **Test.** `python tools/validate_repo.py` after every slice. Zero errors.
5. **Validate.** Run the `validate` agent against the original request.
6. **Review.** Run the `code-reviewer` agent over the diff.
7. **Ship.** One focused commit, push, open a pull request.

The five lifecycle personas in [`.github/agents/`](.github/agents/) carry those
phases: `spec`, `plan`, `build`, `validate`, `code-reviewer`.

## What we accept

| Contribution | Bar |
| --- | --- |
| A fix to an agent's process or thresholds | Explain the failure it prevents. "This reads better" is not a reason |
| A new anti-pattern | It must be a real failure you hit, not a hypothetical |
| A new skill | It must be read by two or more agents. Single-agent knowledge stays in the agent |
| A new agent | It must cover a recurring workflow the catalog does not. Include the agent, the prompt, and the catalog row |
| A new role playbook | It must be a role measured on something genuinely different from the six that exist |
| A validator check | It must catch a class of defect that has actually occurred |

## What we do not accept

- **Any customer data.** No company names as examples of customers, no contact
  names, no titles attached to real people.
- **Any real numbers.** No quota, revenue, attainment, pipeline, or consumption
  figures. Not even anonymized ones.
- **Any credential**, in any form.
- **Any personal identifier.** No email addresses outside placeholder domains,
  no phone numbers, no record IDs, no GUIDs.
- **A vendor tool name inside an agent body.** Agents name logical sources:
  `crm`, `workplace`, `notes`, `web`, `decks`. Vendor names belong in `docs/`,
  in `config/*.example.md`, and in the `crm-data-contract` skill only.
- **A loosened guardrail.** You may tighten. You may not remove "no
  fabrication", "propose never write", "drafts only", or "output stays local".
- **A new dependency.** There are none, and that is the point. The validator is
  Python standard library only.
- **Brand assets or brand guidelines**, including a customer's logo.

## Style

- **No em dashes and no en dashes.** Anywhere. Use a comma, a colon,
  parentheses, or a second sentence. This is enforced by the validator, and it
  is also the loudest tell that text was machine generated.
- Agent descriptions are third person and contain the phrases a human would say.
  Prompt descriptions are first person.
- Placeholders look like placeholders: `<account name>`, `<first name>`,
  `${input:account:Account name}`. Never a plausible-looking fake that a reader
  could mistake for real data.
- Explain **why** a rule exists, not just what it is. A rule without a reason
  gets deleted by the next person.
- Keep agent files readable. If one passes about 60 KB the validator warns, and
  that is usually a sign it should be a skill plus a thinner agent.

## Verification

```bash
python tools/validate_repo.py
```

Zero errors before every commit. CI runs the same command on push and pull
request, so a failing local run is a failing build.

Validation proves the file is well formed. It cannot prove the agent is any
good, so if you changed behaviour, run the agent end to end in a real session
first. In particular, unmap a source and confirm the agent degrades gracefully
instead of inventing. That is the test most changes fail.

## Commits and pull requests

- One focused change per commit. A message that says what changed and why.
- In the pull request, state which agents or skills change behaviour, and what
  you ran to verify.
- If you changed a skill, list the agents that read it, because you changed all
  of them.

## Reporting a problem

- **An agent fabricated something.** Open an issue with the agent name and what
  it invented. Do not include the customer data it invented it about. This is
  the highest priority defect class in this repo.
- **A guardrail did not hold.** Same, and mark it clearly.
- **The validator let something through.** See [`SECURITY.md`](SECURITY.md), use
  a private advisory rather than a public issue.

## Code of conduct

Be direct about the work and decent to the people. Review the content, not the
contributor. Assume the person who wrote the rule you are deleting had a reason,
and ask before you delete it.
