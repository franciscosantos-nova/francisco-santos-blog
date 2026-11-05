---
title: "How RedotPay Turned Stablecoins Into a Visa Card"
date: 2026-11-05
excerpt: "A tap at a restaurant in Buenos Aires, a few seconds of USDC moving somewhere in the background, pesos in the register. Nobody at the table thinks about blockchains. Here's how RedotPay turned the hardest problem in stablecoins — getting out — into something as simple as a card."
tags: ["stablecoins", "payments", "fintech", "crypto"]
cover: "/images/redotpay-cover.svg"
slug: "redotpay-turning-stablecoins-into-a-visa-card"
---

A few weeks ago, I sent Carlitos the €500 I owed him, in USDC. It landed
in his wallet in Buenos Aires in seconds. But what does Carlitos
actually do with digital dollars? His landlord wants pesos. So does the
restaurant on the corner.

The usual answer is the off-ramp: sell the stablecoins on an exchange,
wait for the pesos to reach his bank account, pay the fees, then spend.
Carlitos skips all of that.

On Friday night he takes his girlfriend to dinner in San Isidro. When
the bill arrives, he taps a Visa card on the terminal. The restaurant
receives pesos, and the waiter has no idea that, a second earlier, a
small amount of USDC left an app on Carlitos's phone and was converted
on the spot. Nobody at the table thinks about blockchains, exchanges or
off-ramps. It's just food.

The card in his hand belongs to RedotPay, a Hong Kong company that did
not exist before 2023. Today, it reportedly serves more than 9 million
customers and is weighing a stock market listing in the US at a
valuation of up to $5 billion. Its business is built on one simple
idea: removing the off-ramp, and making the exit from stablecoins
disappear.

In this post, I want to look at how that trick works, and who pays for
it.

## Who Is RedotPay?

RedotPay was founded in Hong Kong in 2023 by Michael Gao, its CEO, and
Jonathan Chan. It started with one product: a Visa card you could top
up with crypto, available as a virtual card for Apple Pay and Google
Pay, or as a physical card for shops and ATMs.

Nowadays, it looks a lot more like a financial super-app built around
that card. Inside the same app, users can:

- Hold stablecoins and crypto in a wallet
- Swap between them
- Trade with other users on a P2P marketplace
- Send money to local bank accounts through domestic payment systems,
  like PIX in Brazil or SEPA in Europe
- Earn a return on their stablecoins, borrow against their crypto, or
  pay a monthly subscription for perks like cashback

More recently, it has started serving businesses too, with a product
that lets companies accept stablecoins and receive traditional
currencies.

The growth has been fast. In 2025, RedotPay raised $194 million across
three rounds:

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-size:1.6rem;font-weight:700;color:#1E3A8A;">$40M</div>
    <div style="font-size:0.85rem;color:#5B5F6B;margin-top:0.3rem;">Series A, led by Lightspeed</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-size:1.6rem;font-weight:700;color:#1E3A8A;">$47M</div>
    <div style="font-size:0.85rem;color:#5B5F6B;margin-top:0.3rem;">Strategic round with Coinbase Ventures and Galaxy Ventures — unicorn status</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-size:1.6rem;font-weight:700;color:#1E3A8A;">$107M</div>
    <div style="font-size:0.85rem;color:#5B5F6B;margin-top:0.3rem;">Series B, led by Goodwater Capital, with Pantera, Blockchain Capital and Circle Ventures</div>
  </div>
</div>

By October 2026, according to Bloomberg, it had more than 9 million
customers, around 280 employees, annualised revenue above $180 million,
and an operating margin above 50%.

Who are those customers? Mostly people in emerging markets across Latin
America, Africa, the Middle East and Asia — places where holding
dollars is hard, local currencies are volatile, and international cards
are not always easy to get.

## How the Trick Works

Let's go back to the restaurant. The dinner costs the equivalent of
$100 in pesos, and Carlitos taps his card. What happens next takes
about a second, but involves at least five parties.

