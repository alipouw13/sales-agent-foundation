# Role adoption playbooks

Every agent in this repository can help every revenue role.

The difference is the order of adoption.

A seller measured on booked revenue needs a different first week than a person measured on qualified meetings, technical win rate, retention, or forecast accuracy.

Use these playbooks to decide which agents should earn your trust first.

Read them with the repository contract in [`SPEC.md`](../../SPEC.md), the source mapping in [`config/data-sources.example.md`](../../config/data-sources.example.md), and the full agent list in [`AGENT-CATALOG.md`](../../.github/AGENT-CATALOG.md).

## Pick the role by measurement, not title

Your title may not match one of these files exactly.

That is fine.

Choose the file for the outcome you are held accountable for.

If you carry a number for booked revenue, start with Account Executive.

If you create qualified meetings at volume, start with SDR / BDR.

If you win technical confidence and enable the account team, start with Solution Engineer.

If you own one solution area across many accounts, start with Solution Specialist.

If you protect renewals, adoption, and expansion, start with Customer Success Manager.

If you manage a team forecast, start with Sales Manager.

## Role index

| Role | What this role is measured on | Start here |
| --- | --- | --- |
| Account Executive | Booked revenue against quota in named accounts or a territory. | [account-executive.md](./account-executive.md) |
| SDR / BDR | Qualified meetings created and pipeline sourced at high volume. | [sdr-bdr.md](./sdr-bdr.md) |
| Solution Engineer | Technical win rate, deal influence, and account team enablement. | [solution-engineer.md](./solution-engineer.md) |
| Solution Specialist | One solution area's revenue or consumption across many accounts. | [solution-specialist.md](./solution-specialist.md) |
| Customer Success Manager | Retention, adoption, and expansion in an installed base. | [customer-success-manager.md](./customer-success-manager.md) |
| Sales Manager | Team attainment, forecast accuracy, and coaching leverage. | [sales-manager.md](./sales-manager.md) |

## How to use a role file

First, copy [`config/profile.example.md`](../../config/profile.example.md) to your private profile and fill only the fields that are true for your seat.

Then map sources using [`config/data-sources.example.md`](../../config/data-sources.example.md).

Only `crm` is required.

The other sources improve output, but every agent should say what is unavailable instead of inventing.

Run the three week-one agents before you turn on the rest.

The goal is not to automate everything.

The goal is to make your existing operating rhythm less lossy.

## If your role is not covered

Revenue operations, partner or channel management, and sales leadership above first line should read the closest match.

Keep the same profile structure, source guardrails, and no-fabrication rules from [`copilot-instructions.md`](../../.github/copilot-instructions.md).

Then adapt the agent order to your measurement system.

For example, a revenue operations reader may borrow the Sales Manager rhythm but replace coaching outputs with data-quality actions.

A partner manager may borrow Account Executive and Customer Success Manager patterns but shift the book filter to partner-influenced accounts.

Do not add new agent names or skill names just to fit a title.

Use the catalog first, then specialize prompts and profile settings.
