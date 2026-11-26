---
title: "Is DeFi a Hydra or a Damocles?"
date: 2026-11-26
excerpt: "For one weekend in March 2023, the safest asset in DeFi traded at $0.88. Nassim Taleb has a name for systems that break, survive, or get stronger under stress — and DeFi likes to think it's the third kind. Four real collapses later, here's whether that claim holds."
tags: ["DeFi", "stablecoins", "RWA", "risk"]
cover: "/images/hydra_damocles.jpg"
slug: "is-defi-a-hydra-or-a-damocles"
---

For years, USDC was the "boring" part of crypto. One token, one dollar,
backed by cash and short-term Treasuries. It was where most people
parked their money while everything else moved.

Then came Friday, 10 March 2023. That morning, Silicon Valley Bank
(SVB) entered resolution after depositors pulled over $40 billion in a
single day. At 10 p.m., Circle announced it couldn't withdraw $3.3
billion of USDC reserves from SVB — around 8% of the total — and
redemption requests came flooding in.

By Saturday, USDC had fallen to $0.88. DAI, the flagship decentralized
stablecoin, was more than half backed by USDC and hit similar lows at
almost the same moment.

Nothing on-chain broke. There was no hack and no bug. Every smart
contract did exactly what it was built to do. The weak point was a
bank account in California.

By Monday the scare was over. US authorities protected all deposits at
SVB, and Circle said the reserve risk was gone once the funds became
available that morning. But for one weekend, the safest asset in DeFi
did not look like it.

So here comes Nassim Taleb, who has a framework for systems like this.
In *Antifragile*, he splits the world into three kinds of things: those
that break under stress, those that survive it, and those that get
stronger from it. DeFi likes to think it belongs in the third group.
This post puts that claim to the test, and asks what happens when RWAs
bring even more threads into the system.

## Taleb in Three Minutes

Most people think the opposite of fragile is robust. Taleb says that
only gets you halfway. A wine glass breaks when you drop it, and a
steel cup survives the fall. But we have no word for something that
gets *better* when it's dropped. Taleb made the word: antifragile.

To explain it, he uses three myths:

- **Damocles — fragile.** He feasts at a royal banquet with a sword
  hanging over his head by a single horse hair. Everything is fine
  while the hair holds, but sooner or later it snaps.
- **The Phoenix — robust.** Each time it's destroyed, it's reborn from
  its own ashes, exactly as it was before.
- **The Hydra — antifragile.** Cut off one head and two grow back. Harm
  makes it stronger.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 460" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Damocles breaks suddenly, the Phoenix returns unchanged, the Hydra comes back stronger">
