---
title: "Canton vs. Ethereum: Here We Go?"
date: 2026-11-08
excerpt: "Transfer deals leak for weeks before the 'Here we go!' — and the moment they close, they become public record. That exact balance is what Wall Street wants from a blockchain. Here's why Ethereum's transparency scares banks, how Canton hides the negotiation while still proving the result, and why the real question was never which one wins."
tags: ["blockchain", "ethereum", "institutional finance", "crypto"]
cover: "/images/gyokeres.jpg"
slug: "canton-vs-ethereum-here-we-go"
---

Every summer, millions of football fans refresh the same account on
their phones, waiting for the "Here we go!" from Fabrizio Romano. Last
summer, when Sporting sold Viktor Gyokeres to Arsenal, that moment felt
instant.

But before the "Here we go", there were weeks of negotiation that
nobody saw in full. Even Fabrizio only reports what leaks.

Now imagine every one of those offers was published live, the second it
was made. Arsenal bids, and within a minute every rival club in Europe
knows the exact number and can top it. Sporting's asking price is
visible to every buyer. The player's agent sees what each club is
willing to pay. The market simply wouldn't work.

Once the deal is done, though, privacy is the last thing anyone wants.
The transfer is announced, the contract is registered, and because
Sporting SAD is listed on the stock exchange, it has to disclose the
deal to the market regulator. Private negotiation, public result.

That balance is exactly what the financial world is looking for on
blockchains. Ethereum is built on transparency: every transaction
visible to everyone, from the start. That's what makes it trustworthy —
and also what makes banks nervous. Canton was built on the opposite
idea: keep the negotiation private, but make the result verifiable. In
this post, I'll look at both philosophies, who's building on each, and
why the real question isn't which one wins.

## Why Transparency Scares Banks

On Ethereum, every transaction is public. Anyone can open a block
explorer and see which address sent what, to whom, when, and for how
much. Addresses don't show names, but that protection is thinner than
it looks. Analytics firms spend their days labelling wallets, and once
an address is linked to a fund or a bank, its entire history is
visible — every position, every counterparty, every move.

For individuals, that's mildly uncomfortable. For a financial
institution, it's a dealbreaker, for three reasons:

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It reveals the strategy</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">This is the transfer-window problem. A fund slowly building a large position doesn't want the market to see it coming. A bank doesn't want competitors to know who its clients are, or how much it's lending to whom.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It invites front-running</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Imagine shouting at a market stall that you'll buy all the tomatoes, whatever the price. The man next to you buys them first and sells them back to you at a markup. On Ethereum, this happens for real — pending transactions are visible before they're confirmed, and bots jump in front of them.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It clashes with the law</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Banks have a legal duty to protect their clients' data. Publishing client transactions on a public ledger, even under pseudonyms, sits very badly with bank secrecy and data-protection rules.</div>
  </div>
</div>

The second point is already visible in the numbers. One of the most
common versions of front-running, the "sandwich attack", drained nearly
$40 million from Ethereum users in 2025 — though the good news is that
it's falling fast, as more traders route their transactions through
private channels.

Traditional finance has been dealing with the same problem for decades,
and there's a name for the solution: **dark pools**, trading venues
where large orders aren't displayed to the public before they're
executed, so big investors can buy or sell without moving the market
against themselves.

<div style="background:#1E3A8A;border-radius:12px;padding:1.25rem 1.5rem;margin:1.75em 0;display:flex;align-items:center;gap:1.25rem;">
  <div style="font-size:2.2rem;font-weight:700;color:#FFFFFF;white-space:nowrap;">&gt;50%</div>
  <div style="font-size:0.92rem;color:#DCE4F7;">of all US stock trading in 2025 happened away from public exchanges — the first time dark pools and private venues passed half the market. Wall Street already pays for privacy every single day.</div>
</div>

So the question was never whether institutions want privacy on a
blockchain. It's how to give it to them without losing what blockchain
does well: a shared record that everyone trusts. That's the problem
Canton was built to solve.

## How Canton Keeps the Cards Face Down

Canton was created by Digital Asset, a company founded in New York in
2014, and its main network went live in 2024. It describes itself as a
public blockchain for regulated finance. Here's how it actually works.

**Each party sees only its own part of the deal.** On Ethereum, every
computer on the network processes and stores every transaction. Canton
turns that around: a transaction is split into pieces, and each
participant only receives the pieces that concern it — what the
industry calls **sub-transaction privacy**.

