---
name: outreach-voice
description: voice profile, writing style, tone matching, sounds like me, anti-template, email voice, style derivation
---

# Outreach Voice Contract

## Purpose
This skill defines how outreach agents derive and apply the runner's writing
style without copying private content.
Use it for first-touch notes, re-engagement, event follow-up, prospecting
sequences, and reviewed drafts that should sound like the runner.
The goal is recognizable human style, not imitation of confidential substance.

## Required inputs
| Input | Required | Source | Use |
|---|---|---|---|
| Runner profile | yes | profile | Provides voice settings, word cap, and banned phrases. |
| Sent-mail sample access | optional | workplace | Used only when `voice.derive_from` is `workplace`. |
| Draft context | yes | crm, workplace, notes, web | Provides account, recipient role, signal, and ask. |
| Relationship context | conditional | crm, notes, workplace | Sets familiarity and ask size. |
| Source citations | conditional | crm, notes, web, decks | Supports factual claims in the draft. |
If profile voice settings are missing, use a plain professional fallback and say
which settings could not be read.

## Derivation method
Derive voice only from the runner's own sent messages.
Never derive voice from inbox messages, forwarded content, meeting transcripts,
chat messages from other people, or third-party documents.
Use a recency window of the last ninety days.
Filter to comparable context: external recipients, short-form business messages,
non-sensitive topics, and human-authored messages.
Exclude internal-only discussions, legal matters, personnel topics, customer
incidents, negotiations, pricing, confidential strategy, and any message that
contains restricted or personal information.
A reliable profile requires at least twelve usable sent messages after filtering.
A strong profile requires at least twenty usable sent messages after filtering.
If fewer than twelve usable messages remain, do not infer a style profile.
Fallback rule: use the manual `voice` settings from the profile and state,
"Voice source used: manual profile fallback."
When derivation succeeds, state, "Voice source used: derived from runner sent
messages."
Do not expose the sampled messages, their subjects, their recipients, or their
content.

## Sampling boundaries
The sample is read only to count and classify style signals.
The agent may count sentence length, greeting pattern, paragraph shape, register,
contraction use, hedging, questions, list use, and punctuation tendencies.
The agent may not quote phrases longer than three words from a sampled message.
The agent may not preserve account-specific wording from the sample.
The agent may not use any sampled fact as evidence for the new draft.
The agent may not store the sample or a derived profile in a committed file.

## Voice profile shape
Return or apply the following profile fields.
| Field | Definition | Allowed values or measurement |
|---|---|---|
| Greeting form | How the runner opens a message | Exact placeholder pattern, such as `Hi <first name>,`. |
| Sign-off form | How the runner closes | Exact placeholder pattern from the profile or derived style. |
| Average sentence length | Mean words per sentence | Short, medium, or long, with observed range. |
| Maximum sentence length | Hard ceiling for draft sentences | Word count ceiling. |
| Paragraph length | Typical number of sentences per paragraph | One, two, or three. |
| Formality register | How polished or direct the language is | Casual professional, neutral professional, or formal. |
| Contraction use | Whether contractions are natural for the runner | Frequent, occasional, rare, or never. |
| Hedging frequency | Use of softeners such as may, might, likely | Low, medium, or high. |
| Question use | Whether the runner asks direct questions | None, one closing question, or multiple questions. |
| Technical density | Amount of technical language | Low, medium, or high, always audience matched. |
| List use | Whether bullets are natural | Avoid, short bullets, or structured bullets. |
| Emoji policy | Whether emoji appear in external business mail | Never, rare, or allowed when relationship supports it. |
| Exclamation policy | Whether exclamation marks are allowed | Never, rare, or one maximum. |
| Characteristic phrasings | Short reusable style markers | Only generic phrasing under three words. |
If a field cannot be derived, use the profile value if present.
If neither derived nor profile value exists, choose the most restrained option.

## What must not be copied
Do not copy confidential language from sampled messages.
Do not copy customer specifics from sampled messages.
Do not copy third-party words, even if they appear in a sent message.
Do not copy personal details about the runner, a recipient, or any other person.
Do not copy pricing, negotiation language, legal terms, escalation history, or
relationship commentary.
Do not copy a sentence structure so distinctive that it identifies a prior
message.
Style can be reused. Substance cannot.