<g font-family="Inter, sans-serif">

  <rect x="40" y="40" width="360" height="380" rx="16" fill="#EEF2FC"/>
  <circle cx="220" cy="110" r="30" fill="#1E3A8A"/>
  <line x1="220" y1="90" x2="220" y2="104" stroke="#FFFFFF" stroke-width="4"/>
  <path d="M208 104 L232 104 L220 128 Z" fill="#FFFFFF"/>
  <text x="220" y="178" text-anchor="middle" font-size="22" font-weight="700" fill="#111318">Damocles</text>
  <text x="220" y="202" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="1" fill="#1E3A8A">FRAGILE</text>
  <text x="220" y="240" text-anchor="middle" font-size="13" fill="#5B5F6B">Breaks suddenly after</text>
  <text x="220" y="260" text-anchor="middle" font-size="13" fill="#5B5F6B">a long calm.</text>
  <line x1="70" y1="300" x2="370" y2="300" stroke="#D4D6DC" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="220" y="322" text-anchor="middle" font-size="11" letter-spacing="1" fill="#9094A0">IN DEFI, IT LOOKS LIKE&#8230;</text>
  <text x="220" y="348" text-anchor="middle" font-size="13" fill="#111318">A stablecoin that depends</text>
  <text x="220" y="370" text-anchor="middle" font-size="13" fill="#111318">on one bank account.</text>

  <rect x="420" y="40" width="360" height="380" rx="16" fill="#EEF2FC"/>
  <circle cx="600" cy="110" r="30" fill="#1E3A8A"/>
  <path d="M588 100 A14 14 0 1 1 588 120" fill="none" stroke="#FFFFFF" stroke-width="4"/>
  <path d="M588 120 L582 112 M588 120 L596 116" fill="none" stroke="#FFFFFF" stroke-width="4"/>
  <text x="600" y="178" text-anchor="middle" font-size="22" font-weight="700" fill="#111318">The Phoenix</text>
  <text x="600" y="202" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="1" fill="#1E3A8A">ROBUST</text>
  <text x="600" y="240" text-anchor="middle" font-size="13" fill="#5B5F6B">Returns to where it was,</text>
  <text x="600" y="260" text-anchor="middle" font-size="13" fill="#5B5F6B">unchanged.</text>
  <line x1="450" y1="300" x2="750" y2="300" stroke="#D4D6DC" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="600" y="322" text-anchor="middle" font-size="11" letter-spacing="1" fill="#9094A0">IN DEFI, IT LOOKS LIKE&#8230;</text>
  <text x="600" y="348" text-anchor="middle" font-size="13" fill="#111318">A protocol that pauses,</text>
  <text x="600" y="370" text-anchor="middle" font-size="13" fill="#111318">patches and reopens.</text>

  <rect x="800" y="40" width="360" height="380" rx="16" fill="#EEF2FC"/>
  <circle cx="980" cy="110" r="30" fill="#1E3A8A"/>
  <path d="M980 96 V124 M968 102 L980 112 L992 102 M968 118 L980 112 L992 118" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>
  <text x="980" y="178" text-anchor="middle" font-size="22" font-weight="700" fill="#111318">The Hydra</text>
  <text x="980" y="202" text-anchor="middle" font-size="13" font-weight="600" letter-spacing="1" fill="#1E3A8A">ANTIFRAGILE</text>
  <text x="980" y="240" text-anchor="middle" font-size="13" fill="#5B5F6B">Comes back stronger</text>
  <text x="980" y="260" text-anchor="middle" font-size="13" fill="#5B5F6B">than before.</text>
  <line x1="830" y1="300" x2="1130" y2="300" stroke="#D4D6DC" stroke-width="2" stroke-dasharray="4 4"/>
  <text x="980" y="322" text-anchor="middle" font-size="11" letter-spacing="1" fill="#9094A0">IN DEFI, IT LOOKS LIKE&#8230;</text>
  <text x="980" y="348" text-anchor="middle" font-size="13" fill="#111318">An ecosystem where each</text>
  <text x="980" y="370" text-anchor="middle" font-size="13" fill="#111318">exploit leads to better audits.</text>

</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Three myths, three ways of meeting stress.</figcaption>
</figure>

### The Pebble Test

How do you tell which one you're looking at? Taleb borrows an old
rabbinical story. A furious king swears to crush his son with a huge
stone. Once he calms down, he regrets the oath, but a king cannot break
his word. His advisor finds a way out: cut the stone into tiny pebbles
and throw those at him instead. It is the same weight of stone. One way
kills him, and the other leaves a few bruises.

That's Taleb's test for fragility. If a shock twice as big does more
than twice the damage, the thing is fragile — the damage speeds up as
the shock grows. If a shock twice as big brings more than twice the
gain, the thing is antifragile.

Taleb gives these two shapes names. Draw the damage against the size of
the shock and you don't get a straight line, you get a curve. When the
harm bends upward and gets steeper with every extra bit of shock, the
curve is concave: small shocks barely matter, big ones are
catastrophic. That's the fragile. When the gain bends upward instead,
the curve is convex: you lose a little when things are calm and win a
lot when they aren't. That's the antifragile, and it's why convex
things actually like volatility. On average, disorder pays them.

In DeFi, this is easy to find. If ETH drops 5%, a few loans get
liquidated. If it drops 30%, the liquidations dump collateral onto the
market, which pushes prices lower, which triggers more liquidations.
Each extra percent hurts more than the one before. That is the stone,
not the pebbles.

So keep the test in mind for the rest of this post. For any protocol,
ask one question: what happens when the shock doubles?

## Where DeFi Is Genuinely Antifragile

### The Restaurant Rule

