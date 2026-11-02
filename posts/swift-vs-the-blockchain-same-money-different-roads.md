---
title: "SWIFT vs. the Blockchain: Same Money, Different Roads"
date: 2026-11-02
excerpt: "A €10 transfer to a friend in Lisbon lands before he's finished his drink. The same kind of payment, €500 to Argentina, takes days and loses money along the way. Here's what actually happens inside both, and why stablecoins only win once you look at the edges."
tags: ["stablecoins", "payments", "crypto", "finance"]
cover: "/images/cover-page-stablecoins.jpg"
slug: "swift-vs-the-blockchain-same-money-different-roads"
---

It's Friday night in Bairro Alto, Lisbon. Classes are over for the week,
the streets are packed, and a friend has just paid for a round of
drinks. You owe him €10. You open your banking app, send it, and before
he's finished his drink, the money is already in his account. Since
October 2025, every bank in the euro area has had to offer instant
transfers, around the clock, at no extra cost. Europe quietly fixed one
of banking's oldest annoyances.

Among the group that night is Carlitos, an exchange student from Buenos
Aires. At the end of the semester he flies home, and a few weeks later
you still owe him €500 for a trip you planned together. Now you need to
send it to Argentina. The money leaves your account, passes through a
chain of banks, gets converted along the way, and arrives some days
later, often after the weekend, with a slice taken off for fees and the
exchange rate. Same friends, same kind of payment, completely different
experience.

Carlitos has a simpler suggestion: just send him dollars in a
stablecoin. In Argentina, where people have spent years watching the
peso lose value, digital dollars like USDT and USDC have become part of
everyday financial life. In Nigeria, the country that received the most
crypto in Africa last year, stablecoin activity rises almost in step
with every drop in the naira.

