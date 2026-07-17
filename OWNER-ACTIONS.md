# City Play Co. — Owner actions

The website changes that can be completed in code are in place. The items below require access to external accounts, business-policy approval, or a real payment/email identity.

## 1. Finish the ticket and payment setup

1. Complete approval and payout setup in TicketSpice or the chosen ticketing platform.
2. Create these products:
   - Early Ticket — $29 per person, limited to the first 10 paid seats;
   - Solo Ticket — $39, one seat; and
   - Pair Ticket — $69, exactly two seats.
3. Set the total event capacity to 25 people. Confirm that every Pair Ticket reduces inventory by two.
4. Decide the price transition so the $69 Pair Ticket is not presented as a better choice while two $29 Early Tickets are still available.
5. Collect both attendee names and emails for a pair, plus accessibility needs, team requests, operational phone number, and marketing consent as a separate optional field.
6. Configure confirmation, reminder, cancellation, refund, waitlist, sold-out, and post-event messages.
7. Complete a real or test-mode purchase on a phone and desktop. Verify confirmation, attendee export, inventory count, and a refund.
8. Provide or insert the final checkout URL for each ticket. Then:
   - replace the three temporary Google Form URLs in `index.html`;
   - remove the Google Form/Venmo explanation;
   - update the three JSON-LD `Offer.url` values and their live availability; and
   - add completed-purchase tracking from the ticket platform.

## 2. Fix consent in the temporary Google Form

The current required checkbox combines event terms, safety, refund policy, and photography permission. Separate them before sending more traffic.

Use this required checkbox:

> I have read and agree to the City Play Co. event terms, walking expectations, safety rules, and refund policy: https://cityplayco.com/event-terms.html

Use this separate optional checkbox:

> City Play Co. may use photos or video that include me to promote future events. I understand I can decline and still attend.

Add this privacy link near the email and phone fields:

> Privacy: https://cityplayco.com/privacy.html

## 3. Approve the public policies

Review `event-terms.html` and `privacy.html` for business and legal accuracy. In particular, confirm:

- the refund and weather policy;
- the July 29 go/no-go date;
- the photography opt-out/consent approach;
- the event-data retention period;
- the listed service providers; and
- the contact email and Community Play Tools, LLC identity.

Have qualified counsel review the policies if you need legal assurance.

## 4. Finish MailerLite deliverability and test a real signup

The supplied MailerLite form is connected in the site. In MailerLite:

1. Verify the sending domain and From address.
2. Confirm whether the form uses single or double opt-in.
3. Add the welcome/confirmation email and make sure it promises only the frequency and content you intend to send.
4. Confirm the unsubscribe footer and business address are present.
5. Subscribe with an email address you control from the production site. Confirm the success state, subscriber record, confirmation/welcome email, and unsubscribe flow.
6. Delete any test subscriber after verification if it should not remain on the list.

## 5. Finish search-account setup

1. In Google Search Console, verify the `cityplayco.com` domain property.
2. Submit `https://cityplayco.com/sitemap.xml`.
3. Inspect and request indexing for `https://cityplayco.com/`.
4. Decide whether to allow `Google-Extended` in Cloudflare’s crawler controls. Keeping it blocked does not block normal Google Search, but it limits use for Gemini training and grounding.

## 6. Publish matching event facts elsewhere

Use the same event name, date, time, venue, address, prices, age limit, capacity, and official URL on:

- Instagram;
- the final ticketing platform;
- Voodoo Brewing Co.’s event listings or social channels; and
- relevant St. Petersburg event calendars.

Prepare the next-event or waitlist offer before Case No. 001 ends.
