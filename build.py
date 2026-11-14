#!/usr/bin/env python3
"""Builds the static legal pages for Stop for a Verse from the texts below.

Pages: index.html (/), privacy/index.html (/privacy/), terms/index.html (/terms/).
Run: python3 build.py

Each document is a list of sections: (anchor id, heading, [blocks]). A block that starts with "<" is written
as it is (lists, notes); any other block becomes a paragraph. Blocks may contain simple HTML (<b>, <a>, <i>).
No scripts, no cookies, no third-party requests: the Lora font is served from assets/fonts.
"""
import html
import pathlib

UPDATED = "2026-11-14"
APP = "Stop for a Verse"
COMPANY = "Activley Oy Ab"
BID = "3348464-6"
ADDRESS = "Vinkelvägen 8, 68630 Jakobstad, Finland"
CONTACT = "activley@proton.me"
# Shown as +358 50 550 6502. Never written in the page source as plain digits: see phone().
PHONE = "+358505506502"
PHONE_SHOWN = "+358 50 550 6502"
PROTON_PRIVACY = "https://proton.me/legal/privacy"
SITE = "https://veklund.github.io/stop-for-a-verse-legal/"
PRICE_MONTH = "EUR 4.99"
PRICE_YEAR = "EUR 34.99"

MAIL = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'


def phone() -> str:
    """The phone number, kept away from simple scrapers: the source holds it reversed, CSS shows it the right way
    round (bidi override), and a small script turns it into a tap-to-call link. No plain digit run is in the page."""
    rev = PHONE_SHOWN[::-1]
    return f'<span class="ph" data-r="{PHONE[::-1]}">{rev}</span>'



def link(url: str, text: str) -> str:
    return f'<a href="{url}">{text}</a>'


def ul(*items: str) -> str:
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def note(text: str) -> str:
    return f'<div class="note">{text}</div>'


# Links to other parties' own policies and help pages.
APPLE_PRIVACY = "https://www.apple.com/legal/privacy/"
APPLE_STORE_PRIVACY = "https://www.apple.com/legal/privacy/data/en/app-store/"
APPLE_MEDIA_TERMS = "https://www.apple.com/legal/internet-services/itunes/"
APPLE_CANCEL = "https://support.apple.com/118428"
APPLE_REFUND = "https://reportaproblem.apple.com/"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"
GOOGLE_PAY_PRIVACY = "https://payments.google.com/payments/apis-secure/get_legal_document?ldo=0&ldt=privacynotice"
GOOGLE_PLAY_TERMS = "https://play.google.com/about/play-terms/"
GOOGLE_CANCEL = "https://support.google.com/googleplay/answer/7018481"
GOOGLE_REFUND = "https://support.google.com/googleplay/answer/2479637"
REVENUECAT_PRIVACY = "https://www.revenuecat.com/privacy/"
REVENUECAT_DPA = "https://www.revenuecat.com/dpa/"
BIBLEGATEWAY_PRIVACY = "https://www.biblegateway.com/legal/privacy/"
TIETOSUOJA = "https://tietosuoja.fi/en"
EDPB_MEMBERS = "https://www.edpb.europa.eu/about-edpb/about-edpb/members_en"
KULUTTAJARIITA = "https://www.kuluttajariita.fi/en/"
OFL = "https://openfontlicense.org/"


# --------------------------------------------------------------------------------------------------------------
# Privacy Policy
# --------------------------------------------------------------------------------------------------------------

PRIVACY_LEAD = (
    f"{APP} has no accounts and no ads, and the app contains no analytics, crash-reporting or tracking software. "
    "Your topics, reminder times, likes and notes are kept on your phone, and we do not receive them unless you "
    "choose to send them to us, for example in a problem report. The app itself sends something from your phone "
    "only in a few cases: when you open, buy, restore or manage Premium; if you have Premium, when it checks that "
    "your subscription is still active; when you open a whole chapter on Bible Gateway; when you email us; and "
    "when you share a verse. Your phone’s own backups can also include the app’s data. This page explains each "
    "of those in plain words."
)

