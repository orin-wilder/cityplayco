# Backup audit — September 10, 2026

Source: user-provided `Community Play Tools supabase_08-09-2026@17-20-05.backup.gz`.
Destination: `cityplayco-case001-prod` (`fqgnfjmhxwtvxzvfjqhh`).

## Migrated

All 10 rows from `public.speakeasy_events` were imported into private `public.cityplayco_legacy_events`, preserving original IDs, timestamps, event names, and other fields. Imports are idempotent by original ID. Eight are page_view and two are cta_hero, dated July 9–18, 2026. None contains an email address. This precursor-site history remains separate from the new funnel; event names do not establish current campaign attribution.

The old table accepted only page_view, cta_hero, email_signup, and buy_click. Newer cityplayco_* events would be rejected. The old project reported INACTIVE during this work.

New website analytics use cityplayco_site_events with constrained values and insert-only public access. A valid public insert returned 201; reads, deletes, and invalid event inserts were rejected. The labeled test record was removed.

## Other backup contents

- No auth users, storage buckets, storage objects, or vault secrets.
- No City Play Co. gameplay tables or public application functions.
- Unrelated data: Williams Park counts (37), sessions (5), surveys (6), one mashup idea, two sentiment responses and ten answers. No card-sort results or sentiment comments. These datasets were left in the backup.

The target already contains the case app gameplay tables. They were not overwritten or modified.

## Scope

This database audit does not establish the contents of MailerLite subscribers/settings, TicketSpice orders, deployed Edge Function code, hosting configuration, or external files. Keep the original backup. No old project was deleted, restored, or unpaused.

Website changes remain local. Verify MailerLite double opt-in and a real confirmation email before publishing.