For millions of people, stablecoins are not a crypto experiment. They
are the fastest way to move money, and the easiest way to hold dollars.
So how do they actually compare with the banking system we already
have? And what happens when money goes in, and when it comes back out?

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The traditional path: euros, through your bank, SWIFT, correspondent banks, and Carlitos's bank, to pesos">
<g font-family="Inter, sans-serif">
<rect x="20" y="30" width="195" height="110" rx="14" fill="#EEF2FC"/>
<text x="117" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">You pay</text>
<text x="117" y="99" text-anchor="middle" font-size="13" fill="#5B5F6B">in euros</text>
<path d="M223 85 H272" stroke="#9094A0" stroke-width="2.5"/>
<path d="M272 85 L258 77 M272 85 L258 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="280" y="30" width="195" height="110" rx="14" fill="#EEF2FC"/>
<text x="377" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">Your bank</text>
<text x="377" y="99" text-anchor="middle" font-size="13" fill="#5B5F6B">sends a SWIFT message</text>
<path d="M483 85 H532" stroke="#9094A0" stroke-width="2.5"/>
<path d="M532 85 L518 77 M532 85 L518 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="540" y="30" width="195" height="110" rx="14" fill="#1E3A8A"/>
<text x="637" y="70" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">Correspondent</text>
<text x="637" y="90" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">banks</text>
<text x="637" y="112" text-anchor="middle" font-size="12.5" fill="#DCE4F7">fees + FX margin, each stop</text>
<path d="M743 85 H792" stroke="#9094A0" stroke-width="2.5"/>
<path d="M792 85 L778 77 M792 85 L778 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="800" y="30" width="195" height="110" rx="14" fill="#EEF2FC"/>
<text x="897" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">Carlitos's bank</text>
<text x="897" y="99" text-anchor="middle" font-size="13" fill="#5B5F6B">in Argentina</text>
<path d="M1003 85 H1052" stroke="#9094A0" stroke-width="2.5"/>
<path d="M1052 85 L1038 77 M1052 85 L1038 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="1060" y="30" width="120" height="110" rx="14" fill="#EEF2FC"/>
<text x="1120" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">Pesos</text>
<text x="1120" y="99" text-anchor="middle" font-size="13" fill="#5B5F6B">received</text>
<text x="600" y="200" text-anchor="middle" font-size="15" fill="#5B5F6B">⏱ 1–5 business days &#160;&#160;·&#160;&#160; 💸 fees often unknown until arrival &#160;&#160;·&#160;&#160; 🕘 banking hours only</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">The traditional path. SWIFT doesn't move money — it only carries the instructions. The money queues through every bank in between.</figcaption>
</figure>

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The stablecoin path: euros, through an on-ramp, the blockchain, and an off-ramp, to pesos">
<g font-family="Inter, sans-serif">
<rect x="20" y="30" width="180" height="110" rx="14" fill="#EEF2FC"/>
<text x="110" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">You pay</text>
<text x="110" y="99" text-anchor="middle" font-size="13" fill="#5B5F6B">in euros</text>
<path d="M208 85 H257" stroke="#9094A0" stroke-width="2.5"/>
<path d="M257 85 L243 77 M257 85 L243 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="265" y="30" width="205" height="110" rx="14" fill="#EEF2FC"/>
<text x="367" y="70" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">On-ramp</text>
<text x="367" y="91" text-anchor="middle" font-size="13" fill="#5B5F6B">€ → USDC</text>
<text x="367" y="112" text-anchor="middle" font-size="12" fill="#9094A0">ID check + fee/spread</text>
<path d="M478 85 H527" stroke="#9094A0" stroke-width="2.5"/>
<path d="M527 85 L513 77 M527 85 L513 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="535" y="30" width="205" height="110" rx="14" fill="#1E3A8A"/>
<text x="637" y="78" text-anchor="middle" font-size="16" font-weight="600" fill="#FFFFFF">Blockchain</text>
<text x="637" y="99" text-anchor="middle" font-size="13" fill="#DCE4F7">seconds, 24/7</text>
<path d="M748 85 H797" stroke="#9094A0" stroke-width="2.5"/>
<path d="M797 85 L783 77 M797 85 L783 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="805" y="30" width="205" height="110" rx="14" fill="#EEF2FC"/>
<text x="907" y="70" text-anchor="middle" font-size="16" font-weight="600" fill="#111318">Off-ramp</text>
<text x="907" y="91" text-anchor="middle" font-size="13" fill="#5B5F6B">USDC → pesos</text>
<text x="907" y="112" text-anchor="middle" font-size="12" fill="#9094A0">ID check + fee/spread</text>
<path d="M1018 85 H1060" stroke="#9094A0" stroke-width="2.5"/>
<path d="M1060 85 L1046 77 M1060 85 L1046 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="1068" y="30" width="112" height="110" rx="14" fill="#EEF2FC"/>
<text x="1124" y="78" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Pesos</text>
<text x="1124" y="99" text-anchor="middle" font-size="12" fill="#5B5F6B">received</text>
<text x="600" y="200" text-anchor="middle" font-size="15" fill="#5B5F6B">⏱ seconds in the middle &#160;&#160;·&#160;&#160; the ramps on each side set the real speed and cost</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">The stablecoin path. The blockchain in the middle is nearly instant. Everything that determines the real experience happens at the two ends.</figcaption>
</figure>

## How a Traditional Cross-Border Payment Works

When you send €500 to Carlitos in Buenos Aires, it feels like money
flying from one account to another. In reality, money between banks
moves as a series of accounting entries, and your bank almost certainly
has no direct relationship with Carlitos's bank in Argentina.

So it happens through intermediaries. Your bank holds an account with a
large international bank, which holds an account with another bank,
which eventually has a relationship in Argentina. These are called
correspondent banks, and your €500 travels along that chain. At each
stop, one bank debits one account and credits another.

The famous SWIFT network doesn't actually move any money. It only
carries the messages — the instructions telling each bank what to do.
The money itself sits in accounts that banks keep with each other, often
pre-funded in advance, just in case a payment needs to go through.

Each step along the chain adds friction:

- **Fees.** Intermediary banks can each take a cut, so Carlitos may
  receive less than you sent — and neither of you knows exactly how much
  until it arrives.
- **Exchange rates.** Somewhere along the way, euros become dollars or
  pesos, usually with a margin hidden in the rate.
- **Time.** Banks have cut-off times, work across different time zones,
  and don't settle on weekends or public holidays.
- **Checks.** Every bank runs its own anti-money-laundering checks, and
  any one of them can stop the payment for questions.

Add it all up and it's expensive. According to the World Bank, sending
the equivalent of $200 across a border costs on average more than 6% of
the amount sent — and sending it through a bank is usually far more
expensive than through a digital provider.

