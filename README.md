# City Play Co.

Launch site for **City Play Co.** and the first St. Pete Detective Club event.

## Current launch

The repository root is the temporary sales page for:

> City Play Co. presents St. Pete Detective Club — Case No. 001

The site is intentionally static: one HTML file, local image/SVG assets, Google Fonts, a temporary Google Form checkout handoff, and lightweight event analytics.

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

## Connect TicketSpice

In `index.html`, find `EVENT_CONFIG.registrationUrls` and replace the temporary Google Form URL for each ticket tier:

- `early`: first ten seats at $29;
- `solo`: one standard seat at $39; and
- `pair`: two standard seats at $69.

The three calls to action and analytics events already distinguish these tiers. If TicketSpice uses one event URL for all tiers, use that same URL for all three values.

## Connect the mailing list

Set `EVENT_CONFIG.mailingListEndpoint` to an HTTPS endpoint that accepts this JSON body:

```json
{
  "email": "player@example.com",
  "source": "cityplayco.com"
}
```

Until that value is configured, the form clearly tells visitors that email signup is being connected and directs them to `@cityplayco` on Instagram.

## Deployment

No deployment provider, workflow, custom-domain file, or auto-deploy configuration is included yet. The intended public domain is `cityplayco.com`.

When a provider is selected:

1. publish the repository root;
2. attach `cityplayco.com` and `www.cityplayco.com`;
3. choose one canonical hostname and redirect the other;
4. verify the social card at `/assets/social-card.png`; and
5. test every ticket tier and mailing-list submission in production.

## Legal identity

City Play Co. is the public brand. The legal operator is **Community Play Tools, LLC**.
