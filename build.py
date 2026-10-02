"""Builds the website into docs/ (served by GitHub Pages).

Usage:  python build.py

Edit COMPANY below (the same details as the app's frontend/src/legal/company.ts), then rebuild.
While COMPANY['completed'] is False every page shows a "Draft" notice.
"""
import html
import shutil
from pathlib import Path

COMPANY = {
    'completed': False,
    'product': 'POS',
    'name': 'Collins Muigai',
    'registration': 'sole trader',
    'email': 'murucollins@gmail.com',
    'phone': '0180048478',
    'whatsapp': '',                        # e.g. 254712345678 (digits only); empty hides the link
    'licence_fee': 'KSh 25,000 per shop, paid once',
    'installation_fee': 'KSh 3,000',
    'support_fee': 'optional; charged only if the shop asks for it, at a price agreed in writing first',
    'refund_days': '14',
    'last_updated': '2 October 2026',
}

PAGES = {
    'index': 'Point of sale for Kenyan shops',
    'privacy': 'Privacy policy',
    'terms': 'Terms of service',
    'refunds': 'Refund policy',
    'cookies': 'Cookie policy',
}

ROOT = Path(__file__).parent
OUT = ROOT / 'docs'

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{product}: point-of-sale software for small and medium shops in Kenya. Sales, stock, M-Pesa and cash, receipts, reports and backups, on your own computer.">
  <meta name="theme-color" content="#2563eb">
  <link rel="icon" href="favicon.ico" sizes="any">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {draft}
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="./"><img src="favicon.svg" alt="" width="34" height="34"> {product}</a>
      <nav class="site-nav" aria-label="Main">
        <a href="./#features">Features</a>
        <a href="./#how-it-works">How it works</a>
        <a href="./#faq">FAQ</a>
        <a class="nav-cta" href="./#contact">Contact us</a>
      </nav>
    </div>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <p>&copy; 2026 {name}. No cookies, tracking or analytics on this site.</p>
      <nav aria-label="Legal">
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
        <a href="refunds.html">Refunds</a>
        <a href="cookies.html">Cookies</a>
      </nav>
    </div>
  </footer>
</body>
</html>
"""

DRAFT = ('<aside class="draft" aria-label="Draft notice">Draft website: the legal pages are '
         'awaiting review by an advocate.</aside>')


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / 'assets', OUT)
    values = {k: html.escape(v) for k, v in COMPANY.items() if isinstance(v, str)}
    whatsapp = COMPANY['whatsapp']
    values['whatsapp_link'] = (f'<li>WhatsApp: <a href="https://wa.me/{whatsapp}">message us</a></li>'
                               if whatsapp else '')
    for page, title in PAGES.items():
        body = (ROOT / 'content' / f'{page}.html').read_text(encoding='utf-8')
        for key, value in values.items():
            body = body.replace('{{' + key + '}}', value)
        full_title = f"{COMPANY['product']}: {title}" if page == 'index' else f"{title} | {COMPANY['product']}"
        page_html = TEMPLATE.format(title=html.escape(full_title), body=body, product=values['product'],
                                    name=values['name'], draft='' if COMPANY['completed'] else DRAFT)
        (OUT / f'{page}.html').write_text(page_html, encoding='utf-8')
    (OUT / '.nojekyll').write_text('', encoding='utf-8')  # serve files as they are
    print(f'Built {len(PAGES)} pages into {OUT}')


if __name__ == '__main__':
    main()