What about cards? A card payment abroad feels instant, but the same
complexity hides behind the tap. Four parties are involved: your bank,
which issued the card; the network, like Visa or Mastercard; the
merchant's bank; and the merchant itself. The payment is approved in
seconds, but the money settles between banks later, and fees are taken
along the way — from the merchant's side, and when currencies change,
from yours too.

## How a Stablecoin Payment Works

A stablecoin is a token designed to be worth exactly one unit of a
traditional currency, usually one US dollar. The best known are USDT,
issued by Tether, and USDC, issued by Circle. For every token in
circulation, the issuer says it holds an equivalent amount in reserves —
mostly cash and short-term US government debt. If that sounds familiar,
it's the coat check again: the token is the ticket, the reserves are the
coat, and whether you can trust the link between them is exactly the
question in [The Oracle Problem](/posts/the-oracle-problem).

Now the payment itself. Say you already have USDC in a digital wallet.
To pay Carlitos, you only need his wallet address. You enter the amount,
confirm, and the transaction is recorded on a blockchain. That's it.
There's no chain of correspondent banks, no SWIFT message, no account
sitting pre-funded somewhere waiting. The blockchain is both the
messaging system and the settlement system at the same time — the
moment the transaction is confirmed, the dollars have moved, and nobody
can quietly delay it.

So the experience is completely different:

- **Speed.** The transfer settles in seconds or minutes, not days.
- **Always on.** Blockchains don't close at 5pm, on weekends, or on
  public holidays. Friday night in Bairro Alto and Sunday at 3am are
  exactly the same.
- **Cost.** The network fee is often a few cents, and it doesn't depend
  on whether the money is going to Porto or to Buenos Aires.
- **Transparency.** Both of you can see the transaction on the
  blockchain, with the exact amount and time. No hidden deductions along
  the way.

And for Carlitos there's a bonus that has nothing to do with speed. He
receives dollars, and he can keep them as dollars. In a country where
people have spent years protecting their savings from inflation, that
matters as much as the transfer itself.

It sounds almost too good — and that's because we skipped two steps. You
didn't start with USDC, you started with euros. Carlitos can't pay his
rent in USDC, he needs pesos. That's where the real story begins.

## On-Ramp and Off-Ramp: Where the Real Race Happens

Nobody lives in stablecoins. You earn euros, Carlitos pays rent in
pesos. So every stablecoin payment is a sandwich: traditional money
going in, a stablecoin in the middle, traditional money coming out. The
blockchain is the filling. A sandwich, though, is only as good as its
bread.

**The on-ramp: euros in.** To get USDC, you need a platform that
converts your euros into stablecoins — usually an exchange or a fintech
app. You verify your identity, send euros, and buy the stablecoin. The
platform makes money through a fee, a spread on the exchange rate, or
both.

In Europe, this step is now heavily regulated. Under MiCA, the EU's
crypto rulebook, any platform serving European clients needs a licence,
and stablecoins must be authorised too. That has a surprising
consequence: USDC is authorised in the EU, but USDT, the largest
stablecoin in the world, is not — and licensed European exchanges no
longer offer it. So in Lisbon, you'd almost certainly send USDC, even if
Carlitos, like many people in Latin America, might prefer USDT.

**The off-ramp: pesos out.** On the other side, Carlitos has two
options. He can keep the dollars, which for many Argentinians is the
whole point, or he can sell them for pesos on a local exchange or app and
transfer the money to his bank account. Again there's an identity check,
a fee, and an exchange rate — and how good that rate is depends on how
many people are buying and selling in his country at that moment.

<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">How easy is it to get in and out?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">In some countries there are many competing apps; in others, very few.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">How much does each conversion cost?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Two conversions mean two spreads.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">Is it allowed?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Rules on crypto vary enormously between countries, and they keep changing.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">Who checks your identity?</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">The same anti-money-laundering rules that slow down banks also apply to the ramps.</div>
  </div>
</div>

> Stablecoins don't remove the old financial system — they connect to it
> at both ends. Where those connections are cheap and fast, stablecoins
> are hard to beat. Where they're slow, expensive, or restricted, the
> advantage shrinks quickly.

## Side by Side

