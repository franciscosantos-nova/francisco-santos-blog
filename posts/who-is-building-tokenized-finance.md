---
title: "Who's Building the Rails for Tokenized Finance?"
date: 2026-10-09
excerpt: "BlackRock, Circle, JPMorgan and even the DTCC are all racing to put real money on-chain — for very different reasons."
tags: ["RWA", "tokenization", "DeFi", "institutions"]
cover: "/images/rails-cover.svg"
slug: "who-is-building-tokenized-finance"
---

Ask many Portuguese families where they keep their savings, and sooner or
later someone mentions Certificados de Aforro. You lend money to the
Portuguese state, and the state pays you interest. Simple, safe.

Now imagine the same idea, but instead of a paper certificate, you hold a
token in a digital wallet. You could send it to someone in seconds, and it
would keep earning interest every single day.

Some of the largest financial companies in the world already offer exactly
this, using US government debt instead of Portuguese. And they are just the
beginning.

<div style="overflow-x:auto;margin:1.75em 0;border:1px solid #E7E8EC;border-radius:12px;">
<table style="width:100%;border-collapse:collapse;font-size:0.875rem;min-width:560px;">
<thead>
<tr style="background:#EEF2FC;">
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Company</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Product</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">What it is</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Launched</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Network</th>
</tr>
</thead>
<tbody>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Franklin Templeton</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">BENJI</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized money market fund</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">2021</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Stellar (+ since)</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">BlackRock</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">BUIDL</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized money market fund</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Mar 2024</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Ethereum (+ since)</td></tr>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Circle</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">USYC</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized yield fund</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Acquired 2025</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Multi-chain</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Ondo Finance</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">USDY / OUSG</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized Treasuries</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">2023</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Multi-chain</td></tr>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">JPMorgan</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">JPM Coin</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Deposit token</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">2019</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Base &#8594; Canton</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Goldman Sachs &amp; HSBC</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Digital bonds (EIB)</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized bond issuance</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">2022–23</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Private platforms</td></tr>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">DTCC</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Live pilot</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Tokenized stocks, ETFs, Treasuries</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Jul 2026</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">—</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">HKEX</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Synapse</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Settlement platform</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Oct 2023</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;white-space:nowrap;">Smart contracts</td></tr>
</tbody>
</table>
</div>

## The asset managers: selling the same product in another way

The first big names to move were asset management companies — the ones who
run funds on behalf of investors. Their logic is simple: they already sell
funds that hold safe government debt, so why not let people hold those
funds as tokens?

Franklin Templeton was first. Back in 2021, long before tokenization was
so well known, it launched BENJI, a US government money market fund that
records ownership on a public blockchain. Each token is a share of a
regulated fund.

BlackRock also joined the game. In March 2024, the world's largest asset
manager launched BUIDL on Ethereum. The fund holds cash and short-term US
government debt, and each token represents a share of it. Investors earn
interest, paid out every day as new tokens land in their wallet. Within a
year, BUIDL had become the largest tokenized fund in the world.

Since then, tokenization stopped being a crypto experiment and became
something serious institutions had to have an opinion on.

## The twist: crypto companies are keeping up

If you think BlackRock owns this market, think again. By mid-September
2026, BUIDL was still the largest tokenized government debt fund — but
only by a small margin. A close competitor is USYC, a fund owned by
Circle, the company behind the USDC stablecoin. Close behind both was
Ondo, a company built from day one to put real-world assets on-chain.