## Anti-template rules
The following phrases are banned in outreach drafts.
| Banned phrase | Reason |
|---|---|
| I hope this email finds you well | Template opening. |
| circling back | Low-information follow-up. |
| just following up | Apologetic and generic. |
| touch base | Vague ask. |
| synergies | Inflated language. |
| leverage, when used as a verb | Jargon substitute for use. |
| reach out, when used as a noun phrase | Corporate filler. |
| wanted to connect | No clear reason. |
| checking in | No clear value. |
| thought leadership | Self-focused. |
| game changer | Unsourced exaggeration. |
| unlock value | Vague outcome. |
| exciting opportunity | Sender-centric. |
| innovative solution | Product-first and generic. |
| any generic flattery about the recipient's company | Not personalization. |
Do not use em dashes or en dashes.
The em dash is the loudest tell that text was machine written.
Use a comma, colon, parentheses, or a second sentence instead.
Do not use three-part rhetorical lists such as "faster, smarter, and safer".
Do not write a subject line that overpromises relative to the body.
Do not open with generic praise for the recipient's company.
Do not claim familiarity with priorities unless a source supports it.
A draft that could be sent unchanged to a different account is not personalized
and must be rewritten.

## Length and structure contract for a first touch
Use one idea.
Use one ask.
Use the first-touch word cap from the profile field
`voice.max_words_first_touch`.
If that field is missing, use a cap of one hundred twenty words.
At most one link is allowed.
No attachment is allowed unless the user explicitly asks for one.
Subject is written last, after the body is finished.
The subject must be specific, modest, and aligned to the body.
The body must fit this shape.
| Part | Sentence count | Job |
|---|---|---|
| Opening | one | Name the relevant signal or context. |
| Relevance | one or two | Connect the signal to the recipient's likely business problem. |
| Credible idea | one or two | State the motion or useful point in plain language. |
| Ask | one | Request a proportional next step. |
| Close | optional | Use the runner's normal sign-off. |
Do not add a second idea because the draft feels short.
Short is acceptable when the signal, relevance, and ask are clear.

## Relationship calibration
For a cold recipient, ask for confirmation, a referral, or a short diagnostic.
For a warm recipient, reference only sourced shared context and ask for a narrow
working session.
For an active opportunity, connect to the agreed business problem and ask for the
next named step.
For an executive, keep the ask smaller than the status gap unless the runner
already has an executive relationship.
Never use first-name warmth to imply relationship depth.

## Tone rules
Prefer plain verbs over abstract nouns.
Prefer customer language over seller language.
Prefer observed facts over adjectives.
Prefer a specific business problem over a broad value claim.
Use contractions only if the profile allows them.
Use technical terms only when the recipient level and context support them.
Hedging is allowed when the signal is uncertain.
Overconfidence is not allowed when the source is weak.

## Personalization standard
A personalized draft must include at least one sourced account-specific fact,
signal, or relationship context.
The fact must come from crm, workplace, notes, web, or decks.
The draft must explain why that fact matters to this recipient's role.
The draft must use a first step that follows from the fact.
The draft must still avoid confidential or sensitive detail.
If the only available personalization is the account name, label the draft as low
personalization and ask for more context in the output note.

## Privacy boundary
Sent-mail sampling is for style extraction only.
The agent never quotes sampled messages.
The agent never stores sampled messages.
The agent never summarizes sampled messages.
The agent never surfaces sampled message content to the user.
The agent never derives a profile from anyone else's mail.
The agent never writes a derived profile into a committed file.
The agent never uses sampled message content as a source for account claims.
The agent may write a temporary in-memory style profile for the current drafting
turn only.
If a workflow requires persistent preferences, use only the manual `voice`
settings in the profile.

## Self-check before returning a draft
Run this checklist before returning any outreach draft.
1. The draft uses one idea and one ask.
2. The body is within the profile word cap.
3. The subject was written after the body and does not overpromise.
4. The greeting and sign-off match the selected voice source.
5. No banned phrase appears.
6. No em dash or en dash appears.
7. No three-part rhetorical list appears.
8. No confidential, personal, or third-party wording was copied.
9. At least one sourced account-specific signal is present, or low personalization is disclosed.
10. Every factual claim can be traced to crm, workplace, notes, web, or decks.
11. The ask is proportional to the relationship and audience level.
12. The draft could not be sent unchanged to another account.
13. Any link is necessary, singular, and directly relevant.
14. The message leads with the customer's problem, not a product.
15. The final text sounds human when read aloud.
If any check fails, rewrite before returning the draft.

## Output note
Return the draft plus a brief note with voice source used, word count,
personalization source type, and any confidence limits.
Do not include sampled-message details in the note.