Taleb's favourite example is restaurants. Each one on its own is
fragile. They open, struggle and close all the time. Yet the restaurant
scene as a whole keeps getting better, precisely because bad
restaurants die fast and the rest learn from them. The same goes for
the coffee machine in your kitchen — it's better because other
entrepreneurs failed trying to sell you one first. Antifragility works
in layers: the whole gets stronger because the parts are allowed to
break.

DeFi looks a lot like this. Protocols launch, get exploited and die. It
is painful for the people inside, but every failure is public, recorded
on-chain and picked apart within days. The next team reads the
post-mortem. Reentrancy bugs, oracle manipulation, flash-loan attacks:
each becomes a known pattern because someone paid for it first. That's
the Hydra. Lose a head, grow back better ones.

### Skin in the Game: Black Thursday

On 12 March 2020, ETH crashed, the Ethereum network jammed and
MakerDAO's liquidation auctions broke. Bots won collateral for nothing:
cumulative losses from auctions with zero bids amounted to $8.3
million. The protocol was left with a hole.

What happened next is the interesting part. There was no government and
no bailout. By design, MKR holders cover these shortfalls through MKR
dilution, and that risk is what pushes them to govern responsibly. By
29 March, 20,980 MKR had been auctioned off to raise Dai and cover the
hole. The community then set out to change the auction rules so keepers
could no longer be locked out of bidding.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Zero-bid auctions left a debt hole, which was closed by minting and auctioning new MKR">
<g font-family="Inter, sans-serif">
  <rect x="40" y="60" width="300" height="160" rx="16" fill="#EEF2FC"/>
  <text x="190" y="120" text-anchor="middle" font-size="18" font-weight="700" fill="#111318">Zero-bid auctions</text>
  <text x="190" y="148" text-anchor="middle" font-size="13" fill="#5B5F6B">$8.3M in collateral</text>
  <text x="190" y="168" text-anchor="middle" font-size="13" fill="#5B5F6B">won for nothing</text>

  <path d="M355 140 H430" stroke="#9094A0" stroke-width="3"/>
  <path d="M430 140 L412 129 M430 140 L412 151" stroke="#9094A0" stroke-width="3" fill="none"/>

  <rect x="450" y="60" width="300" height="160" rx="16" fill="#EEF2FC"/>
  <text x="600" y="120" text-anchor="middle" font-size="18" font-weight="700" fill="#111318">Protocol debt hole</text>
  <text x="600" y="148" text-anchor="middle" font-size="13" fill="#5B5F6B">No government,</text>
  <text x="600" y="168" text-anchor="middle" font-size="13" fill="#5B5F6B">no bailout</text>

  <path d="M765 140 H840" stroke="#9094A0" stroke-width="3"/>
  <path d="M840 140 L822 129 M840 140 L822 151" stroke="#9094A0" stroke-width="3" fill="none"/>

  <rect x="860" y="60" width="300" height="160" rx="16" fill="#1E3A8A"/>
  <text x="1010" y="120" text-anchor="middle" font-size="18" font-weight="700" fill="#FFFFFF">MKR dilution</text>
  <text x="1010" y="148" text-anchor="middle" font-size="13" fill="#DCE4F7">+20,980 MKR minted</text>
  <text x="1010" y="168" text-anchor="middle" font-size="13" fill="#DCE4F7">and auctioned off</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">MKR holders, not taxpayers, absorbed Black Thursday's shortfall.</figcaption>
</figure>

Compare that with 2008. Taleb argues that bailouts move fragility from
the system onto the people least fit to carry it, and protect the firms
that took the risk. At MakerDAO, the people who governed the system
paid for its failure, and then they fixed it.

### Tinkering in Public

Taleb argues that most innovation comes from trial and error, not from
top-down plans. DeFi is tinkering at scale. Code is open, and anyone
can copy a design that works, change one thing and ship it. Each
project is a small bet: if it fails the loss is limited, but if it
works, the upside is huge. That is a convex curve built from thousands
of cheap experiments.

## Where DeFi Is Fragile

Taleb's restaurant rule has some limitations. Dangerous risk-taking is
healthy for the whole system only under three conditions.

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">1. Failures stay local</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">When one restaurant closes, the place across the street does not go bankrupt.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">2. Not everyone takes the same risk</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Diners spread themselves across many kitchens, many cuisines, many bets.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">3. No one's fall drags others down</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">A closed restaurant doesn't take its suppliers, landlord and staff's other jobs with it.</div>
  </div>
