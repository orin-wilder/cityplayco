# City Play Co.

Static waitlist site for St. Pete Detective Club, planned for early October in Downtown St. Pete. Date, venue, ticketing, and group arrangements are not finalized.

## Preview

From the parent workspace: `python -m http.server 8000 --directory cityplayco`, then open http://localhost:8000. Use HTTP rather than file URLs so the YouTube embed receives a referrer.

## Waitlist

The single MailerLite form sits in the hero. All waitlist links lead to it. Instagram appears beneath signup, in the success message, and in the footer. The mobile sticky button hides while signup is visible.

MailerLite account `2516137`, form `193256915046761884`, embed `43858234`. The success callback means form acceptance, not completed double opt-in. Verify double opt-in in MailerLite and complete a real signup/confirmation test with an authorized test address before publishing. No account settings were modified.

## Analytics

Project: [cityplayco-case001-prod](https://supabase.com/dashboard/project/fqgnfjmhxwtvxzvfjqhh).

Open **Table Editor → cityplayco_site_events**. The browser has insert-only access; use the signed-in dashboard for reports. Local previews do not send production analytics.

| Event | Meaning |
| --- | --- |
| `cityplayco_page_view` | Page load, including reloads |
| `cityplayco_mailing_list_cta_click` | Jump-to-signup click |
| `cityplayco_mailing_list_intent` | Form submission attempt |
| `cityplayco_mailing_list_success` | MailerLite success callback, not email confirmation |
| `cityplayco_instagram_click` | Outbound click, not a verified follow |

The placement column distinguishes header, hero, closing, mobile, footer, and signup_success. Records include a temporary per-tab session identifier, allowlisted UTM parameters, and referrer origin. No email address is sent to analytics. Tracking failures warn in the browser console without interrupting signup.

In **SQL Editor**, run:

```sql
select event, placement, count(*) as events,
       count(distinct session_id) as browser_sessions
from public.cityplayco_site_events
where created_at >= now() - interval '30 days'
group by event, placement
order by event, placement;
```

Sessions are not unique people. Direct form submissions need not include a CTA click. Confirmed subscriptions in MailerLite are the primary outcome.

Migration: `../cityplayco_case001/webapp/supabase/migrations/202609100001_cityplayco_site_analytics.sql`, applied September 10, 2026. No gameplay tables changed. Historical records are in `cityplayco_legacy_events`; see MIGRATION-NOTES.md.

## Publishing

Website edits remain local. Before deployment, verify MailerLite double opt-in, the teaser, social preview, and mobile signup. After deployment, verify page views and CTA clicks in the new table. The live page keeps its old configuration until deployed.

The old event-terms page is retained but unlinked from the homepage and privacy page. Replace its July details before linking it again when registration opens.

City Play Co. is a brand of Community Play Tools, LLC.
