---
title: "The Anatomy of a Real-World Asset"
date: 2026-10-16
excerpt: "A graded Pokémon card sold for an estimated $250,000 and the buyer never touched it. Taking that trade apart reveals the same six-layer architecture behind BlackRock's $2 billion BUIDL fund."
tags: ["RWA", "tokenization", "NFT", "custody"]
cover: "/images/charizard.jpg"
slug: "the-anatomy-of-a-real-world-asset"
---

In 1999, a kid in a schoolyard somewhere opened a pack of Pokémon cards
and found a holographic Charizard. Twenty-five years later, a perfect
copy of that same card sold for an estimated $250,000. The buyer never
touched it.

The card sits in a Brink's vault. What the buyer received was a token on
a blockchain. If they ever want to hold the card, they can ask for it to
be shipped. Until then, they can sell it to anyone in the world in
seconds, and the card never leaves the vault.

This sounds like a gimmick. It is actually one of the cleanest examples
of how a Real World Asset is built. In this post, I'll take the Charizard
apart, layer by layer, and show that the same architecture sits behind a
$2 billion BlackRock fund.

<figure style="margin:2em 0;">
<svg viewBox="0 0 1200 620" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The six layers of a tokenized asset: Asset, Legal, Custody, Token, Data, Distribution">
<g font-family="Inter, sans-serif">
<rect x="40" y="10" width="1120" height="80" rx="14" fill="#EEF2FC"/>
<circle cx="100" cy="50" r="22" fill="#1E3A8A"/>
<text x="100" y="57" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">1</text>
<text x="145" y="46" font-size="20" font-weight="600" fill="#111318">Asset</text>
<text x="145" y="68" font-size="14" fill="#5B5F6B">Is it identifiable, verifiable, valued?</text>
<rect x="40" y="100" width="1120" height="80" rx="14" fill="#EEF2FC"/>
<circle cx="100" cy="140" r="22" fill="#1E3A8A"/>
<text x="100" y="147" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">2</text>
<text x="145" y="136" font-size="20" font-weight="600" fill="#111318">Legal</text>
<text x="145" y="158" font-size="14" fill="#5B5F6B">What does the token actually entitle you to?</text>
<rect x="40" y="190" width="1120" height="80" rx="14" fill="#EEF2FC"/>
<circle cx="100" cy="230" r="22" fill="#1E3A8A"/>
<text x="100" y="237" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">3</text>
<text x="145" y="226" font-size="20" font-weight="600" fill="#111318">Custody</text>
<text x="145" y="248" font-size="14" fill="#5B5F6B">Is the asset really there, and is it safe?</text>
<rect x="40" y="280" width="1120" height="80" rx="14" fill="#EEF2FC"/>
<circle cx="100" cy="320" r="22" fill="#1E3A8A"/>
<text x="100" y="327" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">4</text>
<text x="145" y="316" font-size="20" font-weight="600" fill="#111318">Token</text>
<text x="145" y="338" font-size="14" fill="#5B5F6B">The smart contract — unique or fungible, open or gated.</text>
<rect x="40" y="370" width="1120" height="80" rx="14" fill="#EEF2FC"/>
<circle cx="100" cy="410" r="22" fill="#1E3A8A"/>
<text x="100" y="417" text-anchor="middle" font-size="19" font-weight="700" fill="#FFFFFF">5</text>
<text x="145" y="406" font-size="20" font-weight="600" fill="#111318">Data</text>
<text x="145" y="428" font-size="14" fill="#5B5F6B">Who tells the chain what's true off-chain?</text>
<rect x="40" y="460" width="1120" height="80" rx="14" fill="#1E3A8A"/>
<circle cx="100" cy="500" r="22" fill="#FFFFFF"/>
<text x="100" y="507" text-anchor="middle" font-size="19" font-weight="700" fill="#1E3A8A">6</text>
<text x="145" y="496" font-size="20" font-weight="600" fill="#FFFFFF">Distribution</text>
<text x="145" y="518" font-size="14" fill="#DCE4F7">Where does the token live, and who can buy it?</text>
</g>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Six layers, one token. Every RWA is built the same way, from a trading card to a treasury fund.</figcaption>
</figure>

