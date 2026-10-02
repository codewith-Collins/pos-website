# POS website

Product website for the POS (point-of-sale software for Kenyan shops), served by GitHub Pages
from `docs/`. The POS source code is in a separate private repository.

- `content/` - page bodies (home, privacy, terms, refunds, cookies)
- `assets/` - stylesheet, icons and screenshots
- `build.py` - assembles `docs/` from the two; **company details and fees are at its top**

## Update the site

1. Edit `COMPANY` at the top of `build.py` (same details as the app's
   `frontend/src/legal/company.ts`); set `completed` to `True` once they are real and the legal
   pages have been reviewed by an advocate. Until then every page shows a "Draft" notice.
2. `python build.py`
3. Commit and push; GitHub Pages republishes within a minute or two.

No cookies, analytics, web fonts or scripts: keep it that way, or the cookie and privacy pages
must change and a consent banner becomes necessary. Screenshots show the real software with
sample data from a demonstration shop.