PRIVACY = [
    ("who-we-are", "Who we are", [
        f"{APP} (“the app”) is published by {COMPANY} (Business ID {BID}), {ADDRESS}. We are the controller of "
        "the small amount of personal data described on this page.",
        f"If you have a question about your privacy, write to {MAIL}. A real person reads every message.",
    ]),
    ("on-your-phone", "What stays on your phone", [
        "To work, the app saves a few things in its own private storage on your phone. The app does not send this "
        "data to us or to anyone else, apart from the cases described under “What leaves your phone” below and "
        "your phone’s own backups, and we cannot see it:",
        ul(
            "the topics you chose and the order you chose them in;",
            "whether reminders are on, and the times you picked;",
            "the verses you liked;",
            "the notes you wrote on verses;",
            "whether “Learn from my likes” is on. When it is, the app suggests verses by looking at your likes, "
            "and that happens entirely on your phone;",
            "which verses have already been sent as reminders, so you are not sent the same one again too soon, "
            "and the date until which reminders are planned;",
            "small things such as whether you have finished setting up the app and which tips you have seen;",
            "if you buy Premium: your plan, whether it is active, when it renews or ends, and when it was last "
            "checked. The RevenueCat software in the app (see below) also keeps a copy of your subscription "
            "status and a random customer number on the phone.",
        ),
        "If the app ever finds its saved data damaged, it repairs it and keeps up to five copies of the earlier "
        "saved data on the phone, so nothing you wrote is lost. Because of this, such a copy can still hold the "
        "text of a note you later deleted. These copies stay on the phone, like the rest, and are removed when "
        "you uninstall the app or clear its storage.",
        "If you use the app in a web browser, the same information is kept in that browser’s local storage "
        "instead, and is removed when you clear the site’s data.",
    ]),
    ("reminders", "Reminders are made on your phone", [
        "Verse reminders are local notifications. The app plans them on your phone for the times you chose, up to "
        "two weeks ahead. They do not come from a server, and the app does not create or send a push token.",
        "The app asks for permission to show notifications when you turn reminders on, save your settings or send "
        "a test reminder. On Android, the app can also ask you to allow “Alarms & reminders”, so that reminders "
        "arrive exactly at your chosen times instead of up to an hour later; this is optional and lets the app set "
        "precise reminder times, nothing more. It does not use your camera, contacts, location or microphone, and "
        "it never reads your photos. On iPhone, if you choose to save a verse picture to your photos from the share "
        "sheet, iPhone asks once whether the app may add pictures to your photo library; this only adds the "
        "picture you chose and does not let the app see your other photos.",
        "A reminder shows the verse and its reference. Depending on your phone’s settings, it can be visible on "
        "the lock screen. You can change that in your phone’s notification settings.",
    ]),
    ("phone-backups", "Your phone’s own backups", [
        "Like most apps, the app’s data can be included in the backups your phone makes for you: Android backup "
        "to your Google account, iCloud Backup, or a backup to your computer. These backups belong to you and are "
        "handled by Google or Apple under the settings and terms of your own account. The app never uploads "
        "anything for backup itself, and we cannot see these backups.",
    ]),
    ("leaves-your-phone", "What leaves your phone, and when", [
        "Information leaves your phone only in the situations below.",
        "<h3>Downloading the app</h3>",
        "You get the app from the App Store or Google Play. Apple or Google handle your download, account and "
        "payment details under their own privacy policies. We receive reports from them about downloads and "
        "sales, such as numbers per country, which we use for our accounts. We do not use "
        "them to find out who you are.",
        "If your phone settings allow it, Apple and Google also share anonymous usage statistics and crash reports "
        "with us, such as how often the app is opened or where it stopped working. We use them to fix problems and "
        "improve the app. You can turn this sharing off in your phone’s privacy or Google Play settings.",
        "<h3>Premium purchases</h3>",
        "If you buy Premium, Apple or Google take the payment. We never see your card or bank details. The store "
        "confirms the purchase with a receipt (Apple) or a purchase token (Google), which the app passes to "
        "RevenueCat to check that your subscription is active.",
        f"RevenueCat, Inc. is a company in the United States that provides this subscription check for us. It "
        "acts on our behalf, as our data processor. The app gives RevenueCat no name, email address or other "
        "detail about you: RevenueCat creates a random customer number for your phone. It receives that number, "
        "the store receipt or purchase token, the time of your purchases and renewals, the type of device and "
        "its operating system, the version of the app and of RevenueCat’s software, your store country, language "
        "setting and currency, and, as with any internet connection, the IP address of your phone.",
        "RevenueCat also turns this data into subscription statistics for us, such as how many people subscribe, "
        "renew or cancel. We use them to run and improve Premium, not to find out who you are.",
        "The app contacts RevenueCat when you open Premium in the app (to show the current prices), when you buy, "
        "restore or manage a subscription, and afterwards while the app stays open. If Premium is saved on your "
        "phone, for example because you subscribed or a backup brought it back, the app also checks your "
        "subscription when it starts and each time you return to it. If you never open Premium or use “Restore "
        "purchases” or “Manage subscription”, the app does not contact RevenueCat.",
        "<h3>Reading a whole chapter on Bible Gateway</h3>",
        "In a verse’s context, “Read the full chapter” opens the chapter on Bible Gateway in your browser. The "
        "link contains only the book and chapter, for example John 14. Once the page opens, you are on Bible "
        "Gateway’s website, run by HarperCollins Christian Publishing in the United States. It uses cookies and "
        f"its own {link(BIBLEGATEWAY_PRIVACY, 'privacy notice')} applies. Nothing about you is passed to it by "
        "the app.",
        "<h3>Reporting a problem</h3>",
        f"In Settings, “Report a problem” opens your own email app with a message to {MAIL}. Nothing is sent "
        "until you press Send, and you can change or delete anything in the message first. To help us find the "
        "problem, the message includes, below a space for your own words:",
        ul(
            "a subject line with the app version and build, and your phone’s operating system and its version "
            "(for example “Android 15”), which are repeated in the message;",
            "whether reminders are on, off, or on but blocked in your phone’s settings;",
            "your reminder times, the date until which reminders are planned, and the topics you chose (or “all”);",
            "whether you have Premium, and its state (for example active or ended).",
        ),
        "It does not include your phone model, your likes, your notes, or any identifier. When you send it, we "
        "receive your email address, your name if your email app adds it, what you write, and anything you "
        "attach. Our mailbox is with Proton (Proton AG, Switzerland), so Proton stores these emails under its own "
        f"terms and {link(PROTON_PRIVACY, 'privacy policy')}. Switzerland is recognised by the EU as giving personal "
        "data adequate protection.",
        "<h3>Sharing a verse</h3>",
        "“Share text” and “Share image” open your phone’s own share menu with the verse, its reference and the "
        "app’s name, as text or as a picture. Your notes and likes are never included. The app sends nothing "
        "itself: the app or person you choose receives what you share, under their own terms. A picture is made "
        "as a temporary file on your phone and is removed afterwards.",
    ]),
    ("we-do-not", "What we do not do", [
        ul(
            "We have no user accounts and no sign-in.",
            "We show no ads and use no advertising ID.",
            "The app contains no analytics, crash-reporting or tracking software, and we do not track you across "
            "other apps or websites. The only statistics we see are the ones Apple, Google and RevenueCat provide, "
            "as described above.",
            "We do not sell your personal data or share it for advertising.",
            "We do not build a profile of you. Topic labels on verses are chosen by our editors, and “Learn from "
            "my likes” works only on your phone.",
            "We do not run our own server for the app. The Bible text and the explanations are part of the app, "
            "so reading them does not use the internet.",
        ),
        "On Android, the notification software the app is built with includes Google Firebase code that could be "
        "used for push messages. The app does not set it up, so it does not create a push token or send "
        "anything. The Android version also lists some standard permissions that come with its building blocks. "
        "It uses internet access (for Premium), notifications, and keeping reminders after the phone restarts. "
        "Others are listed but not used by the app, such as storage access on older Android versions and showing "
        "over other apps. The app uses no permission to collect information about you.",
    ]),
    ("legal-bases", "Why we use data, and our legal grounds", [
        "Data that stays on your phone is not collected by us. For the rest, the EU General Data Protection "
        "Regulation (GDPR) asks us to name a legal ground:",
        ul(
            "<b>Selling and checking Premium</b> (Apple or Google, and RevenueCat): to provide the subscription "
            "you asked for, which is performing our contract with you (GDPR Article 6(1)(b)).",
            "<b>Subscription statistics</b> (from RevenueCat and the stores: how many people subscribe, renew or "
            "cancel): our legitimate interest in running and improving Premium (Article 6(1)(f)).",
            "<b>Usage statistics and crash reports</b> from Apple and Google, if your phone settings allow them: "
            "our legitimate interest in fixing problems and improving the app (Article 6(1)(f)).",
            "<b>Answering your email:</b> our legitimate interest in helping you and fixing problems in the app "
            "(Article 6(1)(f)), or our contract with you when your question is about your subscription.",
            "<b>Accounting records</b> of sales, as reported to us by the stores: our legal duty under Finnish "
            "accounting law (Article 6(1)(c)).",
        ),
        "You never have to give us personal data. Without the store receipt or purchase token we cannot check "
        "Premium, and without your email address we cannot reply to you. Everything else in the app works "
        "without either.",
        "When you open Bible Gateway or share a verse, you send the information yourself, to a party you choose. "
        "That party decides how it uses it.",
        note("<b>Your right to object.</b> Where we rely on our legitimate interest (statistics, crash reports and "
             "answering your email), you can object at any time by writing to us, and we will stop unless we have "
             "compelling grounds to continue. You can also turn off the sharing of usage statistics and crash "
             "reports in your phone’s settings."),
    ]),
    ("recipients", "Who receives data", [
        ul(
            f"<b>Apple</b>, for downloads and purchases on iPhone, under the "
            f"{link(APPLE_STORE_PRIVACY, 'App Store privacy notice')} and {link(APPLE_PRIVACY, 'Apple’s privacy policy')}.",
            f"<b>Google</b>, for downloads and purchases on Android, under {link(GOOGLE_PRIVACY, 'Google’s privacy policy')} "
            f"and the {link(GOOGLE_PAY_PRIVACY, 'Google Payments privacy notice')}.",
            f"<b>Proton AG</b> (Switzerland), our email provider, when you email us, under its own terms and "
            f"{link(PROTON_PRIVACY, 'privacy policy')}.",
            f"<b>RevenueCat, Inc.</b>, our processor for the subscription check and subscription statistics, under "
            f"a data processing agreement. See {link(REVENUECAT_PRIVACY, 'RevenueCat’s privacy policy')}.",
            f"<b>Bible Gateway</b>, only if you open a chapter there, under its {link(BIBLEGATEWAY_PRIVACY, 'privacy notice')}.",
        ),
        "RevenueCat, the one company that handles data for us, is bound by contract to protect it at least as "
        "well as this policy describes. Apple and Google act under their own responsibility as stores and "
        "payment providers, and Proton as our email provider. We may also have to share information if the law requires it, for "
        "example with the tax authorities.",
    ]),
    ("transfers", "Data outside the EU", [
        f"RevenueCat stores data in the United States, on Amazon Web Services, and uses providers that are mainly "
        f"in the United States. Our agreement with RevenueCat includes the European Commission’s Standard "
        f"Contractual Clauses to protect data sent there ({link(REVENUECAT_DPA, 'RevenueCat’s data processing agreement')}).",
        "Apple and Google may process data in the United States and elsewhere, as described in their own "
        "policies. Emails you send us are kept by Proton in Switzerland, which the EU recognises as giving "
        "adequate protection. Bible Gateway is in the United States; you connect to it directly when you open a chapter.",
    ]),
    ("retention", "How long data is kept", [
        ul(
            "<b>On your phone:</b> until you delete it in the app, clear the app’s storage, or uninstall the app. "
            "If Premium ends, your likes, notes and topics stay saved.",
            "<b>Subscription records at RevenueCat:</b> while your subscription is active, and for up to 24 months "
            "after it ends, so we can answer questions about renewals and refunds. Then we delete them. You can ask "
            "us to delete them sooner.",
            "<b>Your emails to us:</b> for up to 12 months after your question has been answered, unless a "
            "subscription matter or a legal claim needs them for longer. You can ask us to delete them sooner.",
            "<b>Usage statistics and crash reports:</b> for as long as Apple or Google keep them available to us in "
            "their developer tools. They do not tell us who you are.",
            "<b>Sales records:</b> as long as the Finnish Accounting Act requires: 10 years for the accounts and "
            "6 years for the reports behind them, counted from the end of the financial year.",
        ),
    ]),
    ("delete", "How to delete your data", [
        "Because your data is on your phone, you can delete it yourself:",
        ul(
            "<b>A note:</b> open it and choose “Delete note”, or save it empty.",
            "<b>One liked verse:</b> tap the heart again, or double-tap it in Liked.",
            "<b>All likes:</b> in Settings, under For you, use the “Clear … liked verses” button. Your notes are kept.",
            "<b>Suggestions from your likes:</b> turn off “Learn from my likes”.",
            "<b>Reminders:</b> turn Reminders off and save. All planned reminders are cancelled.",
            "<b>Everything:</b> uninstall the app. On Android you can also go to the phone’s Settings, Apps, "
            f"{APP}, Storage, and choose Clear storage. This also removes the repair copies described above.",
        ),
        "Copies inside your own phone backups are managed in your Google or Apple account settings.",
        note("Deleting the app does not cancel a Premium subscription. Cancel it in the App Store or Google Play "
             "first (see the Terms of Use)."),
        f"To have your subscription records deleted at RevenueCat, email {MAIL}. Since we do not know your name, "
        "tell us which store you bought Premium in and roughly when, and include the order number from your "
        "receipt if you have it (on Google Play it starts with “GPA.”). If we cannot find your record from "
        "these details, we will tell you.",
    ]),
    ("rights", "Your rights", [
        "Under the GDPR you have the right to ask for access to your personal data, to have it corrected or "
        "deleted, to restrict or object to its use, and to receive it in a portable form. Most of your data is "
        "only on your phone, where you can see, change and delete it yourself. For anything we or RevenueCat "
        f"hold, write to {MAIL}. We answer within one month.",
        "Where we rely on our legitimate interest, you can object at any time, and we will stop unless we have "
        "compelling grounds to continue.",
        f"If you think we have handled your data wrongly, please tell us first so we can put it right. You can "
        f"also complain to the Finnish Data Protection Ombudsman ({link(TIETOSUOJA, 'tietosuoja.fi')}) or to "
        f"the {link(EDPB_MEMBERS, 'data protection authority')} where you live or work.",
    ]),
    ("children", "Children", [
        "The app is not directed at children under 13. Its content, Bible verses, suits every age, and families "
        "are welcome to use it together. We do not knowingly collect personal data from children. Beyond what "
        "this page describes, the app collects no personal data from anyone. Purchases by children are "
        "controlled by the parental settings of the App Store or Google Play.",
    ]),
    ("security", "Keeping data safe", [
        "Your data is kept in the app’s private storage, which other apps cannot read, and is protected by your "
        "phone’s own security. Notes are not encrypted separately, so we recommend a screen lock. Connections to "
        "the stores and to RevenueCat are encrypted.",
    ]),
    ("changes", "Changes to this policy", [
        "If the app starts handling data differently, we will update this page before the change takes effect "
        "and change the date at the top. If the change is important, we will also tell you in the app or in the "
        "store listing.",
    ]),
    ("contact", "Contact", [
        f"{COMPANY}, {ADDRESS}. Email: {MAIL}. Phone: {phone()}.",
    ]),
]