Back to football. When Sporting sells a striker to Arsenal, the deal
has several parts. On Canton, Sporting would see the fee, but not the
player's salary. The agent would see their commission, but not the
rest. No other club in Europe would see anything at all. Each party can
still check, cryptographically, that the slice it sees is valid and
consistent with the whole.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="One encrypted transfer deal splits into pieces: Sporting sees the fee only, the agent sees the commission only, rival clubs see nothing, and the Global Synchronizer orders everything without reading any of it">
<g font-family="Inter, sans-serif">
<rect x="40" y="70" width="280" height="160" rx="16" fill="#1E3A8A"/>
<text x="180" y="140" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">One transfer deal</text>
<text x="180" y="162" text-anchor="middle" font-size="13" fill="#DCE4F7">encrypted on Canton</text>
<path d="M320 100 L470 50" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<path d="M320 150 L470 150" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<path d="M320 200 L470 250" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="480" y="10" width="300" height="80" rx="12" fill="#EEF2FC"/>
<text x="630" y="42" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Sporting</text>
<text x="630" y="64" text-anchor="middle" font-size="12.5" fill="#5B5F6B">sees: the fee only</text>
<rect x="480" y="110" width="300" height="80" rx="12" fill="#EEF2FC"/>
<text x="630" y="142" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">The agent</text>
<text x="630" y="164" text-anchor="middle" font-size="12.5" fill="#5B5F6B">sees: the commission only</text>
<rect x="480" y="210" width="300" height="80" rx="12" fill="#EEF2FC"/>
<text x="630" y="242" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Rival clubs</text>
<text x="630" y="264" text-anchor="middle" font-size="12.5" fill="#5B5F6B">see: nothing at all</text>
<path d="M800 50 H900" stroke="#9094A0" stroke-width="2" stroke-dasharray="4 4" fill="none"/>
<path d="M800 150 H900" stroke="#9094A0" stroke-width="2" stroke-dasharray="4 4" fill="none"/>
<path d="M800 250 H900" stroke="#9094A0" stroke-width="2" stroke-dasharray="4 4" fill="none"/>
<rect x="910" y="90" width="260" height="120" rx="16" fill="#FFFFFF" stroke="#1E3A8A" stroke-width="2.5"/>
<text x="1040" y="140" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Global Synchronizer</text>
<text x="1040" y="162" text-anchor="middle" font-size="12.5" fill="#5B5F6B">orders every piece,</text>
<text x="1040" y="180" text-anchor="middle" font-size="12.5" fill="#5B5F6B">reads none of them</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Sub-transaction privacy: everyone can verify their own slice is valid, but only their slice.</figcaption>
</figure>

**Each institution runs its own node.** Banks and other participants
run their own servers, called validators, which hold their own data and
their clients' contracts. In effect, Canton is a network of separate
ledgers that can talk to each other.

Separate ledgers, though, still need someone to keep order — otherwise
two banks could disagree about what happened first. That's the job of
the **Global Synchronizer**. It puts transactions in order and confirms
that everyone involved has approved them, but it only ever sees
encrypted data.

This also makes something very useful possible: **atomic settlement**.
Either every part of a transaction happens, or none of it does. A
football club cannot receive the player without the money leaving its
account, and the money cannot leave without the player arriving. In
finance, that removes one of the oldest risks there is — paying for
something you never receive.

<div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.25rem;margin:1.75em 0;">
<strong style="color:#111318;">Who runs the Global Synchronizer:</strong>
<span style="color:#5B5F6B;">a group of organisations called Super Validators, among them Visa, Nasdaq, Circle and the London Stock Exchange Group. Changes to the network's rules need a two-thirds majority. They're paid in Canton Coin, the network's own token — users burn Canton Coin to pay their fees, and new coins are minted to reward the infrastructure operators and the applications that generate activity.</span>
</div>

Put simply, Canton offers institutions something Ethereum, by design,
doesn't: a shared network where they can transact with each other
without showing their hand.

## Who's Playing Where

Institutions are using each network for a different kind of job.

**Ethereum: where assets live.** When the goal is to issue an asset and
distribute it to many holders, Ethereum is still the default. It holds
around 60% of the value of all tokenized real-world assets, and
tokenized US Treasuries on Ethereum hit a record of around $8 billion
in May 2026. BlackRock's BUIDL lives there. So does MONY, the tokenized
money-market fund JPMorgan launched in December 2025. These products
need what Ethereum does best: easy access for investors, wallets
everyone already uses, and the chance to plug into the rest of the
crypto economy as collateral.

