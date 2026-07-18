# City Play Co.

Launch site for **City Play Co.** and the first St. Pete Detective Club event.

## Current launch

The repository root is the temporary sales page for:

> City Play Co. presents St. Pete Detective Club — Case No. 001

The site is intentionally static: HTML pages, local image/SVG assets, Google Fonts, a TicketSpice checkout handoff, MailerLite email signup, and lightweight event analytics.

## Brand assets

- `assets/city-play-co-mark.svg` — primary square vector mark;
- `assets/city-play-co-wordmark.svg` — horizontal website wordmark;
- `assets/city-play-co-profile.png` — 1080 × 1080 Instagram/profile export;
- `assets/social-card.svg` — editable event-sharing artwork; and
- `assets/social-card.png` — 1200 × 630 sharing export used by page metadata.

The mark is intentionally flat and geometric so it remains recognizable at small sizes: a city skyline, a magnifying glass, and a red game pawn.

## Preview locally

Serve the repository over HTTP, then open the local address in a browser:

```powershell
python -m http.server 8000
```

## TicketSpice checkout

The Early, Solo, and Pair ticket buttons open the hosted TicketSpice event page at `https://cityplayco.ticketspice.com/city-play-co-presents-st-pete-detective-club`. The same destination is used in the page’s Event structured data.

Each button keeps its ticket-tier and price attributes for outbound-click analytics. If the hosted event URL changes, update all three ticket anchors and the three JSON-LD `Offer.url` values together.

## Mailing list

The homepage signup form is connected to MailerLite form `193256915046761884` for account `2516137`. The form keeps a direct MailerLite action as a no-JavaScript fallback and loads MailerLite’s webform script for the inline success state.

MailerLite account actions—sending-domain verification, opt-in choice, welcome email, and a real subscriber test—are tracked in `OWNER-ACTIONS.md`.

## Deployment

The public site deploys from the `main` branch. The canonical hostname is `https://cityplayco.com/`; plain HTTP and `www` redirect to it.

After each release, verify the social card, ticket links, MailerLite form, Event structured data, `robots.txt`, and `sitemap.xml` in production.

## Owner actions

See `OWNER-ACTIONS.md` for the exact ticketing, consent, MailerLite, policy, Search Console, Cloudflare, and event-listing work that cannot be completed in source alone.

## Legal identity

City Play Co. is the public brand. The legal operator is **Community Play Tools, LLC**.
