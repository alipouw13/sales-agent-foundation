---
name: sentiment-analysis
description: sentiment analysis, tone analysis, management tone, sentiment score, hedging language, tone shift, confidence language
---

# Sentiment Analysis

## Purpose

This skill defines a shared tone rubric for filings, earnings calls, public remarks, and news quotations.
It helps agents compare management language across periods without guessing intent.
Sentiment here means observable language about confidence, specificity, commitment, and risk.
It is sales signal detection for account planning and outreach judgment.

## Required scoring principle

Score tone relative to the same speaker's prior period whenever prior text is available.
Absolute tone varies by company culture, disclosure style, industry norms, legal review, and executive habit.
The delta is more informative than the level.
A cautious executive becoming more specific may be a positive shift.
An enthusiastic executive becoming vague may be a negative shift.
When prior-period text is unavailable, label the comparison basis as `baseline unavailable`.
Do not compare one company's tone to another company's tone unless the task is explicitly peer benchmarking.

## Dimensions scored separately

Score four dimensions independently.
Do not collapse them into one blended number unless a downstream template requires a summary.
A single blended number misleads because confident language can coexist with high risk, and specific language can describe negative conditions.

| Dimension | What it measures | Why it stands alone |
| --- | --- | --- |
| Confidence | How strongly the speaker asserts belief in the current position or plan | Confidence can rise even when risks remain high |
| Specificity | How concrete the speaker is about drivers, timing, scope, and actions | Specific detail is often more useful than positive tone |
| Forward commitment | How clearly the speaker commits to future action, investment, milestones, or operating changes | Commitment language indicates execution intent, not just explanation |
| Risk acknowledgment | How directly the speaker names constraints, uncertainty, tradeoffs, or downside | Honest risk language can be constructive rather than negative |

Each dimension gets a score from 1 to 5 and a confidence qualifier.
Each dimension requires a verbatim excerpt and location.
If evidence is insufficient for one dimension, withhold that dimension only.

## Shared 1 to 5 anchors

Use these anchors for every dimension, adapted to the dimension definition.
A score must be grounded in observable language, not vibes.

| Score | Label | Observable language pattern |
| --- | --- | --- |
| 5 | Very strong | Direct commitment verbs, specific actions, named timeframe, active voice, clear ownership, measurable operating language |
| 4 | Strong | Positive or decisive language, concrete drivers, near-term direction, mostly active voice, limited hedging |
| 3 | Balanced | Mix of positive and cautious language, some specifics, conditional execution, neutral explanation |
| 2 | Guarded | Frequent conditions, deferred timing, passive constructions, vague drivers, broad caveats, limited ownership |
| 1 | Highly guarded | Avoidance, non-answer, repeated uncertainty, no timeframe, no owner, no concrete action, heavy reliance on boilerplate |

Do not assign score 5 without a timeframe or action.
Do not assign score 4 or 5 based only on adjectives such as strong, exciting, robust, disciplined, or resilient.
Do not assign score 1 based only on the presence of a required risk factor.
Risk factor sections are inherently cautious and must be compared with prior risk language.

## Confidence dimension anchors

Score **confidence** by how directly the speaker asserts belief or certainty.

| Score | Confidence anchor |
| --- | --- |
| 5 | The speaker says the plan is working, names evidence, and commits to continued execution in a stated period |
| 4 | The speaker expresses clear belief and provides at least one concrete support point |
| 3 | The speaker gives a neutral or mixed assessment with partial support |
| 2 | The speaker uses conditions, caveats, or limited visibility around the assessment |
| 1 | The speaker avoids a clear assessment or repeatedly says visibility is limited |

Markers for high confidence include `we are seeing`, `we expect`, `we will`, `we have committed`, `on track`, and `by <date>`.
Markers for guarded confidence include `may`, `could`, `subject to`, `assuming`, `challenging`, `limited visibility`, and `too early to say`.
Quote the phrase that drives the score.

## Specificity dimension anchors

Score **specificity** by the amount of concrete detail in the language.