## Layer 1: The Asset

Every RWA starts with something real. But not everything real can be
tokenized easily. A good asset needs to be three things:

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">Identifiable</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">You know exactly which one it is.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">Verifiable</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Someone trusted confirms it is genuine.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.3rem;">Valued</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">People agree on what it is worth.</div>
  </div>
</div>

A Pokémon card on its own is none of these. There are countless
Charizards in the world, many in bad shape, some fake. That is why every
card on Courtyard is first sent to a grading company like PSA. The grader
checks that it is authentic, gives it a condition score from 1 to 10, and
seals it in a plastic case with a unique certification number. The
difference between a 9 and a 10 can be worth tens of thousands of
dollars.

Only then does the card become a good asset to tokenize: one specific,
verified card, with a grade the whole market recognises.

Government debt is the opposite extreme. Every US Treasury bill of the
same issue is identical, recorded electronically and valued every second
by the market. Nobody needs to inspect it under a lamp. That is a big
part of why Treasuries became the first RWA to scale.

## Layer 2: The Legal Layer

This is the layer nobody sees and everything depends on. The question it
answers is simple: if I hold the token, what exactly am I entitled to,
and who has to give it to me?

With Courtyard, the answer comes from the platform's own rules. As long
as you hold the NFT, Courtyard keeps the card in the vault for you. When
you want the card, you go through a redemption process on their website,
including identity checks, and the token is destroyed once the card is
shipped.

But there is a detail: you can not get the card just by interacting with
the smart contract.

> The code does not hand you the card, a company does.

Your right to the Charizard ultimately depends on Courtyard keeping its
promise, and on the law making it keep it.

I went to Courtyard's terms and conditions to see how strong that promise
really is. When you buy the NFT, you take over the seller's storage
contract with Courtyard, so the token is really a ticket that carries a
contract from one owner to the next. The cards are insured, but Courtyard
is only liable for losses caused by gross negligence, and its total
liability is capped at $100 or the fee it earned on the sale, whichever
is higher. And if the company goes bankrupt, you have three months to
claim your card back, paying the shipping yourself.

This is how every RWA works. The question is just how strong that promise
is. Holding a BUIDL token makes you an investor in a regulated fund, with
rights defined by securities law. Holding a Courtyard NFT means relying
on a contract with a private company. Both are tokens, both live on a
blockchain, but the legal layer underneath is very different.

<div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.25rem;margin:1.75em 0;font-size:0.9rem;color:#5B5F6B;">
<strong style="color:#1E3A8A;">Worth knowing — ERC-7578.</strong> There is an Ethereum standard proposal for physical asset NFTs, built around one idea: before trusting a token, its holder needs to know who legally owns the item behind it, under which terms and in which jurisdiction.
</div>

## Layer 3: Custody

A token is only as good as the thing behind it, and the thing has to be
somewhere. For Courtyard, that somewhere is a Brink's vault, the same
company that moves cash and gold for banks.

<figure style="margin:1.75em 0;">
  <img src="/images/logistic-shot.jpg" alt="A secure storage facility, rows of locked vault units down a corridor" style="width:100%;border-radius:12px;" />
  <figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Every token on the blockchain is only worth as much as the lock on the other end.</figcaption>
</figure>

Custody answers a simple question: is the asset really there, and is it
safe? The card has to be stored properly, insured, and kept separate, so
that every token on the blockchain matches exactly one card in the vault.
That 1:1 link is the whole promise.

> If there were more tokens than cards, or a card went missing, the token
> would become a claim on nothing.

There is an important point here. You do not have a relationship with
Brink's. Courtyard does, and according to its terms, Courtyard holds the
cards on behalf of whoever owns each token, and it is Courtyard you
depend on if something goes wrong.