<div style="overflow-x:auto;margin:1.75em 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.92rem;">
<thead>
<tr>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:10px 0 0 0;">&#160;</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;">Instant transfer, euro area</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;">International bank transfer</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:0 10px 0 0;">Stablecoin payment</th>
</tr>
</thead>
<tbody>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Speed</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Seconds</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">1–5 business days</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Seconds to minutes on-chain; ramps add time</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Opening hours</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">24/7</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Banking hours, no weekends</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">24/7</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Cost</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Usually free for individuals</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Fees plus an FX margin, often several %</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Network fee is cents; ramp fees and spreads add up</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Fee transparency</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Clear upfront</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Often unknown until it arrives</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Network fee is clear; ramp costs vary</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Currency received</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Euros</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Local currency</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Dollars, which the recipient can keep</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">If something goes wrong</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Limited recall, but a regulated bank on each side</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Recall possible, but slow</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Usually irreversible</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Privacy</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Private between banks</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Private between banks</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Visible on a public blockchain, under pseudonymous addresses</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;border-radius:0 0 0 10px;">Who you trust</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Your bank and the recipient's</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">Every bank in the chain</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;border-radius:0 0 10px 0;">The stablecoin issuer and the two ramps</td>
</tr>
</tbody>
</table>
</div>

## Where Stablecoins Already Win — And Where They Don't

It's easy to read headlines about stablecoins moving trillions of
dollars and assume they're replacing banks. The reality is more
interesting. Most of that volume is crypto trading. When McKinsey and
Artemis filtered for real payments — money actually moving between
people and businesses — they found around $390 billion in 2025. That's
more than double the year before, but still only about 0.02% of all
payments in the world.

<figure style="margin:2em 0;">
<img src="/images/mckinsey_report.png" alt="McKinsey chart: annualized stablecoin payment volumes by category, $390 billion total, B2B at $226 billion" style="width:100%;border-radius:12px;border:1px solid #E7E8EC;" />
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">B2B alone accounts for more than half of real stablecoin payment volume — and still only 0.01% market penetration.</figcaption>
</figure>

So stablecoins aren't replacing the system. They're winning in specific
places where the old system works badly.

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.25rem;margin:1.75em 0;">
<div>
<div style="font-weight:700;color:#1E3A8A;margin-bottom:0.6rem;">Where they win</div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Holding dollars where the local currency is weak.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Carlitos's case. In Argentina, Nigeria and elsewhere, a stablecoin is mainly a way to save in dollars without a US bank account.</span></div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Businesses paying across borders.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">B2B payments: about $226B, ~60% of real stablecoin volume, up more than 7x in a year.</span></div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Salaries and remittances in cheap corridors.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Where the ramps on both ends are cheap, workers get paid faster and for less.</span></div>
<div style="background:#EEF2FC;border-radius:12px;padding:0.9rem 1rem;"><strong style="color:#111318;">Spending with a card.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Card-linked spending hides the off-ramp entirely — the shop gets normal money, you never think about converting.</span></div>
</div>
<div>
<div style="font-weight:700;color:#5B5F6B;margin-bottom:0.6rem;">Where they don't, yet</div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">Everyday payments where local systems already work.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">In Europe, instant transfers and cards are fast, cheap and familiar. Your coffee in Lisbon doesn't need a blockchain.</span></div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;margin-bottom:0.6rem;"><strong style="color:#111318;">When you need protection.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">Cards let you dispute a payment. A stablecoin sent to the wrong address is usually gone.</span></div>
<div style="background:#FFFFFF;border:1px solid #D4D6DC;border-radius:12px;padding:0.9rem 1rem;"><strong style="color:#111318;">Where the ramps are weak or the rules are unclear.</strong><br/><span style="font-size:0.9rem;color:#5B5F6B;">The advantage only exists if getting in and out is easy and legal.</span></div>
</div>
</div>

## Back to Bairro Alto

The €10 for drinks and the €500 for Carlitos look like the same kind of
payment. They aren't.

Stablecoins don't replace either road. They build a new one between
them — fast, open around the clock, and cheap in the middle, but only as
good as the on-ramps and off-ramps at each end. That's where the real
competition is. Whoever makes getting in and out of stablecoins simple,
cheap and legal will decide how far this new road actually goes.

> The technology in the middle is largely solved. The hard and
> interesting problem is the edges — regulation, where digital dollars
> meet real people, real banks and real rules.

That's also why payments is one of the parts of this space I find most
exciting. One company has built its business precisely at that edge.
Instead of asking users to convert stablecoins back into local money, it
lets them spend them directly with a card, wherever card networks are
accepted. In my next post, I'll take a closer look at RedotPay: how it
works, how it makes money, and what could stand in its way.
