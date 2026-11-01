---
title: "The Oracle Problem"
date: 2026-11-01
excerpt: "$237 million was riding on whether Zelensky wore a suit. The code worked perfectly. The question was wrong. Here's what that says about every tokenized asset that depends on the real world."
tags: ["RWA", "oracles", "DeFi", "tokenization"]
cover: "/images/zelesnky.jpg"
slug: "the-oracle-problem"
---

On 24 June 2025, Volodymyr Zelensky arrived at the NATO summit in The
Hague wearing a dark jacket and matching trousers. For years he had
appeared almost exclusively in military-style clothing, so the change
made headlines. The BBC described it as a suit.

For most people, this was a curiosity. For a group of bettors on
Polymarket, a prediction market built on a blockchain, it was a question
worth more than $237 million. For months, they had been betting on one
thing: would Zelensky be photographed in a suit before July?

<figure style="margin:2em 0;">
<img src="/images/polymarket.png" alt="Polymarket's 'Zelensky wears a suit' market, showing over $237 million in volume" style="width:100%;border-radius:12px;" />
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">$237 million riding on a jacket.</figcaption>
</figure>

The answer seemed easy. It wasn't. The market was settled by a
decentralized oracle — a system where token holders vote on what
happened in the real world. After days of disputes and accusations of
manipulation, the vote came back: no, it wasn't a suit.

So nothing broke. The smart contracts did exactly what they were
supposed to do, and every payout executed perfectly. The problem was the
question. A blockchain has no eyes. It cannot look at a photo and decide
what counts as a suit. Someone has to tell it.

That someone is called an oracle. How much we can trust it is one of the
most important, and least understood, problems in crypto.

## Why a Blockchain Can't See

To understand why Zelensky's suit caused so much trouble, you need to
know one strange fact about blockchains: they are completely blind to
the outside world.

This is not a bug, it's by design. A blockchain works because thousands
of computers process the same transactions and must reach exactly the
same result. If a smart contract could simply check a website for the
price of gold, two computers might ask a second apart, get different
answers, and disagree about what happened. The whole system would fall
apart. So blockchains only work with information that is already inside
them.

That creates a problem. Almost everything interesting happens outside.
Prices, interest rates, election results, whether a vault still holds
the gold it claims to hold. For a blockchain to know any of it, someone
has to bring the information in. That someone is called an oracle.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 460" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The coat, off-chain, goes to a messenger, who reports to the receipt, on-chain">
<g font-family="Inter, sans-serif">
<rect x="80" y="40" width="300" height="160" rx="16" fill="#EEF2FC"/>
<circle cx="230" cy="105" r="26" fill="#1E3A8A"/>
<text x="230" y="113" text-anchor="middle" font-size="22" font-weight="700" fill="#FFFFFF">1</text>
<text x="230" y="155" text-anchor="middle" font-size="22" font-weight="600" fill="#111318">The coat</text>
<text x="230" y="179" text-anchor="middle" font-size="13" fill="#5B5F6B">Real asset, off-chain</text>

<path d="M395 120 H470" stroke="#1E3A8A" stroke-width="3"/>
<path d="M470 120 L452 109 M470 120 L452 131" stroke="#1E3A8A" stroke-width="3" fill="none"/>

<line x1="500" y1="10" x2="500" y2="230" stroke="#D4D6DC" stroke-width="2" stroke-dasharray="6 6"/>
<text x="500" y="255" text-anchor="middle" font-size="12" letter-spacing="1" fill="#9094A0">OFF-CHAIN &#160;&#160;|&#160;&#160; ON-CHAIN</text>

<path d="M530 120 H605" stroke="#1E3A8A" stroke-width="3"/>
<path d="M605 120 L587 109 M605 120 L587 131" stroke="#1E3A8A" stroke-width="3" fill="none"/>

<rect x="450" y="40" width="300" height="160" rx="16" fill="#1E3A8A"/>
<circle cx="600" cy="105" r="26" fill="#FFFFFF"/>
<text x="600" y="113" text-anchor="middle" font-size="22" font-weight="700" fill="#1E3A8A">2</text>
<text x="600" y="155" text-anchor="middle" font-size="22" font-weight="600" fill="#FFFFFF">The messenger</text>
<text x="600" y="179" text-anchor="middle" font-size="13" fill="#DCE4F7">The oracle</text>

