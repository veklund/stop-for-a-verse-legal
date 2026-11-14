# Stop for a Verse – Privacy Policy and Terms of Use

> **Not legal advice.** These texts were drafted carefully from what the app actually does, but they have not been
> reviewed by a lawyer. Have them checked by a lawyer before relying on them, and again whenever the app starts
> handling data differently.

Published with GitHub Pages: https://veklund.github.io/stop-for-a-verse-legal/

- Privacy Policy: https://veklund.github.io/stop-for-a-verse-legal/privacy/
- Terms of Use (also the Premium subscription terms and the end-user licence): https://veklund.github.io/stop-for-a-verse-legal/terms/

## Before publishing

The texts describe the app as it will be when Premium ships. Do not make the repo public, or link the pages
from the stores, until all of these are true:

- [ ] A build has the paywall and the Settings Premium card with buttons named exactly “Restore purchases” and
      “Manage subscription”, and `termsUrl` / `privacyUrl` in `src/premiumConfig.ts` point at these pages.
- [ ] The RevenueCat account is opened under Activley Oy Ab, the API keys are in the app, and the RevenueCat DPA
      (with the EU Standard Contractual Clauses) is accepted. RevenueCat’s current subprocessors and hosting
      locations still match the Privacy Policy.
- [ ] Deleting a subscriber in RevenueCat has been tried in the sandbox, starting from what a user can give us
      (store, date, Google Play order number). Better still: show the RevenueCat customer ID in Settings or the
      problem report, and ask for it in the Privacy Policy.
- [ ] The retention periods in the Privacy Policy (RevenueCat records 24 months after a subscription ends, email
      12 months after the question is answered) are calendared and actually followed.
- [ ] Unused Android permissions are blocked in the app’s `app.json` (`android.blockedPermissions`:
      READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, SYSTEM_ALERT_WINDOW) and checked in a release manifest. Then
      the Privacy Policy sentence about unused permissions can be shortened.
- [x] Contact mailbox (2026-11-14): activley@proton.me (Proton AG, Switzerland), described as acting under its own
      terms. A Proton business plan with a data processing agreement would let the Privacy Policy name it as a processor.
- [x] Company telephone (2026-11-14): `PHONE` at the top of `build.py`, in both Contact sections and the home page.
      The page source holds it reversed (CSS shows it the right way round, a small script makes it a tel: link),
      so simple scrapers do not find it.
- [ ] Replace the app repo’s Expo MIT `LICENSE` with an all-rights-reserved notice for Activley Oy Ab, and add an
      open-source licences screen in the app (Feather icons, Expo and the other dependencies).
- [ ] The store privacy answers (Apple label: Purchases, App Functionality and Analytics, not linked, no
      tracking; Google Data safety: Purchase history) match the Privacy Policy.
- [ ] A lawyer has read both texts.

## Editing

All texts live in `build.py`. Edit them there, then run:

```
python3 build.py
```

This writes `index.html`, `privacy/index.html` and `terms/index.html`. Commit the generated pages together with
`build.py`; GitHub Pages serves them as they are (`.nojekyll` turns Jekyll off).

- Change `UPDATED` at the top of `build.py` whenever the meaning of a text changes.
- Prices, the company details and the contact address are constants at the top of `build.py`.
- Each section has an anchor id (for example `/terms/#premium`, `/privacy/#delete`) that can be linked to.
- Do not write that the app, or its free version, will always stay free.

## Design

Paper background and green text from the app (`DESIGN.md` in the app repo). Headings use Lora, served from
`assets/fonts` (SIL Open Font License, see `assets/fonts/OFL.txt`). The pages load nothing from other sites and
use no scripts or cookies.

© 2026 Activley Oy Ab