**Canton: where institutions deal with each other.** Canton's activity
looks completely different. It isn't mainly about assets sitting in
wallets, but about flows between institutions: repo, collateral,
securities lending, settlement. Broadridge runs its repo platform on
it. EquiLend runs its securities-lending platform on it. HSBC completed
a tokenized deposit pilot on it in April 2026. And at the end of
October, the most important name of all went live: DTCC, the company
that settles most of the US stock market, launched its tokenization
service with Canton as one of its first two networks.

**Both: the ones hedging their bets.** The most telling cases are the
institutions using both. JPMorgan's deposit token, JPM Coin, went live
on Base, a network built on Ethereum, and is now coming to Canton too.
Circle issues USDC mainly on public chains like Ethereum, and is also a
Super Validator on Canton. And DTCC's second network, its own private
chain, runs on Besu — which is Ethereum software. Even the biggest
Canton launch of the year has Ethereum technology sitting right next to
it.

<div style="overflow-x:auto;margin:1.75em 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.92rem;">
<thead>
<tr>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:10px 0 0 0;">&#160;</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;">Ethereum</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:0 10px 0 0;">Canton</th>
</tr>
</thead>
<tbody>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Main use</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Issuing and distributing assets</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Transactions between institutions</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Typical activity</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Tokenized funds, stablecoins, DeFi</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Repo, collateral, securities lending, settlement</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Examples</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">BlackRock BUIDL, JPMorgan MONY</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">DTCC, Broadridge, EquiLend, HSBC pilot</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;border-radius:0 0 0 10px;">On both</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">JPM Coin, Circle</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;border-radius:0 0 10px 0;">JPM Coin, Circle</td>
</tr>
</tbody>
</table>
</div>

Canton's big numbers are mostly flows — short-term repo loans that move
across the network every day. Ethereum's are mostly assets held over
time. Comparing them is like comparing the number of cars that cross
the Hong Kong–Macau bridge every day with the number of cars parked in
Macau. Both matter, but they don't tell you which is bigger.

One measure is a bit more comparable: fees.

<div style="background:#1E3A8A;border-radius:12px;padding:1.25rem 1.5rem;margin:1.75em 0;display:flex;align-items:center;gap:1.25rem;">
  <div style="font-size:2.2rem;font-weight:700;color:#FFFFFF;white-space:nowrap;">~42%</div>
  <div style="font-size:0.92rem;color:#DCE4F7;">of all fees across the blockchains tracked by Messari in Q1 2026 were generated on Canton — more than any other network. Whatever you think of Canton, institutions are paying to use it.</div>
</div>

## Ethereum's Response: Privacy, Proven in Public

Ethereum's community didn't ignore the problem. Over the past year,
privacy has become one of its top priorities.

The Ethereum Foundation set up a dedicated **Privacy Cluster** — a team
of 47 engineers, researchers and cryptographers — alongside an
Institutional Privacy Task Force focused on what banks and regulators
actually need. Its flagship project, **Kohaku**, is a toolkit that lets
wallets hide balances and transactions by default, though it's still
early.

The more immediate answer for institutions comes from Layer 2 networks,
and the clearest example is ZKsync's **Prividium**. The idea: let a
bank run its own private chain, where only authorized parties can see
the transactions, while regularly sending proof to Ethereum that
everything on that chain is valid.

The trick behind it is a **zero-knowledge proof** — a way of proving
something is true without revealing the information behind it. Ethereum
confirms the rules were followed, without ever seeing the details, just
mathematically.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A bank's private Prividium chain keeps its transactions hidden, sends a zero-knowledge proof to Ethereum, and Ethereum confirms the rules were followed without ever seeing the details">
<g font-family="Inter, sans-serif">
<rect x="40" y="70" width="280" height="160" rx="16" fill="#1E3A8A"/>
<text x="180" y="138" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">Bank's private chain</text>
<text x="180" y="160" text-anchor="middle" font-size="13" fill="#DCE4F7">e.g. Deutsche Bank, UBS</text>
<text x="180" y="182" text-anchor="middle" font-size="12.5" fill="#DCE4F7">transactions stay hidden</text>
<path d="M320 150 L470 150" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<path d="M470 150 L456 143 M470 150 L456 157" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<circle cx="600" cy="150" r="80" fill="#EEF2FC" stroke="#1E3A8A" stroke-width="2.5"/>
<text x="600" y="145" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">ZK proof</text>
<text x="600" y="166" text-anchor="middle" font-size="11.5" fill="#5B5F6B">"the rules were followed"</text>
<path d="M730 150 L880 150" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<path d="M880 150 L866 143 M880 150 L866 157" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="900" y="70" width="260" height="160" rx="16" fill="#FFFFFF" stroke="#1E3A8A" stroke-width="2.5"/>
<text x="1030" y="138" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">Ethereum</text>
<text x="1030" y="160" text-anchor="middle" font-size="12.5" fill="#5B5F6B">confirms the rules,</text>
<text x="1030" y="180" text-anchor="middle" font-size="12.5" fill="#5B5F6B">sees none of the details</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Prividium: the bank's chain stays private, but Ethereum still mathematically confirms it played by the rules.</figcaption>
</figure>

