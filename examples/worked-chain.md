# A worked chain

The value in this repo is not any single agent. It is the handoffs. This page
walks one signal from "something happened in the news" to "a draft I would
actually send", showing what each agent contributes and, more usefully, where
each one is allowed to stop the chain.

Everything below uses placeholders. No real account, person, or number appears
here, and none should ever appear in this file.

---

## The chain

```
market-news-scout      finds the signal
        |
account-intel-360      finds who it affects and who to talk to
        |
industry-analyst       finds the evidence that makes it credible
        |
motion-strategist      picks the framing for that person's level
        |
outreach-writer        drafts it in your voice
        |
        you            read it, verify the citations, and send it yourself
```

`outreach-orchestrator` runs this whole chain for you. Running the steps
individually is worth doing once, so you can see where the quality comes from
and where it leaks.

---

## Step 1: `market-news-scout`

**You ask:** for a news sweep across your book over the last seven days.

**It resolves:** your book from `crm`, then public news per account.

**What comes back** is not a news digest. It is a short list of events that
survived a hard filter, each classified with the `opportunity-signal-taxonomy`
vocabulary and scored with the `sentiment-analysis` rubric.

```
Signal: leadership-change (strong, this quarter)
Account: <account name>
Source:  <publication>, <URL>, published <date>
Excerpt: "<verbatim excerpt from the article>"
Note:    Same event also appears in <other publication>, deduplicated.
```

**Where it stops:** most accounts return nothing, and it says so rather than
padding. If it cannot find a citable source, there is no signal. That is the
point of the filter.

**What you check:** the excerpt is verbatim and the date is recent enough to
matter.

---

## Step 2: `account-intel-360`

**You ask:** who this signal affects at that account.

**It resolves:** the account family and which entity the signal actually belongs
to (this matters more than people expect, because pipeline often sits on a
sibling entity), the buying committee, and contact freshness.

**What comes back** is a ranked stakeholder list in the shape the
`stakeholder-mapping` skill defines: inferred buying-committee role, role
confidence with the evidence behind it, last interaction date, and whether a
warmer internal path exists.

**Where it stops:** if the account has no identified economic buyer and no
executive contact inside the freshness window, it reports that as a **coverage
gap**, which is a finding in its own right and often more valuable than the
outreach you were planning.

**What you check:** the highest-ranked contact is frequently not the most senior
person. If it ranked the CEO first, ask why.

---

## Step 3: `industry-analyst`

**You ask:** why this matters now, for this sub-vertical.

**It resolves:** the sub-vertical (not the broad industry, because pressures
differ sharply inside one industry), current operating pressures, and public
peer evidence.

**What comes back** is at least two independent peer datapoints, each with a
source, a date, and a verbatim excerpt, plus what the account itself has said
publicly, plus the inference being drawn stated out loud.

**Where it stops:** if it cannot meet the peer evidence threshold, it says the
"why now" is **not yet supportable**. That is a correct and useful answer. A
stretched "why now" is the thing that gets an email deleted.

**What you check:** any vendor-published material is labelled as such. Vendor
marketing is not independent evidence.

---

## Step 4: `motion-strategist`

**You ask:** what motion fits, for the person you picked in step 2.

**It resolves:** the signal type, your `solution_catalog` from your profile, and
the **level** of the person, because the same motion framed for a VP of
Engineering and framed for a CFO are different messages.

**What comes back:** a one-sentence thesis, the outcome in the language that
level actually uses, two or three sourced proof points, the smallest first step
that is easy to say yes to, and the traps for that motion.

**Where it stops:** it refuses to recommend a motion your catalog cannot
deliver. It also switches the motion when the signal is negative. If the trigger
was a miss, a layoff, or an incident, the motion becomes efficiency, risk, or
support, and it will say so rather than helping you pitch growth into bad news.

**What you check:** does the first step actually fit the relationship you have?
An ask that is too large for a cold contact is the most common failure here.

---

## Step 5: `outreach-writer`

**You ask:** for the draft.

**It resolves:** your voice from your own sent mail via `workplace` per the
`outreach-voice` skill, falling back to the manual voice settings in your
profile and telling you which it used.

**What comes back:** one short draft under your word cap, one idea, one ask, at
most one link, subject line written last from the finished body. Beside it, not
inside it, sits the source trace: every factual claim in the draft mapped to the
citation or record it came from.

**Where it stops:** it will not draft to a contact carrying an opt-out or
suppression flag. It will not invent a mutual connection, a prior conversation,
a shared alma mater, or a customer reference. And it never sends.

**What you check:** read the source trace before the draft. If a claim has no
trace, delete the claim.

---

## Step 6: you

The chain deliberately ends with a human. The agent produced a draft in your
`output_dir`, which is gitignored. Sending is your action, in your own client,
under your own name.

Thirty seconds of verification before you send:

1. Click the two citations. Confirm the dates.
2. Read the draft as if you received it. Is the ask proportional to the
   relationship?
3. Ask whether this draft could be sent unchanged to a different account. If it
   could, it is not personalized, and the `outreach-voice` skill says to rewrite
   it.

---

## What this shows

Each agent alone is mediocre. `market-news-scout` on its own gives you a filtered
news list, which is mildly useful. `outreach-writer` on its own gives you a
well-written email about nothing.

Chained, each one narrows the next one's job, and every narrowing is grounded in
a source. That is why the shared skills matter: because all five agents classify
signals with the same vocabulary and score tone with the same rubric, step 5 can
trust what step 1 handed it.

The other thing the chain shows is how often the correct answer is to stop.
Three of the five steps have an explicit condition under which they refuse to
continue. An agent team that cannot say "there is no credible reason to reach
out here" is not a productivity tool, it is a way to send more bad email faster.

## Other chains worth running

| Chain | When |
| --- | --- |
| `pipeline-hygiene` then `deal-review` then `forecast-review` | Before a forecast call. Clean the records, inspect the deals that move the number, then make the call |
| `market-intel-sweep` then `portfolio-dashboard` | Monthly. External signal lands as a tab in the portfolio view, so whitespace carries evidence |
| `gap-analysis` then `motion-strategist` then `outreach-orchestrator` | When you are behind. Find the gap, pick the motion per account, generate the outreach |
| `account-brief` then `enablement-deck` | Before a first customer meeting. Ground the deck in what is actually true about the account |
| `renewal-expansion` then `account-intel-360` | Quarterly. Find the at-risk renewals, then find who you are missing on each |
