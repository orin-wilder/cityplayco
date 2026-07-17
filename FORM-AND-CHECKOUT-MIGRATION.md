# Registration and checkout migration

## Temporary Google Form

Keep the Google Form/Venmo path active until TicketSpice approves the account. Align the live Form to the following public information:

- Organizer: **City Play Co.**
- Event series: **St. Pete Detective Club**
- Event: **Case No. 001 — The Sea-Vamp Syndicate**
- Date: **Friday, July 31, 2026**
- Optional pre-game arrival: **from 7 p.m. at Voodoo Brewing Co.**
- Briefing and game start: **8 p.m.**
- Reveal: **around 10 p.m.**
- Capacity: **25 paid attendees**
- Minimum to run: **12 paid attendees**
- First ten paid seats: **Early Ticket — $29 per person**
- Standard Solo Ticket: **$39**
- Standard Pair Ticket: **$69 for two people**

### Required Form text changes

1. Change every instance of “Detection Club” to “Detective Club.”
2. Replace “Founding Seat” with “Early Ticket.”
3. Replace “Founding Hunt” with “event” or “Case No. 001.”
4. Correct “Pre-hunt hang hangout” to “Optional pre-game hangout.”
5. Correct “submit this forum” to “submit this form.”
6. Change the acquisition question to “How did you hear about this event?”
7. Confirm the capacity is 25 and the minimum is 12 wherever those figures appear.
8. Preserve the warning that a Form submission does not reserve a seat; matched payment confirms it.

### Recommended opening copy

> City Play Co. presents St. Pete Detective Club: Case No. 001 — The Sea-Vamp Syndicate on Friday, July 31, 2026. Meet at Voodoo Brewing Co., 220 4th St N. The optional pre-game hangout opens at 7 p.m.; the briefing and game begin at 8 p.m.; the official reveal lands around 10 p.m. Expect approximately 1–1.5 miles of outdoor walking. This event is 21+. Food and drinks are purchased separately.
>
> Capacity is 25. The event requires at least 12 paid attendees. Tickets are nonrefundable unless the organizer cancels or postpones the event because of weather or insufficient sales.
>
> Submitting this form does not reserve a seat. Your ticket is confirmed only after your Venmo payment is received and matched to this registration.

## TicketSpice cutover

Before replacing the temporary checkout URLs:

- create Early, Solo, and Pair ticket types;
- cap the Early tier at ten paid seats;
- ensure Pair Tickets consume two seats;
- set total paid-seat capacity to 25;
- collect both attendee names and emails for Pair Tickets;
- carry accessibility, team-placement, photography, and marketing-consent fields forward;
- configure confirmation, reminder, cancellation, refund, and waitlist messages;
- export a test attendee record and verify its fields; and
- complete one low-value or test-mode purchase/refund cycle if the platform permits.

After validation, replace the three values in `EVENT_CONFIG.registrationUrls` and update the short checkout explanation below the ticket cards so it no longer mentions Google Form or Venmo.

Also replace the three ticket anchors’ direct `href` values, update the JSON-LD `Offer.url` and availability values, and add completed-purchase tracking from the ticket platform. Keep `OWNER-ACTIONS.md` current until the cutover is complete.