One detail first: RedotPay is not a Visa member. Only licensed
institutions can issue Visa cards, so RedotPay works with a partner
that lends it access to the network — a so-called BIN sponsor. It
issues the card under its own license, while RedotPay is just the
"program manager."

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Payment flow: Carlitos pays, RedotPay checks and converts, the issuer and Visa route it, the acquirer forwards it, the restaurant receives pesos">
<g font-family="Inter, sans-serif">
<rect x="10" y="30" width="170" height="110" rx="14" fill="#EEF2FC"/>
<text x="95" y="78" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Carlitos</text>
<text x="95" y="99" text-anchor="middle" font-size="12.5" fill="#5B5F6B">taps the card</text>
<path d="M186 85 H228" stroke="#9094A0" stroke-width="2.5"/>
<path d="M228 85 L214 77 M228 85 L214 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="236" y="30" width="190" height="110" rx="14" fill="#1E3A8A"/>
<text x="331" y="70" text-anchor="middle" font-size="15" font-weight="600" fill="#FFFFFF">RedotPay</text>
<text x="331" y="91" text-anchor="middle" font-size="12.5" fill="#DCE4F7">checks balance,</text>
<text x="331" y="109" text-anchor="middle" font-size="12.5" fill="#DCE4F7">sells USDC for $</text>
<path d="M434 85 H476" stroke="#9094A0" stroke-width="2.5"/>
<path d="M476 85 L462 77 M476 85 L462 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="484" y="30" width="200" height="110" rx="14" fill="#EEF2FC"/>
<text x="584" y="70" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Issuer + Visa</text>
<text x="584" y="91" text-anchor="middle" font-size="12.5" fill="#5B5F6B">approves, routes</text>
<text x="584" y="109" text-anchor="middle" font-size="12.5" fill="#5B5F6B">the payment</text>
<path d="M690 85 H732" stroke="#9094A0" stroke-width="2.5"/>
<path d="M732 85 L718 77 M732 85 L718 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="740" y="30" width="170" height="110" rx="14" fill="#EEF2FC"/>
<text x="825" y="78" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Acquirer</text>
<text x="825" y="99" text-anchor="middle" font-size="12.5" fill="#5B5F6B">merchant's bank</text>
<path d="M916 85 H958" stroke="#9094A0" stroke-width="2.5"/>
<path d="M958 85 L944 77 M958 85 L944 93" stroke="#9094A0" stroke-width="2.5" fill="none"/>
<rect x="966" y="30" width="224" height="110" rx="14" fill="#EEF2FC"/>
<text x="1078" y="78" text-anchor="middle" font-size="15" font-weight="600" fill="#111318">Restaurant</text>
<text x="1078" y="99" text-anchor="middle" font-size="12.5" fill="#5B5F6B">receives pesos</text>
<text x="600" y="200" text-anchor="middle" font-size="15" fill="#5B5F6B">⏱ ~1 second to approve &#160;&#160;·&#160;&#160; 💱 USDC → USD happens behind the scenes &#160;&#160;·&#160;&#160; 🏦 settlement follows a day or two later</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">RedotPay plugs into Visa through a BIN-sponsoring issuer, and sells stablecoins for dollars the instant you tap.</figcaption>
</figure>

**Step 1: Authorisation (one second).** The restaurant's terminal sends
the payment request to its acquirer, the merchant's payment provider.
The acquirer passes it to Visa, and Visa routes it to the card issuer.
The issuer asks RedotPay whether the customer has enough funds, and
RedotPay checks Carlitos's balance, sets aside the USDC needed to cover
the bill plus its fees, and confirms. The terminal shows "approved."

**Step 2: Conversion (behind the scenes).** Visa doesn't settle in
stablecoins, so RedotPay sells the USDC it set aside for regular
dollars and keeps a pre-funded account with the issuer, which pays for
customers' purchases. That's where the off-ramp is hidden.

**Step 3: Settlement (usually a day or two later).** The issuer pays
Visa, Visa pays the acquirer, and the acquirer pays the restaurant in
pesos, minus its usual card fees.

It's the same logic for RedotPay's transfers. If Carlitos wants to send
money to a friend in São Paulo, he sends stablecoins inside the app,
RedotPay converts them into reais, and a local partner delivers them
through PIX. The friend receives reais in a normal bank account.

In both cases, RedotPay does not remove the old financial system. It
adds stablecoins into it, at the exact moment money needs to become
local currency.

## Who Pays for the Trick?

Let's put numbers on Carlitos's dinner. The bill is the equivalent of
$100 in pesos.

On Carlitos's side, RedotPay charges two fees: about 1% to convert his
stablecoins, and about 1.2% because the purchase is in a currency other
than the dollar. So Carlitos pays around 102.20 USDC for a $100 dinner.
RedotPay keeps the $2.20, and out of that it pays its own costs: the
card issuer, the network fees on its side, and the cost of converting
stablecoins into dollars.

On the restaurant's side, nothing unusual happens. Like with any card,
the restaurant pays its acquirer a fee, often somewhere around 1.5%,
split between the acquirer, Visa and the card issuer. The issuer's
share, called interchange, may partly flow back to RedotPay through its
agreement with the BIN sponsor — but that split isn't public.

<figure style="margin:2em 0;">
<svg viewBox="0 0 900 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Fee comparison on the same 100 dollar bill: Carlitos pays about 2.20 dollars in fees, 2.2 percent; the restaurant pays about 1.50 dollars, 1.5 percent">
<g font-family="Inter, sans-serif">
<text x="0" y="30" font-size="14" font-weight="600" fill="#111318">Carlitos pays (conversion + currency fee)</text>
<rect x="0" y="40" width="660" height="34" rx="6" fill="#1E3A8A"/>
<text x="675" y="63" font-size="15" font-weight="700" fill="#111318">$2.20 (2.2%)</text>
<text x="0" y="120" font-size="14" font-weight="600" fill="#111318">Restaurant pays (card acceptance fee)</text>
<rect x="0" y="130" width="450" height="34" rx="6" fill="#9094A0"/>
<text x="465" y="153" font-size="15" font-weight="700" fill="#111318">$1.50 (1.5%)</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">On the same $100 bill, Carlitos pays nearly 50% more in fees than the restaurant does — the price of never having to off-ramp himself.</figcaption>
</figure>