<rect x="820" y="40" width="300" height="160" rx="16" fill="#EEF2FC"/>
<circle cx="970" cy="105" r="26" fill="#1E3A8A"/>
<text x="970" y="113" text-anchor="middle" font-size="22" font-weight="700" fill="#FFFFFF">3</text>
<text x="970" y="155" text-anchor="middle" font-size="22" font-weight="600" fill="#111318">The receipt</text>
<text x="970" y="179" text-anchor="middle" font-size="13" fill="#5B5F6B">The token, on-chain</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">The coat stays off-chain. The messenger is the only thing standing between it and the token you hold.</figcaption>
</figure>

The simplest way I've found to capture it is a coat check. You hand over
your coat and get a ticket. The coat is the real asset, kept somewhere
off-chain: dollars in a bank, treasuries at a custodian, gold in a vault.
The ticket is the token you hold in your wallet. Between the two sits a
messenger who tells the blockchain what's really in the back room. That
messenger is the oracle.

> Blockchains were built so that nobody would have to trust anybody. But
> the moment a token depends on the real world, everything depends on
> the messenger.

In the Zelensky case, the messenger was a group of token holders voting
on what counted as a suit. Elsewhere, it might be a price feed, an
auditor, or the token's own issuer.

So the real question is never just "what does the blockchain say?" It's:
is the messenger telling the truth, and would anyone notice if it
weren't?

## Not All Truths Are Equal

Some questions are much harder to bring on-chain than others. I find it
useful to think of three levels.

<div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1.1rem 1.25rem;margin:1.5em 0;">
<strong style="color:#1E3A8A;">Level 1 — Objective and frequent.</strong>
<span style="color:#5B5F6B;"> What is the price of gold right now? How
many dollars is one euro worth? There's a clear answer, it changes
constantly, and dozens of independent sources report it. An oracle can
collect prices from many of them, combine them, and update the
blockchain every few minutes. If one source lies, the others outvote
it. This is the problem oracles solve best.</span>
</div>

<div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1.1rem 1.25rem;margin:1.5em 0;">
<strong style="color:#1E3A8A;">Level 2 — Objective but rare.</strong>
<span style="color:#5B5F6B;"> Does the vault really hold the gold
behind every token? Does the fund really own the Treasuries it claims?
There's a true answer here too, but nobody can watch it in real time.
It usually comes from an auditor's report, published once a month or
once a quarter, often from a single firm. So you end up with a mismatch:
a token that can be traded every few seconds, backed by a truth that's
checked a few times a year.</span>
</div>

<div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1.1rem 1.25rem;margin:1.5em 0;">
<strong style="color:#1E3A8A;">Level 3 — Subjective.</strong>
<span style="color:#5B5F6B;"> Was that a suit? Is a borrower really in
default? What is an illiquid loan actually worth? Here, even humans
disagree. There's no feed to read, only judgement — and whoever makes
that judgement holds real power over the outcome.</span>
</div>

The further down the list you go, the harder it gets to trust the
messenger. And here's the uncomfortable part: almost everything that
matters for Real World Assets lives in levels 2 and 3. Prices are the
easy bit. The hard questions are whether the asset exists, what it's
really worth, and who gets to decide.

## How Oracles Fail

If the messenger is the weak point, attackers will go after the
messenger. In practice, oracles fail in three main ways.

**1. Poison the source.** In October 2022, a trader named Avraham
Eisenberg targeted Mango Markets, a crypto lending platform. Mango's
oracle read the price of its own token, MNGO, from a handful of
exchanges. MNGO was thinly traded, so Eisenberg pushed its price up by
more than 1,000% in about twenty minutes. The oracle faithfully reported
the new price. Mango's smart contracts then treated his inflated tokens
as valuable collateral and let him borrow and withdraw around $110
million. The code worked perfectly. It was simply fed a lie.

> The code worked perfectly. It was simply fed a lie.

The story has a twist. Eisenberg was convicted of fraud in 2024, but in
2025 a judge overturned the convictions, partly because Mango's own
rules didn't forbid what he did.

> A system can be drained without anyone technically breaking its rules.

**2. Capture the messenger.** Some oracles don't read a price, they
vote. That's how the Zelensky suit was decided — holders of the UMA
token vote on what happened in the real world. The weakness is economic.
At the time, all the UMA tokens in existence were worth less than the
money riding on that single bet. When it's cheaper to buy the vote than
the amount you can win, someone will eventually try.

**3. Trust a single or conflicted messenger.** The quietest failure is
also the most common. If one source feeds the oracle, one mistake or one
bad actor is enough. And sometimes the messenger isn't neutral at all —
it's the same company that issued the token, reporting on its own
reserves. That's like asking the coat-check attendant to audit himself.