# --------------------------------------------------------------------------------------------------------------
# Terms of Use (also the subscription terms and end-user licence agreement)
# --------------------------------------------------------------------------------------------------------------

TERMS_LEAD = (
    f"These terms are the agreement between you and {COMPANY} for using {APP}. They are also the terms of the "
    "Premium subscription and the app’s end-user licence. We have tried to keep them short and clear. Nothing "
    "in them takes away the rights that consumer law gives you."
)

TERMS = [
    ("about", "About these terms", [
        f"{APP} (“the app”) is provided by {COMPANY} (Business ID {BID}), {ADDRESS} (“we”, “us”). By "
        "downloading or using the app, you accept these terms. If you do not accept them, please do not use the "
        "app.",
        f"How we handle personal data is explained in our {link('../privacy/', 'Privacy Policy')}.",
    ]),
    ("app", "The app and Premium", [
        "The app is free to download. Today, without paying, you can read a selection of verses, follow a "
        "limited number of topics at a time, and use reminders, likes, notes and sharing.",
        "Premium is an optional subscription. It opens every verse and every topic in the app, including verses "
        "we add while you are subscribed. Each subscription also helps us keep the app going and spread the "
        "Word.",
        "We may change what the free version and Premium include, as explained under “Changes to the app” below.",
    ]),
    ("premium", "Premium subscription", [
        "<h3>Price</h3>",
        f"Premium costs {PRICE_MONTH} a month or {PRICE_YEAR} a year, including VAT where it applies. The App "
        "Store or Google Play may show the price in your local currency, and the price shown when you confirm "
        "the purchase is the one that applies. There is no free trial: you are charged when you confirm the "
        "purchase.",
        "<h3>Automatic renewal</h3>",
        "The subscription renews automatically for the same period, and the store charges you again, until you "
        "cancel. On the App Store, cancel at least 24 hours before the current period ends, or it will renew "
        "for one more period. On Google Play, cancel before the renewal date.",
        "If we change the price, the store tells you before the new price applies, and you can cancel before "
        "then. Some stores ask for your consent to a higher price.",
        "<h3>How to cancel</h3>",
        ul(
            f"<b>iPhone:</b> open Settings, tap your name, then Subscriptions, and choose {APP}. "
            f"{link(APPLE_CANCEL, 'Apple’s help page')}.",
            f"<b>Android:</b> open Google Play, tap your profile picture, then Payments and subscriptions, "
            f"Subscriptions, and choose {APP}. {link(GOOGLE_CANCEL, 'Google’s help page')}.",
            "In the app you can also use “Manage subscription”, which opens the same place.",
        ),
        "Deleting the app does not cancel the subscription.",
        "<h3>Billing and refunds</h3>",
        f"Payments are taken and handled by Apple or Google under their own terms "
        f"({link(APPLE_MEDIA_TERMS, 'Apple Media Services Terms')}, {link(GOOGLE_PLAY_TERMS, 'Google Play Terms of Service')}). "
        f"Because we do not receive your payment details, refunds are requested from the store: "
        f"{link(APPLE_REFUND, 'Apple')} or {link(GOOGLE_REFUND, 'Google Play')}. If something has gone wrong, "
        f"you are also welcome to write to {MAIL} and we will help as far as we can.",
        "<h3>A new phone</h3>",
        "On a new phone, sign in to the same App Store or Google Play account and choose “Restore purchases” in "
        "the app. A subscription bought on the App Store works on iPhone, and one bought on Google Play works on "
        "Android.",
        "<h3>When Premium ends</h3>",
        "After you cancel, Premium continues until the end of the period you have paid for. Then the app returns "
        "to the free version. Nothing you made is deleted: your likes, notes and chosen topics stay saved on "
        "your phone. Verses and topics that need Premium are hidden, and once the app has checked your "
        "subscription, reminders come only from the free verses. Reminders that were already planned may still "
        "arrive until you next open the app. Everything comes back if you subscribe again.",
    ]),
    ("withdrawal", "Right of withdrawal in the EU", [
        "If you live in the EU or EEA, consumer law generally gives you 14 days to withdraw from a purchase made "
        "online. For digital content and services that start straight away, this right can end once the "
        "service has started, if you asked for it to start at once and confirmed that you understood this. "
        "Premium is bought through the App Store or Google Play. Apple and Google explain how withdrawal works "
        f"for purchases in their store in the {link(APPLE_MEDIA_TERMS, 'Apple Media Services Terms')} and the "
        f"{link(GOOGLE_PLAY_TERMS, 'Google Play Terms of Service')}. Nothing in these terms takes away a right "
        "you have under the law that applies to you.",
    ]),
    ("scripture", "The Bible text and the explanations", [
        "Every verse in the app is from the World English Bible (WEB), a modern English translation in the "
        "public domain. The text is taken word for word from the published edition; we leave out only the "
        "headings of the Psalms and a closing “Selah”. We never rewrite or paraphrase it.",
        "The short explanations in “In context” are brief summaries, written by us, of what named public-domain "
        "commentaries say about the verse, such as Matthew Henry’s Concise Commentary, Barnes’ Notes, the "
        "Cambridge Bible, Jamieson-Fausset-Brown, Ellicott’s Commentary and the Pulpit Commentary. The sources "
        "are named with each explanation. The topics a verse is filed under are also our own editorial choice.",
        "The explanations are a help for seeing a verse in its setting. They are not a replacement for reading "
        "the whole passage, for the teaching of your church, or for the counsel of a pastor. The app is also not "
        "medical, psychological or other professional advice. If you are in crisis, please contact someone you "
        "trust or your local emergency number.",
        "We take great care with the text and the explanations. If you find a mistake, please tell us at "
        f"{MAIL} so we can correct it.",
    ]),
    ("use", "Using the app well", [
        "You may use the app for your own personal, non-commercial use. Please do not:",
        ul(
            "copy, sell, rent or redistribute the app or its design;",
            "try to get around Premium, or reverse engineer or modify the app, except where the law allows it;",
            "use the app in a way that breaks the law or harms the app or other people.",
        ),
        "When you use the app, you also follow the terms of the services it works with, such as your app store, "
        "your email app and the apps you share to.",
        "You are welcome to share verses with anyone, as text or as the pictures the app makes for sharing.",
    ]),
    ("ip", "Who owns what", [
        f"The app’s design, code, name, explanations and topic choices belong to {COMPANY}. We give you "
        "a personal, non-exclusive, non-transferable licence to use the app on devices you own or control, under "
        "these terms and the rules of the store you got it from.",
        "The World English Bible text is in the public domain, and the commentaries the explanations draw on are "
        f"in the public domain too. The Lora typeface is © The Lora Project Authors and is used under the "
        f"{link(OFL, 'SIL Open Font License 1.1')}. Some icons and other open-source parts of the app are used "
        "under their own licences.",
        "Your notes are yours. They stay on your phone and we never see them. We cannot restore them if the "
        "phone is lost or the app is deleted without a backup.",
    ]),
    ("changes-app", "Changes to the app", [
        "We work to keep the app helpful and running well. We may update it, add or remove features, change what "
        "is included in the free version and in Premium, change prices, or stop offering the app. Some updates "
        "may be needed for the app to keep working.",
        "We change Premium only for a valid reason, such as a change in the law or in the stores’ rules, security "
        "or technical needs, keeping the app working on new versions of iOS and Android, a change in the rights "
        "to or the sources of the texts in the app, or improving the app and its content.",
        "If a change takes away a significant part of what you pay Premium for or otherwise makes Premium clearly "
        "worse for you, or if we stop offering Premium, we will tell you reasonably in advance: by email where we "
        "have your address, and otherwise in the app and in the store listing. You can then end Premium free of "
        "charge within 30 days of the notice or of the change, whichever is later, and you will get back what "
        "you paid for the time you can no longer use. Where the law gives you more, such as a lower price, you "
        "keep it.",
        "Reminders depend on your phone. Battery saving, Focus or Do Not Disturb modes, and notification settings "
        "can delay or hide them, and we cannot control that.",
    ]),
    ("liability", "Our responsibility", [
        "We provide the app with care, but we cannot promise that it will run without interruption or without errors.",
        "As far as the law allows, we are not responsible for indirect losses, such as lost data you had not "
        "backed up, and our total responsibility to you is limited to what you paid for Premium in the 12 months "
        "before the problem arose. We are not responsible for services run by others, such as the App Store, "
        "Google Play, Bible Gateway or the apps you share with.",
        "None of this limits our responsibility where the law does not allow it to be limited, for example for "
        "intent or gross negligence, or for personal injury. It also does not limit your rights as a consumer, "
        "including your rights when the app or Premium does not work as promised. You have the legal guarantee "
        "of conformity for digital content under consumer law (in Finland, chapter 5a of the Consumer Protection "
        "Act).",
    ]),
    ("ending", "Ending the agreement", [
        "You can stop using the app at any time by deleting it. If you have Premium, cancel it in the store as "
        "well. We may end your licence if you seriously break these terms.",
    ]),
    ("apple", "If you got the app from the App Store", [
        "These terms are between you and us, not Apple. Apple is not responsible for the app or its content, and "
        "has no duty to provide maintenance or support for it. If the app does not work as promised, you may "
        "tell Apple, and Apple may refund the price you paid for it; beyond that, as far as the law allows, Apple "
        "has no other warranty obligation for the app. We, not Apple, are responsible for handling any claims "
        "about the app, including product liability claims, claims that it does not meet legal or regulatory "
        "requirements, consumer protection claims, and claims that it infringes someone else’s rights.",
        "You confirm that you are not in a country under a United States government embargo and are not on a "
        "United States government list of prohibited or restricted parties. Apple and its subsidiaries are third "
        "party beneficiaries of these terms and may enforce them against you.",
        f"If you got the app from the App Store, you also follow the Usage Rules in the "
        f"{link(APPLE_MEDIA_TERMS, 'Apple Media Services Terms')}. If you got the app from Google Play, the "
        f"{link(GOOGLE_PLAY_TERMS, 'Google Play Terms of Service')} also apply.",
    ]),
    ("law", "Law and disputes", [
        "These terms are governed by the law of Finland. If you are a consumer, you also keep the protection of "
        "the mandatory consumer law of the country where you live, and you can bring a claim in the courts "
        "there.",
        f"If something is wrong, please write to us first at {MAIL}; we would much rather put it right. Consumers "
        f"may also bring a dispute to the Finnish Consumer Disputes Board ({link(KULUTTAJARIITA, 'kuluttajariita.fi')}) "
        "or to the consumer authority in their own country.",
    ]),
    ("changes-terms", "Changes to these terms", [
        "We may update these terms for a valid reason: when the app or Premium changes as described above, when "
        "the law or the stores’ rules change, or to make the terms clearer or correct a mistake. The date at the "
        "top shows the latest version.",
        "If a change affects you in an important way, we will tell you before it takes effect: by email where we "
        "have your address, and otherwise in the app or in the store listing. Changes to the Premium terms apply "
        "to you from your next renewal after we have told you, and you can cancel before then. If you do not "
        "agree to a change, you can stop using the app and cancel Premium.",
    ]),
    ("contact", "Contact", [
        f"{COMPANY}, Business ID {BID}, {ADDRESS}. Email: {MAIL}. Phone: {phone()}.",
    ]),
]