</div>

Restaurants pass all three. DeFi is built on protocols plugging into
each other like Lego. That is what makes it powerful, and it is also
what breaks the rule.

### Case 1: Stream Finance, One Fall and Many Victims

In November 2025, Stream Finance announced that an external fund
manager had lost about $93 million in user assets, and it immediately
suspended all withdrawals and deposits. Its stablecoin, xUSD, crashed
from its $1 peg and fell more than 70%.

The $93 million was only the start. Analysts mapped about $285 million
in Stream-linked debt across at least seven networks, involving
counterparties such as Elixir, MEV Capital, Varlamore and TelosC. The
reason was a loop: USDC became deUSD, deUSD became leverage, leverage
minted xUSD, and xUSD borrowed more USDC.

<figure style="margin:2em 0;">
<svg viewBox="0 0 900 560" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="USDC becomes deUSD, deUSD becomes leverage, leverage mints xUSD, and xUSD borrows more USDC, closing the loop">
<g font-family="Inter, sans-serif">
  <circle cx="450" cy="280" r="190" fill="none" stroke="#D4D6DC" stroke-width="2" stroke-dasharray="6 6"/>
  <text x="450" y="280" text-anchor="middle" font-size="13" letter-spacing="1" fill="#9094A0">THE LOOP</text>

  <rect x="365" y="40" width="170" height="80" rx="14" fill="#1E3A8A"/>
  <text x="450" y="88" text-anchor="middle" font-size="17" font-weight="700" fill="#FFFFFF">USDC</text>

  <rect x="700" y="240" width="170" height="80" rx="14" fill="#EEF2FC"/>
  <text x="785" y="288" text-anchor="middle" font-size="17" font-weight="700" fill="#111318">deUSD</text>

  <rect x="365" y="440" width="170" height="80" rx="14" fill="#EEF2FC"/>
  <text x="450" y="488" text-anchor="middle" font-size="17" font-weight="700" fill="#111318">Leverage</text>

  <rect x="30" y="240" width="170" height="80" rx="14" fill="#EEF2FC"/>
  <text x="115" y="288" text-anchor="middle" font-size="17" font-weight="700" fill="#111318">xUSD</text>

  <path d="M538 90 C 640 110, 720 170, 760 238" fill="none" stroke="#1E3A8A" stroke-width="3"/>
  <path d="M760 238 L756 216 M760 238 L738 232" fill="none" stroke="#1E3A8A" stroke-width="3"/>

  <path d="M770 322 C 720 400, 630 445, 538 470" fill="none" stroke="#1E3A8A" stroke-width="3"/>
  <path d="M538 470 L560 464 M538 470 L548 450" fill="none" stroke="#1E3A8A" stroke-width="3"/>

  <path d="M362 470 C 260 445, 170 400, 130 322" fill="none" stroke="#1E3A8A" stroke-width="3"/>
  <path d="M130 322 L140 342 L156 326" fill="none" stroke="#1E3A8A" stroke-width="3"/>

  <path d="M140 238 C 180 170, 260 110, 362 90" fill="none" stroke="#1E3A8A" stroke-width="3" stroke-dasharray="5 5"/>
  <path d="M362 90 L340 96 L348 76" fill="none" stroke="#1E3A8A" stroke-width="3" stroke-dasharray="0"/>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Each step looked safe alone. The dashed arrow is where xUSD borrowed more USDC — closing the loop.</figcaption>
</figure>

Each step looked safe on its own. Together they built one long chain,
and when one link broke, every lender attached to it was hit. That's
condition 3 failing in the clearest possible way: one restaurant
closes, and half the street goes with it.

### Case 2: 10 October 2025, the Squeeze

Taleb's favourite example of a forced sale is Société Générale in 2008.
After uncovering Jérôme Kerviel's hidden positions, the bank had to
dump around $70 billion of stocks into a thin market. The size alone
was not the problem. The problem was that it could not wait. When
selling is not optional, a fire sale occurs.