| Score | Specificity anchor |
| --- | --- |
| 5 | Names the driver, affected business area, action, timeframe, and success measure |
| 4 | Names the driver, action, and timeframe, but omits one major detail |
| 3 | Names the topic and at least one concrete detail, but leaves scope or timing broad |
| 2 | Uses broad categories without concrete scope, timing, or owner |
| 1 | Uses generic corporate language that could apply to any company |

Specificity is not the same as optimism.
A very specific negative disclosure can score high for specificity.
A positive but generic statement can score low for specificity.

## Forward commitment dimension anchors

Score **forward commitment** by whether the speaker makes a future action accountable.

| Score | Forward commitment anchor |
| --- | --- |
| 5 | Commits to a specific action, owner area, and timeframe using active verbs |
| 4 | Commits to a clear action with either owner area or timeframe stated |
| 3 | Describes intended direction but leaves ownership or timing open |
| 2 | Describes options, evaluation, or possibility without a firm action |
| 1 | Defers, avoids, or refuses to state next action |

High commitment verbs include `will`, `are launching`, `are expanding`, `are reducing`, `are investing`, and `have approved`.
Moderate commitment verbs include `plan`, `intend`, `expect`, and `target`.
Low commitment phrases include `evaluate`, `consider`, `explore`, `monitor`, `as appropriate`, and `over time`.
Forward commitment must be scored from source language, not from what the agent thinks management should do.

## Risk acknowledgment dimension anchors

Score **risk acknowledgment** by clarity, not negativity.
A higher score means risks are named clearly and connected to actions.
A lower score means risks are vague, minimized, or hidden behind boilerplate.

| Score | Risk acknowledgment anchor |
| --- | --- |
| 5 | Names material risks, affected areas, mitigation actions, and monitoring approach |
| 4 | Names specific risks and at least one mitigation or response |
| 3 | Names risks but gives limited mitigation detail |
| 2 | Mentions broad uncertainty without specific risk drivers |
| 1 | Uses boilerplate risk language or avoids addressing an obvious risk raised by the source context |

A high risk acknowledgment score does not mean the account is in good condition.
It means the source gives usable detail for planning.
A low risk acknowledgment score can be a signal when risks are visible elsewhere but not addressed directly.

## Hedging markers

Treat these markers as evidence only when they change the meaning of a statement.
Do not count every legal caveat as a meaningful hedge.

- `may`, `might`, `could`, `can`, when they replace action with possibility.
- `subject to`, `assuming`, `depending on`, `provided that`, and `if conditions allow`.
- `we believe`, when unsupported by evidence or action.
- `we continue to monitor`, when no decision or mitigation is stated.
- `over time`, `long term`, `eventually`, and `at the appropriate time`.
- `challenging environment`, `macro uncertainty`, and `dynamic conditions`, when not tied to specifics.
- `right-sizing`, `optimization`, and `streamlining`, when used to avoid naming operational impact.
- Passive voice such as `actions were taken` when owner, timing, or accountability is omitted.
- Excessive noun phrases such as `strategic initiatives` without actions.
- Repetition of the same broad phrase across periods with no new detail.

## Non-answer patterns

Flag a non-answer when the speaker appears to answer a question but avoids the requested information.
Do not overstate intent, just mark the pattern.

- Restates the question without adding facts.
- Answers a different question.
- Repeats prepared remarks rather than addressing the prompt.
- Uses bridge phrases such as `what I would say is` followed by unrelated content.
- Says the topic is important but gives no action, timing, or owner.
- Refers to future updates while withholding current status.
- Cites confidentiality without offering a bounded alternative.
- Gives a directional adjective with no concrete driver.
- Uses excessive aggregation that hides the affected segment.
- Repeats prior period language after conditions materially changed.

Non-answer patterns lower specificity and forward commitment.
They may also lower confidence if the avoided topic is central to the question.

## Prepared versus unscripted language

