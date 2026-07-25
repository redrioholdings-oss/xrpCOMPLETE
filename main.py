"""
═══════════════════════════════════════════════════════════════════════
XRP Complete — Iteration 3
Version 102 — Full rebrand: XRP Complete → XRP Complete (xrpcomplete.com)
Red Rio Ventures, LLC
═══════════════════════════════════════════════════════════════════════

V127 changes:
  1. Final dimensions locked: 250px wide x 70px tall (height:70px,
     width:250px). Supersedes V126's 170x70.

V126 changes:
  1. Correction: confirmed final dimensions are 70px tall x 170px wide
     (height:70px, width:170px) — reverting V125's swap back to V124's
     values, now stated explicitly to avoid further ambiguity.

V125 changes:
  1. Correction: V124 transposed the requested dimensions (set width:170px,
     height:70px). Fixed to the dimensions as given — width:70px,
     height:170px.

V124 changes:
  1. Correction: V123 sized the blog ad to the border-alignment rule (full
     column width). Clarified the sample image was for style/color match
     only — actual size is fixed at 170x70px. Ad now rendered at that fixed
     box (object-fit:contain, so the square source image scales down without
     stretching/distortion rather than being squeezed to fit).

V123 changes:
  1. Header BLOG button replaced with a clickable blog advertisement image
     (Template D v2 — Full-Bleed ad graphic, provided by Rich). Still links
     out to xrpcompleteblog.com (target=_blank). Sized to width:100% of the
     right-side header column so its left edge lands on the ABOUT US
     button's left edge and its right edge lands on the same edge the
     "feeds scanned" line's right border already sits on (that column
     auto-sizes to its widest row, so both border points align without
     hardcoded pixel widths). Source image downscaled to 320x320 PNG
     (preserves the rounded-corner transparency) and embedded the same
     way the header logo already is, served at /blog_ad.png.

V109 changes:
  1. Dollar Cost Averaging Calculator: weekly vs monthly contribution
     comparison using real daily close prices (reuses the same Coinbase
     candle fetch already powering RSI/52-week/etc, no new API call).
     Client-side JS recalculates live as the user changes either amount.
  2. 30-Day Historical Price Data table: Date, Day of Week, Open, High,
     Low, Close, $ Change, % Change — newest first, real OHLC from the
     same candle source.
  3. News Mention Volume (for yesterday): real story counts across all
     RSS feeds this site already tracks, broken down by category, with
     total count and contributing-source count. Locks in at 00:15 UTC
     daily. Built as an honest substitute for a literal "social media
     post count" section, which was not built — no free/reliable API
     exists for real cross-platform social post counts, and fabricating
     that data would violate this site's own established principle of
     never inventing figures (see SENTIMENT_HISTORY's existing comment:
     "Builds up honestly over time -- no fabricated history").

V108 changes:
  1. Correction: V107 darkened the shared card background (--s1) per an
     initial reading of user markup. Clarified request was the opposite —
     boxes needed to be BRIGHTER than the original V106 baseline, not
     darker. --s1 changed 0a0a0a (V106) -> 050505 (V107, wrong direction)
     -> 161f2e (V108, ~3x brighter luminance than the V106 original).
     Borders on .si and .acct also strengthened (rgba(117,188,255,.25/.
     var(--b)) -> .35/.4 opacity) for additional definition.

V107 changes:
  1. Permanent cross-platform flag fix: all 132 flag-emoji instances (36
     distinct countries/regions) now render via inline SVG through a single
     centralized post-processor (replace_flags_with_svg), applied once to
     the final page output. Fixes flags showing as raw two-letter codes on
     Windows (Segoe UI Emoji has never shipped flag glyphs) on every
     browser, permanently — no font/OS dependency remains.
  2. Mainstream Integration icon: replaced Carpentry Saw (Unicode 13.0,
     2020 — unsupported on older Windows installs, rendered as a blank
     box) with Hammer and Wrench, already used 40x elsewhere on this page.
  3. US Intelligence icon: automatically fixed by item 1 (it was the US
     flag emoji).
  4. Fixed a real color-duplication bug in XRP Complete Exclusive
     Intelligence: "Partnership Momentum" was hardcoded to the same yellow
     as "Institutional Confidence Index"; changed to blue for a distinct
     4-color set matching Catalyst Clock (orange) and Narrative Diffusion
     Map (turquoise).
  5. Darkened the shared card-surface background (--s1, 0a0a0a -> 050505)
     used by the top 3-box status row and every .acct panel (RSI Signals,
     Support & Resistance, etc.) per direct user markup.
  6. Responsive layout: added a phone-width breakpoint for the previously
     uncovered 3-box status row, plus a comprehensive small-phone safety
     net (480px and 360px breakpoints) catching any remaining
     multi-column grids, table overflow, and spacing on narrow screens —
     layered on top of the 19 section-specific breakpoints already
     present (900px/700px), which were left untouched.

V106 changes:
  1. Blog button doubled in size: font-size 13px->26px, padding 3px/10px->
     6px/20px, icon 15px->30px, border 1px->2px. Hollow outline style from
     V105 preserved (transparent bg, var(--hdr) text/border).

V105 changes:
  1. Blog button changed from filled gradient slab to hollow outline style,
     matching the ABOUT US button exactly (transparent bg, var(--hdr) text
     and border, same padding/radius/font-weight). Still links to
     xrpcompleteblog.com.

V104 changes:
  1. Blog button now links to xrpcompleteblog.com (XRP Rx brand retired
     before launch; XRPRadar and XRP Rx are both dead brands)

V103 changes:
  1. Blog button (originally xrprx.com) added under the feeds-scanned line —
     light blue, lab-flask icon, 130x55 (half the 110px satellite icon height)
  2. XRP Global Liquidity Tracker section added directly under the Live Chart:
     global 24h volume, market cap, turnover ratio, and liquidity rating,
     computed from existing CoinPaprika data (no new API dependencies).
     Data layer refreshes every 60s (exceeds the 5-minute requirement).

V102 changes (rebrand only — zero functional changes):
  1. Site name, titles, headers, footer, About page: XRP Complete → XRP Complete
  2. Domain references → xrpcomplete.com (single domain)
  3. Copyright line updated to XRP Complete / Red Rio Ventures, LLC
  4. User-Agent identifiers → XRPComplete/*
  5. Third frozen copyright archive added: /copyright7_26_c (2026-07-12, V102)
     Prior archives /copyright7_26 and /copyright7_26_b remain untouched.

All fonts, colors, layout, feeds, features, and logic identical to V101.

Live data (background thread, refreshed every 60s):
  • XRP / USD      — CoinPaprika / Coinbase
  • Fear & Greed   — alternative.me
  • Active Sources — count of live data sources connected
═══════════════════════════════════════════════════════════════════════
"""

import base64
import os
import time
import threading
from datetime import datetime, timezone, timedelta
import html
import json
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from email.utils import parsedate_to_datetime
try:
    from zoneinfo import ZoneInfo
    CENTRAL = ZoneInfo("America/Chicago")
except Exception:
    CENTRAL = timezone(timedelta(hours=-6))  # CST fallback

import requests
from flask import Flask, Response, jsonify

# ─────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────
APP_VERSION = "129"

# LOGO (V120) - helix, recoloured to XRP blue #008CFF and sized to 375px
# tall (three times what the header displays). Embedded here so the whole
# deploy stays a single main.py edit. Served at /logo.jpg.
LOGO_B64 = (
    "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"
    "AyUa0uPJZllk9RRaV8MXV1VpraT9DV7p8p+ZypDZIm+ioCAsXraROSWySbEwp6p8T9ppoe7ZoOOe71ygK9KZX+q0dhaT82KpFHHG"
    "PlC94Vi+uTWFrK/95I303ZQ4bky0sGbM2vr3Gt4miubmimWqxIW0t61BbSxPdpwcgOWU8YTe7kJeaC8nOByvNfDe1zwDe3o0cFtB"
    "bQUzC9uLD+E1laytZ/F//8QAKRABAAIBAwIFBQEBAQAAAAAAAQARITFBUWFxIDCBkaEQscHR8OFA8f/aAAgBAQABPyH/AKWZWC3A"
    "EF09nP8AwcF2oszdnl+0Zg5n/vH7n8J+ZY7Cw3eLImp8ZiejS3+Y/rV+fLtfob6t/j6XOiHvH/PEGjgOxwx0zVVAZn4rPpr4wVoj"
    "wXu617yhWXBfsT3fflstZdtl2iyx9hmqA+Et+/jy7fs3D+H1hgciKJ0Zqd0HU2YioK9JS1bvcPdlY9FF+xcrG/n8lmUC8texUOHr"
    "QblUaODEXe82qsXtywFCoqS+0rNVFOBmaqXvL4wEqPYf2TuprN6OUTLFYWvYhlU/DcwmB0mCSLvsYTXr+Hj3JqiLIV2Vi7XvbCNK"
    "K8fd6oxoh5ePzHkPKXZwwiCsR7k3e1TCwOZCPLRT5ol35lndHYofEQtK8s6Asb7JWKjgHzEgA4FfgmH1wlPglA8oWgH0EJNrsbsA"
    "lnqfL6+Tr44jxxBFYXl3qQ8OIonuwiAcH6i+IyPTiD8w4ujkXzOmNgiktPeAFK6mh5Yrhp3FlImaoUMKmP6z+/LDMrU3cdoDB1lH"
    "VdC4RkmONJdJrMR2rCIfWnFmLsdOh1ek5tt7Xlf6vpESsGsym496FmoX26eZd0V9swT07wxYCex8E3IWNjs8MpNpTwX4IQAKKV/d"
    "4LW4AvAm8cXXOA62h+/OYJaO5BqCIgdamxt1eIURmlbHY/M4GaCYEbOA5ny5ZNo+NP8Af+C3igwnz3c56u8evTn6FlVrQbwRsvmF"
    "m1Xoaf8AAsKLJw/qSkE9NGIK4YwvbLaAHjS9I7uhS/tGLbm7c9/n/tJRj0+8cp0UAprEtQIwEGpGqR45yhLZkSOHVCKcHETUX+vT"
    "zadWbG6fiN/X/P0LUgfUcrLVw0oxe/22bSxOuT+Rgm0/E3T3mHA0E0Skq3HVx5YIv+GN2VsC2xqEk6hxgAVxvOka8mmYi0uHGtoi"
    "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"
)
LOGO_BYTES = base64.b64decode(LOGO_B64)

# BLOG AD (V128/V129) - header advertisement for XRP Complete Blog. Purpose-built
# 250x70 banner (embedded at 500x140 for retina crispness, displayed at
# 250x70): satellite photo left, "XRP COMPLETE BLOG" wordmark, tagline,
# domain, Template D palette. Replaces the V123 square graphic that was
# letterboxed inside the 250x70 slot. Served at /blog_ad.png.
# V129: the <img> src now carries ?v={APP_VERSION}, so every version bump
# produces a distinct URL. A browser holding a cached copy of the previous
# image physically cannot serve it for the new URL, which removes stale
# caching as a possible cause on this and all future ad swaps.
BLOG_AD_B64 = (
    "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"
    "O9/xNu7+7Dt51Pe9gTzt05Oa6VadhcU5lldWac9MM+iskl9yKY96bMBtX/ksp+Kn0mjOs76xRntmhkHf54YHLuXkyZPs2LWbq6/Y"
    "Q3egOXH/bbSWD1PfcR3Tu66nNdXm+Mk1jFC02zW6/SF01olcSmN6B+vrI8LAMdVKCANYXRsRxJJQSlox6OEa9y4tYZ1X8+NEAeRF"
    "d6JNincK73sshqsaJJTUN8CmEq9nyt/OLAy72YTwANlo1PjP/9dPopQsuq35MrR/8Kfv4rY772PnjkXe/p6P8n3PeBLf/71PLEDf"
    "x9b/6y+/iS9/7XbSLHvQanHOOuq1hDvuvp+3/MX7+Zmf+MGiWY4/t1/82TfwmS98FWMtofzOymVKL/3Wzgy/df/V/Pzld/oCLdZ7"
    "30I4Lm/0ubrptS6ZxZeILa5nM3Cs5wG/ed/1rOURdaW9cK0Y962HL2dbNOI5207R0Z4e72moSctNU+vIwptOre/eBp4enw0df7O0"
    "yJ8dvqLoJnaB88DT7nf32tzdb/GwVodBUZZWCF/g5rOri+eBhO+8lcC4ozbkTx/+T6UCBPAZAD2teOM3H4PN4rM+udrBda0uN7a7"
    "m+ZuHMyF8MCwzsdO76rEo9/WeX8Hju9dKMeNUZtHx9OVHsY5H1cfOZ/ymBeA9/nRGrdnXRKpzkjhFGTOsjus8f4dj9oE5AHj3O6e"
    "0zSk4vc7B9kRxLy4sYMNm2NwdJ2mJiSPj2fGn0Vn6BYNVCSCeRnxwf5JfnfjIHWpJj5BjhDJr68dYKeKeVIyy2rRyrXrfKOWh8dt"
    "3xnOeY++7zxvoBDMyIj39k7wh51DVfnb71aTWlvuP77KZ297gHuOLaOkpN2ssW/HPFftWWCqVUMKydxUk0a9ThiG7Ns+y/WXbeNJ"
    "j7iCa/YucMWebVy+e4GF6SaZMcRx7AUqYcgjLr+E/TtmmWk2iKOI4SgjiLzq1uKreEmkb94iBEdPrIFzLMw0uWLPPO16jMmzcY64"
    "0zibYbVvvuIrwfniMDofMhoN6PUGDAcpg35KPuhh0xX0YJnRYIVseAo7OoEeniDvL5P1V0gHpxn1jjHsPEDaOYWzU8StJ9JaeCLJ"
    "9OWEzTZRc4qkNUutNUfUmCZqThE3ZkgaU4RJE5k0EVEdFdcJa3WCuI4jJG62ycMab3nru1ldXub1b/gxptQ6X/urP8I5y8L2RY4c"
    "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"
    "G/ovjjGWJImxNmI4HJAe/DqjlUM0L3k4re3XMMgHbDBNww2Ym2vRHWQkqSSOJEKFrHeGBFFCzfU4dOoExpgiy4Hqm7e5ixqAm4iL"
    "i7PA35W15zd9dc/1e/HX5k2bXpuZbvNbf/gXvsFKsZBY3+jw8b/9TJEX7r1rrQ3tVpN3vf+vaNRrTE+1KiZBKkmtFhPFIcNRyn/7"
    "339KFIXVImRldQNjvUbAGEuz0eCd7/s4jUaNJI4p0/aCQDE3O8X9h47QqNf5u09/keFw5Cn+otb+l792e3E/vj0JLxbvqZ/MavzO"
    "/VfzjqP7uaLRZXetT6Pwvjs65NCwyf39Jus6oia9t3k+r6+83I0g59aNWb7emWFXMuSKZodt0YhYGTIjOZ0l3Ntrc2RUxzlfXMZN"
    "PED9OL4Zyp8dvoxIWh8ekrCahVVueCAsJ9M6v33/1SzGqa8oCXxyaUclhkuk4cvrc/zv+1WhBfBpaXd2pwiFRQlx3tfj4rgPZuec"
    "K+eWPJXeY2YlIyupnTG3B9NYWgc1BV9enyaZyI8vX4ul5c7uFL97/35yW4L1ufcv33PmtflWjz/ex+djf260tikf+3yWYlkxGXdm"
    "Pe7J+wDUi2Ytsoi9/+7GA8TIC17TFFvE4jdvb4qAL6Xr/HO6wSVBjWuiJjtVTCIUqTOcNCl3ZD0O6SEWHyt3DxKqKavbBULwN4Ml"
    "/n64wr6wxtVhk20qIhaKzBlOmow7sy4PXOS4300mdj76+S6OQ1QheJNSooBhrhmlmrnE8vhrdzEzu4jJMza6XdIsZ70/wqqIOIoJ"
    "lGJhqsEoTavOVL6ka4BSgvuPnWal0+feI0vMtur0ByNWOn2UECRxRG40WNA6x+FLmFpjcKZYiQugKLcZhQH9wRCtDUopkjgCIdHW"
    "YXJfd1uoAGQAKO+1Cx9n953evCIcESFlSBAlREmEiiIcDYKgRpi0kGENEfoWrmHcIEimCJM5wrgNbpnB+q2MescxWU4+7JNnfUw6"
    "IBv1sdmIfNTH6BE6HeC0bwLjTAbOMlg9xVMe/3C+5+lP4yMffD/fvOcBrnzCq6lNbcM6yxNu2ME9x9Y4/MAx2k3ByqkVajPz7Gv1"
    "OfDNL7ESXM71V1/K2r3/wJf++Vauu2qBPftvoDcwKCXQ2pBlGVJJ4qRGlqZFqqCj0Z5DtC9h53WPZWlpnXSUMjvboJ5EHD29TjtR"
    "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"
    "VPZxXclcK6ATz3Dy6mFGayWec8FWrrrjYQq+zYbxOu0gYqbRo90NybTGsQTVSoGw0SOKE4qORWQ7RFE0WGR9RL2Vu5GWp0kIIUnS"
    "DNe1SFITjymXC3Q6PWzLWKdpkqIyQcG32LByhMmZFnGWsdDsopRm1fgQc4sdRofKNLo9FloBJdchjCNcz2X1hOGP37O/iSU1mdIs"
    "NHpUyh5hlGBhCHeCVpcnnHMiF5+9hYJvQIBpmGLbLr1uD9/30UAcRWZAbePGKfoeSSzp9jo8sns/1dk9WMk8ifCwc301eOCEIOoF"
    "PO3pz+CsJzyHX/vVd3HGCRNUxk/Hdu8n7PYQqk0lB0YlcYrWFlkS4kqBXyzSbrdZuXotlm2xZ9dOXK/AilWr0SqjFwQIBNNTU3ie"
    "Z5j2MCEEK4iIoxAhJdVqdcDwJi2JtB0cS1MMJ4l7MZE9SoLAkg6WLXJETkIv1jg5Pay0JL5rIzB0wo4FoUhNyqLWpKkkThSWV0L6"
    "PmW3TJbFpFFInCTGXT7Y6B1elFJLaY+5ZPl3UvWtVI1T8rnx2tt5/Ts/SacbUikX+OQH3sDPP/0Cnnjhqfzbt2+kXi/znre9lMVG"
    "h+f+8vu5++6HQUpGRmp88W9+h3e95SVcdd1dzMw1ByChgeTeqA/81Ze5+PyTee9vvJzL3vyhQ+LzZooFKsl4ztPOZ/P6lXie8Q58"
    "/cqb2Tk5S5KkXH/rA7zsBZdw7umbueGW+7n4/FNYv2ac//fX/0ap6PPMp5zLaSet54Htezn/zBPwPIcf3XL/IHa7HFSotMbzHPZO"
    "zfNnn/gKf/Z7r+b33vZSbrtnB3/9+W9T8N1D+uk4NsWii+c6PPfnzuelz3sCCwtN7ntoN1bfTao1w/Uy61aPUi4XuPj8k7nshZcw"
    "O9vg3m278FznwI3FYSRNM4Tn8qOrbuUN7zp0bi4+bytXXH0rX//uzZy0aTUf+IPX8KVvXMc/feVqxkfrjI1UefdbfuGIc/a7b34J"
    "V157O70wflTAWJoqEysHkiTj9a94BmeesYUPf/KrfPDjl5OmGZaU/PHvXMavvOzn2Ds1lwMBA17x4ifzC89/Ih/4iy/we3/2T8aN"
    "lCle/uIn88+f+C1e/dJL+cRnv4XKzPvt7X/w9/zbf9yEEPDcp53Ppz/8Vi574ZO44qrb6AQhb3zlszjz9M28648/y19/7gpAMDFW"
    "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"
    "SUVORK5CYII="
)
BLOG_AD_BYTES = base64.b64decode(BLOG_AD_B64)

APP_NAME    = "XRP Complete"
TAGLINE     = "The NEW XRP Intelligence Standard"
COPYRIGHT   = "\u00A9\uFE0F Copyright 2026 XRP Complete / Red Rio Ventures, LLC. All rights reserved globally."
BOOT_TIME   = datetime.now(timezone.utc)

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────
# LIVE MARKET DATA (background refresh; page reads the cache)
# ─────────────────────────────────────────────────────────────────────
MARKET = {
    "xrp_price": None, "xrp_chg": None,
    "fng": None, "fng_label": None,
    "mcap": None, "vol24": None, "rank": None, "h24": None, "l24": None, "xrpbtc": None,
    "fng_history": [], "funding": None, "hist_30d": [], "hist_full": [],
    "perf_1w": None, "perf_30d": None, "perf_90d": None, "perf_6m": None,
    "fx": {},
    "competitors": {},
    "ad_7d_delta": None, "ad_30d_delta": None,
    "corr_btc": None, "corr_eth": None,
    "ob_bids": [], "ob_asks": [], "ob_bid_total": None, "ob_ask_total": None,
    "sources_active": 0, "sources_total": 3,
    "updated": None,
    # technicals (Binance klines)
    "rsi_1h": None, "rsi_1d": None,
    "w52_low": None, "w52_high": None,
    "tm_1y": None, "tm_1m": None,
    "sr_support": None, "sr_resistance": None,
}


def calc_rsi(closes, period=14):
    if len(closes) < period + 1:
        return None
    deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    gains  = [d if d > 0 else 0 for d in deltas]
    losses = [-d if d < 0 else 0 for d in deltas]
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    for i in range(period, len(deltas)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - 100 / (1 + rs), 1)


def _coinbase_candles(product_id, granularity=86400, limit=300):
    """Public Coinbase Exchange candles. Returns oldest->newest as
    [time, low, high, open, close, volume] floats. No key needed; not
    subject to Binance's cloud-IP geo-block."""
    hdr = {"User-Agent": "XRPComplete/4"}
    r = requests.get(f"https://api.exchange.coinbase.com/products/{product_id}/candles",
                      params={"granularity": granularity}, headers=hdr, timeout=8)
    data = r.json()
    if not isinstance(data, list):
        return []
    data.sort(key=lambda c: c[0])  # Coinbase returns newest-first; sort oldest->newest
    return data[-limit:]

def fetch_market():
    active = 0
    hdr = {"User-Agent": "XRPComplete/4"}

    # Price, 24h change, market cap, volume, rank — CoinPaprika (keyless; CoinCap v2 was
    # deprecated April 2025 and now requires a paid key, so it no longer works here)
    try:
        r = requests.get("https://api.coinpaprika.com/v1/tickers/xrp-xrp", headers=hdr, timeout=8)
        d = r.json()
        q = (d.get("quotes") or {}).get("USD") or {}
        p = float(q.get("price", 0) or 0)
        if p > 0:
            MARKET["xrp_price"] = p
            MARKET["xrp_chg"]   = float(q.get("percent_change_24h", 0) or 0)
            MARKET["mcap"]      = float(q.get("market_cap", 0) or 0)
            MARKET["vol24"]     = float(q.get("volume_24h", 0) or 0)
            MARKET["rank"]      = d.get("rank")
            active += 1
    except Exception:
        pass

    try:
        r = requests.get("https://api.alternative.me/fng/?limit=30", headers=hdr, timeout=5)
        arr = r.json().get("data", [])
        if arr:
            MARKET["fng"]       = int(arr[0].get("value", 0))
            MARKET["fng_label"] = arr[0].get("value_classification", "")
            MARKET["fng_history"] = [int(x.get("value", 0)) for x in reversed(arr)]  # oldest -> newest
            active += 1
    except Exception:
        pass

    # Note: funding rate needs a futures/perpetual exchange (Binance fapi was used before).
    # No safe cloud-reachable replacement is wired up, so this stays None. Smart Money Score
    # already rescales cleanly across whichever of its components are actually available.

    # Historical daily + hourly candles — Coinbase Exchange (public, no key, and not subject
    # to Binance.com's block on cloud-hosting IPs). Powers RSI, 52-week range, Price Time
    # Machine, Support & Resistance, longitudinal performance, and the A/D line.
    try:
        k1h = _coinbase_candles("XRP-USD", granularity=3600, limit=200)
        k1d = _coinbase_candles("XRP-USD", granularity=86400, limit=300)

        if k1h:
            closes_1h = [float(c[4]) for c in k1h]
            MARKET["rsi_1h"] = calc_rsi(closes_1h)
            last24 = k1h[-24:]
            MARKET["h24"] = max(float(c[2]) for c in last24)  # candle[2] = high
            MARKET["l24"] = min(float(c[1]) for c in last24)  # candle[1] = low

        if k1d:
            closes_1d = [float(c[4]) for c in k1d]
            highs_1d  = [float(c[2]) for c in k1d]
            lows_1d   = [float(c[1]) for c in k1d]
            MARKET["rsi_1d"]    = calc_rsi(closes_1d)
            MARKET["w52_low"]   = min(lows_1d)
            MARKET["w52_high"]  = max(highs_1d)
            # Price Time Machine (oldest available candle stands in for "~1 year ago" when
            # fewer than 365 days are available from a single 300-candle request)
            if len(closes_1d) >= 2:
                MARKET["tm_1y"] = closes_1d[0]
            if len(closes_1d) >= 31:
                MARKET["tm_1m"] = closes_1d[-31]
            # Support & Resistance from the last 90 days
            window = k1d[-90:] if len(k1d) >= 90 else k1d
            MARKET["sr_support"]    = min(float(c[1]) for c in window)
            MARKET["sr_resistance"] = max(float(c[2]) for c in window)
            # Longitudinal performance windows
            cur = closes_1d[-1]
            def _perf(days):
                if len(closes_1d) > days and closes_1d[-(days + 1)]:
                    old = closes_1d[-(days + 1)]
                    return (cur - old) / old * 100
                return None
            MARKET["perf_1w"]  = _perf(7)
            MARKET["perf_30d"] = _perf(30)
            MARKET["perf_90d"] = _perf(90)
            MARKET["perf_6m"]  = _perf(180)
            # 30-Day Historical Price Data + full DCA history (V109) \u2014 reuses the
            # k1d candles already fetched above for RSI/52-week/etc.; no new API call.
            MARKET["hist_30d"] = [
                {"t": int(c[0]), "o": float(c[3]), "h": float(c[2]),
                 "l": float(c[1]), "c": float(c[4])}
                for c in k1d[-30:]
            ]
            MARKET["hist_full"] = [
                {"t": int(c[0]), "c": float(c[4])} for c in k1d
            ]
            # Chaikin Accumulation/Distribution Line (pure price/volume TA indicator)
            ad = 0.0
            ad_series = []
            for c in k1d:
                lo, hi, cl, v = float(c[1]), float(c[2]), float(c[4]), float(c[5])
                mfm = ((cl - lo) - (hi - cl)) / (hi - lo) if hi != lo else 0.0
                ad += mfm * v
                ad_series.append(ad)
            if len(ad_series) >= 8:
                MARKET["ad_7d_delta"] = ad_series[-1] - ad_series[-8]
            if len(ad_series) >= 31:
                MARKET["ad_30d_delta"] = ad_series[-1] - ad_series[-31]
        if k1h or k1d:
            active += 1
    except Exception:
        pass

    # XRP/BTC cross-rate, computed from each asset's own USD close (Coinbase doesn't
    # need a direct XRP-BTC pair for this and it keeps one fewer network call in play)
    try:
        if MARKET.get("xrp_price"):
            btc_k = _coinbase_candles("BTC-USD", granularity=86400, limit=2)
            if btc_k:
                btc_price = float(btc_k[-1][4])
                if btc_price:
                    MARKET["xrpbtc"] = MARKET["xrp_price"] / btc_price
    except Exception:
        pass

    MARKET["sources_active"] = active
    MARKET["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


COMPETITORS = [
    {"id": "solana",   "symbol": "SOL", "emoji": "\u25CE", "paprika": "sol-solana",   "coinbase": "SOL-USD"},
    {"id": "ethereum", "symbol": "ETH", "emoji": "\u27E0", "paprika": "eth-ethereum", "coinbase": "ETH-USD"},
    {"id": "cardano",  "symbol": "ADA", "emoji": "\u20B3", "paprika": "ada-cardano",  "coinbase": "ADA-USD"},
    {"id": "stellar",  "symbol": "XLM", "emoji": "\u2726", "paprika": "xlm-stellar",  "coinbase": "XLM-USD"},
]
COMPETITOR_EDGE = {
    "SOL": "Payment rails vs. smart contract platform \u2014 XRP settles instantly for a near-zero fee.",
    "ETH": "XRP settles far cheaper per transaction with faster finality \u2014 purpose-built for payments.",
    "ADA": "XRP has live ODL corridors, bank partnerships and regulatory clarity vs. a research-first roadmap.",
    "XLM": "XRP carries deeper liquidity, more active corridors and broader institutional adoption.",
}

# ── CLARITY Act Tracker — top 10 most influential stories, hard-capped, oldest/lowest-ranked drop off ──
CLARITY_FEED = "https://news.google.com/rss/search?q=CLARITY+Act+crypto+Senate&hl=en-US&gl=US&ceid=US:en"
CLARITY_ACT_STORIES = []
_CLARITY_SEEN_KEYS = set()
_CLARITY_MAX = 10

def fetch_clarity_tracker():
    hdr = {"User-Agent": "XRPComplete/4"}
    now = datetime.now(timezone.utc)
    candidates = []

    # 1. Dedicated Google News RSS search
    try:
        r = requests.get(CLARITY_FEED, headers=hdr, timeout=8)
        for e in _parse_feed(r.content)[:12]:
            if not e["title"]:
                continue
            dt = _parse_date(e["date_str"]) or now
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            candidates.append({"key": "clarity:" + e["title"].lower()[:80], "title": e["title"][:160],
                               "link": e["link"] or "#", "source": "Google News", "dt": dt,
                               "influence": _influence(e["title"], "Google News")})
    except Exception:
        pass

    # 2. Scan the existing XRP news pool for CLARITY Act mentions (already-classified stories)
    for s in NEWS.get("pool", []):
        text = (s["title"] + " " + s.get("summary", "")).lower()
        if "clarity act" in text or "digital asset market clarity" in text:
            candidates.append({"key": "clarity:" + s["key"], "title": s["title"], "link": s["link"],
                               "source": s["source"], "dt": s["dt"], "influence": s["influence"]})

    for c in candidates:
        if c["key"] in _CLARITY_SEEN_KEYS:
            continue
        _CLARITY_SEEN_KEYS.add(c["key"])
        CLARITY_ACT_STORIES.append(c)

    # Keep only the 10 MOST RECENT stories — oldest drop off as fresh ones arrive
    CLARITY_ACT_STORIES.sort(key=lambda s: s["dt"], reverse=True)
    del CLARITY_ACT_STORIES[_CLARITY_MAX:]
    kept_keys = {s["key"] for s in CLARITY_ACT_STORIES}
    _CLARITY_SEEN_KEYS.intersection_update(kept_keys)


EXECUTIVES = [
    {"name": "Brad Garlinghouse", "title": "CEO, Ripple", "tab": "BRAD",
     "feed": "https://news.google.com/rss/search?q=Brad+Garlinghouse+XRP+Ripple&hl=en-US&gl=US&ceid=US:en"},
    {"name": "Monica Long", "title": "President, Ripple", "tab": "MONICA",
     "feed": "https://news.google.com/rss/search?q=Monica+Long+Ripple+XRP&hl=en-US&gl=US&ceid=US:en"},
    {"name": "David Schwartz", "title": "CTO, Ripple", "tab": "DAVID",
     "feed": "https://news.google.com/rss/search?q=David+Schwartz+Ripple+XRPL&hl=en-US&gl=US&ceid=US:en"},
    {"name": "Stuart Alderoty", "title": "Chief Legal Officer, Ripple", "tab": "STUART",
     "feed": "https://news.google.com/rss/search?q=Stuart+Alderoty+Ripple+SEC&hl=en-US&gl=US&ceid=US:en"},
]
EXEC_TRACKER = {"stories": [], "updated": None}

def fetch_exec_tracker():
    hdr = {"User-Agent": "XRPComplete/4"}
    now = datetime.now(timezone.utc)
    all_stories = []
    for ex in EXECUTIVES:
        try:
            r = requests.get(ex["feed"], headers=hdr, timeout=8)
            entries = _parse_feed(r.content)
            for e in entries[:4]:
                if not e["title"]:
                    continue
                dt = _parse_date(e["date_str"]) or now
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                all_stories.append({
                    "exec": ex["name"], "exec_title": ex["title"], "tab": ex["tab"],
                    "title": e["title"][:140], "link": e["link"] or "#", "dt": dt,
                })
        except Exception:
            continue
    all_stories.sort(key=lambda s: s["dt"], reverse=True)
    EXEC_TRACKER["stories"] = all_stories[:24]
    EXEC_TRACKER["updated"] = now.strftime("%H:%M UTC")


GITHUB_REPOS = [("XRPLF", "rippled"), ("XRPLF", "xrpl-dev-portal"), ("XRPLF", "xrpl.js")]
GITHUB_DEV = {"commits": [], "stars": 0, "issues": 0, "rippled_7d": 0, "other_7d": 0, "updated": None}

# ── Regulatory & Ledger Watch (V66) — XRPL amendments, SEC EDGAR, Federal Register ──
REG_WATCH = {"amendments": [], "edgar": [], "fedreg": [], "updated": None}

def fetch_reg_watch():
    """Fetch XRPL amendment voting, SEC EDGAR filings, and Federal Register crypto rules.
    All keyless public sources. Failures leave prior data intact."""
    # 1. XRPL Amendments — XRPScan public API
    try:
        r = requests.get("https://api.xrpscan.com/api/v1/amendments",
                         headers={"User-Agent": "Mozilla/5.0 XRPComplete/26"}, timeout=8)
        if r.status_code == 200:
            data = r.json()
            amendments = []
            for a in data:
                if not a.get("enabled", True):  # only pending/voting amendments
                    amendments.append({
                        "name": a.get("name", "Unknown"),
                        "threshold": a.get("threshold", ""),
                        "count": a.get("count", 0),
                        "eta": a.get("eta", ""),
                        "introduced": a.get("introduced", ""),
                    })
            if amendments:
                REG_WATCH["amendments"] = amendments[:8]
    except Exception:
        pass
    # 2. SEC EDGAR full-text search — official government RSS (Ripple mentions)
    try:
        r = requests.get(
            "https://efts.sec.gov/LATEST/search-index?q=%22Ripple%22%20%22XRP%22&dateRange=custom&forms=&output=atom",
            headers={"User-Agent": "XRP Complete admin@xrpcomplete.com"}, timeout=8)
        if r.status_code != 200:
            r = requests.get(
                "https://www.sec.gov/cgi-bin/srqsb?text=form-type%3D8-K+%22XRP%22&first=1&last=20&output=atom",
                headers={"User-Agent": "XRP Complete admin@xrpcomplete.com"}, timeout=8)
        if r.status_code == 200:
            entries = _parse_feed(r.content)
            edgar = []
            for e in entries[:6]:
                if e["title"]:
                    edgar.append({"title": e["title"][:140], "link": e["link"] or "#",
                                  "date": e["date_str"][:16] if e["date_str"] else ""})
            if edgar:
                REG_WATCH["edgar"] = edgar
    except Exception:
        pass
    # 3. Federal Register — official API, documents mentioning digital assets/crypto
    try:
        r = requests.get(
            "https://www.federalregister.gov/api/v1/documents.json?conditions%5Bterm%5D=digital+asset+cryptocurrency&per_page=6&order=newest",
            headers={"User-Agent": "Mozilla/5.0 XRPComplete/26"}, timeout=8)
        if r.status_code == 200:
            docs = r.json().get("results", [])
            fedreg = []
            for d in docs[:6]:
                fedreg.append({
                    "title": (d.get("title") or "")[:140],
                    "link": d.get("html_url") or "#",
                    "date": d.get("publication_date") or "",
                    "type": d.get("type") or "",
                    "agency": (d.get("agencies", [{}])[0].get("name", "") if d.get("agencies") else "")[:40],
                })
            if fedreg:
                REG_WATCH["fedreg"] = fedreg
    except Exception:
        pass
    REG_WATCH["updated"] = datetime.now(timezone.utc).strftime("%H:%M UTC")

def fetch_github_dev():
    hdr = {"Accept": "application/vnd.github.v3+json", "User-Agent": "XRPComplete/4"}
    all_commits = []
    stars = 0
    issues = 0
    for owner, repo in GITHUB_REPOS:
        try:
            r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10",
                              headers=hdr, timeout=10)
            commits = r.json()
            if isinstance(commits, list):
                for c in commits[:6]:
                    cm = c.get("commit", {})
                    au = cm.get("author", {})
                    msg = (cm.get("message") or "")[:90]
                    nl = msg.find("\n")
                    if nl > 0:
                        msg = msg[:nl]
                    all_commits.append({
                        "repo": repo, "msg": msg, "author": (au.get("name") or "")[:30],
                        "date": (au.get("date") or "")[:10], "url": c.get("html_url", ""),
                    })
        except Exception:
            pass
        try:
            r2 = requests.get(f"https://api.github.com/repos/{owner}/{repo}", headers=hdr, timeout=8)
            meta = r2.json()
            stars += int(meta.get("stargazers_count", 0) or 0)
            issues += int(meta.get("open_issues_count", 0) or 0)
        except Exception:
            pass

    all_commits.sort(key=lambda c: c.get("date", ""), reverse=True)
    GITHUB_DEV["commits"] = all_commits[:15]
    GITHUB_DEV["stars"] = stars
    GITHUB_DEV["issues"] = issues
    cutoff = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d")
    recent = [c for c in all_commits if c.get("date", "") >= cutoff]
    GITHUB_DEV["rippled_7d"] = len([c for c in recent if c["repo"] == "rippled"])
    GITHUB_DEV["other_7d"] = len([c for c in recent if c["repo"] != "rippled"])
    GITHUB_DEV["updated"] = datetime.now(timezone.utc).strftime("%H:%M UTC")


def fetch_competitors():
    hdr = {"User-Agent": "XRPComplete/4"}
    for c in COMPETITORS:
        entry = MARKET["competitors"].setdefault(c["id"], {})
        try:
            r = requests.get(f"https://api.coinpaprika.com/v1/tickers/{c['paprika']}", headers=hdr, timeout=8)
            d = r.json()
            q = (d.get("quotes") or {}).get("USD") or {}
            price = float(q.get("price", 0) or 0)
            if price:
                entry["price"] = price
                entry["change_24h"] = float(q.get("percent_change_24h", 0) or 0)
                entry["mcap"] = float(q.get("market_cap", 0) or 0)
        except Exception:
            pass
        try:
            closes = [float(x[4]) for x in _coinbase_candles(c["coinbase"], granularity=86400, limit=10)]
            if len(closes) > 7 and closes[-8]:
                entry["change_7d"] = (closes[-1] - closes[-8]) / closes[-8] * 100
        except Exception:
            pass


def _pearson(x, y):
    n = min(len(x), len(y))
    if n < 5:
        return None
    x, y = x[-n:], y[-n:]
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((x[i] - mx) * (y[i] - my) for i in range(n))
    vx = sum((v - mx) ** 2 for v in x)
    vy = sum((v - my) ** 2 for v in y)
    if vx == 0 or vy == 0:
        return None
    return cov / ((vx * vy) ** 0.5)

def _pct_returns(closes):
    return [(closes[i] - closes[i - 1]) / closes[i - 1] for i in range(1, len(closes)) if closes[i - 1]]

def fetch_correlation():
    def _closes(product_id):
        try:
            candles = _coinbase_candles(product_id, granularity=86400, limit=31)
            return [float(c[4]) for c in candles]
        except Exception:
            return []
    xrp_c = _closes("XRP-USD")
    btc_c = _closes("BTC-USD")
    eth_c = _closes("ETH-USD")
    xrp_r, btc_r, eth_r = _pct_returns(xrp_c), _pct_returns(btc_c), _pct_returns(eth_c)
    if xrp_r and btc_r:
        MARKET["corr_btc"] = _pearson(xrp_r, btc_r)
    if xrp_r and eth_r:
        MARKET["corr_eth"] = _pearson(xrp_r, eth_r)


def fetch_orderbook():
    hdr = {"User-Agent": "XRPComplete/4"}
    try:
        r = requests.get("https://api.exchange.coinbase.com/products/XRP-USD/book",
                          params={"level": 2}, headers=hdr, timeout=8)
        d = r.json()
        bids = [(float(p), float(q)) for p, q, *_ in d.get("bids", [])][:8]
        asks = [(float(p), float(q)) for p, q, *_ in d.get("asks", [])][:8]
        if bids and asks:
            MARKET["ob_bids"] = bids
            MARKET["ob_asks"] = asks
            MARKET["ob_bid_total"] = sum(p * q for p, q in bids)
            MARKET["ob_ask_total"] = sum(p * q for p, q in asks)
    except Exception:
        pass


def fetch_fx():
    hdr = {"User-Agent": "XRPComplete/4"}
    codes = ["EUR", "GBP", "JPY", "AUD", "CAD", "SGD", "INR", "BRL",
             "CHF", "CNY", "KRW", "MXN", "PHP", "NGN", "ZAR", "AED",
             "SAR", "HKD", "NZD", "SEK", "NOK", "TRY", "THB", "IDR",
             "VND", "PLN"]
    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/USD", headers=hdr, timeout=8)
        rates = r.json().get("rates", {})
        if rates:
            MARKET["fx"] = {c: float(rates[c]) for c in codes if c in rates}
            return
    except Exception:
        pass
    try:
        r = requests.get("https://open.er-api.com/v6/latest/USD", headers=hdr, timeout=8)
        rates = r.json().get("rates", {})
        if rates:
            MARKET["fx"] = {c: float(rates[c]) for c in codes if c in rates}
    except Exception:
        pass


def _bg_refresh():
    n = 0
    while True:
        try:
            fetch_market()
            if n % 5 == 0:
                fetch_fx()
                fetch_competitors()
                fetch_correlation()
            if n % 2 == 0:
                fetch_orderbook()
            if n % 60 == 0:  # check hourly whether the 3-day static directory refresh is due
                load_static_partner_directory()
        except Exception:
            pass
        n += 1
        time.sleep(60)

threading.Thread(target=_bg_refresh, daemon=True).start()

def _bg_news():
    n = 0
    while True:
        try:
            fetch_news()
            fetch_exec_tracker()
            fetch_clarity_tracker()
            if n % 2 == 0:
                fetch_github_dev()
            if n % 4 == 0:
                fetch_reg_watch()
        except Exception:
            pass
        n += 1
        time.sleep(300)

threading.Thread(target=_bg_news, daemon=True).start()

def _bg_brief():
    while True:
        try:
            slot_id, _ = _brief_slot(datetime.now(CENTRAL))
            if BRIEF["slot_id"] != slot_id:
                generate_brief()
        except Exception:
            pass
        time.sleep(60)

threading.Thread(target=_bg_brief, daemon=True).start()


# ─────────────────────────────────────────────────────────────────────
# FEAR & GREED — horizontal color-coded line + tinted ball with number
# ─────────────────────────────────────────────────────────────────────
def fng_zone_color(v):
    if v < 25:   return "#ea3943"   # extreme fear  — red
    if v < 45:   return "#ea8c00"   # fear          — orange
    if v < 55:   return "#f3d42f"   # neutral       — yellow
    if v < 75:   return "#93d900"   # greed         — light green
    return "#16c784"                # extreme greed — green

def fng_bar_html(value):
    if value is None:
        return ('<div class="fng-wrap">'
                '<div class="fng-bar"></div>'
                '<div class="fng-ball" style="left:50%;background:#555">--</div>'
                '</div>')
    v = max(0, min(100, int(value)))
    col = fng_zone_color(v)
    return (f'<div class="fng-wrap">'
            f'<div class="fng-bar"></div>'
            f'<div class="fng-ball" style="left:{v}%;background:{col}">{v}</div>'
            f'</div>')


# ─────────────────────────────────────────────────────────────────────
# NEWS FEED (RSS/Atom via stdlib ElementTree — no feedparser dependency)
# ─────────────────────────────────────────────────────────────────────
NEWS_FEEDS = [
    # ── MAJOR CRYPTO NEWS (81 feeds) ─────────────────────────────────────────
    ("CoinDesk",                    "https://www.coindesk.com/arc/outboundfeeds/rss/"),
    ("Decrypt",                     "https://decrypt.co/feed"),
    ("The Block",                   "https://www.theblock.co/rss.xml"),
    ("Blockworks",                  "https://blockworks.co/feed"),
    ("Daily Hodl",                  "https://dailyhodl.com/feed/"),
    ("AMBCrypto",                   "https://ambcrypto.com/feed/"),
    ("BeInCrypto",                  "https://beincrypto.com/feed/"),
    ("NewsBTC",                     "https://www.newsbtc.com/feed/"),
    ("Finbold",                     "https://finbold.com/feed/"),
    ("CryptoSlate",                 "https://cryptoslate.com/feed/"),
    ("CryptoPotato",                "https://cryptopotato.com/feed/"),
    ("ZyCrypto",                    "https://zycrypto.com/feed/"),
    ("Bitcoinist",                  "https://bitcoinist.com/feed/"),
    ("Cryptonews",                  "https://cryptonews.com/news/feed/"),
    ("CoinGape",                    "https://coingape.com/feed/"),
    ("CryptoGlobe",                 "https://www.cryptoglobe.com/latest/feed/"),
    ("Crypto Daily",                "https://cryptodaily.co.uk/feed"),
    ("Invezz",                      "https://invezz.com/feed/"),
    ("InsideBitcoins",              "https://insidebitcoins.com/feed"),
    ("Crypto Briefing",             "https://cryptobriefing.com/feed/"),
    ("The Defiant",                 "https://thedefiant.io/feed"),
    ("Bitcoin Magazine",            "https://bitcoinmagazine.com/feed"),
    ("CoinGecko Blog",              "https://blog.coingecko.com/rss/"),
    ("CoinJournal XRP",             "https://news.google.com/rss/search?q=XRP+ripple+site:coinjournal.net&hl=en-US&gl=US&ceid=US:en"),
    ("99Bitcoins",                  "https://99bitcoins.com/feed/"),
    ("UseTheBitcoin",               "https://usethebitcoin.com/feed/"),
    ("BitcoinExchangeGuide",        "https://bitcoinexchangeguide.com/feed/"),
    ("GN: XRP Futures",             "https://news.google.com/rss/search?q=XRP+futures&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Coinbase2",           "https://news.google.com/rss/search?q=XRP+Coinbase&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Binance2",            "https://news.google.com/rss/search?q=XRP+Binance&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Price Target",        "https://news.google.com/rss/search?q=XRP+price+target&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Technical2",          "https://news.google.com/rss/search?q=XRP+technical+analysis&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Liquidity",           "https://news.google.com/rss/search?q=XRP+liquidity&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CoinDesk2",           "https://news.google.com/rss/search?q=XRP+site:coindesk.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP TheBlock2",           "https://news.google.com/rss/search?q=XRP+site:theblock.co&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Decrypt2",            "https://news.google.com/rss/search?q=XRP+site:decrypt.co&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Market Cap",          "https://news.google.com/rss/search?q=XRP+market+cap&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Bitstamp",            "https://news.google.com/rss/search?q=XRP+Bitstamp&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Blockworks EU",       "https://news.google.com/rss/search?q=XRP+Blockworks&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Altcoin",             "https://news.google.com/rss/search?q=XRP+altcoin+season&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Halving",             "https://news.google.com/rss/search?q=XRP+crypto+halving&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Dominance",           "https://news.google.com/rss/search?q=XRP+dominance&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Volume",              "https://news.google.com/rss/search?q=XRP+trading+volume&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Chart",               "https://news.google.com/rss/search?q=XRP+chart+analysis&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Sentiment",           "https://news.google.com/rss/search?q=XRP+sentiment&hl=en-US&gl=US&ceid=US:en"),
    ("CryptoCompare Global",        "https://news.google.com/rss/search?q=XRP+cryptocompare&hl=en-US&gl=US&ceid=US:en"),
    ("Coinglass Derivatives",       "https://news.google.com/rss/search?q=XRP+coinglass+derivatives&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP LunarCrush",          "https://news.google.com/rss/search?q=XRP+LunarCrush&hl=en-US&gl=US&ceid=US:en"),
    ("Ledger Insights",             "https://ledgerinsights.com/feed/"),
    ("Finextra Finance",            "https://www.finextra.com/rss/headlines.aspx"),
    ("PYMNTS Blockchain",           "https://www.pymnts.com/feed/"),
    ("The Fintech Times",           "https://thefintechtimes.com/feed/"),
    ("GN: XRP Options",             "https://news.google.com/rss/search?q=XRP+options&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Evernode",            "https://news.google.com/rss/search?q=XRP+Evernode&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Sologenic",           "https://news.google.com/rss/search?q=XRP+Sologenic&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP XUMM",                "https://news.google.com/rss/search?q=XRP+XUMM+Xaman&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Hooks",               "https://news.google.com/rss/search?q=XRPL+Hooks&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPL NFT",                "https://news.google.com/rss/search?q=XRPL+NFT&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPL AMM",                "https://news.google.com/rss/search?q=XRPL+AMM&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPL DeFi",               "https://news.google.com/rss/search?q=XRPL+DeFi&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Peersyst",            "https://news.google.com/rss/search?q=XRP+Peersyst&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP WSJ",                 "https://news.google.com/rss/search?q=XRP+site:wsj.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Bloomberg",           "https://news.google.com/rss/search?q=XRP+site:bloomberg.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Reuters",             "https://news.google.com/rss/search?q=XRP+site:reuters.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP FT",                  "https://news.google.com/rss/search?q=XRP+site:ft.com&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP CNBC",                "https://news.google.com/rss/search?q=XRP+site:cnbc.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Forbes",              "https://news.google.com/rss/search?q=XRP+site:forbes.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Fortune",             "https://news.google.com/rss/search?q=XRP+site:fortune.com&hl=en-US&gl=US&ceid=US:en"),
    ("CoinDesk XRP",                "https://news.google.com/rss/search?q=XRP+ripple+site:coindesk.com&hl=en-US&gl=US&ceid=US:en"),
    ("Ledger Insights Direct",      "https://ledgerinsights.com/category/blockchain/feed/"),
    ("Finextra Direct",             "https://www.finextra.com/rss/pressrelease.aspx"),
    ("PYMNTS Direct",               "https://www.pymnts.com/blockchain/feed/"),
    ("Fintech Times Direct",        "https://thefintechtimes.com/category/blockchain/feed/"),
    ("InsideBitcoins Direct",       "https://insidebitcoins.com/category/news/feed"),
    ("UseTheBitcoin Direct",        "https://usethebitcoin.com/category/news/feed/"),
    ("Invezz Crypto Direct",        "https://invezz.com/category/crypto/feed/"),
    ("Bitcoinist XRP Direct",       "https://bitcoinist.com/tag/xrp/feed/"),
    ("NewsBTC XRP Direct",          "https://www.newsbtc.com/tag/xrp/feed/"),
    ("CoinJournal XRP Direct",      "https://news.google.com/rss/search?q=XRP+ripple+coinjournal&hl=en&gl=GB&ceid=GB:en"),
    ("ZyCrypto XRP Direct",         "https://zycrypto.com/tag/xrp/feed/"),
    ("Crypto Daily Direct",         "https://cryptodaily.co.uk/tag/xrp/feed"),
    ("Cointelegraph",               "https://cointelegraph.com/rss"),
    # ── INSTITUTIONAL & BANKING (45 feeds) ───────────────────────────────────
    ("GN: XRP ETF",                 "https://news.google.com/rss/search?q=XRP+ETF&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Bank",                "https://news.google.com/rss/search?q=XRP+bank+partnership&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Custody",             "https://news.google.com/rss/search?q=XRP+crypto+custody&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ETF Latest",          "https://news.google.com/rss/search?q=XRP+ETF+approval+2026&hl=en-US&gl=US&ceid=US:en"),
    ("Coinbase Blog",               "https://www.coinbase.com/blog/landing-page-data/rss"),
    ("GN: XRP Reserve",             "https://news.google.com/rss/search?q=XRP+strategic+reserve&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Custody Bank",        "https://news.google.com/rss/search?q=XRP+bank+custody+institutional&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Spot ETF",            "https://news.google.com/rss/search?q=XRP+spot+ETF&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Futures ETF",         "https://news.google.com/rss/search?q=XRP+futures+ETF&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP BlackRock",           "https://news.google.com/rss/search?q=XRP+BlackRock&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Seeking Alpha",       "https://news.google.com/rss/search?q=XRP+site:seekingalpha.com&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Messari",             "https://news.google.com/rss/search?q=XRP+Messari&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP EU Inst",             "https://news.google.com/rss/search?q=XRP+European+institutional&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Grayscale",           "https://news.google.com/rss/search?q=XRP+Grayscale&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Galaxy",              "https://news.google.com/rss/search?q=XRP+Galaxy+Digital&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Pantera",             "https://news.google.com/rss/search?q=XRP+Pantera+Capital&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP a16z",                "https://news.google.com/rss/search?q=XRP+a16z+andreessen&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ProShares",           "https://news.google.com/rss/search?q=XRP+ProShares&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Franklin",            "https://news.google.com/rss/search?q=XRP+Franklin+Templeton&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Ripple IPO",          "https://news.google.com/rss/search?q=Ripple+IPO&hl=en-US&gl=US&ceid=US:en"),
    ("Santiment Analytics",         "https://news.google.com/rss/search?q=XRP+Santiment+analytics&hl=en-US&gl=US&ceid=US:en"),
    ("Glassnode On-Chain",          "https://news.google.com/rss/search?q=XRP+Glassnode+on-chain&hl=en-US&gl=US&ceid=US:en"),
    ("Messari XRP",                 "https://news.google.com/rss/search?q=XRP+Messari+report&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CryptoQuant",         "https://news.google.com/rss/search?q=XRP+CryptoQuant&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP IntoTheBlock",        "https://news.google.com/rss/search?q=XRP+IntoTheBlock&hl=en-US&gl=US&ceid=US:en"),
    ("GN: BIS XRP Research",        "https://news.google.com/rss/search?q=BIS+XRP+research&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP BIS Research",        "https://news.google.com/rss/search?q=XRP+Bank+International+Settlements&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP IMF",                 "https://news.google.com/rss/search?q=XRP+IMF&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP World Bank",          "https://news.google.com/rss/search?q=XRP+World+Bank&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP JPMorgan",            "https://news.google.com/rss/search?q=XRP+JPMorgan&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Goldman",             "https://news.google.com/rss/search?q=XRP+Goldman+Sachs&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP BlackRock ETF",       "https://news.google.com/rss/search?q=XRP+BlackRock+ETF&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Fidelity",            "https://news.google.com/rss/search?q=XRP+Fidelity&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Nasdaq",              "https://news.google.com/rss/search?q=XRP+Nasdaq&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Nansen",              "https://news.google.com/rss/search?q=XRP+Nansen&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Chainalysis",         "https://news.google.com/rss/search?q=XRP+Chainalysis&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Coin Metrics",        "https://news.google.com/rss/search?q=XRP+CoinMetrics&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Token Terminal",      "https://news.google.com/rss/search?q=XRP+Token+Terminal&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Dune Analytics",      "https://news.google.com/rss/search?q=XRP+Dune+Analytics&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CME",                 "https://news.google.com/rss/search?q=XRP+CME+futures&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Wintermute",          "https://news.google.com/rss/search?q=XRP+Wintermute&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Cumberland",          "https://news.google.com/rss/search?q=XRP+Cumberland+DRW&hl=en-US&gl=US&ceid=US:en"),
    ("Santiment Blog",              "https://santiment.net/blog/feed/"),
    ("GN: XRP Seeking Alpha 2",     "https://news.google.com/rss/search?q=Ripple+XRP+seekingalpha&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Motley Fool",         "https://news.google.com/rss/search?q=XRP+Motley+Fool&hl=en-US&gl=US&ceid=US:en"),
    # ── LEGAL & REGULATORY (36 feeds) ────────────────────────────────────────
    ("GN: XRP Legal",               "https://news.google.com/rss/search?q=XRP+legal+ruling&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Congress",            "https://news.google.com/rss/search?q=XRP+Congress+crypto+legislation&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CFTC",                "https://news.google.com/rss/search?q=XRP+CFTC&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP OCC",                 "https://news.google.com/rss/search?q=XRP+OCC&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Treasury",            "https://news.google.com/rss/search?q=XRP+US+Treasury&hl=en-US&gl=US&ceid=US:en"),
    ("Crypto Slate SEC",            "https://cryptoslate.com/tag/sec/feed/"),
    ("GN: Crypto Act",              "https://news.google.com/rss/search?q=crypto+legislation+act+2026&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP SEC Update",          "https://news.google.com/rss/search?q=XRP+SEC+update&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Crypto Tax US",           "https://news.google.com/rss/search?q=crypto+tax+IRS+2026&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP OCC Reg",             "https://news.google.com/rss/search?q=XRP+OCC+regulation&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Treasury 2",          "https://news.google.com/rss/search?q=Ripple+Treasury+crypto+policy&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP MiCA EU",             "https://news.google.com/rss/search?q=XRP+MiCA+Europe&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP UK FCA",              "https://news.google.com/rss/search?q=XRP+FCA+UK&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Germany",             "https://news.google.com/rss/search?q=XRP+Germany+BaFin&hl=de&gl=DE&ceid=DE:de"),
    ("GN: XRP France",              "https://news.google.com/rss/search?q=XRP+France+AMF&hl=fr&gl=FR&ceid=FR:fr"),
    ("GN: XRP Netherlands",         "https://news.google.com/rss/search?q=XRP+Netherlands+DNB&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Korea Reg",           "https://news.google.com/rss/search?q=XRP+Korea+FSC+regulation&hl=ko&gl=KR&ceid=KR:ko"),
    ("GN: XRP Japan FSA",           "https://news.google.com/rss/search?q=XRP+Japan+FSA&hl=ja&gl=JP&ceid=JP:ja"),
    ("GN: XRP Congress 2",          "https://news.google.com/rss/search?q=XRP+Senate+House+crypto+bill&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Gensler",             "https://news.google.com/rss/search?q=XRP+SEC+crypto+regulation&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP FDIC",                "https://news.google.com/rss/search?q=XRP+FDIC+crypto&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP White House",         "https://news.google.com/rss/search?q=XRP+White+House+crypto+policy&hl=en-US&gl=US&ceid=US:en"),
    ("VARA Dubai Reg",              "https://news.google.com/rss/search?q=VARA+Dubai+crypto+regulation&hl=en&gl=AE&ceid=AE:en"),
    ("ADGM Abu Dhabi",              "https://news.google.com/rss/search?q=ADGM+Abu+Dhabi+crypto&hl=en&gl=AE&ceid=AE:en"),
    ("SEC Press Releases",          "https://news.google.com/rss/search?q=SEC+crypto+press+release&hl=en-US&gl=US&ceid=US:en"),
    ("GN: SEC Crypto XRP",          "https://news.google.com/rss/search?q=SEC+XRP+crypto+enforcement&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Federal Reserve",     "https://news.google.com/rss/search?q=XRP+Federal+Reserve+CBDC&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ECB Digital",         "https://news.google.com/rss/search?q=XRP+ECB+digital+euro&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP FinCEN",              "https://news.google.com/rss/search?q=XRP+FinCEN&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CFTC Crypto",         "https://news.google.com/rss/search?q=CFTC+crypto+XRP+commodity&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP OCC Bank",            "https://news.google.com/rss/search?q=OCC+bank+crypto+XRP&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP UK FCA 2",            "https://news.google.com/rss/search?q=XRP+FCA+UK+crypto+regulation&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP MAS Singapore",       "https://news.google.com/rss/search?q=XRP+MAS+Singapore&hl=en&gl=SG&ceid=SG:en"),
    ("GN: XRP ASIC Australia",      "https://news.google.com/rss/search?q=XRP+ASIC+Australia&hl=en&gl=AU&ceid=AU:en"),
    ("GN: XRP FSA Japan Reg",       "https://news.google.com/rss/search?q=XRP+FSA+Japan+regulation&hl=ja&gl=JP&ceid=JP:ja"),
    ("GN: XRP FATF",                "https://news.google.com/rss/search?q=XRP+FATF+crypto&hl=en&gl=GB&ceid=GB:en"),
    # ── INTERNATIONAL & REGIONAL (82 feeds) ──────────────────────────────────
    ("GN: XRP SBI",                 "https://news.google.com/rss/search?q=XRP+SBI+Ripple&hl=ja&gl=JP&ceid=JP:ja"),
    ("CoinPost Japan",              "https://coinpost.jp/?feed=rss2"),
    ("CoinPost JP All",             "https://coinpost.jp/feed/"),
    ("Crypto Times JP",             "https://crypto-times.jp/feed/"),
    ("GN Japan XRP",                "https://news.google.com/rss/search?q=XRP+%E3%83%AA%E3%83%83%E3%83%97%E3%83%AB&hl=ja&gl=JP&ceid=JP:ja"),
    ("GN Japan XRP EN",             "https://news.google.com/rss/search?q=XRP+Japan+Ripple&hl=en-US&gl=US&ceid=US:en"),
    ("CoinPost JP XRP",             "https://coinpost.jp/tag/xrp/feed/"),
    ("CoinDesk Japan",              "https://news.google.com/rss/search?q=XRP+CoinDesk+Japan&hl=ja&gl=JP&ceid=JP:ja"),
    ("GN Korea XRP",                "https://news.google.com/rss/search?q=XRP+%EB%A6%AC%ED%94%8C&hl=ko&gl=KR&ceid=KR:ko"),
    ("GN Korea XRP EN",             "https://news.google.com/rss/search?q=XRP+Korea+Ripple&hl=en-US&gl=US&ceid=US:en"),
    ("Decenter KR",                 "https://news.google.com/rss/search?q=XRP+decenter+korea&hl=ko&gl=KR&ceid=KR:ko"),
    ("GN UAE XRP",                  "https://news.google.com/rss/search?q=XRP+UAE+Ripple&hl=en&gl=AE&ceid=AE:en"),
    ("GN ME Crypto",                "https://news.google.com/rss/search?q=XRP+Middle+East+crypto&hl=en&gl=AE&ceid=AE:en"),
    ("Rain Financial ME",           "https://news.google.com/rss/search?q=XRP+Rain+Financial+Bahrain&hl=en&gl=AE&ceid=AE:en"),
    ("VARA Dubai Reg 2",            "https://news.google.com/rss/search?q=VARA+Dubai+XRP+crypto&hl=en&gl=AE&ceid=AE:en"),
    ("ADGM Abu Dhabi 2",            "https://news.google.com/rss/search?q=ADGM+XRP+Abu+Dhabi&hl=en&gl=AE&ceid=AE:en"),
    ("GN Europe XRP",               "https://news.google.com/rss/search?q=XRP+Europe+Ripple&hl=en&gl=GB&ceid=GB:en"),
    ("GN UK XRP",                   "https://news.google.com/rss/search?q=XRP+UK+Ripple&hl=en&gl=GB&ceid=GB:en"),
    ("BTC Echo DE",                 "https://www.btc-echo.de/feed/"),
    ("CoinTelegraph DE",            "https://de.cointelegraph.com/rss"),
    ("CoinTelegraph IT",            "https://it.cointelegraph.com/rss"),
    ("CoinTelegraph FR",            "https://fr.cointelegraph.com/rss"),
    ("ForkLog Eastern EU",          "https://forklog.com/feed/"),
    ("GN India XRP",                "https://news.google.com/rss/search?q=XRP+India+Ripple&hl=en&gl=IN&ceid=IN:en"),
    ("WazirX Blog",                 "https://wazirx.com/blog/feed/"),
    ("Coinpedia",                   "https://coinpedia.org/feed/"),
    ("CoinDCX India",               "https://coindcx.com/blog/feed/"),
    ("GN LatAm XRP",                "https://news.google.com/rss/search?q=XRP+Ripple+Latin+America&hl=es&gl=MX&ceid=MX:es"),
    ("CriptoNoticias",              "https://www.criptonoticias.com/feed/"),
    ("Diario Bitcoin",              "https://www.diariobitcoin.com/feed/"),
    ("Bitso Blog LatAm",            "https://blog.bitso.com/feed/"),
    ("GN Africa XRP",               "https://news.google.com/rss/search?q=XRP+Africa+Ripple&hl=en&gl=ZA&ceid=ZA:en"),
    ("Bitmama Africa",              "https://news.google.com/rss/search?q=XRP+Bitmama+Africa+crypto&hl=en&gl=ZA&ceid=ZA:en"),
    ("Yellow Card Africa",          "https://news.google.com/rss/search?q=XRP+Yellow+Card+Africa&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN SEA XRP",                  "https://news.google.com/rss/search?q=XRP+Southeast+Asia+Ripple&hl=en&gl=SG&ceid=SG:en"),
    ("Forkast Asia",                "https://forkast.news/feed/"),
    ("HashKey Exchange",            "https://news.google.com/rss/search?q=XRP+HashKey+Exchange&hl=en&gl=SG&ceid=SG:en"),
    ("Indodax Indonesia",           "https://news.google.com/rss/search?q=XRP+Indodax+Indonesia&hl=id&gl=ID&ceid=ID:id"),
    ("Tokocrypto Indonesia",        "https://news.google.com/rss/search?q=XRP+Tokocrypto+Indonesia&hl=id&gl=ID&ceid=ID:id"),
    ("CoinJar News",                "https://news.google.com/rss/search?q=XRP+CoinJar+Australia&hl=en&gl=AU&ceid=AU:en"),
    ("BTC Markets Australia",       "https://news.google.com/rss/search?q=XRP+BTC+Markets+Australia&hl=en&gl=AU&ceid=AU:en"),
    ("BlockTempo Taiwan",           "https://news.google.com/rss/search?q=XRP+BlockTempo+Taiwan&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"),
    ("GN: XRP Australia",           "https://news.google.com/rss/search?q=XRP+Australia+Ripple&hl=en&gl=AU&ceid=AU:en"),
    ("GN: XRP Hong Kong",           "https://news.google.com/rss/search?q=XRP+Hong+Kong&hl=en&gl=HK&ceid=HK:en"),
    ("GN: XRP Taiwan",              "https://news.google.com/rss/search?q=XRP+Taiwan+ripple&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"),
    ("GN: XRP Indonesia",           "https://news.google.com/rss/search?q=XRP+Indonesia+Ripple&hl=id&gl=ID&ceid=ID:id"),
    ("GN: XRP Malaysia",            "https://news.google.com/rss/search?q=XRP+Malaysia+Ripple&hl=en&gl=MY&ceid=MY:en"),
    ("GN: XRP Philippines",         "https://news.google.com/rss/search?q=XRP+Philippines+Ripple&hl=en&gl=PH&ceid=PH:en"),
    ("GN: XRP Thailand",            "https://news.google.com/rss/search?q=XRP+Thailand+Ripple&hl=th&gl=TH&ceid=TH:th"),
    ("GN: XRP Vietnam",             "https://news.google.com/rss/search?q=XRP+Vietnam+Ripple&hl=vi&gl=VN&ceid=VN:vi"),
    ("GN: XRP Brazil",              "https://news.google.com/rss/search?q=XRP+Brasil+Ripple&hl=pt-BR&gl=BR&ceid=BR:pt-419"),
    ("GN: XRP Mexico",              "https://news.google.com/rss/search?q=XRP+Mexico+Ripple&hl=es&gl=MX&ceid=MX:es"),
    ("GN: XRP Argentina 1",         "https://news.google.com/rss/search?q=XRP+Argentina+Ripple&hl=es&gl=AR&ceid=AR:es"),
    ("GN: XRP Colombia 1",          "https://news.google.com/rss/search?q=XRP+Colombia+Ripple&hl=es&gl=CO&ceid=CO:es"),
    ("GN: XRP Nigeria",             "https://news.google.com/rss/search?q=XRP+Nigeria+Ripple&hl=en&gl=NG&ceid=NG:en"),
    ("GN: XRP Kenya 1",             "https://news.google.com/rss/search?q=XRP+Kenya+Ripple&hl=en&gl=KE&ceid=KE:en"),
    ("GN: XRP South Africa 1",      "https://news.google.com/rss/search?q=XRP+South+Africa+Ripple&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN: XRP Ghana 1",             "https://news.google.com/rss/search?q=XRP+Ghana+Ripple&hl=en&gl=GH&ceid=GH:en"),
    ("GN: XRP Ethiopia",            "https://news.google.com/rss/search?q=XRP+Ethiopia+crypto&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN: XRP Morocco",             "https://news.google.com/rss/search?q=XRP+Morocco+crypto&hl=fr&gl=MA&ceid=MA:fr"),
    ("GN: XRP Saudi",               "https://news.google.com/rss/search?q=XRP+Saudi+Arabia+Ripple&hl=en&gl=SA&ceid=SA:en"),
    ("GN: XRP Bahrain 1",           "https://news.google.com/rss/search?q=XRP+Bahrain+crypto&hl=en&gl=AE&ceid=AE:en"),
    ("GN: XRP Israel 1",            "https://news.google.com/rss/search?q=XRP+Israel+crypto&hl=en&gl=IL&ceid=IL:en"),
    ("GN: XRP Pakistan 1",          "https://news.google.com/rss/search?q=XRP+Pakistan+Ripple&hl=en&gl=IN&ceid=IN:en"),
    ("GN: XRP Bangladesh 1",        "https://news.google.com/rss/search?q=XRP+Bangladesh+crypto&hl=en&gl=IN&ceid=IN:en"),
    ("GN: XRP Poland",              "https://news.google.com/rss/search?q=XRP+Poland+crypto&hl=pl&gl=PL&ceid=PL:pl"),
    ("GN: XRP Spain",               "https://news.google.com/rss/search?q=XRP+Spain+Ripple&hl=es&gl=ES&ceid=ES:es"),
    ("GN: XRP Switzerland",         "https://news.google.com/rss/search?q=XRP+Switzerland+FINMA&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP ECB",                 "https://news.google.com/rss/search?q=XRP+ECB+European+Central+Bank&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Scandinavia",         "https://news.google.com/rss/search?q=XRP+Scandinavia+Nordic+crypto&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP UK Adoption",         "https://news.google.com/rss/search?q=XRP+UK+adoption+Ripple&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Germany 2",           "https://news.google.com/rss/search?q=XRP+Deutschland+Krypto&hl=de&gl=DE&ceid=DE:de"),
    ("GN: XRP France 2",            "https://news.google.com/rss/search?q=XRP+France+crypto&hl=fr&gl=FR&ceid=FR:fr"),
    ("GN: XRP Netherlands 2",       "https://news.google.com/rss/search?q=XRP+Netherlands+crypto&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP Japan Bank",          "https://news.google.com/rss/search?q=XRP+Japan+bank+SBI&hl=ja&gl=JP&ceid=JP:ja"),
    ("GN: XRP Turkey 1",            "https://news.google.com/rss/search?q=XRP+Turkey+crypto&hl=tr&gl=TR&ceid=TR:tr"),
    ("GN: XRP Egypt",               "https://news.google.com/rss/search?q=XRP+Egypt+crypto&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN: XRP Argentina 2",         "https://news.google.com/rss/search?q=XRP+Argentina+crypto+2026&hl=es&gl=AR&ceid=AR:es"),
    ("GN: XRP Colombia 2",          "https://news.google.com/rss/search?q=XRP+Colombia+crypto&hl=es&gl=CO&ceid=CO:es"),
    ("GN: XRP Chile",               "https://news.google.com/rss/search?q=XRP+Chile+crypto&hl=es&gl=CL&ceid=CL:es"),
    ("GN: XRP South Africa 2",      "https://news.google.com/rss/search?q=XRP+South+Africa+crypto&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN: XRP Kenya 2",             "https://news.google.com/rss/search?q=XRP+Kenya+crypto&hl=en&gl=KE&ceid=KE:en"),
    ("GN: XRP Tanzania",            "https://news.google.com/rss/search?q=XRP+Tanzania+crypto&hl=en&gl=ZA&ceid=ZA:en"),
    ("GN: XRP Ghana 2",             "https://news.google.com/rss/search?q=XRP+Ghana+crypto&hl=en&gl=GH&ceid=GH:en"),
    ("GN: XRP Vietnam 2",           "https://news.google.com/rss/search?q=XRP+Vietnam+crypto&hl=vi&gl=VN&ceid=VN:vi"),
    ("GN: XRP Thailand 2",          "https://news.google.com/rss/search?q=XRP+Thailand+crypto&hl=th&gl=TH&ceid=TH:th"),
    ("GN: XRP Pakistan 2",          "https://news.google.com/rss/search?q=XRP+Pakistan+crypto&hl=en&gl=IN&ceid=IN:en"),
    ("GN: XRP Bangladesh 2",        "https://news.google.com/rss/search?q=XRP+Bangladesh+Ripple&hl=en&gl=IN&ceid=IN:en"),
    ("GN: XRP Bahrain 2",           "https://news.google.com/rss/search?q=XRP+Bahrain+Ripple&hl=en&gl=AE&ceid=AE:en"),
    ("GN: XRP Israel 2",            "https://news.google.com/rss/search?q=XRP+Israel+Ripple&hl=en&gl=IL&ceid=IL:en"),
    # ── ECOSYSTEM & TECHNICAL (22 feeds) ─────────────────────────────────────
    ("GN: XRP Adoption",            "https://news.google.com/rss/search?q=XRP+adoption+use+case&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ODL",                 "https://news.google.com/rss/search?q=XRP+ODL+on-demand+liquidity&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ISO 20022",           "https://news.google.com/rss/search?q=XRP+ISO+20022&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CBDC",                "https://news.google.com/rss/search?q=XRP+CBDC+central+bank&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Partnership",         "https://news.google.com/rss/search?q=XRP+Ripple+partnership&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Payment",             "https://news.google.com/rss/search?q=XRP+payment+cross-border&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Fintech",             "https://news.google.com/rss/search?q=XRP+fintech+integration&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Ripple CBDC",             "https://news.google.com/rss/search?q=Ripple+CBDC+platform&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP RippleNet",           "https://news.google.com/rss/search?q=RippleNet+XRP&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP ISO 20022 2",         "https://news.google.com/rss/search?q=XRP+ISO20022+payment+rails&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPL Dev",                "https://news.google.com/rss/search?q=XRPL+developer+update&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPL Tech",               "https://news.google.com/rss/search?q=XRPL+technical+upgrade&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP DeFi",                "https://news.google.com/rss/search?q=XRP+DeFi&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Web3 DeFi",           "https://news.google.com/rss/search?q=XRPL+Web3+DeFi&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP NFT Gaming",          "https://news.google.com/rss/search?q=XRPL+NFT+gaming&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Validator",           "https://news.google.com/rss/search?q=XRPL+validator+node&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP EU Banking",          "https://news.google.com/rss/search?q=XRP+European+banking+integration&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP UK Adoption 2",       "https://news.google.com/rss/search?q=XRP+UK+fintech+adoption&hl=en&gl=GB&ceid=GB:en"),
    ("GN: XRP EVM Sidechain",       "https://news.google.com/rss/search?q=XRPL+EVM+sidechain&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP AMM Liquidity",       "https://news.google.com/rss/search?q=XRPL+AMM+liquidity+DEX&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Stablecoin Tech",     "https://news.google.com/rss/search?q=RLUSD+stablecoin+XRPL&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Tokenization",        "https://news.google.com/rss/search?q=XRP+tokenization+RWA&hl=en-US&gl=US&ceid=US:en"),
    # ── OFFICIAL RIPPLE SOURCES (9 feeds) ────────────────────────────────────
    ("Ripple Insights",             "https://ripple.com/insights/feed/"),
    ("XRPL.org Blog",               "https://xrpl.org/blog/feed.xml"),
    ("GN: Garlinghouse",            "https://news.google.com/rss/search?q=Brad+Garlinghouse+XRP+Ripple&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Ripple CEO",              "https://news.google.com/rss/search?q=Ripple+CEO+XRP&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Brad Interview",          "https://news.google.com/rss/search?q=Brad+Garlinghouse+interview&hl=en-US&gl=US&ceid=US:en"),
    ("GN: David Schwartz",          "https://news.google.com/rss/search?q=David+Schwartz+Ripple+XRPL&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Monica Long",             "https://news.google.com/rss/search?q=Monica+Long+Ripple+XRP&hl=en-US&gl=US&ceid=US:en"),
    ("GN: Ripple Labs",             "https://news.google.com/rss/search?q=Ripple+Labs+XRP&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRPLF",                   "https://news.google.com/rss/search?q=XRP+Ledger+Foundation&hl=en-US&gl=US&ceid=US:en"),
    # ── XRP PRICE & MARKET (9 feeds) ─────────────────────────────────────────
    ("U.Today XRP",                 "https://u.today/rss"),
    ("Crypto News Flash",           "https://www.crypto-news-flash.com/feed/"),
    ("XRP News CoinTele",           "https://cointelegraph.com/tags/xrp/feed"),
    ("CryptoSlate XRP",             "https://cryptoslate.com/tag/xrp/feed/"),
    ("GN: RLUSD",                   "https://news.google.com/rss/search?q=RLUSD+Ripple+stablecoin&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Price",               "https://news.google.com/rss/search?q=XRP+price+prediction&hl=en-US&gl=US&ceid=US:en"),
    ("Crypto Potato XRP",           "https://cryptopotato.com/tag/xrp/feed/"),
    ("Crypto Slate Ripple",         "https://cryptoslate.com/tag/ripple/feed/"),
    ("GN: XRP Stablecoin",          "https://news.google.com/rss/search?q=XRP+stablecoin+RLUSD&hl=en-US&gl=US&ceid=US:en"),
    # ── WHALE & AGGREGATOR (3 feeds) ─────────────────────────────────────────
    ("GN: XRP Whale",               "https://news.google.com/rss/search?q=XRP+whale+transaction&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Ripple Aggregator",   "https://news.google.com/rss/search?q=XRP+Ripple+news&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Breaking",            "https://news.google.com/rss/search?q=XRP+breaking+news&hl=en-US&gl=US&ceid=US:en"),
    # ── COMMUNITY (6 feeds) ──────────────────────────────────────────────────
    ("Reddit r/Ripple",             "https://www.reddit.com/r/Ripple/.rss"),
    ("Reddit r/XRP",                "https://www.reddit.com/r/XRP/.rss"),
    ("Reddit r/XRPTrader",          "https://www.reddit.com/r/XRPTrader/.rss"),
    ("Reddit r/CryptoCurr",         "https://www.reddit.com/r/CryptoCurrency/.rss"),
    ("Reddit r/XRPtrader 2",        "https://www.reddit.com/r/xrptrader/.rss"),
    ("Reddit r/Ripple 2",           "https://www.reddit.com/r/ripple/.rss"),
    # ── MAINSTREAM MEDIA XRP (12 feeds) ──────────────────────────────────────
    ("Forbes Crypto",               "https://www.forbes.com/crypto-blockchain/feed/"),
    ("Yahoo Finance Crypto",        "https://finance.yahoo.com/news/rssindex"),
    ("GN: XRP Reuters 2",           "https://news.google.com/rss/search?q=XRP+Reuters&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Bloomberg 2",         "https://news.google.com/rss/search?q=XRP+Bloomberg&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP CNBC 2",              "https://news.google.com/rss/search?q=XRP+CNBC&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP WSJ 2",               "https://news.google.com/rss/search?q=XRP+Wall+Street+Journal&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Forbes 2",            "https://news.google.com/rss/search?q=XRP+Forbes&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Fortune 2",           "https://news.google.com/rss/search?q=XRP+Fortune+magazine&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP AP News",             "https://news.google.com/rss/search?q=XRP+AP+News&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Nasdaq 2",            "https://news.google.com/rss/search?q=XRP+Nasdaq+listing&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Fed Policy",          "https://news.google.com/rss/search?q=XRP+Federal+Reserve+policy&hl=en-US&gl=US&ceid=US:en"),
    ("GN: XRP Inflation",           "https://news.google.com/rss/search?q=XRP+inflation+hedge&hl=en-US&gl=US&ceid=US:en"),
]

NEWS = {"current": [], "weekly": [], "pool": [], "feeds_active": 0, "feeds_total": len(NEWS_FEEDS), "updated": None}

# Regions (match Iteration-1) for Regional Discourse + Global Pulse signals
REGIONS = ["Japan", "Korea", "UAE", "Europe", "India", "LatAm", "Africa", "SEA"]
REGION_FLAGS = {"Japan": "\U0001F1EF\U0001F1F5", "Korea": "\U0001F1F0\U0001F1F7", "UAE": "\U0001F1E6\U0001F1EA",
                "Europe": "\U0001F1EA\U0001F1FA", "India": "\U0001F1EE\U0001F1F3", "LatAm": "\U0001F30E",
                "Africa": "\U0001F30D", "SEA": "\U0001F30F"}
REGION_KEYWORDS = {
    "Japan":  ["japan", "japanese", "sbi", "bitflyer", "coincheck", "jpn", "yen"],
    "Korea":  ["korea", "korean", "upbit", "bithumb", "coinone", "korbit", "krw"],
    "UAE":    ["uae", "dubai", "abu dhabi", "emirates", "difc", "vara", "middle east"],
    "Europe": ["europe", "european", " eu ", "mica", "ecb", " uk ", "britain", "germany", "france", "swiss", "spain"],
    "India":  ["india", "indian", "wazirx", "coinswitch", "coindcx", "inr", "sebi", "rbi"],
    "LatAm":  ["latin", "latam", "mexico", "brazil", "argentina", "colombia", "peru", "chile", "bitso"],
    "Africa": ["africa", "nigeria", "kenya", "south africa", "ghana", "ethiopia", "naira"],
    "SEA":    ["singapore", "thailand", "vietnam", "philippines", "indonesia", "malaysia", "tranglo"],
}
US_KEYWORDS = {"sec", "cftc", "etf", "congress", "senate", "white house", "united states",
               "nasdaq", "blackrock", "fidelity", "treasury", "washington", "u.s.", "american"}

def _classify_region(text_low):
    for region, kws in REGION_KEYWORDS.items():
        if any(kw in text_low for kw in kws):
            return region
    return None

_BULLISH = {"surge","surges","rally","rallies","soar","soars","jump","jumps","gain","gains",
            "bullish","approved","approval","win","wins","victory","adoption","partnership",
            "breakout","launch","launches","integration","etf","upgrade","record","high","boost"}
_BEARISH = {"crash","crashes","plunge","plunges","plummet","drop","drops","fall","falls","dump",
            "bearish","lawsuit","warning","hack","hacked","selloff","decline","declines","fud",
            "dip","fine","sued","delay","rejected","ban","risk","fear"}
_IMPORTANT = {"sec","etf","ruling","settlement","partnership","ripple","swift","billion",
              "approved","launch","lawsuit","court","bank","institutional","cbdc","blackrock",
              "nasdaq","fidelity","tokenization","rlusd","custody"}
_SOURCE_WEIGHT = {"CoinDesk":5,"Cointelegraph":5,"Decrypt":4,"The Daily Hodl":3,"U.Today":3,
                  "CryptoSlate":3,"Bitcoinist":2,"NewsBTC":2,"CryptoPotato":2,"AMBCrypto":2}


def _ln(tag):
    return tag.split('}')[-1] if '}' in tag else tag

def _parse_feed(content):
    root = ET.fromstring(content)
    out = []
    for node in root.iter():
        if _ln(node.tag) in ("item", "entry"):
            title = link = date_str = summary = ""
            for ch in node:
                c = _ln(ch.tag)
                if c == "title":
                    title = (ch.text or "").strip()
                elif c == "link":
                    if ch.text and ch.text.strip():
                        link = ch.text.strip()
                    elif ch.get("href"):
                        link = ch.get("href")
                elif c in ("pubDate", "published", "updated", "date") and not date_str:
                    date_str = (ch.text or "").strip()
                elif c in ("description", "summary", "content") and not summary:
                    summary = (ch.text or "")
            out.append({"title": title, "link": link, "date_str": date_str, "summary": summary})
    return out

def _parse_date(s):
    if not s:
        return None
    try:
        return parsedate_to_datetime(s)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            pass
    return None

def _sentiment(text):
    t = text.lower()
    b = sum(1 for w in _BULLISH if w in t)
    r = sum(1 for w in _BEARISH if w in t)
    if b > r:
        return "bullish"
    if r > b:
        return "bearish"
    return "neutral"

def _influence(text, source):
    kw = sum(1 for w in _IMPORTANT if w in text.lower())
    return _SOURCE_WEIGHT.get(source, 1) * 2 + kw * 3

_BREAKING_KW = {"breaking", "just in", "urgent", "alert", "confirmed", "official"}

def _category(text):
    t = text.lower()
    if any(k in t for k in ["whale", "million xrp", "billion xrp", "large transfer", "moved xrp"]):
        return "Whale"
    if any(k in t for k in ["sec", "court", "lawsuit", "ruling", "settlement", "judge", "legal", "appeal"]):
        return "Legal"
    if any(k in t for k in ["regulat", "mica", "cftc", "policy", "license", "compliance", "sanction"]):
        return "Reg"
    if any(k in t for k in ["rlusd", "amm", "defi", "partnership", "tokeniz", "stablecoin", "adoption", "nft", "ecosystem"]):
        return "Ecosystem"
    if any(k in t for k in ["xrpl", "ledger", "upgrade", "hooks", "evm", "validator", "amendment"]):
        return "Tech"
    if any(k in t for k in ["price", "surge", "rally", "dump", "plunge", "target", "forecast", "breakout"]):
        return "Price"
    return "General"

def _is_foreign(text):
    if not text:
        return False
    non_ascii = sum(1 for c in text if ord(c) > 127)
    return (non_ascii / max(len(text), 1)) > 0.12

def _is_breaking(text, influence):
    return any(k in text.lower() for k in _BREAKING_KW) or influence >= 22

def _clean_summary(raw, limit=240):
    if not raw:
        return ""
    txt = re.sub(r"<[^>]+>", "", raw)          # strip HTML tags
    txt = re.sub(r"\s+", " ", txt).strip()      # collapse whitespace
    if len(txt) > limit:
        txt = txt[:limit].rsplit(" ", 1)[0] + "\u2026"
    return txt

def _translate_url(link):
    return "https://translate.google.com/translate?sl=auto&tl=en&u=" + html.escape(link, quote=True)

def _fetch_one_feed(name, url):
    """Fetch a single feed via network only. No shared state. Thread-safe."""
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 XRPComplete/26"}, timeout=6)
        if r.status_code != 200:
            return name, []
        return name, _parse_feed(r.content)
    except Exception:
        return name, []

def fetch_news():
    now = datetime.now(timezone.utc)
    active = 0
    seen = set()
    pool = []
    # Fetch all feeds in parallel — network I/O only, no shared state in threads
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(_fetch_one_feed, name, url): name for name, url in NEWS_FEEDS}
        results = {}
        for future in as_completed(futures):
            name, entries = future.result()
            results[name] = entries
    # Process results serially — all state updates single-threaded
    for name, url in NEWS_FEEDS:
        entries = results.get(name, [])
        got = False
        for e in entries:
            title = e["title"]
            if not title:
                continue
            text = title + " " + e["summary"]
            low = text.lower()
            if "xrp" not in low and "ripple" not in low and "\u30ea\u30c3\u30d7\u30eb" not in text:
                continue
            key = title.lower()[:80]
            if key in seen:
                continue
            seen.add(key)
            dt = _parse_date(e["date_str"]) or now
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            infl = _influence(text, name)
            summary = _clean_summary(e["summary"])
            pool.append({
                "key": key, "title": title, "link": e["link"] or "#", "source": name, "dt": dt,
                "sentiment": _sentiment(text), "influence": infl,
                "region": _classify_region(low),
                "summary": summary,
                "category": _category(title + " " + summary),
                "foreign": _is_foreign(title),
                "breaking": _is_breaking(text, infl),
            })
            got = True
        if got:
            active += 1

    NEWS["pool"] = pool
    # Influential = the week's 20 most influential (takes priority so it always fills to 20)
    week_ago = now.timestamp() - 7 * 86400
    weekly_pool = [s for s in pool if s["dt"].timestamp() >= week_ago]
    NEWS["weekly"] = sorted(weekly_pool, key=lambda s: (s["influence"], s["dt"].timestamp()), reverse=True)[:20]
    weekly_keys = {s["key"] for s in NEWS["weekly"]}
    # Current = the 20 most recent, EXCLUDING anything already in Influential (no overlap)
    NEWS["current"] = [s for s in sorted(pool, key=lambda s: s["dt"], reverse=True)
                       if s["key"] not in weekly_keys][:20]
    NEWS["feeds_active"] = active
    NEWS["updated"] = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    _track_sentiment_history(pool)
    _track_news_volume(pool)
    _detect_partnership_deals(pool)
    _track_catalyst_clock(pool)
    _track_narrative_diffusion(pool)


# ── Narrative Diffusion Map — how fast a theme spreads from first mention to full regional coverage ──
# Reuses the existing theme keywords (Intelligence Brief) and region tags (news engine) already computed
# per story. Persistent accumulator, builds up honestly over time.
NARRATIVE_DIFFUSION = {}   # theme -> {"first_seen": dt, "regions": {region: dt_first_seen_in_region}}
_DIFFUSION_SEEN_KEYS = set()

def _track_narrative_diffusion(pool):
    for s in pool:
        key = s["key"]
        if key in _DIFFUSION_SEEN_KEYS:
            continue
        text = (s["title"] + " " + s.get("summary", "")).lower()
        matched = [name for name, kws in _BRIEF_THEMES.items() if any(kw in text for kw in kws)]
        if not matched:
            continue
        _DIFFUSION_SEEN_KEYS.add(key)
        dt = s["dt"]
        region = s.get("region")
        for theme in matched:
            entry = NARRATIVE_DIFFUSION.setdefault(theme, {"first_seen": dt, "regions": {}})
            if dt < entry["first_seen"]:
                entry["first_seen"] = dt
            if region:
                if region not in entry["regions"] or dt < entry["regions"][region]:
                    entry["regions"][region] = dt


# ── Catalyst Clock — when XRP-moving stories actually break (hour x weekday, UTC) ──
# Persistent accumulator, builds up honestly over time. Counts only stories already
# flagged "breaking" by the existing classifier -- no new definition of "significant" invented.
CATALYST_CLOCK = [[0] * 24 for _ in range(7)]   # [weekday 0=Mon..6=Sun][hour 0-23 UTC]
_CATALYST_SEEN_KEYS = set()
_CATALYST_TOTAL = 0

def _track_catalyst_clock(pool):
    global _CATALYST_TOTAL
    for s in pool:
        if not s.get("breaking"):
            continue
        key = s["key"]
        if key in _CATALYST_SEEN_KEYS:
            continue
        _CATALYST_SEEN_KEYS.add(key)
        try:
            dt = s["dt"].astimezone(timezone.utc)
        except Exception:
            continue
        CATALYST_CLOCK[dt.weekday()][dt.hour] += 1
        _CATALYST_TOTAL += 1


# ── Global XRP Enterprise & Partnership Ledger ──

# ── Static Global Partnership Directory (right rail) — refreshed every 3 days ──
# PLACEHOLDER data structure. Rich will supply the real 100+ entry list; this proves the mechanism.
STATIC_PARTNER_DIRECTORY = {"entries": [], "last_refreshed": None}
STATIC_PARTNER_REFRESH_DAYS = 3

def load_static_partner_directory(force=False):
    """(Re)loads the curated 100+ partnership list on a true 3-day elapsed-time cycle.
    Currently placeholder pending Rich's real list. Purely static/curated data — no external API call."""
    now = datetime.now(timezone.utc)
    last = STATIC_PARTNER_DIRECTORY.get("_last_dt")
    due = force or not last or (now - last).days >= STATIC_PARTNER_REFRESH_DAYS
    if not due and STATIC_PARTNER_DIRECTORY["entries"]:
        return
    STATIC_PARTNER_DIRECTORY["entries"] = [
        ("AMINA Bank", "FINMA-regulated digital asset institution with live native Ripple Payments", "ODL/XRP Live", "🚀", "🇨🇭"),
        ("Azimo", "International digital money transmitter processing enterprise payouts", "ODL/XRP Live", "🚀", "🇪🇺"),
        ("Bitso", "Core liquidity hub routing heavy institutional USD-to-MXN lanes", "ODL/XRP Live", "🚀", "🇲🇽"),
        ("BTC Markets", "Currency bridge managing the AUD leg of regional ODL clearing", "ODL/XRP Live", "🚀", "🇦🇺"),
        ("ChinaBank", "Clears Gulf-region corporate payments anchored to digital liquidity", "ODL/XRP Live", "🚀", "🇵🇭"),
        ("CIBC", "Settles institutional growth transfers via ODL infrastructure", "ODL/XRP Live", "🚀", "🇨🇦"),
        ("Coins.ph", "Digital consumer network handling incoming XRP liquid conversions", "ODL/XRP Live", "🚀", "🇵🇭"),
        ("Cuallix", "First fintech to pilot original xRapid/ODL settlement engines", "ODL/XRP Live", "🚀", "🇺🇸"),
        ("FlashFX", "Automated FX software routing transfers via on-chain token paths", "ODL/XRP Live", "🚀", "🇦🇺"),
        ("Independent Reserve", "Regional liquidity exchange partner providing settlement architecture", "ODL/XRP Live", "🚀", "🇦🇺"),
        ("iRemit", "Non-bank remittance giant using ledger for real-time treasury management", "ODL/XRP Live", "🚀", "🇵🇭"),
        ("Mercury FX", "Enterprise currency platform processing instant commercial payments via XRP", "ODL/XRP Live", "🚀", "🇬🇧"),
        ("MoneyMatch", "Digital conversion firm routing commercial payments to European endpoints", "ODL/XRP Live", "🚀", "🇲🇾"),
        ("Novatti", "Payments processor using XRP ledger routes for Southeast Asian corridors", "ODL/XRP Live", "🚀", "🇦🇺"),
        ("Pyypl", "Blockchain fintech offering consumer digital wallets via ODL", "ODL/XRP Live", "🚀", "🌍"),
        ("Qatar National Bank", "Cross-border pipeline targeting Philippine remittance partners", "ODL/XRP Live", "🚀", "🇶🇦"),
        ("SBI Remit / SBI Holdings", "Multi-corridor APAC retail & commercial remittance powered by XRP", "ODL/XRP Live", "🚀", "🇯🇵"),
        ("Siam Commercial Bank", "Active live ODL corridors for inbound Japanese capital", "ODL/XRP Live", "🚀", "🇹🇭"),
        ("Tranglo", "Regional processing giant fully integrated into ODL", "ODL/XRP Live", "🚀", "🇲🇾"),
        ("Travelex Bank", "First operational Latin American bank using XRP liquidity corridors", "ODL/XRP Live", "🚀", "🇧🇷"),
        ("UnionBank", "Automated processing for inbound domestic overseas worker remittances", "ODL/XRP Live", "🚀", "🇵🇭"),
        ("X Money", "Retail cross-border digital financial platform using decentralized settlement", "ODL/XRP Live", "🚀", "🌐"),
        ("Zand Bank", "Digital corporate bank processing payments via XRP and RLUSD", "ODL/XRP Live", "🚀", "🇦🇪"),
        ("Akbank", "Early regional banking partner conducting secure real-time automated tests", "Global Banks", "🏛️", "🇹🇷"),
        ("American Express", "Commercial B2B international payments clearing partner", "Global Banks", "🏛️", "🇺🇸"),
        ("ANZ Bank", "Historical testing partner of the underlying clearing protocol", "Global Banks", "🏛️", "🇦🇺"),
        ("Axis Bank", "Live infrastructure client managing real-time regional transaction tunnels", "Global Banks", "🏛️", "🇮🇳"),
        ("Banco Santander", "Powers international One Pay FX app via RippleNet messaging", "Global Banks", "🏛️", "🇪🇸"),
        ("Bank of America", "Infrastructure pilot participant holding patents referencing XRP settlement", "Global Banks", "🏛️", "🇺🇸"),
        ("BBVA", "Corporate banking implementing cross-border branch liquidity trials", "Global Banks", "🏛️", "🇪🇸"),
        ("BDO Unibank", "Major destination settlement point for international inbound money streams", "Global Banks", "🏛️", "🇵🇭"),
        ("BMO Financial Group", "North American commercial entity exploring cross-border clearing efficiency", "Global Banks", "🏛️", "🇨🇦"),
        ("CIMB Bank", "Deep integration node managing corridors across ASEAN borders", "Global Banks", "🏛️", "🇲🇾"),
        ("Commonwealth Bank (CBA)", "Major retail institution participating in pilot ecosystem networks", "Global Banks", "🏛️", "🇦🇺"),
        ("Deutsche Bank", "Combined Ripple blockchain architecture with legacy SWIFT mechanisms", "Global Banks", "🏛️", "🇩🇪"),
        ("Federal Bank", "Major localized retail bank utilizing automated routing systems", "Global Banks", "🏛️", "🇮🇳"),
        ("HSBC", "Multi-national banking network mapped via active system routing IDs", "Global Banks", "🏛️", "🇬🇧"),
        ("IndusInd Bank", "Captures inbound international money transfers using decentralized engines", "Global Banks", "🏛️", "🇮🇳"),
        ("ING Group", "Multi-national bank registered in regional backend messaging directories", "Global Banks", "🏛️", "🇳🇱"),
        ("Intesa Sanpaolo", "Enterprise participant tracking structural digital payment innovations", "Global Banks", "🏛️", "🇮🇹"),
        ("JPMorgan Chase", "Overlapping participant in multi-network settlement ledger groups", "Global Banks", "🏛️", "🌐"),
        ("Kotak Mahindra Bank", "Fintech clearing provider handling instant retail capital inflows", "Global Banks", "🏛️", "🇮🇳"),
        ("Krungsri (Bank of Ayudhya)", "Streamlines real-time corporate pipelines between Thailand and Japan", "Global Banks", "🏛️", "🇹🇭"),
        ("Macquarie Bank", "Financial and transaction group listed on official routing logs", "Global Banks", "🏛️", "🇦🇺"),
        ("MUFG Bank", "Tier-1 retail giant optimizing transaction messaging across APAC", "Global Banks", "🏛️", "🇯🇵"),
        ("National Australia Bank (NAB)", "Incorporated into the ledger settlement network indexing systems", "Global Banks", "🏛️", "🇦🇺"),
        ("PNC Bank", "First major domestic U.S. institutional network client", "Global Banks", "🏛️", "🇺🇸"),
        ("Royal Bank of Canada (RBC)", "Explored the decentralized rail protocol for automated settlement", "Global Banks", "🏛️", "🇨🇦"),
        ("SEB", "Operates high-volume corporate lines over Ripple software rails", "Global Banks", "🏛️", "🇸🇪"),
        ("Shinhan Bank", "Top South Korean network client maintaining active system access keys", "Global Banks", "🏛️", "🇰🇷"),
        ("Standard Chartered", "Core early corporate investor and active digital clearing hub collaborator", "Global Banks", "🏛️", "🇬🇧"),
        ("UBS", "Asset and investment firm evaluating high-speed distributed ledgers", "Global Banks", "🏛️", "🇨🇭"),
        ("Westpac", "Registered network member maintaining live backend communication IDs", "Global Banks", "🏛️", "🇦🇺"),
        ("Woori Bank", "Multi-channel asset institution utilizing programmatic payment lines", "Global Banks", "🏛️", "🇰🇷"),
        ("Yes Bank", "Commercial institution conducting high-velocity payment remittance operations", "Global Banks", "🏛️", "🇮🇳"),
        ("Accenture", "Consulting giant managing global deployment strategies for payment architecture", "Tech/Custody", "🛠️", "🌐"),
        ("Amazon Web Services (AWS)", "Hosts architecture allowing global nodes to run XRPL validation configurations", "Tech/Custody", "🛠️", "🌐"),
        ("BDACS", "Regulated secure vault platform for native ledger token storage", "Tech/Custody", "🛠️", "🇰🇷"),
        ("BeeTech", "Digital financial operator executing automated Latin American clearings", "Tech/Custody", "🛠️", "🇧🇷"),
        ("BNY Mellon", "Primary tier-1 institutional reserve custodian for stablecoin offerings", "Tech/Custody", "🛠️", "🇺🇸"),
        ("CGI Group", "IT consulting firm incorporating decentralized financial frameworks", "Tech/Custody", "🛠️", "🇨🇦"),
        ("Cross River Bank", "Financial tech enabler providing direct underlying banking backbone", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Currencycloud", "B2B multi-currency platform streamlining automated foreign exchange", "Tech/Custody", "🛠️", "🇬🇧"),
        ("DBS Bank", "Southeast Asian institution utilizing bank-grade digital asset vaults", "Tech/Custody", "🛠️", "🇸🇬"),
        ("Deloitte", "Integrated distributed financial systems into client business models", "Tech/Custody", "🛠️", "🌐"),
        ("DZ Bank", "Leverages digital custody solutions for tokenized asset issuance", "Tech/Custody", "🛠️", "🇩🇪"),
        ("Fidor Bank", "Digital banking pioneer integrating alternative clearing protocol tools", "Tech/Custody", "🛠️", "🇩🇪"),
        ("Finastra", "Core banking software opening network access to 2,000+ regional banks", "Tech/Custody", "🛠️", "🇬🇧"),
        ("Frankenmuth Credit Union", "Local cooperative providing digital asset services to local consumers", "Tech/Custody", "🛠️", "🇺🇸"),
        ("GTreasury", "Corporate liquidity software suite managing modern capital balance sheets", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Hidden Road", "Major institutional prime brokerage expanding liquidity paths for digital assets", "Tech/Custody", "🛠️", "🇺🇸"),
        ("InstaReM", "High-speed digital payment gateway connected via localized nodes", "Tech/Custody", "🛠️", "🇸🇬"),
        ("Kbank", "Digital platform implementing secure cryptographic wallet structures", "Tech/Custody", "🛠️", "🇰🇷"),
        ("Kyobo Life Insurance", "Utilizing token ledger blueprint for corporate structural bond settlement", "Tech/Custody", "🛠️", "🇰🇷"),
        ("Metaco", "Institutional crypto custody firm acquired by Ripple to secure bank assets globally", "Tech/Custody", "🛠️", "🇨🇭"),
        ("Modulr", "Payments provider optimizing massive local commercial transaction times", "Tech/Custody", "🛠️", "🇬🇧"),
        ("Nium", "Fintech provider optimizing massive outbound payment paths across global corridors", "Tech/Custody", "🛠️", "🇸🇬"),
        ("Sabadell", "Commercial infrastructure partner running real-time corporate data modules", "Tech/Custody", "🛠️", "🇪🇸"),
        ("Sentbe", "High-speed international remittance engine using the global banking network", "Tech/Custody", "🛠️", "🇰🇷"),
        ("Temenos", "Core banking software provider embedding automated accounting rails", "Tech/Custody", "🛠️", "🇨🇭"),
        ("Al Ansari Exchange", "High-volume Middle Eastern exchange network routing institutional transfers", "Regional", "🌍", "🇦🇪"),
        ("Banco Rendimento", "Foreign currency commercial bank using optimized digital payment tunnels", "Regional", "🌍", "🇧🇷"),
        ("Bank Alfalah", "Manages automated digital channels targeting the UAE-to-Pakistan corridor", "Regional", "🌍", "🇵🇰"),
        ("bKash", "Mobile financial giant plugged in to capture worker remittances", "Regional", "🌍", "🇧🇩"),
        ("Faysal Bank", "Specialized commercial banking provider processing inward retail cash flows", "Regional", "🌍", "🇵🇰"),
        ("Interbank", "Traditional retail banking destination tied to alternative clearing systems", "Regional", "🌍", "🇵🇪"),
        ("Intercorp", "Large conglomerate stabilizing localized payment legs for regional retail assets", "Regional", "🌍", "🇵🇪"),
        ("Itau Unibanco", "Giant South American banking provider utilizing alternative communication networks", "Regional", "🌍", "🇧🇷"),
        ("National Bank of Fujairah", "Trade finance group optimizing real-time B2B payment workflows", "Regional", "🌍", "🇦🇪"),
        ("National Bank of Kuwait (NBK)", "Runs international corporate transfer paths targeting the Gulf", "Regional", "🌍", "🇰🇼"),
        ("RAKBANK", "Integrates transaction routes to improve speed across enterprise pipelines", "Regional", "🌍", "🇦🇪"),
        ("Saudi Central Bank (SAMA)", "Central entity piloting distributed frameworks for commercial branches", "Regional", "🌍", "🇸🇦"),
        ("Vietcombank", "Explores modern asset frameworks under regional digital banking pilots", "Regional", "🌍", "🇻🇳"),
        ("Bitwise Asset Management", "Regulated Wall Street provider offering institutional XRP exposure", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Canary Capital Partners", "Asset management firm deploying institutional-grade XRP capital avenues", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Franklin Templeton", "Legacy asset firm filing for exchange-traded digital investment products", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Grayscale Investments", "Asset manager operating the regulated Grayscale XRP Trust and spot fund", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Hashdex Asset Management", "Global investment manager offering systemic access to ledger tokens", "ETF/Treasury", "🟡", "🌐"),
        ("Nature's Miracle Holding", "Agriculture Tech firm implementing a $20M Corporate Treasury on the XRPL", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Worksport Ltd.", "Clean automotive developer utilizing digital assets for inventory clearings", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Mastercard", "$9T payment network partnered with Ripple on settlement rails in 2026", "Global Banks", "🏛️", "🌐"),
        ("Banco Genial", "Ripple Payments for cross-border payouts, live 2026", "ODL/XRP Live", "🚀", "🇧🇷"),
        ("Thunes", "Brought stablecoin payouts to 11,500 SWIFT-connected banks via Ripple ODL routing", "Tech/Custody", "🛠️", "🇸🇬"),
        ("SendFriend", "ODL for international remittances", "ODL/XRP Live", "🚀", "🇺🇸"),
        ("Remitr", "RippleNet for cross-border business payments", "ODL/XRP Live", "🚀", "🌐"),
        ("Ondo Finance", "$323M+ tokenized US Treasury products on XRP Ledger", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Archax", "UK-regulated exchange bringing $1B tokenized assets onto XRPL by mid-2026", "Tech/Custody", "🛠️", "🇬🇧"),
        ("Guggenheim Treasury Services", "Tokenized commercial paper / treasury products on XRPL", "Tech/Custody", "🛠️", "🇺🇸"),
        ("OpenEden", "Tokenized US Treasury products on the XRP Ledger", "Tech/Custody", "🛠️", "🇸🇬"),
        ("Zoniqx", "Prepared hundreds of millions in RWA for issuance on XRPL", "Tech/Custody", "🛠️", "🇺🇸"),
        ("abrdn", "£3.8B liquidity fund tokenized on XRPL via Archax (first tokenized MMF)", "ETF/Treasury", "🟡", "🇬🇧"),
        ("Aviva Investors", "Announced tokenization partnership with Ripple in 2026", "ETF/Treasury", "🟡", "🇬🇧"),
        ("Justoken", "Independent RWA tokenization project building on XRPL", "Tech/Custody", "🛠️", "🌐"),
        ("Ctrl Alt", "Partnered with Ripple + Dubai Land Department for real estate tokenization", "Tech/Custody", "🛠️", "🇦🇪"),
        ("Figment", "Staking infrastructure partnership for Ripple Custody (2026)", "Tech/Custody", "🛠️", "🌐"),
        ("Securosys", "HSM support partnership for Ripple Custody (2026)", "Tech/Custody", "🛠️", "🇨🇭"),
        ("Palisade", "Acquired by Ripple to expand custody stack", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Chainalysis", "Compliance tools integrated into Ripple Custody", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Doppler Finance", "Partnered with SBI Ripple Asia for XRP-based institutional yield products", "Tech/Custody", "🛠️", "🌏"),
        ("SBI Digital Markets", "Segregated custody for SBI Ripple Asia XRP yield products", "Tech/Custody", "🛠️", "🇸🇬"),
        ("Royal Monetary Authority of Bhutan", "National CBDC pilot on XRPL since 2021", "Regional", "🌍", "🇧🇹"),
        ("Central Bank of Montenegro", "CBDC pilot exploring blockchain national currency on XRPL", "Regional", "🌍", "🇲🇪"),
        ("Republic of Palau", "National stablecoin built with Ripple on XRPL", "Regional", "🌍", "🇵🇼"),
        ("Banco de la Republica", "Central bank exploring XRPL for digital peso settlement", "Regional", "🌍", "🇨🇴"),
        ("Reserve Bank of Australia", "Project Acacia deployed wholesale CBDC on XRPL in live tests with tokenized govt bonds", "Regional", "🌍", "🇦🇺"),
        ("Monetary Authority of Singapore", "MAS sandbox projects using RLUSD for programmable trade finance", "Regional", "🌍", "🇸🇬"),
        ("Hong Kong Monetary Authority", "e-HKD CBDC pilots involving XRPL infrastructure", "Regional", "🌍", "🇭🇰"),
        ("Dubai Land Department", "Real estate tokenization on XRPL with Ripple + Ctrl Alt (2025)", "Regional", "🌍", "🇦🇪"),
        ("21Shares", "Live XRP ETP issuer", "ETF/Treasury", "🟡", "🇨🇭"),
        ("CoinShares", "Live XRP exchange-traded product issuer", "ETF/Treasury", "🟡", "🇪🇺"),
        ("WisdomTree", "XRP ETF issuer", "ETF/Treasury", "🟡", "🇺🇸"),
        ("VanEck", "Live XRP ETF issuer", "ETF/Treasury", "🟡", "🇺🇸"),
        ("ProShares", "XRP futures/ETF product under review", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Volatility Shares", "XRP futures ETF issuer", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Teucrium", "Launched 2x leveraged XRP ETF", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Goldman Sachs", "Reported largest institutional XRP holder in the US", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Societe Generale (SG-FORGE)", "Launched EUR CoinVertible euro stablecoin on XRPL (Feb 2026)", "Global Banks", "🏛️", "🇫🇷"),
        ("WebBank", "Settles fiat card transactions using RLUSD on XRPL (with Gemini)", "Global Banks", "🏛️", "🇺🇸"),
        ("Gemini", "Card transaction settlement using RLUSD on the XRP Ledger", "Tech/Custody", "🛠️", "🇺🇸"),
        ("Mastercard (RLUSD cards)", "Fiat card settlement via RLUSD on XRPL with WebBank + Gemini", "ETF/Treasury", "🟡", "🌐"),
        ("BlackRock (BUIDL)", "BUIDL fund supported on Ripple Treasury platform routing via XRPL DEX", "ETF/Treasury", "🟡", "🇺🇸"),
        ("Alloy Networks", "Runs an XRPL validator node — signal of active XRP settlement usage", "ODL/XRP Live", "🚀", "🌐"),
        ("Onafriq", "Pan-African payments network using Ripple for cross-border corridors", "Regional", "🌍", "🌍"),
        ("Ripple National Trust Bank", "OCC conditionally approved Dec 2025 — federally chartered trust bank", "Global Banks", "🏛️", "🇺🇸"),
        ("Absa Group", "Major African bank exploring Ripple cross-border infrastructure", "Regional", "🌍", "🇿🇦"),
        ("Fenasbac", "Brazil central bank innovation arm partnered on Ripple pilots", "Regional", "🌍", "🇧🇷"),
        ("DZ Bank Digital", "Digital asset custody pilots involving XRPL infrastructure", "Global Banks", "🏛️", "🇩🇪"),
    ]
    STATIC_PARTNER_DIRECTORY["_last_dt"] = now
    STATIC_PARTNER_DIRECTORY["last_refreshed"] = now.strftime("%Y-%m-%d %H:%M UTC")

load_static_partner_directory()
# Ever-growing, never-trimmed. Seed = 100 known entities (undated baseline).
# New entries detected from the live news feed get real timestamps and always sort above the baseline.
PARTNERSHIP_LEDGER = []          # list of dicts: name, country, cat, status, detail, date(None or datetime), source, key
_PARTNERSHIP_SEEDED = False
_PARTNERSHIP_SEEN_KEYS = set()
_PARTNERSHIP_DEAL_KW = ["partner", "partnership", "collaborat", "agreement", "signs", "joins forces",
                        "integrat", "teams up", "merger", "acquisition", "acquires", "deal with",
                        "onboards", "adopts xrp", "adopts ripple"]

def seed_partnership_ledger():
    global _PARTNERSHIP_SEEDED
    if _PARTNERSHIP_SEEDED:
        return
    for name, country, cat, status, detail in ENTERPRISE_SEED:
        PARTNERSHIP_LEDGER.append({
            "key": f"seed:{name.lower()}", "name": name, "country": country, "cat": cat,
            "status": status, "detail": detail, "date": None, "source": "baseline", "link": None,
        })
    _PARTNERSHIP_SEEDED = True

def _detect_partnership_deals(pool):
    for s in pool:
        key = s["key"]
        if key in _PARTNERSHIP_SEEN_KEYS:
            continue
        text = (s["title"] + " " + s.get("summary", "")).lower()
        if s.get("category") != "Ecosystem":
            continue
        if not any(kw in text for kw in _PARTNERSHIP_DEAL_KW):
            continue
        _PARTNERSHIP_SEEN_KEYS.add(key)
        PARTNERSHIP_LEDGER.append({
            "key": f"news:{key}", "name": s["title"], "country": None, "cat": "N",
            "status": "NEW", "detail": s.get("summary", "") or s["source"], "date": s["dt"],
            "source": "detected", "link": s.get("link"),
        })

def partnership_ledger_html(limit=30):
    detected = sorted((e for e in PARTNERSHIP_LEDGER if e["source"] == "detected"),
                       key=lambda e: e["date"], reverse=True)
    baseline = [e for e in PARTNERSHIP_LEDGER if e["source"] == "baseline"]
    ordered = (detected + baseline)[:limit]
    if not ordered:
        return '<div class="empty">Directory loading\u2026</div>'
    out = ""
    for e in ordered:
        col = ENTERPRISE_CATEGORY_COLORS.get(e["cat"], "var(--tx)")
        if e["source"] == "detected":
            badge = '<span class="pl-new">\U0001F195 NEW</span>'
            when = _time_ago(e["date"])
            title_html = (f'<a href="{html.escape(e["link"] or "#", quote=True)}" target="_blank" rel="noopener">'
                          f'{html.escape(e["name"])}</a>')
            meta = html.escape(e["detail"][:140])
        else:
            badge = ""
            when = "Established"
            title_html = html.escape(e["name"])
            meta = f'{html.escape(e["country"] or "")} \u2014 {html.escape(e["detail"])}'
        out += (
            f'<div class="pl-row" data-cat="{e["cat"]}" data-text="{html.escape((e["name"] + " " + (e["country"] or "") + " " + e["detail"]).lower(), quote=True)}">'
            f'<div class="pl-top"><span class="pl-cat" style="color:{col}">{ENTERPRISE_CATEGORY_LABELS.get(e["cat"], "\U0001F195 New Deal")}</span>'
            f'{badge}<span class="pl-status" style="color:{col}">{html.escape(e["status"])}</span>'
            f'<span class="pl-when">{when}</span></div>'
            f'<div class="pl-name">{title_html}</div>'
            f'<div class="pl-meta">{meta}</div>'
            f'</div>'
        )
    return out


SENTIMENT_HISTORY = {}   # date_str -> {"bull","bear","neut","total","_keys"}
NEWS_VOLUME_HISTORY = {}  # date_str -> {"total","sources":set,"by_cat":{},"_keys":set} \u2014 real,
                          # honestly-accumulated daily counts from the feeds this site already
                          # tracks. Never fabricated or estimated; builds up over time like
                          # SENTIMENT_HISTORY above. Used by "News Mention Volume" (V109).
NEWS_VOLUME_HISTORY_MAX = 30
SENTIMENT_HISTORY_MAX = 30

def tech_specs_html():
    out = ""
    for metric, xrpl, eth, sol, btc in TECH_SPECS:
        out += (
            f'<tr><td style="padding:6px;color:var(--br)">{metric}</td>'
            f'<td style="text-align:center;padding:6px;color:var(--gr);font-weight:700">{xrpl}</td>'
            f'<td style="text-align:center;padding:6px;color:var(--tx)">{eth}</td>'
            f'<td style="text-align:center;padding:6px;color:var(--tx)">{sol}</td>'
            f'<td style="text-align:center;padding:6px;color:var(--tx)">{btc}</td></tr>'
        )
    return out

def use_case_html():
    out = ""
    for icon, title, col, detail in USE_CASES:
        out += (
            f'<div class="uc-card" style="border-left-color:{col}">'
            f'<div class="uc-title" style="color:{col}">{icon} {title}</div>'
            f'<div class="uc-detail">{detail}</div></div>'
        )
    return out

def ad_line_html():
    d7 = MARKET.get("ad_7d_delta")
    d30 = MARKET.get("ad_30d_delta")
    def _sig(delta):
        if delta is None:
            return "\u2014", "var(--tx)"
        return ("\U0001F7E2 Accumulation", "var(--gr)") if delta > 0 else ("\U0001F534 Distribution", "var(--rd)")
    s7, c7 = _sig(d7)
    s30, c30 = _sig(d30)
    return s7, c7, s30, c30

def correlation_html():
    def _row(label, val):
        if val is None:
            return f'<div class="corr-row"><span>{label}</span><span style="color:var(--tx)">\u2014</span></div>'
        col = "var(--gr)" if val >= 0 else "var(--rd)"
        sign = "+" if val >= 0 else ""
        lbl = "positive" if val >= 0 else "inverse"
        return (f'<div class="corr-row"><span>{label}</span>'
                f'<span style="color:{col}">{sign}{val:.2f} <small style="color:var(--tx)">({lbl})</small></span></div>')
    return _row("XRP vs BTC", MARKET.get("corr_btc")) + _row("XRP vs ETH", MARKET.get("corr_eth"))

def orderbook_html():
    bids = MARKET.get("ob_bids") or []
    asks = MARKET.get("ob_asks") or []
    if not bids or not asks:
        return ('<div class="home-base"><div class="home-base-icon">\U0001F4CA</div>'
                '<div class="home-base-title">Loading Order Book</div>'
                '<div class="home-base-sub">Live bid/ask depth from Binance populates on deploy.</div></div>', "", "\u2014", "\u2014")
    all_sizes = [q for _, q in bids] + [q for _, q in asks]
    mx = max(all_sizes) or 1
    bid_rows = "".join(
        f'<div class="ob-row"><span class="ob-price gr">${p:.4f}</span>'
        f'<div class="ob-bar-wrap"><div class="ob-bar gr" style="width:{q/mx*100:.0f}%"></div></div>'
        f'<span class="ob-qty">{q:,.0f}</span></div>' for p, q in bids)
    ask_rows = "".join(
        f'<div class="ob-row"><span class="ob-price rd">${p:.4f}</span>'
        f'<div class="ob-bar-wrap"><div class="ob-bar rd" style="width:{q/mx*100:.0f}%"></div></div>'
        f'<span class="ob-qty">{q:,.0f}</span></div>' for p, q in asks)
    bid_total = _fmt_usd(MARKET.get("ob_bid_total"))
    ask_total = _fmt_usd(MARKET.get("ob_ask_total"))
    return bid_rows, ask_rows, bid_total, ask_total

def liquidity_map_html():
    bids = MARKET.get("ob_bids") or []
    asks = MARKET.get("ob_asks") or []
    if not bids or not asks:
        return '<div class="empty">Liquidity data populates on deploy.</div>'
    bid_val = sum(p * q for p, q in bids)
    ask_val = sum(p * q for p, q in asks)
    total = bid_val + ask_val
    bid_pct = round(bid_val / total * 100) if total else 50
    ask_pct = 100 - bid_pct
    skew = "Buy-side heavier" if bid_pct > 55 else ("Sell-side heavier" if ask_pct > 55 else "Balanced")
    return (
        f'<div class="liq-bar"><div class="liq-fill" style="width:{bid_pct}%"></div></div>'
        f'<div class="liq-labels"><span style="color:var(--gr)">{bid_pct}% bids</span>'
        f'<span style="color:var(--rd)">{ask_pct}% asks</span></div>'
        f'<div class="liq-skew">{skew}</div>'
        f'<div class="liq-note">Top 8 levels each side \u00B7 Binance XRP/USDT</div>'
    )


def clarity_tracker_html():
    stories = sorted(CLARITY_ACT_STORIES, key=lambda s: s["dt"], reverse=True)
    if not stories:
        return ('<div class="home-base"><div class="home-base-icon">\U0001F3DB\uFE0F</div>'
                '<div class="home-base-title">Monitoring the CLARITY Act</div>'
                '<div class="home-base-sub">The 10 most recent stories on the bill\u2019s progress through the '
                'Senate will appear here automatically as they\u2019re published.</div></div>')
    out = ""
    for i, s in enumerate(stories, 1):
        out += (
            f'<div class="ca-row"><div class="ca-rank">#{i}</div><div class="ca-body">'
            f'<div class="ca-top"><span class="ca-src">{html.escape(s["source"])}</span>'
            f'<span class="ca-time">{_time_ago(s["dt"])}</span></div>'
            f'<a class="ca-hl" href="{html.escape(s["link"], quote=True)}" target="_blank" rel="noopener">'
            f'{html.escape(s["title"])}</a></div></div>'
        )
    return out


_WEEKDAY_LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def narrative_diffusion_html(limit=6):
    if not NARRATIVE_DIFFUSION:
        return ('<div class="home-base"><div class="home-base-icon">\U0001F30D</div>'
                '<div class="home-base-title">Monitoring Narrative Spread</div>'
                '<div class="home-base-sub">As themes emerge and reach multiple regions, their spread timeline '
                'will appear here automatically.</div></div>', "\u2014")

    themes = sorted(NARRATIVE_DIFFUSION.items(),
                     key=lambda kv: (len(kv[1]["regions"]), kv[1]["first_seen"]), reverse=True)[:limit]
    now = datetime.now(timezone.utc)
    cards = ""
    fastest_theme, fastest_span = None, None
    for theme, data in NARRATIVE_DIFFUSION.items():
        regs = data["regions"]
        if len(regs) >= 2:
            span = max(regs.values()) - min(regs.values())
            if fastest_span is None or span < fastest_span:
                fastest_span, fastest_theme = span, theme

    for theme, data in themes:
        age = _time_ago(data["first_seen"])
        regs_sorted = sorted(data["regions"].items(), key=lambda kv: kv[1])
        n_regs = len(regs_sorted)
        chips = ""
        for region, dt in regs_sorted:
            lag_sec = (dt - data["first_seen"]).total_seconds()
            lag_txt = "first" if lag_sec < 60 else f"+{int(lag_sec // 3600)}h" if lag_sec >= 3600 else f"+{int(lag_sec // 60)}m"
            chips += (f'<span class="nd-chip">{REGION_FLAGS.get(region, "")} {region} '
                      f'<span class="nd-lag">{lag_txt}</span></span>')
        spread_note = (f'Reached {n_regs} regions' if n_regs >= 2 else 'Still regional \u2014 1 region so far')
        cards += (
            f'<div class="nd-card"><div class="nd-top"><span class="nd-theme">{html.escape(theme)}</span>'
            f'<span class="nd-age">first seen {age}</span></div>'
            f'<div class="nd-chips">{chips}</div>'
            f'<div class="nd-note">{spread_note}</div></div>'
        )

    if fastest_theme and fastest_span:
        h = fastest_span.total_seconds() / 3600
        fastest_txt = f'"{fastest_theme}" reached multiple regions in {h:.1f}h' if h >= 1 else f'"{fastest_theme}" reached multiple regions in {int(fastest_span.total_seconds()//60)}m'
    else:
        fastest_txt = "\u2014 (building up)"
    return cards, fastest_txt


def catalyst_clock_html():
    mx = max(max(row) for row in CATALYST_CLOCK) or 1
    cells = ""
    for wd in range(7):
        cells += f'<div class="cc-row"><span class="cc-daylbl">{_WEEKDAY_LABELS[wd]}</span>'
        for hr in range(24):
            v = CATALYST_CLOCK[wd][hr]
            inten = v / mx if mx else 0
            if v == 0:
                bg = "var(--s2)"
            else:
                bg = f"rgba(255,153,0,{0.15 + inten * 0.75:.2f})"
            cells += f'<div class="cc-cell" style="background:{bg}" title="{_WEEKDAY_LABELS[wd]} {hr:02d}:00 UTC \u2014 {v} breaking stor{"y" if v == 1 else "ies"}"></div>'
        cells += '</div>'

    # Peak hour / weekday
    hour_totals = [sum(CATALYST_CLOCK[wd][hr] for wd in range(7)) for hr in range(24)]
    day_totals = [sum(CATALYST_CLOCK[wd]) for wd in range(7)]
    if _CATALYST_TOTAL:
        peak_hr = hour_totals.index(max(hour_totals))
        peak_day = _WEEKDAY_LABELS[day_totals.index(max(day_totals))]
        peak_txt = f"{peak_hr:02d}:00 UTC on {peak_day}s"
    else:
        peak_txt = "\u2014 (building up)"
    hour_lbls = "".join(f'<span class="cc-hourlbl">{h if h % 3 == 0 else ""}</span>' for h in range(24))
    return cells, peak_txt, hour_lbls


def ici_comps_html(comps):
    out = ""
    for name, detail, pts in comps:
        pct = round(pts / 20 * 100)
        out += (
            f'<div class="ici-comp-row"><span class="ici-comp-name">{html.escape(name)}</span>'
            f'<div class="ici-comp-track"><div class="ici-comp-fill" style="width:{pct}%"></div></div>'
            f'<span class="ici-comp-pts">{pts}/20</span></div>'
            f'<div class="ici-comp-detail">{html.escape(detail)}</div>'
        )
    return out


def partnership_momentum_html(weeks=10):
    """Deals detected per week, bucketed from our own Enterprise Ledger timestamps.
    Builds up honestly over time -- no fabricated history."""
    now = datetime.now(timezone.utc)
    detected = [e for e in PARTNERSHIP_LEDGER if e.get("source") == "detected" and e.get("date")]
    buckets = [0] * weeks
    for e in detected:
        age_days = (now - e["date"]).days
        week_idx = weeks - 1 - (age_days // 7)
        if 0 <= week_idx < weeks:
            buckets[week_idx] += 1
    mx = max(buckets) or 1
    bars = "".join(
        f'<div class="pm-bar" style="height:{max(6, v / mx * 100):.0f}%" title="{v} deal{"s" if v != 1 else ""}"></div>'
        for v in buckets
    )
    total = len(detected)
    this_week = buckets[-1]
    last_week = buckets[-2] if weeks >= 2 else 0
    if this_week > last_week:
        trend, tcol = f"\u25B2 up from {last_week} last week", "var(--gr)"
    elif this_week < last_week:
        trend, tcol = f"\u25BC down from {last_week} last week", "var(--rd)"
    else:
        trend, tcol = "\u2192 steady week over week", "var(--tx)"
    avg = round(total / weeks, 1) if total else 0.0
    return bars, total, this_week, trend, tcol, avg


def _track_news_volume(pool):
    """Real, honestly-accumulated daily news volume \u2014 same de-dup pattern as
    _track_sentiment_history. No estimation, no fabrication: only counts
    stories this site's own 306+ RSS feeds have actually returned."""
    for s in pool:
        try:
            day = s["dt"].astimezone(timezone.utc).date().isoformat()
        except Exception:
            continue
        bucket = NEWS_VOLUME_HISTORY.setdefault(
            day, {"total": 0, "sources": set(), "by_cat": {}, "_keys": set()})
        if s["key"] in bucket["_keys"]:
            continue
        bucket["_keys"].add(s["key"])
        bucket["total"] += 1
        bucket["sources"].add(s.get("source", "Unknown"))
        cat = s.get("category", "General")
        bucket["by_cat"][cat] = bucket["by_cat"].get(cat, 0) + 1
    if len(NEWS_VOLUME_HISTORY) > NEWS_VOLUME_HISTORY_MAX:
        for old_day in sorted(NEWS_VOLUME_HISTORY.keys())[:len(NEWS_VOLUME_HISTORY) - NEWS_VOLUME_HISTORY_MAX]:
            del NEWS_VOLUME_HISTORY[old_day]


def _track_sentiment_history(pool):
    for s in pool:
        try:
            day = s["dt"].astimezone(timezone.utc).date().isoformat()
        except Exception:
            continue
        bucket = SENTIMENT_HISTORY.setdefault(
            day, {"bull": 0, "bear": 0, "neut": 0, "total": 0, "_keys": set()})
        if s["key"] in bucket["_keys"]:
            continue
        bucket["_keys"].add(s["key"])
        bucket["total"] += 1
        if s["sentiment"] == "bullish":
            bucket["bull"] += 1
        elif s["sentiment"] == "bearish":
            bucket["bear"] += 1
        else:
            bucket["neut"] += 1
    if len(SENTIMENT_HISTORY) > SENTIMENT_HISTORY_MAX:
        for old_day in sorted(SENTIMENT_HISTORY.keys())[:len(SENTIMENT_HISTORY) - SENTIMENT_HISTORY_MAX]:
            del SENTIMENT_HISTORY[old_day]


def news_velocity_24h():
    """Stories per hour for the last 24h, oldest -> newest (24 buckets)."""
    now = datetime.now(timezone.utc)
    buckets = [0] * 24
    for s in NEWS.get("pool", []):
        try:
            hrs_ago = (now - s["dt"]).total_seconds() / 3600
            if 0 <= hrs_ago < 24:
                buckets[23 - int(hrs_ago)] += 1
        except Exception:
            continue
    return buckets


def interest_score():
    """XRP interest score (0-100), honestly derived from our own feed velocity
    (Iteration-1 used this exact approach as its fallback when Google Trends was unavailable)."""
    now = datetime.now(timezone.utc)
    pool = NEWS.get("pool", [])
    recent_6h = sum(1 for s in pool if (now - s["dt"]).total_seconds() < 21600)
    score = min(recent_6h * 6 + min(len(pool), 20), 100)
    if score > 70:
        label = "\U0001F525 Trending"
    elif score > 40:
        label = "\U0001F4C8 Rising"
    elif score > 15:
        label = "\U0001F634 Quiet"
    else:
        label = "\U0001F4A4 Minimal"
    return score, label


def sentiment_source_table(n=15):
    pool = NEWS.get("pool", [])
    agg = {}
    for s in pool:
        e = agg.setdefault(s["source"], {"name": s["source"], "total": 0, "bull": 0, "bear": 0, "breaking": 0})
        e["total"] += 1
        if s["sentiment"] == "bullish":
            e["bull"] += 1
        if s["sentiment"] == "bearish":
            e["bear"] += 1
        if s.get("breaking"):
            e["breaking"] += 1
    return sorted(agg.values(), key=lambda x: x["total"], reverse=True)[:n]


def _time_ago(dt):
    secs = (datetime.now(timezone.utc) - dt).total_seconds()
    if secs < 3600:
        return f"{int(secs // 60)}m ago"
    if secs < 86400:
        return f"{int(secs // 3600)}h ago"
    return f"{int(secs // 86400)}d ago"

def story_rows_html(stories):
    if not stories:
        return '<div class="empty">Connecting to news feeds\u2026 headlines populate on deploy.</div>'
    sent_col = {"bullish": "var(--gr)", "bearish": "var(--rd)", "neutral": "var(--tx)"}
    out = ""
    for i, s in enumerate(stories, 1):
        col = sent_col.get(s["sentiment"], "var(--tx)")
        out += (
            f'<a class="story" href="{html.escape(s["link"], quote=True)}" target="_blank" rel="noopener">'
            f'<span class="story-num">{i}</span>'
            f'<span class="story-body">'
            f'<span class="story-hl">{html.escape(s["title"])}</span>'
            f'<span class="story-meta"><span style="color:{col};font-weight:700">{s["sentiment"]}</span>'
            f' \u00B7 {html.escape(s["source"])} \u00B7 {_time_ago(s["dt"])}</span>'
            f'</span></a>'
        )
    return out


_GN_CAT_COLORS = {
    "ALL": "var(--br)", "PRICE": "var(--yl)", "LEGAL": "var(--rd)", "REG": "var(--or)",
    "ECOSYSTEM": "var(--gr)", "TECH": "var(--tq)", "WHALE": "var(--bl)", "GENERAL": "var(--tx)",
}

def global_feed_html(limit=60):
    pool = NEWS.get("pool", [])
    if not pool:
        return '<div class="empty">Connecting to news feeds\u2026 stories populate on deploy.</div>'
    sent_col = {"bullish": "var(--gr)", "bearish": "var(--rd)", "neutral": "#8099b3"}
    stories = sorted(pool, key=lambda s: s["dt"], reverse=True)[:limit]
    out = ""
    for s in stories:
        cat = s.get("category", "General")
        sent = s.get("sentiment", "neutral")
        col = sent_col.get(sent, "#8099b3")
        cat_col = _GN_CAT_COLORS.get(cat.upper(), "var(--tx)")
        title = html.escape(s["title"])
        summary = html.escape(s.get("summary", ""))
        data_text = html.escape((s["title"] + " " + s.get("summary", "")).lower(), quote=True)
        breaking = ('<span class="gn-break">\u26A1 BREAKING</span>' if s.get("breaking") else '')
        translate = ('' if not s.get("foreign") else
                     f'<a class="gn-tr" href="{_translate_url(s["link"])}" target="_blank" rel="noopener">\U0001F310 Translate</a>')
        summary_html = f'<div class="gn-sum">{summary}</div>' if summary else ''
        out += (
            f'<div class="gn-card" data-cat="{cat.upper()}" data-text="{data_text}">'
            f'<div class="gn-top"><span class="gn-src">{html.escape(s["source"])}</span>'
            f'<span class="gn-cat" style="color:{cat_col}">{cat}</span>{breaking}'
            f'<span class="gn-time">{_time_ago(s["dt"])}</span></div>'
            f'<a class="gn-hl" href="{html.escape(s["link"], quote=True)}" target="_blank" rel="noopener">{title}</a>'
            f'{translate}'
            f'{summary_html}'
            f'<div class="gn-foot"><span class="gn-dot" style="background:{col}"></span>'
            f'<span style="color:{col};text-transform:capitalize">{sent}</span></div>'
            f'</div>'
        )
    return out


def _matches(story, kws):
    t = (story["title"] + " " + story["source"]).lower()
    return any(k in t for k in kws)

def us_intelligence():
    """News-derived US briefing. (Upgrade point: swap internals for a Claude API call,
    keeping this computed version as the fallback.)"""
    pool = NEWS.get("pool", [])
    ts = NEWS.get("updated")
    us = [s for s in pool if _matches(s, US_KEYWORDS) or "ripple" in s["title"].lower()]
    if not us:
        return {"pulse": "Awaiting US market signals \u2014 the news feed is still loading.",
                "regulatory": "No US regulatory headlines in the current cycle.",
                "institutional": "No US institutional headlines in the current cycle.", "ts": ts}
    bulls = sum(1 for s in us if s["sentiment"] == "bullish")
    bears = sum(1 for s in us if s["sentiment"] == "bearish")
    lean = "bullish" if bulls > bears else "bearish" if bears > bulls else "balanced"
    n = len(us)
    pulse = (f"{n} US-focused XRP stor{'y' if n == 1 else 'ies'} this cycle; sentiment reads {lean} "
             f"({bulls} bullish, {bears} bearish), centered on regulatory clarity and institutional access.")
    reg = [s for s in us if _matches(s, {"sec", "cftc", "court", "ruling", "settlement", "legislation", "congress", "senate", "regulat"})]
    regulatory = (f"{len(reg)} stor{'y' if len(reg) == 1 else 'ies'} touch{'es' if len(reg) == 1 else ''} US regulation (SEC / CFTC / legislation)."
                  if reg else "Quiet on the US regulatory front this cycle.")
    inst = [s for s in us if _matches(s, {"etf", "bank", "custody", "blackrock", "fidelity", "nasdaq", "institutional", "fund"})]
    institutional = (f"{len(inst)} stor{'y' if len(inst) == 1 else 'ies'} cover{'s' if len(inst) == 1 else ''} US institutional activity (ETFs, banks, custody)."
                     if inst else "No notable US institutional moves this cycle.")
    return {"pulse": pulse, "regulatory": regulatory, "institutional": institutional, "ts": ts}

def _region_signals():
    pool = NEWS.get("pool", [])
    signals = {}
    for reg in REGIONS:
        rs = [s for s in pool if s.get("region") == reg]
        if rs:
            b = sum(1 for s in rs if s["sentiment"] == "bullish")
            r = sum(1 for s in rs if s["sentiment"] == "bearish")
            signals[reg] = "bullish" if b > r else "bearish" if r > b else "neutral"
        else:
            signals[reg] = "quiet"
    return signals

def global_pulse():
    """News-derived global synthesis (same upgrade point as US Intelligence)."""
    pool = NEWS.get("pool", [])
    ts = NEWS.get("updated")
    signals = _region_signals()
    if not pool:
        return {"pulse": "Awaiting global signals \u2014 the news feed is still loading.",
                "thesis": "Region signals populate as feeds report in.", "signals": signals, "ts": ts}
    bulls = sum(1 for s in pool if s["sentiment"] == "bullish")
    bears = sum(1 for s in pool if s["sentiment"] == "bearish")
    active = [r for r in REGIONS if signals[r] != "quiet"]
    lean = "risk-on" if bulls > bears else "risk-off" if bears > bulls else "balanced"
    pulse = (f"{len(pool)} XRP stories across {len(active)} active region{'s' if len(active) != 1 else ''}; "
             f"the global tape reads {lean} ({bulls} bullish, {bears} bearish).")
    bull_regions = [r for r in REGIONS if signals[r] == "bullish"]
    if bull_regions:
        thesis = f"Positive momentum is concentrated in {', '.join(bull_regions)}. "
    else:
        thesis = "No single region is clearly leading. "
    thesis += ("Broad positive flow supports continuation \u2014 watch US regulatory catalysts for confirmation."
               if bulls >= bears else
               "Mixed-to-cautious flow points to range-bound action until a clearer catalyst emerges.")
    return {"pulse": pulse, "thesis": thesis, "signals": signals, "ts": ts}

def _fmt_usd(v):
    if not v:
        return "\u2014"
    if v >= 1e9:
        return f"${v / 1e9:.2f}B"
    if v >= 1e6:
        return f"${v / 1e6:.2f}M"
    if v >= 1e3:
        return f"${v / 1e3:.1f}K"
    return f"${v:.2f}"

def signal_stats():
    pool = NEWS.get("pool", [])
    total = len(pool)
    bull = sum(1 for s in pool if s["sentiment"] == "bullish")
    bear = sum(1 for s in pool if s["sentiment"] == "bearish")
    neut = total - bull - bear
    return total, bull, bear, neut

# ─────────────────────────────────────────────────────────────────────
# XRP INTELLIGENCE BRIEF — twice daily (AM 12:00 PM CST, PM 9:00 PM CST)
# News-derived; each edition is generated at its slot and cached until the next.
# ─────────────────────────────────────────────────────────────────────
BRIEF = {"slot_id": None, "edition": None, "generated": None, "next_run": None, "sections": {}}
BRIEF_ARCHIVE = {}   # slot_id -> {"edition","generated","sections"} — this week's editions live here
BRIEF_ARCHIVE_MAX = 1   # current edition only — next brief replaces it
BRIEF_ARCHIVE_FILE = "/tmp/xrpcomplete_brief_archive.json"  # survives simple restarts; wiped only on full redeploy

def _save_brief_archive():
    """Persist BRIEF_ARCHIVE to disk so a simple process restart doesn't lose it. Never raises."""
    try:
        with open(BRIEF_ARCHIVE_FILE, "w") as f:
            json.dump(BRIEF_ARCHIVE, f)
    except Exception:
        pass

def _load_brief_archive():
    """Load BRIEF_ARCHIVE from disk on startup, if present. Never raises."""
    try:
        with open(BRIEF_ARCHIVE_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                BRIEF_ARCHIVE.update(data)
    except Exception:
        pass

_load_brief_archive()

_BRIEF_THEMES = {
    "Spot ETF": ["etf", "spot etf"],
    "SEC / Legal": ["sec", "lawsuit", "court", "ruling", "settlement", "appeal"],
    "RLUSD / Stablecoin": ["rlusd", "stablecoin"],
    "Bank Partnerships": ["partnership", "bank", "santander", "sbi", "custody"],
    "XRPL Tech": ["xrpl", "ledger", "amm", "evm", "amendment", "upgrade"],
    "Whale Flows": ["whale", "million xrp", "billion xrp", "transfer"],
    "CBDC / Sovereign": ["cbdc", "central bank", "sovereign", "digital currency"],
}

def _brief_slot(now_ct):
    d = now_ct.date()
    h = now_ct.hour
    if h >= 21:
        return f"{d.isoformat()}-PM", "PM"
    if h >= 12:
        return f"{d.isoformat()}-AM", "AM"
    yd = (now_ct - timedelta(days=1)).date()
    return f"{yd.isoformat()}-PM", "PM"

def _brief_next_run_dt(now_ct):
    h = now_ct.hour
    if h < 12:
        return now_ct.replace(hour=12, minute=0, second=0, microsecond=0)
    elif h < 21:
        return now_ct.replace(hour=21, minute=0, second=0, microsecond=0)
    else:
        return (now_ct + timedelta(days=1)).replace(hour=12, minute=0, second=0, microsecond=0)

def _brief_next_run(now_ct):
    nxt = _brief_next_run_dt(now_ct)
    try:
        return nxt.strftime("%b %d, %-I:%M %p CST")
    except ValueError:
        return nxt.strftime("%b %d, %I:%M %p CST")

def _brief_sections(pool):
    total = len(pool)
    if not total:
        msg = "Awaiting the news feed \u2014 this edition publishes once stories are in."
        return {k: msg for k in ["pulse", "connections", "domino", "regional", "watchlist", "tradfi"]}
    bull = sum(1 for s in pool if s["sentiment"] == "bullish")
    bear = sum(1 for s in pool if s["sentiment"] == "bearish")
    lean = "bullish" if bull > bear else "bearish" if bear > bull else "balanced"
    chg = MARKET.get("xrp_chg")
    dir_txt = ("up" if (chg or 0) >= 0 else "down") + (f" {abs(chg):.2f}% over 24h" if chg is not None else "")
    fng = MARKET.get("fng")
    fng_txt = (f"Fear & Greed reads {fng} ({MARKET.get('fng_label', '')})" if fng is not None
               else "Fear & Greed is unavailable")

    pulse = (f"The tape carries {total} XRP stor{'y' if total == 1 else 'ies'} this edition, leaning {lean} "
             f"({bull} bullish, {bear} bearish). {fng_txt}; XRP is {dir_txt}.")

    theme_hits = []
    for name, kws in _BRIEF_THEMES.items():
        stories = [s for s in pool if any(k in (s["title"] + " " + s.get("summary", "")).lower() for k in kws)]
        if stories:
            srcs = len({s["source"] for s in stories})
            theme_hits.append((name, len(stories), srcs))
    theme_hits.sort(key=lambda t: (t[1], t[2]), reverse=True)
    if theme_hits:
        parts = [f"{n} ({c} stor{'y' if c == 1 else 'ies'} across {sc} outlet{'s' if sc != 1 else ''})"
                 for n, c, sc in theme_hits[:3]]
        connections = "The dominant thread is " + parts[0]
        if len(parts) > 1:
            connections += ", followed by " + " and ".join(parts[1:])
        connections += ". Cross-outlet convergence suggests the narrative is broadening, not isolated."
    else:
        connections = "Coverage is fragmented with no single dominant thread this edition."

    if theme_hits:
        lead = theme_hits[0][0]
        if lean == "bullish":
            domino = (f"If {lead} momentum holds, expect follow-through buying and secondary coverage from lagging "
                      f"outlets; watch for confirmation in price and volume.")
        elif lean == "bearish":
            domino = (f"With sentiment tilting bearish around {lead}, near-term downside headlines could compound; "
                      f"a single positive catalyst would be needed to reverse the tone.")
        else:
            domino = (f"{lead} is driving the cycle but sentiment is balanced \u2014 the next major headline likely "
                      f"sets direction; until then, expect a range-bound reaction.")
    else:
        domino = "No clear catalyst chain this edition; the market is between stories and likely to drift."

    reg_rows = _rank_counts([s["region"] for s in pool if s.get("region")])
    if reg_rows:
        parts = []
        for reg, cnt in reg_rows[:3]:
            rs = [s for s in pool if s.get("region") == reg]
            b = sum(1 for s in rs if s["sentiment"] == "bullish")
            r = sum(1 for s in rs if s["sentiment"] == "bearish")
            sig = "bullish" if b > r else "bearish" if r > b else "neutral"
            parts.append(f"{REGION_FLAGS.get(reg, '')} {reg} ({cnt}, {sig})")
        regional = "Regional activity concentrates in " + ", ".join(parts) + ". Other regions are quiet."
    else:
        regional = "No regional flashpoints \u2014 coverage is US and global-centric this edition."

    watch = sorted(pool, key=lambda s: s["influence"], reverse=True)[:4]
    if watch:
        items = "; ".join(f"({i}) {html.escape(s['title'])} \u2014 {html.escape(s['source'])}"
                          for i, s in enumerate(watch, 1))
        watchlist = "Highest-signal stories to watch: " + items + "."
    else:
        watchlist = "No standout stories to flag this edition."

    tradfi_kw = {"etf", "bank", "custody", "sec", "institutional", "nasdaq", "blackrock", "fidelity", "swift", "settlement"}
    tf = [s for s in pool if any(k in (s["title"] + " " + s.get("summary", "")).lower() for k in tradfi_kw)]
    if tf:
        tradfi = (f"{len(tf)} stor{'y' if len(tf) == 1 else 'ies'} touch traditional-finance integration "
                  f"(ETFs, banks, regulators, settlement rails). Institutional plumbing remains the structural story "
                  f"beneath the daily price noise.")
    else:
        tradfi = "Quiet on traditional-finance integration this edition; watch for ETF and banking headlines next cycle."

    return {"pulse": pulse, "connections": connections, "domino": domino,
            "regional": regional, "watchlist": watchlist, "tradfi": tradfi}

def generate_brief():
    now_ct = datetime.now(CENTRAL)
    slot_id, edition = _brief_slot(now_ct)
    BRIEF["slot_id"] = slot_id
    BRIEF["edition"] = edition
    try:
        BRIEF["generated"] = now_ct.strftime("%b %d, %Y \u00B7 %-I:%M %p CST")
    except ValueError:
        BRIEF["generated"] = now_ct.strftime("%b %d, %Y \u00B7 %I:%M %p CST")
    BRIEF["next_run"] = _brief_next_run(now_ct)
    BRIEF["sections"] = _brief_sections(NEWS.get("pool", []))

    BRIEF_ARCHIVE[slot_id] = {
        "edition": BRIEF["edition"],
        "generated": BRIEF["generated"],
        "sections": dict(BRIEF["sections"]),
    }
    if len(BRIEF_ARCHIVE) > BRIEF_ARCHIVE_MAX:
        for old_key in sorted(BRIEF_ARCHIVE.keys())[:len(BRIEF_ARCHIVE) - BRIEF_ARCHIVE_MAX]:
            del BRIEF_ARCHIVE[old_key]
    _save_brief_archive()


def brief_week_slots(now_ct, n=BRIEF_ARCHIVE_MAX):
    """Current + previous edition slots (n=BRIEF_ARCHIVE_MAX), most recent first."""
    cur_id, cur_edition = _brief_slot(now_ct)
    y, m, d, _ = cur_id.split("-")
    cur_date = datetime(int(y), int(m), int(d)).date()
    slots = []
    dd, ed = cur_date, cur_edition
    for _ in range(n):
        slot_id = f"{dd.isoformat()}-{ed}"
        slots.append({"slot_id": slot_id, "date": dd, "edition": ed})
        if ed == "PM":
            ed = "AM"
        else:
            ed = "PM"
            dd = dd - timedelta(days=1)
    return slots


# ── World briefing clocks: UTC + 7 major crypto-trading cities ──
WORLD_CITIES = [
    ("UTC",       "UTC"),
    ("New York",  "America/New_York"),
    ("London",    "Europe/London"),
    ("Dubai",     "Asia/Dubai"),
    ("Singapore", "Asia/Singapore"),
    ("Hong Kong", "Asia/Hong_Kong"),
    ("Tokyo",     "Asia/Tokyo"),
    ("Seoul",     "Asia/Seoul"),
]

def _tz(name):
    if name == "UTC":
        return timezone.utc
    try:
        return ZoneInfo(name)
    except Exception:
        return timezone.utc

def _fmt_local(dt, z):
    try:
        return dt.astimezone(z).strftime("%-I:%M %p")
    except ValueError:
        return dt.astimezone(z).strftime("%I:%M %p").lstrip("0")

def world_clocks_html():
    now_utc = datetime.now(timezone.utc)
    ct = datetime.now(CENTRAL)
    b1 = ct.replace(hour=12, minute=0, second=0, microsecond=0)   # 12:00 PM CST edition
    b2 = ct.replace(hour=21, minute=0, second=0, microsecond=0)   # 9:00 PM CST edition
    out = ""
    for city, tzname in WORLD_CITIES:
        z = _tz(tzname)
        off = now_utc.astimezone(z).utcoffset().total_seconds() / 3600
        hh = int(abs(off)); mm = int(round((abs(off) - hh) * 60))
        if tzname == "UTC":
            off_disp = "\u00B10"
        else:
            off_disp = ("+" if off >= 0 else "\u2212") + str(hh) + (f":{mm:02d}" if mm else "")
        out += (
            f'<div class="wc">'
            f'<div class="wc-city">{city}</div>'
            f'<div class="wc-clock" data-tz="{tzname}">'
            f'<span class="wc-hand wc-hr"></span>'
            f'<span class="wc-hand wc-min"></span>'
            f'<span class="wc-hand wc-sec"></span>'
            f'<span class="wc-center"></span>'
            f'</div>'
            f'<div class="wc-off">UTC {off_disp}</div>'
            f'<div class="wc-b">1st {_fmt_local(b1, z)}</div>'
            f'<div class="wc-b">2nd {_fmt_local(b2, z)}</div>'
            f'</div>'
        )
    return out


def institutional_confidence_index():
    """XRP Complete Institutional Confidence Index (ICI) — 0-100, rescaled from five real components
    unique to this site's own accumulated tracking. Every component is disclosed and computed
    from data already gathered elsewhere on the page; nothing here is invented or opaque."""
    comps = []

    # 1. Partnership Momentum — from our own growing Enterprise Ledger (detected deals only)
    detected_n = sum(1 for e in PARTNERSHIP_LEDGER if e["source"] == "detected")
    if detected_n >= 6:
        pm = 20
    elif detected_n >= 3:
        pm = 15
    elif detected_n >= 1:
        pm = 10
    else:
        pm = 5
    comps.append(("Partnership Momentum", f"{detected_n} new deals detected", pm))

    # 2. Developer Activity — from live XRPL GitHub tracking
    dev_commits = GITHUB_DEV.get("rippled_7d", 0) + GITHUB_DEV.get("other_7d", 0)
    if dev_commits >= 16:
        da = 20
    elif dev_commits >= 6:
        da = 15
    elif dev_commits >= 1:
        da = 10
    else:
        da = 5
    comps.append(("Developer Activity", f"{dev_commits} commits/7d", da))

    # 3. Smart Money Positioning — rescale the existing Smart Money Score (0-100 -> 0-20)
    sm = smart_money()
    smp = round(sm["score"] / 100 * 20)
    comps.append(("Smart Money Positioning", f'{sm["score"]}/100 \u2014 {sm["label"]}', smp))

    # 4. Executive Tone — sentiment across real statements in the Ripple Exec Tracker
    ex_stories = EXEC_TRACKER.get("stories", [])
    if ex_stories:
        ex_bull = sum(1 for s in ex_stories if _sentiment(s["title"]) == "bullish")
        ex_bear = sum(1 for s in ex_stories if _sentiment(s["title"]) == "bearish")
        ex_share = (ex_bull - ex_bear) / len(ex_stories)
        et = round(10 + ex_share * 10)
        et = max(0, min(20, et))
        et_disp = f"{ex_bull} positive / {ex_bear} negative of {len(ex_stories)}"
    else:
        et, et_disp = 10, "Awaiting statements"
    comps.append(("Executive Tone", et_disp, et))

    # 5. Regulatory Momentum — CLARITY Act tracker fill + net sentiment of Legal/Reg news
    ca_n = len(CLARITY_ACT_STORIES)
    pool = NEWS.get("pool", [])
    reg_stories = [s for s in pool if s.get("category") in ("Legal", "Reg")]
    if reg_stories:
        reg_bull = sum(1 for s in reg_stories if s["sentiment"] == "bullish")
        reg_bear = sum(1 for s in reg_stories if s["sentiment"] == "bearish")
        reg_share = (reg_bull - reg_bear) / len(reg_stories)
    else:
        reg_share = 0
    rm = round((ca_n / 10) * 10 + (reg_share * 10 + 10) / 2)
    rm = max(0, min(20, rm))
    comps.append(("Regulatory Momentum", f"{ca_n}/10 CLARITY Act stories tracked", rm))

    score = sum(c[2] for c in comps)
    if score >= 80:
        label, col = "Institutional Grade", "var(--gr)"
    elif score >= 65:
        label, col = "Strong Confidence", "var(--gr)"
    elif score >= 50:
        label, col = "Moderate Confidence", "var(--yl)"
    elif score >= 35:
        label, col = "Cautious", "var(--or)"
    else:
        label, col = "Low Confidence", "var(--rd)"
    return {"score": score, "label": label, "color": col, "comps": comps}


def signal_score():
    """Composite 0-100, rescaled from the 4 components we have real data for:
    Price Momentum (15), RSI (12), Sentiment (15), Fear & Greed (5) = 47 max."""
    chg = MARKET.get("xrp_chg")
    rsi = MARKET.get("rsi_1d")
    fng = MARKET.get("fng")
    total, bull, bear, _ = signal_stats()

    if chg is None:   pm = 5
    elif chg > 5:     pm = 15
    elif chg > 2:     pm = 12
    elif chg > 0:     pm = 8
    elif chg > -2:    pm = 5
    elif chg > -5:    pm = 3
    else:             pm = 0

    if not rsi:              rv = 8
    elif 30 <= rsi <= 40:    rv = 12
    elif 40 < rsi <= 50:     rv = 10
    elif 50 < rsi <= 60:     rv = 8
    elif 60 < rsi <= 70:     rv = 6
    elif rsi > 70:           rv = 3
    else:                    rv = 5

    ratio = (bull / total) if total else 0
    if not total:        se = 7
    elif ratio > 0.5:    se = 15
    elif ratio > 0.35:   se = 11
    elif ratio > 0.25:   se = 7
    elif ratio > 0.15:   se = 4
    else:                se = 1

    if fng is None:   fg = 2
    elif fng <= 20:   fg = 5
    elif fng <= 40:   fg = 4
    elif fng <= 60:   fg = 2
    elif fng <= 80:   fg = 1
    else:             fg = 0

    score = round((pm + rv + se + fg) / 47 * 100)
    if   score >= 75: label, col = "STRONG",   "var(--gr)"
    elif score >= 60: label, col = "BULLISH",  "var(--gr)"
    elif score >= 45: label, col = "NEUTRAL",  "var(--yl)"
    elif score >= 30: label, col = "CAUTIOUS", "var(--or)"
    else:             label, col = "BEARISH",  "var(--rd)"
    return {"score": score, "label": label, "color": col}

def smart_money():
    """Smart Money Score (0-100), rescaled from the components with real data:
    RSI 1D, Sentiment, Funding Rate. Higher = accumulation, lower = distribution."""
    rsi = MARKET.get("rsi_1d")
    total, bull, bear, _ = signal_stats()
    fund = MARKET.get("funding")
    comps = []

    if rsi:
        if rsi < 30:   rs = 85
        elif rsi < 45: rs = 70
        elif rsi < 55: rs = 55
        elif rsi < 70: rs = 40
        else:          rs = 25
        comps.append(("RSI 1D", f"{rsi:.1f}", rs))

    if total:
        share = bull / total * 100
        if share >= 60:   ss = 75
        elif share >= 45: ss = 62
        elif share >= 30: ss = 52
        elif share >= 15: ss = 42
        else:             ss = 32
        comps.append(("Sentiment", f"{round(share)}% bullish", ss))

    if fund is not None:
        fpct = fund * 100
        if fpct < -0.01:  fs = 80
        elif fpct < 0.01: fs = 62
        elif fpct < 0.05: fs = 46
        else:             fs = 30
        comps.append(("Funding Rate", f"{fpct:+.4f}%", fs))

    score = round(sum(c[2] for c in comps) / len(comps)) if comps else 50
    if   score < 35: label, col = "Distribution", "var(--rd)"
    elif score < 45: label, col = "Cautious", "var(--or)"
    elif score < 55: label, col = "Neutral / Mixed", "var(--yl)"
    elif score < 70: label, col = "Accumulation", "var(--gr)"
    else:            label, col = "Strong Accumulation", "var(--gr)"
    return {"score": score, "label": label, "color": col, "comps": comps}

def _fng_color(v):
    if v <= 25: return "var(--rd)"
    if v <= 45: return "var(--or)"
    if v <= 55: return "var(--yl)"
    if v <= 75: return "var(--gr)"
    return "var(--tq)"

def news_mention_volume_html():
    """News Mention Volume for 'yesterday' \u2014 real counts from the site's own
    306+ RSS feeds, never estimated. Resets at 00:15 UTC (the 15-minute
    buffer lets the last fetch cycle of the prior day land before the
    figure locks in as final)."""
    now = datetime.now(timezone.utc)
    if now.hour == 0 and now.minute < 15:
        target = (now - timedelta(days=2)).date()
    else:
        target = (now - timedelta(days=1)).date()
    day_str = target.isoformat()
    day_label = target.strftime("%A, %B %d")
    bucket = NEWS_VOLUME_HISTORY.get(day_str)

    if not bucket or bucket["total"] == 0:
        return (
            '<div class="home-base"><div class="home-base-icon">\U0001F4F0</div>'
            '<div class="home-base-title">Building Today\'s Count</div>'
            '<div class="home-base-sub">This tracker started counting from deploy \u2014 a full '
            "day's honest figure will appear here once one complete day has passed. "
            "Nothing here is ever estimated or backfilled.</div></div>", day_label, 0, 0, ""
        )

    total = bucket["total"]
    contributors = len(bucket["sources"])
    cats = sorted(bucket["by_cat"].items(), key=lambda kv: -kv[1])[:8]
    max_cat = max((n for _, n in cats), default=1) or 1
    cat_rows = "".join(
        f'<div class="nmv-row"><span class="nmv-cat">{html.escape(cat)}</span>'
        f'<div class="nmv-bar-track"><div class="nmv-bar-fill" style="width:{n / max_cat * 100:.0f}%"></div></div>'
        f'<span class="nmv-n">{n}</span></div>'
        for cat, n in cats
    )
    return cat_rows, day_label, total, contributors, day_str


def historical_30d_html():
    """30-Day Historical Price Data table \u2014 real daily OHLC from the same
    Coinbase candles already powering RSI/52-week/etc. No new API, no
    estimation."""
    rows = MARKET.get("hist_30d") or []
    if not rows:
        return '<div class="home-base"><div class="home-base-icon">\U0001F4C5</div>' \
               '<div class="home-base-title">Building History</div>' \
               '<div class="home-base-sub">30 days of daily price history populates on deploy.</div></div>'
    out = []
    prev_close = None
    for r in rows:
        d = datetime.fromtimestamp(r["t"], tz=timezone.utc)
        date_str = d.strftime("%b %d, %Y")
        day_str = d.strftime("%A")
        o, h, l, c = r["o"], r["h"], r["l"], r["c"]
        if prev_close:
            chg = c - prev_close
            pct = (chg / prev_close * 100) if prev_close else 0
            chg_col = "var(--gr)" if chg >= 0 else "var(--rd)"
            chg_str = f'{"+" if chg >= 0 else ""}{chg:.4f}'
            pct_str = f'{"+" if pct >= 0 else ""}{pct:.2f}%'
        else:
            chg_col, chg_str, pct_str = "var(--tx)", "\u2014", "\u2014"
        out.append(
            f'<tr><td>{date_str}</td><td>{day_str}</td>'
            f'<td>${o:.4f}</td><td>${h:.4f}</td><td>${l:.4f}</td><td>${c:.4f}</td>'
            f'<td style="color:{chg_col}">{chg_str}</td><td style="color:{chg_col}">{pct_str}</td></tr>'
        )
        prev_close = c
    out.reverse()  # newest first for display
    return (
        '<table class="hist-table"><thead><tr>'
        '<th>Date</th><th>Day</th><th>Open</th><th>High</th><th>Low</th><th>Close</th>'
        '<th>$ Change</th><th>% Change</th></tr></thead><tbody>'
        + "".join(out) + "</tbody></table>"
    )


def fng_history_html():
    hist = MARKET.get("fng_history") or []
    if not hist:
        return '<div class="empty">Fear &amp; Greed history populates on deploy.</div>'
    bars = ""
    n = len(hist)
    for i, v in enumerate(hist):
        col = _fng_color(v)
        h = max(6, min(100, v))
        last = " fg-today" if i == n - 1 else ""
        bars += f'<div class="fg-bar{last}" style="height:{h}%;background:{col}" title="{v}"></div>'
    return bars

REGION_DISPLAY = {"Japan": "Japan", "Korea": "Korea", "UAE": "UAE/Middle East", "Europe": "Europe",
                  "India": "India", "LatAm": "Latin America", "Africa": "Africa", "SEA": "SE Asia"}

def regional_heatmap_html():
    pool = NEWS.get("pool", [])
    counts = {r: 0 for r in REGIONS}
    for s in pool:
        r = s.get("region")
        if r in counts:
            counts[r] += 1
    mx = max(counts.values()) if counts else 0
    cards = ""
    for reg in REGIONS:
        c = counts[reg]
        if mx and c:
            inten = c / mx
            bg = f"rgba(72,255,130,{0.06 + inten * 0.22:.2f})"
            bd = f"rgba(72,255,130,{0.25 + inten * 0.45:.2f})"
            num_col = "var(--gr)"
        else:
            bg = "var(--s2)"
            bd = "var(--b)"
            num_col = "var(--tx)"
        cards += (
            f'<div class="rh-card" style="background:{bg};border-color:{bd}">'
            f'<div class="rh-flag">{REGION_FLAGS.get(reg, "")}</div>'
            f'<div class="rh-name">{REGION_DISPLAY.get(reg, reg)}</div>'
            f'<div class="rh-num" style="color:{num_col}">{c}</div>'
            f'<div class="rh-lbl">stories today</div>'
            f'</div>'
        )
    return cards


def velocity_chart_html():
    buckets = news_velocity_24h()
    mx = max(buckets) or 1
    return "".join(
        f'<div class="vel-bar" style="height:{max(6, v / mx * 100):.0f}%" title="{v} stories"></div>'
        for v in buckets
    )


def sentiment_trend_html():
    days = sorted(SENTIMENT_HISTORY.keys())
    if not days:
        return '<div class="empty">Sentiment history builds day by day as the server runs \u2014 check back soon.</div>'
    mx = max(SENTIMENT_HISTORY[d]["total"] for d in days) or 1
    bars = ""
    for d in days:
        b = SENTIMENT_HISTORY[d]
        h = max(6, b["total"] / mx * 100)
        if b["bull"] > b["bear"]:
            col = "var(--gr)"
        elif b["bear"] > b["bull"]:
            col = "var(--rd)"
        else:
            col = "var(--tx)"
        title = f'{d}: {b["bull"]} bull / {b["bear"]} bear / {b["neut"]} neutral'
        bars += f'<div class="sdt-bar" style="height:{h:.0f}%;background:{col}" title="{title}"></div>'
    return bars


def sentiment_leaderboard_html():
    rows = sentiment_source_table()
    if not rows:
        return '<tr><td colspan="6" class="empty">Feeds loading\u2026</td></tr>'
    out = ""
    for i, r in enumerate(rows, 1):
        t = max(r["total"], 1)
        bull_pct = r["bull"] / t * 100
        bear_pct = r["bear"] / t * 100
        out += (
            f'<tr><td>{i}</td><td style="color:var(--br);font-weight:700">{html.escape(r["name"])}</td>'
            f'<td style="text-align:center">{r["total"]}</td>'
            f'<td style="text-align:center;color:var(--gr)">{r["bull"]}</td>'
            f'<td style="text-align:center;color:var(--rd)">{r["bear"]}</td>'
            f'<td><div class="sent-bar-mini"><span style="width:{bull_pct:.0f}%;background:var(--gr)"></span>'
            f'<span style="width:{bear_pct:.0f}%;background:var(--rd)"></span></div></td>'
            f'<td style="text-align:center;color:var(--yl)">{r["breaking"] or "\u2014"}</td></tr>'
        )
    return out


def exec_tracker_html():
    stories = EXEC_TRACKER.get("stories", [])
    if not stories:
        return '<div class="home-base"><div class="home-base-icon">\U0001F3A4</div><div class="home-base-title">Monitoring Executive Statements</div><div class="home-base-sub">Public statements from Ripple\u2019s leadership team surface here automatically as they\u2019re published.</div></div>'
    out = ""
    for s in stories:
        out += (
            f'<div class="ex-row" data-tab="{s["tab"]}">'
            f'<div class="ex-top"><span class="ex-name">{html.escape(s["exec"])}</span>'
            f'<span class="ex-title">{html.escape(s["exec_title"])}</span>'
            f'<span class="ex-time">{_time_ago(s["dt"])}</span></div>'
            f'<a class="ex-hl" href="{html.escape(s["link"], quote=True)}" target="_blank" rel="noopener">{html.escape(s["title"])}</a>'
            f'</div>'
        )
    return out


def github_commits_html():
    commits = GITHUB_DEV.get("commits", [])
    if not commits:
        return '<div class="home-base"><div class="home-base-icon">\U0001F4BB</div><div class="home-base-title">Monitoring XRPL Development</div><div class="home-base-sub">Commits across rippled, xrpl-dev-portal and xrpl.js surface here automatically.</div></div>'
    out = ""
    for c in commits:
        out += (
            f'<div class="gh-row">'
            f'<span class="gh-repo">{html.escape(c["repo"])}</span>'
            f'<a class="gh-msg" href="{html.escape(c["url"], quote=True)}" target="_blank" rel="noopener">{html.escape(c["msg"] or "(no message)")}</a>'
            f'<span class="gh-meta">{html.escape(c["author"])} \u00B7 {html.escape(c["date"])}</span>'
            f'</div>'
        )
    return out


def competitor_table_html():
    xrp_price = MARKET.get("xrp_price")
    xrp_chg = MARKET.get("xrp_chg")
    xrp_7d = MARKET.get("perf_1w")
    xrp_mcap = MARKET.get("mcap")

    def _row(sym, emoji, price, chg24, chg7d, mcap, edge, is_self):
        px = f"${price:.4f}" if price and price < 1 else (f"${price:,.2f}" if price else "\u2014")
        c24 = f'{chg24:+.2f}%' if chg24 is not None else "\u2014"
        c24col = "var(--gr)" if (chg24 or 0) >= 0 else "var(--rd)"
        c7 = f'{chg7d:+.2f}%' if chg7d is not None else "\u2014"
        c7col = "var(--gr)" if (chg7d or 0) >= 0 else "var(--rd)"
        mc = _fmt_usd(mcap)
        rowbg = "background:rgba(117,188,255,.06);border-left:3px solid var(--bl)" if is_self else ""
        symcol = "var(--bl)" if is_self else "var(--br)"
        edgecol = "var(--bl)" if is_self else "var(--tx)"
        return (
            f'<tr style="{rowbg}"><td><span style="margin-right:6px">{emoji}</span>'
            f'<span style="font-weight:900;color:{symcol}">{sym}</span></td>'
            f'<td style="text-align:right">{px}</td>'
            f'<td style="text-align:right;color:{c24col}">{c24}</td>'
            f'<td style="text-align:right;color:{c7col}">{c7}</td>'
            f'<td style="text-align:right;color:var(--tx)">{mc}</td>'
            f'<td style="color:{edgecol};max-width:260px">{edge}</td></tr>'
        )

    rows = _row("XRP", "\U0001FA99", xrp_price, xrp_chg, xrp_7d, xrp_mcap, "\U0001F3AF Tracking live", True)
    for c in COMPETITORS:
        e = MARKET["competitors"].get(c["id"], {})
        rows += _row(c["symbol"], c["emoji"], e.get("price"), e.get("change_24h"), e.get("change_7d"),
                     e.get("mcap"), COMPETITOR_EDGE.get(c["symbol"], ""), False)
    return rows


def _rank_counts(items):
    counts = {}
    for it in items:
        counts[it] = counts.get(it, 0) + 1
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)

def lb_sources_html(n=6):
    rows = _rank_counts([s["source"] for s in NEWS.get("pool", [])])[:n]
    if not rows:
        return '<div class="lb-empty">Feeds loading\u2026</div>'
    out = ""
    for i, (src, cnt) in enumerate(rows, 1):
        out += (f'<div class="lb-row"><span class="lb-rank">{i}</span>'
                f'<span class="lb-name">{html.escape(src)}</span>'
                f'<span class="lb-cnt">{cnt}</span></div>')
    return out

def lb_regions_html(n=8):
    rows = _rank_counts([s["region"] for s in NEWS.get("pool", []) if s.get("region")])[:n]
    if not rows:
        return '<div class="lb-empty">Feeds loading\u2026</div>'
    out = ""
    for i, (reg, cnt) in enumerate(rows, 1):
        out += (f'<div class="lb-row"><span class="lb-rank">{i}</span>'
                f'<span class="lb-name">{REGION_FLAGS.get(reg, "")} {reg}</span>'
                f'<span class="lb-cnt">{cnt}</span></div>')
    return out

def regional_discourse_html():
    pool = NEWS.get("pool", [])
    sig_col = {"bullish": "var(--gr)", "bearish": "var(--rd)", "neutral": "var(--yl)", "quiet": "var(--tx)"}
    cards = ""
    for reg in REGIONS:
        rs = sorted([s for s in pool if s.get("region") == reg], key=lambda s: s["dt"], reverse=True)
        n = len(rs)
        if rs:
            b = sum(1 for s in rs if s["sentiment"] == "bullish")
            r = sum(1 for s in rs if s["sentiment"] == "bearish")
            sig = "bullish" if b > r else "bearish" if r > b else "neutral"
            top = html.escape(rs[0]["title"])
        else:
            sig = "quiet"
            top = "No regional stories yet \u2014 feeds are loading."
        col = sig_col[sig]
        cards += (
            f'<div class="rd-card">'
            f'<div class="rd-top"><span class="rd-name">{REGION_FLAGS[reg]} {reg}</span>'
            f'<span class="rd-sig" style="color:{col};border-color:{col}">{sig}</span></div>'
            f'<div class="rd-count">{n} stor{"y" if n == 1 else "ies"}</div>'
            f'<div class="rd-hl">{top}</div>'
            f'</div>'
        )
    return cards


def next_escrow_release():
    """Ripple releases 1B XRP from escrow on the 1st of each month (00:00 UTC)."""
    now = datetime.now(timezone.utc)
    if now.month == 12:
        nxt = now.replace(year=now.year + 1, month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        nxt = now.replace(month=now.month + 1, day=1, hour=0, minute=0, second=0, microsecond=0)
    return nxt


ECOSYSTEM_CARDS = [
    {"ic": "\U0001F517", "name": "XRPL", "role": "The Foundation", "color": "var(--tq)",
     "bg": "rgba(0,229,204,.06)", "bd": "rgba(0,229,204,.3)",
     "desc": "Open-source, decentralised blockchain maintained by the independent XRPL Foundation. Consensus settles in 3-5 seconds. Native DEX, AMM pools, escrow, and payment channels built in at the protocol level.",
     "stats": [("Total Accounts", "6.4M+"), ("Settlement", "3-5 seconds"), ("Tx Fee", "~$0.0002")]},
    {"ic": "\U0001F3E2", "name": "Ripple Labs", "role": "The Company", "color": "var(--bl)",
     "bg": "rgba(117,188,255,.06)", "bd": "rgba(117,188,255,.3)",
     "desc": "Private San Francisco company that created XRP and builds enterprise blockchain solutions. NOT the same as XRPL. Revenue from ODL, software licensing, and XRP sales. Led by Brad Garlinghouse.",
     "stats": [("Founded", "2012"), ("HQ", "San Francisco + Dubai"), ("SEC Case", "\u2705 Settled 2025")]},
    {"ic": "\U0001F48E", "name": "XRP", "role": "The Asset", "color": "var(--gr)",
     "bg": "rgba(72,255,130,.06)", "bd": "rgba(72,255,130,.3)",
     "desc": "Native digital asset of the XRPL. Used as bridge currency in ODL, transaction gas, and wallet reserve. Fixed supply of 100 billion \u2014 no mining, no inflation. Burned slightly with every transaction.",
     "stats": [("Total Supply", "100B XRP"), ("Circulating", "~62B XRP"), ("In Escrow", "~43B XRP")]},
    {"ic": "\U0001F310", "name": "RippleNet", "role": "The Network", "color": "var(--or)",
     "bg": "rgba(255,153,0,.06)", "bd": "rgba(255,153,0,.3)",
     "desc": "Ripple's B2B payment network connecting 300+ financial institutions globally. Three tiers: Direct (messaging), Multi-hop (routing), and ODL (XRP bridge). Banks choose their level of XRP integration.",
     "stats": [("Partners", "300+ institutions"), ("Countries", "55+"), ("Type", "Enterprise B2B")]},
    {"ic": "\u26A1", "name": "ODL", "role": "On-Demand Liquidity", "color": "var(--rd)",
     "bg": "rgba(255,64,96,.06)", "bd": "rgba(255,64,96,.3)",
     "desc": "Instant cross-border settlement that converts fiat to XRP, moves it on the XRPL in seconds, then converts to the destination fiat \u2014 removing pre-funded accounts.",
     "stats": [("Active Corridors", "8+"), ("Settlement", "3-5 seconds"), ("Savings vs SWIFT", "Up to 60%")]},
    {"ic": "\U0001F4B5", "name": "RLUSD", "role": "The Stablecoin", "color": "var(--bl)",
     "bg": "rgba(117,188,255,.06)", "bd": "rgba(117,188,255,.3)",
     "desc": "Ripple's USD-pegged stablecoin launched December 2024. Runs natively on the XRPL and Ethereum, fully backed and regulated.",
     "stats": [("Peg", "1:1 USD"), ("Regulator", "NYDFS"), ("Networks", "XRPL + ETH")]},
    {"ic": "\U0001F6E0\uFE0F", "name": "XRPL Dev", "role": "Developer Layer", "color": "var(--tq)",
     "bg": "rgba(0,229,204,.06)", "bd": "rgba(0,229,204,.3)",
     "desc": "Tools, standards, and programmability: Hooks (lightweight smart contracts), AMM, native tokens, and multi-purpose tokens \u2014 expanding what builders can ship on the ledger.",
     "stats": [("Smart Contracts", "Hooks"), ("Native AMM", "Live"), ("Tokens", "IOU + MPT")]},
    {"ic": "\U0001F6E1\uFE0F", "name": "Validators", "role": "Consensus Layer", "color": "var(--yl)",
     "bg": "rgba(255,204,0,.06)", "bd": "rgba(255,204,0,.3)",
     "desc": "Independent validators worldwide run the consensus protocol, agreeing on ledger state every 3-5 seconds with no mining. A Unique Node List keeps the network decentralised, fast, and energy-efficient.",
     "stats": [("Validators", "150+"), ("Consensus", "RPCA"), ("Energy", "Carbon-neutral")]},
]


def ecosystem_cards_html():
    out = ""
    for c in ECOSYSTEM_CARDS:
        stats = "".join(
            f'<div class="eco-stat"><span class="k">{k}</span>'
            f'<span style="color:{c["color"]};font-weight:700">{v}</span></div>'
            for k, v in c["stats"]
        )
        out += (
            f'<div class="eco-card" style="background:{c["bg"]};border:1px solid {c["bd"]}">'
            f'<div class="eco-bar" style="background:linear-gradient(90deg,{c["color"]},transparent)"></div>'
            f'<div class="eco-ic">{c["ic"]}</div>'
            f'<div class="eco-name">{c["name"]}</div>'
            f'<div class="eco-role" style="color:{c["color"]}">{c["role"]}</div>'
            f'<div class="eco-desc">{c["desc"]}</div>'
            f'{stats}'
            f'</div>'
        )
    return out


# ─────────────────────────────────────────────────────────────────────
# MAINSTREAM INTEGRATION + INSTITUTIONAL PARTNERSHIPS (static reference)
# ─────────────────────────────────────────────────────────────────────
STATUS_COLORS = {
    "CONFIRMED": "var(--gr)",
    "LIVE":      "var(--gr)",
    "EXPLORING": "var(--bl)",
    "RUMORED":   "var(--yl)",
    "PILOT":     "var(--or)",
    "COMPETING": "var(--rd)",
}
STATUS_TINT = {
    "CONFIRMED": "rgba(72,255,130,.35)",
    "LIVE":      "rgba(72,255,130,.35)",
    "EXPLORING": "rgba(117,188,255,.35)",
    "RUMORED":   "rgba(255,204,0,.35)",
    "PILOT":     "rgba(255,153,0,.35)",
    "COMPETING": "rgba(255,64,96,.35)",
}
STATUS_EMOJI = {
    "CONFIRMED": "\u2705",
    "LIVE":      "\u2705",
    "EXPLORING": "\U0001F50D",
    "RUMORED":   "\U0001F4AC",
    "PILOT":     "\U0001F9EA",
    "COMPETING": "\u2694\uFE0F",
}

# Institutional Partnership Tracker — 20 institutions (screenshot order) = 5 rows of 4
# (name, type, flag, status, detail, source)
INSTITUTIONS = [
    ("Bank of America", "Bank", "\U0001F1FA\U0001F1F8", "RUMORED", "Multiple reports suggest BofA exploring Ripple ODL for cross-border settlement. Not officially confirmed.", "Industry reports 2025-2026"),
    ("JPMorgan Chase", "Bank", "\U0001F1FA\U0001F1F8", "EXPLORING", "JPM Coin runs on a private blockchain but JPMorgan has engaged with ISO 20022 standards compatible with XRPL. Watching closely.", "Bloomberg 2025"),
    ("SBI Holdings", "Bank", "\U0001F1EF\U0001F1F5", "CONFIRMED", "SBI Ripple Asia \u2014 joint venture fully operational. SBI VC Trade, SBI Remit, and MoneyTap all run on Ripple technology.", "SBI Holdings IR 2024"),
    ("Santander", "Bank", "\U0001F1EA\U0001F1F8", "CONFIRMED", "One Pay FX powered by Ripple since 2018. Expanded to multiple markets. One of the earliest major bank adopters.", "Santander Press Release"),
    ("Standard Chartered", "Bank", "\U0001F1EC\U0001F1E7", "CONFIRMED", "SC Ventures partnership with Ripple for cross-border payments in Asia-Pacific corridors.", "Standard Chartered 2023"),
    ("PNC Bank", "Bank", "\U0001F1FA\U0001F1F8", "CONFIRMED", "PNC joined RippleNet for cross-border payment capabilities. One of the largest US banks on the network.", "Ripple Press Release"),
    ("Ita\u00FA Unibanco", "Bank", "\U0001F1E7\U0001F1F7", "CONFIRMED", "Brazil's largest private bank partnered with Ripple for international transfers via RippleNet.", "Ripple Blog 2023"),
    ("Axis Bank", "Bank", "\U0001F1EE\U0001F1F3", "CONFIRMED", "Axis Bank uses RippleNet for inbound remittances into India. Major corridor from Gulf states.", "Ripple Partner Network"),
    ("Tranglo", "Payments", "\U0001F1F8\U0001F1EC", "CONFIRMED", "Ripple acquired 40% stake in Tranglo. Powers ODL across SE Asia including Philippines, Malaysia, Indonesia.", "Ripple Acquisition 2021"),
    ("Coins.ph", "Payments", "\U0001F1F5\U0001F1ED", "CONFIRMED", "Philippines-based wallet using ODL for the US-Philippines corridor. Millions of OFW remittances monthly.", "Ripple ODL Partner"),
    ("Bitso", "Exchange", "\U0001F1F2\U0001F1FD", "CONFIRMED", "Mexico's largest crypto exchange. Primary ODL partner for the USA-Mexico corridor \u2014 the largest ODL corridor globally.", "Bitso/Ripple 2021"),
    ("Western Union", "Payments", "\U0001F1FA\U0001F1F8", "EXPLORING", "WU tested Ripple technology in 2018 pilots. No full deployment but ongoing ISO 20022 alignment is notable.", "WU Annual Report 2023"),
    ("MoneyGram", "Payments", "\U0001F1FA\U0001F1F8", "EXPLORING", "Former deep Ripple partner (2019-2021). Regulatory pressure caused pause. Re-engagement rumored post-SEC settlement.", "Industry reports 2025"),
    ("Modulr", "Fintech", "\U0001F1EC\U0001F1E7", "CONFIRMED", "UK fintech using RippleNet for European payment infrastructure. Backed by PayPal Ventures.", "Ripple Partner 2023"),
    ("Bank of Bhutan", "Central Bank", "\U0001F1E7\U0001F1F9", "CONFIRMED", "National digital currency (Druk) built on XRPL. First sovereign digital currency on the XRP Ledger.", "Royal Monetary Authority 2023"),
    ("SWIFT", "Network", "\U0001F310", "COMPETING", "SWIFT gpi is ISO 20022 compliant \u2014 same standard as XRPL. Direct competitive overlap. SWIFT Connect explores DLT bridges.", "SWIFT 2024"),
    ("Nasdaq", "Exchange", "\U0001F1FA\U0001F1F8", "EXPLORING", "Nasdaq applied for XRP ETF custody services. Potential listing venue for spot XRP ETF products.", "SEC Filings 2025"),
    ("Fidelity", "Asset Manager", "\U0001F1FA\U0001F1F8", "EXPLORING", "Fidelity Digital Assets expanding custody. XRP support rumored post-SEC settlement clarity.", "Industry reports 2026"),
    ("BlackRock", "Asset Manager", "\U0001F1FA\U0001F1F8", "EXPLORING", "BlackRock BUIDL fund uses blockchain infrastructure. XRP Ledger compatibility being evaluated.", "BlackRock Digital 2025"),
    ("Ripple \u00D7 BIS", "Research", "\U0001F310", "CONFIRMED", "Bank for International Settlements Project Nexus exploring XRPL for multi-CBDC settlements between central banks.", "BIS Innovation Hub 2024"),
]

# Sovereign / CBDC projects (kept for a future dedicated section; not rendered here)
PARTNERSHIPS = [
    ("Bhutan", "\U0001F1E7\U0001F1F9", "Druk Digital", "LIVE", "National digital currency on XRPL. Royal Monetary Authority partnership."),
    ("Palau", "\U0001F1F5\U0001F1FC", "Palau Stablecoin", "LIVE", "PSC, a USD-backed digital currency on XRPL for government payments."),
    ("Montenegro", "\U0001F1F2\U0001F1EA", "Digital Euro Pilot", "PILOT", "Central Bank of Montenegro piloting digital euro infrastructure on XRPL."),
    ("Hong Kong", "\U0001F1ED\U0001F1F0", "HKD CBDC", "PILOT", "HKMA participating in Project mBridge. Ripple in discussion for the XRPL settlement layer."),
    ("Colombia", "\U0001F1E8\U0001F1F4", "Banco de la Rep\u00FAblica", "EXPLORING", "Colombia's central bank exploring XRPL for digital peso settlement infrastructure."),
    ("Georgia", "\U0001F1EC\U0001F1EA", "Digital GEL", "EXPLORING", "National Bank of Georgia exploring Ripple technology for a national digital currency."),
]

INTEGRATION_TIMELINE = [
    ("2012", "Ripple Founded", "OpenCoin (later Ripple) created with a mission to replace correspondent banking.", False),
    ("2018", "First Bank Partnerships", "Santander One Pay FX and American Express FX International Payments launch on RippleNet.", True),
    ("2019", "ODL Goes Live", "On-Demand Liquidity launches commercially. XRP used as a bridge currency at scale for the first time.", True),
    ("2020", "SEC Lawsuit", "SEC files suit \u2014 temporarily freezing institutional adoption in the US. Global expansion continues.", False),
    ("2021", "SBI + Tranglo", "SBI Holdings scales Japan operations. Ripple acquires 40% of Tranglo \u2014 an SE Asia ODL hub.", True),
    ("2022", "SWIFT ISO 20022", "SWIFT mandates ISO 20022 migration \u2014 the same standard XRPL natively supports. Alignment begins.", True),
    ("2023", "Bhutan CBDC Live", "Bank of Bhutan launches a national digital currency on XRPL. First sovereign CBDC on the ledger.", True),
    ("2023", "Partial Legal Victory", "Judge Torres: XRP is not a security in programmatic sales. US institutional adoption starts thawing.", True),
    ("2024", "XRPL EVM Sidechain", "An Ethereum-compatible sidechain launches on XRPL \u2014 opening DeFi and smart-contract integration.", True),
    ("2025", "SEC Settlement", "SEC drops the case. $50M settlement. Full US regulatory clarity arrives; institutional floodgates open.", True),
    ("2025", "ETF Filings Wave", "Bitwise, WisdomTree, and Canary Capital file US spot XRP ETF applications. European ETPs already live.", True),
    ("2026", "TradFi Integration Era", "Banks, asset managers, and payment networks actively building on XRPL. Post-lawsuit adoption accelerating.", True),
]

def timeline_html():
    out = ""
    for year, event, detail, major in INTEGRATION_TIMELINE:
        dot_col = "var(--gr)" if major else "var(--yl)"
        dot_sz  = "16px" if major else "11px"
        yr_col  = "var(--gr)" if major else "var(--yl)"
        out += (
            f'<div class="tl-node">'
            f'<div class="tl-top">'
            f'<div class="tl-year" style="color:{yr_col}">{year}</div>'
            f'<div class="tl-dot" style="width:{dot_sz};height:{dot_sz};background:{dot_col}"></div>'
            f'</div>'
            f'<div class="tl-event">{event}</div>'
            f'<div class="tl-detail">{detail}</div>'
            f'</div>'
        )
    return out


def institution_cards_html():
    out = ""
    for name, kind, flag, status, detail, source in INSTITUTIONS:
        col   = STATUS_COLORS.get(status, "var(--tx)")
        tint  = STATUS_TINT.get(status, "var(--b)")
        emoji = STATUS_EMOJI.get(status, "")
        out += (
            f'<div class="trk-card" data-status="{status}" style="border:1px solid {tint}">'
            f'<div class="trk-top">'
            f'<span class="trk-status">{flag} {emoji} <span style="color:{col}">{status}</span></span>'
            f'<span class="trk-type">{kind}</span>'
            f'</div>'
            f'<div class="trk-name">{name}</div>'
            f'<div class="trk-detail">{detail}</div>'
            f'<div class="trk-src">{source}</div>'
            f'</div>'
        )
    return out



# ─────────────────────────────────────────────────────────────────────
# PREFLIGHT
# ─────────────────────────────────────────────────────────────────────
def run_preflight():
    checks = []
    checks.append(("Flask app responding", True, "Server handled the request"))
    checks.append(("Version string present", bool(APP_VERSION), f"Reporting version {APP_VERSION}"))
    try:
        up = (datetime.now(timezone.utc) - BOOT_TIME).total_seconds()
        checks.append(("Uptime clock running", up >= 0, f"{int(up)} seconds since boot"))
    except Exception as e:
        checks.append(("Uptime clock running", False, str(e)))
    port = os.environ.get("PORT", "8080")
    checks.append(("Port configured", bool(port), f"PORT={port}"))

    passed = sum(1 for _, ok, _ in checks if ok)
    total  = len(checks)
    overall = "PASS" if passed == total else "FAIL"
    # informational (does not affect PASS/FAIL)
    checks.append(("Live data sources", True,
                   f"{MARKET['sources_active']}/{MARKET['sources_total']} connected"))
    return checks, passed, total, overall


# ─────────────────────────────────────────────────────────────────────
# PAGE
# ─────────────────────────────────────────────────────────────────────
TECH_SPECS = [
    ("Max TPS", "1,500", "~30", "65,000", "7"),
    ("Settlement", "3-5 sec", "12 sec", "0.4 sec", "60 min"),
    ("Tx Fee", "$0.0002", "$1-50", "$0.001", "$1-20"),
    ("Energy Use", "0.0079 kWh", "0.03 kWh", "0.00051 kWh", "1,173 kWh"),
    ("Consensus", "FBC", "PoS", "PoH+PoS", "PoW"),
    ("ISO 20022", "\u2705 Native", "\u274C No", "\u274C No", "\u274C No"),
    ("Supply Cap", "100B fixed", "Unlimited", "Fixed", "21M"),
]

USE_CASES = [
    ("\u26A1", "Cross-Border Payments (ODL)", "var(--gr)",
     "Banks use XRP as bridge currency to eliminate pre-funded nostro accounts. Saves up to 60% vs SWIFT. Active in 8+ corridors."),
    ("\U0001F4B5", "RLUSD Stablecoin Settlement", "var(--bl)",
     "NYDFS-regulated USD stablecoin on XRPL. Enables stable-value settlement while XRP handles liquidity bridge function."),
    ("\U0001F3DB\uFE0F", "Central Bank Digital Currency", "var(--yl)",
     "Bhutan (live), Montenegro (pilot), Palau (live), Colombia, Hong Kong exploring XRPL as CBDC settlement layer."),
    ("\U0001F3A8", "NFT Marketplace (XLS-20)", "var(--tq)",
     "Native NFT standard on XRPL. Low-fee minting ($0.0002), instant settlement. Multiple marketplaces active."),
    ("\U0001F4C8", "Tokenized Real-World Assets", "var(--or)",
     "Sologenic tokenizes stocks/ETFs on XRPL. Institutional-grade settlement infrastructure for the RWA market."),
    ("\u2697\uFE0F", "DeFi & AMM Protocols", "var(--rd)",
     "Native AMM live on XRPL mainnet. DEX built into protocol level. No smart contract risk \u2014 settlement at protocol layer."),
    ("\U0001F517", "ISO 20022 Payment Rails", "var(--gr)",
     "XRPL natively supports ISO 20022 data fields \u2014 the same standard SWIFT, Fedwire, CHAPS and TARGET2 are migrating to."),
    ("\U0001F310", "Micropayments & Streaming", "var(--bl)",
     "XRP enables sub-cent micropayments at $0.0002/tx \u2014 streaming money, API monetization, IoT payments."),
    ("\U0001F916", "AI Agent Payments", "var(--tq)",
     "Ripple integrating XRP/XRPL for AI agent-to-agent payments \u2014 instant, programmable, low-cost settlement."),
]

ENTERPRISE_CATEGORY_LABELS = {
    "A": "\U0001F680 ODL/XRP Live", "B": "\U0001F3DB\uFE0F Global Banks", "C": "\U0001F6E0\uFE0F Tech/Custody",
    "D": "\U0001F30D Regional", "E": "\U0001F7E1 ETF/Treasury",
}
ENTERPRISE_CATEGORY_COLORS = {"A": "var(--gr)", "B": "var(--bl)", "C": "var(--tq)", "D": "var(--or)", "E": "var(--yl)"}

ENTERPRISE_SEED = [
    # Category A: Live ODL / XRP Production Users (23)
    ("SBI Remit / SBI Holdings", "\U0001F1EF\U0001F1F5 Japan", "A", "LIVE ODL", "Multi-corridor APAC retail & commercial remittance powered by XRP"),
    ("Tranglo", "\U0001F1F2\U0001F1FE Malaysia/SE Asia", "A", "LIVE ODL", "Regional processing giant fully integrated into ODL"),
    ("Bitso", "\U0001F1F2\U0001F1FD Mexico/LatAm", "A", "LIVE ODL", "Core liquidity hub routing heavy institutional USD-to-MXN lanes"),
    ("Travelex Bank", "\U0001F1E7\U0001F1F7 Brazil", "A", "LIVE ODL", "First operational Latin American bank using XRP liquidity corridors"),
    ("Zand Bank", "\U0001F1E6\U0001F1EA UAE", "A", "LIVE", "Digital corporate bank processing payments via XRP and RLUSD"),
    ("AMINA Bank", "\U0001F1E8\U0001F1ED Switzerland", "A", "LIVE", "FINMA-regulated digital asset institution with live native Ripple Payments"),
    ("Siam Commercial Bank", "\U0001F1F9\U0001F1ED Thailand", "A", "LIVE ODL", "Active live ODL corridors for inbound Japanese capital"),
    ("UnionBank", "\U0001F1F5\U0001F1ED Philippines", "A", "LIVE ODL", "Automated processing for inbound domestic overseas worker remittances"),
    ("CIBC", "\U0001F1E8\U0001F1E6 Canada", "A", "LIVE ODL", "Settles institutional growth transfers via ODL infrastructure"),
    ("Qatar National Bank", "\U0001F1F6\U0001F1E6 Qatar", "A", "LIVE ODL", "Cross-border pipeline targeting Philippine remittance partners"),
    ("ChinaBank", "\U0001F1F5\U0001F1ED Philippines", "A", "LIVE", "Clears Gulf-region corporate payments anchored to digital liquidity"),
    ("Independent Reserve", "\U0001F1E6\U0001F1FA Australia", "A", "LIVE", "Regional liquidity exchange partner providing settlement architecture"),
    ("BTC Markets", "\U0001F1E6\U0001F1FA Australia", "A", "LIVE", "Currency bridge managing the AUD leg of regional ODL clearing"),
    ("Coins.ph", "\U0001F1F5\U0001F1ED Philippines", "A", "LIVE ODL", "Digital consumer network handling incoming XRP liquid conversions"),
    ("FlashFX", "\U0001F1E6\U0001F1FA Australia", "A", "LIVE ODL", "Automated FX software routing transfers via on-chain token paths"),
    ("Mercury FX", "\U0001F1EC\U0001F1E7 UK", "A", "LIVE ODL", "Enterprise currency platform processing instant commercial payments via XRP"),
    ("Cuallix", "\U0001F1FA\U0001F1F8/\U0001F1F2\U0001F1FD USA/Mexico", "A", "PIONEER", "First fintech to pilot original xRapid/ODL settlement engines"),
    ("X Money", "\U0001F310 Global", "A", "LIVE", "Retail cross-border digital financial platform using decentralized settlement"),
    ("Novatti", "\U0001F1E6\U0001F1FA Australia", "A", "LIVE ODL", "Payments processor using XRP ledger routes for Southeast Asian corridors"),
    ("iRemit", "\U0001F1F5\U0001F1ED Philippines", "A", "LIVE", "Non-bank remittance giant using ledger for real-time treasury management"),
    ("Azimo", "\U0001F1EA\U0001F1FA Europe", "A", "LIVE", "International digital money transmitter processing enterprise payouts"),
    ("Pyypl", "\U0001F30D Middle East/Africa", "A", "LIVE ODL", "Blockchain fintech offering consumer digital wallets via ODL"),
    ("MoneyMatch", "\U0001F1F2\U0001F1FE Malaysia", "A", "LIVE", "Digital conversion firm routing commercial payments to European endpoints"),
    # Category B: Global Banking Giants (32)
    ("Bank of America", "\U0001F1FA\U0001F1F8 USA", "B", "PILOT", "Infrastructure pilot participant holding patents referencing XRP settlement"),
    ("Banco Santander", "\U0001F1EA\U0001F1F8 Spain/UK", "B", "PRODUCTION", "Powers international One Pay FX app via RippleNet messaging"),
    ("PNC Bank", "\U0001F1FA\U0001F1F8 USA", "B", "PRODUCTION", "First major domestic U.S. institutional network client"),
    ("American Express", "\U0001F1FA\U0001F1F8 USA", "B", "PRODUCTION", "Commercial B2B international payments clearing partner"),
    ("Deutsche Bank", "\U0001F1E9\U0001F1EA Germany", "B", "PILOT", "Combined Ripple blockchain architecture with legacy SWIFT mechanisms"),
    ("Standard Chartered", "\U0001F1EC\U0001F1E7 UK", "B", "PRODUCTION", "Core early corporate investor and active digital clearing hub collaborator"),
    ("JPMorgan Chase", "\U0001F310 Global", "B", "PARTICIPANT", "Overlapping participant in multi-network settlement ledger groups"),
    ("HSBC", "\U0001F1EC\U0001F1E7 UK", "B", "PARTICIPANT", "Multi-national banking network mapped via active system routing IDs"),
    ("MUFG Bank", "\U0001F1EF\U0001F1F5 Japan", "B", "PRODUCTION", "Tier-1 retail giant optimizing transaction messaging across APAC"),
    ("ING Group", "\U0001F1F3\U0001F1F1 Netherlands", "B", "REGISTERED", "Multi-national bank registered in regional backend messaging directories"),
    ("BBVA", "\U0001F1EA\U0001F1F8 Spain", "B", "PILOT", "Corporate banking implementing cross-border branch liquidity trials"),
    ("Commonwealth Bank (CBA)", "\U0001F1E6\U0001F1FA Australia", "B", "PILOT", "Major retail institution participating in pilot ecosystem networks"),
    ("Westpac", "\U0001F1E6\U0001F1FA Australia", "B", "REGISTERED", "Registered network member maintaining live backend communication IDs"),
    ("ANZ Bank", "\U0001F1E6\U0001F1FA Australia", "B", "HISTORICAL", "Historical testing partner of the underlying clearing protocol"),
    ("National Australia Bank (NAB)", "\U0001F1E6\U0001F1FA Australia", "B", "REGISTERED", "Incorporated into the ledger settlement network indexing systems"),
    ("Macquarie Bank", "\U0001F1E6\U0001F1FA Australia", "B", "REGISTERED", "Financial and transaction group listed on official routing logs"),
    ("Royal Bank of Canada (RBC)", "\U0001F1E8\U0001F1E6 Canada", "B", "EXPLORING", "Explored the decentralized rail protocol for automated settlement"),
    ("SEB", "\U0001F1F8\U0001F1EA Sweden", "B", "PRODUCTION", "Operates high-volume corporate lines over Ripple software rails"),
    ("UBS", "\U0001F1E8\U0001F1ED Switzerland", "B", "EVALUATING", "Asset and investment firm evaluating high-speed distributed ledgers"),
    ("BMO Financial Group", "\U0001F1E8\U0001F1E6 Canada", "B", "EXPLORING", "North American commercial entity exploring cross-border clearing efficiency"),
    ("Intesa Sanpaolo", "\U0001F1EE\U0001F1F9 Italy", "B", "PARTICIPANT", "Enterprise participant tracking structural digital payment innovations"),
    ("Akbank", "\U0001F1F9\U0001F1F7 Turkey", "B", "PILOT", "Early regional banking partner conducting secure real-time automated tests"),
    ("Axis Bank", "\U0001F1EE\U0001F1F3 India", "B", "LIVE", "Live infrastructure client managing real-time regional transaction tunnels"),
    ("IndusInd Bank", "\U0001F1EE\U0001F1F3 India", "B", "LIVE", "Captures inbound international money transfers using decentralized engines"),
    ("Kotak Mahindra Bank", "\U0001F1EE\U0001F1F3 India", "B", "LIVE", "Fintech clearing provider handling instant retail capital inflows"),
    ("Yes Bank", "\U0001F1EE\U0001F1F3 India", "B", "LIVE", "Commercial institution conducting high-velocity payment remittance operations"),
    ("Federal Bank", "\U0001F1EE\U0001F1F3 India", "B", "LIVE", "Major localized retail bank utilizing automated routing systems"),
    ("Shinhan Bank", "\U0001F1F0\U0001F1F7 South Korea", "B", "LIVE", "Top South Korean network client maintaining active system access keys"),
    ("Woori Bank", "\U0001F1F0\U0001F1F7 South Korea", "B", "LIVE", "Multi-channel asset institution utilizing programmatic payment lines"),
    ("Krungsri (Bank of Ayudhya)", "\U0001F1F9\U0001F1ED Thailand", "B", "LIVE", "Streamlines real-time corporate pipelines between Thailand and Japan"),
    ("CIMB Bank", "\U0001F1F2\U0001F1FE Malaysia", "B", "LIVE", "Deep integration node managing corridors across ASEAN borders"),
    ("BDO Unibank", "\U0001F1F5\U0001F1ED Philippines", "B", "LIVE", "Major destination settlement point for international inbound money streams"),
    # Category C: Enterprise Tech, Custody & Infrastructure (25)
    ("Amazon Web Services (AWS)", "\U0001F310 Global", "C", "INFRASTRUCTURE", "Hosts architecture allowing global nodes to run XRPL validation configurations"),
    ("Finastra", "\U0001F1EC\U0001F1E7 UK", "C", "PRODUCTION", "Core banking software opening network access to 2,000+ regional banks"),
    ("Deloitte", "\U0001F310 Global", "C", "PRODUCTION", "Integrated distributed financial systems into client business models"),
    ("DZ Bank", "\U0001F1E9\U0001F1EA Germany", "C", "PRODUCTION", "Leverages digital custody solutions for tokenized asset issuance"),
    ("BNY Mellon", "\U0001F1FA\U0001F1F8 USA", "C", "PRODUCTION", "Primary tier-1 institutional reserve custodian for stablecoin offerings"),
    ("DBS Bank", "\U0001F1F8\U0001F1EC Singapore", "C", "LIVE", "Southeast Asian institution utilizing bank-grade digital asset vaults"),
    ("Kbank", "\U0001F1F0\U0001F1F7 South Korea", "C", "LIVE", "Digital platform implementing secure cryptographic wallet structures"),
    ("Kyobo Life Insurance", "\U0001F1F0\U0001F1F7 South Korea", "C", "LIVE", "Utilizing token ledger blueprint for corporate structural bond settlement"),
    ("BDACS", "\U0001F1F0\U0001F1F7 South Korea", "C", "LIVE", "Regulated secure vault platform for native ledger token storage"),
    ("Hidden Road", "\U0001F1FA\U0001F1F8 USA", "C", "EXPANDING", "Major institutional prime brokerage expanding liquidity paths for digital assets"),
    ("GTreasury", "\U0001F1FA\U0001F1F8 USA", "C", "LIVE", "Corporate liquidity software suite managing modern capital balance sheets"),
    ("Metaco", "\U0001F1E8\U0001F1ED Switzerland", "C", "ACQUIRED", "Institutional crypto custody firm acquired by Ripple to secure bank assets globally"),
    ("Temenos", "\U0001F1E8\U0001F1ED Switzerland", "C", "PRODUCTION", "Core banking software provider embedding automated accounting rails"),
    ("Accenture", "\U0001F310 Global", "C", "PRODUCTION", "Consulting giant managing global deployment strategies for payment architecture"),
    ("CGI Group", "\U0001F1E8\U0001F1E6 Canada", "C", "PRODUCTION", "IT consulting firm incorporating decentralized financial frameworks"),
    ("Modulr", "\U0001F1EC\U0001F1E7 UK/Europe", "C", "LIVE", "Payments provider optimizing massive local commercial transaction times"),
    ("Sentbe", "\U0001F1F0\U0001F1F7 South Korea", "C", "LIVE", "High-speed international remittance engine using the global banking network"),
    ("Currencycloud", "\U0001F1EC\U0001F1E7 UK", "C", "LIVE", "B2B multi-currency platform streamlining automated foreign exchange"),
    ("Nium", "\U0001F1F8\U0001F1EC Singapore", "C", "LIVE", "Fintech provider optimizing massive outbound payment paths across global corridors"),
    ("InstaReM", "\U0001F1F8\U0001F1EC Singapore", "C", "LIVE", "High-speed digital payment gateway connected via localized nodes"),
    ("BeeTech", "\U0001F1E7\U0001F1F7 Brazil", "C", "LIVE", "Digital financial operator executing automated Latin American clearings"),
    ("Fidor Bank", "\U0001F1E9\U0001F1EA Germany", "C", "PIONEER", "Digital banking pioneer integrating alternative clearing protocol tools"),
    ("Sabadell", "\U0001F1EA\U0001F1F8 Spain", "C", "LIVE", "Commercial infrastructure partner running real-time corporate data modules"),
    ("Cross River Bank", "\U0001F1FA\U0001F1F8 USA", "C", "LIVE", "Financial tech enabler providing direct underlying banking backbone"),
    ("Frankenmuth Credit Union", "\U0001F1FA\U0001F1F8 USA", "C", "LIVE", "Local cooperative providing digital asset services to local consumers"),
    # Category D: Regional / Middle East / LatAm (13)
    ("Al Ansari Exchange", "\U0001F1E6\U0001F1EA UAE", "D", "LIVE", "High-volume Middle Eastern exchange network routing institutional transfers"),
    ("National Bank of Fujairah", "\U0001F1E6\U0001F1EA UAE", "D", "LIVE", "Trade finance group optimizing real-time B2B payment workflows"),
    ("Saudi Central Bank (SAMA)", "\U0001F1F8\U0001F1E6 Saudi Arabia", "D", "PILOT", "Central entity piloting distributed frameworks for commercial branches"),
    ("National Bank of Kuwait (NBK)", "\U0001F1F0\U0001F1FC Kuwait", "D", "LIVE", "Runs international corporate transfer paths targeting the Gulf"),
    ("RAKBANK", "\U0001F1E6\U0001F1EA UAE", "D", "LIVE", "Integrates transaction routes to improve speed across enterprise pipelines"),
    ("Itau Unibanco", "\U0001F1E7\U0001F1F7 Brazil", "D", "LIVE", "Giant South American banking provider utilizing alternative communication networks"),
    ("Banco Rendimento", "\U0001F1E7\U0001F1F7 Brazil", "D", "LIVE", "Foreign currency commercial bank using optimized digital payment tunnels"),
    ("Intercorp", "\U0001F1F5\U0001F1EA Peru", "D", "LIVE", "Large conglomerate stabilizing localized payment legs for regional retail assets"),
    ("Faysal Bank", "\U0001F1F5\U0001F1F0 Pakistan", "D", "LIVE", "Specialized commercial banking provider processing inward retail cash flows"),
    ("Bank Alfalah", "\U0001F1F5\U0001F1F0 Pakistan", "D", "LIVE", "Manages automated digital channels targeting the UAE-to-Pakistan corridor"),
    ("bKash", "\U0001F1E7\U0001F1E9 Bangladesh", "D", "LIVE", "Mobile financial giant plugged in to capture worker remittances"),
    ("Vietcombank", "\U0001F1FB\U0001F1F3 Vietnam", "D", "PILOT", "Explores modern asset frameworks under regional digital banking pilots"),
    ("Interbank", "\U0001F1F5\U0001F1EA Peru", "D", "LIVE", "Traditional retail banking destination tied to alternative clearing systems"),
    # Category E: ETF Issuers & Corporate Treasury (7)
    ("Grayscale Investments", "\U0001F1FA\U0001F1F8 USA", "E", "LIVE ETF", "Asset manager operating the regulated Grayscale XRP Trust and spot fund"),
    ("Bitwise Asset Management", "\U0001F1FA\U0001F1F8 USA", "E", "LIVE ETF", "Regulated Wall Street provider offering institutional XRP exposure"),
    ("Franklin Templeton", "\U0001F1FA\U0001F1F8 USA", "E", "FILED", "Legacy asset firm filing for exchange-traded digital investment products"),
    ("Canary Capital Partners", "\U0001F1FA\U0001F1F8 USA", "E", "LIVE ETF", "Asset management firm deploying institutional-grade XRP capital avenues"),
    ("Hashdex Asset Management", "\U0001F310 Global", "E", "LIVE ETF", "Global investment manager offering systemic access to ledger tokens"),
    ("Worksport Ltd.", "\U0001F1FA\U0001F1F8 USA", "E", "TREASURY", "Clean automotive developer utilizing digital assets for inventory clearings"),
    ("Nature's Miracle Holding", "\U0001F1FA\U0001F1F8 USA", "E", "TREASURY", "Agriculture Tech firm implementing a $20M Corporate Treasury on the XRPL"),
]

COUNTRY_STATUS = [
    ("United States", "\U0001F1FA\U0001F1F8", "CONTESTED", "SEC lawsuit settled; XRP non-security ruling in programmatic sales. Evolving clarity."),
    ("European Union", "\U0001F1EA\U0001F1FA", "LEGAL", "MiCA regulation fully in force. XRP classified as crypto-asset, not security."),
    ("United Kingdom", "\U0001F1EC\U0001F1E7", "LEGAL", "FCA regulated. Crypto-asset promotion rules apply. No XRP-specific restrictions."),
    ("Japan", "\U0001F1EF\U0001F1F5", "LEGAL", "FSA regulated. XRP officially recognized as a crypto-asset. SBI Holdings major partner."),
    ("South Korea", "\U0001F1F0\U0001F1F7", "LEGAL", "FSC/FSS regulated. Major trading volume on Upbit and Bithumb."),
    ("Singapore", "\U0001F1F8\U0001F1EC", "LEGAL", "MAS regulated under PSA. Ripple holds a Major Payment Institution license."),
    ("UAE", "\U0001F1E6\U0001F1EA", "LEGAL", "VARA (Dubai) and ADGM (Abu Dhabi) regulated. Ripple has a regional HQ in Dubai."),
    ("Switzerland", "\U0001F1E8\U0001F1ED", "LEGAL", "FINMA regulated. Crypto Valley in Zug. Openly traded on licensed exchanges."),
    ("Australia", "\U0001F1E6\U0001F1FA", "LEGAL", "ASIC regulated. Crypto exchanges licensed. No XRP-specific restrictions."),
    ("Germany", "\U0001F1E9\U0001F1EA", "LEGAL", "BaFin regulated under MiCA. Deutsche B\u00F6rse-listed crypto products available."),
    ("Brazil", "\U0001F1E7\U0001F1F7", "LEGAL", "Banco Central do Brasil regulated. Bitso is a major corridor partner."),
    ("Canada", "\U0001F1E8\U0001F1E6", "LEGAL", "CSA regulated. Crypto ETPs listed on TSX. Active Canada-Mexico ODL corridor."),
    ("Mexico", "\U0001F1F2\U0001F1FD", "LEGAL", "CNBV regulated. Major Ripple ODL remittance corridor with the United States."),
    ("Philippines", "\U0001F1F5\U0001F1ED", "LEGAL", "BSP regulated. Major remittance corridor for OFW payments via Ripple partners."),
    ("India", "\U0001F1EE\U0001F1F3", "TAXED", "30% crypto tax + 1% TDS. Legal to hold and trade; framework still developing."),
    ("Thailand", "\U0001F1F9\U0001F1ED", "LEGAL", "SEC Thailand regulated. Listed on licensed exchanges with active Ripple partnerships."),
    ("Nigeria", "\U0001F1F3\U0001F1EC", "RESTRICTED", "CBN lifted crypto ban in 2023; regulated under SEC Nigeria, bank restrictions remain."),
    ("China", "\U0001F1E8\U0001F1F3", "BANNED", "All crypto trading banned since 2021. Citizens may not legally trade or hold XRP."),
    ("Russia", "\U0001F1F7\U0001F1FA", "RESTRICTED", "Limited legal use. Crypto as payment banned; trading tolerated but heavily restricted."),
    ("Saudi Arabia", "\U0001F1F8\U0001F1E6", "PENDING", "SAMA evaluating framework. Not officially prohibited but no clear legal status."),
]
COUNTRY_STATUS_COLORS = {
    "LEGAL": "var(--gr)", "CONTESTED": "var(--yl)", "TAXED": "var(--or)",
    "RESTRICTED": "var(--or)", "BANNED": "var(--rd)", "PENDING": "var(--bl)",
}

ETF_TRACKER = [
    {"applicant": "21Shares", "product": "XRP ETP", "market": "Europe", "status": "LIVE", "date": "2019",
     "note": "Actively trading on SIX Swiss Exchange. AUM growing."},
    {"applicant": "CoinShares", "product": "XRP ETP", "market": "Europe", "status": "LIVE", "date": "2020",
     "note": "Listed on multiple European exchanges. Institutional grade."},
    {"applicant": "WisdomTree", "product": "XRP ETP", "market": "Europe", "status": "LIVE", "date": "2021",
     "note": "FCA and EU regulated. Available in UK and Europe."},
    {"applicant": "VanEck", "product": "XRP ETP", "market": "Europe", "status": "LIVE", "date": "2021",
     "note": "Deutsche B\u00F6rse listed. Physically backed."},
    {"applicant": "Bitwise", "product": "XRP ETF", "market": "USA", "status": "FILED", "date": "2025",
     "note": "SEC review pending. Filed as a spot XRP ETF."},
    {"applicant": "WisdomTree", "product": "XRP ETF", "market": "USA", "status": "FILED", "date": "2025",
     "note": "US spot ETF filing submitted to the SEC."},
    {"applicant": "ProShares", "product": "XRP Futures ETF", "market": "USA", "status": "REVIEW", "date": "2025",
     "note": "Futures-based product under SEC consideration."},
    {"applicant": "Canary Capital", "product": "XRP ETF", "market": "USA", "status": "FILED", "date": "2024",
     "note": "First US spot XRP ETF filing. Pioneer application."},
]
ETF_STATUS_COLORS = {"LIVE": "var(--gr)", "FILED": "var(--yl)", "REVIEW": "var(--or)"}

SEC_TIMELINE = [
    ("Dec 2020", "SEC Files Lawsuit", "SEC sues Ripple Labs and its CEO for a $1.3B unregistered securities offering.", False),
    ("Nov 2022", "Judge Sides on Documents", "Court orders release of the Hinman speech documents.", False),
    ("Jul 2023", "Historic Partial Victory", "Judge Torres rules XRP is NOT a security in programmatic exchange sales.", True),
    ("Aug 2023", "SEC Appeals", "SEC files notice of appeal on the programmatic sales ruling.", False),
    ("Oct 2024", "SEC Drops Charges", "SEC drops charges against Ripple's leadership personally.", True),
    ("Mar 2025", "Settlement Reached", "Ripple and SEC settle. $50M fine paid vs. the original $2B demand.", True),
    ("2026", "Post-Settlement Era", "XRP operating in post-lawsuit clarity under a crypto-friendlier SEC.", True),
]

MICA_CALENDAR = [
    ("Jun 2023", "MiCA Published", "EU Markets in Crypto-Assets regulation officially published.", True),
    ("Dec 2024", "Stablecoin Rules Live", "Title III/IV provisions effective; RLUSD and issuers must comply.", True),
    ("Dec 2024", "Full MiCA in Force", "Complete framework operational across all 27 EU member states.", True),
    ("2025", "National Implementation", "Member states complete national regulatory adaptations.", False),
    ("2025-2026", "CASP Licensing Wave", "Crypto Asset Service Providers complete MiCA licensing.", False),
    ("2026+", "MiCA Review Clause", "European Commission reviews effectiveness and possible DeFi/NFT expansion.", False),
]

ODL_CORRIDORS = [
    {"from_c": "\U0001F1FA\U0001F1F8 USA", "to_c": "\U0001F1F2\U0001F1FD Mexico", "partner": "Bitso", "status": "ACTIVE",
     "note": "Largest ODL corridor globally \u2014 high daily volume via Bitso."},
    {"from_c": "\U0001F1FA\U0001F1F8 USA", "to_c": "\U0001F1F5\U0001F1ED Philippines", "partner": "Coins.ph", "status": "ACTIVE",
     "note": "Major OFW remittance route serving millions of Filipino workers."},
    {"from_c": "\U0001F1EA\U0001F1FA Europe", "to_c": "\U0001F1F2\U0001F1FD Mexico", "partner": "Bitso", "status": "ACTIVE",
     "note": "Cross-Atlantic corridor expanding with MiCA regulatory clarity."},
    {"from_c": "\U0001F1EF\U0001F1F5 Japan", "to_c": "\U0001F1F5\U0001F1ED Philippines", "partner": "SBI Remit", "status": "ACTIVE",
     "note": "SBI Holdings' flagship ODL corridor \u2014 high volume."},
    {"from_c": "\U0001F1E6\U0001F1FA Australia", "to_c": "\U0001F1F5\U0001F1ED Philippines", "partner": "FlashFX", "status": "ACTIVE",
     "note": "AUD to PHP remittance \u2014 major OFW corridor."},
    {"from_c": "\U0001F1EC\U0001F1E7 UK", "to_c": "\U0001F1F3\U0001F1EC Nigeria", "partner": "Ripple Partner", "status": "GROWING",
     "note": "Africa expansion focus with Flutterwave integration."},
    {"from_c": "\U0001F1FA\U0001F1F8 USA", "to_c": "\U0001F1EE\U0001F1F3 India", "partner": "Various", "status": "GROWING",
     "note": "Largest remittance market globally \u2014 $100B+ annual flows."},
    {"from_c": "\U0001F1F8\U0001F1EC Singapore", "to_c": "\U0001F30F SE Asia", "partner": "Various", "status": "GROWING",
     "note": "Regional hub \u2014 Ripple's Singapore MPI license is active."},
]

ISO20022_ADOPTERS = [
    {"name": "SWIFT gpi", "region": "Global", "note": "Fully ISO 20022 compliant since 2023."},
    {"name": "TARGET2", "region": "EU", "note": "ECB's large-value payment system, migrated Nov 2022."},
    {"name": "CHAPS", "region": "UK", "note": "Bank of England high-value payment system, migrated 2023."},
    {"name": "Fedwire", "region": "USA", "note": "US Federal Reserve system, migration completed 2024."},
    {"name": "CHIPS", "region": "USA", "note": "Clearing House Interbank Payments System, ISO 20022 compliant."},
    {"name": "SIC", "region": "Switzerland", "note": "Swiss Interbank Clearing system, migrated 2023."},
    {"name": "HVPS+", "region": "Canada", "note": "High Value Payment System Canada, completed 2023."},
    {"name": "RITS", "region": "Australia", "note": "Reserve Bank Information Transfer System, migrated."},
]


def country_grid_html():
    out = ""
    for name, flag, status, note in COUNTRY_STATUS:
        col = COUNTRY_STATUS_COLORS.get(status, "var(--tx)")
        out += (
            f'<div class="cg-card" style="border-color:{col}55">'
            f'<div class="cg-top"><span class="cg-flag">{flag}</span>'
            f'<span class="cg-name">{html.escape(name)}</span></div>'
            f'<span class="odl-status" style="background:{col}26;color:{col}">{status}</span>'
            f'<div class="cg-note">{html.escape(note)}</div>'
            f'</div>'
        )
    return out

def etf_tracker_html():
    out = ""
    for e in ETF_TRACKER:
        col = ETF_STATUS_COLORS.get(e["status"], "var(--tx)")
        out += (
            f'<tr><td style="font-weight:700;color:var(--br)">{html.escape(e["applicant"])}</td>'
            f'<td>{html.escape(e["product"])}</td><td style="color:var(--tx)">{html.escape(e["market"])}</td>'
            f'<td><span class="odl-status" style="background:{col}26;color:{col}">{e["status"]}</span></td>'
            f'<td style="color:var(--tx)">{html.escape(e["date"])}</td>'
            f'<td style="color:var(--tx);max-width:220px">{html.escape(e["note"])}</td></tr>'
        )
    return out

def sec_timeline_html():
    out = ""
    for date, event, detail, major in SEC_TIMELINE:
        dot_col = "var(--gr)" if major else "var(--yl)"
        dot_sz = "16px" if major else "11px"
        out += (
            f'<div class="tl-node" style="flex-basis:170px;min-width:170px">'
            f'<div class="tl-top">'
            f'<div class="tl-year" style="color:{dot_col};font-size:15px">{date}</div>'
            f'<div class="tl-dot" style="width:{dot_sz};height:{dot_sz};background:{dot_col}"></div>'
            f'</div>'
            f'<div class="tl-event" style="font-size:15px">{html.escape(event)}</div>'
            f'<div class="tl-detail" style="font-size:12px">{html.escape(detail)}</div>'
            f'</div>'
        )
    return out

def mica_calendar_html():
    out = ""
    for date, event, detail, done in MICA_CALENDAR:
        icon = "\u2705" if done else "\u25CB"
        col = "var(--gr)" if done else "var(--tx)"
        out += (
            f'<div class="mica-row">'
            f'<span class="mica-icon" style="color:{col}">{icon}</span>'
            f'<span class="mica-date">{html.escape(date)}</span>'
            f'<span class="mica-event" style="color:{col}">{html.escape(event)}</span>'
            f'<span class="mica-detail">{html.escape(detail)}</span>'
            f'</div>'
        )
    return out

def cbdc_grid_html():
    out = ""
    for name, flag, project, status, detail in PARTNERSHIPS:
        col = STATUS_COLORS.get(status, "var(--tx)")
        out += (
            f'<div class="cg-card" style="border-color:{col}55">'
            f'<div class="cg-top"><span class="cg-flag">{flag}</span>'
            f'<span class="cg-name">{html.escape(name)}</span></div>'
            f'<span class="odl-status" style="background:{col}26;color:{col}">{status}</span>'
            f'<div class="cg-note"><b style="color:var(--br)">{html.escape(project)}</b><br>{html.escape(detail)}</div>'
            f'</div>'
        )
    return out


def odl_corridors_html():
    out = ""
    for c in ODL_CORRIDORS:
        cls = c["status"].lower()
        out += (
            f'<div class="odl-item"><span class="odl-route">{c["from_c"]} \u2192 {c["to_c"]}</span>'
            f'<span class="odl-status {cls}">{c["status"]}</span>'
            f'<span style="color:var(--tx)">via {html.escape(c["partner"])}</span>'
            f'<span class="odl-note">{html.escape(c["note"])}</span></div>'
        )
    return out

def iso20022_html():
    out = ""
    for a in ISO20022_ADOPTERS:
        out += (
            f'<div class="iso-item"><span class="odl-status live">LIVE</span>'
            f'<span style="font-weight:700;color:var(--br)">{html.escape(a["name"])}</span>'
            f'<span style="color:var(--tx)">{html.escape(a["region"])}</span>'
            f'<span class="odl-note">{html.escape(a["note"])}</span></div>'
        )
    return out


# ----------------------------------------------------------------------
# FLAG_SVG (V107) \u2014 permanent replacement for Unicode flag emoji.
# Windows has never shipped flag glyphs in its system emoji font, so flag
# emoji fall back to showing the raw two-letter country code as text on
# every browser on Windows. These small inline SVGs render identically on
# every OS, browser, and version \u2014 no font dependency at all.
# Simplified but accurate to each flag's real colors and stripe/layout.
# ----------------------------------------------------------------------
FLAG_SVG = {
"US": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#B22234"/><rect y="1.08" width="20" height="1.08" fill="#fff"/><rect y="3.23" width="20" height="1.08" fill="#fff"/><rect y="5.38" width="20" height="1.08" fill="#fff"/><rect y="7.54" width="20" height="1.08" fill="#fff"/><rect y="9.69" width="20" height="1.08" fill="#fff"/><rect y="11.85" width="20" height="1.08" fill="#fff"/><rect width="8" height="7.54" fill="#3C3B6E"/></svg>',
"GB": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#00247d"/><path d="M0 0L20 14M20 0L0 14" stroke="#fff" stroke-width="2.2"/><path d="M0 0L20 14M20 0L0 14" stroke="#cf142b" stroke-width="0.9"/><path d="M10 0V14M0 7H20" stroke="#fff" stroke-width="3.6"/><path d="M10 0V14M0 7H20" stroke="#cf142b" stroke-width="2"/></svg>',
"AU": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#00247d"/><path d="M0 0L6 4.5M6 0L0 4.5" stroke="#fff" stroke-width="0.9"/><path d="M0 0V7H10V0Z" fill="#00247d" stroke="#fff" stroke-width="0.4"/><g fill="#fff"><circle cx="15" cy="4" r="0.8"/><circle cx="17" cy="7" r="0.8"/><circle cx="15" cy="10" r="0.8"/><circle cx="12" cy="8" r="0.6"/><circle cx="12" cy="4" r="0.6"/></g></svg>',
"CH": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#d52b1e"/><rect x="8.5" y="4" width="3" height="6" fill="#fff"/><rect x="6.5" y="6" width="7" height="2" fill="#fff"/></svg>',
"SG": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="7" fill="#ed2939"/><rect y="7" width="20" height="7" fill="#fff"/><circle cx="5" cy="3.5" r="2" fill="#fff"/><circle cx="6" cy="3.5" r="1.7" fill="#ed2939"/></svg>',
"BR": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#009c3b"/><polygon points="10,2 18,7 10,12 2,7" fill="#ffdf00"/><circle cx="10" cy="7" r="2.6" fill="#002776"/></svg>',
"AE": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="4.67" y="0" fill="#00732f"/><rect width="20" height="4.67" y="4.67" fill="#fff"/><rect width="20" height="4.67" y="9.33" fill="#000"/><rect width="5" height="14" fill="#ff0000"/></svg>',
"KR": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><circle cx="10" cy="7" r="3" fill="#c60c30"/><path d="M10 4A1.5 1.5 0 0 1 10 7A1.5 1.5 0 0 0 10 10A3 3 0 0 0 10 4" fill="#003478"/></svg>',
"PH": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="7" fill="#0038a8"/><rect y="7" width="20" height="7" fill="#ce1126"/><polygon points="0,0 7,7 0,14" fill="#fff"/><circle cx="2.3" cy="7" r="1" fill="#fcd116"/></svg>',
"IN": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="4.67" fill="#ff9933"/><rect width="20" height="4.67" y="4.67" fill="#fff"/><rect width="20" height="4.67" y="9.33" fill="#138808"/><circle cx="10" cy="7" r="1.3" fill="none" stroke="#000080" stroke-width="0.25"/></svg>',
"CA": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><rect width="5" height="14" fill="#ff0000"/><rect x="15" width="5" height="14" fill="#ff0000"/><path d="M10 3l1 2.2 2-1-0.6 2.3 2.1-0.2-1.6 1.7 1.6 1.7-2.1-0.2 0.6 2.3-2-1-1 2.2-1-2.2-2 1 0.6-2.3-2.1 0.2 1.6-1.7-1.6-1.7 2.1 0.2-0.6-2.3 2 1z" fill="#ff0000"/></svg>',
"DE": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="4.67" fill="#000"/><rect width="20" height="4.67" y="4.67" fill="#dd0000"/><rect width="20" height="4.67" y="9.33" fill="#ffce00"/></svg>',
"MY": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><g fill="#cc0001"><rect y="0" width="20" height="1"/><rect y="2" width="20" height="1"/><rect y="4" width="20" height="1"/><rect y="6" width="20" height="1"/><rect y="8" width="20" height="1"/><rect y="10" width="20" height="1"/><rect y="12" width="20" height="1"/></g><rect width="10" height="7.5" fill="#010066"/><circle cx="4" cy="3.5" r="2" fill="#ffcc00"/><circle cx="4.9" cy="3.5" r="1.7" fill="#010066"/></svg>',
"ES": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#aa151b"/><rect y="3.5" width="20" height="7" fill="#f1bf00"/></svg>',
"EU": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#003399"/><g fill="#ffcc00"><circle cx="10" cy="2.6" r="0.5"/><circle cx="10" cy="11.4" r="0.5"/><circle cx="5.6" cy="7" r="0.5"/><circle cx="14.4" cy="7" r="0.5"/><circle cx="6.9" cy="3.9" r="0.5"/><circle cx="13.1" cy="3.9" r="0.5"/><circle cx="6.9" cy="10.1" r="0.5"/><circle cx="13.1" cy="10.1" r="0.5"/></g></svg>',
"JP": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><circle cx="10" cy="7" r="3.4" fill="#bc002d"/></svg>',
"TH": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#f4f5f8"/><rect width="20" height="2.8" fill="#a51931"/><rect y="11.2" width="20" height="2.8" fill="#a51931"/><rect y="4.67" width="20" height="4.67" fill="#2d2a4a"/></svg>',
"PK": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#01411c"/><rect width="5" height="14" fill="#fff"/><circle cx="13" cy="7" r="2.6" fill="#fff"/><circle cx="14" cy="7" r="2.2" fill="#01411c"/></svg>',
"PE": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="6.67" height="14" fill="#d91023"/><rect x="6.67" width="6.67" height="14" fill="#fff"/><rect x="13.33" width="6.67" height="14" fill="#d91023"/></svg>',
"MX": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="6.67" height="14" fill="#006847"/><rect x="6.67" width="6.67" height="14" fill="#fff"/><rect x="13.33" width="6.67" height="14" fill="#ce1126"/><circle cx="10" cy="7" r="1.3" fill="#8b5a2b"/></svg>',
"QA": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#8d1b3d"/><rect width="6" height="14" fill="#fff"/><polygon points="6,0 8,1.75 6,3.5" fill="#fff"/><polygon points="6,3.5 8,5.25 6,7" fill="#fff"/><polygon points="6,7 8,8.75 6,10.5" fill="#fff"/><polygon points="6,10.5 8,12.25 6,14" fill="#fff"/></svg>',
"TR": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#e30a17"/><circle cx="8.5" cy="7" r="3" fill="#fff"/><circle cx="9.3" cy="7" r="2.5" fill="#e30a17"/></svg>',
"NL": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="4.67" fill="#ae1c28"/><rect width="20" height="4.67" y="4.67" fill="#fff"/><rect width="20" height="4.67" y="9.33" fill="#21468b"/></svg>',
"IT": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="6.67" height="14" fill="#009246"/><rect x="6.67" width="6.67" height="14" fill="#fff"/><rect x="13.33" width="6.67" height="14" fill="#ce2b37"/></svg>',
"SE": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#006aa7"/><rect x="6" width="2.2" height="14" fill="#fecc00"/><rect y="5.9" width="20" height="2.2" fill="#fecc00"/></svg>',
"BD": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#006a4e"/><circle cx="9" cy="7" r="3.2" fill="#f42a41"/></svg>',
"KW": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="4.67" fill="#007a3d"/><rect width="20" height="4.67" y="4.67" fill="#fff"/><rect width="20" height="4.67" y="9.33" fill="#000"/><polygon points="0,0 5,7 0,14" fill="#ce1126"/></svg>',
"SA": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#006c35"/><rect x="3" y="6.3" width="14" height="1.4" fill="#fff"/></svg>',
"VN": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#da251d"/><polygon points="10,3.5 11.2,6.7 14.5,6.7 11.8,8.7 12.8,12 10,10 7.2,12 8.2,8.7 5.5,6.7 8.8,6.7" fill="#ffff00"/></svg>',
"BT": '<svg viewBox="0 0 20 14" width="18" height="13"><polygon points="0,0 20,0 0,14" fill="#ffcc00"/><polygon points="20,0 20,14 0,14" fill="#ff4e12"/></svg>',
"ME": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#c40308"/><rect x="1" y="1" width="18" height="12" fill="none" stroke="#d4af37" stroke-width="1"/><circle cx="10" cy="7" r="2.6" fill="#d4af37"/></svg>',
"PW": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#4aadd6"/><circle cx="8.5" cy="7" r="3.4" fill="#ffde00"/></svg>',
"CO": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="7" fill="#fcd116"/><rect width="20" height="3.5" y="7" fill="#003893"/><rect width="20" height="3.5" y="10.5" fill="#ce1126"/></svg>',
"HK": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#de2910"/><circle cx="10" cy="7" r="3.6" fill="#fff"/></svg>',
"FR": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="6.67" height="14" fill="#0055A4"/><rect x="6.67" width="6.67" height="14" fill="#fff"/><rect x="13.33" width="6.67" height="14" fill="#EF4135"/></svg>',
"ZA": '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" fill="#fff"/><rect width="20" height="4.67" fill="#000c8a"/><rect width="20" height="4.67" y="9.33" fill="#de3831"/><polygon points="0,4.67 8,7 0,9.33" fill="#007847"/><polygon points="0,5.4 6,7 0,8.6" fill="#ffb612"/></svg>',
}
_FLAG_FALLBACK = '<svg viewBox="0 0 20 14" width="18" height="13"><rect width="20" height="14" rx="1.5" fill="#3a4a63"/><circle cx="10" cy="7" r="4" fill="none" stroke="#a8bdd0" stroke-width="0.8"/></svg>'


def _region_indicator_to_code(pair):
    """Decode a 2-char regional-indicator flag emoji (e.g. US flag) to its ISO code."""
    try:
        return ''.join(chr(ord(ch) - 0x1F1E6 + ord('A')) for ch in pair)
    except Exception:
        return None


_FLAG_EMOJI_RE = re.compile(
    '[' + '\U0001F1E6-\U0001F1FF' + ']{2}'
)


def replace_flags_with_svg(html_text):
    """Post-process any fully-rendered HTML page and replace every flag emoji
    (wherever it came from \u2014 partner directory, region lookups, FX table,
    anywhere) with an inline SVG that renders identically on every OS and
    browser. This is applied once, centrally, to the final page output, so
    every flag on the site is covered regardless of which code path produced
    it."""
    def repl(m):
        code = _region_indicator_to_code(m.group(0))
        svg = FLAG_SVG.get(code, _FLAG_FALLBACK)
        return f'<span class="flag-ic" style="display:inline-flex;vertical-align:-2px">{svg}</span>'
    return _FLAG_EMOJI_RE.sub(repl, html_text)



# ═════════════════════════════════════════════════════════════════════
# V116 — REGULATORY PAGE SECTIONS (six, new this version)
#
# Five of the six run on curated data maintained by hand. That data lives
# in the plainly labelled tuples directly below each section's function so
# it can be found and edited without reading any surrounding logic.
#
# REG_LAST_REVIEWED is displayed on every one of the six sections. Change
# it whenever the curated data below is updated.
#
# The sixth, the Regulator Voice Tracker, is computed. It reads the news
# pool the existing feed cycle already fetches (NEWS["pool"]). It adds no
# feeds and makes no network calls of its own, so it cannot slow or break
# the existing fetch path.
#
# Palette for this page: blue (--hdr), turquoise (--tq), orange (--or),
# white and the neutral text vars. No red, no pink.
# ═════════════════════════════════════════════════════════════════════

REG_LAST_REVIEWED = "July 24, 2026"

_RG_BLUE = "var(--hdr)"
_RG_TURQ = "var(--tq)"
_RG_ORNG = "var(--or)"
_RG_ROTATION = (_RG_BLUE, _RG_TURQ, _RG_ORNG)


def _rg_reviewed():
    return ('<div class="rg-note">Curated data \u00b7 last reviewed '
            + REG_LAST_REVIEWED + '</div>')


def _rg_head(icon, title, colour, sub):
    return ('<div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">'
            '<div class="sec-title" style="color:' + colour + '">'
            '<span class="sic">' + icon + '</span> ' + title + '</div>'
            '<div class="rg-sub">' + sub + '</div>')


# ─────────────────────────────────────────────────────────────────────
# 1. GLOBAL REGULATORY STATUS MAP
#    (jurisdiction, posture, accent, one-line status)
#    Posture vocabulary: COMPREHENSIVE / DEVELOPING / RESTRICTIVE
# ─────────────────────────────────────────────────────────────────────
RG_JURISDICTIONS = (
    ("United States",  "DEVELOPING",    _RG_ORNG,
     "Spot XRP exchange-traded products trade on US venues. Comprehensive market-structure "
     "legislation remains before the Senate."),
    ("European Union", "COMPREHENSIVE", _RG_BLUE,
     "MiCA applies in full across member states. XRP is treated as a crypto-asset that is "
     "neither an e-money token nor an asset-referenced token."),
    ("United Kingdom", "DEVELOPING",    _RG_ORNG,
     "FCA cryptoasset regime phasing in, with authorisation and a financial-promotions "
     "regime already live."),
    ("Japan",          "COMPREHENSIVE", _RG_BLUE,
     "FSA registration regime long established. XRP has been listed on registered domestic "
     "exchanges for years."),
    ("Singapore",      "COMPREHENSIVE", _RG_BLUE,
     "MAS licenses digital payment token services under the Payment Services Act."),
    ("UAE \u2014 Dubai",    "COMPREHENSIVE", _RG_BLUE,
     "VARA operates a dedicated virtual-asset regime; Ripple holds a DFSA licence in the DIFC."),
    ("Switzerland",    "COMPREHENSIVE", _RG_BLUE,
     "FINMA supervises under the DLT Act, one of the earliest complete frameworks."),
    ("Hong Kong",      "COMPREHENSIVE", _RG_BLUE,
     "SFC licenses trading platforms; a separate stablecoin regime sits alongside it."),
    ("Canada",         "COMPREHENSIVE", _RG_BLUE,
     "CSA requires platform registration and pre-registration undertakings."),
    ("Brazil",         "DEVELOPING",    _RG_ORNG,
     "Central Bank has been building out the VASP authorisation framework."),
    ("South Korea",    "COMPREHENSIVE", _RG_BLUE,
     "Virtual Asset User Protection Act in force, with strict exchange and custody duties."),
    ("Australia",      "DEVELOPING",    _RG_ORNG,
     "Treasury's digital-asset platform licensing reform still working through Parliament."),
    ("India",          "RESTRICTIVE",   _RG_TURQ,
     "Heavy transaction tax and no comprehensive framework, though trading is not banned."),
    ("China",          "RESTRICTIVE",   _RG_TURQ,
     "Trading and related services prohibited on the mainland. Hong Kong is separate."),
)


def rg_status_map_html():
    cards = []
    for name, posture, colour, note in RG_JURISDICTIONS:
        cards.append(
            '<div class="rg-j" style="border-left-color:' + colour + '">'
            '<div class="rg-j-n">' + name + '</div>'
            '<div class="rg-j-s" style="color:' + colour + '">' + posture + '</div>'
            '<div class="rg-j-d">' + note + '</div>'
            '</div>')
    return (_rg_head("\U0001F30D", "Global Regulatory Status Map", _RG_BLUE,
                     "Where XRP and the wider digital-asset market stand jurisdiction by "
                     "jurisdiction. Posture describes the framework in place, not a view on "
                     "any asset.")
            + '<div class="rg-map">' + "".join(cards) + '</div>'
            + _rg_reviewed() + '</div>')


# ─────────────────────────────────────────────────────────────────────
# 2. ETF & PRODUCT APPROVAL BOARD
#    (product, issuer, venue/market, status, accent)
# ─────────────────────────────────────────────────────────────────────
RG_PRODUCTS = (
    ("Spot XRP ETF",            "Multiple US issuers", "US exchanges",  "TRADING",  _RG_BLUE),
    ("XRP futures ETF",         "Multiple US issuers", "US exchanges",  "TRADING",  _RG_BLUE),
    ("XRP ETP",                 "European issuers",    "SIX / Xetra",   "TRADING",  _RG_BLUE),
    ("XRP ETP",                 "Canadian issuers",    "TSX",           "TRADING",  _RG_BLUE),
    ("Further US spot filings", "Additional issuers",  "US exchanges",  "PENDING",  _RG_ORNG),
    ("Staking / yield wrappers","Various",             "Various",       "PENDING",  _RG_ORNG),
)


def rg_product_board_html():
    rows = []
    for prod, issuer, venue, status, colour in RG_PRODUCTS:
        rows.append(
            '<tr><td><b>' + prod + '</b></td><td>' + issuer + '</td><td>' + venue + '</td>'
            '<td><span class="rg-pill" style="color:' + colour + '">' + status + '</span></td></tr>')
    return (_rg_head("\U0001F4CB", "ETF &amp; Product Approval Board", _RG_TURQ,
                     "Regulated XRP investment products by category and status. Issuer-level "
                     "detail is deliberately generalised here so this board stays accurate "
                     "between reviews.")
            + '<table class="rg-tbl"><thead><tr><th>Product</th><th>Issuer</th>'
              '<th>Market</th><th>Status</th></tr></thead><tbody>'
            + "".join(rows) + '</tbody></table>'
            + '<div class="rg-flag">Listing status is not an endorsement and says nothing '
              'about whether any product is suitable for you. Not financial advice.</div>'
            + _rg_reviewed() + '</div>')


# ─────────────────────────────────────────────────────────────────────
# 3. ENFORCEMENT & LITIGATION DOCKET
#    (matter, forum, posture, accent, note)
# ─────────────────────────────────────────────────────────────────────
RG_DOCKET = (
    ("SEC v. Ripple Labs", "S.D.N.Y. / 2d Cir.", "CLOSED", _RG_BLUE,
     "The long-running action ended in 2025. The 2023 summary-judgment holding \u2014 that "
     "programmatic exchange sales did not meet the Howey test while institutional sales did "
     "\u2014 stands as the operative outcome, together with a civil penalty."),
    ("Ripple \u2014 OCC charter", "Office of the Comptroller", "PENDING", _RG_ORNG,
     "Ripple's national trust bank application remains a live regulatory question rather "
     "than a litigation matter, but it sits on the same critical path for institutional "
     "access."),
    ("Private class actions", "US federal and state", "LARGELY RESOLVED", _RG_BLUE,
     "The principal investor class litigation against Ripple has been resolved. Residual "
     "filings appear periodically and are tracked here as they arise."),
    ("Exchange-side matters", "Various", "ONGOING", _RG_ORNG,
     "Enforcement aimed at trading venues rather than at XRP itself can still affect XRP "
     "market access, so it is monitored on this page."),
)


def rg_docket_html():
    rows = []
    for matter, forum, posture, colour, note in RG_DOCKET:
        rows.append(
            '<tr><td><b>' + matter + '</b><div style="font-size:12px;color:var(--tx);'
            'margin-top:4px;line-height:1.5">' + note + '</div></td>'
            '<td>' + forum + '</td>'
            '<td><span class="rg-pill" style="color:' + colour + '">' + posture + '</span></td></tr>')
    return (_rg_head("\u2696\uFE0F", "Enforcement &amp; Litigation Docket", _RG_ORNG,
                     "Matters that shape how XRP may be sold, held and listed. Summaries are "
                     "plain-language and are not legal advice.")
            + '<table class="rg-tbl"><thead><tr><th>Matter</th><th>Forum</th>'
              '<th>Posture</th></tr></thead><tbody>'
            + "".join(rows) + '</tbody></table>'
            + _rg_reviewed() + '</div>')


# ─────────────────────────────────────────────────────────────────────
# 4. RULEMAKING & LEGISLATIVE CALENDAR
#    (when, what, detail)
# ─────────────────────────────────────────────────────────────────────
RG_CALENDAR = (
    ("Live now", "CLARITY Act \u2014 Senate",
     "Market-structure legislation passed the House and remains before the Senate. The "
     "spot-market jurisdictional split between the SEC and the CFTC is the provision that "
     "matters most for XRP."),
    ("Live now", "GENIUS Act implementation",
     "Payment-stablecoin rulemaking by the federal banking agencies and Treasury. Relevant "
     "to RLUSD. XRP is not a stablecoin and is not covered by this framework."),
    ("Live now", "SEC rulemaking agenda",
     "Custody, exchange definitions and disclosure items that would apply across "
     "digital-asset markets."),
    ("Live now", "OCC charter decisions",
     "National trust bank applications from digital-asset firms, Ripple's among them."),
    ("Rolling",  "Federal Register comment windows",
     "Comment deadlines open and close continuously. The Regulatory &amp; Ledger Watch "
     "section on this page reads the Federal Register directly and will show live items."),
    ("Rolling",  "EU \u2014 MiCA supervisory guidance",
     "ESMA and EBA continue issuing technical standards and guidance under the framework "
     "already in force."),
)


def rg_calendar_html():
    rows = []
    for when, what, detail in RG_CALENDAR:
        rows.append(
            '<div class="rg-c"><div class="rg-c-d">' + when + '</div>'
            '<div><div class="rg-c-t">' + what + '</div>'
            '<div class="rg-c-b">' + detail + '</div></div></div>')
    return (_rg_head("\U0001F5D3\uFE0F", "Rulemaking &amp; Legislative Calendar", _RG_BLUE,
                     "What is actually moving, and where. Dated deadlines are deliberately "
                     "avoided here because they slip; live dated items surface in Regulatory "
                     "&amp; Ledger Watch below.")
            + '<div class="rg-cal">' + "".join(rows) + '</div>'
            + _rg_reviewed() + '</div>')


# ─────────────────────────────────────────────────────────────────────
# 5. REGULATOR VOICE TRACKER  (computed — no new feeds, no new calls)
#    (display name, matching keywords)
# ─────────────────────────────────────────────────────────────────────
RG_VOICES = (
    ("SEC",           ("sec ", " sec", "securities and exchange")),
    ("CFTC",          ("cftc", "commodity futures")),
    ("US Treasury",   ("treasury",)),
    ("Federal Reserve", ("federal reserve", "the fed ", "fomc")),
    ("OCC",           ("occ ", "comptroller of the currency")),
    ("FDIC",          ("fdic",)),
    ("US Congress",   ("congress", "senate", "house committee", "lawmaker")),
    ("ESMA / EU",     ("esma", "european commission", "mica", "european union")),
    ("FCA / UK",      ("fca", "bank of england", "united kingdom", " uk ")),
    ("MAS Singapore", ("mas ", "monetary authority of singapore")),
    ("FSA Japan",     ("fsa", "japan financial services")),
    ("VARA / UAE",    ("vara", "dubai", "uae")),
    ("BIS / FSB",     ("bis ", "bank for international settlements", "financial stability board")),
    ("IMF",           ("imf", "international monetary fund")),
)


def rg_voice_tracker_html():
    """Reads the pool the existing news cycle already fetched. Never raises."""
    try:
        pool = NEWS.get("pool", []) or []
    except Exception:
        pool = []

    cards = []
    idx = 0
    for name, keys in RG_VOICES:
        hits = []
        for s in pool:
            try:
                blob = ((s.get("title") or "") + " " + (s.get("source") or "")).lower()
            except Exception:
                continue
            if any(k in blob for k in keys):
                hits.append(s)
        colour = _RG_ROTATION[idx % len(_RG_ROTATION)]
        idx += 1

        if hits:
            try:
                hits.sort(key=lambda s: s.get("dt"), reverse=True)
            except Exception:
                pass
            top = hits[0]
            title = (top.get("title") or "").strip()
            if len(title) > 150:
                title = title[:147] + "\u2026"
            link = top.get("link") or ""
            src = top.get("source") or ""
            body = ('<a href="' + link + '" target="_blank" rel="noopener">' + title + '</a>'
                    ) if link else title
            sub = '<div class="rg-v-s">' + src + '</div>' if src else ""
            count = str(len(hits)) + (" mention" if len(hits) == 1 else " mentions")
        else:
            body = ('<span style="color:var(--tx)">No mention in the current news cycle.</span>')
            sub = ""
            count = "0 mentions"

        cards.append(
            '<div class="rg-v" style="border-left:3px solid ' + colour + '">'
            '<div class="rg-v-h">'
            '<span class="rg-v-n" style="color:' + colour + '">' + name + '</span>'
            '<span class="rg-v-c">' + count + '</span></div>'
            '<div class="rg-v-q">' + body + '</div>' + sub + '</div>')

    return (_rg_head("\U0001F5E3\uFE0F", "Regulator Voice Tracker", _RG_TURQ,
                     "Which regulators and legislatures are actually being heard from right "
                     "now, measured against the same news pool this site already collects. "
                     "Counts cover the current cycle only, so a zero means quiet today, not "
                     "absent from the debate.")
            + '<div class="rg-vt">' + "".join(cards) + '</div>'
            + '<div class="rg-note">Computed live from the existing feed cycle \u00b7 '
              'no additional sources</div></div>')


# ─────────────────────────────────────────────────────────────────────
# 6. STABLECOIN REGULATORY OVERLAY
#    (instrument, issuer, regime, note)
# ─────────────────────────────────────────────────────────────────────
RG_STABLES = (
    ("RLUSD", "Ripple",
     "US payment-stablecoin framework; NYDFS-supervised issuance",
     "Ripple's own dollar stablecoin. Reserve-backed and redeemable at par by design. This "
     "is the Ripple-issued instrument that stablecoin rules actually apply to."),
    ("USDC", "Circle",
     "US payment-stablecoin framework; EU e-money token under MiCA",
     "Widely used in XRPL and cross-chain liquidity routing."),
    ("USDT", "Tether",
     "Varies by jurisdiction; constrained in the EU under MiCA",
     "The largest stablecoin by supply, with a different compliance posture region to region."),
    ("EURC and other euro tokens", "Various",
     "EU e-money tokens under MiCA",
     "Euro-denominated tokens sit squarely inside the MiCA e-money category."),
)


def rg_stablecoin_overlay_html():
    cards = []
    for name, issuer, regime, note in RG_STABLES:
        cards.append(
            '<div class="rg-s"><div class="rg-s-n">' + name + '</div>'
            '<div class="rg-s-i">' + issuer + '</div>'
            '<div class="rg-s-d"><b style="color:var(--br)">Regime:</b> ' + regime + '<br>' + note
            + '</div></div>')
    return (_rg_head("\U0001F517", "Stablecoin Regulatory Overlay", _RG_ORNG,
                     "Stablecoin rules move separately from the rest of digital-asset "
                     "regulation, and they increasingly govern the settlement instruments "
                     "that ride on the XRP Ledger. This is where those two tracks meet.")
            + '<div class="rg-sc">' + "".join(cards) + '</div>'
            + '<div class="rg-flag"><b style="color:var(--or)">XRP is not a stablecoin.</b> '
              'XRP is a floating-price digital asset with no peg, no issuer redemption promise '
              'and no reserve backing. RLUSD is Ripple\'s stablecoin. Payment-stablecoin '
              'legislation such as the GENIUS Act governs instruments like RLUSD \u2014 it does '
              'not govern XRP. Conflating the two is the single most common error in coverage '
              'of this topic.</div>'
            + _rg_reviewed() + '</div>')


def regulatory_sections():
    """All six new Regulatory sections, in the order Rich approved them.
    Any single failure degrades to a visible notice rather than a broken page."""
    out = []
    for fn in (rg_status_map_html, rg_product_board_html, rg_docket_html,
               rg_calendar_html, rg_voice_tracker_html, rg_stablecoin_overlay_html):
        try:
            out.append(fn())
        except Exception:
            out.append('<div class="acct" style="border-color:rgba(204,95,0,.35);margin:10px 0">'
                       '<div class="rg-sub">This section is temporarily unavailable.</div></div>')
    return "".join(out)


def render_page(page="main"):
    checks, passed, total, overall = run_preflight()
    overall_color = "#48ff82" if overall == "PASS" else "#ff4060"
    boot_str = BOOT_TIME.strftime("%Y-%m-%d %H:%M:%S UTC")
    hdr_feeds_active = NEWS["feeds_active"]
    hdr_feeds_total = NEWS["feeds_total"]

    # Breaking News bar — real breaking stories when present, home-base message otherwise
    _pool = NEWS.get("pool", [])
    _breaking_stories = sorted((s for s in _pool if s.get("breaking")), key=lambda s: s["dt"], reverse=True)
    if _breaking_stories:
        _top_break = _breaking_stories[0]
        bktext = f'{html.escape(_top_break["source"])}: {html.escape(_top_break["title"])}'
    elif _pool:
        bktext = "\U0001F6F0\uFE0F Monitoring live feeds \u2014 breaking alerts appear here automatically."
    else:
        bktext = "\U0001F6F0\uFE0F Connecting to news feeds \u2014 breaking alerts appear here automatically."

    # Whale Alert Feed — real whale-tagged stories when present, home-base placeholder otherwise
    _whale_stories = sorted((s for s in _pool if s.get("category") == "Whale"), key=lambda s: s["dt"], reverse=True)[:8]
    if _whale_stories:
        whale_feed_html = "".join(
            f'<div class="wa-row"><span class="wa-src">{html.escape(w["source"])}</span>'
            f'<a class="wa-hl" href="{html.escape(w["link"], quote=True)}" target="_blank" rel="noopener">{html.escape(w["title"])}</a>'
            f'<span class="wa-time">{_time_ago(w["dt"])}</span></div>'
            for w in _whale_stories
        )
        whale_ts_val = _time_ago(_whale_stories[0]["dt"])
    else:
        whale_feed_html = (
            '<div class="home-base"><div class="home-base-icon">\U0001F433</div>'
            '<div class="home-base-title">Monitoring On-Chain Movements</div>'
            '<div class="home-base-sub">Whale-sized transfers surface here automatically as soon as they appear in the live news feed \u2014 no action needed.</div></div>'
        )
        whale_ts_val = "\u2014"

    # XRP price — red or green by movement
    if MARKET["xrp_price"] is not None:
        chg = MARKET["xrp_chg"] or 0
        price_color = "#48ff82" if chg >= 0 else "#ff4060"
        arrow = "\u25B2" if chg >= 0 else "\u25BC"
        price_str = f"${MARKET['xrp_price']:.4f}"
        chg_str = f"{arrow} {abs(chg):.2f}%"
    else:
        price_color = "#8099b3"
        price_str = "\u2014"
        chg_str = ""

    sources_str = f"{MARKET['sources_active']} / {MARKET['sources_total']}"
    fng_label = MARKET["fng_label"] or ""
    fng_bar = fng_bar_html(MARKET["fng"])

    # ── Section 3 values ──
    def rsi_parts(v):
        if v is None:
            return "--", "--", "var(--tx)", 50
        if v >= 70:
            col, lbl = "#ff4060", "Overbought"
        elif v <= 30:
            col, lbl = "#48ff82", "Oversold"
        else:
            col, lbl = "#75bcff", "Neutral"
        return f"{v:.1f}", lbl, col, max(0, min(100, v))

    r1h_val, r1h_lbl, r1h_col, r1h_pct = rsi_parts(MARKET["rsi_1h"])
    r1d_val, r1d_lbl, r1d_col, r1d_pct = rsi_parts(MARKET["rsi_1d"])

    cur = MARKET["xrp_price"]
    lo, hi = MARKET["w52_low"], MARKET["w52_high"]
    if cur and lo and hi and hi > lo:
        w52_pos = (cur - lo) / (hi - lo) * 100
        w52_low_s  = f"${lo:.4f}"
        w52_high_s = f"${hi:.4f}"
        w52_cur_s  = f"${cur:.4f}"
        w52_from_low  = f"+{(cur-lo)/lo*100:.1f}%"
        w52_from_high = f"{(cur-hi)/hi*100:.1f}%"
        w52_pos_s = f"{w52_pos:.0f}%"
    else:
        w52_pos = 50
        w52_low_s = w52_high_s = w52_cur_s = "--"
        w52_from_low = w52_from_high = w52_pos_s = "--"

    sup, res = MARKET["sr_support"], MARKET["sr_resistance"]
    if sup and res:
        sr_html = (f'<div class="sr-line"><span style="color:var(--rd)">Resistance</span>'
                   f'<span style="color:var(--rd);font-weight:700">${res:.4f}</span></div>'
                   f'<div class="sr-line"><span style="color:var(--tx)">Current</span>'
                   f'<span style="color:var(--br);font-weight:700">${cur:.4f}</span></div>'
                   f'<div class="sr-line"><span style="color:var(--gr)">Support</span>'
                   f'<span style="color:var(--gr);font-weight:700">${sup:.4f}</span></div>') if cur else \
                  '<div class="empty">Calculating from 90-day price history...</div>'
    else:
        sr_html = '<div class="empty">Calculating from 90-day price history...</div>'

    def tm_box(price_then, label):
        if price_then and cur:
            chg = (cur - price_then) / price_then * 100
            col = "#48ff82" if chg >= 0 else "#ff4060"
            arrow = "\u25B2" if chg >= 0 else "\u25BC"
            return (f'<div class="albl">{label}</div>'
                    f'<div class="aval">${price_then:.4f}</div>'
                    f'<div class="asub" style="color:{col}">{arrow} {abs(chg):.1f}%</div>')
        return f'<div class="albl">{label}</div><div class="aval">--</div><div class="asub">--</div>'

    tm_1y_html = tm_box(MARKET["tm_1y"], "1 Year Ago")
    tm_1m_html = tm_box(MARKET["tm_1m"], "1 Month Ago")
    if MARKET["tm_1y"] and cur:
        chg1y = (cur - MARKET["tm_1y"]) / MARKET["tm_1y"] * 100
        updown = "up" if chg1y >= 0 else "down"
        tm_narr = f"XRP is {updown} {abs(chg1y):.1f}% versus one year ago (${MARKET['tm_1y']:.4f} then vs ${cur:.4f} now)."
    else:
        tm_narr = "Loading..."

    # Escrow release date + ecosystem cards
    esc = next_escrow_release()
    esc_date_str = esc.strftime("%b %d, %Y")
    esc_iso = esc.strftime("%Y-%m-%dT%H:%M:%SZ")
    eco_html = ecosystem_cards_html()
    inst_html = institution_cards_html()
    tl_html = timeline_html()
    stories_current = story_rows_html(NEWS["current"])
    stories_weekly = story_rows_html(NEWS["weekly"])

    us = us_intelligence()
    gl = global_pulse()
    _sig_col = {"bullish": "var(--gr)", "bearish": "var(--rd)", "neutral": "var(--yl)", "quiet": "var(--tx)"}
    gl_signals_html = "".join(
        f'<span class="sig-chip" style="color:{_sig_col[gl["signals"][r]]}">'
        f'<span class="sig-dot" style="background:{_sig_col[gl["signals"][r]]}"></span>'
        f'{REGION_FLAGS[r]} {r}: {gl["signals"][r]}</span>'
        for r in REGIONS
    )
    us_ts = us["ts"] or "\u2014"
    gl_ts = gl["ts"] or "\u2014"
    us_pulse = us["pulse"]
    us_regulatory = us["regulatory"]
    us_institutional = us["institutional"]
    gl_pulse = gl["pulse"]
    gl_thesis = gl["thesis"]
    rd_html = regional_discourse_html()

    # Signal Scoreboard
    sb_total, sb_bull, sb_bear, sb_neut = signal_stats()
    _t = sb_total or 1
    sb_bull_pct = round(sb_bull / _t * 100)
    sb_bear_pct = round(sb_bear / _t * 100)
    sb_net = sb_bull - sb_bear
    sb_net_col = "var(--gr)" if sb_net >= 0 else "var(--rd)"
    sb_net_str = f"+{sb_net}" if sb_net >= 0 else str(sb_net)
    sb_fng = MARKET["fng"] if MARKET["fng"] is not None else "\u2014"
    sb_fng_lbl = MARKET["fng_label"] or "\u2014"
    sb_rank = f'#{MARKET["rank"]}' if MARKET.get("rank") else "#\u2014"
    sb_mcap = _fmt_usd(MARKET.get("mcap"))
    sb_vol = _fmt_usd(MARKET.get("vol24"))
    sb_high = f'${MARKET["h24"]:.4f}' if MARKET.get("h24") else "\u2014"
    sb_low = f'${MARKET["l24"]:.4f}' if MARKET.get("l24") else "\u2014"
    sb_feeds = f'{NEWS["feeds_active"]}/{NEWS["feeds_total"]}'

    # Global Liquidity Tracker (V103) — computed from existing CoinPaprika data, no new calls
    liq_vol  = _fmt_usd(MARKET.get("vol24"))
    liq_mcap = _fmt_usd(MARKET.get("mcap"))
    _v, _m = MARKET.get("vol24"), MARKET.get("mcap")
    if _v and _m:
        _t = (_v / _m) * 100.0
        liq_turn = f"{_t:.2f}%"
        # Rating bands: major-asset daily turnover context — <2% thin, 2-5% moderate,
        # 5-12% healthy, >12% very deep
        if _t >= 12:   liq_rating, liq_color, liq_pct = "VERY DEEP", "var(--gr)", 100
        elif _t >= 5:  liq_rating, liq_color, liq_pct = "HEALTHY",   "var(--gr)", 78
        elif _t >= 2:  liq_rating, liq_color, liq_pct = "MODERATE",  "var(--yl)", 50
        else:          liq_rating, liq_color, liq_pct = "THIN",      "var(--rd)", 22
    else:
        liq_turn, liq_rating, liq_color, liq_pct = "\u2014", "\u2014", "var(--tx)", 0

    # On-Chain / Market Vitals — rebuilt to use reliably-populated MARKET data (V95)
    oc_mcap = _fmt_usd(MARKET.get("mcap"))
    oc_rank = f'Rank #{MARKET["rank"]}' if MARKET.get("rank") else "Rank \u2014"
    oc_vol = _fmt_usd(MARKET.get("vol24"))
    if MARKET.get("vol24") and MARKET.get("mcap"):
        oc_volmcap = f'{MARKET["vol24"] / MARKET["mcap"] * 100:.1f}% of mcap'
    else:
        oc_volmcap = "\u2014"
    oc_high = f'${MARKET["h24"]:.4f}' if MARKET.get("h24") else "\u2014"
    oc_low = f'${MARKET["l24"]:.4f}' if MARKET.get("l24") else "\u2014"
    oc_rsi = f'RSI {MARKET["rsi_1d"]:.0f}' if MARKET.get("rsi_1d") else "RSI \u2014"
    oc_52h = f'${MARKET["w52_high"]:.4f}' if MARKET.get("w52_high") else "\u2014"
    oc_52l = f'${MARKET["w52_low"]:.4f}' if MARKET.get("w52_low") else "\u2014"

    # Global News Feed + right rail
    gn_html = global_feed_html()
    gn_total = len(NEWS.get("pool", []))
    gn_shown = min(gn_total, 60)
    # Market Structure (excluded rows dropped: ATH, % Below ATH)
    ms_rank = f'#{MARKET["rank"]}' if MARKET.get("rank") else "\u2014"
    ms_price = f'${MARKET["xrp_price"]:.4f}' if MARKET.get("xrp_price") else "\u2014"
    if MARKET.get("xrp_chg") is not None:
        _c = MARKET["xrp_chg"]
        ms_chg = f'{_c:+.2f}%'
        ms_chg_col = "var(--gr)" if _c >= 0 else "var(--rd)"
    else:
        ms_chg = "\u2014"
        ms_chg_col = "var(--tx)"
    ms_mcap = _fmt_usd(MARKET.get("mcap"))
    ms_vol = _fmt_usd(MARKET.get("vol24"))
    if MARKET.get("vol24") and MARKET.get("mcap"):
        ms_volmcap = f'{MARKET["vol24"] / MARKET["mcap"] * 100:.2f}%'
    else:
        ms_volmcap = "\u2014"
    ms_high = f'${MARKET["h24"]:.4f}' if MARKET.get("h24") else "\u2014"
    ms_low = f'${MARKET["l24"]:.4f}' if MARKET.get("l24") else "\u2014"
    ms_xrpbtc = f'{MARKET["xrpbtc"]:.8f}' if MARKET.get("xrpbtc") else "\u2014"
    esc_next_str = esc_date_str

    # Analytics Lab
    al_ratio = (f'{(sb_bull / sb_bear):.2f}:1 bull/bear' if sb_bear else ('\u221E bull/bear' if sb_bull else '0:0'))
    al_fng = f'{MARKET["fng"]} \u2014 {MARKET["fng_label"]}' if MARKET.get("fng") is not None else "\u2014"
    al_foreign = sum(1 for s in NEWS.get("pool", []) if s.get("foreign"))

    # XRP Complete Leaderboard
    lb_ss = signal_score()
    lb_score = lb_ss["score"]
    lb_label = lb_ss["label"]
    lb_color = lb_ss["color"]
    lb_sources = lb_sources_html()
    lb_regions = lb_regions_html()

    # XRP Intelligence Brief — never show an empty box if a prior edition exists anywhere in the archive
    if not BRIEF.get("sections"):
        try:
            generate_brief()
        except Exception:
            pass
    if not BRIEF.get("sections") and BRIEF_ARCHIVE:
        # Fall back to the most recent archived edition instead of a placeholder
        _latest_key = sorted(BRIEF_ARCHIVE.keys())[-1]
        _latest = BRIEF_ARCHIVE[_latest_key]
        BRIEF["sections"] = dict(_latest.get("sections", {}))
        BRIEF["edition"] = _latest.get("edition")
        BRIEF["generated"] = _latest.get("generated")
        BRIEF["slot_id"] = _latest_key
    _bs = BRIEF.get("sections", {})
    brf_edition = BRIEF.get("edition") or "\u2014"
    brf_gen = BRIEF.get("generated") or "\u2014"
    brf_next = BRIEF.get("next_run") or "\u2014"
    brf_pulse = _bs.get("pulse", "\u2014")
    brf_conn = _bs.get("connections", "\u2014")
    brf_domino = _bs.get("domino", "\u2014")
    brf_regional = _bs.get("regional", "\u2014")
    brf_watch = _bs.get("watchlist", "\u2014")
    brf_tradfi = _bs.get("tradfi", "\u2014")
    wc_html = world_clocks_html()

    # Brief Home — designated schedule strip (this week's 14 editions)
    _now_ct = datetime.now(CENTRAL)
    _live_slot = BRIEF.get("slot_id")
    _next_run_dt = _brief_next_run_dt(_now_ct)
    brf_next_iso = _next_run_dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # Single-edition mode: no edition strip. Only the current brief is kept and displayed.
    brf_strip_html = ""
    try:
        _archive_json = json.dumps(BRIEF_ARCHIVE).replace("</", "<\\/")
    except Exception:
        _archive_json = "{}"

    # Unique Displays — Smart Money Score + F&G history
    sm = smart_money()
    sm_score = sm["score"]
    sm_label = sm["label"]
    sm_color = sm["color"]
    sm_rows = "".join(
        f'<div class="sm-row"><span class="sm-k">{html.escape(name)}</span><span class="sm-v">{html.escape(val)}</span></div>'
        for name, val, _ in sm["comps"]
    ) or '<div class="sm-row"><span class="sm-k">Awaiting live signals\u2026</span><span class="sm-v">\u2014</span></div>'
    fng_hist_html = fng_history_html()

    # Longitudinal Value Markers
    def _perf_card(label, val):
        if val is None:
            return f'<div class="lvm-card"><div class="lvm-win">{label}</div><div class="lvm-val" style="color:var(--tx)">\u2014</div><div class="lvm-sub">price change</div></div>'
        col = "var(--gr)" if val >= 0 else "var(--rd)"
        arrow = "\u25B2" if val >= 0 else "\u25BC"
        return (f'<div class="lvm-card"><div class="lvm-win">{label}</div>'
                f'<div class="lvm-val" style="color:{col}">{arrow} {abs(val):.1f}%</div>'
                f'<div class="lvm-sub">price change</div></div>')
    lvm_html = (_perf_card("1 Week", MARKET.get("perf_1w")) + _perf_card("30 Day", MARKET.get("perf_30d")) +
                _perf_card("90 Day", MARKET.get("perf_90d")) + _perf_card("6 Month", MARKET.get("perf_6m")))

    # Regional News Activity Heatmap
    rh_html = regional_heatmap_html()

    # V109: 30-Day Historical Price Table, News Mention Volume, DCA Calculator data
    hist30_html = historical_30d_html()
    nmv_cat_html, nmv_day_label, nmv_total, nmv_contributors, nmv_day_str = news_mention_volume_html()
    dca_history_json = json.dumps([
        {"t": r["t"], "c": round(r["c"], 6)} for r in (MARKET.get("hist_full") or [])
    ])
    dca_days_available = len(MARKET.get("hist_full") or [])

    # Sentiment Engine
    _isc_score, _isc_label = interest_score()
    vel_html = velocity_chart_html()
    sdt_html = sentiment_trend_html()
    sent_lb_rows = sentiment_leaderboard_html()

    # Competitive Briefing
    comp_rows = competitor_table_html()
    odl_html = odl_corridors_html()
    iso_html = iso20022_html()

    # Ripple Executive Tracker + XRPL Dev Activity
    ex_html = exec_tracker_html()
    ex_ts = EXEC_TRACKER.get("updated") or "\u2014"
    gh_commits_html = github_commits_html()
    gh_ts = GITHUB_DEV.get("updated") or "\u2014"
    gh_stars = f'{GITHUB_DEV.get("stars", 0):,}'
    gh_issues = f'{GITHUB_DEV.get("issues", 0):,}'
    gh_rippled_7d = GITHUB_DEV.get("rippled_7d", 0)
    gh_other_7d = GITHUB_DEV.get("other_7d", 0)
    _commits = GITHUB_DEV.get("commits", [])
    if _commits:
        gh_last_msg = html.escape(_commits[0]["msg"] or "(no message)")
        gh_last_meta = f'{html.escape(_commits[0]["author"])} \u00B7 {html.escape(_commits[0]["date"])}'
    else:
        gh_last_msg = "Awaiting first sync\u2026"
        gh_last_meta = "\u2014"

    # Regulatory Radar
    cg_html = country_grid_html()
    etf_html = etf_tracker_html()
    sec_tl_html = sec_timeline_html()
    mica_html = mica_calendar_html()
    cbdc_html = cbdc_grid_html()

    # Global XRP Enterprise & Partnership Ledger
    pl_html = partnership_ledger_html()
    pl_total = len(PARTNERSHIP_LEDGER)
    pl_detected = sum(1 for e in PARTNERSHIP_LEDGER if e["source"] == "detected")

    # Static Global Partnership Directory (right rail, refreshes every 3 days)
    sd_entries = STATIC_PARTNER_DIRECTORY.get("entries", [])
    sd_updated = STATIC_PARTNER_DIRECTORY.get("last_refreshed") or "\u2014"
    sd_count = len(sd_entries)
    sd_html = "".join(
        f'<div class="sd-item">'
        f'<div class="sd-item-top"><span class="sd-flag">{flag}</span>'
        f'<span class="sd-name">{html.escape(name)}</span></div>'
        f'<span class="sd-cat">{cat_emoji} {html.escape(cat_lbl)}</span>'
        f'<span class="sd-desc">{html.escape(desc)}</span></div>'
        for name, desc, cat_lbl, cat_emoji, flag in sd_entries
    ) or '<div class="sd-empty">Directory loading\u2026</div>'

    pl_by_cat = {}
    for e in PARTNERSHIP_LEDGER:
        pl_by_cat[e["cat"]] = pl_by_cat.get(e["cat"], 0) + 1

    # Advanced Metrics
    ts_html = tech_specs_html()
    uc_html = use_case_html()
    ad_s7, ad_c7, ad_s30, ad_c30 = ad_line_html()
    corr_html = correlation_html()
    ob_bid_html, ob_ask_html, ob_bid_total, ob_ask_total = orderbook_html()
    ob_has_data = bool(MARKET.get("ob_bids") and MARKET.get("ob_asks"))
    if ob_has_data:
        ob_body_html = (
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">'
            f'<div><div style="font-size:15px;font-weight:700;color:var(--gr);font-family:var(--mn);margin-bottom:6px;text-align:center">\U0001F7E2 BUY WALLS (BIDS)</div>'
            f'{ob_bid_html}'
            f'<div style="margin-top:8px;padding:6px;background:rgba(72,255,130,.1);border:1px solid rgba(72,255,130,.2);border-radius:4px;text-align:center">'
            f'<span style="font-size:12px;color:var(--tx)">Total Bid Depth: </span>'
            f'<span style="font-size:15px;font-weight:700;color:var(--gr);font-family:var(--mn)">{ob_bid_total}</span></div></div>'
            f'<div><div style="font-size:15px;font-weight:700;color:var(--rd);font-family:var(--mn);margin-bottom:6px;text-align:center">\U0001F534 SELL WALLS (ASKS)</div>'
            f'{ob_ask_html}'
            f'<div style="margin-top:8px;padding:6px;background:rgba(255,64,96,.1);border:1px solid rgba(255,64,96,.2);border-radius:4px;text-align:center">'
            f'<span style="font-size:12px;color:var(--tx)">Total Ask Depth: </span>'
            f'<span style="font-size:15px;font-weight:700;color:var(--rd);font-family:var(--mn)">{ob_ask_total}</span></div></div>'
            f'</div>'
        )
    else:
        ob_body_html = ob_bid_html  # home-base placeholder
    liq_html = liquidity_map_html()

    # CLARITY Act Tracker
    ca_html = clarity_tracker_html()
    ca_count = len(CLARITY_ACT_STORIES)

    # XRP Complete Exclusive Intelligence — Institutional Confidence Index
    _ici = institutional_confidence_index()
    ici_score = _ici["score"]
    ici_label = _ici["label"]
    ici_color = _ici["color"]
    ici_comps_rendered = ici_comps_html(_ici["comps"])
    pm_bars, pm_total, pm_this_week, pm_trend, pm_tcol, pm_avg = partnership_momentum_html()
    cc_cells, cc_peak, cc_hourlbls = catalyst_clock_html()
    cc_total = _CATALYST_TOTAL
    nd_cards, nd_fastest = narrative_diffusion_html()
    flagship_ts = MARKET.get("updated") or NEWS.get("updated") or "\u2014"

    # Regulatory & Ledger Watch (V66)
    rw_amendments = ""
    for a in REG_WATCH["amendments"]:
        eta = f' \u00B7 ETA {html.escape(str(a["eta"])[:10])}' if a.get("eta") else ""
        rw_amendments += (f'<div class="rw-item"><span class="rw-name">{html.escape(a["name"])}</span>'
                          f'<span class="rw-meta">{a["count"]} validator votes{eta}</span></div>')
    if not rw_amendments:
        rw_amendments = '<div class="rw-empty">No pending amendments detected \u2014 all active amendments enabled, or data refreshing\u2026</div>'

    rw_edgar = ""
    for e in REG_WATCH["edgar"]:
        d = f'<span class="rw-meta">{html.escape(e["date"])}</span>' if e.get("date") else ""
        rw_edgar += (f'<div class="rw-item"><a href="{html.escape(e["link"])}" target="_blank" rel="noopener" '
                     f'class="rw-link">{html.escape(e["title"])}</a>{d}</div>')
    if not rw_edgar:
        rw_edgar = '<div class="rw-empty">No recent Ripple/XRP filings detected \u2014 data refreshing\u2026</div>'

    rw_fedreg = ""
    for f in REG_WATCH["fedreg"]:
        agency = f' \u00B7 {html.escape(f["agency"])}' if f.get("agency") else ""
        rw_fedreg += (f'<div class="rw-item"><a href="{html.escape(f["link"])}" target="_blank" rel="noopener" '
                      f'class="rw-link">{html.escape(f["title"])}</a>'
                      f'<span class="rw-meta">{html.escape(f["date"])}{agency}</span></div>')
    if not rw_fedreg:
        rw_fedreg = '<div class="rw-empty">No recent federal rulemaking detected \u2014 data refreshing\u2026</div>'

    rw_updated = REG_WATCH.get("updated") or "\u2014"

    # Practical Tools — multi-currency conversion (XRP price x FX rate)
    _fx = MARKET.get("fx") or {}
    _xp = MARKET.get("xrp_price") or 0
    def _fx_val(code, dec=4):
        rate = _fx.get(code)
        if rate is None or not _xp:
            return "\u2014"
        return f"{_xp * rate:,.{dec}f}"
    fx_eur = _fx_val("EUR"); fx_gbp = _fx_val("GBP"); fx_jpy = _fx_val("JPY", 2)
    fx_aud = _fx_val("AUD"); fx_cad = _fx_val("CAD"); fx_sgd = _fx_val("SGD")
    fx_inr = _fx_val("INR", 2); fx_brl = _fx_val("BRL")
    fx_chf = _fx_val("CHF"); fx_cny = _fx_val("CNY", 2); fx_krw = _fx_val("KRW", 0)
    fx_mxn = _fx_val("MXN", 2); fx_php = _fx_val("PHP", 2); fx_ngn = _fx_val("NGN", 2)
    fx_zar = _fx_val("ZAR", 2); fx_aed = _fx_val("AED", 2); fx_sar = _fx_val("SAR", 2)
    fx_hkd = _fx_val("HKD", 2); fx_nzd = _fx_val("NZD"); fx_sek = _fx_val("SEK", 2)
    fx_nok = _fx_val("NOK", 2); fx_try = _fx_val("TRY", 2); fx_thb = _fx_val("THB", 2)
    fx_idr = _fx_val("IDR", 0); fx_vnd = _fx_val("VND", 0); fx_pln = _fx_val("PLN", 2)
    fx_usd_disp = f"{_xp:.4f}" if _xp else "\u2014"
    fx_ts = MARKET.get("updated") or "\u2014"
    xrp_price_js = _xp or 0

    modal_rows = ""
    for label, ok, detail in checks:
        c = "#48ff82" if ok else "#ff4060"
        t = "PASS" if ok else "FAIL"
        modal_rows += (
            '<div class="pf-row">'
            f'<span class="pf-row-label">{label}</span>'
            f'<span class="pf-row-badge" style="color:{c}">{t}</span>'
            f'<span class="pf-row-detail">{detail}</span>'
            '</div>'
        )

    _regnew = regulatory_sections()

    _head = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{APP_NAME} \u2014 {TAGLINE}</title>
<style>
  :root{{
    --bg:#000; --s1:#161f2e; --s2:#111; --b:#1a2030;
    --gr:#48ff82; --grd:rgba(72,255,130,.1);
    --rd:#ff4060; --rdd:rgba(255,64,96,.1);
    --yl:#ffcc00; --yld:rgba(255,204,0,.1);
    --bl:#75bcff; --bld:rgba(117,188,255,.12);
    --tq:#00e5cc; --tqd:rgba(0,229,204,.15);
    --or:#ff9900; --tx:#a8bdd0; --br:#cce0ff; --hdr:#03b1fc;
    --mn:'Courier New',monospace;
  }}
  *{{ box-sizing:border-box; }}
  body{{ background:var(--bg); color:var(--br); font-family:system-ui,sans-serif; font-size:15px; min-height:100vh; -webkit-font-smoothing:antialiased; margin:0; }}
  .w{{ max-width:1400px; margin:0 auto; padding:10px 24px; }}
  @media(max-width:1440px){{ .w{{ max-width:1280px; padding:10px 18px; }} }}

  /* BREAKING NEWS BAR */
  #breaking{{ background:var(--s1); padding:8px 0; overflow:hidden; }}
  .bkinner{{ max-width:2400px; margin:0 auto; padding:0 28px; }}
  .bkrow{{ display:flex; align-items:center; width:100%; padding-bottom:8px; border-bottom:2px solid var(--hdr); }}
  .bklbl{{ color:var(--hdr); font-weight:900; font-size:17px; font-family:var(--mn); flex-shrink:0; padding-right:14px; margin-right:14px; border-right:2px solid rgba(3,177,252,.5); text-transform:uppercase; letter-spacing:.08em; display:inline-flex; align-items:center; gap:9px; }}
  .bk-bolt{{ font-size:22px; }}
  .bkscroll{{ flex:1; overflow:hidden; height:26px; position:relative; display:flex; align-items:center; }}
  .bktext{{ display:inline-block; animation:bkscroll 45s linear infinite; white-space:nowrap; will-change:transform; padding-left:100%; font-size:15px; color:var(--br); font-family:system-ui; font-weight:500; line-height:26px; }}
  .bkscroll:hover .bktext{{ animation-play-state:paused; }}
  @keyframes bkscroll{{ 0%{{transform:translateX(0)}} 100%{{transform:translateX(-100%)}} }}

  /* HEADER */
  .hdr{{ display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; padding-top:36px; padding-bottom:40px; border-bottom:2px solid var(--hdr); flex-wrap:wrap; gap:6px; }}
  .logo{{ display:flex; align-items:center; gap:12px; }}
  .icon{{ width:auto; height:125px; border-radius:0; background:#000000;
          box-shadow:none; display:flex; align-items:center; justify-content:center; padding:0; }}
  .icon img{{ height:125px; width:auto; display:block; background:#000000; }}
  .f-helix{{ height:20px; width:auto; vertical-align:middle; display:inline-block; }}
  .title{{ font-size:22px; font-weight:900; color:var(--br); font-style:italic; }}
  .sub{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-top:2px; letter-spacing:1px; }}
  .hright{{ display:flex; align-items:center; gap:10px; flex-wrap:wrap; }}
  .dot{{ width:12px; height:12px; border-radius:50%; background:var(--gr); box-shadow:0 0 10px var(--gr); display:inline-block; animation:blink 2s infinite; }}
  @keyframes blink{{ 50%{{opacity:.1}} }}
  .run-lbl{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--gr); letter-spacing:1px; }}
  .pill{{ padding:5px 14px; border-radius:20px; font-size:15px; font-family:var(--mn); font-weight:700; letter-spacing:1.5px; text-transform:uppercase; }}
  .plive{{ background:var(--grd); color:var(--gr); border:1px solid rgba(72,255,130,.4); }}
  .upd{{ font-family:var(--mn); font-size:15px; color:var(--tx); }}

  /* STATUS ROW — compact horizontal rectangles */
  .srow{{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin:10px 0; }}
  @media(max-width:700px){{ .srow{{ grid-template-columns:1fr; }} }}
  .si{{ background:var(--s1); border:1px solid rgba(117,188,255,.35); border-radius:8px; padding:14px 18px; display:flex; align-items:center; justify-content:space-between; gap:12px; min-height:64px; }}
  .si-lbl{{ color:#ffffff; font-size:17px; font-family:var(--mn); font-weight:700; letter-spacing:.5px; display:flex; align-items:center; gap:9px; white-space:nowrap; }}
  .si-lbl .ic{{ font-size:22px; }}
  .sv{{ font-weight:800; font-size:22px; font-family:var(--mn); line-height:1; text-align:right; }}
  .sv-sub{{ font-size:15px; font-family:var(--mn); margin-top:2px; }}

  /* FEAR & GREED horizontal line + ball */
  .fng-wrap{{ position:relative; width:180px; height:34px; display:flex; align-items:center; flex-shrink:0; }}
  .fng-bar{{ width:100%; height:10px; border-radius:6px;
    background:linear-gradient(90deg,#ea3943,#ea8c00,#f3d42f,#93d900,#16c784); }}
  .fng-ball{{ position:absolute; top:50%; transform:translate(-50%,-50%);
    width:32px; height:32px; border-radius:50%; border:2px solid #fff;
    display:flex; align-items:center; justify-content:center;
    font-family:var(--mn); font-weight:800; font-size:15px; color:#fff;
    text-shadow:0 1px 2px rgba(0,0,0,.7); box-shadow:0 0 6px rgba(0,0,0,.5); }}

  /* SECTION 3 — technical panels (RSI, S&R, Time Machine, 52-Week) */
  .grid2{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0; align-items:stretch; }}
  .col{{ display:flex; flex-direction:column; gap:10px; }}
  .acct{{ background:var(--s1); border:1px solid rgba(117,188,255,.4); border-radius:10px; padding:14px; }}
  .acct.grow{{ flex:1; }}   /* lets 52-week + time machine match column height */
  .sec-title{{ font-size:17px; text-transform:uppercase; letter-spacing:2px; font-family:var(--mn); color:#ffffff; margin-bottom:12px; font-weight:800; display:flex; align-items:center; gap:10px; }}
  .sec-title .sic{{ font-size:22px; }}   /* header icon = same size as status-row icons */
  .rsi-head{{ display:flex; justify-content:space-between; margin-bottom:6px; font-size:15px; font-family:var(--mn); }}
  .rsi-track{{ height:11px; background:var(--s2); border-radius:6px; overflow:hidden; border:1px solid var(--b); position:relative; }}
  .rsi-tick{{ position:absolute; top:0; bottom:0; width:1px; background:rgba(255,255,255,.12); }}
  .rsi-fill{{ height:100%; border-radius:6px; transition:all .6s; }}
  .rsi-scale{{ display:flex; justify-content:space-between; font-size:15px; font-family:var(--mn); color:var(--tx); margin-top:3px; }}
  .w52-row{{ display:flex; justify-content:space-between; font-family:var(--mn); font-size:15px; }}
  .w52-bar{{ height:15px; background:linear-gradient(90deg,var(--rd),var(--yl),var(--gr)); border-radius:7px; position:relative; border:1px solid var(--b); margin:10px 0; }}
  .w52-needle{{ position:absolute; top:-4px; width:6px; height:23px; background:var(--br); border-radius:3px; border:2px solid var(--bg); transform:translateX(-50%); transition:left .6s; }}
  .agrid2{{ display:grid; grid-template-columns:repeat(2,1fr); gap:8px; }}
  .abox{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:14px; text-align:center; }}
  .albl{{ font-size:15px; text-transform:uppercase; letter-spacing:1.5px; font-family:var(--mn); color:var(--tx); margin-bottom:6px; }}
  .aval{{ font-size:22px; font-weight:900; font-family:var(--mn); color:var(--br); line-height:1; }}
  .asub{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-top:5px; }}
  .sr-line{{ display:flex; justify-content:space-between; font-family:var(--mn); font-size:15px; padding:8px 0; border-bottom:1px solid var(--b); }}
  .sr-line:last-child{{ border-bottom:none; }}
  .empty{{ padding:16px; font-family:var(--mn); font-size:15px; color:var(--tx); text-align:center; }}

  /* Reusable "home base" — reserved space for upcoming/still-filling sections */
  .home-base{{ padding:26px 20px; text-align:center; border:1px dashed rgba(128,153,179,.3); border-radius:8px;
    background:rgba(128,153,179,.03); }}
  .home-base-icon{{ font-size:32px; line-height:1; margin-bottom:10px; opacity:.85; }}
  .home-base-title{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:.5px; color:var(--br); margin-bottom:5px; }}
  .home-base-sub{{ font-size:12px; font-family:var(--mn); color:var(--tx); max-width:420px; margin:0 auto; line-height:1.6; }}
  .tvs{{ margin-top:12px; padding:10px 12px; background:var(--s2); border-radius:6px; border:1px solid var(--b); }}
  .tvs-lbl{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-bottom:4px; text-transform:uppercase; letter-spacing:1px; }}
  .tvs-txt{{ font-size:15px; color:var(--br); line-height:1.6; }}

  /* SECTION 5 — On-Chain Intelligence + Whale Alert Feed */
  .oc-grid{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0; align-items:stretch; }}
  .ocbox-grid{{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; }}
  .ocbox{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:14px; text-align:center; }}
  .ocbox.tq{{ border-color:rgba(0,229,204,.3); background:var(--tqd); }}
  .ocbox.esc{{ border-color:rgba(72,255,130,.3); background:var(--grd); grid-column:span 2; }}
  .oclbl{{ font-size:15px; text-transform:uppercase; letter-spacing:1.5px; font-family:var(--mn); color:var(--tx); margin-bottom:6px; }}
  .ocval{{ font-size:17px; font-weight:900; font-family:var(--mn); color:var(--br); line-height:1; }}
  .ocsub{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-top:5px; }}
  .esc-row{{ display:flex; align-items:baseline; gap:10px; justify-content:center; margin:6px 0; }}
  .esc-num{{ font-size:22px; font-weight:900; font-family:var(--mn); color:var(--gr); line-height:1; }}
  .esc-sep{{ color:var(--tx); font-size:17px; font-family:var(--mn); }}
  .panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; overflow:hidden; }}
  .ph{{ padding:10px 14px; border-bottom:1px solid var(--b); display:flex; justify-content:space-between; align-items:center; background:var(--s2); }}
  .pt{{ font-size:17px; text-transform:uppercase; letter-spacing:2px; font-family:var(--mn); font-weight:800; display:flex; align-items:center; gap:10px; }}
  .pt .sic{{ font-size:22px; }}
  .whale-feed{{ padding:8px 14px; max-height:240px; overflow-y:auto; }}
  .wa-row{{ display:flex; align-items:center; gap:10px; padding:8px 0; border-bottom:1px solid rgba(26,32,48,.4); font-family:var(--mn); font-size:15px; }}
  .wa-row:last-child{{ border-bottom:none; }}
  .wa-src{{ color:var(--yl); font-weight:700; white-space:nowrap; }}
  .wa-hl{{ color:var(--br); text-decoration:none; flex:1; }}
  .wa-hl:hover{{ color:var(--hdr); text-decoration:underline; }}
  .wa-time{{ color:var(--tx); white-space:nowrap; font-size:12px; }}
  .whale-item{{ padding:10px 0; border-bottom:1px solid var(--b); }}
  .whale-item:last-child{{ border-bottom:none; }}
  .whale-hl{{ font-size:15px; font-weight:700; color:var(--yl); font-family:system-ui; line-height:1.4; margin-bottom:4px; }}
  .whale-meta{{ font-size:15px; font-family:var(--mn); color:var(--tx); }}

  /* SECTION 6 — XRP Ecosystem */
  .eco-wrap{{ background:linear-gradient(135deg,#06060f,#0a0a18); border:1px solid rgba(72,255,130,.35); border-radius:12px; overflow:hidden; margin:10px 0; }}
  .eco-head{{ padding:16px 18px; background:rgba(117,188,255,.06); border-bottom:1px solid rgba(117,188,255,.2); display:flex; align-items:center; gap:14px; }}
  .eco-head .gicon{{ font-size:22px; filter:drop-shadow(0 0 10px rgba(117,188,255,.6)); }}
  .eco-title{{ font-size:17px; font-weight:900; color:var(--hdr); font-family:var(--mn); text-transform:uppercase; letter-spacing:2px; }}
  .eco-sub{{ font-size:15px; font-family:system-ui; color:var(--bl); margin-top:3px; }}
  .eco-grid{{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; padding:14px 18px; }}
  .eco-card{{ border-radius:8px; padding:14px; position:relative; overflow:hidden; }}
  .eco-bar{{ position:absolute; top:0; left:0; right:0; height:2px; }}
  .eco-ic{{ font-size:22px; margin-bottom:6px; }}
  .eco-name{{ font-size:15px; font-weight:900; color:#fff; font-family:var(--mn); margin-bottom:4px; }}
  .eco-role{{ font-size:15px; font-weight:700; font-family:var(--mn); margin-bottom:8px; text-transform:uppercase; letter-spacing:1px; }}
  .eco-desc{{ font-size:15px; color:var(--tx); line-height:1.6; margin-bottom:10px; font-family:system-ui; }}
  .eco-stat{{ display:flex; justify-content:space-between; font-size:15px; font-family:var(--mn); padding:2px 0; }}
  .eco-stat .k{{ color:var(--tx); }}

  /* SECTION 6b — How the Layers Connect + Misconceptions (inside eco-wrap) */
  .eco-sub-h{{ font-size:15px; font-weight:700; color:var(--hdr); font-family:var(--mn); text-transform:uppercase; letter-spacing:1.5px; margin:6px 0 10px; padding:0 18px; display:flex; align-items:center; gap:8px; }}
  .flow{{ display:flex; align-items:center; justify-content:center; gap:0; overflow-x:auto; padding:6px 18px 18px; }}
  .flow-node{{ display:flex; flex-direction:column; align-items:center; min-width:120px; text-align:center; padding:8px; }}
  .flow-ic{{ font-size:22px; margin-bottom:8px; }}
  .flow-name{{ font-size:15px; font-weight:700; font-family:var(--mn); }}
  .flow-role{{ font-size:15px; color:var(--tx); font-family:var(--mn); margin-top:2px; }}
  .flow-arrow{{ color:var(--bl); font-size:22px; padding:0 8px; flex-shrink:0; font-weight:300; }}
  .myth-grid{{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; padding:0 18px 18px; }}
  .myth-card{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:14px; }}
  .myth-lbl{{ font-size:15px; font-weight:700; color:var(--rd); font-family:var(--mn); margin-bottom:5px; }}
  .myth-q{{ font-size:15px; color:var(--br); font-weight:700; margin-bottom:8px; }}
  .real-lbl{{ font-size:15px; font-weight:700; color:var(--gr); font-family:var(--mn); margin-bottom:5px; }}
  .real-txt{{ font-size:15px; color:var(--tx); line-height:1.55; font-family:system-ui; }}

  /* SECTION 7 — Mainstream Integration + Institutional Partnership trackers */
  .trk-tag{{ font-size:15px; font-style:italic; color:var(--yl); font-family:system-ui; margin:2px 0 12px; line-height:1.5; }}
  .trk-legend{{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:6px; }}
  .trk-btn{{ padding:6px 12px; border-radius:4px; font-size:15px; font-weight:700; font-family:var(--mn); letter-spacing:.5px; border:1px solid; cursor:pointer; background:transparent; opacity:.6; transition:opacity .15s; }}
  .trk-btn:hover{{ opacity:.9; }}
  .trk-btn.active{{ opacity:1; box-shadow:0 0 0 1px currentColor inset; }}
  .trk-grid{{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; }}
  .trk-card{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:12px 14px; display:flex; flex-direction:column; }}
  .trk-top{{ display:flex; align-items:center; justify-content:space-between; gap:8px; margin-bottom:6px; }}
  .trk-status{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1px; display:flex; align-items:center; gap:6px; }}
  .trk-type{{ font-size:15px; color:var(--tx); font-family:var(--mn); white-space:nowrap; }}
  .trk-name{{ font-size:17px; font-weight:800; color:var(--br); font-family:var(--mn); margin-bottom:6px; }}
  .trk-detail{{ font-size:15px; color:var(--tx); line-height:1.5; font-family:system-ui; margin-bottom:8px;
    display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }}
  .trk-src{{ font-size:12px; font-style:italic; color:var(--tx); font-family:var(--mn); margin-top:auto; }}
  .trk-empty{{ padding:22px; text-align:center; color:var(--tx); font-family:var(--mn); font-size:15px; border:1px dashed var(--b); border-radius:8px; margin-top:8px; }}

  /* Integration Timeline (horizontal) */
  .tl-wrap{{ position:relative; padding:6px 0 4px; }}
  .tl-line{{ position:absolute; top:43px; left:0; right:0; height:2px; background:linear-gradient(90deg,transparent,var(--yl),var(--gr),transparent); }}
  .tl-track{{ display:flex; gap:0; overflow-x:auto; padding-bottom:10px; position:relative;
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2); }}
  .tl-track::-webkit-scrollbar{{ height:6px; }}
  .tl-track::-webkit-scrollbar-track{{ background:var(--s2); border-radius:6px; }}
  .tl-track::-webkit-scrollbar-thumb{{ background:#33405e; border-radius:6px; }}
  .tl-node{{ flex:0 0 200px; min-width:200px; text-align:center; padding:0 10px; position:relative; }}
  .tl-top{{ height:44px; display:flex; flex-direction:column; align-items:center; justify-content:flex-end; gap:8px; margin-bottom:12px; }}
  .tl-year{{ font-size:17px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .tl-dot{{ border-radius:50%; box-shadow:0 0 8px currentColor; border:2px solid var(--bg); flex-shrink:0; }}
  .tl-event{{ font-size:15px; font-weight:800; color:var(--br); font-family:var(--mn); margin-bottom:5px; }}
  .tl-detail{{ font-size:15px; color:var(--tx); line-height:1.5; font-family:system-ui; }}

  /* Top 20 XRP Stories */
  .story-list{{ display:flex; flex-direction:column; gap:2px; margin-bottom:14px; }}
  .story{{ display:flex; gap:12px; align-items:flex-start; padding:9px 8px; border-bottom:1px solid var(--b); text-decoration:none; border-radius:6px; }}
  .story:hover{{ background:var(--s2); }}
  .story:last-child{{ border-bottom:none; }}
  .story-num{{ flex:0 0 26px; text-align:center; font-family:var(--mn); font-weight:900; color:var(--hdr); font-size:15px; padding-top:1px; }}
  .story-body{{ display:flex; flex-direction:column; gap:3px; }}
  .story-hl{{ font-size:15px; font-weight:600; color:var(--br); font-family:system-ui; line-height:1.4; }}
  .story:hover .story-hl{{ color:#fff; }}
  .story-meta{{ font-size:15px; font-family:var(--mn); color:var(--tx); text-transform:capitalize; }}

  /* US Intelligence + Global Pulse (2-column) + Regional Discourse */
  .intel-grid{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0; align-items:stretch; }}
  .intel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; overflow:hidden; display:flex; flex-direction:column; }}
  .intel-h{{ padding:10px 14px; border-bottom:1px solid var(--b); background:var(--s2); display:flex; justify-content:space-between; align-items:center; }}
  .intel-t{{ font-size:17px; font-weight:800; font-family:var(--mn); letter-spacing:1.5px; text-transform:uppercase; display:flex; align-items:center; gap:8px; }}
  .intel-t .sic{{ font-size:22px; }}
  .intel-b{{ padding:12px 14px; display:flex; flex-direction:column; gap:10px; }}
  .intel-pulse{{ font-size:15px; color:var(--br); line-height:1.55; font-family:system-ui; }}
  .intel-row{{ font-size:15px; color:var(--tx); line-height:1.5; font-family:system-ui; }}
  .intel-row b{{ color:var(--label,#8099b3); font-family:var(--mn); text-transform:uppercase; letter-spacing:1px; font-size:12px; font-weight:800; }}
  .sig-row{{ display:flex; flex-wrap:wrap; gap:10px; margin-top:6px; }}
  .sig-chip{{ font-size:12px; font-family:var(--mn); font-weight:700; cursor:default; display:inline-flex; align-items:center; gap:5px; }}
  .sig-chip .sig-dot{{ width:7px; height:7px; border-radius:50%; display:inline-block; }}
  .rd-grid{{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; }}
  .rd-card{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:12px 14px; }}
  .rd-top{{ display:flex; justify-content:space-between; align-items:center; gap:8px; margin-bottom:6px; }}
  .rd-name{{ font-size:15px; font-weight:800; color:var(--br); font-family:var(--mn); }}
  .rd-sig{{ font-size:12px; font-weight:700; font-family:var(--mn); padding:1px 8px; border-radius:4px; border:1px solid; text-transform:uppercase; letter-spacing:1px; }}
  .rd-count{{ font-size:15px; color:var(--tx); font-family:var(--mn); margin-bottom:5px; }}
  .rd-hl{{ font-size:15px; color:var(--tx); line-height:1.5; font-family:system-ui;
    display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }}

  /* Signal Scoreboard */
  .sb-grid{{ display:grid; grid-template-columns:repeat(6,1fr); gap:8px; }}
  .sb-grid4{{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-top:8px; }}
  .sb-box{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:12px 10px; text-align:center; }}
  .sb-num{{ font-size:22px; font-weight:900; font-family:var(--mn); line-height:1.1; color:var(--br); }}
  .sb-lbl{{ font-size:12px; text-transform:uppercase; letter-spacing:1px; color:var(--tx); font-family:var(--mn); margin-top:7px; }}
  .sb-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:3px; }}
  .sb-bar{{ height:8px; background:var(--s2); border:1px solid var(--b); border-radius:4px; overflow:hidden; margin-top:10px; }}
  .sb-fill{{ height:100%; background:linear-gradient(90deg,var(--rd),var(--yl),var(--gr)); transition:width .4s; }}
  @media(max-width:900px){{ .sb-grid{{ grid-template-columns:repeat(3,1fr); }} .sb-grid4{{ grid-template-columns:repeat(2,1fr); }} }}

  /* Global News Feed + right rail */
  .feed-wrap{{ display:grid; grid-template-columns:2fr 1fr; gap:10px; margin:10px 0; align-items:start; }}
  .ledger-wrap{{ display:grid; grid-template-columns:2fr 1fr; gap:10px; margin:10px 0; align-items:stretch; }}
  @media(max-width:900px){{ .ledger-wrap{{ grid-template-columns:1fr; }} }}
  .gn-search{{ width:100%; box-sizing:border-box; background:#e9ecf1; border:1px solid #c3c8d1; border-radius:8px;
    color:#1a2a4a; font-family:var(--mn); font-size:15px; padding:12px 14px; margin-bottom:10px; }}
  .gn-search::placeholder{{ color:#6b7280; }}
  .gn-cats{{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:10px; }}
  .gn-btn{{ padding:6px 14px; border-radius:6px; font-size:15px; font-weight:700; font-family:var(--mn); letter-spacing:1px;
    border:1px solid var(--b); background:transparent; color:var(--tx); cursor:pointer; opacity:.75; }}
  .gn-btn:hover{{ opacity:1; }}
  .gn-btn.active{{ opacity:1; box-shadow:0 0 0 1px currentColor inset; }}
  .gn-stats{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-bottom:10px; }}
  .gn-stats b{{ color:var(--gr); }}
  .gn-list{{ display:flex; flex-direction:column; gap:8px; max-height:920px; overflow-y:scroll; padding-right:6px;
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2); }}
  .gn-list::-webkit-scrollbar{{ width:8px; }}
  .gn-list::-webkit-scrollbar-track{{ background:var(--s2); border-radius:6px; }}
  .gn-list::-webkit-scrollbar-thumb{{ background:#33405e; border-radius:6px; }}
  .gn-list::-webkit-scrollbar-thumb:hover{{ background:var(--hdr); }}
  .gn-card{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:14px; }}
  .gn-top{{ display:flex; align-items:center; gap:8px; margin-bottom:8px; flex-wrap:wrap; }}
  .gn-src{{ font-size:12px; font-weight:700; font-family:var(--mn); color:var(--tq); border:1px solid rgba(0,229,204,.4);
    border-radius:4px; padding:1px 8px; }}
  .gn-cat{{ font-size:12px; font-family:var(--mn); color:var(--tx); }}
  .gn-break{{ font-size:12px; font-weight:800; font-family:var(--mn); color:var(--yl); letter-spacing:1px; }}
  .gn-time{{ font-size:12px; font-family:var(--mn); color:var(--tx); margin-left:auto; }}
  .gn-hl{{ display:block; font-size:17px; font-weight:700; color:var(--hdr); font-family:system-ui; line-height:1.4;
    text-decoration:none; margin-bottom:4px; }}
  .gn-hl:hover{{ text-decoration:underline; }}
  .gn-tr{{ display:inline-block; font-size:15px; font-family:var(--mn); color:var(--tx); text-decoration:none; margin-bottom:6px; }}
  .gn-tr:hover{{ color:var(--hdr); text-decoration:underline; }}
  .gn-sum{{ font-size:15px; color:var(--tx); line-height:1.6; font-family:system-ui; margin-bottom:8px; }}
  .gn-foot{{ display:flex; align-items:center; gap:8px; font-size:15px; font-family:var(--mn); font-weight:700; }}
  .gn-dot{{ width:12px; height:12px; border-radius:50%; display:inline-block; }}
  .gn-empty{{ padding:22px; text-align:center; color:var(--tx); font-family:var(--mn); font-size:15px; }}
  .rail{{ display:flex; flex-direction:column; gap:10px; }}
  .rail-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px 18px; }}
  .rail-h{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1.5px; text-transform:uppercase;
    color:var(--hdr); display:flex; align-items:center; gap:10px; margin-bottom:6px; }}
  .rail-h .sic{{ font-size:22px; }}
  .rail-row{{ display:flex; justify-content:space-between; align-items:center; gap:10px; min-height:34px;
    font-family:var(--mn); font-size:15px; border-bottom:1px solid rgba(26,32,48,.35); }}
  .rail-row:last-child{{ border-bottom:none; }}
  .rail-k{{ color:var(--tx); }}
  .rail-v{{ font-weight:700; color:var(--br); text-align:right; white-space:nowrap; }}
  @media(max-width:900px){{ .feed-wrap{{ grid-template-columns:1fr; }} }}

  /* Analytics Lab */
  .lab3{{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-bottom:10px; }}
  .labp{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:14px 16px; }}
  .labt{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--hdr); margin-bottom:8px; display:flex; align-items:center; gap:8px; }}
  .bstat{{ display:flex; justify-content:space-between; align-items:center; min-height:33px; font-family:var(--mn); font-size:15px; border-bottom:1px solid rgba(26,32,48,.35); }}
  .bstat:last-child{{ border-bottom:none; }}
  .bk{{ color:var(--tx); }}
  .bv{{ font-weight:700; color:var(--br); text-align:right; }}
  @media(max-width:900px){{ .lab3{{ grid-template-columns:1fr; }} }}

  /* XRP Complete Leaderboard */
  .lb-grid{{ display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }}
  .lb-panel{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:14px 16px; }}
  .lb-t{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1.5px; margin-bottom:10px; text-transform:uppercase; }}
  .lb-row{{ display:flex; align-items:center; gap:12px; padding:7px 0; font-family:var(--mn); font-size:15px; border-bottom:1px solid rgba(26,32,48,.35); }}
  .lb-row:last-child{{ border-bottom:none; }}
  .lb-rank{{ color:var(--hdr); font-weight:900; width:18px; text-align:center; }}
  .lb-name{{ color:var(--br); flex:1; }}
  .lb-cnt{{ color:var(--tx); font-weight:700; }}
  .lb-empty{{ color:var(--tx); font-family:var(--mn); font-size:15px; padding:6px 0; }}
  .lb-score{{ text-align:center; padding:6px 0 10px; }}
  .lb-score-num{{ font-size:46px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .lb-score-cap{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:4px; }}
  .lb-score-lbl{{ font-size:15px; font-weight:800; font-family:var(--mn); margin-top:6px; letter-spacing:1px; }}
  .lb-mini{{ border-top:1px solid var(--b); padding-top:8px; margin-top:4px; }}
  .lb-mini-row{{ display:flex; justify-content:space-between; font-size:15px; font-family:var(--mn); padding:3px 0; }}
  .lb-mini-row span:first-child{{ color:var(--tx); }}
  @media(max-width:900px){{ .lb-grid{{ grid-template-columns:1fr; }} }}

  /* XRP Intelligence Brief */
  .brf-head{{ display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:14px; }}
  .brf-sub{{ font-size:15px; color:var(--or); font-family:var(--mn); margin-top:3px; }}
  .brf-meta{{ text-align:right; font-family:var(--mn); }}
  .brf-badge{{ display:inline-block; font-size:15px; font-weight:800; letter-spacing:1px; padding:3px 12px; border-radius:5px;
    background:rgba(255,153,0,.12); color:var(--or); border:1px solid rgba(255,153,0,.45); }}
  .brf-when{{ font-size:15px; color:var(--br); font-family:var(--mn); margin-top:6px; font-weight:600; }}
  .brf-now-showing{{ font-size:15px; color:var(--hdr); font-family:var(--mn); font-weight:800; letter-spacing:0.5px;
    margin-bottom:8px; padding-bottom:8px; border-bottom:1px solid var(--b); display:flex; align-items:center;
    flex-wrap:wrap; gap:10px; }}
  .brf-now-spacer{{ color:var(--tx); font-weight:400; }}
  #brf-next-line{{ font-size:15px; color:var(--tx); font-weight:600; text-transform:none; letter-spacing:normal; }}
  .brf-ribbon-wrap{{ display:inline-flex; align-items:center; gap:6px; margin-right:4px; }}
  .brf-ribbon-icon{{ font-size:17px; }}
  .brf-ribbon{{ background:var(--or); color:#ffffff; font-family:var(--mn); font-weight:900; font-size:15px;
    letter-spacing:0.5px; padding:5px 16px 5px 12px; position:relative;
    clip-path:polygon(0 0, calc(100% - 8px) 0, 100% 50%, calc(100% - 8px) 100%, 0 100%); }}
  .brf-intro-line{{ font-size:15px; color:var(--tx); font-family:var(--mn); margin-bottom:10px; font-style:italic; }}
  .brf-grid{{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
  .brf-block{{ background:rgba(117,188,255,.07); border:1px solid rgba(117,188,255,.25); border-radius:8px; padding:16px 18px; border-left:3px solid var(--or); min-height:140px; }}
  .brf-t{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1px; color:var(--hdr); text-transform:uppercase; margin-bottom:6px; display:flex; align-items:center; gap:8px; }}
  .brf-x{{ font-size:15px; color:var(--br); line-height:1.75; font-family:system-ui; }}
  .brf-note{{ font-size:12px; color:var(--tx); font-family:var(--mn); opacity:.7; margin-top:12px; }}
  @media(max-width:900px){{ .brf-grid{{ grid-template-columns:1fr; }} }}

  /* Brief Home — designated schedule strip */
  .brf-home{{ background:var(--s2); border:1px solid rgba(255,153,0,.3); border-radius:8px; padding:12px 14px; margin-bottom:14px; }}
  .brf-home-t{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1px; color:var(--or); text-transform:uppercase; margin-bottom:3px; display:flex; align-items:center; gap:8px; }}
  .brf-home-sub{{ font-size:15px; color:var(--br); font-family:var(--mn); margin-bottom:10px; font-weight:600; }}
  .brf-strip{{ display:flex; flex-wrap:wrap; gap:6px; }}
  .brf-slot{{ flex:1 1 60px; min-width:58px; text-align:center; padding:7px 4px; border-radius:6px; font-family:var(--mn);
    border:1px solid var(--b); background:var(--s1); cursor:default; display:block; text-decoration:none; }}
  .brf-slot-day{{ font-size:12px; color:var(--tx); }}
  .brf-slot-ed{{ font-size:15px; font-weight:800; margin-top:2px; }}
  .brf-slot.ready{{ cursor:pointer; border:2px solid var(--tq); background:rgba(0,229,204,.16); box-shadow:0 0 6px rgba(0,229,204,.25); }}
  .brf-slot.ready:hover{{ border-color:var(--tq); background:rgba(0,229,204,.28); box-shadow:0 0 10px rgba(0,229,204,.4); transform:translateY(-1px); }}
  .brf-slot.ready .brf-slot-ed{{ color:var(--tq); font-weight:900; }}
  .brf-slot.ready .brf-slot-day{{ color:var(--br); font-weight:700; }}
  .brf-slot.live{{ border-color:var(--or); background:rgba(255,153,0,.14); box-shadow:0 0 0 1px var(--or) inset; }}
  .brf-slot.live .brf-slot-ed{{ color:var(--or); }}
  .brf-slot.pending{{ opacity:.45; cursor:pointer; }}
  .brf-pending-msg{{ margin-top:8px; padding:8px 12px; background:rgba(255,153,0,.1); border:1px solid rgba(255,153,0,.35);
    border-radius:6px; font-size:12px; font-family:var(--mn); color:var(--or); }}
  .brf-slot.pending .brf-slot-ed{{ color:var(--tx); }}
  .brf-slot.active-view{{ outline:2px solid var(--br); outline-offset:1px; }}

  /* Next Briefing countdown teaser — same footprint as Brief Home, white fill */
  .brf-teaser{{ background:#3d7fc4; border:2px solid #2a5f96; border-radius:8px; padding:10px 14px; margin-bottom:14px; text-align:center; }}
  .brf-teaser-line{{ font-size:15px; font-weight:900; font-family:var(--mn); color:#ffffff; }}
  .brf-teaser-line span{{ color:var(--or); font-weight:900; }}
  .brf-teaser-sub{{ font-size:15px; font-family:var(--mn); color:#dcebfa; margin-top:4px; font-weight:600; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}

  /* World briefing clocks */
  .wc-row{{ display:flex; flex-wrap:wrap; gap:8px; justify-content:space-between; margin:14px 0; padding:12px;
    background:var(--s2); border:1px solid var(--b); border-radius:10px; }}
  .wc{{ flex:1 1 92px; min-width:84px; text-align:center; font-family:var(--mn); }}
  .wc-city{{ font-size:12px; font-weight:700; color:var(--br); margin-bottom:6px; white-space:nowrap; }}
  .wc-clock{{ position:relative; width:54px; height:54px; border-radius:50%; margin:0 auto 6px; border:2px solid #4a5878;
    background:radial-gradient(circle,rgba(128,153,179,.16),rgba(128,153,179,.04)); }}
  .wc-clock.wc-day{{ border-color:var(--or); background:radial-gradient(circle,rgba(255,153,0,.28),rgba(255,153,0,.07)); }}
  .wc-hand{{ position:absolute; left:50%; bottom:50%; transform-origin:bottom center; transform:rotate(0deg); background:var(--br); border-radius:2px; }}
  .wc-hr{{ width:3px; height:14px; margin-left:-1.5px; }}
  .wc-min{{ width:2px; height:20px; margin-left:-1px; }}
  .wc-sec{{ width:1px; height:21px; margin-left:-.5px; background:var(--rd); }}
  .wc-clock.wc-day .wc-hr, .wc-clock.wc-day .wc-min{{ background:#3a2200; }}
  .wc-center{{ position:absolute; left:50%; top:50%; width:5px; height:5px; border-radius:50%; background:var(--rd); transform:translate(-50%,-50%); }}
  .wc-off{{ font-size:12px; font-weight:700; color:var(--hdr); margin-bottom:2px; }}
  .wc-b{{ font-size:12px; color:var(--tx); line-height:1.5; white-space:nowrap; }}

  /* Unique Displays: Smart Money Score + F&G history */
  .ud-grid{{ display:grid; grid-template-columns:1fr 2fr; gap:12px; }}
  .ud-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .sm-score{{ font-size:52px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .sm-cap{{ font-size:15px; color:var(--tx); font-family:var(--mn); }}
  .sm-label{{ font-size:17px; font-weight:800; font-family:var(--mn); margin:8px 0; }}
  .sm-bar{{ height:8px; background:var(--s2); border:1px solid var(--b); border-radius:4px; overflow:hidden; margin-bottom:14px; }}
  .sm-fill{{ height:100%; background:linear-gradient(90deg,var(--rd),var(--yl),var(--gr)); }}
  .sm-row{{ display:flex; justify-content:space-between; align-items:center; min-height:31px; font-family:var(--mn); font-size:15px; border-bottom:1px solid rgba(26,32,48,.35); }}
  .sm-row:last-child{{ border-bottom:none; }}
  .sm-k{{ color:var(--tx); }}
  .sm-v{{ color:var(--br); font-weight:700; }}
  .fg-title{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1px; color:var(--hdr); margin-bottom:12px; display:flex; align-items:center; gap:8px; }}
  .fg-chart{{ display:flex; align-items:flex-end; gap:3px; height:130px; padding:6px 0; }}
  .fg-bar{{ flex:1; min-width:4px; border-radius:2px 2px 0 0; }}
  .fg-bar.fg-today{{ outline:2px solid var(--br); outline-offset:1px; }}
  .fg-axis{{ display:flex; justify-content:space-between; font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:4px; }}
  .fg-legend{{ display:flex; flex-wrap:wrap; gap:12px; margin-top:10px; font-size:12px; font-family:var(--mn); color:var(--tx); }}
  .fg-key{{ display:inline-block; width:10px; height:10px; border-radius:2px; margin-right:5px; vertical-align:middle; }}
  @media(max-width:900px){{ .ud-grid{{ grid-template-columns:1fr; }} }}

  /* Longitudinal Value Markers */
  .lvm-grid{{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }}
  .lvm-card{{ background:var(--s2); border:1px solid var(--b); border-radius:10px; padding:16px; text-align:center; }}
  .lvm-win{{ font-size:15px; color:var(--tx); font-family:var(--mn); text-transform:uppercase; letter-spacing:1px; margin-bottom:8px; }}
  .lvm-val{{ font-size:22px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .lvm-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:6px; }}
  @media(max-width:900px){{ .lvm-grid{{ grid-template-columns:repeat(2,1fr); }} }}

  /* Regional News Activity Heatmap */
  .rh-grid{{ display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }}
  .rh-card{{ border:1px solid var(--b); border-radius:10px; padding:16px 12px; text-align:center; }}
  .rh-flag{{ font-size:22px; line-height:1; }}
  .rh-name{{ font-size:15px; font-weight:800; color:var(--br); font-family:var(--mn); margin:6px 0; }}
  .rh-num{{ font-size:22px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .rh-lbl{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:5px; }}
  @media(max-width:900px){{ .rh-grid{{ grid-template-columns:repeat(2,1fr); }} }}

  /* Sentiment Engine */
  .sent-top{{ display:grid; grid-template-columns:200px 1fr; gap:10px; margin-bottom:14px; }}
  .vel-chart{{ display:flex; align-items:flex-end; gap:2px; height:60px; margin-top:8px; }}
  .vel-bar{{ flex:1; min-width:2px; background:var(--yl); border-radius:1px 1px 0 0; opacity:.85; }}
  .sdt-chart{{ display:flex; align-items:flex-end; gap:2px; height:80px; }}
  .sdt-bar{{ flex:1; min-width:3px; border-radius:2px 2px 0 0; }}
  .sent-bar-mini{{ display:flex; height:8px; border-radius:4px; overflow:hidden; width:80px; background:var(--s2); }}
  @media(max-width:900px){{ .sent-top{{ grid-template-columns:1fr; }} }}

  /* Competitive Briefing */
  .odl-item, .iso-item{{ background:var(--s2); border:1px solid var(--b); border-radius:6px; padding:9px 12px;
    margin-bottom:6px; font-family:var(--mn); font-size:15px; display:flex; align-items:center; gap:10px; flex-wrap:wrap; }}
  .odl-route{{ font-weight:700; color:var(--br); white-space:nowrap; }}
  .odl-status{{ font-size:12px; font-weight:800; padding:2px 8px; border-radius:4px; letter-spacing:.5px; white-space:nowrap; }}
  .odl-status.active{{ background:rgba(72,255,130,.15); color:var(--gr); }}
  .odl-status.growing{{ background:rgba(255,204,0,.15); color:var(--yl); }}
  .odl-status.live{{ background:rgba(0,229,204,.15); color:var(--tq); }}
  .odl-note{{ color:var(--tx); font-size:12px; flex:1; min-width:140px; }}
  .sw-grid{{ display:grid; grid-template-columns:repeat(5,1fr); gap:8px; }}
  @media(max-width:900px){{ .sw-grid{{ grid-template-columns:repeat(2,1fr); }} }}

  /* Ripple Executive Tracker + XRPL Dev Activity */
  .ed-grid{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
  .ed-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; overflow:hidden; }}
  .ed-head{{ padding:10px 14px; background:var(--s2); border-bottom:1px solid var(--b); display:flex; justify-content:space-between; align-items:center; }}
  .ed-title{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1px; }}
  .ex-tabs{{ display:flex; gap:0; border-bottom:1px solid var(--b); overflow-x:auto; }}
  .ex-tab{{ padding:7px 14px; background:transparent; border:none; color:var(--tx); font-family:var(--mn);
    font-size:12px; font-weight:700; cursor:pointer; text-transform:uppercase; letter-spacing:1px; white-space:nowrap;
    border-bottom:2px solid transparent; }}
  .ex-tab.on{{ color:var(--or); border-bottom-color:var(--or); }}
  .ex-feed{{ max-height:340px; overflow-y:auto; padding:8px 12px; }}
  .ex-row{{ padding:9px 0; border-bottom:1px solid rgba(26,32,48,.4); }}
  .ex-row:last-child{{ border-bottom:none; }}
  .ex-top{{ display:flex; align-items:center; gap:8px; margin-bottom:4px; flex-wrap:wrap; }}
  .ex-name{{ font-size:15px; font-weight:800; color:var(--or); font-family:var(--mn); }}
  .ex-title{{ font-size:12px; color:var(--tx); font-family:var(--mn); }}
  .ex-time{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-left:auto; }}
  .ex-hl{{ display:block; font-size:15px; color:var(--br); text-decoration:none; line-height:1.5; font-family:system-ui; }}
  .ex-hl:hover{{ color:var(--hdr); text-decoration:underline; }}
  .gh-stats{{ display:grid; grid-template-columns:repeat(4,1fr); border-bottom:1px solid var(--b); background:var(--s2); }}
  .gh-stat{{ padding:9px 6px; text-align:center; border-right:1px solid var(--b); }}
  .gh-stat:last-child{{ border-right:none; }}
  .gh-stat-num{{ font-size:17px; font-weight:900; font-family:var(--mn); }}
  .gh-stat-lbl{{ font-size:12px; color:var(--tx); font-family:var(--mn); text-transform:uppercase; letter-spacing:.5px; line-height:1.4; margin-top:2px; }}
  .gh-latest{{ padding:9px 12px; border-bottom:1px solid var(--b); background:rgba(72,255,130,.04); }}
  .gh-latest-lbl{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-bottom:2px; }}
  .gh-latest-msg{{ font-size:15px; font-weight:700; color:var(--gr); font-family:system-ui; }}
  .gh-latest-meta{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:2px; }}
  .gh-feed{{ max-height:220px; overflow-y:auto; padding:8px 12px; }}
  .gh-row{{ padding:8px 0; border-bottom:1px solid rgba(26,32,48,.4); font-family:var(--mn); font-size:12px; }}
  .gh-row:last-child{{ border-bottom:none; }}
  .gh-repo{{ display:inline-block; color:var(--tq); font-weight:700; margin-right:6px; }}
  .gh-msg{{ color:var(--br); text-decoration:none; }}
  .gh-msg:hover{{ color:var(--hdr); text-decoration:underline; }}
  .gh-meta{{ display:block; color:var(--tx); margin-top:2px; }}
  @media(max-width:900px){{ .ed-grid{{ grid-template-columns:1fr; }} }}

  /* Regulatory Radar */
  .cg-grid{{ display:grid; grid-template-columns:repeat(5,1fr); gap:8px; }}
  .cg-card{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:10px; }}
  .cg-top{{ display:flex; align-items:center; gap:6px; margin-bottom:6px; }}
  .cg-flag{{ font-size:17px; }}
  .cg-name{{ font-size:12px; font-weight:700; color:var(--br); font-family:var(--mn); }}
  .cg-note{{ font-size:12px; color:var(--tx); line-height:1.5; font-family:system-ui; margin-top:6px; }}
  .mica-row{{ display:flex; align-items:center; gap:12px; padding:9px 4px; border-bottom:1px solid rgba(26,32,48,.4); font-family:var(--mn); }}
  .mica-row:last-child{{ border-bottom:none; }}
  .mica-icon{{ font-size:15px; flex:0 0 18px; text-align:center; }}
  .mica-date{{ font-size:12px; color:var(--tx); flex:0 0 78px; }}
  .mica-event{{ font-size:15px; font-weight:700; flex:0 0 190px; }}
  .mica-detail{{ font-size:12px; color:var(--tx); flex:1; font-family:system-ui; line-height:1.5; }}
  @media(max-width:700px){{ .mica-row{{ flex-wrap:wrap; }} .mica-event{{ flex-basis:100%; order:1; }} .mica-detail{{ flex-basis:100%; order:2; }} }}
  @media(max-width:900px){{ .cg-grid{{ grid-template-columns:repeat(2,1fr); }} }}

  /* Static Global Partnership Directory (right rail, V90) */
  .sd-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:14px; display:flex; flex-direction:column; }}
  .sd-head{{ display:flex; justify-content:space-between; align-items:center; margin-bottom:4px; }}
  .sd-title{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--hdr); letter-spacing:0.5px; }}
  .sd-count{{ font-size:15px; font-weight:900; font-family:var(--mn); color:var(--yl); }}
  .sd-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); line-height:1.5; margin-bottom:10px; }}
  .sd-list{{ display:flex; flex-direction:column; gap:6px; flex:1 1 auto; min-height:0; max-height:820px; overflow-y:scroll; padding-right:6px;
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2); }}
  .sd-list::-webkit-scrollbar{{ width:8px; }}
  .sd-list::-webkit-scrollbar-track{{ background:var(--s2); border-radius:6px; }}
  .sd-list::-webkit-scrollbar-thumb{{ background:#33405e; border-radius:6px; }}
  .sd-item{{ background:var(--s2); border:1px solid var(--b); border-radius:6px; padding:8px 10px; display:flex; flex-direction:column; gap:3px; }}
  .sd-item-top{{ display:flex; align-items:center; gap:7px; }}
  .sd-flag{{ font-size:15px; line-height:1; flex-shrink:0; }}
  .sd-name{{ font-size:15px; font-weight:700; color:var(--br); }}
  .sd-cat{{ font-size:12px; font-weight:700; font-family:var(--mn); color:var(--tq); letter-spacing:0.3px; }}
  .sd-desc{{ font-size:12px; color:var(--tx); line-height:1.4; }}
  .sd-empty{{ font-size:12px; color:var(--tx); font-style:italic; padding:10px 0; }}

  /* Global XRP Enterprise & Partnership Ledger */
  .pl-search{{ width:100%; box-sizing:border-box; background:#e9ecf1; border:1px solid #c3c8d1; border-radius:8px;
    color:#1a2a4a; font-family:var(--mn); font-size:15px; padding:11px 14px; margin-bottom:10px; }}
  .pl-search::placeholder{{ color:#6b7280; }}
  .pl-cats{{ display:flex; flex-wrap:wrap; gap:8px; margin-bottom:10px; }}
  .pl-btn{{ padding:6px 13px; border-radius:6px; font-size:12px; font-weight:700; font-family:var(--mn); letter-spacing:.5px;
    border:1px solid var(--b); background:transparent; color:var(--tx); cursor:pointer; opacity:.75; }}
  .pl-btn:hover{{ opacity:1; }}
  .pl-btn.active{{ opacity:1; box-shadow:0 0 0 1px currentColor inset; }}
  .pl-stats{{ font-size:15px; font-family:var(--mn); color:var(--tx); margin-bottom:10px; }}
  .pl-stats b{{ color:var(--yl); }}
  .pl-list{{ display:flex; flex-direction:column; gap:7px; max-height:600px; overflow-y:scroll; padding-right:6px;
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2); }}
  .pl-list::-webkit-scrollbar{{ width:8px; }}
  .pl-list::-webkit-scrollbar-track{{ background:var(--s2); border-radius:6px; }}
  .pl-list::-webkit-scrollbar-thumb{{ background:#33405e; border-radius:6px; }}
  .pl-row{{ background:var(--s1); border:1px solid var(--b); border-radius:8px; padding:10px 14px; }}
  .pl-top{{ display:flex; align-items:center; gap:8px; margin-bottom:4px; flex-wrap:wrap; }}
  .pl-cat{{ font-size:12px; font-weight:800; font-family:var(--mn); letter-spacing:.5px; }}
  .pl-new{{ font-size:12px; font-weight:900; font-family:var(--mn); color:var(--bg); background:var(--yl);
    padding:1px 6px; border-radius:4px; letter-spacing:.5px; }}
  .pl-status{{ font-size:12px; font-weight:700; font-family:var(--mn); }}
  .pl-when{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-left:auto; }}
  .pl-name{{ font-size:15px; font-weight:700; color:var(--br); font-family:system-ui; margin-bottom:2px; }}
  .pl-name a{{ color:var(--hdr); text-decoration:none; }}
  .pl-name a:hover{{ text-decoration:underline; }}
  .pl-meta{{ font-size:12px; color:var(--tx); line-height:1.5; font-family:system-ui; }}
  .pl-counter{{ font-size:22px; font-weight:900; font-family:var(--mn); color:var(--yl); }}

  /* Advanced Metrics */
  .am-grid2{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
  .am-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .am-title{{ font-size:15px; font-weight:800; font-family:var(--mn); margin-bottom:4px; display:flex; align-items:center; gap:8px; }}
  .am-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-bottom:12px; }}
  .uc-list{{ display:flex; flex-direction:column; gap:6px; max-height:340px; overflow-y:auto; }}
  .uc-card{{ padding:9px 11px; background:var(--s2); border-radius:6px; border-left:3px solid; }}
  .uc-title{{ font-size:15px; font-weight:700; font-family:var(--mn); margin-bottom:2px; }}
  .uc-detail{{ font-size:12px; color:var(--tx); line-height:1.5; font-family:system-ui; }}
  .abox{{ padding:10px; background:var(--s2); border-radius:6px; border-left:3px solid var(--b); }}
  .abox-lbl{{ font-size:12px; color:var(--tx); font-family:var(--mn); text-transform:uppercase; letter-spacing:.5px; }}
  .abox-val{{ font-size:17px; font-weight:800; font-family:var(--mn); margin-top:4px; }}
  .corr-row{{ display:flex; justify-content:space-between; align-items:center; padding:9px 12px; background:var(--s2);
    border-radius:6px; border:1px solid var(--b); font-family:var(--mn); font-size:15px; font-weight:700; margin-bottom:8px; color:var(--br); }}
  .ob-row{{ display:grid; grid-template-columns:70px 1fr 60px; align-items:center; gap:8px; font-family:var(--mn); font-size:12px; padding:2px 0; }}
  .ob-price.gr{{ color:var(--gr); }}
  .ob-price.rd{{ color:var(--rd); }}
  .ob-bar-wrap{{ height:8px; background:var(--s2); border-radius:2px; overflow:hidden; }}
  .ob-bar{{ height:100%; }}
  .ob-bar.gr{{ background:rgba(72,255,130,.5); }}
  .ob-bar.rd{{ background:rgba(255,64,96,.5); }}
  .ob-qty{{ color:var(--tx); text-align:right; }}
  .liq-bar{{ height:22px; border-radius:6px; overflow:hidden; background:rgba(255,64,96,.35); margin-bottom:6px; }}
  .liq-fill{{ height:100%; background:rgba(72,255,130,.55); }}
  .liq-labels{{ display:flex; justify-content:space-between; font-size:15px; font-family:var(--mn); font-weight:700; margin-bottom:6px; }}
  .liq-skew{{ font-size:15px; font-weight:800; color:var(--br); font-family:var(--mn); margin-bottom:4px; }}
  .liq-note{{ font-size:12px; color:var(--tx); font-family:var(--mn); }}
  @media(max-width:900px){{ .am-grid2{{ grid-template-columns:1fr; }} }}

  /* CLARITY Act Tracker */
  .ca-list{{ display:flex; flex-direction:column; gap:7px; max-height:520px; overflow-y:auto; }}

  /* Visible thin scrollbars, applied consistently to every scrollable container on the site */
  .whale-feed, .ex-feed, .gh-feed, .uc-list, .ca-list {{
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2);
  }}
  .whale-feed::-webkit-scrollbar, .ex-feed::-webkit-scrollbar, .gh-feed::-webkit-scrollbar,
  .uc-list::-webkit-scrollbar, .ca-list::-webkit-scrollbar {{ width:8px; }}
  .whale-feed::-webkit-scrollbar-track, .ex-feed::-webkit-scrollbar-track, .gh-feed::-webkit-scrollbar-track,
  .uc-list::-webkit-scrollbar-track, .ca-list::-webkit-scrollbar-track {{ background:var(--s2); border-radius:6px; }}
  .whale-feed::-webkit-scrollbar-thumb, .ex-feed::-webkit-scrollbar-thumb, .gh-feed::-webkit-scrollbar-thumb,
  .uc-list::-webkit-scrollbar-thumb, .ca-list::-webkit-scrollbar-thumb {{ background:#33405e; border-radius:6px; }}

  .flow, .ex-tabs, .cc-panel, .tbl-scroll {{
    scrollbar-width:thin; scrollbar-color:#33405e var(--s2); overflow-x:auto;
  }}
  .flow::-webkit-scrollbar, .ex-tabs::-webkit-scrollbar, .cc-panel::-webkit-scrollbar, .tbl-scroll::-webkit-scrollbar {{ height:8px; }}
  .flow::-webkit-scrollbar-track, .ex-tabs::-webkit-scrollbar-track, .cc-panel::-webkit-scrollbar-track, .tbl-scroll::-webkit-scrollbar-track {{ background:var(--s2); border-radius:6px; }}
  .flow::-webkit-scrollbar-thumb, .ex-tabs::-webkit-scrollbar-thumb, .cc-panel::-webkit-scrollbar-thumb, .tbl-scroll::-webkit-scrollbar-thumb {{ background:#33405e; border-radius:6px; }}
  .ca-row{{ display:flex; align-items:flex-start; gap:12px; background:var(--s1); border:1px solid var(--b);
    border-radius:8px; padding:10px 14px; }}
  .ca-rank{{ flex:0 0 26px; text-align:center; font-size:15px; font-weight:900; font-family:var(--mn); color:var(--yl); padding-top:2px; }}
  .ca-body{{ flex:1; min-width:0; }}
  .ca-top{{ display:flex; align-items:center; gap:8px; margin-bottom:3px; flex-wrap:wrap; }}
  .ca-src{{ font-size:12px; font-weight:700; color:var(--tq); font-family:var(--mn); }}
  .ca-time{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-left:auto; }}
  .ca-hl{{ font-size:15px; font-weight:700; color:var(--br); text-decoration:none; line-height:1.4; font-family:system-ui; }}
  .ca-hl:hover{{ color:var(--hdr); text-decoration:underline; }}

  /* Flagship: Institutional Confidence Index */
  .flagship-intro{{ font-size:15px; color:var(--tx); line-height:1.7; font-family:system-ui; margin-bottom:16px; max-width:920px; }}
  .flagship-list{{ margin:10px 0; padding-left:20px; }}
  .flagship-list li{{ margin-bottom:4px; }}
  .ici-wrap{{ display:grid; grid-template-columns:220px 1fr; gap:20px; background:linear-gradient(135deg,#0a0a14,#0d0d1a);
    border:1px solid rgba(255,204,0,.25); border-radius:14px; padding:22px; }}
  .ici-dial{{ display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; }}
  .ici-score{{ font-size:64px; font-weight:900; font-family:var(--mn); line-height:1; }}
  .ici-cap{{ font-size:15px; color:var(--tx); font-family:var(--mn); margin-top:2px; }}
  .ici-label{{ font-size:15px; font-weight:800; font-family:var(--mn); margin-top:8px; letter-spacing:.5px; }}
  .ici-bar{{ width:100%; height:8px; background:var(--s2); border-radius:4px; overflow:hidden; margin-top:12px; }}
  .ici-fill{{ height:100%; background:linear-gradient(90deg,var(--rd),var(--or),var(--yl),var(--gr)); }}
  .ici-comps{{ display:flex; flex-direction:column; gap:8px; justify-content:center; }}
  .ici-comp-row{{ display:grid; grid-template-columns:170px 1fr 44px; align-items:center; gap:10px; }}
  .ici-comp-name{{ font-size:12px; font-weight:700; color:var(--br); font-family:var(--mn); }}
  .ici-comp-track{{ height:7px; background:var(--s2); border-radius:4px; overflow:hidden; position:relative; }}
  .ici-comp-fill{{ height:100%; background:var(--tq); border-radius:4px; }}
  .ici-comp-detail{{ font-size:12px; color:var(--tx); font-family:var(--mn); grid-column:1/3; margin-top:-4px; }}
  .ici-comp-pts{{ font-size:12px; font-weight:800; color:var(--yl); font-family:var(--mn); text-align:right; }}
  .ici-foot{{ margin-top:16px; padding-top:14px; border-top:1px solid rgba(255,255,255,.08); font-size:12px;
    color:var(--tx); font-family:var(--mn); line-height:1.6; }}
  @media(max-width:900px){{ .ici-wrap{{ grid-template-columns:1fr; }} }}

  /* Partnership Momentum Chart */
  .pm-panel{{ margin-top:16px; background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .pm-title{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--yl); margin-bottom:4px; display:flex; align-items:center; gap:8px; }}
  .pm-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-bottom:12px; }}
  .pm-stats{{ display:flex; gap:18px; flex-wrap:wrap; margin-bottom:12px; }}
  .pm-stat-num{{ font-size:22px; font-weight:900; font-family:var(--mn); }}
  .pm-stat-lbl{{ font-size:12px; color:var(--tx); font-family:var(--mn); text-transform:uppercase; letter-spacing:.5px; }}
  .pm-chart{{ display:flex; align-items:flex-end; gap:5px; height:70px; }}
  .pm-bar{{ flex:1; min-width:8px; background:var(--yl); border-radius:2px 2px 0 0; opacity:.85; }}
  .pm-axis{{ display:flex; justify-content:space-between; font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:4px; }}

  /* Catalyst Clock */
  .cc-panel{{ margin-top:16px; background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; overflow-x:auto; }}
  .cc-title{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--or); margin-bottom:4px; display:flex; align-items:center; gap:8px; }}
  .cc-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-bottom:12px; }}
  .cc-peak{{ font-size:15px; font-family:var(--mn); color:var(--br); margin-bottom:12px; }}
  .cc-peak b{{ color:var(--or); }}
  .cc-grid{{ min-width:640px; }}
  .cc-row{{ display:flex; align-items:center; gap:2px; margin-bottom:2px; }}
  .cc-daylbl{{ flex:0 0 30px; font-size:12px; color:var(--tx); font-family:var(--mn); }}
  .cc-cell{{ flex:1; height:14px; border-radius:2px; min-width:8px; }}
  .cc-hourlbls{{ display:flex; gap:2px; margin-top:2px; margin-left:32px; min-width:608px; }}
  .cc-hourlbl{{ flex:1; font-size:12px; color:var(--tx); font-family:var(--mn); text-align:center; min-width:8px; }}
  .cc-scrollnote{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-top:8px; }}

  /* Narrative Diffusion Map */
  .nd-panel{{ margin-top:16px; background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .nd-title{{ font-size:15px; font-weight:800; font-family:var(--mn); color:var(--tq); margin-bottom:4px; display:flex; align-items:center; gap:8px; }}
  .nd-sub{{ font-size:12px; color:var(--tx); font-family:var(--mn); margin-bottom:8px; }}
  .nd-fastest{{ font-size:15px; font-family:var(--mn); color:var(--br); margin-bottom:12px; }}
  .nd-fastest b{{ color:var(--tq); }}
  .nd-list{{ display:flex; flex-direction:column; gap:8px; }}
  .nd-card{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:10px 14px; }}
  .nd-top{{ display:flex; justify-content:space-between; align-items:center; margin-bottom:6px; flex-wrap:wrap; gap:6px; }}
  .nd-theme{{ font-size:15px; font-weight:800; color:var(--br); font-family:var(--mn); }}
  .nd-age{{ font-size:12px; color:var(--tx); font-family:var(--mn); }}
  .nd-chips{{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom:6px; }}
  .nd-chip{{ font-size:12px; font-family:var(--mn); background:var(--s1); border:1px solid var(--b); border-radius:12px;
    padding:3px 10px; color:var(--br); }}
  .nd-lag{{ color:var(--tq); font-weight:700; margin-left:3px; }}
  .nd-note{{ font-size:12px; color:var(--tx); font-family:var(--mn); }}

  /* Practical Tools */
  .pt-cols{{ display:grid; grid-template-columns:1fr 1fr; gap:10px; align-items:start; }}
  .pt-col{{ display:flex; flex-direction:column; gap:10px; }}
  .pt-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; overflow:hidden; }}
  .pt-head{{ padding:10px 14px; background:var(--s2); border-bottom:1px solid var(--b); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px; }}
  .pt-title{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1.2px; }}
  .pt-body{{ padding:14px; display:flex; flex-direction:column; gap:10px; }}
  .pt-lbl{{ font-size:12px; font-family:var(--mn); color:var(--tx); text-transform:uppercase; letter-spacing:1px; margin-bottom:4px; }}
  .pt-row2{{ display:grid; grid-template-columns:1fr 1fr; gap:8px; }}
  .pt-input, .pt-select{{ width:100%; box-sizing:border-box; background:var(--s2); border:1px solid var(--b); color:var(--br);
    padding:8px 10px; border-radius:5px; font-size:15px; font-family:var(--mn); outline:none; }}
  .pt-input::placeholder{{ color:var(--tx); }}
  .pt-use-live{{ color:var(--tq); cursor:pointer; margin-left:6px; font-size:12px; }}
  .pt-results{{ background:var(--s2); border:1px solid var(--b); border-radius:6px; padding:10px; font-family:var(--mn); font-size:15px; display:none; }}
  .pt-res-row{{ display:flex; justify-content:space-between; padding:4px 0; border-bottom:1px solid rgba(255,255,255,.05); }}
  .pt-res-row:last-child{{ border-bottom:none; }}
  .pt-note{{ font-size:12px; font-family:var(--mn); color:var(--tx); }}
  .pt-btn{{ background:rgba(117,188,255,.1); border:1px solid var(--bl); color:var(--bl); padding:8px 14px; border-radius:5px;
    cursor:pointer; font-family:var(--mn); font-size:15px; font-weight:700; text-transform:uppercase; white-space:nowrap; }}
  .pt-btn:hover{{ background:var(--bl); color:#000; }}
  .pt-btn-gr{{ background:rgba(72,255,130,.1); border:1px solid var(--gr); color:var(--gr); padding:6px 10px; border-radius:4px;
    cursor:pointer; font-family:var(--mn); font-size:15px; font-weight:700; }}
  .pt-btn-gr:hover{{ background:var(--gr); color:#000; }}
  .fx-grid{{ display:grid; grid-template-columns:repeat(3,1fr); gap:6px; padding:12px; }}
  .fx-box{{ background:var(--s2); border:1px solid var(--b); border-radius:6px; padding:8px; text-align:center; }}
  .fx-box.hi{{ border-color:var(--bl); }}
  .fx-lbl{{ font-size:12px; font-family:var(--mn); color:var(--tx); text-transform:uppercase; letter-spacing:1px; }}
  .fx-val{{ font-size:17px; font-weight:900; font-family:var(--mn); margin-top:4px; color:var(--br); }}
  .pt-tbl{{ width:100%; border-collapse:collapse; font-family:var(--mn); font-size:15px; margin-bottom:6px; }}
  .pt-tbl th{{ padding:4px 6px; text-align:right; color:var(--tx); font-size:12px; border-bottom:1px solid var(--b); }}
  .pt-tbl th:first-child{{ text-align:left; }}
  .pt-tbl td{{ padding:5px 6px; text-align:right; border-bottom:1px solid rgba(255,255,255,.03); }}
  .pt-tbl td:first-child{{ text-align:left; color:var(--br); font-weight:700; }}
  .pt-x{{ cursor:pointer; color:var(--rd); font-weight:900; }}
  .rm-fee-box{{ border-radius:6px; padding:10px; text-align:center; }}
  @media(max-width:900px){{ .pt-cols{{ grid-template-columns:1fr; }} .fx-grid{{ grid-template-columns:repeat(3,1fr); }} }}

  /* MAIN */
  main{{ max-width:1180px; margin:0 auto; padding:14px 28px 90px; min-height:46vh; }}
 
  .subtitle{{ color:var(--tx); font-size:15px; font-family:var(--mn); letter-spacing:1px; margin-bottom:22px; }}
  .note{{ border:1px solid var(--b); border-radius:8px; background:var(--s1); padding:16px 20px; color:var(--tx); font-size:15px; }}

  /* Regulatory & Ledger Watch (V66) */
  .rw-wrap {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:14px; }}
  .rw-panel {{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .rw-panel-title {{ font-size:15px; font-weight:700; color:var(--hdr); margin-bottom:4px; letter-spacing:0.5px; font-family:var(--mn); }}
  .rw-panel-sub {{ font-size:12px; color:var(--tx); margin-bottom:12px; line-height:1.5; }}
  .rw-item {{ padding:8px 0; border-bottom:1px solid var(--b); display:flex; flex-direction:column; gap:2px; }}
  .rw-item:last-child {{ border-bottom:none; }}
  .rw-name {{ font-size:15px; color:var(--br); font-weight:600; }}
  .rw-link {{ font-size:15px; color:var(--bl); text-decoration:none; line-height:1.4; }}
  .rw-link:hover {{ color:var(--tq); }}
  .rw-meta {{ font-size:12px; color:var(--tx); }}
  .rw-empty {{ font-size:12px; color:var(--tx); padding:12px 0; font-style:italic; }}

  /* XRP Community Hub (V67) */
  .cm-wrap {{ display:grid; grid-template-columns:1fr 1fr; gap:14px; }}
  @media(max-width:700px){{ .cm-wrap {{ grid-template-columns:1fr; }} }}
  .cm-panel {{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px; }}
  .cm-panel-title {{ font-size:15px; font-weight:700; color:var(--hdr); margin-bottom:10px; letter-spacing:0.5px; font-family:var(--mn); }}
  .cm-item {{ padding:7px 0; border-bottom:1px solid var(--b); }}
  .cm-item:last-child {{ border-bottom:none; }}
  .cm-link {{ font-size:15px; color:var(--bl); text-decoration:none; font-weight:600; }}
  .cm-link:hover {{ color:var(--tq); }}
  .cm-desc {{ font-size:12px; color:var(--tx); margin-top:2px; line-height:1.4; }}

  /* FOOTER */
  footer{{ border-top:2px solid var(--bl); background:var(--bg); padding:16px 28px 16px; text-align:center; color:var(--tx); font-size:15px; font-family:var(--mn); }}
  footer .f-line{{ margin:5px 0; }}
  footer .brand-em{{ color:var(--bl); font-weight:700; font-style:normal; }}
  footer .val{{ color:var(--br); font-weight:700; }}
  .footer-btn{{ font-family:var(--mn); font-size:15px; font-weight:700; text-decoration:none; border-radius:3px; padding:1px 8px; cursor:pointer; margin-left:6px; }}
  .debug-btn{{ color:var(--or); border:1px solid var(--or); background:transparent; }}
  .debug-btn:hover{{ background:rgba(255,153,0,.12); }}
  .details-btn{{ color:var(--bl); border:1px solid var(--bl); background:transparent; }}
  .details-btn:hover{{ background:var(--bld); }}
  .notice{{ color:var(--yl); }}
  .copyright{{ font-size:12px; color:var(--tx); border-top:1px solid var(--b); padding-top:10px; margin-top:10px; }}

  /* PREFLIGHT MODAL */
  #pf-modal{{ display:none; position:fixed; inset:0; background:rgba(0,0,0,.92); z-index:9999; align-items:center; justify-content:center; padding:20px; }}
  #pf-box{{ background:var(--s1); border:1px solid var(--bl); border-radius:10px; max-width:580px; width:100%; overflow:hidden; }}
  #pf-box .pf-head{{ padding:12px 16px; background:var(--s2); border-bottom:1px solid var(--b); display:flex; justify-content:space-between; align-items:center; font-family:var(--mn); }}
  #pf-box .pf-head .t{{ color:var(--bl); font-weight:800; font-size:15px; text-transform:uppercase; letter-spacing:1px; }}
  #pf-box .pf-head .x{{ color:var(--bl); cursor:pointer; font-size:17px; font-weight:900; border:1px solid var(--bl); width:26px; height:26px; display:flex; align-items:center; justify-content:center; border-radius:4px; }}
  #pf-box .pf-head .x:hover{{ background:var(--bl); color:#000; }}
  #pf-box .pf-body{{ padding:14px 16px; font-family:var(--mn); font-size:15px; }}
  #pf-box .pf-overall{{ font-weight:800; color:{overall_color}; margin-bottom:10px; }}
  .pf-row{{ display:grid; grid-template-columns:1fr auto; grid-template-areas:"label badge" "detail detail"; gap:2px 10px; padding:8px 0; border-bottom:1px solid var(--b); }}
  .pf-row-label{{ grid-area:label; font-weight:700; color:var(--br); }}
  .pf-row-badge{{ grid-area:badge; font-weight:800; }}
  .pf-row-detail{{ grid-area:detail; color:var(--tx); font-size:12px; }}

  /* FLOATING RETURN / BACK-TO-TOP */
  #back-to-top{{ position:fixed; right:22px; bottom:22px; z-index:200; background:var(--bl); color:#000; border:none; border-radius:50%; width:46px; height:46px; font-size:17px; font-weight:900; cursor:pointer; box-shadow:0 0 14px rgba(117,188,255,.5); display:none; align-items:center; justify-content:center; line-height:1; }}
  #back-to-top:hover{{ background:#a6d4ff; }}

  /* V109: DCA Calculator, Historical Table, News Mention Volume */
  .dca-row{{ display:flex; justify-content:space-between; padding:4px 0; font-size:14px; color:var(--tx); }}
  .dca-row span:last-child{{ color:var(--br); font-weight:600; font-family:var(--mn); }}
  .hist-table{{ width:100%; border-collapse:collapse; font-size:13px; font-family:var(--mn); margin-top:8px; }}
  .hist-table th{{ text-align:left; color:var(--hdr); font-size:12px; padding:8px 6px; border-bottom:1px solid var(--b); white-space:nowrap; }}
  .hist-table td{{ padding:6px; border-bottom:1px solid var(--b); color:var(--tx); white-space:nowrap; }}
  .hist-table tr:hover td{{ background:rgba(3,177,252,.06); }}
  .nmv-row{{ display:flex; align-items:center; gap:10px; padding:5px 0; }}
  .nmv-cat{{ font-size:13px; color:var(--tx); width:150px; flex-shrink:0; }}
  .nmv-bar-track{{ flex:1; height:8px; background:var(--s2); border-radius:4px; overflow:hidden; }}
  .nmv-bar-fill{{ height:100%; background:var(--yl); }}
  .nmv-n{{ font-size:13px; color:var(--br); font-family:var(--mn); width:30px; text-align:right; flex-shrink:0; }}

  /* ============================================================
     RESPONSIVE SAFETY NET (V107) \u2014 catch-all rules for phones and
     small tablets, layered on top of the section-specific breakpoints
     above. Placed last so it wins the cascade. Covers iPhone/Android
     widths (~360-430px) that nothing above specifically targeted.
     ============================================================ */
  @media(max-width:480px){{
    .w{{ padding:8px 12px; }}
    main{{ padding:10px 12px 70px; }}
    body{{ font-size:14px; }}
    .hdr{{ padding-top:20px; padding-bottom:20px; gap:12px; }}
    [class$="-grid"], [class$="-grid3"], .sb-grid4 {{
      grid-template-columns: 1fr !important;
    }}
    .fx-grid{{ grid-template-columns:repeat(2,1fr) !important; }}
    .sb-grid{{ grid-template-columns:repeat(2,1fr) !important; }}
    .sb-grid4{{ grid-template-columns:1fr !important; }}
    table{{ display:block; overflow-x:auto; white-space:nowrap; }}
    .acct{{ padding:10px; }}
  }}
  @media(max-width:360px){{
    .w{{ padding:6px 8px; }}
    .sic{{ font-size:15px; }}
  }}

  /* ══ V119: REGULATORY SECTIONS ══ blue / turquoise / orange only */
  .rg-note{{ font-size:12px; color:var(--tx); font-family:var(--mn); letter-spacing:.5px; margin-top:10px; }}
  .rg-sub{{ font-size:12px; color:var(--tx); line-height:1.6; margin-bottom:14px; }}
  .rg-map{{ display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:10px; }}
  .rg-j{{ background:var(--s1); border:1px solid var(--b); border-left-width:4px; border-radius:8px; padding:11px 13px; }}
  .rg-j-n{{ font-weight:800; font-size:14px; color:var(--br); margin-bottom:3px; }}
  .rg-j-s{{ font-family:var(--mn); font-size:11px; font-weight:800; letter-spacing:1px; text-transform:uppercase; }}
  .rg-j-d{{ font-size:12px; color:var(--tx); line-height:1.5; margin-top:5px; }}
  .rg-tbl{{ width:100%; border-collapse:collapse; font-size:13px; }}
  .rg-tbl th{{ text-align:left; font-family:var(--mn); font-size:11px; letter-spacing:1px;
               text-transform:uppercase; color:var(--tx); border-bottom:1px solid var(--b); padding:8px 10px; }}
  .rg-tbl td{{ border-bottom:1px solid var(--b); padding:9px 10px; color:var(--br); vertical-align:top; }}
  .rg-tbl tr:last-child td{{ border-bottom:none; }}
  .rg-pill{{ font-family:var(--mn); font-size:11px; font-weight:800; letter-spacing:.8px;
             text-transform:uppercase; padding:3px 9px; border-radius:20px; border:1px solid currentColor;
             white-space:nowrap; display:inline-block; }}
  .rg-cal{{ display:flex; flex-direction:column; gap:9px; }}
  .rg-c{{ display:flex; gap:13px; align-items:flex-start; background:var(--s1);
          border:1px solid var(--b); border-radius:8px; padding:11px 13px; }}
  .rg-c-d{{ font-family:var(--mn); font-size:12px; font-weight:800; color:var(--tq);
            min-width:96px; letter-spacing:.5px; }}
  .rg-c-t{{ font-weight:700; font-size:13px; color:var(--br); }}
  .rg-c-b{{ font-size:12px; color:var(--tx); line-height:1.5; margin-top:3px; }}
  .rg-vt{{ display:grid; grid-template-columns:repeat(auto-fill,minmax(268px,1fr)); gap:10px; }}
  .rg-v{{ background:var(--s1); border:1px solid var(--b); border-radius:8px; padding:11px 13px; }}
  .rg-v-h{{ display:flex; justify-content:space-between; align-items:baseline; gap:8px; margin-bottom:5px; }}
  .rg-v-n{{ font-family:var(--mn); font-size:13px; font-weight:800; letter-spacing:1px; }}
  .rg-v-c{{ font-family:var(--mn); font-size:11px; color:var(--tx); white-space:nowrap; }}
  .rg-v-q{{ font-size:12px; color:var(--br); line-height:1.5; }}
  .rg-v-q a{{ color:var(--br); text-decoration:none; }}
  .rg-v-q a:hover{{ color:var(--hdr); text-decoration:underline; }}
  .rg-v-s{{ font-size:11px; color:var(--tx); font-family:var(--mn); margin-top:4px; }}
  .rg-sc{{ display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:10px; }}
  .rg-s{{ background:var(--s1); border:1px solid var(--b); border-radius:8px; padding:12px 14px; }}
  .rg-s-n{{ font-weight:800; font-size:14px; color:var(--br); }}
  .rg-s-i{{ font-family:var(--mn); font-size:11px; color:var(--tq); letter-spacing:.8px; margin:3px 0 6px; }}
  .rg-s-d{{ font-size:12px; color:var(--tx); line-height:1.55; }}
  .rg-flag{{ border:1px solid var(--or); border-radius:8px; padding:11px 14px; margin-top:12px;
             font-size:12px; color:var(--br); line-height:1.6; background:rgba(204,95,0,.07); }}
  @media(max-width:480px){{ .rg-c{{ flex-direction:column; gap:4px; }} .rg-tbl{{ font-size:12px; }} }}
  /* ---- V121 six-page navigation ---- */
  .xnav{{ position:sticky; top:0; z-index:60; background:var(--bg);
         border-top:2px solid var(--hdr); border-bottom:2px solid var(--hdr);
         padding:10px 0; }}
  .xnav-in{{ max-width:1280px; margin:0 auto; padding:0 10px;
            display:flex; justify-content:center; flex-wrap:wrap; gap:8px; }}
  .xnav a{{ display:inline-block; padding:8px 18px; border:1px solid var(--hdr);
           border-radius:4px; background:transparent; color:var(--hdr);
           font-family:var(--mn); font-size:15px; font-weight:700; letter-spacing:1.5px;
           text-decoration:none; white-space:nowrap; line-height:1.1; }}
  .xnav a:hover{{ background:rgba(3,177,252,.15); }}
  .xnav a.on{{ background:var(--hdr); color:#000; font-weight:800; }}
  @media(max-width:480px){{ .xnav a{{ padding:7px 13px; font-size:12px; letter-spacing:1px; }}
                           .xnav-in{{ gap:6px; }} }}
</style>
</head>
"""

    _pages = (("main","/","MAIN"), ("markets","/markets","MARKETS"),
              ("news","/news","NEWS"), ("institutional","/institutional","INSTITUTIONAL"),
              ("regulatory","/regulatory","REGULATORY"), ("community","/community","COMMUNITY"))
    _nav = ('<nav class="xnav"><div class="xnav-in">' + ''.join(
        f'<a href="{h}" class="{"on" if k == page else ""}">{t}</a>'
        for k, h, t in _pages) + '</div></nav>')

    _chrome = f"""<body id="top">

  <!-- BREAKING NEWS BAR -->
  <div id="breaking">
    <div class="bkinner">
      <div class="bkrow">
        <span class="bklbl"><span class="bk-bolt">\u26A1</span>BREAKING NEWS</span>
        <div class="bkscroll">
          <div class="bktext" id="bktext">{bktext}</div>
        </div>
      </div>
    </div>
  </div>

  <div class="w">
    <!-- HEADER -->
    <div class="hdr">
      <div class="logo">
        <div class="icon"><img src="/logo.jpg" alt="XRP Complete" width="47" height="100"></div>
        <div>
          <div class="title">{APP_NAME}</div>
          <div class="sub" style="font-size:17px;color:var(--hdr);letter-spacing:1.5px">The <i>NEW</i> XRP Intelligence Standard</div>
          <div class="sub" style="font-size:15px;color:var(--br);letter-spacing:1.2px">Every Signal. Every Region. Every Hour.</div>
          <div class="sub" style="font-size:15px;color:var(--tx);letter-spacing:1px">306+ sources over 8 global regions signaling 24/7</div>
        </div>
      </div>
      <div class="hright" style="display:flex;flex-direction:column;align-items:flex-end;gap:6px">
        <div style="display:flex;align-items:center;gap:8px">
          <a href="/about" style="color:var(--hdr);font-size:13px;font-weight:700;text-decoration:none;border:1px solid var(--hdr);padding:3px 10px;border-radius:5px;letter-spacing:0.5px">ABOUT US</a>
          <span class="dot"></span>
          <span class="run-lbl">LIVE</span>
          <span class="upd" id="uts">{boot_str}</span>
          <span style="font-size:12px;color:var(--tx);margin-left:8px;letter-spacing:0.5px">v{APP_VERSION}</span>
        </div>
        <div class="sub" style="font-size:15px;color:var(--gr);letter-spacing:1px">\u25CF {hdr_feeds_active}/{hdr_feeds_total} feeds scanned</div>
        <a href="https://xrpcompleteblog.com" target="_blank" rel="noopener" style="display:block;width:250px;height:70px">
          <img src="/blog_ad.png?v={APP_VERSION}" alt="XRP Complete Blog" style="display:block;width:250px;height:70px;object-fit:contain">
        </a>
      </div>
    </div>

{_nav}
"""

    _B = {}

    _B['status'] = f"""    <!-- SECTION 2: STATUS ROW (3 compact rectangles) -->
    <div class="srow">
      <div class="si">
        <span class="si-lbl"><span class="ic" style="color:var(--gr);font-weight:900">$</span> XRP / USD</span>
        <span>
          <span class="sv" id="st-price" style="color:{price_color};display:block">{price_str}</span>
          <span class="sv-sub" id="st-chg" style="color:{price_color};text-align:right;display:block">{chg_str}</span>
        </span>
      </div>
      <div class="si">
        <span class="si-lbl"><span class="ic">\U0001F4E1</span> Active Sources</span>
        <span class="sv" id="st-feeds" style="color:var(--bl)">{sources_str}</span>
      </div>
      <div class="si">
        <span class="si-lbl"><span class="ic">\U0001F630</span> Fear &amp; Greed</span>
        {fng_bar}
      </div>
    </div>

"""

    _B['rsi'] = f"""    <!-- SECTION 3: RSI / Support-Resistance / Time Machine / 52-Week -->
    <div class="grid2">
      <!-- LEFT COLUMN: RSI + 52-Week -->
      <div class="col">
        <div class="acct" style="border-color:rgba(3,177,252,.35)">
          <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4D0</span> RSI Signals</div>
          <div style="margin-bottom:14px">
            <div class="rsi-head">
              <span style="color:var(--tx)">1H RSI</span>
              <span style="font-weight:700;color:{r1h_col}">{r1h_val}</span>
              <span style="color:{r1h_col}">{r1h_lbl}</span>
            </div>
            <div class="rsi-track">
              <div class="rsi-tick" style="left:30%"></div>
              <div class="rsi-tick" style="left:70%"></div>
              <div class="rsi-fill" style="width:{r1h_pct}%;background:{r1h_col}"></div>
            </div>
            <div class="rsi-scale"><span>0 \u2014 Oversold</span><span>30</span><span>50</span><span>70</span><span>Overbought \u2014 100</span></div>
          </div>
          <div>
            <div class="rsi-head">
              <span style="color:var(--tx)">1D RSI</span>
              <span style="font-weight:700;color:{r1d_col}">{r1d_val}</span>
              <span style="color:{r1d_col}">{r1d_lbl}</span>
            </div>
            <div class="rsi-track">
              <div class="rsi-tick" style="left:30%"></div>
              <div class="rsi-tick" style="left:70%"></div>
              <div class="rsi-fill" style="width:{r1d_pct}%;background:{r1d_col}"></div>
            </div>
            <div class="rsi-scale"><span>0 \u2014 Oversold</span><span>30</span><span>50</span><span>70</span><span>Overbought \u2014 100</span></div>
          </div>
        </div>

        <div class="acct grow" style="border-color:rgba(3,177,252,.35)">
          <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4C5</span> 52-Week Range</div>
          <div class="w52-row">
            <span>Low: <strong style="color:var(--rd)">{w52_low_s}</strong></span>
            <span style="color:var(--tx)">Current: <strong style="color:var(--br)">{w52_cur_s}</strong></span>
            <span>High: <strong style="color:var(--gr)">{w52_high_s}</strong></span>
          </div>
          <div class="w52-bar">
            <div class="w52-needle" style="left:{w52_pos}%"></div>
          </div>
          <div class="w52-row">
            <span style="color:var(--tx)">From low: <strong style="color:var(--gr)">{w52_from_low}</strong></span>
            <span style="color:var(--tx)">Position: <strong style="color:var(--yl)">{w52_pos_s}</strong></span>
            <span style="color:var(--tx)">From high: <strong style="color:var(--rd)">{w52_from_high}</strong></span>
          </div>
        </div>
      </div>

      <!-- RIGHT COLUMN: Support/Resistance + Time Machine -->
      <div class="col">
        <div class="acct" style="border-color:rgba(255,64,96,.35)">
          <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3AF</span> Support &amp; Resistance</div>
          {sr_html}
        </div>

        <div class="acct grow" style="border-color:rgba(3,177,252,.35)">
          <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4C6</span> Price Time Machine</div>
          <div class="agrid2">
            <div class="abox">{tm_1y_html}</div>
            <div class="abox">{tm_1m_html}</div>
          </div>
          <div class="tvs">
            <div class="tvs-lbl">Today vs 1 Year Ago</div>
            <div class="tvs-txt" id="pt-narrative">{tm_narr}</div>
          </div>
        </div>
      </div>
    </div>

"""

    _B['chart'] = f"""    <!-- SECTION 4: LIVE XRP/USD CHART -->
    <div class="acct" style="padding:10px;border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4CA</span> Live XRP/USD Chart</div>
      <div style="height:440px;border-radius:8px;overflow:hidden;border:1px solid var(--b)">
        <div class="tradingview-widget-container" style="width:100%;height:100%">
          <div class="tradingview-widget-container__widget" style="width:100%;height:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
          {{"autosize":true,"symbol":"BITSTAMP:XRPUSD","interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","backgroundColor":"#000000","gridColor":"#0a0a0a","hide_top_toolbar":false,"allow_symbol_change":false,"save_image":false,"support_host":"https://www.tradingview.com"}}
          </script>
        </div>
      </div>
    </div>

"""

    _B['liquidity'] = f"""    <!-- SECTION 4b: XRP GLOBAL LIQUIDITY TRACKER (V103) -->
    <div class="acct" style="padding:12px;border-color:rgba(117,188,255,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--bl)"><span class="sic">\U0001F4A7</span> XRP Global Liquidity Tracker</div>
      <div style="font-size:15px;color:var(--tx);line-height:1.55;margin:6px 2px 12px 2px">
        Liquidity measures how easily XRP can be bought or sold worldwide without moving its price.
        Deep liquidity means large orders execute smoothly with tight spreads; thin liquidity means
        even modest trades can swing the market. The strongest single indicator is global trading
        volume relative to market capitalization &mdash; the turnover ratio &mdash; which shows how much of
        the total supply changes hands each day across all exchanges combined.
      </div>
      <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px">
        <div style="background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:10px 12px">
          <div style="font-size:12px;color:var(--tx);letter-spacing:1px">GLOBAL 24H VOLUME</div>
          <div style="font-size:22px;font-weight:900;color:var(--bl);font-family:var(--mn)">{liq_vol}</div>
          <div style="font-size:12px;color:var(--tx)">all exchanges, aggregated</div>
        </div>
        <div style="background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:10px 12px">
          <div style="font-size:12px;color:var(--tx);letter-spacing:1px">MARKET CAP</div>
          <div style="font-size:22px;font-weight:900;color:var(--tq);font-family:var(--mn)">{liq_mcap}</div>
          <div style="font-size:12px;color:var(--tx)">circulating value</div>
        </div>
        <div style="background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:10px 12px">
          <div style="font-size:12px;color:var(--tx);letter-spacing:1px">TURNOVER RATIO</div>
          <div style="font-size:22px;font-weight:900;color:var(--yl);font-family:var(--mn)">{liq_turn}</div>
          <div style="font-size:12px;color:var(--tx)">24h volume &divide; market cap</div>
        </div>
        <div style="background:var(--s1);border:1px solid var(--b);border-radius:8px;padding:10px 12px">
          <div style="font-size:12px;color:var(--tx);letter-spacing:1px">LIQUIDITY READ</div>
          <div style="font-size:22px;font-weight:900;color:{liq_color};font-family:var(--mn)">{liq_rating}</div>
          <div style="height:6px;border-radius:3px;background:var(--b);margin-top:6px;overflow:hidden">
            <div style="height:100%;width:{liq_pct}%;background:{liq_color}"></div>
          </div>
        </div>
      </div>
      <div style="font-size:12px;color:var(--tx);margin-top:8px;letter-spacing:0.5px">
        \U0001F4A7 Global aggregate read (not single-exchange) &bull; source: CoinPaprika &bull; refreshes automatically every 5 minutes
      </div>
    </div>

"""

    _B['onchain'] = f"""    <!-- SECTION 5: ON-CHAIN INTELLIGENCE + WHALE ALERT FEED -->
    <div class="oc-grid">
      <div class="acct" style="border-color:rgba(0,229,204,.35)">
        <div class="sec-title" style="color:var(--hdr)"><span class="sic">\u26D3\uFE0F</span> On-Chain Intelligence</div>
        <div class="ocbox-grid">
          <div class="ocbox tq">
            <div class="oclbl">Market Cap</div>
            <div class="ocval" style="color:var(--tq)">{oc_mcap}</div>
            <div class="ocsub">{oc_rank}</div>
          </div>
          <div class="ocbox">
            <div class="oclbl">24h Volume</div>
            <div class="ocval" style="color:var(--bl)">{oc_vol}</div>
            <div class="ocsub">{oc_volmcap}</div>
          </div>
          <div class="ocbox">
            <div class="oclbl">24h Range</div>
            <div class="ocval" style="color:var(--tq);font-size:17px">{oc_low} \u2013 {oc_high}</div>
            <div class="ocsub">{oc_rsi}</div>
          </div>
          <div class="ocbox">
            <div class="oclbl">52-Week Range</div>
            <div class="ocval" style="color:var(--bl);font-size:17px">{oc_52l} \u2013 {oc_52h}</div>
            <div class="ocsub">XRP / USD</div>
          </div>
          <div class="ocbox esc">
            <div class="oclbl">\u23F3 Next Ripple Escrow Release</div>
            <div class="esc-row">
              <div><div class="esc-num" id="esc-days">--</div><div class="ocsub">days</div></div>
              <div class="esc-sep">:</div>
              <div><div class="esc-num" id="esc-hrs">--</div><div class="ocsub">hrs</div></div>
              <div class="esc-sep">:</div>
              <div><div class="esc-num" id="esc-min">--</div><div class="ocsub">min</div></div>
            </div>
            <div class="ocsub">1B XRP \u00B7 Next release: {esc_date_str}</div>
          </div>
        </div>
      </div>

      <div class="panel" style="border-color:rgba(255,204,0,.35)">
        <div class="ph">
          <span class="pt" style="color:var(--hdr)"><span class="sic">\U0001F433</span> Whale Alert Feed</span>
          <span style="font-size:15px;font-family:var(--mn);color:var(--tx)" id="whale-ts">{whale_ts_val}</span>
        </div>
        <div class="whale-feed" id="whale-feed">
          {whale_feed_html}
        </div>
      </div>
    </div>

"""

    _B['ecosystem'] = f"""    <!-- SECTION 6: XRP ECOSYSTEM -->
    <div class="eco-wrap">
      <div class="eco-head">
        <span class="gicon">\U0001F310</span>
        <div>
          <div class="eco-title">XRP Ecosystem</div>
          <div class="eco-sub">Eight interconnected layers powering the future of global finance</div>
        </div>
      </div>
      <div class="eco-grid">
        {eco_html}
      </div>

      <!-- How the Layers Connect -->
      <div class="eco-sub-h">\u26D3\uFE0F How the Layers Connect</div>
      <div class="flow">
        <div class="flow-node"><div class="flow-ic">\U0001F517</div><div class="flow-name" style="color:var(--tq)">XRPL</div><div class="flow-role">Foundation</div></div>
        <div class="flow-arrow">\u2192</div>
        <div class="flow-node"><div class="flow-ic">\U0001F48E</div><div class="flow-name" style="color:var(--gr)">XRP</div><div class="flow-role">Native Asset</div></div>
        <div class="flow-arrow">\u2192</div>
        <div class="flow-node"><div class="flow-ic">\U0001F3E2</div><div class="flow-name" style="color:var(--bl)">Ripple Labs</div><div class="flow-role">Builder</div></div>
        <div class="flow-arrow">\u2192</div>
        <div class="flow-node"><div class="flow-ic">\U0001F310</div><div class="flow-name" style="color:var(--or)">RippleNet</div><div class="flow-role">Network</div></div>
        <div class="flow-arrow">\u2192</div>
        <div class="flow-node"><div class="flow-ic">\u26A1</div><div class="flow-name" style="color:var(--rd)">ODL</div><div class="flow-role">Liquidity</div></div>
        <div class="flow-arrow">+</div>
        <div class="flow-node"><div class="flow-ic">\U0001F4B5</div><div class="flow-name" style="color:var(--bl)">RLUSD</div><div class="flow-role">Stablecoin</div></div>
        <div class="flow-arrow">\u2192</div>
        <div class="flow-node"><div class="flow-ic">\U0001F6E0\uFE0F</div><div class="flow-name" style="color:var(--yl)">Ecosystem</div><div class="flow-role">Builders</div></div>
      </div>

      <!-- Common Misconceptions -->
      <div class="eco-sub-h">\u26A0\uFE0F Common Misconceptions \u2014 Set the Record Straight</div>
      <div class="myth-grid">
        <div class="myth-card">
          <div class="myth-lbl">\u274C MYTH</div>
          <div class="myth-q">"Ripple controls XRP"</div>
          <div class="real-lbl">\u2705 REALITY</div>
          <div class="real-txt">XRP runs on the XRPL, which is decentralised and maintained by the independent XRPL Foundation. Ripple holds XRP but cannot create, destroy, or freeze it.</div>
        </div>
        <div class="myth-card">
          <div class="myth-lbl">\u274C MYTH</div>
          <div class="myth-q">"Ripple can print more XRP"</div>
          <div class="real-lbl">\u2705 REALITY</div>
          <div class="real-txt">XRP has a fixed maximum supply of 100 billion \u2014 hardcoded into the protocol. No mining, no inflation, no new XRP can ever be created. Supply only decreases as tiny amounts are burned per transaction.</div>
        </div>
        <div class="myth-card">
          <div class="myth-lbl">\u274C MYTH</div>
          <div class="myth-q">"XRP is a security"</div>
          <div class="real-lbl">\u2705 REALITY</div>
          <div class="real-txt">Judge Torres ruled in 2023 that XRP is NOT a security in programmatic sales. The SEC settled with Ripple in 2025. XRP now operates with full US regulatory clarity for the first time.</div>
        </div>
      </div>
    </div>

"""

    _B['mainstream'] = f"""    <!-- SECTION 7: MAINSTREAM INTEGRATION MONITOR (title + tagline + legend key) -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F6E0</span> Mainstream Integration Monitor</div>
      <div class="trk-tag">XRP is no longer knocking on the door of traditional finance \u2014 it's building new springboards for growth and utilization.</div>
      <div class="trk-legend">
        <button class="trk-btn active" data-filter="ALL" onclick="filterTracker('ALL',this)" style="color:#ffffff;border-color:rgba(255,255,255,.5)">ALL</button>
        <button class="trk-btn" data-filter="CONFIRMED" onclick="filterTracker('CONFIRMED',this)" style="color:var(--gr);border-color:rgba(72,255,130,.5)">\u2705 CONFIRMED</button>
        <button class="trk-btn" data-filter="EXPLORING" onclick="filterTracker('EXPLORING',this)" style="color:var(--bl);border-color:rgba(117,188,255,.5)">\U0001F50D EXPLORING</button>
        <button class="trk-btn" data-filter="RUMORED" onclick="filterTracker('RUMORED',this)" style="color:var(--yl);border-color:rgba(255,204,0,.5)">\U0001F4AC RUMORED</button>
        <button class="trk-btn" data-filter="PILOT" onclick="filterTracker('PILOT',this)" style="color:var(--or);border-color:rgba(255,153,0,.5)">\U0001F9EA PILOT</button>
        <button class="trk-btn" data-filter="COMPETING" onclick="filterTracker('COMPETING',this)" style="color:var(--rd);border-color:rgba(255,64,96,.5)">\u2694\uFE0F COMPETING</button>
      </div>
    </div>

"""

    _B['instpart'] = f"""    <!-- SECTION 8: INSTITUTIONAL PARTNERSHIP TRACKER (separate section: 20 institutions, 5 rows of 4) -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3DB\uFE0F</span> Institutional Partnership Tracker</div>
      <div class="trk-grid">
        {inst_html}
      </div>
      <div id="trk-empty" class="trk-empty" style="display:none">No institutions in this category are currently available.</div>
    </div>

"""

    _B['tradfi'] = f"""    <!-- SECTION 9: XRP × TRADITIONAL FINANCE — INTEGRATION TIMELINE -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4C5</span> XRP \u00D7 Traditional Finance \u2014 Integration Timeline</div>
      <div class="tl-wrap">
        <div class="tl-line"></div>
        <div class="tl-track">
          {tl_html}
        </div>
      </div>
    </div>

"""

    _B['top20'] = f"""    <!-- SECTION 10: TOP 20 XRP STORIES (two subsections) -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3C6</span> Top 20 XRP Stories</div>
      <div class="eco-sub-h" style="padding:0"><span style="font-size:17px">\U0001F4F0</span> Top 20 Current Stories</div>
      <div class="story-list">
        {stories_current}
      </div>
      <div class="eco-sub-h" style="padding:0"><span style="font-size:17px">\U0001F525</span> Top 20 Most Influential Articles of the Week</div>
      <div class="story-list">
        {stories_weekly}
      </div>
    </div>

"""

    _B['usintel'] = f"""    <!-- SECTION 11: US INTELLIGENCE + GLOBAL PULSE (2-column, news-derived) -->
    <div class="intel-grid">
      <div class="intel" style="border-color:rgba(3,177,252,.35)">
        <div class="intel-h">
          <span class="intel-t" style="color:var(--hdr)"><span class="sic">\U0001F1FA\U0001F1F8</span> US Intelligence</span>
          <span style="font-size:15px;font-family:var(--mn);color:var(--tx)">{us_ts}</span>
        </div>
        <div class="intel-b">
          <div class="intel-pulse">{us_pulse}</div>
          <div class="intel-row"><b>Regulatory</b><br>{us_regulatory}</div>
          <div class="intel-row"><b>Institutional</b><br>{us_institutional}</div>
        </div>
      </div>
      <div class="intel" style="border-color:rgba(72,255,130,.35)">
        <div class="intel-h">
          <span class="intel-t" style="color:var(--hdr)"><span class="sic">\U0001F310</span> Global Pulse</span>
          <span style="font-size:15px;font-family:var(--mn);color:var(--tx)">{gl_ts}</span>
        </div>
        <div class="intel-b">
          <div class="intel-pulse">{gl_pulse}</div>
          <div class="intel-row"><b>Thesis</b><br>{gl_thesis}</div>
          <div class="sig-row">{gl_signals_html}</div>
        </div>
      </div>
    </div>

"""

    _B['regdisc'] = f"""    <!-- SECTION 12: REGIONAL DISCOURSE (news-derived) -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F5FA\uFE0F</span> Regional Discourse</div>
      <div class="rd-grid">
        {rd_html}
      </div>
    </div>

"""

    _B['scoreboard'] = f"""    <!-- SECTION 13: SIGNAL SCOREBOARD -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4E1</span> Signal Scoreboard</div>
      <div class="sb-grid">
        <div class="sb-box"><div class="sb-num" style="color:var(--bl)">{sb_total}</div><div class="sb-lbl">Stories Tracked</div><div class="sb-sub">{sb_feeds} sources</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--gr)">{sb_bull}</div><div class="sb-lbl">Bullish</div><div class="sb-sub">{sb_bull_pct}%</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">{sb_bear}</div><div class="sb-lbl">Bearish</div><div class="sb-sub">{sb_bear_pct}%</div></div>
        <div class="sb-box"><div class="sb-num">{sb_neut}</div><div class="sb-lbl">Neutral</div><div class="sb-sub" style="color:{sb_net_col}">Net: {sb_net_str}</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--yl)">{sb_fng}</div><div class="sb-lbl">Fear &amp; Greed</div><div class="sb-sub">{sb_fng_lbl}</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--bl)">{sb_rank}</div><div class="sb-lbl">Global Rank</div><div class="sb-sub">CoinCap</div></div>
      </div>
      <div class="sb-grid4">
        <div class="sb-box"><div class="sb-num" style="color:var(--bl)">{sb_mcap}</div><div class="sb-lbl">Market Cap</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--yl)">{sb_vol}</div><div class="sb-lbl">24h Volume</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--gr)">{sb_high}</div><div class="sb-lbl">24h High</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">{sb_low}</div><div class="sb-lbl">24h Low</div></div>
      </div>
      <div class="sb-bar"><div class="sb-fill" style="width:{sb_bull_pct}%"></div></div>
    </div>

"""

    _B['newsfeed'] = f"""    <!-- SECTION 14: GLOBAL NEWS FEED + RIGHT RAIL -->
    <div class="ledger-wrap">
      <div class="acct" style="border-color:rgba(3,177,252,.35);margin:0">
        <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F5DE\uFE0F</span> Global News Feed &amp; Search</div>
        <input class="gn-search" id="gn-search" type="text" placeholder="\U0001F50D Search XRP news..." oninput="filterFeed()">
        <div class="gn-cats" id="gn-cats">
          <button class="gn-btn active" data-cat="ALL" style="color:var(--br);border-color:var(--br)" onclick="feedCat('ALL',this)">ALL</button>
          <button class="gn-btn" data-cat="PRICE" style="color:var(--yl);border-color:var(--yl)" onclick="feedCat('PRICE',this)">PRICE</button>
          <button class="gn-btn" data-cat="LEGAL" style="color:var(--rd);border-color:var(--rd)" onclick="feedCat('LEGAL',this)">LEGAL</button>
          <button class="gn-btn" data-cat="REG" style="color:var(--or);border-color:var(--or)" onclick="feedCat('REG',this)">REG</button>
          <button class="gn-btn" data-cat="ECOSYSTEM" style="color:var(--gr);border-color:var(--gr)" onclick="feedCat('ECOSYSTEM',this)">ECOSYSTEM</button>
          <button class="gn-btn" data-cat="TECH" style="color:var(--tq);border-color:var(--tq)" onclick="feedCat('TECH',this)">TECH</button>
          <button class="gn-btn" data-cat="WHALE" style="color:var(--bl);border-color:var(--bl)" onclick="feedCat('WHALE',this)">WHALE</button>
        </div>
        <div class="gn-stats"><b id="gn-shown">{gn_shown}</b> stories shown &nbsp;|&nbsp; {gn_total} total &nbsp;|&nbsp; {sb_feeds} sources online</div>
        <div class="gn-list" id="gn-list">
          {gn_html}
        </div>
        <div class="gn-empty" id="gn-empty" style="display:none">No stories match your filter.</div>
      </div>

      <div class="rail">
        <div class="rail-panel">
          <div class="rail-h"><span class="sic">\U0001F517</span> XRPL Network</div>
          <div class="rail-row"><span class="rail-k">Network</span><span class="rail-v" style="color:var(--gr)">\u25CF Live</span></div>
          <div class="rail-row"><span class="rail-k">Consensus</span><span class="rail-v">Federated Byzantine</span></div>
          <div class="rail-row"><span class="rail-k">Ledger Close</span><span class="rail-v">~3-5 seconds</span></div>
          <div class="rail-row"><span class="rail-k">Tx Fee</span><span class="rail-v">~0.00001 XRP</span></div>
          <div class="rail-row"><span class="rail-k">Circulating</span><span class="rail-v" style="color:var(--gr)">62.2B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Escrow Locked</span><span class="rail-v">~43B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Total Supply</span><span class="rail-v">100B XRP</span></div>
        </div>
        <div class="rail-panel">
          <div class="rail-h"><span class="sic">\U0001F4CA</span> Market Structure</div>
          <div class="rail-row"><span class="rail-k">Price</span><span class="rail-v">{ms_price}</span></div>
          <div class="rail-row"><span class="rail-k">24h Change</span><span class="rail-v" style="color:{ms_chg_col}">{ms_chg}</span></div>
          <div class="rail-row"><span class="rail-k">Global Rank</span><span class="rail-v" style="color:var(--bl)">{ms_rank}</span></div>
          <div class="rail-row"><span class="rail-k">Market Cap</span><span class="rail-v">{ms_mcap}</span></div>
          <div class="rail-row"><span class="rail-k">24h Volume</span><span class="rail-v">{ms_vol}</span></div>
          <div class="rail-row"><span class="rail-k">Vol / MCap</span><span class="rail-v" style="color:var(--yl)">{ms_volmcap}</span></div>
          <div class="rail-row"><span class="rail-k">24h High</span><span class="rail-v" style="color:var(--gr)">{ms_high}</span></div>
          <div class="rail-row"><span class="rail-k">24h Low</span><span class="rail-v" style="color:var(--rd)">{ms_low}</span></div>
          <div class="rail-row"><span class="rail-k">XRP/BTC</span><span class="rail-v">{ms_xrpbtc}</span></div>
        </div>
        <div class="rail-panel">
          <div class="rail-h"><span class="sic">\u23F3</span> Ripple Escrow</div>
          <div class="rail-row"><span class="rail-k">Next Release</span><span class="rail-v" style="color:var(--yl)">{esc_next_str}</span></div>
          <div class="rail-row"><span class="rail-k">Amount</span><span class="rail-v">1B XRP</span></div>
        </div>
      </div>
    </div>

"""

    _B['analytics'] = f"""    <!-- SECTION 15: ANALYTICS LAB -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F52C</span> Analytics Lab</div>
      <div class="lab3">
        <div class="labp">
          <div class="labt"><span style="font-size:17px">\U0001F4C8</span> Signal Metrics</div>
          <div class="bstat"><span class="bk">Stories Today</span><span class="bv" style="color:var(--bl)">{sb_total}</span></div>
          <div class="bstat"><span class="bk">Bullish Signals</span><span class="bv" style="color:var(--gr)">{sb_bull}</span></div>
          <div class="bstat"><span class="bk">Bearish Signals</span><span class="bv" style="color:var(--rd)">{sb_bear}</span></div>
          <div class="bstat"><span class="bk">Neutral</span><span class="bv">{sb_neut}</span></div>
          <div class="bstat"><span class="bk">Net Sentiment</span><span class="bv" style="color:{sb_net_col}">{sb_net_str}</span></div>
          <div class="bstat"><span class="bk">Bull/Bear Ratio</span><span class="bv" style="color:var(--yl)">{al_ratio}</span></div>
        </div>
        <div class="labp">
          <div class="labt"><span style="font-size:17px">\U0001F4CA</span> Market Analytics</div>
          <div class="bstat"><span class="bk">Global Rank</span><span class="bv" style="color:var(--bl)">{ms_rank}</span></div>
          <div class="bstat"><span class="bk">Market Cap</span><span class="bv">{ms_mcap}</span></div>
          <div class="bstat"><span class="bk">24h Volume</span><span class="bv" style="color:var(--yl)">{ms_vol}</span></div>
          <div class="bstat"><span class="bk">Vol / MCap %</span><span class="bv" style="color:var(--bl)">{ms_volmcap}</span></div>
          <div class="bstat"><span class="bk">Fear &amp; Greed</span><span class="bv" style="color:var(--yl)">{al_fng}</span></div>
          <div class="bstat"><span class="bk">24h Change</span><span class="bv" style="color:{ms_chg_col}">{ms_chg}</span></div>
        </div>
        <div class="labp">
          <div class="labt"><span style="font-size:17px">\U0001F50D</span> Feed Intelligence</div>
          <div class="bstat"><span class="bk">Total Sources</span><span class="bv" style="color:var(--bl)">{NEWS["feeds_total"]}</span></div>
          <div class="bstat"><span class="bk">Active Feeds</span><span class="bv" style="color:var(--gr)">{NEWS["feeds_active"]}</span></div>
          <div class="bstat"><span class="bk">Foreign Feeds</span><span class="bv">{al_foreign} stories</span></div>
          <div class="bstat"><span class="bk">Refresh</span><span class="bv">5 min</span></div>
          <div class="bstat"><span class="bk">Regions Tracked</span><span class="bv" style="color:var(--yl)">8 regions</span></div>
          <div class="bstat"><span class="bk">Engine</span><span class="bv" style="color:var(--gr)">News-Derived</span></div>
        </div>
      </div>
      <div class="sb-grid4">
        <div class="sb-box"><div class="sb-num" style="color:var(--bl)">{sb_total}</div><div class="sb-lbl">Total Stories</div><div class="sb-sub">In memory</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--gr)">{sb_bull_pct}%</div><div class="sb-lbl">Bullish</div><div class="sb-sub">of tracked</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">{sb_bear_pct}%</div><div class="sb-lbl">Bearish</div><div class="sb-sub">of tracked</div></div>
        <div class="sb-box"><div class="sb-num" style="color:{sb_net_col}">{sb_net_str}</div><div class="sb-lbl">Net Sentiment</div><div class="sb-sub">bull \u2212 bear</div></div>
      </div>
    </div>

"""

    _B['leaderboard'] = f"""    <!-- SECTION 16: XRP COMPLETE LEADERBOARD -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3C6</span> XRP Complete Leaderboard</div>
      <div class="trk-tag">Top sources, most active regions, and live intelligence \u2014 the XRP Complete rankings.</div>
      <div class="lb-grid">
        <div class="lb-panel">
          <div class="lb-t" style="color:var(--yl)">\U0001F4E1 Top Sources Today</div>
          {lb_sources}
        </div>
        <div class="lb-panel">
          <div class="lb-t" style="color:var(--bl)">\U0001F5FA\uFE0F Most Active Regions</div>
          {lb_regions}
        </div>
        <div class="lb-panel">
          <div class="lb-t" style="color:var(--gr)">\U0001F525 Live Intelligence</div>
          <div class="lb-score">
            <div class="lb-score-num" style="color:{lb_color}">{lb_score}</div>
            <div class="lb-score-cap">Signal Score / 100</div>
            <div class="lb-score-lbl" style="color:{lb_color}">{lb_label}</div>
          </div>
          <div class="lb-mini">
            <div class="lb-mini-row"><span>Feeds Active</span><span style="color:var(--gr)">{sb_feeds}</span></div>
            <div class="lb-mini-row"><span>Stories Today</span><span style="color:var(--bl)">{sb_total}</span></div>
            <div class="lb-mini-row"><span>Bullish Share</span><span style="color:var(--yl)">{sb_bull_pct}%</span></div>
          </div>
        </div>
      </div>
    </div>

"""

    _B['brief'] = f"""    <!-- SECTION 17: XRP INTELLIGENCE BRIEF (twice daily — AM 12:00 PM CST, PM 9:00 PM CST) -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr);margin-bottom:10px"><span class="sic">\U0001F52E</span> XRP Intelligence Brief</div>

      <div class="brf-teaser">
        <div class="brf-teaser-line">\U0001F52E Next Proprietary Briefing in <span id="brf-countdown">\u2014</span></div>
        <div class="brf-teaser-sub">Twice daily \u2014 12:00 PM &amp; 9:00 PM CST \u2014 see World Clocks below</div>
      </div>

      <div class="brf-now-showing" id="brf-now-showing">
        <span class="brf-ribbon-wrap"><span class="brf-ribbon-icon">\U0001F52E</span><span class="brf-ribbon" id="brf-ribbon-label">CURRENT BRIEF</span></span>
        <span id="brf-now-edition">{brf_edition} EDITION</span>, {brf_gen}
        <span class="brf-now-spacer">\u00B7</span>
        <span id="brf-next-line">Next edition {brf_next}</span>
      </div>
      <div class="brf-intro-line">This edition's analysis, broken into 6 topics below \u2014 same briefing, organized by subject:</div>
      <div class="brf-grid" id="brief-{_live_slot}">
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F4CA</span> Market Pulse</div><div class="brf-x" id="brf-pulse">{brf_pulse}</div></div>
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F517</span> Story Connections</div><div class="brf-x" id="brf-connections">{brf_conn}</div></div>
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F3B2</span> Domino Effect</div><div class="brf-x" id="brf-domino">{brf_domino}</div></div>
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F30D</span> Regional Flashpoints</div><div class="brf-x" id="brf-regional">{brf_regional}</div></div>
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F441\uFE0F</span> Watchlist</div><div class="brf-x" id="brf-watchlist">{brf_watch}</div></div>
        <div class="brf-block"><div class="brf-t"><span style="font-size:17px">\U0001F3DB\uFE0F</span> TradFi Integration Outlook</div><div class="brf-x" id="brf-tradfi">{brf_tradfi}</div></div>
      </div>
      <div class="brf-note">\u26A0\uFE0F Informational only \u2014 not financial advice. Editions publish at 12:00 PM and 9:00 PM CST and are derived from the live news feed.</div>
    </div>
    <script type="application/json" id="brief-archive-data">{_archive_json}</script>

"""

    _B['clocks'] = f"""    <!-- SECTION 18: WORLD BRIEFING CLOCKS -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F310</span> World Briefing Clocks</div>
      <div class="trk-tag" style="color:var(--tx)">Local time across major crypto hubs, with each city's 1st (12:00 PM CST) and 2nd (9:00 PM CST) briefing time \u2014 orange by day, gray by night.</div>
      <div class="wc-row">
        {wc_html}
      </div>
    </div>

"""

    _B['unique'] = f"""    <!-- SECTION 19: UNIQUE DISPLAYS -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3A8</span> Unique Displays</div>
      <div class="ud-grid">
        <div class="ud-panel">
          <div class="fg-title"><span style="font-size:17px">\U0001F9E0</span> Smart Money Score</div>
          <div><span class="sm-score" style="color:{sm_color}">{sm_score}</span><span class="sm-cap"> /100</span></div>
          <div class="sm-label" style="color:{sm_color}">{sm_label}</div>
          <div class="sm-bar"><div class="sm-fill" style="width:{sm_score}%"></div></div>
          {sm_rows}
        </div>
        <div class="ud-panel">
          <div class="fg-title"><span style="font-size:17px">\U0001F630</span> Fear &amp; Greed Index \u2014 30-Day History</div>
          <div class="fg-chart">{fng_hist_html}</div>
          <div class="fg-axis"><span>30 days ago</span><span>20 days ago</span><span>10 days ago</span><span>today</span></div>
          <div class="fg-legend">
            <span><span class="fg-key" style="background:var(--rd)"></span>Extreme Fear (0-25)</span>
            <span><span class="fg-key" style="background:var(--or)"></span>Fear (25-45)</span>
            <span><span class="fg-key" style="background:var(--yl)"></span>Neutral (45-55)</span>
            <span><span class="fg-key" style="background:var(--gr)"></span>Greed (55-75)</span>
            <span><span class="fg-key" style="background:var(--tq)"></span>Extreme Greed (75-100)</span>
          </div>
        </div>
      </div>
    </div>

"""

    _B['longitudinal'] = f"""    <!-- SECTION 20: LONGITUDINAL VALUE MARKERS -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F4C8</span> Longitudinal Value Markers</div>
      <div class="trk-tag" style="color:var(--tx)">XRP/USD price performance across key windows.</div>
      <div class="lvm-grid">
        {lvm_html}
      </div>
    </div>

"""

    _B['heatmap'] = f"""    <!-- SECTION 21: REGIONAL NEWS ACTIVITY HEATMAP -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F5FA\uFE0F</span> Regional News Activity Heatmap</div>
      <div class="trk-tag" style="color:var(--tx)">XRP stories by region today \u2014 brighter means more coverage.</div>
      <div class="rh-grid">
        {rh_html}
      </div>
    </div>

"""

    _B['sentiment'] = f"""    <!-- SECTION 22: SENTIMENT ENGINE -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F9E0</span> Sentiment Engine</div>

      <div class="sent-top">
        <div class="ud-panel" style="text-align:center">
          <div class="fg-title" style="justify-content:center"><span style="font-size:17px">\U0001F4E1</span> XRP Interest Score</div>
          <div class="sm-score" style="color:var(--yl)">{_isc_score}</div>
          <div class="sm-label" style="color:var(--yl)">{_isc_label}</div>
          <div class="sm-bar"><div class="sm-fill" style="width:{_isc_score}%"></div></div>
          <div class="pt-note" style="margin-top:8px">Derived from live feed velocity</div>
        </div>
        <div class="ud-panel">
          <div class="fg-title"><span style="font-size:17px">\U0001F4F0</span> News Velocity \u2014 Stories per Hour (24h)</div>
          <div class="vel-chart">{vel_html}</div>
          <div class="fg-axis"><span>24h ago</span><span>12h ago</span><span>now</span></div>
        </div>
      </div>

      <div class="ud-panel" style="margin-bottom:14px">
        <div class="fg-title"><span style="font-size:17px">\U0001F4C8</span> Sentiment Trend \u2014 Since Deploy (up to 30 days)</div>
        <div class="sdt-chart">{sdt_html}</div>
        <div class="fg-legend" style="margin-top:8px">
          <span><span class="fg-key" style="background:var(--gr)"></span>Bullish day</span>
          <span><span class="fg-key" style="background:var(--rd)"></span>Bearish day</span>
          <span><span class="fg-key" style="background:var(--tx)"></span>Balanced day</span>
        </div>
      </div>

      <div class="ud-panel">
        <div class="fg-title"><span style="font-size:17px">\U0001F3C6</span> Source Leaderboard \u2014 Most Active (Today)</div>
        <table class="pt-tbl">
          <thead><tr><th>#</th><th>Source</th><th style="text-align:center">Stories</th>
            <th style="text-align:center">Bull</th><th style="text-align:center">Bear</th>
            <th>Sentiment</th><th style="text-align:center">Breaking</th></tr></thead>
          <tbody>{sent_lb_rows}</tbody>
        </table>
      </div>
    </div>

"""

    _B['competitive'] = f"""    <!-- SECTION 23: COMPETITIVE BRIEFING -->
    <div class="acct" style="border-color:rgba(117,188,255,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\u2694\uFE0F</span> Competitive Briefing</div>

      <div class="trk-tag" style="color:var(--tx)">XRP vs major competitors \u2014 live performance.</div>
      <div class="tbl-scroll" style="margin-bottom:14px">
        <table class="pt-tbl">
          <thead><tr><th>Asset</th><th style="text-align:right">Price</th><th style="text-align:right">24h %</th>
            <th style="text-align:right">7d %</th><th style="text-align:right">Market Cap</th><th>XRP Edge</th></tr></thead>
          <tbody>{comp_rows}</tbody>
        </table>
      </div>

      <div class="pt-cols" style="margin-bottom:14px">
        <div class="pt-col">
          <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\U0001F310 Active ODL Corridors</div>
          {odl_html}
        </div>
        <div class="pt-col">
          <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\U0001F4CB ISO 20022 Adoption</div>
          <div style="background:var(--s2);border:1px solid rgba(72,255,130,.25);border-radius:8px;padding:10px;margin-bottom:8px">
            <div style="font-size:15px;color:var(--gr);line-height:1.7;font-family:system-ui">XRP and the XRPL natively support ISO 20022 data fields, positioning Ripple as infrastructure for the new global payment standard.</div>
          </div>
          {iso_html}
          <div style="margin-top:8px;padding:6px 10px;background:var(--s2);border-radius:5px;border:1px solid var(--b);font-size:15px;font-family:var(--mn)">
            Banks exploring ISO 20022 + Ripple: <span style="color:var(--yl);font-weight:700">200+</span>
          </div>
        </div>
      </div>

      <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\u26A1 XRP vs SWIFT \u2014 The Case for ODL</div>
      <div class="sw-grid">
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">$5T</div><div class="sb-lbl">SWIFT Daily Volume</div><div class="sb-sub">Traditional rails</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">1-5 days</div><div class="sb-lbl">SWIFT Settlement</div><div class="sb-sub">Avg. cross-border</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--rd)">2-10%</div><div class="sb-lbl">SWIFT Avg Cost</div><div class="sb-sub">Remittance fees</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--gr)">3-5 sec</div><div class="sb-lbl">XRPL Settlement</div><div class="sb-sub">Any corridor, 24/7</div></div>
        <div class="sb-box"><div class="sb-num" style="color:var(--gr)">$0.0002</div><div class="sb-lbl">XRPL Cost</div><div class="sb-sub">Per transaction</div></div>
      </div>
      <div style="margin-top:8px;padding:10px 14px;background:rgba(72,255,130,.04);border:1px solid rgba(72,255,130,.2);border-radius:6px;font-size:15px;color:var(--br);line-height:1.7;font-family:system-ui">
        XRPL settles in seconds for fractions of a cent, 24/7/365 \u2014 no correspondent banking chain, no cut-off times.
      </div>
    </div>

"""

    _B['execdev'] = f"""    <!-- SECTION 24: RIPPLE EXECUTIVE TRACKER + XRPL DEV ACTIVITY -->
    <div class="ed-grid" style="margin:10px 0">
      <div class="ed-panel" style="border-color:rgba(255,153,0,.25)">
        <div class="ed-head">
          <span class="ed-title" style="color:var(--or)">\U0001F3A4 Ripple Exec Tracker</span>
          <span style="font-size:12px;font-family:var(--mn);color:var(--tx)">{ex_ts}</span>
        </div>
        <div class="ex-tabs" id="ex-tabs">
          <button class="ex-tab on" data-tab="ALL" onclick="execTab('ALL',this)">ALL</button>
          <button class="ex-tab" data-tab="BRAD" onclick="execTab('BRAD',this)">BRAD</button>
          <button class="ex-tab" data-tab="MONICA" onclick="execTab('MONICA',this)">MONICA</button>
          <button class="ex-tab" data-tab="DAVID" onclick="execTab('DAVID',this)">DAVID</button>
          <button class="ex-tab" data-tab="STUART" onclick="execTab('STUART',this)">STUART</button>
        </div>
        <div class="ex-feed" id="ex-feed">
          {ex_html}
        </div>
      </div>

      <div class="ed-panel" style="border-color:rgba(72,255,130,.2)">
        <div class="ed-head">
          <span class="ed-title" style="color:var(--gr)">\U0001F4BB XRPL Dev Activity</span>
          <span style="font-size:12px;font-family:var(--mn);color:var(--tx)">{gh_ts}</span>
        </div>
        <div class="gh-stats">
          <div class="gh-stat"><div class="gh-stat-num" style="color:var(--gr)">{gh_rippled_7d}</div><div class="gh-stat-lbl">rippled commits<br>7 days</div></div>
          <div class="gh-stat"><div class="gh-stat-num" style="color:var(--bl)">{gh_other_7d}</div><div class="gh-stat-lbl">other repos<br>7 days</div></div>
          <div class="gh-stat"><div class="gh-stat-num" style="color:var(--yl)">{gh_stars}</div><div class="gh-stat-lbl">GitHub stars<br>3 repos</div></div>
          <div class="gh-stat"><div class="gh-stat-num" style="color:var(--or)">{gh_issues}</div><div class="gh-stat-lbl">open issues<br>3 repos</div></div>
        </div>
        <div class="gh-latest">
          <div class="gh-latest-lbl">Latest commit</div>
          <div class="gh-latest-msg">{gh_last_msg}</div>
          <div class="gh-latest-meta">{gh_last_meta}</div>
        </div>
        <div class="gh-feed" id="gh-feed">
          {gh_commits_html}
        </div>
      </div>
    </div>

"""

    _B['regradar'] = f"""    <!-- SECTION 25: REGULATORY RADAR -->
    <div class="acct" style="border-color:rgba(255,153,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F3DB\uFE0F</span> Regulatory Radar</div>

      <div class="trk-tag" style="color:var(--tx);display:flex;justify-content:space-between">
        <span>\U0001F30D Global XRP Legal Status</span><span>Reference \u2014 verify locally before acting</span>
      </div>
      <div class="cg-grid" style="margin-bottom:16px">
        {cg_html}
      </div>

      <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\U0001F4CA XRP ETF / ETP Tracker</div>
      <div class="tbl-scroll" style="margin-bottom:16px">
        <table class="pt-tbl">
          <thead><tr><th>Applicant</th><th>Product</th><th>Market</th><th>Status</th><th>Filed</th><th>Note</th></tr></thead>
          <tbody>{etf_html}</tbody>
        </table>
      </div>

      <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\u2696\uFE0F SEC Case Timeline</div>
      <div class="tl-wrap" style="margin-bottom:16px"><div class="tl-line"></div><div class="tl-track">{sec_tl_html}</div></div>

      <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\U0001F1EA\U0001F1FA MiCA Implementation</div>
      <div style="font-size:15px;color:var(--tx);line-height:1.7;font-family:system-ui;margin-bottom:10px;max-width:820px">
        MiCA (Markets in Crypto-Assets) is the EU's comprehensive crypto regulatory framework \u2014 the closest thing Europe has to
        a single rulebook for digital assets. It gives XRP formal status as a crypto-asset, not a security, across all 27
        member states. Here's how the rollout has progressed:
      </div>
      <div class="ud-panel" style="margin-bottom:16px">{mica_html}</div>

      <div class="trk-tag" style="color:var(--tx);margin-bottom:8px">\U0001F3E6 Central Bank / CBDC Projects on XRPL</div>
      <div class="cg-grid" style="grid-template-columns:repeat(3,1fr)">
        {cbdc_html}
      </div>
    </div>

"""

    _B['clarity'] = f"""    <!-- SECTION 26: CLARITY ACT TRACKER -->
    <div class="acct" style="border-color:rgba(255,153,0,.35);margin:10px 0">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:6px">
        <div class="sec-title" style="color:var(--hdr);margin:0"><span class="sic">\U0001F3DB\uFE0F</span> CLARITY Act Tracker</div>
        <div style="text-align:right"><div class="pl-counter" style="color:var(--or)">{ca_count}/10</div>
          <div style="font-size:12px;color:var(--tx);font-family:var(--mn)">most recent stories</div></div>
      </div>
      <div style="font-size:15px;color:var(--tx);line-height:1.7;font-family:system-ui;margin-bottom:12px;max-width:900px">
        The Digital Asset Market Clarity Act (CLARITY Act) would split crypto oversight between the SEC and CFTC and is
        currently on the Senate calendar awaiting a floor vote. This tracker shows the 10 most recent stories on its
        progress \u2014 newest first, with the oldest dropping off automatically as fresh news breaks. Always current.
      </div>
      <div class="ca-list">
        {ca_html}
      </div>
    </div>

"""

    _B['enterprise'] = f"""    <!-- SECTION 27: GLOBAL XRP ENTERPRISE & PARTNERSHIP LEDGER -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:10px;margin-bottom:6px">
        <div class="sec-title" style="color:var(--hdr);margin:0"><span class="sic">\U0001F310</span> Global XRP Enterprise &amp; Partnership Ledger</div>
        <div style="text-align:right"><div class="pl-counter">{pl_total}+</div><div style="font-size:12px;color:var(--tx);font-family:var(--mn)">institutions &amp; deals</div></div>
      </div>
      <div style="font-size:15px;color:var(--tx);line-height:1.7;font-family:system-ui;margin-bottom:12px;max-width:900px">
        An ever-growing record of banks, institutions, and enterprises using XRP, XRPL, or Ripple technology \u2014 from
        foundational partnerships to newly announced deals. New entries are detected automatically from the live news feed
        and added here permanently; nothing is ever removed. Newest announcements shown first.
      </div>
      <div class="feed-wrap">
        <div>
          <input class="pl-search" id="pl-search" type="text" placeholder="\U0001F50D Search institution, country, category..." oninput="filterPartnerships()">
      <div class="pl-cats" id="pl-cats">
        <button class="pl-btn active" data-cat="ALL" style="color:var(--br);border-color:var(--br)" onclick="plCat('ALL',this)">ALL</button>
        <button class="pl-btn" data-cat="A" style="color:var(--gr);border-color:var(--gr)" onclick="plCat('A',this)">\U0001F680 ODL/XRP Live</button>
        <button class="pl-btn" data-cat="B" style="color:var(--bl);border-color:var(--bl)" onclick="plCat('B',this)">\U0001F3DB\uFE0F Global Banks</button>
        <button class="pl-btn" data-cat="C" style="color:var(--tq);border-color:var(--tq)" onclick="plCat('C',this)">\U0001F6E0\uFE0F Tech/Custody</button>
        <button class="pl-btn" data-cat="D" style="color:var(--or);border-color:var(--or)" onclick="plCat('D',this)">\U0001F30D Regional</button>
        <button class="pl-btn" data-cat="E" style="color:var(--yl);border-color:var(--yl)" onclick="plCat('E',this)">\U0001F7E1 ETF/Treasury</button>
        <button class="pl-btn" data-cat="N" style="color:var(--yl);border-color:var(--yl)" onclick="plCat('N',this)">\U0001F195 New Deals</button>
      </div>
      <div class="pl-stats">
        <b id="pl-shown">{min(pl_total, 30)}</b> shown &nbsp;|&nbsp; <b>{pl_total}</b> total &nbsp;|&nbsp;
        <span style="color:var(--gr)">{pl_detected} newly detected</span>
      </div>
      <div class="pl-list" id="pl-list">
        {pl_html}
      </div>
      <div style="margin-top:10px;font-size:12px;color:var(--tx);font-family:var(--mn);opacity:.7">
        Baseline sources: Ripple.com partner listings, SEC filings, central bank announcements, verified corporate press
        releases. New entries are detected from the live news feed. Directory is for informational purposes; some
        partnerships may be pilots or historical integrations.
      </div>
        </div>
        <div class="sd-panel">
          <div class="sd-head">
            <span class="sd-title">\U0001F4D1 Global Partnership Directory</span>
            <span class="sd-count">{sd_count}+</span>
          </div>
          <div class="sd-sub">Curated master list of confirmed global partnerships &amp; contracts. Refreshes every 3 days. Updated {sd_updated}.</div>
          <div class="sd-list">
            {sd_html}
          </div>
        </div>
      </div>
    </div>

"""

    _B['advmetrics'] = f"""    <!-- SECTION 28: ADVANCED METRICS -->
    <div class="acct" style="border-color:rgba(0,229,204,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F52C</span> Advanced Metrics</div>
      <div class="trk-tag" style="color:var(--tx)">Technical indicators, order book depth, and reference specs \u2014 all computed from live, verifiable market data.</div>

      <div class="am-grid2" style="margin-bottom:10px">
        <div class="am-panel">
          <div class="am-title" style="color:var(--tq)">\u2699\uFE0F XRPL Technical Specs</div>
          <div class="am-sub">How XRPL compares on the metrics that matter for payments</div>
          <table class="pt-tbl">
            <thead><tr><th>Metric</th><th style="text-align:center;color:var(--gr)">XRPL</th>
              <th style="text-align:center;color:var(--bl)">ETH</th><th style="text-align:center;color:var(--or)">SOL</th>
              <th style="text-align:center;color:var(--tx)">BTC</th></tr></thead>
            <tbody>{ts_html}</tbody>
          </table>
        </div>
        <div class="am-panel">
          <div class="am-title" style="color:var(--or)">\U0001F4DA XRP Use Case Library</div>
          <div class="am-sub">Where XRP and XRPL are actually being used today</div>
          <div class="uc-list">{uc_html}</div>
        </div>
      </div>

      <div class="am-grid2" style="margin-bottom:10px">
        <div class="am-panel">
          <div class="am-title" style="color:var(--tq)">\U0001F4E6 Accumulation / Distribution</div>
          <div class="am-sub">Chaikin A/D Line \u2014 computed from price, volume, and daily range (no wallet tracking involved)</div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
            <div class="abox" style="border-left-color:var(--tq)"><div class="abox-lbl">7-Day Signal</div>
              <div class="abox-val" style="color:{ad_c7}">{ad_s7}</div></div>
            <div class="abox" style="border-left-color:var(--bl)"><div class="abox-lbl">30-Day Signal</div>
              <div class="abox-val" style="color:{ad_c30}">{ad_s30}</div></div>
          </div>
        </div>
        <div class="am-panel">
          <div class="am-title" style="color:var(--tq)">\U0001F522 XRP Correlation Matrix</div>
          <div class="am-sub">30-day return correlation (Pearson) \u2014 how closely XRP tracks each asset</div>
          {corr_html}
          <div style="margin-top:4px;font-size:12px;color:var(--tx);font-family:var(--mn)">
            +1.0 = moves identically \u00B7 0 = unrelated \u00B7 -1.0 = moves opposite
          </div>
        </div>
      </div>

      <div class="am-grid2">
        <div class="am-panel" style="grid-column:1/3">
          <div class="am-title" style="color:var(--gr)">\U0001F4CA XRP Order Book Depth</div>
          <div class="am-sub">Live bid/ask walls on Binance XRP/USDT \u2014 top 8 levels each side</div>
          {ob_body_html}
        </div>
      </div>
      <div class="am-panel" style="margin-top:10px">
        <div class="am-title" style="color:var(--tq)">\U0001F4A7 Liquidity Map</div>
        <div class="am-sub">Bid vs. ask value in the visible order book</div>
        {liq_html}
      </div>
    </div>

"""

    _B['practical'] = f"""    <!-- SECTION 29: PRACTICAL TOOLS -->
    <div class="acct" style="border-color:rgba(0,229,204,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F6E0\uFE0F</span> Practical Tools</div>
      <div class="pt-cols">
        <div class="pt-col">
          <!-- P&L Calculator -->
          <div class="pt-panel" style="border-color:rgba(0,229,204,.25)">
            <div class="pt-head"><span class="pt-title" style="color:var(--tq)">\U0001F4B0 XRP P&amp;L Calculator</span></div>
            <div class="pt-body">
              <div class="pt-row2">
                <div><div class="pt-lbl">Buy Price (USD)</div>
                  <input id="pl-buy" class="pt-input" type="number" step="0.0001" placeholder="e.g. 0.50" oninput="calcPL()"></div>
                <div><div class="pt-lbl">Quantity (XRP)</div>
                  <input id="pl-qty" class="pt-input" type="number" step="1" placeholder="e.g. 10000" oninput="calcPL()"></div>
              </div>
              <div>
                <div class="pt-lbl">Sell / Target Price (USD)
                  <span class="pt-use-live" onclick="document.getElementById('pl-sell').value=currentXRPPrice.toFixed(4);calcPL()">[use live price]</span>
                </div>
                <input id="pl-sell" class="pt-input" type="number" step="0.0001" placeholder="e.g. 2.00" oninput="calcPL()">
              </div>
              <div id="pl-results" class="pt-results">
                <div class="pt-res-row"><span class="sm-k">Cost Basis</span><span class="sm-v" id="pl-cost">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">Current / Target Value</span><span class="sm-v" id="pl-value">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">P&amp;L (USD)</span><span id="pl-usd" style="font-weight:700;font-size:17px">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">P&amp;L (%)</span><span id="pl-pct" style="font-weight:700;font-size:17px">\u2014</span></div>
              </div>
              <div class="pt-note">\u26A0\uFE0F Not financial advice. For informational purposes only.</div>
            </div>
          </div>

          <!-- Multi-Currency -->
          <div class="pt-panel" style="border-color:rgba(0,229,204,.2)">
            <div class="pt-head"><span class="pt-title" style="color:var(--tq)">\U0001F4B1 XRP Price \u2014 Multi-Currency</span><span class="pt-note">{fx_ts}</span></div>
            <div class="fx-grid">
              <div class="fx-box hi"><div class="fx-lbl">USD \U0001F1FA\U0001F1F8</div><div class="fx-val">${fx_usd_disp}</div></div>
              <div class="fx-box"><div class="fx-lbl">EUR \U0001F1EA\U0001F1FA</div><div class="fx-val">\u20AC{fx_eur}</div></div>
              <div class="fx-box"><div class="fx-lbl">GBP \U0001F1EC\U0001F1E7</div><div class="fx-val">\u00A3{fx_gbp}</div></div>
              <div class="fx-box"><div class="fx-lbl">JPY \U0001F1EF\U0001F1F5</div><div class="fx-val" style="font-size:17px">\u00A5{fx_jpy}</div></div>
              <div class="fx-box"><div class="fx-lbl">AUD \U0001F1E6\U0001F1FA</div><div class="fx-val">A${fx_aud}</div></div>
              <div class="fx-box"><div class="fx-lbl">CAD \U0001F1E8\U0001F1E6</div><div class="fx-val">C${fx_cad}</div></div>
              <div class="fx-box"><div class="fx-lbl">SGD \U0001F1F8\U0001F1EC</div><div class="fx-val">S${fx_sgd}</div></div>
              <div class="fx-box"><div class="fx-lbl">INR \U0001F1EE\U0001F1F3</div><div class="fx-val" style="font-size:17px">\u20B9{fx_inr}</div></div>
              <div class="fx-box"><div class="fx-lbl">BRL \U0001F1E7\U0001F1F7</div><div class="fx-val">R${fx_brl}</div></div>
              <div class="fx-box"><div class="fx-lbl">CHF \U0001F1E8\U0001F1ED</div><div class="fx-val">Fr{fx_chf}</div></div>
              <div class="fx-box"><div class="fx-lbl">CNY \U0001F1E8\U0001F1F3</div><div class="fx-val" style="font-size:17px">\u00A5{fx_cny}</div></div>
              <div class="fx-box"><div class="fx-lbl">KRW \U0001F1F0\U0001F1F7</div><div class="fx-val" style="font-size:17px">\u20A9{fx_krw}</div></div>
              <div class="fx-box"><div class="fx-lbl">MXN \U0001F1F2\U0001F1FD</div><div class="fx-val" style="font-size:17px">$MX{fx_mxn}</div></div>
              <div class="fx-box"><div class="fx-lbl">PHP \U0001F1F5\U0001F1ED</div><div class="fx-val" style="font-size:17px">\u20B1{fx_php}</div></div>
              <div class="fx-box"><div class="fx-lbl">NGN \U0001F1F3\U0001F1EC</div><div class="fx-val" style="font-size:17px">\u20A6{fx_ngn}</div></div>
              <div class="fx-box"><div class="fx-lbl">ZAR \U0001F1FF\U0001F1E6</div><div class="fx-val" style="font-size:17px">R{fx_zar}</div></div>
              <div class="fx-box"><div class="fx-lbl">AED \U0001F1E6\U0001F1EA</div><div class="fx-val" style="font-size:17px">AED{fx_aed}</div></div>
              <div class="fx-box"><div class="fx-lbl">SAR \U0001F1F8\U0001F1E6</div><div class="fx-val" style="font-size:17px">SAR{fx_sar}</div></div>
              <div class="fx-box"><div class="fx-lbl">HKD \U0001F1ED\U0001F1F0</div><div class="fx-val" style="font-size:17px">HK${fx_hkd}</div></div>
              <div class="fx-box"><div class="fx-lbl">NZD \U0001F1F3\U0001F1FF</div><div class="fx-val">NZ${fx_nzd}</div></div>
              <div class="fx-box"><div class="fx-lbl">SEK \U0001F1F8\U0001F1EA</div><div class="fx-val" style="font-size:17px">{fx_sek}kr</div></div>
              <div class="fx-box"><div class="fx-lbl">NOK \U0001F1F3\U0001F1F4</div><div class="fx-val" style="font-size:17px">{fx_nok}kr</div></div>
              <div class="fx-box"><div class="fx-lbl">TRY \U0001F1F9\U0001F1F7</div><div class="fx-val" style="font-size:17px">\u20BA{fx_try}</div></div>
              <div class="fx-box"><div class="fx-lbl">THB \U0001F1F9\U0001F1ED</div><div class="fx-val" style="font-size:17px">\u0E3F{fx_thb}</div></div>
              <div class="fx-box"><div class="fx-lbl">IDR \U0001F1EE\U0001F1E9</div><div class="fx-val" style="font-size:17px">Rp{fx_idr}</div></div>
              <div class="fx-box"><div class="fx-lbl">VND \U0001F1FB\U0001F1F3</div><div class="fx-val" style="font-size:17px">\u20AB{fx_vnd}</div></div>
              <div class="fx-box"><div class="fx-lbl">PLN \U0001F1F5\U0001F1F1</div><div class="fx-val" style="font-size:17px">z\u0142{fx_pln}</div></div>
            </div>
          </div>
        </div>

        <div class="pt-col">
          <!-- Escrow & Ripple Holdings Tracker -->
          <div class="pt-panel" style="border-color:rgba(117,188,255,.25)">
            <div class="pt-head"><span class="pt-title" style="color:var(--bl)">\U0001F512 Escrow &amp; Ripple Holdings</span></div>
            <div class="pt-body">
              <div class="pt-lbl">Ripple's Own XRP \u2014 Publicly Verifiable</div>
              <div style="background:var(--s2);border:1px solid rgba(117,188,255,.3);border-radius:6px;padding:10px;margin-top:6px">
                <div style="font-size:12px;color:var(--tx);margin-bottom:8px">Next scheduled release (1B XRP, 1st of month 00:00 UTC):</div>
                <div id="esc-countdown" data-eta="{esc_iso}" style="font-size:22px;font-weight:900;font-family:var(--mn);color:var(--bl);margin-bottom:8px">\u2014</div>
                <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--tx);border-top:1px solid var(--b);padding-top:8px">
                  <span>Total in escrow</span><span style="color:var(--br);font-weight:700">~43B XRP</span>
                </div>
                <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--tx);margin-top:4px">
                  <span>Circulating supply</span><span style="color:var(--br);font-weight:700">~62B XRP</span>
                </div>
                <div style="font-size:12px;color:var(--tx);margin-top:8px;font-style:italic">Escrow addresses are public and independently verifiable on-chain \u2014 this is Ripple's own locked supply, not a personal wallet lookup.</div>
              </div>
            </div>
          </div>

          <!-- Portfolio Tracker -->
          <div class="pt-panel" style="border-color:rgba(72,255,130,.2)">
            <div class="pt-head"><span class="pt-title" style="color:var(--gr)">\U0001F4C8 Portfolio Tracker</span><span class="pt-note">Session only</span></div>
            <div class="pt-body">
              <div style="display:grid;grid-template-columns:1fr 1fr 1fr auto;gap:6px">
                <input id="pt-label" class="pt-input" type="text" placeholder="Label (e.g. Wallet 1)">
                <input id="pt-amount" class="pt-input" type="number" placeholder="XRP amount">
                <input id="pt-cost" class="pt-input" type="number" placeholder="Avg buy price">
                <button class="pt-btn-gr" onclick="addPortfolioEntry()">+ ADD</button>
              </div>
              <div id="portfolio-table"><div style="font-size:15px;font-family:var(--mn);color:var(--tx)">No entries yet. Add a position above.</div></div>
              <div id="portfolio-totals" class="pt-results">
                <div class="pt-res-row"><span class="sm-k">Total XRP</span><span class="sm-v" id="pt-total-xrp">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">Total Value</span><span class="sm-v" id="pt-total-val">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">Total P&amp;L</span><span id="pt-total-pl" style="font-weight:700;font-size:15px">\u2014</span></div>
              </div>
              <div class="pt-note">\u26A0\uFE0F Session only \u2014 entries clear on page refresh. Not financial advice.</div>
            </div>
          </div>

          <!-- Remittance Calculator -->
          <div class="pt-panel" style="border-color:rgba(0,229,204,.25)">
            <div class="pt-head"><span class="pt-title" style="color:var(--tq)">\U0001F4B8 Remittance Calculator</span><span class="pt-note">SWIFT vs XRP</span></div>
            <div class="pt-body">
              <div class="pt-row2">
                <div><div class="pt-lbl">Send Amount (USD)</div>
                  <input id="rm-amount" class="pt-input" type="number" placeholder="e.g. 1000" oninput="calcRemittance()"></div>
                <div><div class="pt-lbl">Corridor</div>
                  <select id="rm-corridor" class="pt-select" onchange="calcRemittance()">
                    <option value="6.0">\U0001F1FA\U0001F1F8\u2192\U0001F1F2\U0001F1FD USA to Mexico (6%)</option>
                    <option value="7.5">\U0001F1FA\U0001F1F8\u2192\U0001F1F5\U0001F1ED USA to Philippines (7.5%)</option>
                    <option value="8.0">\U0001F1EC\U0001F1E7\u2192\U0001F1F3\U0001F1EC UK to Nigeria (8%)</option>
                    <option value="5.5">\U0001F1EF\U0001F1F5\u2192\U0001F1F5\U0001F1ED Japan to Philippines (5.5%)</option>
                    <option value="6.5">\U0001F1E6\U0001F1FA\u2192\U0001F1F5\U0001F1ED Australia to Philippines (6.5%)</option>
                    <option value="9.0">\U0001F1FA\U0001F1F8\u2192\U0001F1EE\U0001F1F3 USA to India (9%)</option>
                    <option value="7.0">\U0001F1EA\U0001F1FA\u2192\U0001F1F2\U0001F1FD Europe to Mexico (7%)</option>
                    <option value="5.0">\U0001F1F8\U0001F1EC\u2192\U0001F30F Singapore to SE Asia (5%)</option>
                  </select>
                </div>
              </div>
              <div id="rm-results" style="display:none">
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                  <div class="rm-fee-box" style="background:rgba(255,64,96,.08);border:1px solid rgba(255,64,96,.3)">
                    <div class="pt-lbl" style="color:var(--rd)">SWIFT / Traditional</div>
                    <div style="font-size:22px;font-weight:900;font-family:var(--mn);color:var(--rd)" id="rm-swift-fee">\u2014</div>
                    <div class="pt-note">fee lost</div>
                    <div style="font-size:15px;font-family:var(--mn);color:var(--br);margin-top:6px;font-weight:700" id="rm-swift-recv">\u2014 received</div>
                    <div class="pt-note">\u23F1 1-5 business days</div>
                  </div>
                  <div class="rm-fee-box" style="background:rgba(72,255,130,.08);border:1px solid rgba(72,255,130,.3)">
                    <div class="pt-lbl" style="color:var(--gr)">XRP / XRPL ODL</div>
                    <div style="font-size:22px;font-weight:900;font-family:var(--mn);color:var(--gr)">$0.0002</div>
                    <div class="pt-note">fee lost</div>
                    <div style="font-size:15px;font-family:var(--mn);color:var(--br);margin-top:6px;font-weight:700" id="rm-xrp-recv">\u2014 received</div>
                    <div class="pt-note">\u26A1 3-5 seconds</div>
                  </div>
                </div>
                <div style="background:rgba(0,229,204,.08);border:1px solid rgba(0,229,204,.3);border-radius:6px;padding:10px;text-align:center;margin-top:8px">
                  <div class="pt-lbl" style="color:var(--tq)">XRP Saves You</div>
                  <div style="font-size:22px;font-weight:900;font-family:var(--mn);color:var(--tq)" id="rm-savings">\u2014</div>
                  <div class="pt-note" id="rm-xrp-needed">\u2014 XRP needed \u00B7 at live price</div>
                </div>
              </div>
              <div class="pt-note">\u26A0\uFE0F Traditional fees are averages. Actual rates vary by provider.</div>
            </div>
          </div>

          <!-- Break-Even / Target Price Calculator -->
          <div class="pt-panel" style="border-color:rgba(255,204,0,.25)">
            <div class="pt-head"><span class="pt-title" style="color:var(--yl)">\U0001F3AF Break-Even / Target Price</span><span class="pt-note">Solve for price, not profit</span></div>
            <div class="pt-body">
              <div class="pt-row2">
                <div><div class="pt-lbl">Buy Price (USD)</div>
                  <input id="bt-buy" class="pt-input" type="number" step="0.0001" placeholder="e.g. 0.50" oninput="calcBreakeven()"></div>
                <div><div class="pt-lbl">Quantity (XRP)</div>
                  <input id="bt-qty" class="pt-input" type="number" step="1" placeholder="e.g. 10000" oninput="calcBreakeven()"></div>
              </div>
              <div class="pt-row2">
                <div><div class="pt-lbl">Round-Trip Fee (%)</div>
                  <input id="bt-fee" class="pt-input" type="number" step="0.1" placeholder="e.g. 0.5" oninput="calcBreakeven()"></div>
                <div><div class="pt-lbl">Desired Return (%)</div>
                  <input id="bt-target" class="pt-input" type="number" step="1" placeholder="e.g. 50" oninput="calcBreakeven()"></div>
              </div>
              <div id="bt-results" class="pt-results" style="display:block">
                <div class="pt-res-row"><span class="sm-k">Break-Even Price</span><span class="sm-v" id="bt-breakeven">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">Target Price</span><span class="sm-v" id="bt-target-price">\u2014</span></div>
                <div class="pt-res-row"><span class="sm-k">Profit at Target</span><span id="bt-target-profit" style="font-weight:700;font-size:17px">\u2014</span></div>
              </div>
              <div class="pt-note">\u26A0\uFE0F Not financial advice. Fee % covers combined buy + sell exchange costs.</div>
            </div>
          </div>

        </div>
      </div>
    </div>

  <!-- MAIN -->
"""

    _B['exclusive'] = f"""    <!-- SECTION 30: XRP COMPLETE EXCLUSIVE INTELLIGENCE (flagship) -->
    <div class="acct" style="border-color:rgba(255,204,0,.4);margin:10px 0">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">
        <div class="sec-title" style="color:var(--hdr);margin:0"><span class="sic">\U0001F3C6</span> XRP Complete Exclusive Intelligence</div>
        <div style="font-size:12px;color:var(--tx);font-family:var(--mn);padding-top:4px">Live as of {flagship_ts}</div>
      </div>
      <div class="flagship-intro">
        Metrics built entirely from data we track ourselves \u2014 our own growing partnership ledger, our own executive
        statement archive, our own GitHub monitoring, our own news timing history. Nothing here is copied from another
        site's API; it exists because XRP Complete has been watching and recording since deploy.
        <ul class="flagship-list">
          <li><b style="color:var(--yl)">Institutional Confidence Index</b> \u2014 one flagship score from five disclosed components.</li>
          <li><b style="color:var(--bl)">Partnership Momentum</b> \u2014 deals-per-week velocity from our own ledger.</li>
          <li><b style="color:var(--or)">Catalyst Clock</b> \u2014 when XRP-moving stories actually break, by hour and weekday.</li>
          <li><b style="color:var(--tq)">Narrative Diffusion Map</b> \u2014 how fast a theme spreads across regions.</li>
        </ul>
        Every chart below started empty at deploy and has been filling in honestly ever since \u2014 the longer XRP Complete runs, the sharper this section gets.
      </div>

      <div class="ici-wrap">
        <div class="ici-dial">
          <div class="ici-score" style="color:{ici_color}">{ici_score}</div>
          <div class="ici-cap">/ 100</div>
          <div class="ici-label" style="color:{ici_color}">{ici_label}</div>
          <div class="ici-bar"><div class="ici-fill" style="width:{ici_score}%"></div></div>
        </div>
        <div class="ici-comps">
          {ici_comps_rendered}
        </div>
      </div>
      <div class="ici-foot">
        \U0001F3C6 XRP Complete Institutional Confidence Index (ICI) \u2014 rescaled from five disclosed components: Partnership
        Momentum (our Enterprise Ledger), Developer Activity (live GitHub tracking), Smart Money Positioning (RSI +
        sentiment + funding rate), Executive Tone (sentiment across real Ripple leadership statements), and Regulatory
        Momentum (CLARITY Act coverage + Legal/Reg news sentiment). Each component is shown above with its real
        underlying value \u2014 nothing is a black box. Informational only, not financial advice.
      </div>

      <div class="pm-panel">
        <div class="pm-title">\U0001F4C8 Partnership Momentum</div>
        <div class="pm-sub">New deals detected per week, straight from our own Enterprise Ledger \u2014 builds up day by day, nothing fabricated.</div>
        <div class="pm-stats">
          <div><div class="pm-stat-num" style="color:var(--yl)">{pm_total}</div><div class="pm-stat-lbl">Total Detected</div></div>
          <div><div class="pm-stat-num" style="color:var(--gr)">{pm_this_week}</div><div class="pm-stat-lbl">This Week</div></div>
          <div><div class="pm-stat-num" style="color:{pm_tcol};font-size:15px;padding-top:4px">{pm_trend}</div><div class="pm-stat-lbl">Trend</div></div>
          <div><div class="pm-stat-num" style="color:var(--bl)">{pm_avg}</div><div class="pm-stat-lbl">Avg / Week</div></div>
        </div>
        <div class="pm-chart">{pm_bars}</div>
        <div class="pm-axis"><span>10 weeks ago</span><span>5 weeks ago</span><span>this week</span></div>
      </div>

      <div class="cc-panel">
        <div class="cc-title">\u23F0 Catalyst Clock</div>
        <div class="cc-sub">When XRP-moving stories actually break \u2014 hour (UTC) \u00D7 weekday, built from our own breaking-story history since deploy.</div>
        <div class="cc-peak">Peak so far: <b>{cc_peak}</b> &nbsp;|&nbsp; {cc_total} breaking stories tracked</div>
        <div class="cc-grid">
          {cc_cells}
          <div class="cc-hourlbls">{cc_hourlbls}</div>
        </div>
        <div class="cc-scrollnote">Darker = more breaking stories at that hour \u00B7 scroll horizontally on small screens</div>
      </div>

      <div class="nd-panel">
        <div class="nd-title">\U0001F30D Narrative Diffusion Map</div>
        <div class="nd-sub">How fast a story theme spreads from its first mention to full regional coverage \u2014 tracked from our own news timing history.</div>
        <div class="nd-fastest">Fastest spread so far: <b>{nd_fastest}</b></div>
        <div class="nd-list">
          {nd_cards}
        </div>
      </div>
    </div>

"""

    _B['regledger'] = f"""  <!-- REGULATORY & LEDGER WATCH (V66) -->
    <div class="acct" style="border-color:rgba(0,229,204,.4);margin:10px 0">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">
        <div class="sec-title" style="color:var(--hdr);margin:0"><span class="sic">\U0001F4E1</span> Regulatory &amp; Ledger Watch</div>
        <div style="font-size:12px;color:var(--tx);font-family:var(--mn);padding-top:4px">Updated: {rw_updated}</div>
      </div>
      <div style="font-size:12px;color:var(--tx);margin-bottom:14px;line-height:1.6">
        Direct-from-source monitoring: XRPL protocol amendments in validator voting, official SEC filings mentioning Ripple/XRP, and live US federal rulemaking on digital assets. Government and ledger-level sources only.
      </div>
      <div class="rw-wrap">
        <div class="rw-panel">
          <div class="rw-panel-title">\u2699\uFE0F XRPL Amendment Tracker</div>
          <div class="rw-panel-sub">Protocol changes currently in validator voting \u2014 the earliest possible signal of XRPL evolution. Source: XRPScan.</div>
          {rw_amendments}
        </div>
        <div class="rw-panel">
          <div class="rw-panel-title">\U0001F4C4 SEC EDGAR Filing Watch</div>
          <div class="rw-panel-sub">Official SEC filings mentioning Ripple or XRP \u2014 straight from the source, before the press writes about them.</div>
          {rw_edgar}
        </div>
        <div class="rw-panel">
          <div class="rw-panel-title">\U0001F3DB\uFE0F Federal Register Rule Watch</div>
          <div class="rw-panel-sub">Proposed and final US federal rules on digital assets \u2014 the regulatory pipeline, direct from the Federal Register.</div>
          {rw_fedreg}
        </div>
      </div>
    </div>

"""

    _B['regnew'] = f"""  <!-- V119: SIX REGULATORY SECTIONS -->
    {_regnew}

"""

    _B['community'] = f"""  <!-- XRP COMMUNITY HUB (V67) -->
    <div class="acct" style="border-color:rgba(0,229,204,.4);margin:10px 0 40px 0">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px">
        <div class="sec-title" style="color:var(--hdr);margin:0"><span class="sic">\U0001F465</span> XRP Community Hub</div>
      </div>
      <div style="font-size:12px;color:var(--tx);margin-bottom:14px;line-height:1.6">
        The top 20 XRP-dedicated blogs, newsletters, social accounts, and forums \u2014 curated for signal over noise. External links open in a new tab.
      </div>
      <div class="cm-wrap">
        <div class="cm-panel">
          <div class="cm-panel-title">\U0001F4DD Blogs &amp; News Sites</div>
          <div class="cm-item"><a class="cm-link" href="https://u.today/xrp-news" target="_blank" rel="noopener">U.Today XRP</a><div class="cm-desc">High-volume dedicated XRP news desk</div></div>
          <div class="cm-item"><a class="cm-link" href="https://www.thecryptobasic.com/category/xrp-news/" target="_blank" rel="noopener">The Crypto Basic \u2014 XRP</a><div class="cm-desc">XRP-heavy coverage, community favorite</div></div>
          <div class="cm-item"><a class="cm-link" href="https://xrpl.org/blog/" target="_blank" rel="noopener">XRPL.org Blog</a><div class="cm-desc">Official ledger development blog</div></div>
          <div class="cm-item"><a class="cm-link" href="https://ripple.com/insights/" target="_blank" rel="noopener">Ripple Insights</a><div class="cm-desc">Official Ripple company blog</div></div>
          <div class="cm-item"><a class="cm-link" href="https://coinpost.jp/?s=XRP" target="_blank" rel="noopener">CoinPost Japan (XRP)</a><div class="cm-desc">Japan\u2019s largest crypto outlet \u2014 XRP focus</div></div>
        </div>
        <div class="cm-panel">
          <div class="cm-panel-title">\U0001F4E7 Newsletters &amp; Research</div>
          <div class="cm-item"><a class="cm-link" href="https://xrplf.org/" target="_blank" rel="noopener">XRPL Foundation Updates</a><div class="cm-desc">Ledger foundation announcements</div></div>
          <div class="cm-item"><a class="cm-link" href="https://dev.to/t/xrpl" target="_blank" rel="noopener">XRPL Dev Community</a><div class="cm-desc">Developer tutorials and build logs</div></div>
          <div class="cm-item"><a class="cm-link" href="https://xrpscan.com/" target="_blank" rel="noopener">XRPScan</a><div class="cm-desc">Ledger explorer + weekly metrics</div></div>
          <div class="cm-item"><a class="cm-link" href="https://bithomp.com/" target="_blank" rel="noopener">Bithomp</a><div class="cm-desc">Explorer, rich lists, escrow tracking</div></div>
          <div class="cm-item"><a class="cm-link" href="https://xrpl.services/" target="_blank" rel="noopener">XRPL Services</a><div class="cm-desc">Community tools and ledger utilities</div></div>
        </div>
        <div class="cm-panel">
          <div class="cm-panel-title">\U0001F4F1 Social Accounts</div>
          <div class="cm-item"><a class="cm-link" href="https://x.com/Ripple" target="_blank" rel="noopener">@Ripple</a><div class="cm-desc">Official Ripple company account</div></div>
          <div class="cm-item"><a class="cm-link" href="https://x.com/bgarlinghouse" target="_blank" rel="noopener">@bgarlinghouse</a><div class="cm-desc">Brad Garlinghouse \u2014 Ripple CEO</div></div>
          <div class="cm-item"><a class="cm-link" href="https://x.com/JoelKatz" target="_blank" rel="noopener">@JoelKatz</a><div class="cm-desc">David Schwartz \u2014 Ripple CTO, XRPL architect</div></div>
          <div class="cm-item"><a class="cm-link" href="https://x.com/XRPLF" target="_blank" rel="noopener">@XRPLF</a><div class="cm-desc">XRP Ledger Foundation</div></div>
          <div class="cm-item"><a class="cm-link" href="https://x.com/WietseWind" target="_blank" rel="noopener">@WietseWind</a><div class="cm-desc">Xaman (XUMM) wallet founder, XRPL builder</div></div>
        </div>
        <div class="cm-panel">
          <div class="cm-panel-title">\U0001F4AC Forums &amp; Communities</div>
          <div class="cm-item"><a class="cm-link" href="https://www.reddit.com/r/XRP/" target="_blank" rel="noopener">r/XRP</a><div class="cm-desc">Largest XRP subreddit</div></div>
          <div class="cm-item"><a class="cm-link" href="https://www.reddit.com/r/Ripple/" target="_blank" rel="noopener">r/Ripple</a><div class="cm-desc">Ripple company + ecosystem discussion</div></div>
          <div class="cm-item"><a class="cm-link" href="https://www.xrpchat.com/" target="_blank" rel="noopener">XRPChat</a><div class="cm-desc">Longest-running dedicated XRP forum</div></div>
          <div class="cm-item"><a class="cm-link" href="https://discord.com/invite/xrpl" target="_blank" rel="noopener">XRPL Developers Discord</a><div class="cm-desc">Official developer community chat</div></div>
          <div class="cm-item"><a class="cm-link" href="https://stackoverflow.com/questions/tagged/xrp" target="_blank" rel="noopener">Stack Overflow \u2014 XRP</a><div class="cm-desc">Technical Q&amp;A for XRPL builders</div></div>
        </div>
      </div>
    </div>

"""

    _B['dca'] = f"""    <!-- SECTION 23: DOLLAR COST AVERAGING CALCULATOR (V109) -->
    <div class="acct" style="border-color:rgba(0,229,204,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--tq)"><span class="sic">&#128176;</span> Dollar Cost Averaging Calculator</div>
      <div class="trk-tag" style="color:var(--tx)">Compare weekly vs. monthly contributions using {dca_days_available} days of real historical XRP prices \u2014 not a hypothetical curve.</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:12px 0">
        <div>
          <label style="font-size:13px;color:var(--tx);display:block;margin-bottom:4px">Weekly contribution ($)</label>
          <input id="dca-weekly" type="number" value="25" min="0" step="1" style="width:100%;background:var(--s2);border:1px solid var(--b);border-radius:6px;padding:8px 10px;color:var(--br);font-size:16px;font-family:var(--mn)">
        </div>
        <div>
          <label style="font-size:13px;color:var(--tx);display:block;margin-bottom:4px">Monthly contribution ($)</label>
          <input id="dca-monthly" type="number" value="100" min="0" step="1" style="width:100%;background:var(--s2);border:1px solid var(--b);border-radius:6px;padding:8px 10px;color:var(--br);font-size:16px;font-family:var(--mn)">
        </div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
        <div style="background:var(--s1);border:1px solid rgba(0,229,204,.3);border-radius:8px;padding:14px">
          <div style="color:var(--tq);font-weight:700;font-size:15px;margin-bottom:8px">Weekly Plan</div>
          <div class="dca-row"><span>Total Invested</span><span id="dca-w-invested">$0.00</span></div>
          <div class="dca-row"><span>XRP Acquired</span><span id="dca-w-xrp">0 XRP</span></div>
          <div class="dca-row"><span>Avg Cost / XRP</span><span id="dca-w-avgcost">$0.00</span></div>
          <div class="dca-row"><span>Current Value</span><span id="dca-w-value">$0.00</span></div>
          <div class="dca-row" style="border-top:1px solid var(--b);padding-top:6px;margin-top:6px"><span style="font-weight:700">Return</span><span id="dca-w-return" style="font-weight:700">$0.00</span></div>
        </div>
        <div style="background:var(--s1);border:1px solid rgba(0,229,204,.3);border-radius:8px;padding:14px">
          <div style="color:var(--tq);font-weight:700;font-size:15px;margin-bottom:8px">Monthly Plan</div>
          <div class="dca-row"><span>Total Invested</span><span id="dca-m-invested">$0.00</span></div>
          <div class="dca-row"><span>XRP Acquired</span><span id="dca-m-xrp">0 XRP</span></div>
          <div class="dca-row"><span>Avg Cost / XRP</span><span id="dca-m-avgcost">$0.00</span></div>
          <div class="dca-row"><span>Current Value</span><span id="dca-m-value">$0.00</span></div>
          <div class="dca-row" style="border-top:1px solid var(--b);padding-top:6px;margin-top:6px"><span style="font-weight:700">Return</span><span id="dca-m-return" style="font-weight:700">$0.00</span></div>
        </div>
      </div>
      <div style="font-size:11px;color:var(--tx);margin-top:10px;font-style:italic">Simulated using real daily close prices over the available history window. Not financial advice \u2014 past performance does not predict future results.</div>
    </div>

"""

    _B['hist30'] = f"""    <!-- SECTION 24: 30-DAY HISTORICAL PRICE DATA (V109) -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">&#128197;</span> 30-Day Historical Price Data</div>
      <div class="trk-tag" style="color:var(--tx)">Daily OHLC, newest first. Same live Coinbase feed powering RSI and 52-week range above.</div>
      {hist30_html}
    </div>

"""

    _B['nmv'] = f"""    <!-- SECTION 25: NEWS MENTION VOLUME (V109) -->
    <div class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--yl)"><span class="sic">&#128240;</span> News Mention Volume <span style="font-weight:400;color:var(--tx);font-size:14px">({nmv_day_label})</span></div>
      <div class="trk-tag" style="color:var(--tx)">Real story counts across the {hdr_feeds_total} RSS sources this site already tracks \u2014 never estimated. Locks in at 00:15 UTC each day.</div>
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:12px 0">
        <div style="background:var(--s1);border:1px solid rgba(255,204,0,.3);border-radius:8px;padding:12px;text-align:center">
          <div style="font-size:28px;font-weight:900;color:var(--yl);font-family:var(--mn)">{nmv_total}</div>
          <div style="font-size:12px;color:var(--tx)">total stories, aggregated</div>
        </div>
        <div style="background:var(--s1);border:1px solid rgba(255,204,0,.3);border-radius:8px;padding:12px;text-align:center">
          <div style="font-size:28px;font-weight:900;color:var(--yl);font-family:var(--mn)">{nmv_contributors}</div>
          <div style="font-size:12px;color:var(--tx)">contributing sources</div>
        </div>
      </div>
      <div>{nmv_cat_html}</div>
    </div>
"""

    _ORDER = {'main': ['status', 'liquidity', 'onchain', 'ecosystem', 'mainstream', 'tradfi', 'brief', 'competitive', 'regradar', 'clarity', 'enterprise', 'advmetrics', 'regledger'], 'markets': ['rsi', 'chart', 'analytics', 'longitudinal', 'practical', 'dca', 'hist30'], 'institutional': ['instpart', 'execdev', 'exclusive'], 'news': ['top20', 'usintel', 'regdisc', 'newsfeed', 'clocks', 'heatmap', 'sentiment', 'nmv'], 'community': ['scoreboard', 'leaderboard', 'unique', 'community'], 'regulatory': ['regnew']}

    _body = "".join(_B[k] for k in _ORDER.get(page, _ORDER["main"]))

    _tail = f"""    

  </div>

    <script>
      window.__DCA_HIST_DATA__ = {dca_history_json};
function dcaCalculate() {{
  var weeklyAmt = parseFloat(document.getElementById('dca-weekly').value) || 0;
  var monthlyAmt = parseFloat(document.getElementById('dca-monthly').value) || 0;
  var hist = window.__DCA_HIST_DATA__ || [];
  if (hist.length < 2) return;

  var currentPrice = hist[hist.length - 1].c;
  var startT = hist[0].t;

  function priceNear(targetT) {{
    var best = hist[0];
    for (var i = 0; i < hist.length; i++) {{
      if (hist[i].t <= targetT) {{ best = hist[i]; }} else {{ break; }}
    }}
    return best.c;
  }}

  function simulate(amount, intervalDays) {{
    if (amount <= 0) return {{ invested: 0, xrp: 0 }};
    var invested = 0, xrp = 0;
    var stepSeconds = intervalDays * 86400;
    var t = startT;
    var lastT = hist[hist.length - 1].t;
    while (t <= lastT) {{
      var p = priceNear(t);
      if (p > 0) {{ xrp += amount / p; invested += amount; }}
      t += stepSeconds;
    }}
    return {{ invested: invested, xrp: xrp }};
  }}

  var weekly = simulate(weeklyAmt, 7);
  var monthly = simulate(monthlyAmt, 30);

  function render(prefix, result) {{
    var value = result.xrp * currentPrice;
    var ret = value - result.invested;
    var retPct = result.invested > 0 ? (ret / result.invested * 100) : 0;
    var avgCost = result.xrp > 0 ? (result.invested / result.xrp) : 0;
    document.getElementById(prefix + '-invested').textContent = '$' + result.invested.toLocaleString(undefined, {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
    document.getElementById(prefix + '-xrp').textContent = result.xrp.toLocaleString(undefined, {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' XRP';
    document.getElementById(prefix + '-avgcost').textContent = '$' + avgCost.toFixed(4);
    document.getElementById(prefix + '-value').textContent = '$' + value.toLocaleString(undefined, {{minimumFractionDigits: 2, maximumFractionDigits: 2}});
    var retEl = document.getElementById(prefix + '-return');
    var sign = ret >= 0 ? '+' : '';
    retEl.textContent = sign + '$' + ret.toLocaleString(undefined, {{minimumFractionDigits: 2, maximumFractionDigits: 2}}) + ' (' + sign + retPct.toFixed(2) + '%)';
    retEl.style.color = ret >= 0 ? 'var(--gr)' : 'var(--rd)';
  }}

  render('dca-w', weekly);
  render('dca-m', monthly);
}}

document.addEventListener('DOMContentLoaded', function() {{
  var wInput = document.getElementById('dca-weekly');
  var mInput = document.getElementById('dca-monthly');
  if (wInput) wInput.addEventListener('input', dcaCalculate);
  if (mInput) mInput.addEventListener('input', dcaCalculate);
  dcaCalculate();
}});
    </script>

  <!-- FLOATING RETURN / BACK-TO-TOP -->
  <button id="back-to-top" title="Return to XRP Complete" aria-label="Return to XRP Complete">&#8679;</button>

  <!-- FOOTER -->
  <footer>
    <div class="f-line">
      <img class="f-helix" src="/logo.jpg" alt=""> <em class="brand-em">{APP_NAME}</em>
      &nbsp;|&nbsp; Version: <span class="val">{APP_VERSION}</span>
      &nbsp;|&nbsp; Updated: <span class="val" id="ft-last">{boot_str}</span>
      &nbsp;|&nbsp; Uptime: <span class="val" id="ft-uptime">0s</span>
      <a class="footer-btn debug-btn" href="/debug" target="_blank" rel="noopener">DEBUG</a>
    </div>
    <div class="f-line notice">
      \u26A0\uFE0F Not Financial Advice \u2014 XRP Complete is for informational purposes only. DYOR.
    </div>
    <div class="f-line">
      Feeds: <span class="val" id="ft-feeds">{NEWS["feeds_active"]}/{NEWS["feeds_total"]}</span>
      &nbsp;|&nbsp; Maintenance: <span class="val" id="ft-maint">None</span>
      &nbsp;|&nbsp; Preflight: <span style="color:{overall_color};font-weight:800" id="ft-qa">{overall}</span>
      <button class="footer-btn details-btn" onclick="openPFModal()">\U0001F50D DETAILS</button>
    </div>
    <div class="f-line copyright">{COPYRIGHT}</div>
  </footer>

  <!-- PREFLIGHT DETAILS MODAL -->
  <div id="pf-modal" onclick="closePFModal(event)">
    <div id="pf-box" onclick="event.stopPropagation()">
      <div class="pf-head">
        <span class="t">\U0001F50D Preflight / QA Details</span>
        <span class="x" onclick="closePFModal()">\u2715</span>
      </div>
      <div class="pf-body">
        <div class="pf-overall">OVERALL: {overall} &nbsp;({passed}/{total} checks passed)</div>
        {modal_rows}
        <div style="margin-top:10px;color:var(--tx);font-size:12px">Last run: {boot_str}</div>
      </div>
    </div>
  </div>

  <script>
    (function () {{
      var bootMs = {int(BOOT_TIME.timestamp() * 1000)};
      var el = document.getElementById('ft-uptime');
      function tick() {{
        if (!el) return;
        var s = Math.floor((Date.now() - bootMs) / 1000);
        var h = Math.floor(s / 3600), m = Math.floor((s % 3600) / 60), sec = s % 60;
        el.textContent = (h ? h + 'h ' : '') + (m ? m + 'm ' : '') + sec + 's';
      }}
      tick(); setInterval(tick, 1000);
    }})();

    function openPFModal() {{ var m = document.getElementById('pf-modal'); if (m) m.style.display = 'flex'; }}
    function closePFModal() {{ var m = document.getElementById('pf-modal'); if (m) m.style.display = 'none'; }}
    document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') closePFModal(); }});

    // XRP Intelligence Brief — This Week's Editions (client-side swap, never reloads)
    var briefLiveSlot = {json.dumps(_live_slot)};
    var brfNextGlobal = {json.dumps(brf_next)};
    var briefArchive = {{}};
    try {{
      var _bd = document.getElementById('brief-archive-data');
      briefArchive = _bd ? JSON.parse(_bd.textContent) : {{}};
    }} catch (e) {{ briefArchive = {{}}; }}

    // Single-edition mode: only the current brief is shown (rendered server-side).
    // No edition switching, so no client-side brief loader is needed.

    // Practical Tools — client-side calculators (never block the page load)
    var currentXRPPrice = {xrp_price_js};

    function calcPL() {{
      var buy = parseFloat((document.getElementById('pl-buy') || {{}}).value || 0);
      var qty = parseFloat((document.getElementById('pl-qty') || {{}}).value || 0);
      var sell = parseFloat((document.getElementById('pl-sell') || {{}}).value || 0);
      var res = document.getElementById('pl-results');
      if (!buy || !qty || !sell || !res) return;
      var cost = buy * qty, value = sell * qty, plUSD = value - cost;
      var plPct = ((sell - buy) / buy) * 100;
      var isPos = plUSD >= 0, col = isPos ? 'var(--gr)' : 'var(--rd)', sign = isPos ? '+' : '';
      res.style.display = 'block';
      document.getElementById('pl-cost').textContent = '$' + cost.toLocaleString('en-US', {{minimumFractionDigits:2,maximumFractionDigits:2}});
      document.getElementById('pl-value').textContent = '$' + value.toLocaleString('en-US', {{minimumFractionDigits:2,maximumFractionDigits:2}});
      var u = document.getElementById('pl-usd');
      u.textContent = sign + '$' + Math.abs(plUSD).toLocaleString('en-US', {{minimumFractionDigits:2,maximumFractionDigits:2}});
      u.style.color = col;
      var p = document.getElementById('pl-pct');
      p.textContent = sign + plPct.toFixed(2) + '%';
      p.style.color = col;
    }}

    var portfolioEntries = [];
    function addPortfolioEntry() {{
      var label = ((document.getElementById('pt-label') || {{}}).value || '').trim() || ('Entry ' + (portfolioEntries.length + 1));
      var amount = parseFloat((document.getElementById('pt-amount') || {{}}).value || 0);
      var cost = parseFloat((document.getElementById('pt-cost') || {{}}).value || 0);
      if (!amount || amount <= 0) {{ alert('Enter a valid XRP amount'); return; }}
      portfolioEntries.push({{label: label, amount: amount, cost: cost, id: Date.now()}});
      ['pt-label', 'pt-amount', 'pt-cost'].forEach(function(id) {{
        var el = document.getElementById(id); if (el) el.value = '';
      }});
      renderPortfolio();
    }}
    function removePortfolioEntry(id) {{
      portfolioEntries = portfolioEntries.filter(function(e) {{ return e.id !== id; }});
      renderPortfolio();
    }}
    function renderPortfolio() {{
      var tableEl = document.getElementById('portfolio-table');
      var totalsEl = document.getElementById('portfolio-totals');
      if (!tableEl) return;
      if (!portfolioEntries.length) {{
        tableEl.innerHTML = '<div style="font-size:15px;font-family:var(--mn);color:var(--tx)">No entries yet. Add a position above.</div>';
        if (totalsEl) totalsEl.style.display = 'none';
        return;
      }}
      var totalXRP = 0, totalVal = 0, totalCost = 0;
      var rows = '';
      for (var i = 0; i < portfolioEntries.length; i++) {{
        var e = portfolioEntries[i];
        var val = e.amount * currentXRPPrice, cost = e.cost * e.amount, pl = val - cost;
        var pct = e.cost > 0 ? ((currentXRPPrice - e.cost) / e.cost * 100) : 0;
        var col = pl >= 0 ? 'var(--gr)' : 'var(--rd)', sign = pl >= 0 ? '+' : '';
        totalXRP += e.amount; totalVal += val; totalCost += cost;
        rows += '<tr><td>' + e.label + '</td><td>' + e.amount.toLocaleString() + '</td>' +
          '<td>$' + e.cost.toFixed(4) + '</td>' +
          '<td style="color:var(--bl);font-weight:700">$' + val.toLocaleString(undefined,{{minimumFractionDigits:2,maximumFractionDigits:2}}) + '</td>' +
          '<td style="color:' + col + ';font-weight:700">' + sign + '$' + Math.abs(pl).toLocaleString(undefined,{{minimumFractionDigits:2,maximumFractionDigits:2}}) + '</td>' +
          '<td style="color:' + col + '">' + sign + pct.toFixed(1) + '%</td>' +
          '<td><span class="pt-x" onclick="removePortfolioEntry(' + e.id + ')">\u2715</span></td></tr>';
      }}
      tableEl.innerHTML = '<table class="pt-tbl"><thead><tr><th>Label</th><th>XRP</th><th>Buy $</th><th>Value</th><th>P&amp;L</th><th>%</th><th></th></tr></thead><tbody>' + rows + '</tbody></table>';
      var totalPL = totalVal - totalCost;
      var tCol = totalPL >= 0 ? 'var(--gr)' : 'var(--rd)', tSign = totalPL >= 0 ? '+' : '';
      document.getElementById('pt-total-xrp').textContent = totalXRP.toLocaleString();
      document.getElementById('pt-total-val').textContent = '$' + totalVal.toLocaleString(undefined,{{minimumFractionDigits:2,maximumFractionDigits:2}});
      var tplEl = document.getElementById('pt-total-pl');
      tplEl.textContent = tSign + '$' + Math.abs(totalPL).toLocaleString(undefined,{{minimumFractionDigits:2,maximumFractionDigits:2}});
      tplEl.style.color = tCol;
      if (totalsEl) totalsEl.style.display = 'block';
    }}

    function calcRemittance() {{
      var amount = parseFloat((document.getElementById('rm-amount') || {{}}).value || 0);
      var corridor = parseFloat((document.getElementById('rm-corridor') || {{}}).value || 6.0);
      var res = document.getElementById('rm-results');
      if (!amount || amount <= 0 || !res) return;
      var swiftFee = amount * (corridor / 100), swiftRecv = amount - swiftFee;
      var xrpFee = 0.0002, xrpRecv = amount - xrpFee, savings = swiftFee - xrpFee;
      var xrpNeeded = currentXRPPrice > 0 ? (amount / currentXRPPrice).toFixed(2) : '--';
      var fmt = function(v) {{ return '$' + v.toLocaleString('en-US', {{minimumFractionDigits:2,maximumFractionDigits:2}}); }};
      document.getElementById('rm-swift-fee').textContent = fmt(swiftFee);
      document.getElementById('rm-swift-recv').textContent = fmt(swiftRecv) + ' received';
      document.getElementById('rm-xrp-recv').textContent = fmt(xrpRecv) + ' received';
      document.getElementById('rm-savings').textContent = fmt(savings);
      document.getElementById('rm-xrp-needed').textContent = xrpNeeded + ' XRP needed \u00B7 at live price';
      res.style.display = 'block';
    }}

    // Break-Even / Target Price Calculator — pure client-side math, no network calls
    function calcBreakeven() {{
      var buy = parseFloat((document.getElementById('bt-buy') || {{}}).value || 0);
      var qty = parseFloat((document.getElementById('bt-qty') || {{}}).value || 0);
      var feePct = parseFloat((document.getElementById('bt-fee') || {{}}).value || 0);
      var targetPct = parseFloat((document.getElementById('bt-target') || {{}}).value || 0);
      var beEl = document.getElementById('bt-breakeven');
      var tpEl = document.getElementById('bt-target-price');
      var profEl = document.getElementById('bt-target-profit');
      if (!buy || buy <= 0) {{
        if (beEl) beEl.textContent = '\u2014';
        if (tpEl) tpEl.textContent = '\u2014';
        if (profEl) profEl.textContent = '\u2014';
        return;
      }}
      var fee = feePct / 100;
      var breakeven = (fee > 0 && fee < 1) ? (buy * (1 + fee)) / (1 - fee) : buy;
      var hasTarget = targetPct !== 0 && !isNaN(targetPct);
      var targetPrice = hasTarget ? buy * (1 + targetPct / 100) : null;
      if (beEl) beEl.textContent = '$' + breakeven.toFixed(4);
      if (tpEl) tpEl.textContent = targetPrice !== null ? '$' + targetPrice.toFixed(4) : '\u2014';
      if (profEl) {{
        if (targetPrice !== null && qty > 0) {{
          var profit = (targetPrice - buy) * qty;
          profEl.textContent = '$' + profit.toLocaleString('en-US', {{minimumFractionDigits:2,maximumFractionDigits:2}});
          profEl.style.color = profit >= 0 ? 'var(--gr)' : 'var(--rd)';
        }} else {{
          profEl.textContent = '\u2014';
          profEl.style.color = 'var(--br)';
        }}
      }}
    }}
    function wcTick() {{
      var now = new Date();
      var clocks = document.querySelectorAll('.wc-clock');
      for (var i = 0; i < clocks.length; i++) {{
        var el = clocks[i];
        var tz = el.getAttribute('data-tz');
        var hh = 0, mm = 0, ss = now.getSeconds();
        try {{
          var parts = new Intl.DateTimeFormat('en-GB', {{
            timeZone: tz, hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
          }}).formatToParts(now);
          for (var j = 0; j < parts.length; j++) {{
            if (parts[j].type === 'hour') hh = parseInt(parts[j].value, 10);
            else if (parts[j].type === 'minute') mm = parseInt(parts[j].value, 10);
            else if (parts[j].type === 'second') ss = parseInt(parts[j].value, 10);
          }}
          if (hh === 24) hh = 0;
        }} catch (e) {{ hh = now.getUTCHours(); mm = now.getUTCMinutes(); }}
        var day = (hh >= 6 && hh < 18);
        el.classList.toggle('wc-day', day);
        var hr = el.querySelector('.wc-hr'), mn = el.querySelector('.wc-min'), sc = el.querySelector('.wc-sec');
        if (hr) hr.style.transform = 'rotate(' + (((hh % 12) * 30) + (mm * 0.5)) + 'deg)';
        if (mn) mn.style.transform = 'rotate(' + (mm * 6) + 'deg)';
        if (sc) sc.style.transform = 'rotate(' + (ss * 6) + 'deg)';
      }}
    }}
    setInterval(wcTick, 1000);
    wcTick();

    // Partnership Tracker status filter (Mainstream Integration Monitor buttons)
    function filterTracker(status, btn) {{
      var cards = document.querySelectorAll('.trk-card');
      var visible = 0;
      for (var i = 0; i < cards.length; i++) {{
        var show = (status === 'ALL' || cards[i].getAttribute('data-status') === status);
        cards[i].style.display = show ? '' : 'none';
        if (show) visible++;
      }}
      var empty = document.getElementById('trk-empty');
      if (empty) empty.style.display = (visible === 0) ? 'block' : 'none';
      var btns = document.querySelectorAll('.trk-btn');
      for (var j = 0; j < btns.length; j++) btns[j].classList.remove('active');
      if (btn) btn.classList.add('active');
    }}

    // Global News Feed — search + category filter (client-side, never blocks)
    var _feedCat = 'ALL';
    function _applyFeed() {{
      var q = (document.getElementById('gn-search') || {{}}).value || '';
      q = q.toLowerCase().trim();
      var cards = document.querySelectorAll('#gn-list .gn-card');
      var shown = 0;
      for (var i = 0; i < cards.length; i++) {{
        var okCat = (_feedCat === 'ALL') || (cards[i].getAttribute('data-cat') === _feedCat);
        var okQ = !q || (cards[i].getAttribute('data-text') || '').indexOf(q) !== -1;
        var vis = okCat && okQ;
        cards[i].style.display = vis ? '' : 'none';
        if (vis) shown++;
      }}
      var sh = document.getElementById('gn-shown'); if (sh) sh.textContent = shown;
      var em = document.getElementById('gn-empty'); if (em) em.style.display = shown === 0 ? 'block' : 'none';
    }}
    function filterFeed() {{ _applyFeed(); }}
    function feedCat(cat, btn) {{
      _feedCat = cat;
      var btns = document.querySelectorAll('#gn-cats .gn-btn');
      for (var j = 0; j < btns.length; j++) btns[j].classList.remove('active');
      if (btn) btn.classList.add('active');
      _applyFeed();
    }}

    // Ripple Exec Tracker — tab filter (client-side, never blocks)
    function execTab(tab, btn) {{
      var rows = document.querySelectorAll('#ex-feed .ex-row');
      for (var i = 0; i < rows.length; i++) {{
        rows[i].style.display = (tab === 'ALL' || rows[i].getAttribute('data-tab') === tab) ? '' : 'none';
      }}
      var tabs = document.querySelectorAll('#ex-tabs .ex-tab');
      for (var j = 0; j < tabs.length; j++) tabs[j].classList.remove('on');
      if (btn) btn.classList.add('on');
    }}

    // Global XRP Enterprise & Partnership Ledger — search + category filter
    var _plCat = 'ALL';
    function _applyPl() {{
      var q = ((document.getElementById('pl-search') || {{}}).value || '').toLowerCase().trim();
      var rows = document.querySelectorAll('#pl-list .pl-row');
      var shown = 0;
      for (var i = 0; i < rows.length; i++) {{
        var okCat = (_plCat === 'ALL') || (rows[i].getAttribute('data-cat') === _plCat);
        var okQ = !q || (rows[i].getAttribute('data-text') || '').indexOf(q) !== -1;
        var vis = okCat && okQ;
        rows[i].style.display = vis ? '' : 'none';
        if (vis) shown++;
      }}
      var sh = document.getElementById('pl-shown'); if (sh) sh.textContent = shown;
    }}
    function filterPartnerships() {{ _applyPl(); }}
    function plCat(cat, btn) {{
      _plCat = cat;
      var btns = document.querySelectorAll('#pl-cats .pl-btn');
      for (var j = 0; j < btns.length; j++) btns[j].classList.remove('active');
      if (btn) btn.classList.add('active');
      _applyPl();
    }}

    // Next Briefing countdown (ticks live, hours/minutes)
    (function () {{
      var target = new Date("{brf_next_iso}").getTime();
      var el = document.getElementById('brf-countdown');
      function tickBrf() {{
        if (!el) return;
        var diff = target - Date.now();
        if (diff < 0) diff = 0;
        var h = Math.floor(diff / 3600000);
        var m = Math.floor((diff % 3600000) / 60000);
        el.textContent = h + 'h ' + ('0' + m).slice(-2) + 'm';
      }}
      tickBrf(); setInterval(tickBrf, 1000 * 15);
    }})();

    // Escrow countdown (to next 1st-of-month, 00:00 UTC)
    (function () {{
      var target = new Date("{esc_iso}").getTime();
      function tickEsc() {{
        var diff = target - Date.now();
        if (diff < 0) diff = 0;
        var d = Math.floor(diff / 86400000);
        var h = Math.floor((diff % 86400000) / 3600000);
        var m = Math.floor((diff % 3600000) / 60000);
        var ds = document.getElementById('esc-days');
        var hs = document.getElementById('esc-hrs');
        var ms = document.getElementById('esc-min');
        if (ds) ds.textContent = d;
        if (hs) hs.textContent = ('0' + h).slice(-2);
        if (ms) ms.textContent = ('0' + m).slice(-2);
      }}
      tickEsc(); setInterval(tickEsc, 1000 * 30);
    }})();

    // Practical Tools escrow countdown (same target time, separate display)
    (function () {{
      var el = document.getElementById('esc-countdown');
      if (!el) return;
      var target = new Date(el.getAttribute('data-eta')).getTime();
      function tick() {{
        var diff = target - Date.now();
        if (diff < 0) diff = 0;
        var d = Math.floor(diff / 86400000);
        var h = Math.floor((diff % 86400000) / 3600000);
        var m = Math.floor((diff % 3600000) / 60000);
        el.textContent = d + 'd ' + ('0'+h).slice(-2) + 'h ' + ('0'+m).slice(-2) + 'm';
      }}
      tick(); setInterval(tick, 1000 * 30);
    }})();

    (function () {{
      var btn = document.getElementById('back-to-top'); if (!btn) return;
      function toggle() {{ btn.style.display = (window.scrollY > 120 || document.documentElement.scrollTop > 120) ? 'flex' : 'none'; }}
      window.addEventListener('scroll', toggle, {{ passive:true }});
      document.addEventListener('scroll', toggle, {{ passive:true }});
      window.addEventListener('pageshow', toggle);       // fires on back/forward-cache restore (mobile Safari, etc.)
      document.addEventListener('visibilitychange', function () {{ if (!document.hidden) toggle(); }});
      btn.addEventListener('click', function () {{ window.scrollTo({{ top:0, behavior:'smooth' }}); }});
      toggle();
      setTimeout(toggle, 400);   // safety re-check after late layout shifts (widgets, images loading)
      setInterval(toggle, 2000); // low-frequency safety net in case a scroll event is ever missed
    }})();
  </script>

</body>
</html>"""

    return _head + _chrome + _body + _tail



# ─────────────────────────────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────────────────────────────
@app.route("/")
def home():
    return Response(replace_flags_with_svg(render_page("main")), mimetype="text/html")


@app.route("/markets")
def page_markets():
    return Response(replace_flags_with_svg(render_page("markets")), mimetype="text/html")


@app.route("/news")
def page_news():
    return Response(replace_flags_with_svg(render_page("news")), mimetype="text/html")


@app.route("/institutional")
def page_institutional():
    return Response(replace_flags_with_svg(render_page("institutional")), mimetype="text/html")


@app.route("/regulatory")
def page_regulatory():
    return Response(replace_flags_with_svg(render_page("regulatory")), mimetype="text/html")


@app.route("/community")
def page_community():
    return Response(replace_flags_with_svg(render_page("community")), mimetype="text/html")


@app.route("/logo.jpg")
def logo_jpg():
    """The helix, served as embedded."""
    return Response(LOGO_BYTES, mimetype="image/jpeg",
                    headers={"Cache-Control": "public, max-age=86400"})


@app.route("/blog_ad.png")
def blog_ad_png():
    """Header blog advertisement (V123), served as embedded."""
    return Response(BLOG_AD_BYTES, mimetype="image/png",
                    headers={"Cache-Control": "public, max-age=86400"})


@app.route("/about")
def about_us():
    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>About Us — XRP Complete</title>
<meta name="description" content="About XRP Complete and Red Rio Ventures, LLC — our mission, our commitment to user safety, and what this site does and does not do.">
<style>
  :root{{ --bg:#0a0e1a; --s1:#0f1526; --hdr:#03b1fc; --tq:#00e5cc; --tx:#a8bdd0; --br:#e8eef5; --b:#1e2a42; --or:#CC5F00; }}
  *{{ box-sizing:border-box; }}
  body{{ background:var(--bg); color:var(--br); font-family:system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; margin:0; padding:0; line-height:1.7; }}
  .w{{ max-width:900px; margin:0 auto; padding:40px 24px 80px; }}
  .back-link{{ display:inline-block; margin-bottom:24px; color:var(--hdr); text-decoration:none; font-size:14px; font-weight:600; }}
  .back-link:hover{{ text-decoration:underline; }}
  h1{{ color:var(--hdr); font-size:32px; margin:0 0 8px; }}
  .tagline{{ color:var(--tx); font-size:15px; margin-bottom:36px; }}
  h2{{ color:var(--tq); font-size:20px; margin:36px 0 12px; border-bottom:1px solid var(--b); padding-bottom:8px; }}
  p{{ font-size:15px; color:var(--br); margin:0 0 14px; }}
  .promise-box{{ background:var(--s1); border:2px solid var(--or); border-radius:10px; padding:22px 24px; margin:16px 0; }}
  .promise-box h2{{ margin-top:0; border:none; color:var(--or); }}
  .promise-list{{ margin:12px 0; padding-left:0; list-style:none; }}
  .promise-list li{{ padding:6px 0 6px 28px; position:relative; font-size:15px; }}
  .promise-list li:before{{ content:"\2713"; position:absolute; left:0; color:var(--tq); font-weight:700; }}
  .fine-print{{ font-size:12.5px; color:var(--tx); margin-top:40px; padding-top:20px; border-top:1px solid var(--b); }}
  .contact-box{{ background:var(--s1); border:1px solid var(--b); border-radius:8px; padding:18px 20px; margin-top:8px; }}
</style>
</head>
<body>
<div class="w">
  <a href="/" class="back-link">&larr; Back to XRP Complete</a>
  <h1>About Us</h1>
  <div class="tagline">XRP Complete &middot; Operated by Red Rio Ventures, LLC</div>

  <h2>About Red Rio Ventures, LLC</h2>
  <p>Red Rio Ventures, LLC is an independent, privately held company focused on building informational
  and educational tools for the cryptocurrency community. XRP Complete is our flagship product: a free,
  publicly accessible dashboard that aggregates live market data, news, and publicly available
  research related to XRP and the broader Ripple ecosystem.</p>
  <p>We are not a financial institution, exchange, broker-dealer, or custodian. We do not manage funds,
  execute trades, or provide investment advisory services of any kind.</p>

  <h2>Our Mission</h2>
  <p><strong>In the United States:</strong> XRP Complete exists to give everyday individuals &mdash; from
  first-time crypto observers to experienced traders &mdash; free, centralized access to the same
  caliber of real-time market data, regulatory tracking, and news synthesis that was once scattered
  across dozens of paid tools and specialist forums. We believe informed participation in emerging
  financial technology should not require a subscription or a finance degree.</p>
  <p><strong>Globally:</strong> XRP and the XRP Ledger are used and discussed far beyond U.S. borders.
  XRP Complete tracks regional adoption, partnerships, and regulatory developments across multiple
  geographies specifically so that our global audience is not limited to a U.S.-centric view of a
  worldwide technology. Our goal is to be a genuinely international resource, not a regional one with
  an international-sounding name.</p>

  <div class="promise-box">
    <h2>Our Patron Promise</h2>
    <p style="font-weight:600;color:var(--br);margin-bottom:14px">We will NEVER ask you for your wallet address,
    private keys, seed phrase, banking information, or any financial account credentials &mdash; for any reason,
    at any time, through any part of this site.</p>
    <ul class="promise-list">
      <li>XRP Complete is a read-only information and education site. There is nothing to log into, nothing to
      connect, and no wallet to link.</li>
      <li>We will never send you a message, pop-up, or email asking you to "verify," "connect," or "confirm"
      a wallet or account.</li>
      <li>Every calculator and tool on this site runs entirely in your own browser. Nothing you type into a
      calculator is transmitted, stored, or seen by us.</li>
      <li>If you ever encounter a page, email, or message claiming to be XRP Complete that asks for financial
      credentials, it is not us, and we encourage you to disregard it.</li>
    </ul>
  </div>

  <h2>What This Site Is</h2>
  <p>XRP Complete is an aggregation and educational dashboard. We compile publicly available news, publicly
  available market data from third-party sources (with attribution), and original written analysis. All
  content is provided for informational and educational purposes only and does not constitute financial,
  investment, legal, or tax advice. Cryptocurrency markets are volatile and carry substantial risk;
  always do your own research and consult a licensed professional before making financial decisions.</p>

  <h2>What This Site Is Not</h2>
  <p>XRP Complete does not offer wallet services, custody of any kind, trading execution, account creation,
  deposits, withdrawals, or any function that would require a visitor to share personal financial
  information. We do not sell financial products. We do not offer ads that promote financial products
  on behalf of third parties.</p>

  <h2>Contact</h2>
  <div class="contact-box">
    <p style="margin:0">Red Rio Ventures, LLC<br>
    Operating XRPComplete.com<br>
    For inquiries regarding this site, please reach out through the contact channel listed on our
    primary domain.</p>
  </div>

  <div class="fine-print">
    &copy; 2026 XRP Complete / Red Rio Ventures, LLC. All rights reserved globally. XRP Complete is an independent
    informational service and is not affiliated with, endorsed by, or sponsored by Ripple Labs Inc.
    or the XRP Ledger Foundation. XRP and related marks are property of their respective owners.
  </div>
</div>
</body>
</html>"""
    return Response(html_out, mimetype="text/html")


@app.route("/ping")
def ping():
    return jsonify({"status": "ok", "version": APP_VERSION})


# ─────────────────────────────────────────────────────────────────────
# COPYRIGHT ARCHIVE — PERMANENT, DO NOT MODIFY OR REMOVE THIS ROUTE.
# Serves a static, pre-rendered HTML snapshot captured July 4, 2026 (V56)
# for copyright documentation. This route must NEVER call render_page()
# or reference any live MARKET/NEWS/etc. data. It reads one static file
# and returns it verbatim, unchanged, regardless of any future edits
# made elsewhere in this app. Not linked from any nav/footer. Hidden via
# noindex meta tag (baked into the file itself) and via robots.txt below.
# ─────────────────────────────────────────────────────────────────────
_COPYRIGHT_ARCHIVE_FILE = "copyright_archive_2026_07_04.html"
_COPYRIGHT_ARCHIVE_FILE_B = "copyright_archive_2026_07_07_b.html"
_COPYRIGHT_ARCHIVE_FILE_C = "copyright_archive_2026_07_12_c.html"

@app.route("/copyright7_26")
def copyright_archive_2026_07_04():
    try:
        with open(_COPYRIGHT_ARCHIVE_FILE, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Archive temporarily unavailable.", 503


@app.route("/copyright7_26_b")
def copyright_archive_2026_07_07_b():
    # Second, independent dated snapshot (captured 2026-07-07, V95). The original
    # /copyright7_26 snapshot (2026-07-04, V63) is untouched and remains the earliest
    # dated proof of authorship; this route adds a second, later dated proof point.
    try:
        with open(_COPYRIGHT_ARCHIVE_FILE_B, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Archive temporarily unavailable.", 503


@app.route("/copyright7_26_c")
def copyright_archive_2026_07_12_c():
    # Third, independent dated snapshot (captured 2026-07-12, V102) — the first
    # under the XRP Complete brand. The /copyright7_26 (2026-07-04) and
    # /copyright7_26_b (2026-07-07) XRPRadar-era snapshots are untouched and
    # remain the earliest dated proofs of authorship; this route adds a third,
    # later dated proof point documenting the rebrand.
    try:
        with open(_COPYRIGHT_ARCHIVE_FILE_C, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "Archive temporarily unavailable.", 503


@app.route("/robots.txt")
def robots_txt():
    return (
        "User-agent: *\n"
        "Disallow: /copyright7_26\n"
        "Disallow: /copyright7_26_b\n"
        "Disallow: /copyright7_26_c\n"
    ), 200, {"Content-Type": "text/plain"}


@app.route("/debug")
def debug():
    checks, passed, total, overall = run_preflight()
    uptime = int((datetime.now(timezone.utc) - BOOT_TIME).total_seconds())
    return jsonify({
        "app":           APP_NAME,
        "version":       APP_VERSION,
        "iteration":     3,
        "preflight":     overall,
        "checks_passed": f"{passed}/{total}",
        "market": {
            "xrp_price":      MARKET["xrp_price"],
            "xrp_chg":        MARKET["xrp_chg"],
            "fng":            MARKET["fng"],
            "fng_label":      MARKET["fng_label"],
            "sources_active": MARKET["sources_active"],
            "sources_total":  MARKET["sources_total"],
            "updated":        MARKET["updated"],
        },
        "checks": [
            {"label": label, "status": "PASS" if ok else "FAIL", "detail": detail}
            for label, ok, detail in checks
        ],
        "uptime_secs":   uptime,
        "booted_utc":    BOOT_TIME.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "now_utc":       datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    })


try:
    fetch_market()
except Exception:
    pass

try:
    seed_partnership_ledger()
except Exception:
    pass

try:
    fetch_fx()
except Exception:
    pass

try:
    fetch_competitors()
except Exception:
    pass

try:
    fetch_news()
except Exception:
    pass

try:
    fetch_exec_tracker()
except Exception:
    pass

try:
    fetch_github_dev()
except Exception:
    pass

try:
    fetch_clarity_tracker()
except Exception:
    pass

try:
    fetch_correlation()
except Exception:
    pass

try:
    fetch_orderbook()
except Exception:
    pass

try:
    generate_brief()
except Exception:
    pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