# --------------------------------------------------------------------------------------------------------------
# Page shell
# --------------------------------------------------------------------------------------------------------------

CSS = """@font-face{font-family:Lora;font-style:normal;font-weight:400;font-display:swap;src:url(%(a)sfonts/Lora_400Regular.ttf) format("truetype")}
@font-face{font-family:Lora;font-style:italic;font-weight:400;font-display:swap;src:url(%(a)sfonts/Lora_400Regular_Italic.ttf) format("truetype")}
@font-face{font-family:Lora;font-style:normal;font-weight:600;font-display:swap;src:url(%(a)sfonts/Lora_600SemiBold.ttf) format("truetype")}
:root{color-scheme:light;--paper:#F7F4EC;--green:#1F4438;--muted:#4A5546;--line:#D5D9CB;--neutral:#EBE8DC;--sage:#D5E2CD;--plate:rgba(255,255,255,.55)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%;text-size-adjust:100%%}
body{margin:0;background:var(--paper);color:var(--green);font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;overflow-wrap:break-word}
a{color:var(--green);text-decoration-color:rgba(31,68,56,.4);text-underline-offset:.18em;text-decoration-thickness:1px}
a:hover{text-decoration-color:var(--green)}
a:focus-visible{outline:2px solid var(--green);outline-offset:2px;border-radius:2px}
.wrap{max-width:42rem;margin:0 auto;padding:0 16px}
header.site{border-bottom:1px solid var(--line)}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}
.brand{display:flex;align-items:center;gap:10px;font-family:Lora,Georgia,serif;font-weight:600;font-size:1.05rem;text-decoration:none}
.brand img{width:30px;height:30px;border-radius:8px}
nav.top{display:flex;gap:18px;font-size:.95rem}
nav.top a{text-decoration:none;color:var(--muted)}
nav.top a:hover{color:var(--green)}
nav.top a[aria-current]{color:var(--green);font-weight:600;text-decoration:underline;text-decoration-color:var(--green);text-underline-offset:.35em}
main{padding:36px 0 56px}
h1,h2,h3{font-family:Lora,Georgia,serif;font-weight:600;color:var(--green);line-height:1.25}
h1{font-size:2.05rem;margin:0 0 6px;letter-spacing:-.01em}
h2{font-size:1.35rem;margin:44px 0 10px;padding-top:22px;border-top:1px solid var(--line);scroll-margin-top:16px}
h3{font-size:1.08rem;margin:26px 0 4px}
p{margin:10px 0}
ul{margin:10px 0;padding-left:1.25em}
li{margin:6px 0}
li::marker{color:var(--muted)}
b{font-weight:600}
.meta{color:var(--muted);font-size:.92rem;margin:0 0 22px}
.lead{font-family:Lora,Georgia,serif;font-size:1.12rem;line-height:1.6;background:var(--plate);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin:0 0 8px}
.note{background:var(--sage);border-radius:12px;padding:12px 16px;margin:14px 0}
.toc{margin:26px 0 0;padding:16px 20px;border:1px solid var(--line);border-radius:16px}
.toc p{margin:0 0 6px;font-size:.88rem;color:var(--muted);font-weight:600;letter-spacing:.04em;text-transform:uppercase}
.toc ol{margin:0;padding-left:2em;columns:2;column-gap:36px;font-size:.95rem}
.toc li{margin:0;padding:0 0 6px;break-inside:avoid}
.toc a{text-decoration:none}
.toc a:hover{text-decoration:underline}
.hero{display:flex;align-items:center;gap:18px;margin:0 0 18px}
.hero img{width:72px;height:72px;border-radius:18px;flex:none}
.hero h1{margin:0}
.intro{font-family:Lora,Georgia,serif;font-size:1.2rem;line-height:1.6;margin:0 0 30px}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:0 0 34px}
.card{display:block;text-decoration:none;background:var(--plate);border:1px solid var(--line);border-radius:16px;padding:18px 20px}
.card:hover{border-color:#BFC6B4}
.card strong{display:block;font-family:Lora,Georgia,serif;font-weight:600;font-size:1.15rem;margin-bottom:4px}
.card span{display:block;color:var(--muted);font-size:.95rem;line-height:1.5}
.card em{display:block;font-style:normal;margin-top:10px;font-size:.92rem;text-decoration:underline;text-decoration-color:rgba(31,68,56,.4);text-underline-offset:.18em}
.ph{unicode-bidi:bidi-override;direction:rtl;white-space:nowrap}
a[href^="tel:"]{white-space:nowrap}
.contact{color:var(--muted)}
.contact p{margin:4px 0}
footer.site{border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}
footer.site .wrap{padding-top:20px;padding-bottom:32px}
footer.site p{margin:4px 0}
footer.site nav{display:flex;flex-wrap:wrap;gap:6px 18px;margin-bottom:8px}
footer.site a{color:var(--muted)}
@media (max-width:560px){
 body{font-size:16.5px}
 h1{font-size:1.75rem}
 h2{font-size:1.22rem;margin-top:36px}
 main{padding-top:26px}
 .toc ol{columns:1}
 .cards{grid-template-columns:1fr}
 .hero img{width:60px;height:60px;border-radius:15px}
 .lead{padding:16px}
}
@media print{header.site,footer.site nav,.toc{display:none}body{background:#fff}a{text-decoration:none}}"""