DeFi liquidation engines are built never to wait. On 10 October 2025,
over $19 billion in leveraged positions were forcibly closed within 24
hours — nine times the size of any previous single-day liquidation
event. Prices fell, liquidations fired, prices fell further. That is
the concave curve from the Pebble Test, alive and running.

It also hit the weakest point we have already met on this blog: [the
Oracle Problem](/posts/the-oracle-problem). As Binance's oracle became
the "price of record" across the leveraged trading ecosystem, its
mispriced feeds spread to other exchanges and DEXs. Many protocols were
reading the same broken thermometer — condition 2 failing.

Hyperliquid processed more than $10 billion of the liquidations, while
Binance accounted for roughly $2.4 billion. It was crypto leverage
everywhere, on-chain and off. But the mechanism is the same one DeFi
runs on.

## Why Stablecoins Are the Sharpest Case

In *Antifragile*, Taleb borrows from James Maxwell, who showed that
controlling an engine too tightly makes it unstable. Taleb applies the
same idea to markets. When you suppress all volatility, you get long
calm periods broken by violent jumps.

> Of a currency that never moves, Taleb writes: "a slight, very slight
> move makes people believe that the world is ending."

A stablecoin is designed so its price never moves. That is why a drop
of a few cents feels like a crisis. Think of the USDC weekend from the
opening of this post, or USDe falling to $0.65 on Binance — 35% below
its peg — which triggered secondary liquidations across the market.
That is Damocles: years of calm, and then the hair snaps.

## And the Real World Assets?

On-chain RWA value, excluding stablecoins, has swung hard through
2025 — from under $25 billion to a peak above $29 billion and back down
again, depending on the month and on rwa.xyz's own changing
methodology. The exact number moves fast; what matters here is the
shape of the risk, not the decimal point.

Through Taleb's lens, RWAs change DeFi's risk in one specific way. They
bring the off-chain thread back.

### More Threads

When you hold ETH, the risk sits in the code and the market. When you
hold a tokenized Treasury fund, it sits in the code, plus the
custodian, the bank, the transfer agent, the legal wrapper and whoever
reports the fund's value on-chain. Each one is a hair holding up a
sword. USDC is about the simplest RWA there is, and its hair was a
single bank account.

### Everyone Taking the Same Risk

This is where condition 2 comes back. Not everyone should take the same
risk. Look at BlackRock's BUIDL fund: it supplies more than 90% of the
reserves behind Ethena's USDtb and Jupiter's JupUSD on Solana, and it
has been accepted as collateral on Binance.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="BlackRock's BUIDL fund supplies reserves behind USDtb, JupUSD and collateral on Binance">
<g font-family="Inter, sans-serif">
  <rect x="440" y="160" width="320" height="100" rx="16" fill="#1E3A8A"/>
  <text x="600" y="203" text-anchor="middle" font-size="18" font-weight="700" fill="#FFFFFF">BlackRock BUIDL</text>
  <text x="600" y="228" text-anchor="middle" font-size="12" fill="#DCE4F7">tokenized Treasury fund</text>

  <path d="M760 190 C 900 150, 1000 110, 1080 70" fill="none" stroke="#9094A0" stroke-width="3"/>
  <path d="M760 210 C 920 210, 1000 210, 1080 210" fill="none" stroke="#9094A0" stroke-width="3"/>
  <path d="M760 230 C 900 270, 1000 320, 1080 350" fill="none" stroke="#9094A0" stroke-width="3"/>

  <rect x="1080" y="30" width="200" height="80" rx="14" fill="#EEF2FC" transform="translate(-140,0)"/>
  <rect x="940" y="30" width="200" height="80" rx="14" fill="#EEF2FC"/>
  <text x="1040" y="68" text-anchor="middle" font-size="15" font-weight="700" fill="#111318">Ethena USDtb</text>
  <text x="1040" y="90" text-anchor="middle" font-size="11" fill="#5B5F6B">&gt;90% of reserves</text>

  <rect x="940" y="170" width="200" height="80" rx="14" fill="#EEF2FC"/>
  <text x="1040" y="208" text-anchor="middle" font-size="15" font-weight="700" fill="#111318">Jupiter JupUSD</text>
  <text x="1040" y="230" text-anchor="middle" font-size="11" fill="#5B5F6B">&gt;90% of reserves</text>

  <rect x="940" y="310" width="200" height="80" rx="14" fill="#EEF2FC"/>
  <text x="1040" y="348" text-anchor="middle" font-size="15" font-weight="700" fill="#111318">Binance</text>
  <text x="1040" y="370" text-anchor="middle" font-size="11" fill="#5B5F6B">accepted as collateral</text>

  <rect x="40" y="160" width="320" height="100" rx="16" fill="#EEF2FC"/>
  <text x="200" y="203" text-anchor="middle" font-size="15" font-weight="700" fill="#111318">One fund, one kitchen</text>
  <text x="200" y="228" text-anchor="middle" font-size="12" fill="#5B5F6B">feeding several "restaurants"</text>
  <path d="M365 210 H425" stroke="#9094A0" stroke-width="3"/>
  <path d="M425 210 L407 199 M425 210 L407 221" stroke="#9094A0" stroke-width="3" fill="none"/>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">A problem at BUIDL would not stay local — it reaches every "restaurant" sharing its kitchen.</figcaption>