BUIDL follows the same logic at a much bigger scale. The fund's cash and
Treasuries are not held by BlackRock itself but by a separate custodian
bank, BNY. Different asset, same architecture: a trusted third party
holds the real thing, and the token points to it.

## Layer 4: The Token

This is the part we usually mean when we say "tokenization": the smart
contract on the blockchain. But two tokens can look the same at a glance
and behave very differently.

Each Courtyard card is an NFT on Polygon, a network built on top of
Ethereum. NFT stands for Non-Fungible Token: every token is unique,
because every card is unique. A number 10 Charizard is not interchangeable
with a number 9. BUIDL is the opposite: every token is identical, like
shares of the same fund, so it uses a fungible token, where one unit is
worth exactly the same as another.

<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.4rem;">Courtyard NFT</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Unique, non-fungible. Transferable to any wallet. Identity checks only at redemption.</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;">
    <div style="font-weight:600;color:#1E3A8A;margin-bottom:0.4rem;">BUIDL token</div>
    <div style="font-size:0.9rem;color:#5B5F6B;">Fungible, like a share. Transfers blocked by the contract unless the wallet is pre-approved.</div>
  </div>
</div>

The bigger difference is where the rules are. A Courtyard NFT can be sent
to any wallet in the world. Identity checks only happen at the end, when
someone wants the physical card. BUIDL does the opposite: only
pre-approved, verified investors can hold or receive the token, and the
smart contract itself blocks any transfer to a wallet that is not on the
list. One has compliance at the exit, the other builds it into the
token.

Also, there is one more thing people rarely notice. Tokens are not as
untouchable as crypto marketing suggests. Courtyard's terms allow it to
upgrade its smart contracts and even repossess NFTs it considers
abandoned or obtained in breach of its rules. Regulated tokens usually go
further, letting the issuer freeze or reverse transfers when the law
requires it. In the real world, someone always holds the keys.

## Layer 5: Data

A blockchain is very good at one thing: keeping a perfect record of who
holds which token. However, it is blind to everything outside it. It has
no idea whether the Charizard is still in the vault, whether it is really
a number 10 card, or what it is worth today. Someone has to bring that
information in. In crypto, this is known as the oracle problem.

For a tokenized card, three pieces of information matter:

<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0.9rem;margin:1.75em 0;">
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;text-align:center;">
    <div style="font-weight:600;color:#1E3A8A;">Is it genuine?</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;text-align:center;">
    <div style="font-weight:600;color:#1E3A8A;">Is it still there?</div>
  </div>
  <div style="background:#EEF2FC;border:1px solid #E7E8EC;border-radius:12px;padding:1rem 1.1rem;text-align:center;">
    <div style="font-weight:600;color:#1E3A8A;">What is it worth?</div>
  </div>
</div>

If we look at BUIDL, the value of a fund holding short-term government
debt is calculated every day by a fund administrator, under strict
rules, and audited. Also, in the tokenization world, specialised oracle
networks like Chainlink publish "proof of reserve" data on-chain, so
that a smart contract can check the assets backing a token actually
exist.

So, the lesson is simple. The token is only as trustworthy as the data
feeding it. The blockchain can tell you, with perfect certainty, that you
own token #67. It cannot tell you, on its own, what token #67 is really
worth.

I'll discuss the oracle problem in more detail in another post.

## Layer 6: Distribution

The first five layers make the token exist. This one makes it useful. It
answers the question: where does the token live, and who can buy it?

Firstly, tokenizing an asset does not automatically make it liquid. A
token makes it possible to trade quickly, but it does not create buyers.
Plenty of tokenized assets, from buildings to artworks, sit in wallets
with nobody bidding for them.

Looking at BUIDL again: it isn't trying to reach millions of
"collectors" — only verified, qualified investors can buy it, and much
of its use comes from institutions and crypto firms that need a safe
place to park cash on-chain.