The common thread is simple. An oracle is only as secure as the cost of
corrupting it. If lying is cheap and the reward is large, the truth is
in danger, however elegant the code around it.

## Four Questions, Seven Tokens

Explaining the oracle problem is one thing. I wanted to see what it
looks like in real tokens. So over the past few weeks I built a small
project, the [RWA Oracle Scorecard](/projects/rwa-scorecard), which
looks at seven tokenized assets on Ethereum — dollar stablecoins,
tokenized gold, a Treasury fund, and a private credit token — and asks
each one the same four questions, going back to the coat check:

<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">1. Is the data fresh?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">When did the messenger last report, compared with how often it's supposed to?</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">2. Do tickets match coats?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Are there as many tokens in circulation as there are reserves backing them, and how old is the proof?</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">3. Does the market believe it?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Does the token trade at the value it claims?</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">4. Who could change the rules?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">How many independent keys would it take to mint new tokens, upgrade the contract, or replace the oracle?</div>
  </div>
</div>

The answers were more interesting than I expected.

**"101% backed. $78,900 in cash."** One stablecoin, TUSD, has an
attestation confirming its reserves cover 101.5% of the tokens in
circulation. On paper, perfect. But reading the report, almost all of
those reserves (99.98%) sit in a single illiquid fund that's caught up
in a legal dispute and is valued at cost. The part held in actual cash:
about $78,900. The messenger wasn't lying; the number was true. It just
didn't tell you what you needed to know. That's the oracle problem at
its most subtle: a true statement that still misleads.

**The messenger owns the coat.** Another stablecoin, USD1, publishes a
"proof of reserve" feed on-chain through Chainlink, which sounds
reassuring. But the data in that feed is supplied by BitGo, the company
behind the token itself. "On-chain" doesn't mean "independent." It's the
coat-check attendant auditing himself.

**One key is enough.** For four of the seven tokens, I found at least
one path — whether minting, upgrading, or changing the oracle —
controlled by a single key. Whoever holds it could, in principle, change
the rules on their own. The best result was USDT, where any such change
requires three signatures out of six.

**When it matches to the cent.** Not everything was a warning. For
USTB, a tokenized Treasury fund, the number of tokens on the blockchain
(41,063,563.57) matched the issuer's own register exactly, to the last
decimal. That's what good looks like: two independent records, telling
the same story.

See the full ranking, and every token's breakdown, on the
[scorecard](/projects/rwa-scorecard) itself.

## What the Scorecard Can't Tell You

Before anyone takes these results too far, it's worth being clear about
what the scorecard doesn't measure. Ironically, a project about trusting
the messenger should be honest about its own limits.

**It measures transparency, not safety.** A high score means a token's
data is easy to verify. It doesn't mean the token is safe, solvent, or a
good investment. A token can be very transparent about a very bad
situation.

**It counts quantity, not quality.** The question "do tickets match
coats?" checks that reserves cover the tokens in circulation. It doesn't
yet judge what those reserves are made of. That's exactly what the TUSD
case shows: 101% coverage can hide a very different reality.

**It only sees what's on-chain.** When I say a single key controls part
of a contract, that's what the blockchain shows. Behind that key, there
may be internal approvals, hardware security, or multiple people that
simply aren't visible from the outside. And the question on control only
counts keys for now — safeguards like time delays and minting limits
will come in the next version.

**Some data is collected by hand.** Reserve attestations are published
as reports, not on-chain feeds, so I read them manually. If nobody
updates them, they go stale. Which is, in a way, the oracle problem
showing up in my own project.

**It's small.** Seven tokens, one blockchain, and a methodology that's
still a first draft (v0.1).

## Back to the Suit

In the end, the Zelensky bet was never really about fashion. It was
about a question every blockchain eventually has to answer: who gets to
tell it what's true?

Smart contracts can be perfect, transparent, and unstoppable, and still
pay out on a lie. Blockchains didn't remove the need for trust; they
moved it. It now sits with the messenger: the price feed, the auditor,
the voters, the company reporting on its own reserves. And for Real
World Assets, where the coat always lives off-chain, that messenger
matters more than anything else.

So next time you see a token that claims to represent something real,
don't just ask what it's worth. Ask the four questions. Is the data
fresh? Do the tickets match the coats? Does the market believe it? And
who could change the rules?

This project also changed how I think about my own work. I'm now using
what I learned here to design the oracle for OliToken, my own
tokenization project, and the first rule I've set myself is simple:

> The messenger should never be the one who owns the coat.