This isn't just theory. Deutsche Bank already runs a live institutional
chain built on Prividium, which settles to Ethereum using these proofs.
UBS has tested the same technology to let clients buy fractions of gold
on a permissioned blockchain.

Here's the twist: look closely at Ethereum's answer, and it starts to
resemble Canton. A Prividium chain is permissioned — you can't use
Deutsche Bank's network unless Deutsche Bank has checked who you are.
Both networks now offer private execution with some form of shared
verification. The real difference is who you trust to keep everyone
honest:

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">On Canton</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">A group of known institutions, the Super Validators, voting by a two-thirds majority.</div>
  </div>
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">On Ethereum</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Mathematics, and the public Ethereum network — which anyone can join and check.</div>
  </div>
</div>

Each side thinks the other got it wrong. Canton's people argue that
zero-knowledge technology is still too complex and opaque for regulated
finance. ZKsync's founder, Alex Gluchowski, replies that Canton depends
too much on a small set of operators, which creates centralization
risk. Digital Asset's CEO, Yuval Rooz, fires back that plenty of
Ethereum Layer 2s are run by a single company anyway.

Both have a point, and that's what the next section is about.

## What Each Side Gets Wrong

Canton and Ethereum simply chose to pay different prices.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin:1.75em 0;">
<div>
<div style="font-weight:700;color:#1E3A8A;margin-bottom:0.6rem;">Canton's weak spots</div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">"Public", with an asterisk.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Canton calls itself a public network, but the group that runs it is not open to everyone — becoming a Super Validator is by invitation, approved by the Canton Foundation and a supermajority of existing ones. That's a very different promise from Ethereum's, where anyone can run a node.</span></div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Hard to check from the outside.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Because transactions are hidden by design, outsiders can't independently verify how much activity really happens, or where it comes from. Critic Austin Campbell has bluntly asked whether the repo market would even notice if Canton vanished tomorrow.</span></div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;"><strong style="color:#111318;">A token still finding its balance.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Early on, around 80% of new Canton Coin went to a small group of Super Validators. That's shifted a lot since, but the network still mints more than it burns — a "universal burn" proposal approved in October will fix that, but only from 2027.</span></div>
</div>
<div>
<div style="font-weight:700;color:#5B5F6B;margin-bottom:0.6rem;">Ethereum's weak spots</div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Privacy is still a promise.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">The Foundation's wallet toolkit is still being built, and privacy on public chains carries legal baggage — some of the best-known privacy tools have faced sanctions in the past.</span></div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Its answer recreates walled gardens.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">If every bank runs its own private Layer 2 like Prividium, Ethereum risks becoming a collection of closed networks that happen to send proofs to the same place — and many L2s still rely on a single company to order transactions.</span></div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;"><strong style="color:#111318;">Losing share, slowly.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Ethereum still dominates tokenized assets, but its share has been slipping as other networks compete. Klarna, for example, launched its stablecoin on a different, purpose-built blockchain.</span></div>
</div>
</div>

What's no longer a weakness: cost. A few years ago, high and
unpredictable fees were one of the main arguments against Ethereum.
After the upgrades of late 2025, a simple transaction costs a few
cents.

> The trade-off in one line: Canton asks you to trust a club of known
> institutions; Ethereum asks you to trust open code and mathematics,
> and accept that the open world can see more than you'd like. Neither
> is free — the question is which price each kind of business is
> willing to pay.

## Here We Go? Not Yet

Back to Gyokeres. The transfer negotiation happens behind closed doors,
because no deal would ever close otherwise. The result is announced to
the world, registered and reported to the regulator, because everyone
needs to trust that it really happened.

Canton is built for the closed part. Ethereum is built for the public
part. The more each one tries to cover the other's ground, the more
they start to look alike.

So "Canton vs. Ethereum" is the wrong question. JPMorgan, Circle and
even DTCC have already answered it, by using both. The more interesting
questions are about the border between them. Which activities belong in
private, and which in public? How does an asset move from one side to
the other without losing its legal protection? And who gets to set the
rules at the crossing? Projects are already starting to build those
bridges, and that's where I'd keep an eye over the next few years.

> So, here we go? Not yet. Deals are still being negotiated.