<figure style="margin:1.75em 0;">
<svg viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Approximate AUM: BlackRock BUIDL about 2.9 billion dollars, Circle USYC about 2.8 billion, Ondo about 2.6 billion">
  <line x1="170" y1="12" x2="170" y2="162" stroke="#E7E8EC" stroke-width="1"/>
  <path d="M170,20 H464 Q468,20 468,24 V38 Q468,42 464,42 H170 Z" fill="#1E3A8A"/>
  <text x="160" y="35" text-anchor="end" font-family="Inter, sans-serif" font-size="13" font-weight="500" fill="#5B5F6B">BlackRock &#183; BUIDL</text>
  <text x="478" y="35" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#111318">$2.9B</text>

  <path d="M170,76 H454 Q458,76 458,80 V94 Q458,98 454,98 H170 Z" fill="#1E3A8A"/>
  <text x="160" y="91" text-anchor="end" font-family="Inter, sans-serif" font-size="13" font-weight="500" fill="#5B5F6B">Circle &#183; USYC</text>
  <text x="468" y="91" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#111318">$2.8B</text>

  <path d="M170,132 H433 Q437,132 437,136 V150 Q437,154 433,154 H170 Z" fill="#1E3A8A"/>
  <text x="160" y="147" text-anchor="end" font-family="Inter, sans-serif" font-size="13" font-weight="500" fill="#5B5F6B">Ondo &#183; USDY/OUSG</text>
  <text x="447" y="147" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#111318">$2.6B</text>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Illustrative, approximate AUM — the leaderboard has flipped several times and shifts week to week. Live numbers: <a href="https://app.rwa.xyz" style="color:#9094A0;">rwa.xyz</a></figcaption>
</figure>

Circle didn't build USYC itself. In January 2025, it bought the startup
that created it, and at the time USYC was actually bigger than BlackRock's
fund. The two have been trading places ever since.

So why can a crypto company compete with the world's largest asset
manager? It's called distribution. BlackRock sells mainly to big
institutional clients. Circle and Ondo already sit in the middle of crypto
markets, where traders need somewhere safe to park cash between trades. A
token that earns government bond interest and can be swapped in and out of
USDC in seconds is exactly what they want. The token also works as
collateral on exchanges, not just as an investment.

For now, both are winning. Traditional giants bring trust and scale;
crypto-native firms bring users and speed.

## The banks: tokenizing money itself

Banks are playing a different game. Instead of selling tokenized funds,
they are rebuilding their own infrastructure, starting with the most basic
asset of all: money.

JPMorgan is the clearest example. Its JPM Coin is a deposit token — a
digital version of real dollars inside a JPMorgan account. Unlike a
stablecoin issued by a tech company, it is a direct claim on the bank, with
the same protections as any other deposit. Institutional clients can use
it to send money 24/7, in near real time, including on weekends when
traditional payment systems are closed. JPMorgan also didn't pick one
blockchain: JPM Coin first went live on Base, a public network built on
Ethereum, and is now also going to Canton.

Goldman Sachs and HSBC went to bonds. Both built their own tokenization
platforms and used them to issue digital bonds for the European Investment
Bank. The pitch is faster issuance, instant settlement, and less paperwork
between issuer and investor.

Many of these banks are building on Canton, a blockchain designed
specifically for financial institutions. Its key feature is privacy: banks
can transact with each other without exposing their positions to
competitors — something a fully public network like Ethereum doesn't
offer by default.

## The infrastructure

There are institutions that sit underneath every trade, making sure that
when you buy a share, you actually get it and the seller actually gets
paid.

DTCC (Depository Trust & Clearing Corporation) is one of the clearest
examples. Almost nobody outside finance knows its name, yet it settles most
US securities trades. In July 2026, it ran its first live trades using
tokenized stocks, ETFs and US Treasuries, with more than 30 firms involved,
including BlackRock and JPMorgan. These aren't new products — they're the
same securities DTCC already holds, now able to move as tokens.

Hong Kong shows a softer version of the same idea. HKEX, the Hong Kong
Stock Exchange, uses Synapse, a platform built on smart contracts, to speed
up settlement for international investors trading Chinese stocks through
Stock Connect. Investors in different time zones have to meet mainland
China's same-day settlement deadline, and smart contracts help keep every
party in sync.

## Conclusion

Looking at all these players together, there are three things worth
taking away.

First, this is no longer an experiment. Major institutions are putting
their best effort into it.

Second, everyone is entering for a different reason. Asset managers want
new ways to sell their products. Crypto companies want safe, yield-earning
assets for their users. Banks want faster money. Market infrastructure
wants faster settlement.

> The real competition is not between banks and crypto, or between
> Ethereum and Canton. It is about who builds the rails that everyone
> else ends up using.