Put side by side, Carlitos pays more for this transaction than the
restaurant does. He isn't only paying for a card — he's paying for the
convenience of never having to sell his stablecoins himself.

The card conversion fee is probably RedotPay's main engine, but not the
only one:

<div style="overflow-x:auto;margin:1.75em 0;">
<table style="width:100%;border-collapse:collapse;font-size:0.92rem;">
<thead>
<tr>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:10px 0 0 0;">Revenue stream</th>
<th style="text-align:left;padding:0.75rem 1rem;background:#1E3A8A;color:#FFFFFF;border-radius:0 10px 0 0;">How it works</th>
</tr>
</thead>
<tbody>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Card conversion</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">~1% on every card payment, plus a currency fee on non-dollar purchases</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Card issuance</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">$10 for a virtual card, $100 for a physical one</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">ATM withdrawals</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">A percentage of the amount withdrawn</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Top-ups with a bank card</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">A fee for buying crypto with a regular card</td>
</tr>
<tr style="background:#EEF2FC;">
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;">Transfers to bank accounts</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;">An exchange spread, not published</td>
</tr>
<tr>
<td style="padding:0.65rem 1rem;font-weight:600;color:#111318;border-radius:0 0 0 10px;">Financial products</td>
<td style="padding:0.65rem 1rem;color:#5B5F6B;border-radius:0 0 10px 0;">Interest on credit, margin on Earn, the Pro subscription, fees from businesses using Connect</td>
</tr>
</tbody>
</table>
</div>

This mix can explain what Bloomberg reported: annualised revenue above
$180 million and an operating margin above 50%. It also explains the
valuation. At $5 billion, RedotPay would be worth around 28 times its
annualised revenue — investors are betting it can become a bank for
people traditional banks don't serve well.

## Why It Grew So Fast

A lot of companies launched crypto cards before RedotPay, but few grew
this quickly. Four things explain it.

<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:1rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It solved the last problem</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Holding dollars was already possible — spending them at the corner shop wasn't. Card-linked stablecoin spending was one of the fastest-growing uses of stablecoins in 2025, and RedotPay moved first on the exit, not the entry.</div>
  </div>
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It went where the need was greatest</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Instead of Europe or the US, RedotPay focused on markets like Nigeria, Brazil and Southeast Asia, where currencies are volatile and international cards are hard to get. There, a card like this is a basic financial tool people are willing to pay for.</div>
  </div>
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It grew through people, not just ads</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Invite codes are everywhere — blogs, YouTube videos, social media. There's also a network of local agents who sign up users on the ground.</div>
  </div>
  <div style="background:#EEF2FC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:700;color:#1E3A8A;margin-bottom:0.4rem;">It sold a business, not a token</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">RedotPay never launched its own token. Its revenue comes from fees on real activity, and it reportedly turned profitable — which made it easier to attract investors.</div>
  </div>
</div>

## What Could Go Wrong?

Unfortunately, the same things that made RedotPay grow fast also
created its biggest risks:

- **A legal fight with Binance.**
- **Regulations that differ country by country**, and keep changing.
- **Dependence on partners it does not control**, starting with its BIN
  sponsor.
- **Competition and pressure on fees**, as rivals copy the model.
- **Living up to a $5 billion valuation.**

None of these risks is unusual for a company growing this fast. But
together they show that RedotPay's hardest work may not be technical at
all. The technology already works — what will decide its future is
legal, regulatory and commercial.

## Final Thoughts

Technology is moving at an impressive pace, and the financial world has
to keep up. That's exactly what RedotPay is doing. It did not invent
stablecoins, and it did not build a new payment network. It took
digital dollars and the Visa network, and connected them where most
people get stuck: the moment money has to become local currency.

I'll be honest about why I chose to look at RedotPay so closely. A
month ago, I was supposed to spend next semester on exchange in Hong
Kong. It was my dream and my main goal; the plan fell through, but it
didn't change where I want to learn. Hong Kong's fintech ecosystem is
one of the biggest goals of my professional life. When I talked about
that with one of my mentors, Simão Cruz, founder and CEO of Lightshift
Capital, he told me to keep a close eye on RedotPay.

The more I studied it, the more I realised payments is one of the parts
of fintech I enjoy the most. RedotPay is one of the companies doing
that best, and one day I'd love to contribute there.

> People want to use money that works — and stablecoins are
> increasingly how that money moves.