Prepared language includes filed text, scripted remarks, prepared investor slides, and planned executive statements.
Unscripted language includes Q and A responses, interviews, follow-up remarks, and clarifying answers.
Prepared language is more legally reviewed and should be scored for structure, specificity, and disclosed priorities.
Unscripted language is more useful for tone shift, hedging, and management confidence.
A score from unscripted language may carry higher diagnostic weight when it directly addresses the same topic.
A score from prepared language may carry higher citation weight when it states official commitments.
Do not mix prepared and unscripted excerpts in the same dimension score unless the output clearly labels both.
When prepared and unscripted language conflict, report the conflict rather than averaging it away.

## Minimum evidence per score

Every dimension score requires:

| Required item | Rule |
| --- | --- |
| Source type | Filing, transcript, public interview, company release, or public news quotation |
| Location | Section name, question label, paragraph label, timestamp if available, or page label if available |
| Verbatim excerpt | Exact source text that supports the score |
| Period | Filing period, call period, publication date, or event date |
| Comparison basis | Prior period excerpt, prior period unavailable, or first observed baseline |
| Score rationale | One sentence that ties the excerpt to the anchor |

If a source contains only a summary of remarks, do not score tone from it.
If the text is too short to evaluate a dimension, withhold that dimension.

## Confidence qualifiers

Use **high** when the excerpt is direct, the location is clear, and prior-period comparison is available.
Use **medium** when the excerpt is direct but prior comparison or location is limited.
Use **low** when the excerpt is usable but short, indirect, or isolated.
Withhold the score when confidence would be below low.
Confidence qualifies the score, it does not replace the score.

## When to withhold a score entirely

Withhold rather than guess when any of these conditions apply:

- Insufficient text for the dimension.
- The source is a summary rather than a transcript, filing, or direct quotation.
- The text is translated and the original language is unavailable to the agent.
- The excerpt is paraphrased by a reporter rather than quoted.
- The speaker is not management or an authorized company representative, unless the task is news tone about external perception.
- The source cannot be cited with URL, date, and location.
- The text is boilerplate copied from prior periods with no meaningful change and no specific context.
- The agent cannot separate account-specific language from industry-wide commentary.

Output `withheld` for the dimension and explain the missing evidence.
Do not fill a withheld dimension with the average of other dimensions.

## Tone shift rules

Compute tone shift separately for each dimension.
Use these labels:

| Delta | Label | Interpretation |
| --- | --- | --- |
| +2 or more | Materially more constructive | The speaker became much more concrete, committed, or clear |
| +1 | More constructive | The speaker improved in one observable way |
| 0 | Stable | No meaningful shift in observable language |
| -1 | More guarded | The speaker added hedging, reduced specificity, or deferred action |
| -2 or less | Materially more guarded | The speaker materially withdrew commitment, avoided detail, or emphasized uncertainty |

A delta requires the same topic across periods.
Do not compare risk language about one topic with confidence language about another topic.
If the topic changed, report `not comparable`.
If the speaker changed, compare with caution and lower confidence unless the company voice is consistent.

## Anti-patterns

Do not read intent into ordinary corporate boilerplate.
Do not score a summary instead of a source.
Do not treat tone as a prediction.
Do not treat confident wording as proof that budget exists.
Do not treat guarded wording as proof that a company is failing.
Do not infer emotion from punctuation, headline framing, or reporter adjectives.
Do not use one dramatic sentence to override a longer, topic-specific body of evidence.
Do not average prepared and unscripted language without showing the conflict.
Do not create outreach from tone alone.
Tone can prioritize discovery, but it cannot replace account evidence.

## Refusal and guardrails

This is sales signal detection, not investment advice, and never a basis for a trading decision.
Refuse to provide trading recommendations, investment ratings, price targets, or buy or sell conclusions.
Refuse to score tone without a verbatim excerpt, source date, and location.
Refuse to invent prior-period comparisons.
Refuse to infer private intent, budget, quota, revenue, or decision authority from tone.
Refuse to name people, contact details, or private records unless supplied by an authorized internal source and required for the task.
Use placeholders such as `<company>` in examples.
Keep public tone analysis separate from CRM facts.
When evidence is thin, say `withheld` or `low confidence`, not a stronger claim.