PAGES = [("", "Home"), ("privacy/", "Privacy Policy"), ("terms/", "Terms of Use")]


def block(b: str) -> str:
    return b if b.startswith("<") else f"<p>{b}</p>"


def shell(path: str, title: str, description: str, content: str) -> str:
    up = "../" * path.count("/")
    a = f"{up}assets/"
    nav = "".join(
        f'<a href="{up}{p}"{" aria-current=\"page\"" if p == path else ""}>{name}</a>' for p, name in PAGES)
    foot = "".join(f'<a href="{up}{p}">{name}</a>' for p, name in PAGES[1:])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta name="theme-color" content="#F7F4EC">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" type="image/png" href="{a}favicon.png">
<link rel="apple-touch-icon" href="{a}icon-192.png">
<style>{CSS % {"a": a}}</style>
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="{up}"><img src="{a}icon-192.png" alt="" width="30" height="30">{APP}</a><nav class="top" aria-label="Pages">{nav}</nav></div></header>
<main><div class="wrap">
{content}
</div></main>
<footer class="site"><div class="wrap"><nav aria-label="Legal">{foot}<a href="mailto:{CONTACT}">Contact</a></nav>
<p>© 2026 {COMPANY} · Business ID {BID} · {ADDRESS}</p></div></footer>
<script>document.querySelectorAll(".ph").forEach(function(e){{var n=e.dataset.r.split("").reverse().join("");var a=document.createElement("a");a.href="tel:"+n;a.textContent=e.textContent.split("").reverse().join("");e.replaceWith(a)}})</script>
</body>
</html>
"""


def document(title: str, lead: str, sections) -> str:
    toc = "".join(f'<li><a href="#{sid}">{html.escape(h)}</a></li>' for sid, h, _ in sections)
    body = "".join(
        f'<section id="{sid}"><h2>{html.escape(h)}</h2>' + "".join(block(b) for b in blocks) + "</section>"
        for sid, h, blocks in sections)
    return (f'<h1>{html.escape(title)}</h1><p class="meta">{APP} · Last updated {UPDATED}</p>'
            f'<p class="lead">{lead}</p><nav class="toc" aria-label="On this page"><p>On this page</p><ol>{toc}</ol></nav>'
            f"{body}")


HOME = f"""<div class="hero"><img src="assets/icon-192.png" alt="" width="72" height="72"><h1>{APP}</h1></div>
<p class="intro">A short Bible verse, at the times you choose, from the topics that matter to you. Open the app and
there is a quiet place to read it slowly, see it in context, like it, write a note or share it.</p>
<div class="cards">
<a class="card" href="privacy/"><strong>Privacy Policy</strong><span>No accounts, ads or tracking. What stays on your phone, and the few times something leaves it.</span><em>Read the Privacy Policy</em></a>
<a class="card" href="terms/"><strong>Terms of Use</strong><span>Using the app, the Premium subscription, the Bible text and the explanations.</span><em>Read the Terms of Use</em></a>
</div>
<h2>Contact</h2>
<div class="contact"><p>{COMPANY} · Business ID {BID}</p><p>{ADDRESS}</p><p>{MAIL}</p><p>{phone()}</p></div>"""


root = pathlib.Path(__file__).parent
out = {
    "": shell("", f"{APP} · Legal", f"Privacy Policy and Terms of Use for {APP}, published by {COMPANY}.", HOME),
    "privacy/": shell("privacy/", f"Privacy Policy · {APP}", f"How {APP} handles your data.",
                      document("Privacy Policy", PRIVACY_LEAD, PRIVACY)),
    "terms/": shell("terms/", f"Terms of Use · {APP}", f"Terms of Use and Premium subscription terms for {APP}.",
                    document("Terms of Use", TERMS_LEAD, TERMS)),
}
for path, text in out.items():
    f = root / path / "index.html"
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(text, encoding="utf-8")
(root / ".nojekyll").write_text("")
print("built", ["/" + p for p in out])