Courtyard, on the other hand, is designed for collectors, not crypto
experts. Every user gets a digital wallet created automatically when they
sign up, so most never deal with blockchain. You can pay by card or in
USDC, open digital packs that reveal a random card, sell it, or move it
to another NFT marketplace.

<figure style="margin:1.75em 0;max-width:320px;margin-left:auto;margin-right:auto;">
  <img src="/images/packopening.webp" alt="A Courtyard digital pack, ready to be opened to reveal a random graded card" style="width:100%;border-radius:12px;" />
  <figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">No wallet, no seed phrase — just a pack to open.</figcaption>
</figure>

<figure style="margin:1.75em 0;">
<svg viewBox="0 0 600 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Courtyard daily trades: about 10,000 in late 2025, more than 50,000 in 2026">
<line x1="170" y1="20" x2="170" y2="170" stroke="#E7E8EC" stroke-width="1"/>
<path d="M170,30 H260 Q264,30 264,34 V48 Q264,52 260,52 H170 Z" fill="#9094A0"/>
<text x="160" y="45" text-anchor="end" font-family="Inter, sans-serif" font-size="13" font-weight="500" fill="#5B5F6B">Late 2025</text>
<text x="274" y="45" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#111318">~10,000 trades/day</text>
<path d="M170,100 H460 Q464,100 464,104 V118 Q464,122 460,122 H170 Z" fill="#1E3A8A"/>
<text x="160" y="115" text-anchor="end" font-family="Inter, sans-serif" font-size="13" font-weight="500" fill="#5B5F6B">2026</text>
<text x="474" y="115" font-family="Inter, sans-serif" font-size="13" font-weight="600" fill="#111318">50,000+ trades/day</text>
</svg>
<figcaption style="text-align:center;font-size:0.8rem;color:#9094A0;margin-top:0.5rem;">Illustrative, based on figures reported by Courtyard.</figcaption>
</figure>

And, of course, it clearly works. Courtyard went from around 10,000
trades a day in late 2025 to more than 50,000 in 2026. A simple card can
now change hands in seconds.

In conclusion, distribution can only be as strong as the trust built by
the five layers below it.

## Back to the Schoolyard

The kid who opened that Charizard in 1999 held everything in one hand.
The card, the proof it was real, and the right to sell it. Tokenization
just splits those things apart and spreads them across six layers.

> A token is only as strong as its weakest layer. A perfect smart
> contract means little if the legal promise behind it is weak, or
> nobody can verify the asset is still in the vault.

Side by side, the two assets this post keeps coming back to look like
this:

<div style="overflow-x:auto;margin:1.75em 0;border:1px solid #E7E8EC;border-radius:12px;">
<table style="width:100%;border-collapse:collapse;font-size:0.875rem;min-width:560px;">
<thead>
<tr style="background:#EEF2FC;">
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Layer</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">Charizard (Courtyard)</th>
<th style="text-align:left;padding:0.7rem 1rem;color:#1E3A8A;font-weight:600;white-space:nowrap;">BUIDL (BlackRock)</th>
</tr>
</thead>
<tbody>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Asset</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Graded Pokémon card</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Cash &amp; US Treasuries</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Legal</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Storage contract with a private company</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Shares in a regulated fund</td></tr>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Custody</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Brink's vault</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Custodian bank</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Token</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Unique NFT, transferable to anyone</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Fungible token, verified investors only</td></tr>
<tr style="background:#FFFFFF;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Data</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Grader certificate; value set by Courtyard</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Daily fund valuation, audited</td></tr>
<tr style="background:#FAFAFA;"><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#111318;font-weight:500;white-space:nowrap;">Distribution</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Mass-market collectibles app</td><td style="padding:0.65rem 1rem;border-top:1px solid #E7E8EC;color:#5B5F6B;">Institutions and crypto firms</td></tr>
</tbody>
</table>
</div>

That is what makes RWAs powerful, and also what makes them fragile.
Whether it's a $250,000 card or a $2 billion fund, the architecture
holding it up is exactly the same six layers.