</figure>

But this is not a criticism. Treasuries are among the safest assets in
the world. The problem is structural. When many on-chain dollars are
built on the same fund, a problem at that one fund — whether
operational, legal or a delay in redemptions — is not local anymore. It
is a street of restaurants sharing a single kitchen.

BlackRock has asked the OCC to scrap a proposed 20% cap on tokenized
reserve assets in the GENIUS Act's draft rules, arguing that reserve
risk depends on credit quality, duration and liquidity, not on whether
an asset moves on a distributed ledger. On credit quality, maybe
BlackRock has a point. Taleb would ask a different question: not how
safe is the asset, but how many people depend on it at the same time?

## Make RWAs Behave Like Restaurants

Taleb's advice for fragile systems is usually to remove things, not add
them. For RWAs in DeFi, that means:

- **Fewer loops.** Don't reuse the same RWA as collateral across five
  protocols.
- **Fewer single points of failure.** Several funds and several
  custodians, not one.
- **Isolated markets.** One bad asset shouldn't be able to drain a
  shared lending pool.
- **More than one independent data source** per asset.
- **A redemption path tested under stress**, not just written into the
  legal documents.

## Would Taleb Approve?

Taleb was not always a crypto sceptic. In 2018 he called Bitcoin "the
first organic currency" in the foreword to *The Bitcoin Standard*, and
"an insurance policy" against government control over money.

Three years later he changed his mind. In his 2021 paper *Bitcoin,
Currencies, and Fragility*, he argued that it had failed as a currency
without government, as a hedge against inflation and as a safe haven.
In a CNBC interview tied to the paper's release, his verdict was blunt:
"Few assets in financial history have been more fragile than bitcoin."

One of his key arguments matters for this post. Bitcoin, he says,
depends on the existence of miners for perpetuity. Gold, by contrast,
needs no one to keep it going. If something only survives as long as
someone keeps maintaining it, it is not antifragile.

By that logic, Taleb would probably be even harder on DeFi. A lending
protocol needs miners or validators, plus oracles, liquidators, bridges
and front-ends. Plug in RWAs and you add custodians, banks, transfer
agents and lawyers. That is a lot of hands holding a lot of threads.

But his own framework also gives DeFi something he does not give it
credit for. Protocols die in public, and the ecosystem learns from it.
At MakerDAO, the people who governed the system paid for its failure.
Those are the restaurant rule and skin in the game, two of Taleb's own
ideas, working on-chain.

## Hydra or Damocles?

If we go back to that weekend in March 2023, nothing on-chain broke.
The code worked, the contracts worked, the protocols worked. What
failed was a thread nobody was watching.

That is the real lesson. DeFi cannot be a Hydra or a Damocles by
nature. It is whichever one its design makes it. Before trusting any
protocol, stablecoin or tokenized asset, we can ask four questions:

1. If it fails, does the failure stay local?
2. Does everyone depend on the same thing?
3. Who pays when it breaks?
4. What happens when the shock doubles?

Every RWA adds threads, and as more RWAs come on-chain, these questions
only become more important.

The Hydra grows two heads for every one that's cut off. But that only
works if the heads aren't all attached to the same neck.
