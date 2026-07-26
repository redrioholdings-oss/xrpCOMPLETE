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
APP_VERSION = "135"

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

# BLOG AD (V130) - header advertisement for XRP Complete Blog. 375x70 banner
# (embedded at 750x140 for retina crispness, displayed at 375x70): satellite
# photo left, "XRP COMPLETE BLOG" wordmark, BOLD tagline, domain, Template D
# palette. V130 widened it 50% (250->375) and bolded the tagline; artwork was
# regenerated at true 375x70 proportions rather than stretched, so it fills
# the wider slot instead of letterboxing. Served at /blog_ad.png.
# The <img> src carries ?v={APP_VERSION} (V129), so every version bump yields
# a distinct URL and a cached copy of a previous banner can never be served.
BLOG_AD_B64 = (
    "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"
    "+Ge/m6oxQTLza6/7Xb7yBc/mS5/7jBo0J8/8//bv/2VsyhSlVnHl49z5Tf7T//glWu2cC2HDpUMIQbuVh67K0QVpod/jzLlN/vw9"
    "f80zn/akSGvPtLuL/d6cU9KlQutQb5SaQB1ZX+WW2+/m/MYWlx09NAfOF3q9sAr0EPp26wUdaXn++hmaQh3vBT3teeOpy3nTqZMs"
    "R7CWQJLE01eGykl+/p7rOdkZcW1vSBG16M4Huc2TFrd418ZRLIGl/8rDp9ICTz1eX3vedvo4v3H/NSzF/cy6pXoyAatZwT3jPv/5"
    "zifw4zd9hLY0MU/1TBzc0B/w5KUtPrB9iI761N7ZQkDp4TlrZ3njqauYODl3dxovWNIVz107g3EXufUfZaSVAh1XJ7S0FE7yicES"
    "X3n4XD0vnsA61wW+n8WEd39crLg0RQLulwL8NJ7fD+geyyl9ukD7p4qLebYXOM7ZorYrfWzjQ47g63pHa5IHwn3fF5rfGZ7i5/fu"
    "ZVlm8ZxnxxP81HM+aUb8wNbt/OqhJ9KREutDQjDxjie2Fnh6a5n3TgN4/+L2KtdmvRrgN8/rh7bv4HeHZ1hX2ZwEKJm1/fV0l3+x"
    "cQvPaq9QNIC/ACofViIm3j0mOdnnYuilxQUmRRUbEMFwXLKxNZixZVKgo7+7s4FZC4WnCi3BS4kxQStlko0kgYho5RlVaRGUdDot"
    "2llGZV1wQXFBC6UkWGvIWopp5ZgYy3Ivp4WmlSkGI824KBmOCsqipDKhNX2nnQOQS8Virx0aLEnFpKwYTAu2BxOccewOxyggyzW2"
    "3QYclTH02y0Ory6x0muzsTuipSRa+thNUGBMSSaDXt06i3PQyRVataiMY7GjGBYlmco4vzdksd2i38rY3Juw0M0joMmRQqB0bH4h"
    "ghvBqJjSbuWY3FMaUxfaWhuKP4VQWC8xlUQIjY1MfG07GT3iA6DPaxAfgHuGyjroLEfoDlK2KGULqbvovI9uXUZ79Uo6bkQ1uZvp"
    "+AGqyRbOdHFVkM2YaoIppti8QJsCWxQYPQ0rHDoPxazVFG8zlLdoXVGWBV5WCGdDuwlrMFWJsBKR/PtjR16lO7z73e9iPB7yoq9/"
    "Ce12hz/7k7cy2dvi8hueCcJzz733cvKa45Rj2JYaU1koRty1vcCTn/jFnP/T11OYNVqtFpNpyXQ44brrT3LHLXexemiZ81tDqt4a"
    "L/z6l/H2t72B0bggz3OMtWG1I34jpGLV2lFGBknE8soynXabavE4az3PcKdCrPSxCrZ2S0rjOLzSYWN3jPeabnGGQWeJrZ0pC+2c"
    "dqYxkyHnVJelxz2d4uy97Jy6jU7/CNPdDXb29oKlpnehoZfzUZMfZCwuurckUGbtTENdF2qTupiG80iPpULJGvjXCUAA3UlWE5Qp"
    "8X0e58NUVS2dcG62EjBrc9L80ptJRGbAqtF8yTMP3hOg3/f1+4+ILy4ZIiZDP/gff5IvePJNLC32Z7ISIciyedu2IDeS/Nj//BXu"
    "ue9BVpYfWiN+sfCNf0B9HWsr0DSN8ct6PJlSe/M/xHkoFSSPAbh7xuMpvV6X7kUaNg1HE5xN4oSLjEfQLF/RmXBtd0BpqXXtWng2"
    "Ss1bT52kq0yQW+1bRbGxMNUBP3Dr51+gkU4rPx1pKZzisvaExy/sUETZSdrPZqV446mTdKS9YD9pX8ZLlrKKTwyW+eNzl/GK4/fX"
    "qwPOC9ra89TlTd63ffiS8wdN8ZantHCiM+Vpyxv88fljdZGqigW0z149zzW9EVM767T6WNlE2egAm8YxTrKgL+yUaz1Mrao/Fz4T"
    "IYCx0WyXrdhwqJG4N2Qy/xjva+cF21V+gVRGMJPJhHvuMe4Hz4YrL5DKXKnafEX3UASpgcXOkGzbig8Vu7RjU79HGwIosRzTbZ7U"
    "WmDqZmBaI9lwJb82eICODFD4Ymda4VkWGR8r9vi90Rm+bfEKdr2pC1o7QvPMzirvmWwhBDy9tVxr6NOYSyLjd0dn+MPROQ6rPLrh"
    "+Nn+4o8FqfhYucdfT3dqKV3zXBZjA6gDtv2RhX7ytVdwy31nObO1Bw4yrVhY6iOlYKGds9jv0Gm10FKgtWI0KdgbFywttFnotLEO"
    "7jq1wXAyoZ+3kUphKouxPnj4eoexnulwylAULPTaZEpB7Ira77QpK8u0sKwsdNgZTtnYm3B4pYcQksMri1TWcq/b4vzWHliB85bR"
    "eIqUEq0Uk9KwutRDtGBtuc/x1gpFUVIZR2kse8MJg/GUlhJUpePBvR2kUmwOxtx08ihXHllmUhg2d0fcdfpMZCQ9i90Olx9aptsO"
    "bJW3kCuJEoKJs6wvdBHCsdBeJNMagWChq9kbTJFKIqVnUla0MoVS0G4pKmMppoZpUVGWBq01ZeWZlhXOhyUtqYJO3rmghU/NnwTZ"
    "zJ1GZcF/X2mkUiBC8arSGqla6Dww8CprI7M2UrVwVRtbtBG6i84XUK2b6HduwFSnMJN7KcdnMeUUbXrY1pSqHGOrKSYrkFWBr6aY"
    "KmjjrWmFIteqQKiKTGi8rfDeYquS4DYu8cognAYb2XgCw6vzjA9+8EMMBmNe+apvotvt8fa3vQWp4cqbnkeedRhPDa6YcvTyyxkM"
    "BmR5izzL+YePfoy83eP6TsEnP/5ubnjmVzHYHrC5tUOv2yHrtJgOJ5zbHnJ4/Sgveek38tY3v5HxpCTLs6AD976WeHiIOngRutsa"
    "x8krL0d2l8nWrmVoJVm/jbSWxZUO00pxfq9gXFQsdTIKD6duP0f3yONYXVTsDiuUN5w4vsDesGJnOGBh9Tjd1irq9N9x34P3UVaG"
    "Vp7PtOQigPgZHx2FBw3aLtkW+vrpJE5ILHukxy2NUZJbzexv7z24qJOUNPTuSfISKV3f+KStqRIBPvhx+JgAyDoxaH4yN1j5BnJp"
    "nltjy/DRfQFF+Y8H6ZNk5hO3fpIf+5+/zH/54X8xx243LRcTG/+e932Y33rTH7C0uPCIQTsEd5fKmPrenExCDcRznvkUIF1pajvc"
    "2+68hzzLHhK4W+s4d36L8XiC0holBZnWfNdrvoGlxX6s6xCBNJCSO++6l73hiExffFwhoPKKk90BHeWo0q0SgfD7t1c4W7bJhb0A"
    "TKcIIGfWJOlirKqWDmMlV/UG9JW9YD8f2F7hTNEhl5feDySXE8df7xziRZc9UEtXBGAcXN0b0FPmIdnfygtUXBVLmvsvWT/NX2wc"
    "rYFhYrifv36aXMAUQYJoxgv0o5TM7AfJ1gdi7Ib+Li84dJqJna1JSeGZOrhv3EMLR+E//TymIBTFPnv1HItZOZd4petaOsnbz8wX"
    "l342Ivi0V3z7lXdcUJzaLEz98O7aY9K4W+9ZlBn/fOmqfcWpiue0V7kq6zKN7LIC+krzE1v3cK+ZsCA05WPg3AWCynmub/dZkJoq"
    "Jfd4elLxl+NdHjBT2uKhu6E6QAvJX062eEX/eO0Ok5jw63WPtgyPXpt3MX42WxJBgeWdk/PEb4v6tQtiXhDkCUW78iK3ogAm3s0x"
    "8Qfx8EKX1rG62Of44RWsDfaM3bbm0OoimVB4ITi7uc3euKAylr1JGVuci1D1L2Ftqcdiv8vOcIxUisOLfYaTKSBo5QpjLAvdFgjB"
    "1mDK+kKHBzeH4D0beyO67RbWWB7cGJLpAMY3dqesLrYpneX81ojKerTOqFyQZWiZCgsFRWnYHkwpSseotCx0Wiz22rRbGd22Z31l"
    "keE4OCu08ozt3RGbOwM2d8d85Lb7uPbywxxe7pNnml67xd1nzrM1nDItK05v7ZJrxaHlLovdDiCxxiJaGd5ZJqUlk4J2rphWFlOU"
    "HFrpMhgVVLYC4ZmWIzKZ0ckUuYR+S1AZQ2kKdgZDjEmsaGhVH8BZEa0mdWRYVdS/CxAaU2qUyihRSK3IWwJnc5xpgWhRTnOUapPl"
    "GSprIbMOWbuN0x2QbWy5FR1qFslaR2gvHqO1MKCa3Es5ehBT7qHKTmDgy8DCO1MgiwmumuKqAqsLbFYEqYzK8LbCVVUowHUZzpRB"
    "NmMtVko0HlOpAPCdI2stc8stN/Mrv/xLvPrVr6bzTa/iLW9+A6OtTa572peTZZL77jnDVdet0jNthlJhi5K1ruUDt2zxpS96NZ1P"
    "voub/+aPuPzGZ1OMCyaFYe3IChtZm/XlLqaqOOUO87Uvegm//3tvZTieBr99F7XeRHgogzzAWotSmiOH13H5ArnWbJzdZvnQMrot"
    "uOrQAvecGdHvtnHOcH53yqIas9jLmYoOm5tDDh9ewAvBaFxhHSz1O2xvbeFUj65SnDl9qpYtNL9dUnGsJ8gvauDqU8MoX8skauvI"
    "MEgANc7tG8/FTp4yyGXSV3wE+FJEH3sZx4g0ecoJZuPHUlPvG95tKenx+8B6GOtSgpiLQfb03OzP1Jp9/zaf3QguMwv8yuvexle+"
    "4Nk8/zlPn0lmGgBeCsF0WvBDP/YzdbHwp7JS3B9ShgZKwUkmrPStrS7zHd/yEp7/nKcHGYSarbjc9+Bp/vrDH6PTaT3kvlaWF/n3"
    "/8/3UJnQ0yDLNE950uN59hc+uda2h/MI99SfvOsDjMcTVldaF00+BAE8HmpNaUkoTZC5BCYc7pv0mFpFO3vojpbpql4M0KbnjBcc"
    "yS++n3sn/Ye3n1gUe9+4x8hI+qlhjwiWw4fzKbm0jGx24WuBXMCpaYftKucpSztMLEwsfP7SNtf0hnxy1KetLKVTXNEe8/TlzVq3"
    "35Lw0b0llnTFic6Y8hFi9yZIXspKWjIIk5azkmeunGO9VVE6aplRS3oemLb5xHCZtrJM3WcAuIsgF3r22iYvOLQ5ZweZrCD3Kvij"
    "c8eZxkLhzwabKuL+FzPDd1x5T70qlY7NeFjP4X/edSXv3T5MTz26Lq4JJC9F4N6MZAeZQLsACu/5pZ27+I3BA3Q/DdaHguD/fplu"
    "0RaS0psGsy+4sxoz8ZaOyHiodR6PJxeCu8yYoTeNzrACg+OobpHHeqkjqoWJ+nRP0OrvOctt5Yhcyroj6yPpMmu9Z03m/NTu3fzU"
    "3j2sqRzzmVoi+j8w9OpSjyuPrIUukVVY8JiWFaNJxe54yH1nNoM7zLhiUpShAFEKsjxDCEm33aLXzkFAK8vptTNWlnpcdWyNvVEo"
    "cNJK0Y5OMUu9gsG44PJDS+yNppzZ2mM8HbLQbQOSSWnotjztVpu9iaHb0nQ7bca7I6rKzqy7GlpcrGcwGDEYjEFKMq1QMnQ79Qh0"
    "pmjpDC9Aa0GuFKrVoi0Nk8rysbvOcMXhZS4/tMTqcp/lxS6TacnG7oh2S7HU6zAYFxhjaeWKMrKW3W6bngwMvBCCVqZjAaBjqddi"
    "Z+g4cahHZRwPbuyyc24cQDrhi340qcg6Of1O8MIfjSZMywIXGfZ0jkIE8IUQ0RpTR1QlyZXC24xipMhzgc41UrbwLsO5jMJlZKaF"
    "Nm1c2ULqNjrrYHUblXVw1S6m2ETpBVRriazzeWSdGzDlKarJfVTT86iyQJddfFWislFg4asCWU7RVUFVTqDVoSqnSF3ibBtppqis"
    "TVGWeFmiVYZ3JgAFI3HGYp0h665xz9338ws//4u89ltfw6u+5dW84XW/xZ0fMlz95BfQ6+Rsnt9G2IJrrruG8WDA6VvvpLN0lFvv"
    "HfC4E1/M58m/5o57P8DJJ30pg71TbGzscuRI6Maa5Tl3nx4wUD2+/qUv5ffe8hb2hhNarTwy7wCBafd4lNKsrR+m2+0xXLyOfk+S"
    "C8lgZ0x/rcdd58eMqooVWTJGUHT7DB68k62h5PhlLTBwfrvg8FpwLNocjFEiWPDZYsrw9J3sjaYBmF/kc2rWuTU0TRLxXg+OJU04"
    "O/NQngHFwH7bJKdJMgo/K2INmvgA3JMuO4DyhqJFzPzchW/INwSAq1cpkkf2/AmE7Wb5g4e64Uk8/kch/v3HYmREzF7+zX/4Cf78"
    "7b9Mr9uZm6u0CvLjP/Ob/O3f38LK8uIjYttTAnDs6GHe/8e/Vc+f99DptOqCUsFM5qSl5Kd+4XfY2NxmeWmRsiwvOe7SYp//67tf"
    "dcHzCahDYPq11tx1zwO8/m1/xEK/FxO9i4cHOtLOeT1DyOkG5kIA/FDxUF/VHugqc8ESuwMG5uF3mBSEAs+x1Szo2XmF8cN5XOpA"
    "lICJVbx38zBPXdpB4KOW3fHctTPcOngcPW2YWsmzV8+xnhv2zMw//r2bR/iS9dMPuY9LHvdFQHI6/4klgHZm78+WgrecPslOldf1"
    "BZ+JCKsAguG+tZKUVA2M/keTPlgPW1WCzb7xePh7Yj89JaIWz4a9cI5lLM5UCM7bkv+0cydvH53lkMo/Lfut2XWhUI3yY0FYaB04"
    "87D3I4Cpd4ycZUnrerq8J44fRuoJNWedKQWMrGHkzVyNR2LcH06XWYNnUWpa4jNVQv1/duhpadkZ7lEYw7iomE4rtgYTitJgXcjm"
    "lJChgY+QyCyrP/Cdc+wOxuwOJ7RbeSjWEgIGY0aTEmMt48LinKOsLO12hneeVqY4vNLnsrVFrjiyyp0PbjKaTOm1FVSe4dQhlaGd"
    "Z3Q7LXptwXBSsO0sWqgkIkDIma+0kj6K+jzW2KC7ExHUTA1DUaIzidYaLYPLixBB026d4/5zewwnFSePrLDQbXF0fZljh1Z4cGOL"
    "qrIcWu5joyf4cj9nWlZMigKEYDie0s0ztJZkStHJWjg8C90O07JECDi/s0srz+m2MipredyJQ+wOJpzZHGCrksVui8OXr3Hv6S1w"
    "MJpOIgOvEaICEZpkeauih73CWkEpJMvdMV0pMUYjyBFiGrpxyhznNMZkuEojdRshc6zuoPMOTnUwuoXQXVS+gyo2qXSfrLWEyo+T"
    "LV2JW9iiGt9LOX4AU45Q7TauKjHTMVU1xlRTRNHCFlOEbOGyInZuzXC2QAmFtxpnKrwr8VYghUUqi7caYS15b5UzZ3f4+Z//RV7z"
    "2lfz2m/7Ll73W7/GP7z7jTz+uS8j63Q4e982S4cqTq63+IvNTVYe93RaQnD7/SOuPv6F3Jh9mL/+izdzwzNfRDncZmtzh+c940bO"
    "b+3h7S47wxFnFg/xFf/ka3nnH/0+o/GULMtwkbHyUf4xmUw5eeUxStVl8dBlnD6zR7+jWFvStHLJqc0RUis6rRa5qbhMOR60Y5aO"
    "X8f29pBeR3HkUA+B49z2mOV+hneO8zsVq2xy7tS9TIuSLNNzji8ws/qDwPbiZ8BRxMKR+uvIE7sUR/Aefd2Dn3goQFVS4IWIzZqS"
    "L7uoWXK5D0B770CE1axQvBvfUqI2g4zbhQOqa1zT/4SogT7A3LfKRaMhBRL7Hn/oz63PWgghMMZww3VX0crzC65Z+n1jaxu8fzQ5"
    "CRCuZb/XveDxpj98kga+7k3v4Nd+++0sLvQ/pUe89x5j5kF4kjeFxC18Jm5t7/I9/+pH2N7epfcwOqdGk9ILz+MiTh6PJS5VSLgf"
    "zD+cuJjDi4vdRy91w1lCsecHd9Y5W97NalZROSg8PGf1LG86dZKpVSxow/PWz9RdPDMB58uMD+6s81VHHuCRC6dCXAokJ8AUWG7P"
    "kva8+dQx3nH2crpR+vOZBEQ6NttrRgLupXys5ZePPsJKR0011GG9pyVBiU/PsQmCW8v+MHGFwUVg+oMr1/K4rMcv792HEvPFzI8l"
    "LBeeoyDcFxc3y7x4pCRjfzg/q2p6JDNWeMcUx8WESKrx4Zg6xv7j3Sn/3w592wMb7I0Kyvjh7mxYQlJK0spzSmMZT8sIDgIA8Da0"
    "lZBa0s5Ch1UhBb1ui4VuTmUcg2lFv9OiKwTT0rE9mLAzmtTyhLPbI9aX+zz+xGG+8MaT3PHAOTaHU6TyXHloiY4OBv6TqeXM9oC9"
    "vQlSZMEm3lPrdIUMAN07ESwsGzeMbDCH4Ot6WxtZyLbKkFKQZYGdL4zl4/edo5tJ1pcXufrICodXlhlNptx7bgelBEv9Dpm0tPOM"
    "ditjbzRhaaHHaDLBltDKJYUzdFo5xbQiz3OG0wFHVpc4u7HH5taA0jqKwrG61OP4kaVgJVmWLLUl1xxbwcfk49TGgOGkwlahxb2Q"
    "EmsqnFUh8fASh2JjV6CVJcstWlqUCKsOQk1BBKDvlcaUGeg2Rk6oihwvOkjdJss66LxN1u6CGuDK7eBG01pE6hVa/aeS927Elg8w"
    "Hd2Nmewgsxaq7GKrKVU+wbam2GpCNZ2iagnNFFsVuKpEqhJvc5ytcKbAGQOiBCVx1pL1F9jem/JLv/ArfPM3v4Jv+47v5rd//Ve4"
    "7X1v5eRTv4Zef4HBYMpesYuRGe3+IZx3HD60ysdvuZunPvmLeIZ4Lzf/wx+zcuLZ5K0+Z88PWVlfxDvPoUNrPHB6g9HiOi980Ut4"
    "x+++lcGoIG9ls+I/b2l3uqwuL7EjD9FVbdYWK8YGzo0qrl/qYjLYGY2pqgyVtemV22S2pNttMVIlCMXuuOLk4TbWC3b3KrT2rC22"
    "Ke47z+kzZyPAm8kp0u8JLIeGxY3i01oi0wD5qYCUlLCClMFdySPq3gdCRhVQ3E8qcp0VlQa5SwDQMgK92JRNztjxkCz4GsSL2Z9z"
    "kT7sRQ2IwhnMOZ/sw777ofDskQuf+WyGEIKyLDl8eI3/+G+/F61VnRjNNgo/fuj7v5u/+sBHuPe+07TbrYfVdOliUdt0xpDxQ0tK"
    "ye5gyE//wu/wE7/w2+T5w2OcxUUKaffH+z/4UX7gP/4EH/34bSwu9D6lhaUARkZj/fzVEQKWdXlRi79LjbMf/EF9OyOBodXBoWXf"
    "61YewX4c0NcVXWXmfdcjO5zcSy4aHjJpOVN0+MjOGl979Aylg9LCye6Epy1v8PtnruBL1k9zfW8QOrQS/OX/dneVU9MOuXSPPMto"
    "xMVAsgS0DBrqjVLza/ed5I0PnkR/FkBzWMFoNoWazZ4SMDTqH41F9aT9zzvSOB+SqdJfDKY+uv0M/HwHVkEotpQICu/IhOCQzPnX"
    "y9fQE4r/vns3PaF4LDeDJ2jM95yh2ictEcCKylDi4SVtDliQmp7cz6iH8W0kIgbOsK6y+rCth57UdIVi5G3tCCOANZWzdBHGXQB7"
    "ztSPp38H8ehCT0obWHIBAonKFT2tWVvs4BGc2x5hLeS5ihrLkI21stCd1BEudJ5JOi0dGD7Ccm5ZWVb6XYwZkeUZS3mXdksjkWit"
    "2BmN+MS95+m2NDpXfMH1xzm3PcQDC50WRVEwLi3GeJQWZFknuIAACIEzDp8YnrQWGR0RUgMRKUEqWUsHhAqOHC0pabU00guMt2HF"
    "IFNUlcE6z/3nttkZTrnxxCH6nTYnjqxyfmfAfWd2ObTcoZUH20zvYVoZMp0H32NCkjIpKlpZzs7OgHFsfnJkfYnWIGc8nbK1O2Rr"
    "d0C306KVZyx02xhruerIEh+98zStTHHdFWs8sDFkMi0ZDqeYqkTqsNTnnUd4SagRF1ROUpaSPCvpZIKyUnihaLcE5aQTrCu1Blnh"
    "xRSlWyBHeNGl0m2kapPlQ9rdFi4LfvCmGCCzbXTWQ2YrZK3H0Vu7CledZTq8EzM5j6066KqLKcaYoo3Op5iywJZTbDnBZiWmnOBt"
    "ia0KpCmD9EcZvNVYVyKo8MKR9RTWW37lV1/Hy1/29bz2u76H1/3mr/KJd/0WT3zBt7CwsMK9//BXqP46V151grNnzjDYHbK81OGB"
    "jQG99hN44onbeP/H/oiTT38Jk/EeO/ePOXRoFWsLhPVs740op4qvedGLecfb38becEK73UIIwXQy5ZqrryZv9zly9U04LOe2hhw6"
    "vMJKt8OZzRGjsuDw2gKjkWE0Lplu3o9bOEYvF2TOUypJ1ss4u2OYFCXLCy32RiU7u7tkO/ezvTus7faSZjC5h9S6aZdcWnx4b5Jg"
    "bKK4Rd3pNUlgVGyslFh7mTqr1utTYT/BtztJckSDLocEsOfqTH3zK1A0toxJPA3w3vjwd/XjPh5jY7t9oJ3ZZhcJ8dBPfwZDSsl4"
    "POVHfvB7ueLYkVADpJqFvIm5dqwsLfKjP/jPeMV3fP+j2pf3nuFoUrPu+4tgX/emd/DffurXuPf+U/S63Ubi9dCzsr9zaih6LThz"
    "boOPfeJ2/vRdH+BP3vV+yqp6WKA9sKqOM0Wbws2AtwAqD9f2B3Sl/ZSWe4LQaMfY+SJC7wMz3paBhHhg2qPw8w4tlYfH9fce1n6k"
    "8JRWc11vj75yc9aTmfCcnnaZ2Kbo4OLH6hH81eYRvvLwGWKqGzqkrp/hHWcv53nrZ2kpKKpgumA8/NXmEfzD9Ih/qH3vB8nWC4ZW"
    "c2ra5ea9Zd6zdYR7xn26yuzj5T/90WwK9ZZTJ1jKqhr0zdJtwdRe3Ef9MxWeUI/w4LTN9938NEor5xK79GlbOclCdAJ69PuR3F+N"
    "+dbzH6douMpoIbk+6/HPl07yuLzP1AcStPIl37p4BR8sdvnL6Sbtx9A51QOZENxnpsE3vbEWWnjPTfkCPfSn1NJLBIUz3BiLXAtv"
    "SR7rmRDcb6cU3iG94JSd8risR4FBxm0WpOL6rMeDk4KWDCsJpXf81O7dtJB10ywIn/vWe76ud4Rjqk11II55zKE7rYw8y6iMJcsk"
    "mdZ4D1JrtvbGaK04tLaAdZHlE5Ldwaj+0i6qoHkPDYc0LRytLMdUlqVeh14nWBQeXl1kfbnPAxu7HFroc35vQKu9ykInD28wDwvd"
    "Dt1OizObuxSVYVx5CmNZ7LXx/Q6VsbUcwDqLMa5mZ0JRoUApiRSSTAV7yrJyCOlp5zlSSZx1lMZgvA8+6kjyTGO8xxSWhXaLUVHS"
    "67bRSnLzPec4vr7IUr/N5UdWOXF0jcG4YGc0RUjJoaUFKuuYdKYgBNYYyspy15kdVrptFnpt1hY1Z7dHID29bgsnQOc5RVEyHBds"
    "7w6Y9rsMpx1A0O/m3H1qk83BhGlZkmlFf6FDURQU0wqpQlGwlD7aY0qSx/60kFijkNLgCHIaMDifIZRGKQNCo3WBkDmIAtkReNfG"
    "mg5V0UXnHaQeo7Muut3G5l2kHmKmG6jWMlnrKL2V47iF0xTDOynH55FZC533sOWUqhwFsF51MOUUqXKcKZFqgqmmeJkhXYU1GmE0"
    "TpR4Z3C2wjiB021+67ffxIu//qt59Wu/nTe9/vV8/N2/w7O+9OWYYpfuoS9ge3vKsePr3Hf3aTqLSyhfcdf9G9xw/VP4wpv+jg99"
    "6M087Zu/iw/f+gDT3V3W1heQrS7SO7Z2B9zXOcSXf9XX8GfvfCe7gwimheTyKy5jYNvIqWa9ZegeWmZ7d8pluWKlr7EDy7mtCZ0s"
    "Y2Uh59wnz+NWbmRQevJ2l7awXL7c5tSuZVxatnYnaK1ZySfcfM8nGU+CLaX1NspdFHgfu5MmwCYi8J1n5YUMNpEz5jsCR0IyXVdk"
    "kTTpqdlSYOwDUzwr8msibucA75EqFEY670OBarOJUvO7zofxm8AxJBuzFa65F6RDE/PDcFHw2UT48wnDZyuUlAyGQ577RV/Aa175"
    "oguY9iZwFrEe4Ste8Gy+5eVfy6/81ttYXV26QKJysWh2Tv2ir/xmvv1bXsIPfN93zCQy3qOEYHGhz933Phg19O5TFr9e2Dl1ipKq"
    "XtkpipK9wRDvYaHfpdvpPKxmUd4LMum5e9xnYDR9FdrVS+EpLDxhYYerewNuGy7SVfaiAEmKYCl5sjPkcGuKaUjAFDCwmrtGC2Qi"
    "7GerzFnLS0wE8FMLNy3s8rj+Hv8wWP6UrjACz/PWz6AlTFzYR7o7bxstUjhFT11orZjCekFbGv5+b4X7Jh2uaE8oHUwtfN7CNs9Z"
    "O8uTF7dCIgPkEh6Ytvno3iptZebYzEcSlwLJHoHxARxPrKatLH1dzWQ/n+EIyYRiYDJUbAq1Px5r46lHG4Fx1xSXSBzCAv1jP7bE"
    "uDftIIWHP56M2XQlv3H4yfXjlmDV+KLeEd473XpMew9FpZI7qxEbruSwzCN1J5h6y5PyRW5s9flosUdfqEt2JI3fBHxl9xAZggnU"
    "zLkE/qEc1G4vt5VDXtBZr7GWw9NG82Xddf50soGI6UOB56d375nbo0Iw9pZrsh6v6h+fW/Hy+FmCcYDlH1HohX6P89tDSuPIMs1g"
    "VDAcT1Fak2eKVp4zKiq0UHQ7mjMbewgP1lXkuSJTUbYhoLIOUUKmJatLbW688giDcUGxPeDyQyuhcYDOmFQGISRPufo4m3sDTm8P"
    "WOp1+JtbH+Ds1gAtFQhi45gITqwLH4AJmDiHcwmAEDuWBj/fVgaHV5dY6rfZGxVMShNYTAW50nRyzaSomFQVZWUonaMnYvOTTLHe"
    "7nP/uR2kFBQGzuwM2JsYHLus9rusLHRYX+yztTdiZzBhsdeuGXPjBHmec9OJo4xiMe/exIKApU47JBe7mtFkyspCl3Ye5A13n9pk"
    "tZUzKS1SKtZWFhiMpuSZoigc03KPPMtRWoC3EPWpbS0pjWF5sce0CI4JxhiskSCJXWEdUlrwGmcD4+1MjpTTAN6dotUeg8ywto01"
    "XZTu4LIupuwEX/jWEKF7ZOUAM91C6kWyzhrdlcto9c9Tjm+nGJ3FmRa66GGKYQDt+RiZ5diy4P9l77/jLcvKOn/8vdbOJ99Ut3J1"
    "V3VOdICGbqAFSQJKG5BgRB0xjwiOab7zdb6Oo6Oj4yiOjmHAhDqiCEgUkdjQ0NB07qa7unLVrVs3nHx2XGv9/lj7nHtuhe5qBGR+"
    "U8/rdavuPWfvtddee+29P8+zPs/nUZnVnlduhipSq1suXRztkxcljUoVyEAiHI93vON9JHHMd333d/PXf/XXLD34QXIjmVvYTX/Q"
    "oTW7wJaFWRSKY4ePs33nPMeX12hEl3LbzTXe87/fwsK1L0cIQ5olNJtVRqOMwB9y/MRJzHyD573wxXzuM3cSJzFZoaiGEdGuK/G3"
    "znHy2AmqUcTcliYCeOx4j/lmxExFsj7SJCcPI4Wg3ohot7tE1Sq0IsLQx2t3aQYOQ8fQHyrcwUnW1lYBA0aXSo6W3jUGzeOYomFD"
    "YmxDxtFuI4Wwet5mTAPbAPbTco7CmJIIPE4IncS+Nz8BxlzGMtJutezHsqSWY2Omtp0Oj5aUeIyYCtGLjZUEyvPZ+FWctZ0zbToN"
    "96tvQliJxygM+aWf/7EJRWY6t6c/GG3Sdrf5Nob/8DM/xMc//XmOHjtJGPoTGtaTmVKKLC/4gz95O9/xypezZ9c2qwokLL/9FS99"
    "Ht/57S/nL/7mvcy2GjYH4jzs9MqpkyRmKWjWayCsZOT5UnsMljqynEY82G9y29zapKKpMlB1Da/btZ+ff/gmMi0JpLYVGI11GCWG"
    "gfLY4if85yu+wGKYkms7VQsDTRf+6sRO7u/N0HBzVtOAz3XnuH3r0qQSqTZQcQw/sPsxfuahm0i1JJw6DpiJDOFa7vPSLSe4bXaV"
    "YbEBKB1h6BWCz7QX8MVGAOhc5grDShby6fYCl+w4QlKC9NBR/OTFD9PyMlTJiAkk3NmeZz3zmffTfxEmORtIHi+SucLQ9DJbuOor"
    "XFTodDu9KNTp9q+Jw1xhUKX2/en9+HL2y0XglrB17AjOOz6H8pgVlbLTDcmMmcgnXuHXaEqXvi44qz7ieZjB6sIvq5RPJ21eXdtO"
    "WlZOHUtC/mTjIl6/ej+J0URCTiqgjsE6wIrO+JbqVl5UWWBQariPz6mjCz6RrONLgTKGT6UdXjdVfMlBMDAFL6ts4UPxKu8frjDv"
    "2Lo6804w6asDZMbgG8kvti5lwQ3oln11hGCgFV/IegRfBrWd/9tMdvoJcZKT5ZrVdkxvmCGlB0aSpppONyaJC7qDhKWVHq7jUKkG"
    "NBtVm+jpuVZGMQpwHEm9VmHHfJNLdy5SiUKatYhdW+fYttBipl6hGnqc6g5Z68d87rEjfPLBQxxb7XKyPWC1MwAsDSDPcopCUeSa"
    "JMlJs4I8L8gLZX+UQRttFRyEYG6myVX7Ftm10GDrfIv2IGOYZDiOnXyjLAcjqEY+UeCxfaHJYqvOQqvGbL2C51oy8JHlLp1RSqNa"
    "wXFdWo2QNBcst/us9VIeOrTCnQ8d4cCpLtVKxEyjyno/5vByh4NL66z2hziOi+u6hL5HrVJhtlFl61yTUVbw6LF1Tqx28X2PRjVk"
    "vlmjVvG5Zt8OnnnlxezdNs+ebbNcvHWGKAgAh9lmhblWzRbCyu1LJi8KhIAwdCnygrX1Pr4vLYdc5whR4EiFMDlaZxRFRpFZznmR"
    "p2Vi6ZAi75PGQ4b9BJMNcVQbka+gs2WKdIkiPYlKTpENl8kHJxl1V4l7y6TDE8Sdg4zaJ9CqTlB7NrWF24ial+DV6gTNFkFjjrA6"
    "T6U+j19r4ddmCWqzhJUmftTACRs4YR3hRXhBAy+oIb0I4YVI38dvzfO+D3yU97//A3z7q76d7Tv3cPTwIbrLx6i3WnQ7Q46fXKPR"
    "qBAFEZVGC1HkrA9z+v6l3Hr9xRz89N8Q1FsYIRkOBsy2IrywRuC79AtDql0Wt87ztOtvYOuWrXR6A4ZH7yc+9gA7dmxBOD699hDf"
    "c2g1qgwHKe12j0o1wknW6IoZRqlmfsYWo0pixRdP9ukbqAWGhgMzkUfaPs6p1fWNnAshSuUYNQHO1jaK/FgVobH04DQU3gCKFoTJ"
    "ye/TeFicVq3Q6A2QD9b5taozZZGfqei6EAKjTRnhH2uHb46+T/85TnTdSGM97XVuynMrz336OKebYAruj7H+GVt95cyRDt3egB/+"
    "vm/nhuuuRE0liAI88PB+vv11b6TXH9i+lQ6V1oa5mRa//O9/ogTW5w+mjIFKJWJ1rcPv/MHbzkjaNcbwM//2+9myMEs2KZJ1fjau"
    "nOpOfhyr3a71eUXZTzeJLW70jyvbN0nuSQEjJbh1dp2f3vcgrjB0cp9YuWRaEiuHdh6wxU/4hcvuZ0eYkqrSGSrbGSr4+OpimeRq"
    "KWPvW97JqBCTxNfxcW5qdfiFS++n5hS0c49R4ZJqOQG6/cLjJQtLvHHvw5ipjiojqDpwZ3uBLw4aBM4Ta8GDnbmu0NyxvoWhEpsi"
    "yjvCZAISpTCMtOCTa4tfUgLt2cd7AyS7JSAda8R/qUmocrqts/ycz/7jolBn+/nXiriP+3auH7f8/8th4wTLjR9YVxlb3YBZ6W/S"
    "PjcG6qVSy5Md3UXgitN+ys/GhCmJ4O+GJxnqDdAtEQy14pZwhl+bvZyGdFjXOUNTkBpNbDRdXdA1BbdXF/nFmUuZrhyiSuD/sXid"
    "h7I+AQ6RcLg77fKFtEtVbkTwDTbZ9D/NXs43VrfQNwVdnTPQBUNdMNAFp1RGgeHnZvbygsocvRK0K6wqzufSLp9LuxPn4oKdv7n9"
    "UVrq2go8X6KNA1pTaM1YJUE6DkHg4HsOnu+SpAVFoQg9l7lWjSjwEMZQj0IWZqtUAx/XsUWLMmXYu22ew8ttPvvIUbqDEUlqQfTJ"
    "1T5SCAaDguXVEU6pJz1WhwFwXfB8x1ZgLb8y2k63wHeZq/kMU0V/GONIy61XhaEauaz1ExZaNRpVyUw9QgqJArpxxlo/pj9MqddC"
    "extIQRT5JJlivZeS5Sn1Sojf8HEcx2qQFwrHkaRZzv5jq5xa77N7ocn2+RZB4BD6PgdPLHNivUfN99mx0GClOyTwJK16nWatSl4Y"
    "9h89xSApiLMh/VHCXL3KlrkGUeAR+i7aGJKkYHG2iue4uI7g+GqXahRyLLYa6AJBkmRkeUYQSHzPZ64ZUQkc+oOUJM+JR0Nc1wFj"
    "wZ10XbSy+d5aSLS00pLSyVDKpcg9m8vgaoTMcd0E4Y9QzgDXs5F38h46r6PSCk5QIc/65GkH12/gRbME1WfgVy8jHz1OOjqO8lyK"
    "NMQJIvJkSJ6FFEmIyEYoN7GVWL2AIkvQwilVaDKMdNEyxZ9b5OOf/ByD/pBv+dbbiSoh//iBv8T3BLO7n4bvSTr9mJk5K8OnZUAU"
    "elAkDOtX89xnau65731EO5/N3PwMy6dWWNy+jROHUlstV6ccOHCYa6+pcOneRToDzfLx/dQ7J0hOHqS+9ya27dzL0aUVcm2YaVVI"
    "Mo9hex16a8wsXIMpCpbXcubmPLbM+ZxcGZEZTV4NCDyPWbXKPccPMxoluJ47iXJbICgmoWtRgj8pBEg7/8eVVMfyfePI7zQkH1Nh"
    "NijrFuhro2zieBmic6Q91FhVZoNHPd7F/jIGOeNjGmMmxx2/isbRmzGRZXPE8iwgaAqAi6mIuznr1uIcv3/lTUrJcBRz7VWX8oYf"
    "/Z4JKJ8+wd/+g7fxoX+6g99485/wS7/w41bbfeKIaV72oufy3a/6Rt76l+9kttU87+h4URQ06lX+5u8/wOu+43auu/qyCWVGKc3F"
    "e3bwI9//Kv7jf/k9Zmda5y07OS7oNP75l5oygopT8Kn1LXy2M8OzZtr0y6i7wBAXgldsPcFltR4fWN7O/lGDYeFSd3OubnR4+eJx"
    "doQJQyUmIMpKLBo+tLLAvb1ZIqdAGUnFKbi/1+K9y9t59Y7jtHMxAV8jJXjhwikurfb54Mo2Hhm06OYentBsi2KePXOKr5s7hYGJ"
    "2otdMTB0Coe/PH7xeYM4g42uPzpo8MVhnevqPUba8tnHxaE0gkgaHhrUeGTQJHSeTBTv/M1M/fxLTfDklU+fSE7yXPuf3sa/RvXU"
    "c1VOHffty1U9VWClD/2piLuD5PqwwU8091CTDvFUlFoI6Bt1VrWVTf3nzIqsG99BRThEQlIpAfXfDU/yuvpO1nWOiwX2Q1Pw8soi"
    "V3h13jU8yQP5gLbO8ZDsckOeH83x4oqlvoydCwN4QtLWOX/UOzIVgIFUa/5X7yhPD1ql42A/z42hKVx+a/4qPhKv8dF4ncPFiKFW"
    "VITDZX6N26tbuMFvMirHwmAdjAzNH/aOkBuNL5wLwP0pmhsGHq1SylErg9Kq1I+2FTy1ViCtwkzouriupBr6LDQjKmFIlufkhWb7"
    "fJNqGHB0tcvDx9bYPtukHnm4jmS5O+Sj9zzGydU+niMZv2+kFChjL5lbRg03gEfpBSqDKmkhQggcpwQSRpPlhpOdFCkFUmiOL/eo"
    "Rj5+ELAwU0FKyUpvhNGWJ+p5LgbDemeA1jYSNVoflAmzAteBRq1Cuz9ASoe8EKyuD/Act+xvWfhJSuI4pTNIaA+s4sze7fO0ahGt"
    "Wo3FmQbGCOI0J/Q9ZupVeqME35HsWmyybaHJ1pk6vWFMJfRwBBTaEiQ8z2WYJMw0a2xfaLHS7jOIUyqRz8n1Pq7vkWcpxhhbrbWs"
    "opimOY8fPkUl8qlEPovzdbqDlFNrXYzSFIXARVuajDYgHLQuMCLHGA+BQgurWCMdD+n4CFlQ0QnCGZHnEbljq7G6bh/jNNB5DTes"
    "orMhRTa0RZu8Gl44h1e9Cb96KenoMOngACodWB58mpC5A1RegvVsRJ6OQLoox0VkDqIs3pRlAnROOL+Vu+9/jDj5G17z2m8nrER8"
    "4D1/Q299jetueyn9zjqd9R6X7NtKmuQUWrN7+yyfeuAoob+DZ1wnuPNzHyEMn4/EobPWpdGqUg19hisHabe7HHr8fq659lpcr4Lv"
    "efRGMenxB0i6R3FGt1DdcQ2Fclld6xFEPqEZcXJY4DSh4Ra0mhV6mSHopwSexjOCfndAEjTIOqusLC9NCCDa6A3uuDFT0fONqT+O"
    "hNs1f/vKnq6cugGYxxKEBmMkeoKJp6PvJUnGMCWhukEz2wTgKfdFWBrMRoMbiicT0L2ZIsN0fwSIccrfpgTbJ7KzgPknpdV8+U0b"
    "w3/82R+hUatOCi7ZHBqHf/zIp3nnez7Mrj3b+f23/A0vfP4t3HbLTROAPXZ0rMrM3RxbOkUYeE9KxRib4zj0B0N+83/8GX/6e7/M"
    "eCRkOUd++Ptexd+9+5947MBhojD8sgDxL8XGPPXfO3Q5l1Y/R90ryEogLoRhWAguqw64ct+jDBUoI3GFpupAqplE0MGCrcgxnMx8"
    "3nL00s1JhUYQSM1bjl7ClfUeV9f79IoSvGOPsyOK+ZGLDjBSkGlbWTRyDK6AQfmu2Zh7Fly/+eAlfHHQpF5yw8/rnLH86U+ubeGG"
    "Rm8yUaejqq6EO9a2MFCW//+1Zudb+fQ9yzvPOmefaP/T2/hqV099osqp8OWpnmoBq2bRDfnbrTduep6NwbwnBLHRE9CuMQTC4bFs"
    "SE8XuOLsNTzOVZF13EZFOHwqafPptENVOoRG8jvdQ1zr17khaNDRxQS8D0zBbi/i383sY6gVWbmmVBUOrpCWrsPmZ3JFSH61vZ8H"
    "8wFN4U6i6zXp8rFknT/vH+f1jd2s6Qyn7F1eBoG+obLAS6IFhkahyrycmnRQxpR67xa0awyz0uO3ugf5VNKmId1z8vAv2LnNHUeb"
    "PUcSVXyi0KPQ2lJTigIpHaLAoxJ4SCFsMqQxHFnuE2erVKOIi7Y2WR8mHF/r8dkHD9NNcp5+uWD3QpPOKOGOex8nHuW4wqrSjKuq"
    "j2kBk/Lz4zt8GiCMubsItJkqGiMkrmcjYUobCmVBTX+UIUYZa+0+vucgS6UXjMBxwPM8PM8nzxVg8ByHojAEvgNS0h3FzDRqKDRp"
    "WpDnoNCoYrwUKgg8D89zSNKCwHVQSvGZhw7juA5bZ+vs3tJioVUlLgrW+0P6cUZ7EFMJPJq1iPlGgO9Kti3MYpQmLwpcY9BakRXQ"
    "HyYobVg3hsWWrcLZj1OMFtRrIe2uwkGT5YWtjImhGkUM8iG9QUJ3MGKtO6ReiYgCD60Vw1GGLgyOYxAl31RrO3ZGWc6dkA7GcdA6"
    "R+oMgWdfQFEBQoGTofME5aa4wQhZhGjVRDhVPL+CzgZIb4BKe7hpHT+cJaheS1C5mCI5QtzfT+52cXy/lI0ckDs+wg0QcoTr+uSu"
    "h8pipHTxhYNSKbrICOa28PChJf74rX/B677rVVSiCn/713/F4w2H5ranMzs/w8nVIYHnsdCKOHRijbBeZ/34UeoX7+GWm10+/ZkP"
    "Ud39LIQUxKOCXVtnOPh4GzBUI59Cu4BNgK5Vq2RZRrfbIf78B2kc/SKNvTcxt3gZ/aFiuHycxuIeKrNVVk+uE2jBli1NpMo5UUqd"
    "1msVBoMB2ephTq13LF/ZoucJCB8/NseJo+NHmCwdVQNopRHORhGjklsDgo0IyMTZtVF7x7HceSnLSPBU5dTNiiVWdnKjPxufa3Na"
    "HOQsyPtMTD2G3RsFn05v4smB+Jlx+K/Gu991HNa7Pb7zlS/jJS949oRjPuaxJ0nKr/y3P7L9KZ9Lv/BLv8373/4/qVYjxpVIldLM"
    "z83wS7/w43zPj/wCBD7nGytVStGo13jvP36cT3z6bp57y40TNRulNbVqhZ97ww/wvT/677+CI/Hkpo0gdBSPD+v86mPX8B8vv5/I"
    "UYxK8C6FIdbWqZPC4Am7StovixONaS9j0B4rh1977GoOj6rU3I1kUwO4UjMsPH7p0ev4z1d8gctqI7r5Rjs2UdRG/L0S9CfaOqhj"
    "J0CVSbWRNPzRkYt559JuqqW6yPnMrbGzHDiaO9sLfNfOAxNe/dgsNUjy6TFvnq+9nDshzq/y6T+ubOdseSZPtP/pbXw1q6cKnrhy"
    "Knz5qqeOj1cXZ8qsKgz5FGgfN2+A94xOUWA4W4ky2/+zV2S1fTfMOT6/0n6Mf07WqGEB+EAX/PTaw/zu/NVc5dfpaLvKIRFkRk8i"
    "917Zn5HRmPKzcX99JJGQ/PfOIf5qcIK62AymDYZIOPxW9wALjs+3VBfp6AKFmbTTKws/OYzrhTBxDsZKNBLBrPT5i8Fxfr97xMpQ"
    "fs3dIf9nmLttvoFAEPoOBsnyWp84Vxhtl+kD36U/sDrvWa5KQK/wPJddW5sszlY5cKLN48fWMBhcz+WyHfPMNyM6ccxdDx2j38/x"
    "PWcSHRJQKlBYs1VBmXqhj++4UgBLiDMu70aiquX7lnl01pvFlN/Jibxj4HvUKhFJkuJ6NgIWBh5+qaSTFQVpWqA1rPdGhL6Lwkb8"
    "tdGlGo0izSWh7+GUXZ5tViygd10Cz/LNv3hsjUFasGOmxuLcLI5RVEPrtLQqPo4T4HoeWVZYpwUolMZzra58FIU4QjJMEk6sddBG"
    "sNJLaFYrdAdDhHAAQbUSkqZZWXxH4fouplSZERo63SF2aAWuYwFdpnKbWe9IwijEGIhHKeM0G21kGZVXCFEgjUu3cJFOgecqpFOg"
    "hcJLfbwgw1Mx0q2gsibSi3C8EYUX4eUjirSPE9cIqvN41WvwKvso4gOMuo8g3R6uH+D4Q/I0QLo+KvERjo9yA4oyCm/ysj8qI2rN"
    "cXS1xx++9S953Xd+O9/1uu/j7X/9NjrLa1z3/FfSXTtGF4/L9m4jq1U49uBh6rUKwzjm5FrAc55zC3fe+TmyxRsJowrtlVOkSQxl"
    "IqLrhJDlIGw9g8D38T2PYRyzdmI/SfcE9R1X09j3TFIyukVIvLTCwnyLUa5JhwlIzeJcncEgJTealptx/MRher3hREpwwmOnZH2b"
    "jWj1+AYZR65gzGG3D1CrDrMBsDfuoY1ot0141eVtUBZKMhu8eEdK+2A2bNpnfHyDBZATrj1TL8FNoHvD2Zh8Oq6EN95+ck5T220C"
    "9GeC9H8NE0KQpCnbt27h/3nT623iuwEjrAqL6zi85W3v5PP3PMhMyyrGVKsR99z/RX7jzW/l//v5H0MpZSlpUqCU4pu+4et47be9"
    "lD/7639gbrZJUQZgz0Zbmf59XPTpN373T3n2M68vQYil7Nh2n8eLn38rH/znO2g26pvaeKJ2v9ymjaDqFnyqvYWff/hp/PQlj7A3"
    "GjHUUOgNqdBpAGvPpSzRLgx1z3B4FPFfHruaL/RmNoH26eMEUrGURPzMQzfxU/se4rbZNXJjo/d6okpzJkRUxkbnG66hU7i8+cAl"
    "vOvkLirOVBXuKTNs7u/07xaUKo7EVe7tzXLb3CqDcuVgrABz93qLQ6MavrMhVflEbT7R8b9cwP/0tgQwfAqVT893/ydq43z79lTO"
    "+WxjtFE59Uz7UqunnutaFOfoqcAmihosX31W+rylf5QPx6vUhEteuntn7T9nr8halM/6kVFTjpYhEpJjRcLrV+7n/525jBdFc+QY"
    "EqMnhZimpRmnj+MiaEmXNVXwK539/PXgBFUxzp7YfP4Sq47zC+uPsKIyvqe+AwfB0KjJcex5b+wzfY514ZKh+a3OQX6/fxhXiLPM"
    "ngt2vua2BzFKgyoUUghcz6VRDSmUJk5zC1bTgjQv7Go4htD38DyXEye7PHpohSJXRKHHlvkmF22fZdtcjeX1Po8eXqHTjfF9x77I"
    "xxH1sy2dT/FILY1AYIwu5eymu1yC9U3L92UTY25uOU0dRxJGHoUy5FnBYJTaSZkVZHlOfxjTbFSpRoI0LUiSgjTPrRLDIMWxnZ5M"
    "XNd1yfMCfINSdlm7M8yI0xTfc8mynEJpcl1w5MgSc06Ti3bvxnNdBgNBXhS0+11i1ccAjhfSqoRUIx8pygJYWjNbr+BIl5lGhf3H"
    "V2h3h7R7QxaaNXTpSIxfiMKTCAXDxFa6DXzfFtEqFJRRdYHAcRwqFZ8syxjGCY52SUlxHYcgcMkyVQIPAY6HMRqDxOjcShZql1QV"
    "SMfDcXPSIiNLfLwgIggKhJeg0wq+X8ELaph8hMwrONkQlQ8sBz6cxQ2vpVW5mFH3PpLBQRzfx3Ujci9ABSHpaIiTJwjhojwfUg+T"
    "xUjlofOUejNgud/hf771bXzfd3w73/29P8Bf/fmfcN9HcnZf+xJc3+fUqTbzC3Wi0MfkEdmgjxGSR9ohN954PV/43GeIt91Cbc7n"
    "0CC2+Q2VgKKc31I6ZGlKEscEUUij2SAejejHGb2H76R79EF0fTeX3HItg5HmxKk+zWZAc2aGA8fW8WVGNXJBumTrS5xaWaFQqgTu"
    "G3Eso8dOacltL++PcfBcl7keTikZOU4OHQPj6WX68X5i6j6SjmOlAylKZ48JBcYxDnr8SBdiAg4nK1+bovJTRznj73F/p+7pyb1u"
    "NgA/0+BecMar5F8Zu0thc0b+/Rt/kJ07tpaf2k65jsOJk6f4nT/4CyqVCFMmqapC0WrW+f23/A0v+fpnc+szr5+05zh2vH/53/8E"
    "d37ufo4dPzn5zHXdctVw46RddyN6p7WmXqvysTvu4j0f/DiveOnzzmj3F3/2R/j0Xfdu4s8/WbtfCbOANecLvTn+7f1P59U7DvGi"
    "hSUW/LykFVBKGNrRtAmC9ve13OU9x7fyl8cv4lQWUXOLc9JWNDbCv54H/IdHrucbFk7wLduOsq86wJeGQtuI6vg4Qhi88jjdQvCB"
    "lQX+8theHh00qHvnpse4Zf82/p6SNjQ2qp9rySfWtvC8udWyOJJ1Xx0Bn1zfQmYcIjakMJ2yTT3VpnsWbr3ATL5zhAVm47H6Uu30"
    "Nsdmz+nsoHu68ulT2f9cbTyRne/YnM2mr5U47fOz2ZdaPXWsHnP6cc5mdu5tJJO2dc5vdg/wh70j+GWxuydr1z3LiqSDIRSS010O"
    "BUTCYU3l/OTqg9xeXeQ7azu43K/iC0lubBXTMeNRIvDKJNe2znnnYJk/6h/l4axPXXpngPaxGSiVa+C/dPbz6aTN9zd2cYPfoCJd"
    "lDHkmEkwSQpwcfCEYKQVd6Rt/qB7hE+nbarCuQDa/4Xmrq5bTXbPdXAcAWlBpztCGxtpMmq8mCFs1VIkulAkWWGX5IWDF7o0mlUW"
    "5+qEvsNnHjjC8eUOxoDnSCtfd9pcnHDLDEzqpBtR/j7l25e0DtuJM59im1Q0hCjBjtXHLrRGFIJqtcLQxFb2zBi0tsqnUjqM4pxe"
    "PyYKfIoycXMsnWSwMpQY+xBVqqwkNswIAh/HGPrDEcZoBjoldCUVN2NnRRM0PdI04cChQwSej+Na0OUKqHtgNKy3T/K5I4YgqLBl"
    "tspglBJ4Nppfj3zmm1UWWnUkMExaPHpwGVeKSXQ0STMc11KBHFeiUwsmxsVxpJA4QpDl1sdPC0W1WqVaCen0RuR5Rp6D5/mIkhZh"
    "dJmAKC2oEzgYo8hVgeMo0DkYD98PkFKRJwl5FuJ6PsiMPEnwwxg/qOLkMcaPQaWoPEXlI9ysixvOETVvIahexLBzL9JdxUkDsqSP"
    "EC5F6tnrl/k40qOQLrpIEI6LyVOq9SaDZMQf/unf8F2vegWv+8HX8+d/8lb2f3bIZbd+JzN1n4cPnCQMfMKGz/HDfaq1Cu31VQ7J"
    "Ldx862187rN3ErcuY5ik+L4gCiNb6MuRxKOY7Tt3sLCwhUazycHH9jPq9ahWqgx6BUePHOXk8ue585/fz9Of/0L2Pu35GK/G6kqf"
    "eiVAoOiNMmQg8bN1Tq6s4Lkb/OdxtdMxX30c8RYTJ9VMLTqJkmdugbwUG4Af5AZIE6WcoxlXWSwd3zIHYlKIqaRyjG8kx5EUSlkK"
    "Wwn6prnspy+Wb9IvZwzOxQYVf3KvmzPuz7O+9oyY2v5fB71LKRkMY2579k284mXPo9cfTMZizF3/td9+CyeWVmi1GpOkUINVVlBK"
    "8Qv/6bf56//1X6lWI8COk1KKKAx40499Dz/587/GuJ5kt9e3akKTvAYxUaiZNsdx+K3f+zNuuflphEHAeKVGKc3ei3by6m95CX/8"
    "5++wzgTmvNv9cpsuk1V7hcebD17BO5d2cfPMKtfUu+yMBrS8jEBqCi3pFD7H4goP9Zt8prNgo9NS26qmT8I1t0WT7Pvo3cu7+Mja"
    "Vm5srnNjc42LKwMWgoRI2oh9v/A4nlR5ZNDks505Hhs2kJgnBO0Gy2EHMaFQeMImYo5NGUHkKj7XmWP/MGIuyMiVjeqfGnp8trNA"
    "KDevGowKl36hyMs2z1ZdVGCrevYLl0ExUXIFKIsvPXU7W5tPZtN9+1L2P72NJ7PzGZuz2dmu1ZPZl1I91WD12oEzqoGebtZRNQx1"
    "wXGV8kDa44PxKg9nAyrSYUqE6ym1C9bp8LWcaKtvOi8MvrCg+n8PlvjgaIVnhi2eGba41Kuy6ARUSk33ri44UsQ8mPX5ZNLmoWyA"
    "BBrSe1Ku+TiAWRUuH03W+HTa5ka/ya3hDJf7VbY7ITXp4gADo1gqEh7JB3wybvO5tEuOpi7cyWrEBfvSTTSvfpkptLZw1ZQRQWG1"
    "ooWwiT5oXVZXLd/KxkI6ZQyOAwsLLXYtNuj0Eg4eXSVNLTVmsvw/zYuhjApOPhhPw9Mu5SSCZ6ZC8wJO85bN1K6niT9MthDCmSwz"
    "W4J9WVV1OslOlNwswYQmJIQFJbZK6Ubo0BhbjdUpl8S1Miij2Tcv2N60D1kjfYz07e/KTKKnRiuE47DvksvI05Sl5SXuO3CKtaEh"
    "1wJHaCvJ5XrMNCIu2jrL4mydvNA88PgJ1noDW4Aq1zRqAVmWk+bFpNiLKdU/nDI8EvgeaZbhSAdtNNIYPM8hKwyuA0WhyHM1kbqz"
    "9Iixiom0qx9CgrBUKulYJRrP82i16vheRJIpRpnB8yKkdEkLDz+M8IIKnl/BDeq4fgXpVXCDGl5QR3gNgsoiji/IRg8Sdx8jT2J0"
    "lpLHffJshEpH5MmAPBmhi5QiG6HzBFOkoDLSNMbEPV77zS9i567t/Plb/4zYVPjG1/4wBzuK9WNH2blrnn5vxGAwIh+1rRJOPOKG"
    "SxqcOPAAn7/7ATwx4hk3XYP2t9LrrHPDDTeBEOw/8BgYw1pRULv0Chrz8zbC0+2QH1/i8Qfu59EvPsjswnZe/K3fQ/2SmzlxaoAf"
    "SWS1CumA/v3v4+Pv/6BdtSjHd2OKChw5VmopAfAkedRGzMc0GhsYP02uETE1h6fvpfLaUU53xg7CNKWgjIBKy50WMCkUIzbd6yWA"
    "n2ScjnWkLXDfaHeaaz+9rsB4KaDs4cbv4/5OOx9j5L8B+OXYg9kc6f8ym9aGWjWaVJYdP3PGz5Ref7ipANO0CSHI84J6rYLjOpse"
    "ZcYYXNel1x9MnIBqJTqjDWMMw1F8RrtFoajXKhNN/cn25Qj3B8OJk3G+7X6lzEYbbdJqohzLKXcKPKEnQDQ3VhYy0w6ho/Clpaw8"
    "1Re5LDXNY2UpGVWnwJf22WmMVTqJlUuqHXypCGW5ovkEEElglWOmCTei3CdRm3W3DRBIjSs048oFyoiS073ZQkchT2tzXF3UTLXn"
    "C40nN9ob/59NKqc+NTtbm0+2/XTf9FPc/2xtPNke5zM2Z7PTr9X5jM109dTsPMdTYCPa5zv2GktDSYxiqBWBkIQl/eR0R+2ptDsO"
    "8GTGkJ0FvI/NQVBgGBnrwNekSyDkRKEmRxNrRWw0oZCEZY7TU+Way3Kf2CgKY6hIKx05TlotMKRGM9AFrhBUhP3mAqf9y2OiftVL"
    "jZjwLqbh9NTU2BTwLl/MRuP5PgvzdVxH0u8nrHX6CJwNXenx+3jcttlo25SAfBPl5YyA+rQO6vglf/oy1/glv7Esb6lsU4mvWpSd"
    "mDoQlhIwKaoyrp6x6bQ3Iu/ocdt64nlOHApjl2pnq2LiaFy9TSJwUEbgeC5aOeR5gSOtnOSOnTvZvn0baRwzHA5pdzo8dPAYJ/ql"
    "XrQxOK7D3EyVHQstvDLSPogT1roxp9b7BJ5LFDisrvZsMiIG13HJsgyrOuNQCT3iLLdLr0awOFflxFKHNM9wpCQIrHOhtaYoCrQy"
    "G6GVMhqqhUTi4LiOjVYJByElfhBQr9fYNlvD9wMOnYppNWoY7bA2VECAE4R4fhXPq+IFVZygivQseHeDOk4wQ1iZw7BO3L2PdLiE"
    "ynJUOiRPhmTJgCIdUSRDVBZTFAmqVKNBWX36bNDh9hfcwjVXX87b//ovObaect2Lf4BkMKBSkxRxTFRpsHziJK7vMeqvs3P3Trz1"
    "h/jwhz/CtgWfa669jn4aEngOL3rRi3j/e9+H47l0qxUufvE3ctP11xMBcZaxOujTWTlFfnA/S3ffw6c+8XHiQYcrnvVirv/mH2Tk"
    "BozihC2s8eiH/jf33vUFfD+wFKcxMC3HeMJf3xSBL51FOZ3EOp5s1rEag+exo23nur1eUm4unCRl+eLQY378RoEju6w5fnVuRNPH"
    "jsAGVUaUToBdydnEfZ8C4mIKoJtxj08H7mXfzwDxYnxTje/pjc82b/uVMaV1uZoxDUDs/2OKyrlMCGFX7Mzm6JkNLJhNlJVzyTie"
    "7Rhj8G44s93T+/VU2v1KmoCS921B7xiYj4G9nHz/L69hOa1Mo78MxzlbFdDx+Zxup7d7vtuN7XStc4M4a5VVeY4iR+dj52rzyWzc"
    "ty91/+k2nsjOd2zOZk9ULfeJ7KlWT32qqicCC2zHabnnIuZ8KWoqArEpcn+u44/XQxVmU4RblvvLJ+nb+Zo8x3E2jwEXAPuX2dwN"
    "bWaxwVcFNiHYEhjbf+2FdzyfWi2k10/o9WMMAtdxJ/ttio5NB9TYiNBN29nfyeIs349l9Nh4s4IFM8JsgJ6yz0KIUpFj3P8NdC5K"
    "sD+OKtpvbKNmAvDLT4RBOHKiDDIGWwINQiClYW0ISoMrDY8ta7ZUckLPkOcS1w0snQTwPYfhoE8cN/G8gFrDJU0TLl4IqAYFj60I"
    "MgW6MAyGKY+OVlBKUa34BJ4totJsVGnVfNbWhyBdG5Er9feFsFUvDcIW1HLsC1SrgmMrXYQUNBt1lFIMRzFCQBSGVMKAQW9kpe9c"
    "h7Ez5EqD1gVaa6v8UqQYLUmUQhc5rtTM1KvsmnFYGQyoViM8cpIssTSZLEGFMbqIcYsYN0hQxQgvH+EVQ9AD3GCeysxteOEXSQaP"
    "kLsuwvGRjkfm+kjXo0h8ROIhpY92PYpkhCddZMPl7z90J/1hzGu+47v5u7/7G+76+9/maS/9frygxtryKs2ZFjNzLbr9AeChkh75"
    "aIBWGj/wyArDzc94Oi94/tfxsY99gptvvpm7H36Q5jXX843Pvw3aq2SOj9esU6tExHNbWN++m8biVqrNJnd86tMc6yzBfR/i8me/"
    "lKbfRD32BY4fPDyZqOMKpnZqWgdPlYV6Jk4m4DouyiiMNni+j1LFhFozXrk5/T7RmlJJZpzXUN40xjrZY4A95rDLTSDdlEDflH6o"
    "7asYO9ZTFJpJG5NbcLy/2AC85b20afVr0z22+RY+08785nyjav8Sc6REOOfo0ZMkeRpjcJ8AIE/vfy7e+dmOYSP2Z2/39O2fSrtf"
    "STNsgKrTwaw57ft/qU3TXs4Ewk/9OOfiR58vuHwqIPTMu3gzv/6J2jxfO1ebT2YbAOxL23+6jSey8x2bs9n5cuG/lLY3HedLePIY"
    "nhyYf6ntns820/H90+P659O38zX9VTrOBdts7pgna8rI1hkPE7HxALaRPfuCwxi63eFED31MK5neZxrsiy/bq3cc/SvbNhufjpu3"
    "FeuszzdJphP2942iN6YE3KXXPwYWk4iZmfxr27bj5IceAkESp+UNMtb+MLgu+AjSXNFJXeYbHoOioBaUyblaUxQ2khrHMY8/foB6"
    "tYofhigjUATMhClXbckZppLloUt3mOCWRXSyTOG4LkrnzDQqlnPvSKQjKZRNWK1WQvr9xC5ZCUBqHOlOFC+0Bm1stVnfD4jTAiEN"
    "SZrjFAVbt7bodgYM4xTpWH/a6DLppDDkKkZIF6NzkDZx+eRyRpFnbJufYWvTZbU3oD+IAQfhKwQF2SDFhDlKpxR5bBNYdUZRJBQq"
    "w89jVDGDG15KbW4rcf8+MmcZx/Nx/JDM9RCOh+P5mCwmiS19R+UunuNSn/P4p089QBynfNsrX8X73/deHvzo29h94zezZcduVldX"
    "QEi2zM1wZBATuLA6HACaejUkjKrs27eXAwcOculll7G2copYwO7tOwnShP053PvYY3QPPIrOCxzXZWFhG1v3XMLul86RX3M9p7oD"
    "RmvL3PPOP+aaS27AbR+n3e6W9IsxzJVsyukYw1+x4TgXRWEBvrA8dZu4KjfuzSlVlnEy6piPPT23xzfGJhGXEmSbqVt002Lz5o03"
    "ubmT/JNyBWAzeJ/q2+R+MadR107z4De1f47nw1cDsU8f7l8Acs9336d6jK9Uu18t+2r16stxnKfSxvlu+5Vo86nYv7TNr+T1+5e0"
    "/X/SvPpqtvv/78e5YOCactl9oiM9SWyCySt1nIxWRsyKMR/a8XAdygi0BQ6OY5fR0zTHdR1cZwxINjhl0wsqYzm6abxwtvfPZu3p"
    "jb7Zfc3UqoAAWXJuNRO6AeXCUCWyxaYc1yXPc5IkQxqBMBsZ0dZJsdFNoU3J7zdoDaNRDsK6IlIKhMEWkSqBly455IVS5DpgW9Mn"
    "V9aZKIqCKHIBh1pjhkajzrGjh2l31lBa4vsOXqVFpe5Qq4bMnVzhC8cESm84I1orXMelKOD4Sp9Wo4IX5Jhymd4mlkqU0URRiFYO"
    "WZpPruGYRjGMM4QQ1OoVjFLEaYYB2r0Yz/chtd/LUlVHqHIxzIBR+cSB06pAqYJOu81gGBNFEbONiG2zAYNYM0gGOCrH9yPyOEer"
    "FOmmqCLDKxL8MCErUlQ6wstivHyAX1kgajwHPzhAMngY6XpIN0C6ATqLUdkIIx2K1KdwPIo8RsiExuI27njgCMM45+UvfTmV6sf4"
    "xMf/DPncV+KHLTSGdqfDJZfvpVac4vBwhBCGajWiUm3w/ve/j6Wlkzz96U/n4ov2EPghRZ5SOC4H1tZZff8/oJaWEK5LJuHRap0T"
    "1z+d3c97IfN79qEfeoAH77mbU/fdj3/8CM3GLKpQ+IFfXhsDxlZCtai3nEeOTTiU0kFIJknfCJts7Hm2mq7RZuNemKKqGOw6lBBy"
    "cv+OP0OMOfPju886A+MF17HE5OSxO7UaNqHJjB1iKa2mvLGRlvF9uDlnBYyw99NpdzCTVYfJTXba109gX0XsfsEu2AW7YBfsgn3N"
    "mjtJuCqBp41AWz1UZyrCbsqInhTC8ha1plCFXc73XKQU1GsVCqUJPZfKfINMKUZxbrXf84K80CAs99piXYPr2mqPUlAWfNlwECZw"
    "YAoETFYASrRvab0lb1dYRpXYBOBtkp8jpU2kna+zZaZGb5DSHsT4vke/F2MElos5Bj6mTKiaREeZUArG46X0uL/OJudBYlAGDqwW"
    "JKmhVTHMVQTIHKXA8z3iUY8iTwijKlprIlcCDtJxMSpH4yJL6arcSMaJhbqMfnezmFajQpLkoCEIQvLcFszyPVudNh7ZCqtRGBIn"
    "CQJbQKtZj8iVQqsCrTR5liOEYMtsgyzP6fSG+J6PK2GmUWWl00cbiTRm09KYVgWu6yCUIY0T8kyRJinD4ZD52SaNKMB3HUZJRpZl"
    "IAJAoYsUU2QURYouUrwwA5NgdIrKE1Qe41dm8aKLiGYWkf79yOEJpOOQxwFGOARS2uquwkVKB+W6FGnKlvmc+w6tYP7h/dz+8hcR"
    "RhU+/E9vZ9e1z2fbZTeyfPQoMwsFnsjpdjv4gUslqjAYZuRZxtzsDGtrazTqdRabLdbabWIkIh7gpzGpYxOdC8+jdsU1VC+9nPb6"
    "OjMLW9jeqHO8iFnqrHNsOERvt9xm69C6pTSjOZ1DMhUpNVAmiGutJ1VxJ1VUN/Yo/xYb6QjGMK3YO33vCDbUUSxVZyqRdMJh3xyx"
    "HSs0letbtk+qnOPCII2YgPzNDq84q+O9ycSm/zjzrwsw/YJdsAt2wS7YBTubucrYilai5NDmGgJHUqsEDLIcXdgKnbrkWsZZThR6"
    "+IFHJfS57KItNGshldDn2KkOw9TQiiQnOyNWl7tWxsh3WZyrEQQeURjSHyY0qwHSERw+2cFo6HYHBKFvCx6Ni78A0pSMginKztiM"
    "mEYAguktxhF8ORWdVNpwbKnD0nIP33cxGvzQI6qGxHGKUVP6tRMFj3FksfyrXF2wQF1OQNiGMoYpnRKB0gakoZvA0Y7iooWQusgw"
    "eYzjBxRFzszsArV6jVNLR6AsF1xoiOM2jhRo4eI6ZVR0TCLGRj/7w7SkUYDvuyAEo1FCFEVWZcZoHKz+d71WZTAa4fsBxoBT8mEd"
    "R6LxaYY+650RlWrIbKtONQg4vrLGSqfP7EyD1dVuGdHVGzrWWmOMxnU9pCMwFBR5gSpylouChbkmlSjCCSEpIM5SdK5QJsVxE5yi"
    "gilSlMrwixpemINKMSaz8pHZCL8yT6V+Cyo8Tty731KDPB+VBEgnQLoeKvUYjXy2hF0un2lx4HhGpA9zx0ffwY3PeQWVSoUPfOB9"
    "FNowv+NK0sGQgeoyHKWEvkQ6HkVhcwPy3K5ceJ7HYqvJo4cO0R0mzLVmWa3XSTo9cq0JrruBma/7elRRMFo+ycmjh7n24j1cf+01"
    "nHjgAbrdHoPhgN17dnP82HHiOMb1PFzHYaPo0nhei4liyabkxnISK1VY6slEOnFq13KfcZKrna8bq2fTvHozdcxxM5NE8vLesZQb"
    "sylJ1egNh5pxxNx6tWXkfSpKb48Mk+NOcXJOI8xtYsGM5/eZ31ywC3bBLtgFu2AXrDS3VQ1xAw8pHGbqAYM4Z7ZRpT9KGK71SLKc"
    "fTvmCSKfoyfXuXrfNrbON6hGPmmuOLbSJVeaapwxWwkIizUKU2fXfJPLtrZwXYdavcKOLbOcavcZDC14fPT4CqNRTjUKCD2HZj3C"
    "8RyyNGNpuct49d31HKtNPH7xT0UIJ692AVJYvXEpbKKe50mM1ihtbBXIcn9ZqjQopXEkKFUgXQ/X8ynIMVpP0Q2sUzPhvosNbecx"
    "+Bn/PSleg7RReqxax/4Vhe/aVYsvnixYqGoWaoKazEAnHD3cZmFhK9Vqk3jUJUnSUpdWsb8ToBE4jkKrsUZ36dBIqwQiMEjHIU4V"
    "SivqjQp5qqxed2GoViIGcUKepriui5QSx3XIUkWaK2QgmW3VMIXGSEtxygQM4hQpXVxP0G4Pxl4QjpE2E32coGgsBUg6JbWoTNx1"
    "hKbX7xPHCW4QEPo+lbpPXFgt8n6ckaUamWXowqrDBEWGHySIIsMLUzAZqojxwhm8aCvVuTnc4EHSwUEKz0W6Nnk193wi6ZDrgFwu"
    "cdG8plXfweHjJ/nsR/+W629+Gd/w0m/iH9/3bvIk5dJrbmLYWyfNMqKKA7gb0WkB8WhEUSjmZ2doHj/OfffezTU33cT6pZexdugQ"
    "wo+QUuJnKcuPfpHi4H66p06xvX47c5dezmWXXc7n7rqLlZVVqtUaT3/GTZw4dpSl5VN2hUTYQmeudErnZzrSvZnyMo5qb1qFmsa1"
    "Y57ZmEMvNqgrk0j6JgA9bdbJREzLL47VY0q/YYrDNlY2EUKW2vKbAfYmqcvzwd3GrmidDu7P5NFcsAt2wS7YBbtgFwzA/dYXXM8g"
    "zvCkQ5KlLHdHhIHHgqpx+UWL6EJRq4TMz9RohD71SkBvmHKy02eUDtk+12LHfIPO2ik6vS65Uuza2mDnzq20qgEPPPAQnaV1Djx4"
    "H5deeRWuH/LRL+ynEvogBIUydJIRaabIco2QDq7nWc62EBY6SzBlZHkcmfMDlyTOLBB1BP1BhuNIpLRKHRscXEPFk6TKRhwdz0Ua"
    "W9LeGFBKk6tsooctyqS6MQ1mWpRgurDJmIowDeihBNcYjDJkSnPJtgr75h2KpM9aImn4LgKBIx1i5eF5ktWVZarVKkK61GoBtchn"
    "td2hO9Jlm3Z1QYoxP3ncB4EbukgBo8TSXbSrCUKXNEmp1ausrveo1yu4rkDlhkIr4kwT+C4zlYAkzTi52mdxpkqjGtEeJHiSSTRV"
    "G4njugitSbLMSkk5Nl9B58XG2OhSXtORqKIgiWOaQQMpNcIoMIo4GVGJAuqVgMWWSy8RDDPNKO5RZCk6yihUQoWMQmWgMrTOUEVK"
    "kdvoe1C9CTfcSdr7ApkUOF6AMxRor0Ft/TO0D3+OK6/YR6efEYQR6yunOPjoJ7j1ed9KGAb8w7vfxWpVsNgwuEIThgGOF6CMBdCO"
    "4xLHMWma0mw0uGHvXv75jo9z5dOuZ/fNtxAfOsSBxx4jvv9eDj78EJ5SiOEQPwoZdtvM7tjB1n0XEz14P8NhTL/XxYjd3Pz1t6Pi"
    "HktHH+PIwUOstTsM4wQhSknOEqxv5GyUDuOkuqqZzEernDSek8ruC5P5bvNH5QTkj0k0kzlu97QR/Mk83gDe0gibt1E2OlGOYUyN"
    "GTeyQZWZ8N3HRzhn0Pw0sH/GL+O4/GkfXrALdsEu2AW7YBcMd9fCDIUGRxpWewl4ATPVgNB3WeuOGCYZ7V4PRyg6SJJCI4WLQBM5"
    "gppvWFk+jsozCunTWtxGZzCk88B9LCwskBcFKk9otFosnzjK/Uf6nEpcLl3IqTsZDUfQqgvuWpIME00j0ihjgbYUAqkKjJA4RpMW"
    "lvMbhQ4IhyAMyLMc1/O56YoZsrgPWhCGIbWKj9QFjoQkjbnvREGcKOqeIC40ibGJtcJoCqVt1ByDLJP2bHl6y3sXgkmBomkpvNP5"
    "92MzCFxPcvVixNV75jm52kf7LfY2BIM45tFVwzYkvThnseEjRcIoGbE2hNWhxvMirt7Z5OptPe45bnDL4j3SsdVelVJl9B2y3NKK"
    "5lpVRmnGKClwMmVXKjTMzTZK+pHBDwWO0qgiJ81ykrTA8ySB57K8PqRRqzBbj0iznE5/RLUSkKY5oqQ2V6LQOjwY+5lX8ra1Lh0W"
    "iZACpyzq0+8PqFQiRFoQxwmFFuRZDgbmmzV2tnxiZWiPXE6txeRxgS5SVJoSVDN8neFkMU7UBF1+Fwzxo61U516EH95L3N0P4V7m"
    "Dr2L+uhOdFinvd7mkcNt6tWQS694Gs26QGUnWZyr863f9u18/KMfpqPr+K6g0fDxgpA0ZqPKqIETSyeYm59j69wcO08u8/H3vZ8X"
    "f9u3cfGLXkJvvc366ipBYGlHlFQV6Xo4YUQwv8DczAz9wRClFMkoZSWrUvhb2HLNPnZd02d06jArJw5x9OgxVtbaJGmK47o4ZT6G"
    "paiUgFiMpRiZ6LtPQDobKz8beH+Kd16ekBxH4afAsJlQXKZWcoR12CYrTVCG+W0ito3eT2WgiDF8n7gDIDacgjGgn1pTOPv/U3h+"
    "EyPoAna/YBfsgl2wC3bBJubec2CJqu/iGIXUGZUsI8k9ZKMOeYJnFLsWZojTjG57lW07t5H3eiwdO4oRgnWlyNOEy66+hkuaDZI0"
    "43h3jThOeODkGhXfQQnBnp1znDhyGFcWPG3vFippG9cR1GcqDEcJ+2YUy54kkxGjUcrTdgZInbGm6jhFTL1eI8sgYMQj6y4izwlD"
    "l2t31DnVSdjaDKjOOAwGffxA4nmS7lBbzrLKqQQug7jA9zz2zmYc6AjiTJEZB6Qg9D2ElCil8TwXYxRKG3RhI+9aa7TSZQTeTCLf"
    "01H3caRUGFNG7gUfv+8YgS/ZsxCS5tY16AxTlrqSyBMEvstcFHDXEYEWtmBTPEhYHWRctdUh9AvyoiycI2z7nu+TZRlCSsLAR2tD"
    "pRoySnN8z8UPHJQyjJKMahSSJAnKgFCKKHBRhcT1nJJWZKhUA1w3ozdMCH2XauSzIww4dsqC3zy3NJyisMonrhTMNquM0pxuWclV"
    "SFuR1kpHlhz/vCAexkSVAK00ge8zSmKrRKQL6tWQRhSxUPeo+iGHTo4oEgUqp8gzikpKEKZ4JWh3wwSjMnQxwg1mCao3I2qX4H72"
    "ZwnWPkLhNAhdQbuXkqcpC3sv4+KLL+HRRx7m8PG7WF16mOuf9XKe94IXcdenPkq13kRpH4OH0QojKfntLqdOnaLX7eHMtLj1qit5"
    "x52f4cGLL+Ly657G7pe9DPPhf6J7cnmSwM3iNi66eI8d0yCk1ZpBHD1eVrQ1SEeSJgkdArQzg6lGLD7tSnZcuU7eO8mxw4+zdGKJ"
    "1XVLlxqDeCkdC2SNwXHkFG3MmijD6hs0qg2u/DgnQoyLLo0/K7PBTVkxVUpnAvxNSbsZO6UT8F/O9WnqzNg2Vp0mvdrEbx/H6iff"
    "TX16VjuNy3/BLtgFu2AX7IJdMGvix37+V8368nEGnTZJnDK3sIDXnOPE+ohtcw12zFQYJSlLx0/gmBwnqHDi6GHCKGR+bp5RkqGM"
    "oV6JWF1dZT3O2NJqInTO7Nw86+02690enuugFHRknS2hJiRjNIoJQo/55gzHl5agtZ3lXsasr2jIEdqvIwUsVCW9RNHNPQ6eSghE"
    "xuXzDklhEJ7PXMWlO4hxHYew4uFJiKIKWTIiy3J6meDxjsfBY2vccu3FXLu7xsGDh3Fcl4NLXVYzj0L46CKziXjjam7GIBxRgnAb"
    "7dTjMnIllcDy2TeUQSbRTgO50jhScNnWgKZvGMYJM80qKk/53KGM3EikdLh+l8PRtZShCZlrhLQaVQJHstKNaVR8Di+toY0hHmV4"
    "lsdik0q1BT9WRUbgOoJGPUQVBZ1+TFYoKoHHji0N1joD2p0RGoPvSlCKfpyjDQhhCygZo+kPEzxXMteqEbmSI8sdW/RHGIzWZKXM"
    "Z+RJCmVwfc86BoUt0LQpgivEhJJUqUZEUYACfMclcD2k51IJA7bNNtA4jHLD4eWYQQKeGyDcANerElTqeEENN6jhRnWcoIbjNfGq"
    "O/Ae/TXEob/ChHNoleNKq1I0ijNc30cXMcMYbrl5H9Kf5957HmB++2VkhUOv26HX77Nj+3aUKp2PEoQqpQnDkFuefSsYQ2YM77r7"
    "Czz/1d/Brov38vDDD3DqwYcYLh0njiIuf/6LefaORR5ZbXPgzk9x/CP/zOfvu49GvcZVV13L3LUvpd3XNBouRgvyJKPAwfUFrYqL"
    "zlIqYsBo5TDHDh9geXmZ1XYXpYyNwjuOlR8tk54nvPdx4HuccFo6jAZjpTxLfGyMjaaLskqq67jkqmCc94Gw0p+aDe31sQNWPioY"
    "S0MK5GYVGUqKmb0BNnHdp50Jpn7fBOrHn09TeSafjbfe+P6CXbALdsEu2AX7v9Xczuoyw04HpTRu4DMsFCuHTzFIc2oe3NfusLTa"
    "ZsYtuOnG6zl54gTVeoMsL1DSpZf0Ic8YDnrkGuphwO49u/Ecy71uzc2zOBgy6PfwgwDyBNf1WVtfs8WECsP+46ssjULq+Sp1EVMN"
    "GwwTxWJVkiV94qzBfUdjMnKuWPDYtbBIoQ3haEiepwgnoFLxydOEJDacKiRqrU9nVDAsoBsLcjVi785Znn3NNvrDlC1bt2N0wZb5"
    "eZaWT9EuHE72HdbaMZ605boREseRRFUf15VlASNDluVkiSLPCpuMWRYO3qAbSJDGAi3g0ZMpUgo86dKIU/ZtCQhDg0kNhTY8vmqI"
    "HIe4n7MOjFLF1RcvcuuOOY6v9xjEFaTncvhoG6UUfuBRrQRUQo9Ta32EdHEw5KogUxphHHzPY8/2WU6t9xkMrQzl1i0zJTAXLM7U"
    "OLrcZpRkGAPt3ohmvYIRtsrq8ZUei7M16lFIexjjl8mUIMmznMKzVIvAkwgCstwhHsaWFCE3ClmNqRqj4QijbAEpr2IBYpIk9AYJ"
    "o6SgUYtoVCJ2LYQcW0/o9If4JTde65w8TwlUhi5SnKJABh7+Y2+E5Q9iwq04GNJMsWVbnb17tvDZLxxi25Yao7iGMgUPPXSS7Zds"
    "pz6/j263T2tmloUtiwA4josxBYVSlqZSKigNR0MevP8Brrn2Gpyi4MVXXcU//f3bufXlt/OMa65laftOVgcjPM9jV+CRJxmDOCVf"
    "XyMv7OpDGAQI12Om1cDxFcKDNCmQHvhG4aBJ05zOUNKa3cqWi7fiLF7LRcNlhmtHWV46xsmlZboDmwfiOhLHccr6BJTourybS8A+"
    "/kiPNeONrdMwrdeeq6Kkz2yA7HHUfiMBvHRGxxH00gEwU0mp00SxsyXPTv8+ncu6QfI5l51JoblgF+yCfXnN1vYo87P0tDTtBbtg"
    "F+xr1cRLv/k7jVKqjLbZwioFLtu3LiJ0Rj/VLM60cD0Xz5Gsrq+h8xzpR2htqEchc/NzxEnKcDhiZmYGpQqElFTDEFnSD7rdHocP"
    "H6BWr4EBP/D54vEO6/2YduayJxpRDR1EkbKSV6gEDq5wMWiOrCXs2bmVWy+dY63dpjAeo0Gffr9LrVYnHvbwHEE0t422Dvj8g8es"
    "vJ/OCaMQDcyE8JKb9lKr2STQdqfPkaOHCYOARq1Ov9+lnxZ88XiPtVjiSIkrxYRPHlV8PK+MfDqglSHLFEWuKPLCatCXxHchLRjy"
    "fSv9pwurYy8wthgTGiE3gJFVqZFEgVdqzgsKrbnu0m24UrC03uf4yQ7JKMNgCHyPLC+IQqekrwh83yOOU/KiwHOtrv7WuSadwYhm"
    "PQQNy2td6lWfJM2JAh9toFA5cZzhey7xKCHXVu5ythniIEjznLlmhaMn16mEIQpNmuTEcYIQhnolIPQd+nGOMIbRaGQnFhsJqwDj"
    "bErheGij8VwP33MIfM9y65sRjSigElboJTlH12LafYUixDgVHDckCALCSgsRNFlYfzvh4F60N4swBUIIRknCM59xOWurfdqrbQ4e"
    "b/Omn3k9H/nQHew/vIIbbStXT3Ly/iGC+jZyFdHtrLN336VopRjF8YQnLh2HJE7YtXs3+y7ZR5HlxEXOncdPsHDd9dx2883MhxV0"
    "llBozVKu+fRHP4K6726OHjzCeqdLIA17L7uKxjUvRitJsx4ipUOcpOQaVFHgCc1gWFCpezQdwWoMg37MTN3HVQO8fI3eynGWTxzl"
    "5PIpBqPYgnNpV2w2QLm1SZVVw0akukxuFtJBa2WvxUTydHM0eyNR1Uxttxk9T/adJHWPI+0bf0+i9Bt7TfoyRvzTEf1xdP2M/cTX"
    "bsR9ukr0Bcxzwb4W7Fxz8vTPxyuLtso11GvRVJXnC/Z/k32tPce+1vrztWbiTT//n40q1VXCKEIpxaPHOwit2LlQpRJWmJ1tYbRC"
    "OIIwjFCFQkjIssxKBjoOYNBakWU5SmkGg5hCKbZvneXgwSNkuS3Cc83VV9Jut3nk4UfwG3MsLR1jtZdw9UXbCDyXx48tsd5PKNw6"
    "izXBQtVntbNGa24rkedQjSJq1ZCo0uDEySU67TZ4ITOtJvEo4cipVerNWaqMkEbTGww4lNSQ0uOF1+6gGnrUmw2GwyEnTiwz02zQ"
    "H/QnAKg7GNAZ5pwaGrqFpBI4xKOMeJBgynL1jiMIIx+wVWSNBkpVEoEkDF22LzYolKEe+uRFzqm1Ee3eaAL601FiVVjGyXxlVcp6"
    "IwQjSJKURr1CreJTaM3ySo80yTYBmqIokAKktEC9UnWJhxl5riiUIop8ZhpVhknCTD1iMEpRSmM5PthrhiZLFYFvQbQ2cGqtTSXw"
    "caRDkmUszjVYaXcZlupDUejiCMlgmFCoHCnAdyXKQJ7nMFYAAsujdiywTOOMyJFcfclWrrt6H5EnUUVOFAUYpRiOhtRqdZJ4RLvb"
    "IddWq/5UN6edNRnSxPFq7FX/RFQcRTk2aXUcvdVoslxz2a4WoxzS3LBr5yJ3ff5h6jPb0d4cedqnGB6nEjho4bNtz03c/+AD9Ht9"
    "du3cxczcPEoVxKORTTh1XJIkYdu2rezevQetFMoU7F9r0640WLzkcrbv2E6SZ+z/wheQBx5j5eBBrrjiCo4eOcr62ip79l1O5ZLn"
    "Mcok1bpHkStcafA9hzAIMEB3mCMdQUtquomm3xvg+4LhUFGthgiVUfEyRLJC++QxTp1aYnV1nf5giNallr6Uk8RWjJkkn44p40JI"
    "KpUKo1G8oQQjNooyjQszTfRjpChlH8WEA7/x5NgA2JPtx3NzQtuZ0n6fAHM2/ubswH0TSP8qUmVcx2GSuHIuK78vSod+XM0WNhLa"
    "v9Im5UYFZOAMSdGzbVModdbPN9nUuUkhkI6crHgotfkYp3+vtd6gEWKvqzN+CJzl+7E5jixX5c59LpNtsEEgVdbbeKLrZcq8j9Pb"
    "Otc+pqQ7nq2P03aucf2XmH1/8oTjdL52rjl5+ueu65AXBY1ahW/+hmchgL//wJ30BiM8170A3s9hYhwAmeT92HHVZxmvr8Rc+UrY"
    "v9Zz7Fz2tdafr0Vza40Ww1FMlo84tbzM2toqjUaDWjXi4IEDeL7P9u3bEAZ8P2B+YbaUUVS4joPwCgqlJ+9kKQRhFOIHHqNRwrFj"
    "Sywvn6LaaLFz526EEJxaWcWrtpiphVx849OoRD4fv+seBipgvl5h90KTB460cf1ZLrp4F+qQjVovbt/K8eMnSIXHTfsW6XQ6LCVL"
    "KLfJjTu3c88993HNRVu5d/9xdl95JUXSZW1tjR21KifWOnzs/oxvetalGC3odAZcsvci4iTFDwIcx6VZr3H42DEib8jWFhxqx/SN"
    "S5FpEteWlBVTgMPzHBxjyDO7YuF6DhJDpux29dDj0u0ztKohjuvwwc8/Sn+U4wpBz3eQjqTIFXmhCAKPSuBR5AWOJ/EDF6VhpW15"
    "+lIKXNfqfo9xtyxfjLrUq+/3laXkBB6ycIhK5yKOc1QhMCjSNMd3HTxXUChd8vBhlCg8z6UW+QzDABAYYSP5lcjjisY2jiy3CVxB"
    "oaDdHWCExPMDGzX2A6q+pN0e4AYSrUutfM8nSRKEUtxwyQ6+7plX0mxa569aa7C6tk4cx0gpCcIawzglimp4SY6rCiLfpRkNqNdd"
    "Dp04Qry+n6rsU7hNZJlAbIO/gjwreO71O/nO7/923vb2jxHS5+ixNaSUxIWLq9bRwyUajQqu45HGfaQZMDe/SK/bJUkz9j/2KPNz"
    "88zNzzMajcjyjCDwWT65TL8/YPv27biex86wwsyoz8qdn+ALRmGyHLpdksEQKR1Go5jllRVmW01ypVBOhHS1fQjlBbooGBaKNC+I"
    "/IDAdWjUPGZDB9PPiAuFROH7Bs819DNDQgXX34WzaztXXBzTP/EYaRKzsnyCldU1RnFKUVhJS8eRE/lHhERggfpwOJwAYEOZSD0G"
    "zSXgnrDQS077mH4zTY+RY5A/VVuAjXzYMpG1fGeJc9NizsaEsZ99dTkyxhhW273zAixCCBq1CmHg2UJuZVJvHKdPiPm/HCaEYDhK"
    "iZN0Mu6NesUW9prKsxnFKaM4nayENOsVHCnP2PeM9hG0mlVGScYoTibb1WuRrXhdRmrjNGM4SkuHTlOJAqIwmDiERaFYH/QBOzZR"
    "GFCJgjPGt90Z2PdH2Z1mvYIzdS4A650BugTrQgqa9SrAOa+XEALPdYhCf1K5eNyPc+0jpSTwXaIwmGz7ZGM/HtdzjeX52HSfjDGb"
    "xvFLaSv0T5uTSYbWetPnGCtcAPBLP/0dvOb25wJww7V7ecMv/vGFCOc5TEpJnhfESUZR5m45UhAEHmFg37XT9+CXe658Jeysc+ar"
    "8Bz7P6U/X6vmdrs9ut0Oa50OvutTrTVxXBftOFx00S4GwxFKGaIwpFarYTQURY4xAuMARuK7jl1WF9iordZIIwj8gELD7PwCzUad"
    "ei2k37ec7B1bmqy3O9SrVfqDlH0X7eFUZ8iOmVmUTmms9qhHLkmheMbTn87JpZP4QUiSZURpzGfu/AyFMsSyguq1aTbqXHzpJfhC"
    "MFtZ4vETK1y3e5adO3bz6Mku1+5p8ejxHp2RoDAD5udnac20qGQ5URjRGwzodfsMB308P0RKwUUz8NBqysxcDY1m0EswgOtIXM9F"
    "OIKa71IEGqUVnuPgug4LnovB0BslPHhkhUt3zrOlXuFFN13OZx46wmp/xLWXbrPc8kFCfxBTaCvZ16paQHDsVJda6FMJHDo9SNOU"
    "EkUB40Dkhtc/LjwlhKAoNJ4rKQrD2mhIo1ml3xvhupIg8MiyHGPsCsO2+TpLq10MkrXOkGGcsWtxluW1HltmawySnJXuiB1zTWZq"
    "FYwwzNWrzNQCDpxYp1DaAuO0wBhJo1ll0B/h+z5pnBKPEvYszvLcGy7msku2k+WGNLX67+12h3qtBsaQF5Zz7boRhSqohFYNJy8K"
    "jp/sUOuNCLKjaDNAiQgHg55wryVJkjHTjHj9T/wb1kY+hx4/xHe96jkkYoV7H10hyHoY06deq9ixUhpjHJJhhyhsIoWDKgou3reP"
    "5ZPHWX34FDt276HZaDIYDOw5xjH79++n0WjYCrQYwrzADIcMhkNGSUJUqeL7HsPhAN9zCaMKriMIh8eIE0PibUdID0cKfClRxqBQ"
    "9GOFkYZmEBKFLs16gCMMHSPAdQjD0kHUkGaGronojQwLF91AZf5idmddhu1TLC+doNPt2dwFFK7jIaSZgGxZKidN6DRTUXEpBGr8"
    "4sFSnSY0+imO+3jObQLWYvxpuZGYjpKUIU5zWtRcTM3jKcdgwwwY+RXH71obgsDjja+/ffL8OtsLdnr8fuuP380PvPaFvOmHvplu"
    "b0ivH/Otr/8vDAYxrut8ScDryUwKwTBOee7NV/Gcm69ilKQI4H+/+5Ostnt4rq0RMUoSbr3pCp77zKtJs5wsL3jbOz5Guzvgtmdd"
    "zXOecRWjOJk4/tPnlucFf/i2D3Lz9Zfw/FuvI0ntKt87P/gZjp1YJQg8hnHKDVddzAtvu54kyahWQj7x2Qe5466HqVZC0qxg25YW"
    "P/q9L8UAldDnjrse5hOffYhKFGyKKP/gd76YhbkGeW5XAv/6XZ9krd0rlb3sdj/0XS9htlXHGEOa5vz5330Ug+FNr78d/yzXK81y"
    "Dh9b4c67v8jqeo9aNaQoNOE5rrExhv4g5r6HD3P3A48jpSydlM0rDBtjfyVJmpOkOW97x0dJs2LCE38qNj3vfM8l8D0+8ZkH+dTn"
    "HrHj9BTmkOs4rLZ7vPH1t/PGH7ydbt/OyVf98K9z6NgpfuZHv5Wf+jevoNsf0h/EvOL7/jOh73HbM69mebUDwHOfcRXNepVef/QV"
    "m8P/p5oQgv4gZtuWGV7yvEvZtX0e13Fo9wbc99Bh7nv4EK4ry3sQRsmXd658Jexcc+Yr/Rz7P6U/X8vmblmcpzXboNmZQSnN4sIc"
    "xmiiagVHQLc7YL3To16t2kkpwA/CssKoRhWaQggcV6KUQRUF0rVc10IpqvU6bpIQRSGe57K4ZRdbt8yz/+ARKpWIex94kPrCNrY1"
    "Kxw5cpxLLtqDyF1ue9YzaFQjVla7rLc77N27l6XlU0RhQGEEj53ogkmRfsS2qss9995La3aBo6urdBLFaNDhPiRXX7RIZfkks4tX"
    "sC8/wLs++nl2bZ3hFbddz3AUI6UgTWNmZmpIIdj/eA7CIYgiHCnZVnU50BsxP1snikJGSUaWZKRpgevKsgKrQ1ZoCmFQOqOIQi7e"
    "0aIW+nSHCd1BjC8lW2br3HL1Rdz50EGSTDNbD6hHAY9lOXmckxsbOe8NEzzXpd0dkaUFJTRH67xMkNWMtcO1GYN2++LzPJc0tZFX"
    "13NxXQcQVCohQlodddf1MMaQ5QrXC7hk5yLtYUIcx/QHKau9mG1bWhxdatOohcw2qlSjEIGhGgXsP7rK4lyNvTu38OD+YwS+jcQN"
    "RzlCZghsVD7JFDdfvpPv/86XEgYhj+4/QJHneJ4H2KSoPM+JoghTcuMBQje01Bet8TyPmVaTwerDNGsOiRsgxwWyzMbSZaEUu3Ys"
    "sP2iffz3n/tdtsz4FNXbMOKj5GmXZj0gCmpoo0kzheNgr1+RElVDu/qhCo4vrbFrz9VQ9Dly8DEMLjt37kQ6DqMyWt3r9QAmCaJF"
    "oZCeRysMMVgKUxCEtgpukaHx8Sp1Zmkjho+TaY9EVhCVWaQTIDwX1xlhMPQHCauxbTN0oV61uRU68lnvDi2fXVnnUUpJdxAzTDyq"
    "lZ0wv8Al2y4lG6wzaJ9i5dQy3W6POMuRwm5vAdqGdClQziFLUxij84nkpJgGd5sfHmNKupmK2j95nLwk1jzhRjamP739V8rGEePA"
    "9/jJH/gmmo0KRa7KYm4b524jbDZpeTRK+d0/eS+e69JqVCcqUqJszykpJAbzpAl/UoqpJOEnpmtIKYmTlOc+8yp++qe+k+HaOtVm"
    "jbnZOr/wq3+BX/eQQhDHGbc+/Up+5k3fQdEfMhjGvON9n+boUsJtz7yaN73hO0g6HVzHmSzfj89tMEj447/6ELOtOj/zY99Glmb4"
    "lYCl5XUePXCcSiUgy3Juf8kz+YkfeyXDtQ7VuSa7/vqf+ORnH0IKS/O78dp9/L9vei1pkhFEAQd/9n+Q5YpqxTpxUgoGw4RqJeTn"
    "3/hakt6QsF5hYa7Jz//qnxFFPu3OkFe8+Bn81//ndWS5ImxW+eO3vIdOb8DWLbO88Ydup1mvUhRqQo0B63DmheLoiVV+5Xf/lg98"
    "5G4C38X3Pd70+ttpNs7cRylNkuZ86OP38Iu/+Vd0ewPcKcrI5rH/Dor+gE53yNvfcwdxkuN5zibKT6HUJPFzXKRMGz25h2wU1j5P"
    "3/RDt1OrRLj1CuY3/pKP3fkgruuS5flTmivjaGWzUZmsko2TzTd9Dniey3qnz6c+/wjffvtzwcDfvvsTdPvDM1ZvJucwNZ+fjN4z"
    "vd+4b+ekLp3WjiPH1Ci7zxNRh2zezkb/nozudL79On2fNM35nlc+jx//vpezdWEG13XKHAFFnGR86OP38J9++29Yb/epRAFZVvB1"
    "z7qaN77hNRT9IZ3ukL9//6etPHB5TTau68bqqD1ffU6azb94vKaONX4fnDFnnmDMnnAOKFPWmpFnvQ/Odm2+lP5cMHA14Dgei4sL"
    "uK7lyHqO/X+UZhgErXrDgnEDea4IAmcy2QtdkOUZYWgjkK7roLV9eAaBj+M4VIIAz3ctJ7pYZ7ZVZ/fO7aysrlOrXsXC/Dye67Jz"
    "xzb8MOTkUk7g+bRmZqk3mvQGQxCwc8dWDu1/lEOrA3Zu34oTr9HPFHOL25hv1jh45BgzszNII9ixMEunvcZnHuxRi1ocP36Ea/dd"
    "xOMnP0+rGtgXqzF4bogQ0O0OGY1sxLTVauK7gtX1nIqT0vAMQrpAiudK5rfP4klpCzcZTaczIk9yEmVLyGepYrXdpxr6zM9UkTNV"
    "lrpDjq0NkNJw6c4FmlHIB+8+QC1ymGtWWV5fQQqohj6OdHGkwg98tLGVSDFWG16bDdnCjUi7jaAWSoGw454mOUWhcT1bYdZxJPVq"
    "iFOLCH2H1fUeSlmw9uixdRYXGmgkURQyjDOYa9KaqVMNPVrVkOMrHS7bs0ArCphv1bjjnsfRxuD5XnmPGoQj8T2XVi2kO4i5evcW"
    "XnP7czh2/CRRFLFzxw7W19cZjUaTG9l1XQCiKGI4HOJ51qmoVqsWKDsO87MR2xsLDIcFcbJOmuREgSTJQQg7DsoYduyc561/+Gec"
    "OnIfN936cirNXdxz9x3Mz84RhD5KKUCUnFmDMZI47rN1sYaQDnme43s5R44v05yZ5ZLrbqF78giHDj5GpdZi+/btpGlKmqYbEWsM"
    "rrNBWTJs8LbzPKcoCjDQUwG9rMXifBMv6yKHK5huG+FVGAxraK+BY6x6kSNSCiDJbe0ATxlqkdXXj0LXJj2bMtG0KHCEAFUwSjXG"
    "qZO7IY1dW5ndmRL31ui3l2ivt+l2+yRpXnL35cTxGxNkBOOl3hK8jxk0E9pMWcl1QpmxUfSNyGX5qbAUHDPmuk/baTh8XMxrg3j8"
    "r/mYttweIaeoJuULq9moTG1l6UFaG4pCTX6kFGRZznCUUCiN60qqUYjryrO8sOz+w1FKluXWeZKS0PcIw83L7tM2XoJP2h3W2336"
    "g5jXvuI23v/Pd3PHXQ/TalY3qDJrHbqDEcNRYh22qX1X1rt4nruxfF8eShtDFPh89p7HePTxY9SrEU2l2LPLKjAppalXIy7ft4PO"
    "yVUGo4Qkzdh30VYa9QqqsGBi7+6tjIYJne6QJF3jjrseoRL6k3EY00J+963v5WlXXcSLb7uB1SPLvPabb+OfPnEvH/rEPczN1Pmx"
    "730Z3d4IpRT3P3yQ//w7b58Ay9X1HllekGcF1Upoc2W0oVCKOEnZtX2e3/3l1/O9b/jvfPTTD9CoV1ht98iKzftorUnSjKJQvOqb"
    "no3nOvzIL/zPc459vN6h0x/S7Y3K62Y/H1OLhBDMNGukWV5SVQyeK6lUQlzHBrjG+2S5YnWtR5xktPKC1fUe/dUuUejjeS7aGJzz"
    "mCtj02Z6Tuqzf57b55QUgjf90lv54Ee/gJDwrg9+ZnKvj1dg0jQnTlKUtjS/Shjgee456T0CG9BIs5wkySY0KLekLnnnoC5pbahV"
    "Q8LAozsYUeQKISAMfaKpeTN9LQDiNCNNc5TWSCHxfZco9O17cer+eSr9Ov0+7Q8SXvOK5/Bf/8P3MYpT0iyfUBGzrEApzau+6Tk0"
    "6hVe/7P/A6U1g3afU2s9knaPdm9Apzvi1FqXwSBhbrZu2y77OBjGZGUVct9zqVVC4jhjMEomEsDNRhUMX/J4ne1YlSiY5Cidbc7Y"
    "8z+/ORCFAdVKyHCUbKIHzTRrKKXo9JIJFU0bg/Ml9ueCWXMFtiKnUgVCOHZwg8BeKKXLcuzg+x5FoVCFwnVdikJOorzKGLKisHKB"
    "RiCQOFIgHfACD2GgFgVIKcnyDMdxmJlpEoQhUhjCICQvcuaDFieX2zQadSrVqFQ90Ugc0iRlNBri+AG75xx2bm3iBzt4fP9+5mda"
    "dDodtm9dpDeMeeFttzBTb/Cpz95JFAYsdXN2LS5wYnmNay/ZSzUKwXWJwpCisBx9MDbZVgiSUYzyHOLhiEajzh4G3HtyhWEiwWjS"
    "uKBSDXCkg5QQBAHCsdF3++Ky1WWHSU7v+DrrvRGtWki9FrFtpkYUeMw0KzQqPifbPVq1io14FtAbZczWQ2bqVYZJhpCQjLCJqdIB"
    "NQY3ZXVKseGpeq5Lmtik1FrdYziMJ1HrNCvQ3RGzc1UGo4wd2+Y5fmKNrNDs2D7L8eUOoeditKZeq3BkaY1GLeRkO8OXkmsv2sqJ"
    "9R79/pDOqKA/SFHGTBLQhLHetee5DNKMRuDx6m96FqOkIPA9VFGwsrJCtVpFSjlRnxm/IKIoQmlNp92m1WphjGF+YZ79Bw6zta5Y"
    "XeuzvJ5RCRwuu2YHp9ZS4qUTk6i377usrw/47F2PcuN1F5FkDr/x//0IRvWp1qukaY7nSoSBvAClLcUmT2MEimq1xsrySaraUJub"
    "IU5iHjvQoxpVueyaZ7B+6hiPPPwQW7dto9WaYTgaUeQZsqxqe66IjXVEwBEgdIZSipEOKZztBIHB1wPqeh0Vr5EMHOKFrSRpgJIu"
    "nlC4rgCtyZWhHxdIR+IIwUyrjphr0MkknuejhLaRlyJDGujHGiECiHaxfcsetsZ9Bp0VuuvLdDptur0BRZ4jhEQ4DpvlGcfReDPh"
    "sG8UWdoo1CQ20WHKeTkVSp9Q7Kf+sBGUkjMvBGeB9mMXgg0uzVfOxueVZjlvfst7iUKfwSjhlpuu4Lk3XzWhmrz5Le8lSTObZ6I0"
    "aZl3Yk/NRv0Gw4Q9O7fwvFuvpVGLOH5yjX++4366/eGml6mUNirueS7PufkqrrpkJ5UooNMfcs+DB7nvoUM4rsR33XMmvbmug+s5"
    "5bPZ5d/98DfzhQcO2MRNMbWN42xExsp9ndLBznLF77zlPWRZgRAbL2mlNcNhymMHT/DcZ16NVoZLL9pGNbI0mK3zTS7bu9067q7l"
    "ou7cNsfOrfM8euAElSjgkou2Wge8EvDQY0dZWevZpe6xu2s2+vKb//Nd3HzDZUSBjwB+/ideyUc//QDf9rJbuf6avax3+jSqFd78"
    "1vfS7g6oVsJJxE8KSb0W8cnPPsynP/8IYehz2d4dfP2zr2Mwiplp1njdq17AJz/78Jn73PUwn/rcI7QaVV743KexZ8cWlle7fP1z"
    "ruOZN1zGHXc9RLUSbgJBp4+rUzpJz7/1Wp79jCsmtIg/+st/5JKLtvLsZ1xFrRJy9MQqH/nU/fQGMdXIzrGve9bVvOA5TyMIPFzH"
    "IS8Utz3rahr/4XXcff8BPnbnA9RrEcNh8qRzxSu5+ZP5KM5c1Zr+XGKrbj/rpovZutAiSTN+4DUv5q/f9fFybksGgxH7Lt7Gc55x"
    "Fa1mjfV2j49/5iGWltd50+tvxxvTez77EJ8qaVJKawaDERfvXuTm6y9j25YZlNYcPnaKO+/+IiurXWq1CKU0vr9BE4pCnw99/F7u"
    "vv9xXvHim9m7a5E0y/nsPY9xz4MHiaYcFCkEWQnsrrtyDzdcs5dmvcooTnjw0aPcdc9jaGMIAw+tN55f59Ov0wGvUnYOf9e3Pc8+"
    "C7KcvFC88wOfYb074MW3Xc+le7fR7Q95ydfdwPNvuZZ/+sR9/OxPvZrn3XoNWV7gOg61SsC/+5FvoT+Ieds7PkaWF6SZrYnywuc+"
    "jSsu2Ykxhi8+fpwPffwebn36lXz9s68lTqxj8md/9xEEYjLuT3W8kizHmzqW1oYv7j/Ouz/0GfK8KKuGnzlnzncO3HHXw3zkE/fw"
    "gq+7gVufbu+DLMv5g7f9I61Ghdd8823sP7jEHXc9TL0aMUrSL6k/F8yaO5Z/qoQh1UqA6zpkeUGWFdSqIZ7rkJWSh8J1Su6hjTq5"
    "wi2jdJoNZqyNWDmORBqJ70s830PlmkLZ6GO3P2JutkHge3ZJyBF4wifLNdVqOInUp1lOrz9kFNtoSBR6XHvtdSydXMHxAy6/fB9h"
    "FNjs+EaLKAxoNGdBCNZ7A6688lrW1lfIi3W6vR433nAdwhSAtAm0YcDSiWU6nR47d2zF912279hKFIQ8cP/9FsoIQa1aZVc948FB"
    "ijb25dNZH6K0jeAKxpVN7VjAxkMy9H0Gg4xcGbR0aFRzjqz0uHv/SQZJxmyrRreXkCQFzWZEXmg09uUQeB650hS5IY61jTThYJQB"
    "LUq9dGUBlDEgjKUsaU0Y2jHUxpDlBY4jbFJNFlGpBKy2B8zO1Dh4eIWFhQbbFmdZXl4DoNuP2bVtllOrXfJC8djxVbpxwsVbZ1jt"
    "DDl0fI1ca+oVH+k4DIYxwrGgWEqJ0YaXPedyXM+lyFV5E9rvksRya8MwJE3TjdWCoqDZbKKLguXlZbZv315SqxYZrdzN5+49xjA1"
    "fMPXX81Nt3wdn/z4p1k6bp3IrChoNiJOnuqxe+ccjzy+zqMH/5zFuSZBUCPNCwLXRWlLsRESAmkTfU1hyJM+9XqDQ4cOoQHh9Yka"
    "HvValfb6OuudPlvmFrjs6q089tC9rK+ts7C4lXqtwWg0tG2eRgIfr0g5UiJdiRAOWtsqvQ4GTIEqJD1dYaY5y3CQUI8KZLpOOBjR"
    "SyVeY5bCraBwqZYSn1mhSZIcN1IkyibxBL6N1KeJ1aIXUmPyAsr5mSgP12/R80Mq2xZpbY/JB2v0u2t02usMhjF5rhBloSe7umPv"
    "Z1OS3MW0EokYJ6dORefH9JcpCs4ZVirUlMsSmwPsYvLPaU7EV97GkfLf+IN34kiH/lqXf/eGV/Hi266fvKx/4w/eSbc3nIC2LN8M"
    "3LOs4DW3P5cf/d6X2VUVz0UpzQOPHOYNv/jHPHbwhE1gEzAcpVx7xR5+8adezQ3X7MX3PZxyxWx62X2t3SPwvCfkOksp6Q9innnD"
    "5Xz3K5/PH/z5BzbUXJ7wnCVJEvPf/+gfLKfZcybRs1ajRpyk3PvgIV7wnKcxHCVcctFWatWQU2tdrrpsN61mlSwrbDVfbaPw11yx"
    "m3sePMiWhSaXXrydJM2pVgLuefAgg2FMq1mdKMKA5XhXopAHHj3M7/3J+/iPb3wN650hV16yk1//99/LjdfuYxSntOo13vPhu3jv"
    "hz9Ho1aZROhgI/H1Y3c+wK//97+hNd/CCPj9X/lhbn/xzQxHKZfv20GjVrFF1koQF4UBH/v0A/z6b/8NlWaND3z0bt725jciBYSB"
    "z7WX7+Yjd9xHvSrRnFsNZJpC86Y3vBY1GLK82sGRkh947QuZm2ngeQ6qUNz38GHe8B//F4ePLRMnGc+5+Sp+8se/jaUjJwFI0oxn"
    "P+NKvukVt/Frv/k2/vHjX8BLHK6+fPeTzpVub7iRjH4eJqVkFFvn4U1v+E4YDVhr9/m7991BkmakWc7rv+sb+InvezmzM7VJ/sPy"
    "aof/+Wcf5Me/7xuZm6nj1CqoX/8LPvyJe6lWLSB/ww++gu971QuYadbwPEujzIuCY0tr/OYfvJN3ffCz5XPLUpfqtQinEjLbqvN9"
    "r34B3/jCZ9hVUWAwSvgff/o+fvct7yUIPASQ5QWtZpX/5ydfxTc870abhOzY53mW5Xzq81/kF3/jLzl0zFJrlVJobc6jX5+hEm7k"
    "FghhV5ga9YhtizNlHlWd3/5f/8DP/PJbqdUqvOuDn+G3/uP3M05YbzWqSCn4uR9/JZ5r3432fefzxh+8nV5/xN++91N0ekMuuWgb"
    "v/Jz380zb7gM37fPC601b3/Pp9Ba829+4JtQgxGd7pC/eufHEVLwph/6ZmrV8CmNV5xmXLRrC7/6c9+z6ViFUvz1O59mV5umEsTH"
    "556m5z8HfuO3/op3v/sTfN2zruEN//bV6OGQpVNtDh1f4af+zSu48RlX8Ov/7X/z4U/eS+B77Nm58JT6c8E2myuFoF6LiEK7TJHl"
    "tgLm7EwdLQRpnOIIgV+JULqMUGlD7kiUVghkyYPdiJONEzgpl+dUWeHTdQSu72KEYDhKaDaq9iVTRi2EgMD30TojzTO0gXqtSq1a"
    "QRmDLhR5njM722J2pklv0Gd+fh6DwRE2+7jQGlNGnbI0p9mcYdvWbaystsnznFajYWXMMPS6A1zHw/Nc6xhEFYpBzHAY02g2kdLF"
    "931W2gNkWGP7jOHIejEumooUDkxFkOyvcgLetbDL50FolzSjMlN6ab3PMLbqLlpb2TTfL+X8HI1SsNIdopUF4M2Wg++7tNf6E143"
    "pR63EM7kuOPRV8pGzBzHUikwBq1safv+MMWUwKs7SKnVK6yu9mm1qlSrEVpbjvZaZ8hMq86ptTaNakR/lPHFo2s844o91GoRDzx2"
    "nDwvGPRjAt9GvR3XodPr86Ov+nqe+bRLOHrsJFrnk6j6dEKY53k4jsNgMGA4HFKtVlFFwdz8PI7rsn//fi655BIWF5qc6Njo0Ja5"
    "KlL6vP99d9BdO0gYVTBK4XuSLFWsd/oMBgM6g5SLdm4lLwqb9MoGkB5HWAtVgHBQBpK4R6PRsNVp4xFe3MX4EU4Z1aTQHD9xkk6t"
    "RmtulmGvT3t9lVWl2LptJ0EoLa2HDU4p5bKxdBwcz2NxS4tCK6KKT5YphOcjtMFHgc4pNIxkg5nWHIUaErlDGK0SkNPPXFKzjTRz"
    "8F0fY+z5KCMpipy0kFRCD8d3kYWm6kfEqQdKkRWKJC9oehIXRZxLUrcKYYW52T00tnRRaZv++hqdTlmQy57JFKl94wk65saPK7bC"
    "GIeLDbbL1LZivGRtNmD5Jt78WUD6v8YDWwjB/Ewd17F5PNXKhrLH+DvftTkjjhQsrbQn3xVKMdOs8h9+8tU0GxWSNKPTG6KU5vpr"
    "LuZXfu67+c6f+G+AfRleevF2/tdv/jg7ts4zGMb4bPh8xhhe/YrnsLjQ4vvf9OZJ9OlcKzpCCALfYxgn/PB3fwMf+9QDfO6+xzbx"
    "85/IzNRFtEA6sJFwKbnvkcPESYYxhoW5JtsXZzlyYpVrrthDJQqJkx6jOMXzLH/8qst2obRiy1yTrVtmGCeT3vfQwbMm+wJopWnU"
    "Kvzp2/+ZFzznaTz7GVfQ64945TfeSpFbHvp6p89v/dG7J8voZ5yDMYSBT7VVY3amxpHjKxw6esoGmeK0rAy8aWpO7VOnXg15/PBJ"
    "4jSnEgVWKSR8Yofp9GtgKUhdVts9hBD89A9bgJWm+WQu3HjdPn71576L173xd56Ah2yf4VJI0jTj+qsvPq+58vqf/T3ancE5x/mJ"
    "+h2vr0+oP0IIBqOU73vV1/Of/t130B8mdPsjqlFIEHjs3rGFn//xbyNJc5ZOtZnLckZJinStA/MzP/KtvPH1r6DdtQENX7iAoSg0"
    "O7bO8bu//EMIBG9/zx00x9SlvKBY6fCyr7+J+dm6zZcqqWq+5/KzP/qtHDh0knf942epV0N83+N3fukHedFzr2dlvUdRKFzXoSgU"
    "SZrzgudcx8Jcg+/+id+iN4jJ8pyf+7FXPmm/AP7+/XdSr4UoZSbv2jxXDEepdWjTlKsv38U1V+zh+Ml17n/kMN/++l+fJFMnaU69"
    "ZmW1PdfZNN6WESgoCkWrUeV3f/n13HjtPlbbPdLMoVa1yk2vuf25tLsDThxawnMc1rt9ShZiuW1+fuP1oc9SjQJ7rP/0Q9x03fSx"
    "QipewHe/8nm0u0P6g9FkZc6R8inPgeEoBUdO7oO1dp9CKX7lZ7+bei2kGCakeY7Whmaj8pT6c8HONNkogbFTAu0g8KhVKxRKk8Yp"
    "plz+Vkrb8vUlj9d1XTzXw3Gk/V9KPM+1ILRcjhRC4jguG/xZAUbieR6eF5AkBUWhMdpm/GPsA6sSBlQjO4mDwKNSCalFlmrSbDWY"
    "n28hjEFiZQeN0mS5QjouoR8QhgFB4NFqNphp1gkDnz27thP5fgnmFIXWCAS93hDP84kqEWEYkmQp9z30MHNzWyg0aCQzjYiaq1ic"
    "reLKUgcdWVIFxj8lG1gIS58QEiE8rPa7IElyVjoj7n/8JCudmG4/oR9npFlBrjXVeshwmFHkNkJejSKEdEjSgjjOcT2XqBqitQXg"
    "RljO3hgwTfSyjU1e1BryMgFrnAwjpVWcWV0b2OXGXBFGHp7vMBzZJM0xkErSnE5vwEXbtjAcZTSikCxTPHZsmTjO2LdrnvmZJi+5"
    "5Qoa9QqUD7g9CzNctnOGdmfArl272LlzJ5VKZQI+xj+qTFpptVo0m01WV1fpdDrkec78/Dx79+7lvvvvZ9BbhSJh985ZnvvMK1g6"
    "scxcU7Fz904cCY7v0hso0qwgSVPipKBVD+0KkRG4jnWW1JSOtSkdSaUMymiKbES9XsMRkqLQjIZDCzqKnEwZNAY/cEnSlCCqcez4"
    "UcKozrbtOzh65ACnlk9SqVUJgmBynDGG9RyHLIf2MEOrgsDzmG1VqFdDonqE8VwcGeA6EiFBqxylDANdZejuQNd2I90QmZwi7O2n"
    "6BwmH/YYjDRa+jimwPdDsqIgy3OGsf1fGkWzHhKGIdVahUII/DBAOoJ6xdLe4lzS13VUdTe1Hdew9+ob2btvH9VqtSwKthEIHzum"
    "45WkMRgan+vZ8YLY+J5N/5xJgTGTf0778quH4osy6lMU6gxgNflOqZJat2FaG8LQp9Mb8tv/6x/4o7f9I0mSEQYe6+0+N1yzl2fd"
    "dDmjJMUYw7/9gW9k1/YFur0heaH42/d8il/7vXfw4U/ei5CC5ZUOtz3zar7jW25jMEzOqkJhMLiOy1q7xxcePIAjJQuzDX7q9a+Y"
    "SCc+kQekje3zT/7AN/EzP/otvPH1r+AXf+rV3HLj5QyGCVEY8NCjR+h0B4CgEgXs3bMVz3W47so9KGVpk+/8wGdKLmrBtZfvwfc9"
    "Lt69aPmqQKc35L5HDk9oC2c7D0dKsqzgv/yPv6PdHeK6LkmSkReKaiXkj//qQzzwxSNnlZMEC2B936VaDfE9lxc/70a+8UVPp9Mb"
    "UokCHjt4gn5/hDtVXMhM3nUhc7MNfvi7voFWo4IqrDzv0qn2piTNJ7MxhUZK+/5a7/R581vewx/95Wlz4dp93Hz9pQgBn/r8I/zO"
    "773DJixiI/13fO4R/vOv/Tl3fuGLhJ7Hj7/u5ec3V775NpLR2efK+fTbLRXR8lyxdaHJj77uZQzjlEIpwsDnw3fcx6//3jt4/z9/"
    "HseRBIGL42zsm4xSnv60S/j+17yQ1XYfKQWP7D/Ob/3Ru/mDP/8gyytt8rwgy3J++oe/uVQSUrhO6Qw7kkoU8E+fuI9fefPf8tkv"
    "PEqtEpLl9nn4ypffShT69AYjXnP7c/j6Z1/H0ql1otDjnocO8l9//+/59N1fpNWsEicZNz/jSv7t938j650+z3japXz/a8+jXz/0"
    "LSzMNW1gBVHiHEmnN+TdH/wMM80qSZJzy01X8Ld/+HP80k9/By++7XoMcGqtQ5Jmk3fbr/3eO/jkXQ9N5EWTNOO3//jdvPmt76HT"
    "HfLab7mNm67bx/Jql0oUsrre4/f/7H38jz99H0eOr1CvRjhT12Zs4+t0PuNVCX36w4TX3P7csxzr/fzun7yXI8dXqVejDX6/sCsa"
    "T3UOSGk948l94AiqlYCZZpXBMGEwSCzFME6fWn8u2FnNDXzHggwhLF9Y28QAgZhK2DBoMy64sRGFksJG3XWZXGaTbhyEsMDWmBIs"
    "iSk6CdjojikL82Asl73QgERIy+EV0oLhNM/ti6hMxgscm1hnjJ6ACKU0RVGUyXQWZYxfEtVahTyzS6tSWplGM9ZCV5pqNcIAWck3"
    "271zK8Iojp5Y4rJLLubAwcMEYcRso06n1yd0XZLiNDghmGhWmwm4sV/Y8dRUKgG+57Ft7v/H3n/H23ad9b3wd4wx2+pr19OrmtUs"
    "ybj3hu2AMdWEAAkJhNxAQhoJJOTelHtDGhDqBRyICYRqDDa2MWAb9yIXdR1JR9LR6efsXlafZYzx/jHmnGvtffaRjmQb8l72o8/R"
    "3nutWUad8ym/5/fUOX1xlWTkYB6dbocsyXJ4kUIIleNlEwaDxMFflCLLEqI8Wz1LdF4chzJRFWPdmEiJVILUpOV7u8hSFzmm2FeK"
    "OHOsQJUgwNQsoJ2i6/sEFcFmZ8Rmd0S1MmB2qs6lpQ5TrSqr3ZhmPeLQXJM0dcw1+2bbpKlhlAz4mtuPYRBsrK2zsbFBFEUEQUAY"
    "hvT7/TwT3pQeeGstURRx7NgxFhYWOHPmDHNz8xw4sB+E4tKpz/E1txzGj5oYm3HL8w5z7txlbGU/Mmgy0k1WuqfY09a0mm085WAP"
    "ReSh8ECJCePFDzyMsXgeeF5IPOzS3hsRhQHD4QCjE7LUIAJBFIT0+z0kwlHjyQbtVpuTjz/OviM3c93NL6C3dpnTp55ganqOqekZ"
    "RsMhWVmwRiAlkGkSregNE4ajEYGw1KsVAr9GveITIxGexCIIAkNmYozRZFoysE2U55NVYypqSH24RrbcQY6GjIzAixRJBo3Aw4gE"
    "YzSj1BCmLpzebNRo1aqoIGVNgPQVfpAhFAS+JdOCLIUsmkZFKbXqOoPBECHFWAlknJRZLHolJAbHlFFWyS3hMvn6n/Sol9AYW7if"
    "2K6k76Si/kUxzDw3GYfV/++f+V1+6z2fAAsPPHKGn/q3fyfPv/C56fh+PvCRL3LrDYd5xQtvptMdUKuG/PSvvp+ff+cHSpagn/y/"
    "/g5vfeOL6A9iXv/y5/Pr7/roFnjJ5G2ldJGon/zl9/IrP/EPCAOft77xRbzl9V9Dp9u/KmTGJdYaKlHAj/7gt5RRA7/RRv7Mb/Jn"
    "n7iP+lyb5dUOJ5+6xEtfcBNRGHD04DyNeoWbbzjkDL845d1//Bne8roXkGnD9cf2025UOXponmolYDhKOXnqIksrG47d6ipKsDaG"
    "er3C3fee5D1/cjff/51vYnWjQ71a4YETp3nn732ERi3asp8LUUrS6Q35W9/2er7jba9CKUmtGjnlIX83/Pq7PkqauVobk+d8z9tf"
    "z3d846vwlKJZrzAcuWJwC0vrfPrzj7rE1WtU3LesBQn/z8/8Hr95xVpwxsJ1R/bhex6futtRaH7DG18EIVSigE9//hH+60//HlN7"
    "prn++AFe9jU3XdtaecXz+clfek+Z4/BcREoHp3z9K25n/55p+oMRjVqFX/qNP+U//Oy7XFKhkvz7H/4bfN93vJE4GeTngU4zvvZV"
    "d1KrhPQGIy5cWuEf/5tf4cz5JYw1fPxzD/GO//KDxIll/94ZXnzXjXzycydQyiXeViohX7z/Cf7uv/h5Vte7zEw1+fWf+ce86M4b"
    "GMUJx4/uzalEDV/7qjsZxgnVasQjT1zg+374F7h4eYU981P8X//429k7P+Xec75HFAa8/uW3u3b1n75dB/ZO8+K7buT9H/oCzWYV"
    "q4vEy4Bf/I0/pVIJ+Vvf9jqi0OfQ/ln+7nd+Ld/5za/mqbML/PZ7Psnv/NGnEMK973/iZ34PXyne8Io78oTYlP/6S++h2xsy3W7w"
    "+pffzmCUUIl8Li2s8r0//PM88MhpAN7zwbv5Hz/1Q0xP1ccRsQm51vGqRCHaWF778tsZxtd2r+e6BnZqY+D7fORTD/CT73gvq2sd"
    "RnHK3n0zvPJFN19ze3ZlZ/GCwLF4GO0UaGuc8iesoyVSubUnc4+Yta56qDVg8teyU1jzJBAEQshcgXXYZivG3xcKlFLuZ5oZAt9H"
    "KZfMGsdZGXYy2iUTmTybWeVV7wpvfkGF6BRkW+oBRWVXKZ3n31cemdGMhglZlqGUQkmJCjxqngADvucDLgk0jKrs3bOHTGtuvPE4"
    "Z0+fZb3bY62v6Yw0vufhDMxxfxATGF8EQpGPoUVrh/sfxSnnF2KsVXiBpNeNXVuFQKegJFSrPsNhSr83whqo1HwqlQAhBeur3bxA"
    "k8IagRXOW6U8x4iSJc7IcjCegv5PT8yFQnjuxd3tjdCZYVgxVGsROtNsbA7xfEm7VaNWi7h0aYPuMOX49XMsrQ/wA0XkKy4sbBAF"
    "in1zTU6eXWJ1s0+jHvG8Q7McnGnmBaVcm7V23jgpZckgk6YpaZq6cKLvxt3zPA4dOsTU1BSnTz/Fyuoy1113I9F1B7i8uMilhYvc"
    "euft+FZz6lyH6vQUnj9Ns1Vn7/5DTAdr+CJjmDj1T0qBL3FQgzxk6QxSx8eeZnmuQxiwuD5i9ohhbn6O5aUVknjIVMNDBhGJMaSZ"
    "JQoVCJ/OQNNqtlhcXmdlZYneSHPs2EGO3zDD8sI5njr1JHvm91KtVfE8j+FwSFgXyKCGJwcIZSGDVMF6b4AFKkGNKAyoVhSzNY/E"
    "WEaATTWeZ/GVRhhNbARBNEM/rdBs+PjdBfTqJby+IMssQ5pYPDwVImWK9CVSWta7CYm0pAhC38dT0GhWSJMUo7y8sq3J8fi+S6iF"
    "smpqIUKOFXC79ZecJag4sCif5BKoC3aa4mRrC2PKnT/JPmNxRnB53/8ddfUJsRZ8T7G+0edTn3+E2akmAJ/8/AnWN/rUa45JpFaJ"
    "SJKMwwfnqFddtdxRnPI93/Y6vvfb34DyHH5UKYXWGqUURw7OUc0VoYK5aFKMsdSrEfc9/BTv/N2P8C9+4JtJM80/+3vfyD0PniJJ"
    "s6fNFTDGcPrcIo4dzDDbHrC20XPPWinoDUY8cOI0r3npbWhjOLR/ljtuOVbieE+dXeDx05c5dfYyh/bPUKuG3HnrcQ7tn8NoSxj4"
    "3H/iNN3+MGeX2NmLVtDtHdo/y8tecBOjOEEKl/cyP9viyIE5Hn3igmON2UGR1towO9Uo8wdsntezvt7jJ9/xXj5x9wnqNZc4OZ43"
    "p5A1ahXnJTWGdrPGaJTw4z/3+1xcWKX+LD1/k2vhk1dbC1JSq4ZobWi3atSrlfFStw6q1J6fIvA9Du2foV6Nrm2tHJijWg1dvs1z"
    "3DAyh3EcPjhPFPiMRg7y9b/+4GMEgUejVqHbG/Ib7/4Yb3/rK/KcK5fA6YUBRw7OY6xBG8PsTIt3/fKPEAZeOR8FvWajFnH04Dx/"
    "rh8ERJ5I6rj+1zZ6HN4/x/nLK3zmi4/x6pfcymjUp1ZxnutqNeTIwXniJKVVr/Lxzz3MwvI6B/bOMIwT/vV/+c2S71tKV7fkyKE9"
    "eZHCp29XvRZx9OCcqxyMwFAkUTs95j//wh/wx3/+Jd706jt5+Ytu5qbrDlCNQm44tp//+n9+D7fedJgf+y//i0BAY6ZFdRvcbm66"
    "6Z4F1ZBD++ZIkrSEiT1w4jR75qYAyz0PneLPPnEv3/+db6LTG14xT89qvKKAw/tmr/lez20NbN2TLhrooFP/6RfezcMnz9NquPyH"
    "RqP6ZfV9V5x4JQdxHv4uHlOifPk6KR5g2liMdpRfRUl1KcBKNfEAynXogouU8fu3+FvlfJ/GGNI0zbGjknotdFRqKkB5rrCOw51u"
    "fXGVkR0pCAKVsz24ap2ZcCE43/cxWqOkxDMSgSRO4hKjnneUIPC5eHmRWrXCgf17WNvoIKXkkUceRVXqjBLDwmqfWnuGu66rc255"
    "k82BwZcTCXoT1ytYJoQAkWlMZhn2E6rVEAQEUhKPYozWuZFjKFg6Mi3odhwuM6x6qNygMNqSJgZrCyiOJU0dNZgwuV9TenlTioe3"
    "cMp6DnVQvqJS8ci0dnz7StDrD+l1DXMzTVpTEVnivAzNashoukYcZ5w4tciBvW02un32TjXYO9VgrTvg3GKHPfNtmo0KT5xfYboS"
    "cGhfm1GuMFhtc+hQvgZy4y0MQ8IwJI7j0gtfJKdWq1W+5mteyPlz53n44fu4eX6d5904x579c3h2yGe/+BT19jRBFOLbDXTvIvun"
    "Z0jtEeKsi7IrmDRldSND4CICShlq9Ro2S+iPhuzdd4hqrU6/P2Bl+TLHjx0gjYe0ploIpUjihEuXl5nbF/H8W4/x+CnJwvIGQkI/"
    "1sy1ZrD6cUwWIyWcO38ZjOXggSNMz424fOE8m50NZmZmSNKMIO6zdO4khC2srOBFFpHFIBWpdcWnOn2NFRHUPWZaVWIDqmrQmQXf"
    "IH3wM4MfSOhqsqyCtlWG2mduej96dQGZrJIZgbURqakwTCKE55TwSuQx6iYMMsNoZPA9QRB4eJ6jNYt9SZxYZFApK69mWVbuu7H+"
    "XmjhtsRskuNtJ/dBsf7Gj/Rr0cC3H1Pg4YvP//fV4AuldBIOskVRzTdhGHilsV9yIQt3rKcUcZqVWNX1zR4Fxd7VxBjj4CS//WHe"
    "8roX8LzrDnLrTYc5emieXn+4Y7nw4r6d7pBvL+zWFgAAtotJREFU/Xv/hV5/WLYjTlJaDQeVlELw0GNniXM2ncMH5njJnTcShT5S"
    "Kk6cPMfK8gaPPn6B17/i+YSBzwvvuJ5jB+fRxpBmmgceOf2MeHspBYNRzL/8h9/K8285ysp6hygMiOOUffPT/Ksfejt/55/+7I5K"
    "e0GL9ycfu5co9HnVS25xSfiZ5vt/9Be47+HTTLfrJEm25TwhHLNPnKQO190f8sgT5/mNd3+Mz91zMmeTeW7h+mdcCxNtL/i5C3Gw"
    "PqdkBoH/FV0r1yIWi59Dfoqk6+EoIfA90iwjCDwGgxFxkjp2NvKYmJQEecJnsVN9X5WJ+55SrG/2St1hOErG0dC841q791amXcRf"
    "57UTRAkFdcZF4KsStjfMqwNr48YnTTWDYeyuK1wuVZjnlj1Tu7Q2ZbsmlVFjDN3+EIHgE3ef4NNfeIR989PccHwf/+h7v4FXvuhm"
    "ltc6fOc3vZo///SDfOiT92HNlZzlhfEghSiTY4UUdLrDEs1gBUjl4DlX2zfParzks7/Xc1kD2xYRUko6XecIcNWQXWTly+37rjjx"
    "8jy6LV5zit/BKaL5MjbGQVwQYyvUFt4x6zxoJdYam3t5c4jCxHUBjHGKrat8Z8uiQjrTKCFItfO8OwYHncMqnMJfFD7wysUlEcIA"
    "BiEc803RDCmUSzSBPFkkJE5Tx4qRL/ggCNjc7LK+3gEkjXqdixcvMkw07ak2B2d8ju2dotVukY2GNEK498wmo8Q4bHLZ4wk1pfBy"
    "S4sE0sSyHveJQlc1M0tdrFsAVruqp9KTDPpDpHThXD/wEQg8FZBmjhpSGNCppuDQNoVbwDKh5MjcbVlAhw0CF6GYnW2y2R0yHKRY"
    "azBZRqNdw2CphgGx0EipmG83WF4fIKSgUg8ZjBKO75vh3MIGRw5MMdOscXapw4OPXSAMAmqVgL172hhrSJMsn4PxS8ctpa1/h2Ho"
    "ii9Zy9raGr1ejwsXLtBsNdm//yC1yHLjfMANt7+QT33i08w0QwaxRVuPqcoA0gFS+WDWkXQYyhY2OIJQHTYuPMm5S+tYIUkTg/Qb"
    "3HnbQWpqxMXFLt/69q9n7/wcv/4//huL5x9k72FJo95CSTBWY9I+ncGQBx47S+QHHNgzRac7YKM34MB0i0ajwXDQJWpo6q066ITT"
    "5xaoVqocO3Yz5598mOWVNY4dO8q+mTpx/wTra5LljTa6sofm7H58P0AZEJ7EU30yYG1zSG8k6A019UhRrUpmrCXwBakWSE/ihRHa"
    "5Bz6WUJ3lNDVVaJKG5sOqZoRUbIC62tkOkBU2iRhnWo1ZNQdIXDh3FSDFG4+6pGHEJpQ1Ym9IH8Jpltg6QUOfZwk6Fa9FJKicvLk"
    "4YXCvUWZmITLXHFkeRPKK9mtXv///xWLVJKVtS6pdkxLQeDxz/+f/8kH/vyLTOe83zNTzVLZTtOs5N2/GmKj8PIurW7wU+/4I37l"
    "v/6gq8DcrJf5FldtkbWsb/To9AYOFmkdhM33lMPthz4PP3aWze6AdrPG8SN7SracNNM8/NhZpCd5+PFzxHEKQvCal93KgT0zaG3Y"
    "7PR56Gnw7eDeI73+iJe94Ca+65tfw0bHQXwuLa6xd7bNRqfP615+G9/1La/lV3/7Q0y16yUmvOhDNQr52Oce4pOfO8HH/+DHMdYy"
    "1arxTW9+KQ8/du4KeI3Whma9wk/+8nv5uXd+gJmpBnGSlrzstWp41fZ+NcUlQmbESUYUBaysda55rRSJkU+XyPxMYnGJiesbPYeV"
    "zqMQt950mD/52D3MTbdYWevw8hc+j3bTYcmdM06QJWmZHBsEPl+8/wn+zj/7WXzPOYoqYUCzWcNoFz1fXuvQzJM4wX/mtuWPgTjJ"
    "nDKYF9E6fmQv1jh61jhJeMHt1zM71UAbQ5ZpPvX5R1hd6+YOvqdvl5SCjU4/b5djNdHa7YO//zffQhD41Cohn/rCI3zwo/ew/KVN"
    "njq7yCf+4D8S+B5SSZ53wwE+8JEvXrHmivnR2pCkrg/tlqMpvuu24ygl6ec5ML6S3HXbcWdUPscqq+Px0qxt9Gk1r+1ez20N7NzG"
    "Yhk6aKxzIKZ/AX3/qyCeI6dz+Ohi0xfYY4c+sTmbjFNEy5CtLWqwjRVyKaVLnLR2y79CSlhJfrwxjnXAFcQReVEYwWiQIKQkTR2U"
    "IookOrNY4SqzgkVJhVIeQkIOpc85tS0wLuyTkaFw1p41jmdcSud5J29fpjXz8zOcP79At+8KBezbt5c9e/bQ2VxneqpBZhzEY6gF"
    "U1WPFx+ucGpNc3ljlPfHeS6VoIQZGKMn+g6+8olHWVlUQ5SJkpao6mOtII0drMSPAjzpYYzGCwRBGLG5OcBkpiyak9tLzpgihyaU"
    "xtT4ZV8YU9ZYzl9cI0szdJZRrVdzT45HdxAz1ZqiXhU0o4BmLWKqWeWp88vcfuM+Li11iaKAudkWy5sDbj40z13tOk9e8Dm/tIHn"
    "K15+x3FmZ2aJogHD0bBcR8V8b18Lxhh0/mKanZ1FSsnU1BSrKys8+thJVHyWN77sJZx45DTSaC5t7iGLE47sbeIxJLaOd96gMFrj"
    "m0UMAcab5Xm3voiDBxfpdpa49Yb93HPiEguXLvLPvv/V/M/fu5v//gv/hSMHZ1nf7DG7/zZe/uo38slPfxE/8InjhDjuU8vnsdsd"
    "kaUx0+06URRipKLRaLB5eRlhR8RJhTDwiEJDmiWcOr/M4f2HOHPmHI888ggLCwscOHiQ/Xvn8f0eg84qg40n2FRNvPZBwoOHsbKC"
    "Uj6Q4Ck3x51+hlI+vZFmJgqpVgOm6iEYyzAx6Cx0UbLU4AmLspqBkchwGo0GMaQiRmTDRUbZCkZFpDpEypAocpGFqOKz2RnRF5o0"
    "1ajQww8dzMcYi/TY8SVULjQhXL6KkKX2PX4qTDgBigjeBEZ+4opbTvzfHB3znMRhPj1On1vk/MUVbji2Dyx873e8kTMXlrh4eYVv"
    "+Wsv4x9/3zeQphnTUw1+6Tf+hJ96x3tpNWpbYB7bxdExVvnwJ+/nD//kbr7jba9kfbO/o7d9UoQQzEw18sjL+Lnd77uCTZ6nWFzd"
    "5PEc596oVbjtpsNk2rFsPPDoGRqNKg89dpZuf0S1EnDLDYfLQi2Pnbro+NvV1fHt1hoCX/HDf+8biaKALNOcPb/E3/vRX+T//fH/"
    "gxuv209/EPOPvvetfOrzJzhzYSmvBj2WTDsmm4cePcN7/+zzfMfbXkm3N+S7vuU1vO9DX+DE4+cIfO+Kvo9yZd33PLTRRFFQPpf+"
    "osRam1fTdP04dngP+/ZMIaXgqbMLnL+0wg1Hn3mt/MpvfYh//Z9+45qoQK8mRluCwOeBR8/QH8ROKVeSf/NP/jrWWh574gIvfsML"
    "+Vc/9HaKSp3gMlCM1tzz0Cm+/RteyXAYc9dtx/mb3/o63v3Hn2XPXJt//UNv547bjpGmmuEw5tt/4CeI4+SKZ8vTjBSep1ha2eSB"
    "R85w602H2djs8ebX3sX3vP0N/Nkn7uVNr7mTH/+R7yaKAuq1iI9+5kH+9GP3ct+Jp/iub3nNM7ZrMBjxnf/wv9HtD7cwwljgb3zT"
    "a7jh6F4A3viqO+h0B5y5sMTbvvbFVKKANM0wxtLtumrsLppiykqm1WrITdcf5NSZy2xs9nn4sbPc9rzDrG30eM3LbuXf/JO/zm+8"
    "+2MI4G9/+xt4+QtvZjCMr1jr1y7FeHV46ORZbr3p0DXd67mugWsRz1Nsdvo8fPKr3ff/74tnck9ZWZY592xbWxRaKZy3MreAHB5W"
    "yHEI3SWKevnfrpSzyRM7imktlLayHK4gx9MX3n6DTjRB4BNVQuIkAfLkOJEnvuUwEZkrAUUms8m9gC6875RBY13hoSKMZrPMYdaM"
    "88Ir5aEzA0YwGLhCS4cOSwaDBIErT92ealGpVuj3B9TrVTwlSRaWGIxG1Gs13nhkmvXegNVOn4urXTrDjPW+QAnjqt3Z3AufQwm0"
    "1i4sZNyGlsYZSkJ6WCAZpYCEPME0Mxo/9+hbY6lWK66/1mIyZxgIW4xFfi9j2Ko2AUK58TUGUhBWOG+tdWwZvV7M9HQVbSyVyKc/"
    "SklWu46e0vNpVSKW/AGbw5iljR6h53Fxtcd8u8LBvdO0W3Uur25S8aDT6yKEJAiCMhF10vOntSZJktLQK6A0w6HDswVBwOEjR7BC"
    "sXJ6gQcfOMnaygJHb/9Gllc22Lu3hVSW0UgQeJIkcWOUaAHCR1pNyCJJHFKtzRJWZxmZPt/+1jvpD1OsVMzOtFEedAcpg8zn8N42"
    "QkXMzMxQr9UZDlbQSYzRCaOhotGosdmJWVjuEviCejTN7Pw8Z89fJB72CWttpPKwJPieJEk1qVXMz82xsLjC8vIyCwuLPBQEzM3N"
    "s2/vHvbt28u07DBYfYC19cfo6yrtI7dSb7dQfoinLJbEwdAsxKmhM0jxfUkUeXieoR40MStVtBSMUKggQKUahcaiSa1PKkJk1UMG"
    "GjHcpJL2ydIUaxvEcUil4rm2WwvWkBgLnu84gKXY8mK1dvysKPZ6oYyXBuPVvC/ji7hzt3lTRAmL+d9HdnI+XP2Ynb7barA6eMqA"
    "X3/3R/npf/u9rK73uOOWo7z7HT/CYJQw1ayRZppKFLC+2eOP//weAt+/AkO6833di/pnf/X9vPLFtzDTrhMn2VXbn2aaej3iD3/1"
    "X+aBFIvyFN3ugG/6vv9MtzcgDHzWN3s88OgZXvPSW+n1hxjjPNL3nznD4vIGlTBgcXmDp84ucNftxxnkGPPA93jgxGl6gyHTrcYV"
    "kBBwUcX1zR5/59vfwCtffCvrnR5TrTrv/L2P8KUHnuBnfvV9/NJ/+vskacb8bJN/8QPfzA/8q18uF9NWlipXw+Kdv/MR3vSqO/B9"
    "j0a9wg/8zbfwg//6HTvOiRQ5a4fnCts901w/05w/m7UAOQf8MOby8gZ75tpsbPb5+je+kLe/9RX89K+8j//7p36H33rPJ/iJf/09"
    "z7xWPnoPXuCiJs+2fcXnxrqE5YcePcPHP/cw3/SWl7C4vMHxw3t450/9EJudAY16hXototcflTC6zFiiHK70Xd/8Gm573hE63T7/"
    "8h9+Kz/wt95C4PtUKiFxnHD4wBw/+6vv58LlFfbvmXYOtacZ9+17UErB77z3k7ztTS8i8H3STPPjP/pd/MgPfjONnKvfWOdtf+fv"
    "foQg8PmzT9zL3/q21z1ju37mV97Hhcsr1Gvjolue56A0v/Wej/Nj//DbWFjeYG6mxW/87D9hMExoNaskSUoUBqxvdPnUFx4higJG"
    "o4QLl1dK2JPvKX7jZ/8xq+td3vSd/47ffd+n+Oa/9lICz2M0Svl73/Umvv0bXokxhtnpZslsJazYMl/P9Eza+r0AYfn993+ab3rT"
    "i6/pXte8BqoRvcEIEFe05er7QIAQvOv9n+Gb3vySZ933XRmLHFdTu/KFK6VL8kO56qrFC1opldMAiZx73P3tcOvOQlOeQPkSz1f5"
    "PxdKksoVpJFKonzl+LylRAqJkoosdXRsQZkkZxFSOYW9SHAULgHWz2mRwJYYtQLnrjNDlpec15nGGpcN7SmJsY7RJYocZ7E7XtNu"
    "NTh8aA979806asjhKA85G9bWNhkMR7RbTQ4dPMLe/Xux0ufQvj3cceNRXnXbUV5+0zwNf0TgQZYv0iJ5FsYRhzJJt4AdGEsWZ45/"
    "3h2JyQSZsXi+QhvY7I4YjRKq9QqVagTkWPcJ5UoKiVAeyvMQUk1YxDnuLefMt0IgpeOuF0LSalfZN9tw8AuliCKfXpyx0RvRH8Ss"
    "92Ma1YiVzZhmNaLdqnDy3CK9YUKcZQTKwZG0NgyHI/r9AaNRTJalJYNMsU7CMKRer1OtVgmCAM/z8DwPpRSj0YiFhQUeffQkF86c"
    "xOoRFxc2SRLL2uoa5x+/O/cKJHj5evQ8VYZrlRQo5WGsD3qEGZ1F6hUW1z0+ef+AlbURH/jTe7A2ZW1tyMWLaxw9uI/u+kX+8Dd/"
    "GmFhdn7Web/SEVk8Qnl++ZIPKz7aWs5cXKHZmiGshMSjAWmakWkIKxW0dfPeHWXMzs9hjcXzQ6LIYQEXFi5zz7338OGPfJS7v3gf"
    "m51NGl7GgaiDvPhpLj7wZ5x9+PMMNlcYxRovrCCVcjUQPEGSWvqxpjfUjDKL9HwajYhmMyKqBARB6NpQJGArjU4TYuuRqSZpuAft"
    "tbCZpqbXGC6fgdEmJkvJtEAqH+mHhEHgvHdlxKSAgokSuiJkjmQXojTAtiLRJyIs413g1uCWB3IBvXkaBfkZHmRfaZlU6q7m+dl6"
    "zJVGh+fJ8nspBNq4AnPvet+n+YVf+yCtRhXfUwSBz1SrhrEOr7220eOf/vt3cvKpi0RXKV++/b7GuGTLU2cX+IVf+2Oq1cg977a1"
    "f3yue35OtepMt+tMtfOfrfoWZJIQ8NCjZ0gzXdaaqFVCHnr0DN3ekDDw6faHPHzyHLVKVNakiJOsxLfvZHhI4dgrrj+6j3/8d99G"
    "kmZMt+vcfe9Jfv+PP8vBfbN88KP38Hvv/wxzM026/RFve9OL+etveyWd3mBL3zzP5fxEYcCJx8/xrg98lqlWnX4/5q1f+yLe+Ko7"
    "6faHLtdp25w8nbL9bOb82a4FiyNo6A1GvPsDn6ESha6wjpS02nUXwauG175WTl0kDAPg2bVvy+cFEYUU/PjP/T73P3yaffNTJeBt"
    "z1ybdrPGJz73sBtPJcZGn3Le1B/58f/J6fOLTE81sRZazRpRXgio3azxO+/5BD/5y+8lCoI8qrN1XK4+1qqsM/Clh57k3/zkb2Ox"
    "JRXxVLuOlIJaLaQShfzHn383H/3MQ7SbVdY2etfUrp96x3uJwuAKRblWCfkfv/Nh3v3Hn2XvfJso9Al8j6l2DSw061WEFPzHn383"
    "J09dzCvBhnzicyc4cfIce+baeEpRjULajRr1asRn73mM//KLf0i1GtKoV0iSjGa9woG9MyyvdnjosbPUaxFSiS3zNTkezzxehno1"
    "4nP3nOS//tJO95pmebXDg5P32rYG7nvoKfbOTZW6yvxsi3arxufvf5zRKCUK/C1tebp9UOTj3H3vY9fenh320q7AlvhhAW0oq0BS"
    "wC/GWPVChJA5xHUisD0Z4xYCUUTUofSSF5SEJdbdOg9xMfGFnmuMRUhnJIjcs+4pidaO6SbyXVXQ1Bq00Q7HblyIysFonHJQ8NpK"
    "5WG1zhPqPJIkwwK+73jmrTVOuTAWpGCqVSfNNMN4yL59c5w48QRJkrJ//yxtz2NjvUOrVcdTzrPuBRUaNcNbX3oTSyvrXFjvcvJy"
    "ghUefuE25UrYgRsDnSszLsSRJSk61Xi+R9ck1GpuM/iBq7zYalUZDmLSJCvnhnwqlHLKue+5h63JPRBGu0hKlml83/HM6ywjUB43"
    "HZ7FE4L1TszCep+je1uQs+AEvmJxrcv1h2ZZ7w5pNEK6/YR9My1OnFmiWYto1APHV54ZqmHgoDziSku8KMDkoiPj5JcCF1mvN8Aa"
    "4swQdy8SJiHDYZ/OKKB38jMMhz1C38tx6BYpNaORKSv1Og507YpIGVDCR8c9fNslyyo8fnEaFR2h5m+yZ0YyN9NAmR6nzo244fA0"
    "o1GHWq3pMuuTlO7KBXSaERw4QlipkOSJ0qnQZPg0qlW6gz6tagCBxyhO0MYSBCH9kebgdJuoXidLneccIVwUSIboTLO0tMjS4gJh"
    "VGFqZoZD+/fSbk9RNYtkq4usDQ2Xe/vp06ZRPYjvR2Rao6RBYhimljiBuB+TZRrlKZqNiCROsEqRJCkVP2R9cwAIPCFAZ6Q2AFHB"
    "+lWUTfHNADvoIrUgNk0koTOmpCrnzBbwrGJ7k0fk8meEtc67s7VITgF6n9QEd3gK2dzbbsnDe2NWmr8M0IwQosQ8d3oD+sP4CsVu"
    "EmrR6Q7o9oZb1FMLdHtDZzDjji32qed5/PjP/z5fevBJvvXrXs4Nx/dTq4RsdPrc+9Ap3vl7H+HRJy7QqF2ZIPl099Xa0KhX+L33"
    "f5rXvfx2XnLXjWxs9ukNRuVzffJcx1OetzeHxnR7g/IzYwxhGPDgo2c4f3GFajXMvWGa+x5+qoyaWGu5/8RpVtY69AYjAl9xeXHI"
    "g48+Db5duOJLf/vtbygL8USBz8+98wOMRglBo4Lve/zs/3g/d956jD2zbVaSDt/3HW/k4599iFGcOmYs7ZgGkjgFIAx9fv1df87r"
    "X3E77aarR/A93/ZaPnn3w2Ra0+0Ny3PiiTm51nVxxdjvMK7XuhaMttSqEb/7vk+Btbz9ba9kbqqF73kMRkmpBF3LWnF443i8bp+p"
    "fVf53BjHBnT+4jLf/Y/+G9//nW/i9a+4nVazxup6lz/92L286/2f4b3v/DH3zi4M+1ypfvCxs3zHD/4kf+tbX8vLX3gze2bbaGM4"
    "d3GZ9334C/z+Bz6DIH9eG0vnKvNxtT3omJQq/M57P8WTZxb4rm9+DbfffIR2o0Z/MOKxJy/wO3/0KT7+uYeoVhzRxbW3y+kbk++t"
    "IjKcZpp/9u/fyae+8AhvfcMLOXZ4D1HoeOUfefw8v/2eT/LZex6jVo1yHUWy2enzD/7Pd/BDf+fruevW4zQbVTq9QWmA/Pff/DPO"
    "nF/ku7/ltVx/bB9aG85cWOInf/m9fM3t13Hb846wsdmjO8Gu0ukNHbTqWYxXtRLyjt/8M86cX+K7vuW13HBsH9oYzp5f5iff8R5e"
    "cNt13D5xL2MMYeBzcWGV7/mnP8v3f+ebeO3LbqPVcEbQRz79AL/7vk/xv37mn5Qw3VGOSX+6fVA8U6rRs2vPrtP9ShG//QcftM5L"
    "rcvNPOkVBq5UwibC5ZaCXca9xbc8CCegIk5hLz/eIsXmKO+RX99Yk29y5z1WUjivvNaEgYfBMhjEaK3Lsu/DYYIVzjLVmYPMCCnw"
    "lWOYSbUp8WgmV2SLKmeupG/KZqeH0dBs18h0Rr1WJ45jet2B46w1luEgYXq6iee74gOLi8tcurzE9FSbeDRkGCcMEsMj51ZZ6qYu"
    "gW/cvbKvIn+BUWArrc359J2iLZQgrAS0WxU8TzEcpc5bpiSrK12Gw7Q8x3nvs7HyZDV+GICwJMPMKVZYgigkiVOM0cxMNXj+9XvR"
    "RhMnmicurnJwvkGrEnBuucvKeg+B5c7r97G00Ucby3pnQBR4LK12eelth5DCsrjW581fc5hGJboCjzuZ9LyTlOsuN9YsEoZPkg0W"
    "STWOm33kWBOGw4w4r+6bphlJ6ozNJMlI8hCbUy4M1lCWkUYYDBZUG+tPEamMuVbGdMPj4SeXuXBxlVe86jU88uQaj5x4kEa9ztlz"
    "58BKZvYdIWrN41Xb+L6i3+szP1Uj2zjLiUefZO7g9czvP8ZN1x3g5JMX6AxGaGM5Mlfn8rnHuLiwhictWL0l0iKKBcB4HUZRxMzs"
    "LPv372eq1UAIySjJSPHIgnm85jzV9jSZEdSrIZun7kXWphmkHsoXKAlZklKvBmAFUeSz0RuBFNQl9Eea0ShBkOZJ2xKNU5J9mWDi"
    "AcLEJL11Ll++TDyK87W1jUs9t7CLPhReuaI/xZ4uQqklVWzxPAG2MEXlBn2p5JfPi9xBwM5Rwa+GWOtwngUbBdbmxZO2HhMGPkF+"
    "jFubcflsE0ClEpZRyiTJyhdtMWa9/hDf92jWKyilSNPMJWcqSSUKd8RaP+N9BSXDRq3gIbeWwSgpX8jFuVfp/I59rVWj8fhbxwoy"
    "yXEupaASOY+vwOHuB8OEp5syIYSDJeT87NoY+oNRqTwV/PJR4BOGDnrnnoEJaZpRq4bufsIlLSaJS87UWlOJQnzfeWk9pegNxjCf"
    "7edc67racex3GNdnsxYK6Q9G1GsRlTwKXBxTsGtcy1p5Vu27yueDnKWlUgncMzXJ8H1FmEMrF5bXOHxgng/99r8j8H2a9Qr//qd/"
    "t0zytblCGccpzUbVFVYEeoMRg8GIeq0yoWNANQrzCPrW+XimPSilpD9w+WWtpotGaG3Y7A7Q2myBuxTHX2u7rrZWrbX0+kOinEa0"
    "KGi42e2Xe2TynoUybYyh3ayj8gJgxdqQQtDtDwlDn2aeb9btDYkTF30q2FeKeQEczeNzGa+d7tUfEsdX3ms4ijEWlBQkaUYcp7Rb"
    "dQJfEScZm50+lShw14Hxmo5TwvDq+2BSnlV7rnKNv8oi/te73m+LcGHJALNDgsvkMVLK/KGdhxiFg2TIHRZ+qa7nL9/ChyYmrou7"
    "0hajobxX8XIXAk+CELni7lzKDEdOAfU9RRSFJElKnGYl/3um82JF1mKNw0JKJQk9D20y0syQpgbPlzl3sGGz02U4jKnVq+461qIk"
    "CCRJmpBlLpkXoFqNiJOEXm/EwqVLSCWY27MHrTVxr8fC0kUeuBiz0LEEymIgx2655F5RDIidHGOnzDtFJ1fwlcQLFJXIdxVPI596"
    "LaSzOWBjY4g1lmLaPCWp1ELHR5vTTY4Grix1tRZhjSGJY4Iw4Jbj8+xv13ni0iq9YUqgBPVagNWWJy+uYqx7Cd9xfC8b/SGeFGij"
    "OXt5E4Tl4GyLdiNiszvkr73wCLXQJ9uhUMpOa6nEmhZGB5a11VVWVte4+bDG6hhhM4RNSBJNHCckmSGOU9I0Q5tcYU8zklSjjWMl"
    "SjKNsC6DPbcC0caSZhqTpU5hDKcxskGrYqiHQx5//Bz7Dt9MZeow73vPuzl2/Dr27t3LyUcf4dKlCwTVNrX2HFFjH0GtQbUSMBf1"
    "+cwnP0N9ei+1maNMzbSoVSokcUynN8T3JC3V476HHsdXEqtTXHEyW8752CntxsBYlwthjSGMKszNzbF3zx7q9WrpiRuYEKrzVGaP"
    "YNYv4NebGFUnSXoESpAkbj3HaUYj8tFW4nmC+WZIZ5Cw3k9I4xS0RgjwPEGvlxAEjmIuCiR27TQXL12g3x9MGPFibLSXEbkJhpl8"
    "jzuLM4fZISe6Kcq+2nxPjwN0xfX/8hV3cBEdO/ES3inR85mOmaQAFFJcEdpW+XPUOU3cGExCX55r20QesdRmTA9YHLP93J1kp75q"
    "M8mhe+UxFrYU60JwTYmSBZVdcY6rbjrZF6fQF2221pZkBlcb3+K78t2SRxPgmefkmeRqY/+VWAtZ4WTY4ZhrXSvPtn2TnxcO9Gaj"
    "wm/+3D+j1axRrQT81ns+yX/4md8rDe5/8Le/jn/9Q29nMIypRAE/8K9+iQ9+9B4ajWpphMnc6Cra5moDyCucOk83Ls80pkU0PctM"
    "+d4snHw7Gb3Ppl1XExfZNWT5fhBCOMKOq9yz6E+Wz9v2fhT3LgpnecrpIanWO/b9yxkvldNvZ8W9cgjr1e5VjFlhQDsdQ5SG9SS7"
    "U9GWa3lufjnt2RUnHjDxYrY5M8uVsv2lKcFhpYtoWeExy6E17qT84PLN7Y4RYqvXeXyT/AgxLmzk1Fd3DeeYzkvKy6Jqq8mpzCxp"
    "qvPiTG4BGWsIPM8VgDKWDMe97rK+He2h7489gNa6h0FRgEgKlcNLshyC4ZS+MFI5PMA9NNM0Y3OzQ6vdcmXnux2iKODM+fMMk5Rm"
    "BBuDlFh7eEV1SZFDiSBX5t2GLCIPMmdiMHnDTKaJ04x4EDvmHm2oVUP27puiXosYjFK0zhj2E5BgBdSqEd3+gDR2SbHWGAbDmCj0"
    "2TM/RaMaEvk+ke+z2o2Jk4TZVhWdgRGWJDYIYfFCj0GaojPDUnfAXLvOTLvGoD/ikScXmJmpc3C+6ZKAJ16Wk1GU7dGb4vuCztNa"
    "g+d7PPTgQ3zms58hfOVhXvbi46yvpcQj4xKZhST0ZTn/w1HsIj5WOHhKv0OaCSphSBwP8/UsSTPnmXfMRS5hORsuI/0NeszQS5pM"
    "7znM1JSPjELa7WkePfEgnU6XF73s1WyuL3HPPfeyfukpwtoa1fY8o9oc88dmqdaqxMM+TZEyGMSMRglWC1qNCIuiEkmq1YBRbFDS"
    "A5OW+2LSI1cmXwmBzOFb2hguXbrEpYsXCcKI2bk5ZmammZnykPYy3bPnSTX0+3VU4xDSC7B+gPJilySbCYQnSQYajaQfZ1QCj16c"
    "EfkBRls63RGRr8pEVGWto1BVLgek1+uXVF7WThjiRTTNLdox/K3Ax1FG0XPnvJhIKjQgpFP58+fGhA3zv4VI4caukJ08cVuPuRIn"
    "7RSrcQRiuxTKgnsxuWfntdAQPtN9C8XO36H92/u1k+zUVk+N+7LTMQK25QJcG27csXdc/brWOgYu5JV9mbzfdniDUs5o3N6Wq51z"
    "rXK1sf9KrAUpKIvFbT/mWtfKs23f9s+FEKyu9zh7cZlvveN6Vte7/P3vfjPPu+4AJ06e49CBOd7y2rsYjRKiKOD8pVW+cP+Tjm0r"
    "VyqttWjrHHnSG9NV7qQcP918PNMeHCvfxVw/c+LmtbbralIozt7kPDjX8I7HF1EppXae/+LebhzcvGhrrjpfX8547Xgvc/V7FdfY"
    "ugdtaaDs1JZn2gdfbnt2xYm3lffVTcyWgjkwfumKfCLJFTGnsW8Jh0qxdTILhcAyxsgWStzkdinDVGLib5xyYIH8NV8mO7riAxDm"
    "zDHkoUKlFJUgIEkTjBBk1iAReaJefl9jMVLkyoMzBrLMwVSKIgGe8l1CqzfGkDvl14LNF6gU2NwCbTabxHFMlo4wnuTS6fMcPnKY"
    "i4urTEu48WDAIxfXubCa5C6xXMERFteK8YNnrM3nRgy29GTk7jSG/ZiFbIOZmQZ75uo0tWEwTPH8mOFwxLCfkiSa2XaVOHXhL8/z"
    "qFcCtDFMNaqcubxKJVSMMld9r92ocGmlT+jD/HSTSiUgDCQLq10Ekrl2g4trA6qhz9Jal6lmlVuv28uDp5ZY2egRhQFRFOXehbEC"
    "PwmVmTTKxklhWZ7cqjl08CAvfOGLSGyXfm9EuxnR9QQCyaDXY22t487PEgKl8CohUgzZ3FxnZt8tnL0U0x8OqFensdllLIYgcAU3"
    "3NpxFJIu6RTMYBG8NbJghgtLKYePWOr1OtILuXjxIr3P3cett93O1731bVw4d4Z7v3Qf6xdP4VWX6EzfwezsNKfPXCQeDVBBlSCM"
    "6GcxK2sxge8zVW0wN93i9KVVlPKwGDAGBxyxubEoywe8Lf5XvmA8BxszhksXL3DxwgUq1SrTMzPMTU/RbLURYkRv/QSx8RkFLbza"
    "FP7sHEorrBUI5ShGh3HKwMBgZPCloVnzSVOPQEmiauAiUkKCp5B+5PaWLGoDiHJP5hq8ixLkc1ysVSaPKb3wE3+Pnw7OuqT8Mf6c"
    "8fPmL1OuRbF7umNsOZnPdI1rO+5a7/tMxzwXhfVa2vjVu+7OxzyXsX8ubbzWa3y5a2G8b57u3tdwnWfZvsnP3RYW/Lf//kfcdetx"
    "Duydodsf8IZX3sFbXvcCssxRgYaBS9D86V/9I1bXOtTrV1aZvbb+fPlr6tnun2tp11f8ns9w/E79vNbPns33z/26sL39X6nny3Np"
    "z1918SY96UW4elLJgrECXojElTEvbSI7xigX+KvJz8HBQxBjhb9U4Hd4OZdeWtjiyRt78FzoBlGou6L0sqc5FaQVAl8q0izDClcR"
    "1mibVy+zLlKAg7xYI7asySyvTGeBLNVlAoYVzuoUFmzeeSkkvh9gzIAoVJw6dZnp6WmarSbtdoNaJeT8pWVMllD3oFmVrA9cmM3Z"
    "R/m98wRcZ8MzZsYrlNuJuZBKogykccalixsMhgkH9rWJAp+s4pJRBsMhNxyaZd9UjQfPLHN0/zRSWObaVbqDEV967BKh72EMBL7H"
    "/pkaka/oDR0ef7Mfo62hWqkQRQntWkjF9wg86MUJSMHiapckMzRbEUemGzSrIYNRvCV8N5krUbS/5He3jptfYDDGzfP8/B727z/A"
    "pcVlPvPwKabqHSLZ44nTG9x658u48c5ZFhbXmAorXDj1IPfd9wC33PlKnncoYnHxInF3icWlNQ4euY5mtUa/32G9q6lWq/gCRqMY"
    "Y1zUxVqDEQqTGVS2QIZPlh2i3nTMA55SmGTEI489SW94lCOHnscbZ/dw6fwZ7n/gIZ545AGuu+EGFBdJhz1saxYhBKHvkSEZpQkX"
    "lzrMzc1yYWkDIRTWerjCAzpPui5M07GhbK2LKEwqySDwfcczrbOMy5cucvHCBaqVClPTM8xMTzMzFWL0BoONFbrdiwyJsLMHsMJH"
    "+R5WGXybIYUlSQ39UUacgRBuvQch+AoyJPgRXs5MMzawxsmnua5eYtsnIW7jZ0cB1di2yYu1fOU3W58Dz/D9ruzKrnxlpWAnOnnq"
    "It/7wz/Hj/2jt/PC519HgYBTSlKpBFxaWOOn3vFe3vsnd+d48r847vtd2ZW/6iJ+5w8/aO2kEjnxEt5yIKX+UKgZuYI29tIXCa52"
    "h2vYSWU9FzPhYZ8MiUwqCUD+UMhVWiGQiJy7PWcqIaeZxHkBC++qzeEG+eWdomaKxFvn9CYPtzk+Wcdy4/hMbQHdd6wsdty+ydCY"
    "EIIg9Dl37hIrq+tcf91h1tc3WF/fYGlxkUMH99Ns1Dh74RKDUcylzojYBmwOMgajPFnRlp0uPe7WOh7TIgowaVlMGjbgwneVZoU9"
    "cw18T435m7Wje/Q9ybH9Uzx2bpX5dpVuP2a6FbHZjTk82+C243u4sLzOyuaQ1d6QTj+m3Yi4uLBZVqoNlODmY3u4+8Q5l/RrHETp"
    "8N4W1hhWuzFve/Ex9jRDUmO3KO9Fe3fEHUqHiRNijE00xriy1Nqyttlj4dIZLp85wUanwwte8AKi5lFuuPEmnvzSr/P46R57Dt3M"
    "nmaHp049Tru9l0oEly4v0++nbPaGXFzYwPhtZmb2MzXdxpOCNEvyCI6AtItJVkhHHQ7d+EqWVgd8/KMfwVqoNGdp778Ooy3SU3ie"
    "x/WH9tIMM0489AC9wZD19Q5W+NRnD1GfmiOqVBgOhg5PaQxHZ30ee+JxOr3McawbCzpD4moUuAJG5BCzAsplSxhJkaNB/rvIDbnJ"
    "tW6soVqp0Wy12DM/nydKaRIjGSQCUZulObOHWuTTzxTxYEglFMSxwfMEozihEvkIazAIIhGz/NQJLl1eJEmTKyB0Uiom6SFFvvec"
    "QQbKU66OQfEcKKEyonyQlNE8iv6UTxkmHQglDG/bM2lXdmVXvjoipaPrVFJy563HuPnGQ7TzQmDnLi7z+fseZ2F5g3o12vWO7squ"
    "/AWL+P0/+pAFpzw4Bpicoo8crmLMBGSDLYWXnELplGAHuTHOw23HypoUY284xTVL17kLlzu11F3LWoEQFmv0Fo+/pbivU5qVVI4G"
    "0uSYemHxVVGOO3MhezupCExCM/I7mrGXsHj0FBGBooCU1o56Kfe5gwVtLSZn4iloDbXWLC6tMT1VxwrLo488gY57PHxhk9n5OQ42"
    "JNZmLG30GRqfXiq5tJ5SuN6FAWuzMVIgb6uYgM5MKr7WGrBFvoAlM5bGVJ3rj8yxttGjN8jYWOtSa4TcdHSWNMsIfVeZcKoecXC2"
    "xcZgyNH5FmlqeWphhcfPr6KNIQwlKxsD9s208D3J5eUOh+eahJHH0kafQW/E6sYAL/RoVwPuunEff/L5x7njyCzf8uob2eyMtlRi"
    "LOdwB6+s4wJ3/xlryHSWG1numOmpFlZYLl1cZuHSk5w79RB7ZiPm9x1jrtbByhob68usrA84uyR5zeu+nhP3/An93jqZ8Xj+LQdZ"
    "72qeevwkC2sxIx3Rnt5Lo9kGkyKyVUS2xiAWnNqc4/h1N3KkmfDuP/ogaRzjRzVae28gqNWphAGdzQ20kbSbda47PA/JJl/80j30"
    "ugMya2m255iaP4T2IgI/ZDjos2+mwmBzgScvrBEogUlTt76NBuuUd3BZ/IUHu6TUzP9GUFYlLoy9gia1UGiNcetVCEFUqTDVnmJm"
    "ZppqxZVwj7VF2wDqM2SiSqPZxBiL71myLCPLrOOKTzSBssSLj7OwcDnHuRcYzTFszIG48nWaGxLF7pqMtNjx5prYj0VkblKRF1uO"
    "cd//5SSn7squ/FWXwoEwihOSJEPn1LCeUlSiAN/3dj3tu7IrfwniOa+yQImcrq2sbOoUdaPUFZ4xY0yOGZdllnvB9yyFK7ghiiTL"
    "XPkokbKF4iZxeBNhc0+cLD36wLaX9AQ+GpdAW3geRZkY56oBunsWVV5dcqcpHfuSgtVjrPhYHIpnwkOc/zOAUK4IjcrbobVLIkpT"
    "46qgCtBGI5Sk3qiystp13KlRyNm1VVrtJqtrG/QGdeoVxVRrjr0q4WOPr6PxUblSLpTAZqLEPZdDnnsbrXT9GrMr5H3MjSIpDaNe"
    "zPmFDlGkqFY9KpUpsIbeSFOPfKqhxwBLqxZRizxWe5bBKGO1O2C1n3B5uUdmNXtmGsy0Hf3TdDPkkaeWeP6ROQbGIKzkecf38tn7"
    "zwCW1FiqYcidNxzgsScv0e3HKOXGaSfIVDGPBZOMs4UMWmd5Iq6bN5WzAvUGQ3SWsf/APHv2zdOaOcDl86dYX10g62U0agMWNzyW"
    "e/vYc2CaRx59kDSzKGEZxhkbG12GI5+NuMbhfR7dXszG5hmyUYO9bRj0B1we1Lk0mqOTRdTXety4t0293mA9jjE6dSimTCNrHlFU"
    "Q+uU/mDA3fc/wS03HOG6Y0fp9wcMhkPOnDnPoL9BvTVLpTFHUGvSSyQzrTbBwiZWSoQ1SC3Qtlh3uoxkOerKIq9ClFEfcpx7iaUi"
    "1/nzfSaEKPckQpBlGQsLl7m8sEBUiZhuTzE1PUUYgBwuMEwNnU0fW5kmrDRotlrEaYxnAasRykd6AWEQ0KM/xrcXeySvdyClzKNY"
    "sjymjLaI8XyO535ik08YAhNXnjxwV3ZlV/6SpEj+rFZCRwfK2JFmrN1V2ndlV/6SxJPCMYhYRKlkW1swPdixQlsqX7ZUfgsP26Rn"
    "vPh7C7Y5Pzd3LOY0TgIjxoSHhf/OQOnBK0QIMBMve5Xjf52RsJWRYmtbHOuNEIVXsPiZZzGbvJAPW5VLYwzKE64YE+4hJYVwvNfC"
    "YLXNq7i6wgye5yGAmek2nc0eq6urSGm55eabufnm67l45hyfvfsLrHUDEm24oAEVIrMx5EYXJcGLapRjtHsOM8r7qQq+821QJumK"
    "LW2sblJtVggCHyUFmTasrq9hreHQ3hZH903RGSUsne5yYbnPynSP9cGIxeUu8SgBKRmOMhq1ACFgbXPE3tkm1XpEb73HTDPkgccv"
    "MdWusbzZ4yXH9xL4gkGiGRhY78XMtyokEw/17YmphcfYzZFjvPEDD5NZssxg7JhaS2fOMOx2eszOzzE7VWGmfScLy10unn+SqL8K"
    "ZkjcW8e2p6jUZjl8YJbH7/8ExmQ88vATJKklrE0R1mbw6xUajcv0Oj0urykupwdYT0IwEMmE5Q2DNjO0WnXWVlcxWcawv07Vd1Rn"
    "QejT2RwShCFVYGFxhX2tgNMnTvDCF76Yo0eP8vCJE6wsXiTsbtJozzIIp5g7MkW9ErAxcgXE3FrKjVwrAVMqwORRHwSOOrRcn0ys"
    "jHxMiw1iwRbcojn0yvM9B6fJMhYWF1lcWiIIAqamp2k1m9RDgU2XGfUvsbpew/gNTLUJKsTiIz1XiGm70bUlipInUY9jZhPHIvJ2"
    "Tqj8RcSrvObk7r267Krxu7IrfzmyHaq5K7uyK3+54o3xqVu50wuecsC9Z3MPqTEGKRRFQtpkpTGzzbNaSPmZdJ46gSyNAmtdkiAC"
    "hMwTXq3IITRjQwDjPOBKCqRSGG0cdMAY56mdUA6dzjNO+iuMEBjjxxGOEUbkSrBg0vAYK/IOa14oKlkO+3HGR8Hh6inH/661YW5u"
    "mlGc0B8MmZlqEfoejfY0N99+G5lWbFx+ioWhYRCDL8Ay4XneAi2h/NzZR5NsPpR9pOy6KDg6GXSGxH7mhjHNHMeqEowyw8XVPosr"
    "mwxHmuOHpjizuElvmJIOM6RShJFHrRqwuD7g1sMznLq4yd7pGu1qiLWWL5w4x/L6gBuPz7HRV1xY7qCEoD8cUY0C+kkeGbB6i8I+"
    "npuJPpK5MuQyh/x4kkxbV3wqN8mEkKRJhvScFzlNMqq1gEooeMUrXs3lxRUefvBz7JtTZN0T9JM9+N4+Wq0W2m7y0PkhU1WfY/Me"
    "1gtJ4g02u0NSOc3JTp1YQzXMSK1FKp84SUm1pdVsjY1BkxJGHsPBiEotIqpVsKlGCsEo0/jVKQTwqU99lttf+BJe8vLXsHL5PI8+"
    "fpLVhbME0SqrjePsm5ti49w6UgVYx/jonO1WlPqrzU1UC1uSoAs1XZSz7k4o95xgAlpT7rzcKy/wPFckWWvNwsICiwuLRJWIqfYU"
    "tXqdij/CZiOGK4toWSGtzhAJD88r6DrHD4NxFeStbXPGA8j853gvjZX3Ur1/Bn19Jz/8rvK+K7uyK7uyK3/VxRPCsaQwyfoCpa89"
    "j9LnIXGzhSqykC3JKWLsc9vRRi/gH7ZQji1K5IUEJoyH0tsv8he2dAq0kl4OtRElZbQnBeP6IAVW1pYK+NbWjI0LicBIM25YGUlw"
    "UBTsmIe1wA4XpZrtBKTDWkujUSXLMro9zdR0i3q9hjGCpaV1lJTcdfstjOKUD1+6yJ6W4mCccHE1wfccjrDoa5moapwKJ1X+Wc57"
    "LQCrHCtOgXEnN4TKvlrQeQliqRTWWIyG5eU+C6aDFNBsVFle79Ptxnl+A0hP0GpWufnwLN1BQqwtnf6IW4/McnG1x1pvyMXVPjcc"
    "nKZVjeg1UvZO1ejHCQhXzfWep5aYbwZUAv8KTLtbHiJPHC7m2ZBlbvnpzBa5wngKPOWTZhptMkwm2VzfpD9K8SMHl1pbX+elL76L"
    "J544yeyR6zn71EN48QqPfOkEe+Zb1GsRtXqDIwcbCKFYWT7P+qYlaB5EyIAgSNFxQpIKR9VoMrIURqlherqdR3VgOOhRj2MqzTah"
    "L+h3NvDDCp4U9Acj4tSyf/9+Tp06y5kzZ1ncGHHbTcd4/cFDnDvzFI+efJKTj5zg+bfdRCXySbVFqLwyLgJ0lkdVdLmfSqORcWLq"
    "tiDLGOOeL9/x9E+ezxYj2EWKnBc9SVIWFhdhcYkwDGm13Lqtqxg9vEiiDZ4X4nseSZq6SFmprBfPia0KtRg7/Cf2W6G8b5fx2ZPG"
    "xvibXVV9V3ZlV3ZlV3ZlUjwhFAibFwhwDCZjzGqhZ7sXqOd5JXNMgUHeiYGGbQrbFlpJMVYiVInPhfIFPqG8T54npUAiXcJMweoi"
    "BCpnt5DSTnBhF6E9kSsSOaNN7nEvtRwhS+aWMqSfKxmWnPLSmIniFz5aZ0jp+l6UMDbGVeaTUuD7PtZq6rUQT3koJUnTjLW1Dt1e"
    "D09a1nopDvIj0CZH95dGk8Vq4wwTkTfVjBNpkSCsxIqCojKHHtncc1tOQR4FKSrxIdBJChiQivX1Ltbmldp8BVJjEcxP1YgCj8zA"
    "5dUu2hj2zDR4anEdbV35cKkEge8T+Ip9My0+f/ICh+fbrAQBF1Y2yKyLjKR6a7XFMXe7LTU1Y3KDJSuUvRyOhFPi4yRz1e08gdaZ"
    "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"
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
            slot_id, _ = _brief_slot(datetime.now(timezone.utc))
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

def recent_partnerships_html(days=7):
    """MAIN page: only partnerships / TradFi deals detected in the last `days`.

    Ageing is implicit, not a separate store: this view and the full Global
    Partnership Directory on the Institutional page both read the same
    PARTNERSHIP_LEDGER. Once an entry passes the window it simply stops
    matching here and continues to appear in the Directory -- so nothing is
    ever moved, copied or lost, and nothing is ever backdated."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    recent = []
    for e in PARTNERSHIP_LEDGER:
        if e.get("source") != "detected" or not e.get("date"):
            continue
        try:
            if e["date"].astimezone(timezone.utc) >= cutoff:
                recent.append(e)
        except Exception:
            continue
    recent.sort(key=lambda e: e["date"], reverse=True)

    if not recent:
        return ('<div class="home-base"><div class="home-base-icon">\U0001F91D</div>'
                '<div class="home-base-title">No New Deals in the Last 7 Days</div>'
                '<div class="home-base-sub">This section fills automatically as new '
                'partnerships and traditional-finance deals are detected from the live '
                'feed. Nothing is backdated or invented \u2014 an empty week is reported '
                'as an empty week. The complete history stays in the Global Partnership '
                'Directory on the <a href="/institutional" style="color:var(--hdr)">'
                'Institutional</a> page.</div></div>')

    out = ""
    for e in recent:
        col = ENTERPRISE_CATEGORY_COLORS.get(e["cat"], "var(--tx)")
        title_html = (f'<a href="{html.escape(e["link"] or "#", quote=True)}" target="_blank" rel="noopener">'
                      f'{html.escape(e["name"])}</a>') if e.get("link") else html.escape(e["name"])
        out += (
            f'<div class="pl-row">'
            f'<div class="pl-top"><span class="pl-cat" style="color:{col}">'
            f'{ENTERPRISE_CATEGORY_LABELS.get(e["cat"], "\U0001F195 New Deal")}</span>'
            f'<span class="pl-new">\U0001F195 NEW</span>'
            f'<span class="pl-status" style="color:{col}">{html.escape(e["status"])}</span>'
            f'<span class="pl-when">{_time_ago(e["date"])}</span></div>'
            f'<div class="pl-name">{title_html}</div>'
            f'<div class="pl-meta">{html.escape(e["detail"][:140])}</div>'
            f'</div>')
    return out


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

def _intel_stats(pairs):
    """Compact stat strip used by US Intelligence / Global Pulse."""
    return ('<div class="intel-stats">' + "".join(
        f'<div class="intel-stat"><div class="is-n" style="color:{c}">{v}</div>'
        f'<div class="is-l">{lbl}</div></div>' for lbl, v, c in pairs) + '</div>')


def _intel_bars(rows):
    """Labelled count bars; width is share of the largest row."""
    mx = max((v for _, v, _ in rows), default=0) or 1
    return '<div class="intel-bars">' + "".join(
        f'<div class="ib-row"><span class="ib-l">{lbl}</span>'
        f'<span class="ib-t"><span class="ib-f" style="width:{v/mx*100:.0f}%;background:{c}"></span></span>'
        f'<span class="ib-n">{v}</span></div>' for lbl, v, c in rows) + '</div>'


def _intel_heads(stories, empty="No stories in the current cycle."):
    """Real headlines from the pool -- linked, sourced and timestamped."""
    if not stories:
        return f'<div class="ih-empty">{empty}</div>'
    out = '<div class="intel-heads">'
    for s in stories:
        dot = {"bullish": "var(--gr)", "bearish": "var(--rd)"}.get(s["sentiment"], "var(--tx)")
        t = html.escape(s["title"][:110])
        link = html.escape(s.get("link") or "#", quote=True)
        out += (f'<a class="ih-item" href="{link}" target="_blank" rel="noopener">'
                f'<span class="ih-dot" style="background:{dot}"></span>'
                f'<span class="ih-t">{t}</span>'
                f'<span class="ih-m">{html.escape(s["source"])} \u00B7 {_time_ago(s["dt"])}</span></a>')
    return out + '</div>'


def us_intelligence():
    """News-derived US briefing. (Upgrade point: swap internals for a Claude API call,
    keeping this computed version as the fallback.)"""
    pool = NEWS.get("pool", [])
    ts = NEWS.get("updated")
    us = [s for s in pool if _matches(s, US_KEYWORDS) or "ripple" in s["title"].lower()]
    if not us:
        return {"pulse": "Awaiting US market signals \u2014 the news feed is still loading.",
                "regulatory": "No US regulatory headlines in the current cycle.",
                "institutional": "No US institutional headlines in the current cycle.", "ts": ts,
                "n": 0, "bulls": 0, "bears": 0, "neut": 0, "breakdown": [], "top": [],
                "lead_src": None, "n_sources": 0}
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
    # V135: additional breakdowns + real headlines, all derived from the same
    # story pool. Counts are actual matches -- never estimated or padded.
    legal = [s for s in us if _matches(s, {"court", "judge", "ruling", "appeal", "lawsuit", "settlement", "litigation"})]
    legis = [s for s in us if _matches(s, {"congress", "senate", "house", "bill", "act", "legislation", "lawmaker", "clarity"})]
    enforce = [s for s in us if _matches(s, {"enforcement", "fine", "penalty", "subpoena", "investigation", "charges"})]
    breakdown = [("Regulatory", len(reg), "var(--bl)"), ("Institutional", len(inst), "var(--gr)"),
                 ("Legal & Courts", len(legal), "var(--yl)"), ("Legislation", len(legis), "var(--or)"),
                 ("Enforcement", len(enforce), "var(--rd)")]
    top = sorted(us, key=lambda s: s["dt"], reverse=True)[:3]
    sources = {}
    for s in us:
        sources[s["source"]] = sources.get(s["source"], 0) + 1
    lead_src = max(sources.items(), key=lambda kv: kv[1])[0] if sources else None
    return {"pulse": pulse, "regulatory": regulatory, "institutional": institutional, "ts": ts,
            "n": n, "bulls": bulls, "bears": bears, "neut": n - bulls - bears,
            "breakdown": breakdown, "top": top, "lead_src": lead_src, "n_sources": len(sources)}

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
                "thesis": "Region signals populate as feeds report in.", "signals": signals, "ts": ts,
                "total": 0, "bulls": 0, "bears": 0, "neut": 0, "active": 0,
                "reg_counts": {}, "busiest": None, "top": []}
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
    # V135: per-region volume (not just lean) + real headlines from the pool.
    reg_counts = {}
    for r in REGIONS:
        rs = [s for s in pool if s.get("region") == r]
        reg_counts[r] = (len(rs),
                         sum(1 for s in rs if s["sentiment"] == "bullish"),
                         sum(1 for s in rs if s["sentiment"] == "bearish"))
    busiest = max(reg_counts.items(), key=lambda kv: kv[1][0])[0] if reg_counts else None
    top = sorted(pool, key=lambda s: s["dt"], reverse=True)[:3]
    return {"pulse": pulse, "thesis": thesis, "signals": signals, "ts": ts,
            "total": len(pool), "bulls": bulls, "bears": bears, "neut": len(pool) - bulls - bears,
            "active": len(active), "reg_counts": reg_counts, "busiest": busiest, "top": top}

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

# V132: four editions per day, on UTC. Slot times are the single source of
# truth -- _brief_slot, _brief_next_run_dt, the countdown timer and the
# on-page copy all derive from this list.
BRIEF_SLOTS_UTC = [(6, 0), (11, 55), (18, 0), (23, 55)]

def _brief_slot(now_utc):
    """Return (slot_id, edition_label) for the edition currently in force."""
    d = now_utc.date()
    mins_now = now_utc.hour * 60 + now_utc.minute
    chosen = None
    for h, mi in BRIEF_SLOTS_UTC:
        if mins_now >= h * 60 + mi:
            chosen = (h, mi)
    if chosen is None:
        # Before the day's first slot -- the last edition of yesterday still stands.
        d = (now_utc - timedelta(days=1)).date()
        chosen = BRIEF_SLOTS_UTC[-1]
    h, mi = chosen
    return f"{d.isoformat()}-{h:02d}{mi:02d}", f"{h:02d}:{mi:02d} UTC"

def _brief_next_run_dt(now_utc):
    mins_now = now_utc.hour * 60 + now_utc.minute
    for h, mi in BRIEF_SLOTS_UTC:
        if mins_now < h * 60 + mi:
            return now_utc.replace(hour=h, minute=mi, second=0, microsecond=0)
    h, mi = BRIEF_SLOTS_UTC[0]
    return (now_utc + timedelta(days=1)).replace(hour=h, minute=mi, second=0, microsecond=0)

def _brief_next_run(now_utc):
    return _brief_next_run_dt(now_utc).strftime("%b %d, %H:%M UTC")

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
    now_utc = datetime.now(timezone.utc)
    slot_id, edition = _brief_slot(now_utc)
    BRIEF["slot_id"] = slot_id
    BRIEF["edition"] = edition
    BRIEF["generated"] = now_utc.strftime("%b %d, %Y \u00B7 %H:%M UTC")
    BRIEF["next_run"] = _brief_next_run(now_utc)
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

# Global Trading Hub Overlap (V133). Desk hours are 08:00-18:00 local in each
# hub; offsets are read live from the tz database via _tz(), so DST shifts in
# London, Zurich and New York are always current and nothing is hardcoded to a
# season. Computed server-side using the same helper the World Clocks use.
TRADING_HUBS = [
    ("Singapore", "Asia/Singapore",   "asia"),
    ("Hong Kong", "Asia/Hong_Kong",   "asia"),
    ("Tokyo",     "Asia/Tokyo",       "asia"),
    ("Seoul",     "Asia/Seoul",       "asia"),
    ("Dubai",     "Asia/Dubai",       "bridge"),
    ("Zurich",    "Europe/Zurich",    "europe"),
    ("London",    "Europe/London",    "europe"),
    ("New York",  "America/New_York", "americas"),
]
HUB_OPEN, HUB_CLOSE = 8, 18


def trading_hub_overlap_html():
    now = datetime.now(timezone.utc)
    now_frac = now.hour + now.minute / 60.0
    hubs = []
    for city, tzname, region in TRADING_HUBS:
        z = _tz(tzname)
        try:
            off = now.astimezone(z).utcoffset().total_seconds() / 3600.0
        except Exception:
            off = 0.0
        start, end = (HUB_OPEN - off) % 24, (HUB_CLOSE - off) % 24
        segs = [(start, end)] if start < end else [(start, 24.0), (0.0, end)]
        hubs.append({"city": city, "region": region, "off": off, "segs": segs})

    counts = [sum(1 for h in hubs for s, e in h["segs"] if s <= u < e) for u in range(24)]
    max_c = max(counts) if counts else 0
    best_start, best_len, cur_start, cur_len = 0, 0, -1, 0
    for u in range(24):
        if counts[u] == max_c:
            if cur_start < 0:
                cur_start, cur_len = u, 0
            cur_len += 1
            if cur_len > best_len:
                best_len, best_start = cur_len, cur_start
        else:
            cur_start, cur_len = -1, 0
    open_now = sum(1 for h in hubs for s, e in h["segs"] if s <= now_frac < e)

    def fmt_off(o):
        sign = "\u2212" if o < 0 else "+"
        a = abs(o); whole = int(a); mins = int(round((a - whole) * 60))
        return f"UTC{sign}{whole}" + (f":{mins:02d}" if mins else "")

    rows = ""
    for h in hubs:
        bars = "".join(
            f'<div class="th-bar {h["region"]}" style="left:{s/24*100:.4f}%;width:{(e-s)/24*100:.4f}%"></div>'
            for s, e in h["segs"])
        live = any(s <= now_frac < e for s, e in h["segs"])
        dot = ('<span class="th-live" title="Desks staffed now"></span>' if live else
               '<span class="th-live off" title="Outside desk hours"></span>')
        rows += (
            f'<div class="th-row">'
            f'<div class="th-name">{dot}<span class="th-city">{h["city"]}</span>'
            f'<span class="th-off">{fmt_off(h["off"])}</span></div>'
            f'<div class="th-track">{bars}'
            f'<div class="th-now" style="left:{now_frac/24*100:.4f}%"></div></div>'
            f'</div>')

    # Leading cell labels the scale so the hour ticks are unambiguous.
    axis = ('<span class="th-zone">HOURS \u00B7 UTC</span>'
            + "".join(f'<span>{u:02d}:00</span>' for u in range(0, 24, 3)))
    peak_end = (best_start + best_len) % 24
    return (rows, axis, open_now, len(hubs), f"{best_start:02d}:00\u2013{peak_end:02d}:00",
            max_c, f"{now.hour:02d}:{now.minute:02d}")


def world_clocks_html():
    now_utc = datetime.now(timezone.utc)
    # V132: briefing times derive from BRIEF_SLOTS_UTC so the clocks can never
    # drift out of sync with the actual publishing schedule.
    _base = now_utc.replace(second=0, microsecond=0)
    _slots = [_base.replace(hour=h, minute=mi) for h, mi in BRIEF_SLOTS_UTC]
    _ord = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
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
            + "".join(f'<div class="wc-b">{_ord[i]} {_fmt_local(s, z)}</div>'
                       for i, s in enumerate(_slots))
            + f'</div>'
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
            num_col = "#ffffff"      # V135: white reads far better on the green tint than green-on-green
        else:
            bg = "var(--s2)"
            bd = "var(--b)"
            num_col = "var(--br)"    # V135: was --tx, too dim for a headline figure
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
    # V135: expanded panels
    us_stats = _intel_stats([("Stories", us.get("n", 0), "var(--hdr)"),
                             ("Bullish", us.get("bulls", 0), "var(--gr)"),
                             ("Bearish", us.get("bears", 0), "var(--rd)"),
                             ("Neutral", us.get("neut", 0), "var(--tx)")])
    us_bars = _intel_bars(us.get("breakdown", [])) if us.get("breakdown") else ""
    us_heads = _intel_heads(us.get("top", []), "No US-focused stories in the current cycle.")
    us_srcline = (f'Drawn from {us.get("n_sources", 0)} US-reporting source'
                  f'{"" if us.get("n_sources", 0) == 1 else "s"}'
                  + (f' \u00B7 most active: {html.escape(us["lead_src"])}' if us.get("lead_src") else ''))
    gl_stats = _intel_stats([("Stories", gl.get("total", 0), "var(--hdr)"),
                             ("Regions live", gl.get("active", 0), "var(--tq)"),
                             ("Bullish", gl.get("bulls", 0), "var(--gr)"),
                             ("Bearish", gl.get("bears", 0), "var(--rd)")])
    _rc = gl.get("reg_counts", {})
    gl_bars = _intel_bars([(REGION_DISPLAY.get(r, r), _rc[r][0],
                            "var(--gr)" if _rc[r][1] > _rc[r][2] else "var(--rd)" if _rc[r][2] > _rc[r][1] else "var(--bl)")
                           for r in REGIONS if _rc.get(r, (0,))[0] > 0]) if _rc else ""
    gl_heads = _intel_heads(gl.get("top", []), "No global stories in the current cycle.")
    gl_srcline = (f'Busiest region: {REGION_DISPLAY.get(gl["busiest"], gl["busiest"])}'
                  if gl.get("busiest") else "Region volumes populate as feeds report in.")
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
    _now_ct = datetime.now(timezone.utc)   # V134: slots are UTC (see BRIEF_SLOTS_UTC)
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

    # V133: Global Trading Hub Overlap
    th_rows, th_axis, th_open, th_total, th_peak, th_peak_n, th_utc = trading_hub_overlap_html()

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
    # V132: MAIN-page "new this week" view over the same ledger
    nd_html = recent_partnerships_html(days=7)
    nd_count = nd_html.count('class="pl-row"')
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
  .rh-num{{ font-size:32px; font-weight:900; font-family:var(--mn); line-height:1; text-shadow:0 0 10px rgba(0,0,0,.55); }}
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

  /* V135: expanded US Intelligence / Global Pulse panels */
  .intel-stats{{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin:10px 0 12px; }}
  .intel-stat{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:8px 4px; text-align:center; }}
  .is-n{{ font-family:var(--mn); font-size:20px; font-weight:900; line-height:1; }}
  .is-l{{ font-size:10.5px; color:var(--tx); margin-top:3px; letter-spacing:.4px; }}
  .intel-sub{{ font-size:11px; letter-spacing:1.4px; text-transform:uppercase; color:var(--hdr);
               font-weight:800; margin:14px 0 7px; border-top:1px solid var(--b); padding-top:10px; }}
  .intel-bars{{ display:flex; flex-direction:column; gap:5px; }}
  .ib-row{{ display:grid; grid-template-columns:104px 1fr 26px; align-items:center; gap:8px; }}
  .ib-l{{ font-size:12px; color:var(--tx); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .ib-t{{ height:7px; background:var(--s2); border-radius:4px; overflow:hidden; display:block; }}
  .ib-f{{ display:block; height:100%; border-radius:4px; }}
  .ib-n{{ font-family:var(--mn); font-size:12px; font-weight:800; color:var(--br); text-align:right; }}
  .intel-heads{{ display:flex; flex-direction:column; gap:7px; }}
  .ih-item{{ display:grid; grid-template-columns:8px 1fr; gap:8px; text-decoration:none;
             background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:8px 10px; }}
  .ih-item:hover{{ border-color:rgba(3,177,252,.6); }}
  .ih-dot{{ width:8px; height:8px; border-radius:50%; margin-top:5px; }}
  .ih-t{{ font-size:12.5px; color:var(--br); line-height:1.45; }}
  .ih-m{{ grid-column:2; font-family:var(--mn); font-size:10px; color:var(--tx); margin-top:3px; }}
  .ih-empty{{ font-size:12.5px; color:var(--tx); font-style:italic; }}
  .intel-foot{{ font-size:11px; color:var(--tx); margin-top:12px; border-top:1px solid var(--b); padding-top:8px; }}
  @media(max-width:700px){{ .ib-row{{ grid-template-columns:82px 1fr 24px; }} }}

  .nav-marker{{ text-decoration:none; transition:border-color .15s, background .15s; }}
  .nav-marker:hover{{ border-color:rgba(3,177,252,.7)!important; background:#1b2537; }}
  /* V133: Global Trading Hub Overlap */
  .th-axis{{ display:grid; grid-template-columns:118px repeat(8,1fr); font-family:var(--mn); font-size:10px;
             color:var(--tx); border-bottom:1px solid var(--b); padding-bottom:5px; margin-bottom:8px; }}
  .th-zone{{ font-weight:800; letter-spacing:1px; color:var(--hdr); }}
  .th-row{{ display:grid; grid-template-columns:118px 1fr; align-items:center; padding:5px 0; }}
  .th-row + .th-row{{ border-top:1px solid rgba(26,32,48,.7); }}
  .th-name{{ display:flex; align-items:center; gap:6px; padding-right:10px; min-width:0; }}
  .th-city{{ font-size:13px; font-weight:700; color:var(--br); white-space:nowrap; }}
  .th-off{{ font-family:var(--mn); font-size:9.5px; color:var(--tx); white-space:nowrap; }}
  .th-live{{ width:7px; height:7px; border-radius:50%; background:var(--gr); flex:0 0 auto;
             box-shadow:0 0 6px rgba(72,255,130,.8); }}
  .th-live.off{{ background:#33405a; box-shadow:none; }}
  .th-track{{ position:relative; height:22px; background:var(--s2); border-radius:5px; overflow:hidden;
              background-image:repeating-linear-gradient(to right,transparent 0,transparent calc(100%/24 - 1px),rgba(26,32,48,.9) calc(100%/24 - 1px),rgba(26,32,48,.9) calc(100%/24)); }}
  .th-bar{{ position:absolute; top:3px; height:16px; border-radius:4px; opacity:.92; }}
  .th-bar.asia{{ background:var(--bl); }}
  .th-bar.europe{{ background:var(--tq); }}
  .th-bar.americas{{ background:var(--or); }}
  .th-bar.bridge{{ background:linear-gradient(90deg,var(--bl),var(--tq)); }}
  .th-now{{ position:absolute; top:0; bottom:0; width:2px; background:#fff; box-shadow:0 0 7px rgba(255,255,255,.75); z-index:3; }}
  .th-legend{{ display:flex; gap:16px; flex-wrap:wrap; margin-top:12px; font-size:12px; color:var(--tx); }}
  .th-legend b{{ display:inline-block; width:11px; height:11px; border-radius:3px; margin-right:5px; vertical-align:-1px; }}
  @media(max-width:700px){{
    .th-row{{ grid-template-columns:88px 1fr; }}
    .th-axis{{ grid-template-columns:88px repeat(8,1fr); font-size:9px; }}
    .th-city{{ font-size:11.5px; }}
  }}

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
          <div class="sub" style="font-size:17px;color:var(--hdr);letter-spacing:1.5px;font-weight:700">The <i>NEW</i> XRP Intelligence Standard</div>
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
        <a href="https://xrpcompleteblog.com" target="_blank" rel="noopener" style="display:block;width:375px;height:70px">
          <img src="/blog_ad.png?v={APP_VERSION}" alt="XRP Complete Blog" style="display:block;width:375px;height:70px;object-fit:contain">
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

    _B['tradinghub'] = f"""    <!-- SECTION 31: GLOBAL TRADING HUB OVERLAP (V133) -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F310</span> Global Trading Hub Overlap</div>
      <div class="trk-tag" style="color:var(--tx)">Crypto never closes, so these are not exchange hours \u2014 they are the windows when each hub's desks are actually staffed (08:00\u201318:00 local). Where the windows stack is where depth concentrates and spreads tighten.</div>
      <div class="srow" style="margin:12px 0 14px">
        <div class="si"><span style="color:var(--tx);font-size:13px">Staffed right now</span><span style="color:var(--gr);font-weight:800;font-family:var(--mn)">{th_open} / {th_total}</span></div>
        <div class="si"><span style="color:var(--tx);font-size:13px">Peak overlap</span><span style="color:var(--or);font-weight:800;font-family:var(--mn)">{th_peak} UTC</span></div>
        <div class="si"><span style="color:var(--tx);font-size:13px">Hubs at peak</span><span style="color:var(--bl);font-weight:800;font-family:var(--mn)">{th_peak_n} / {th_total}</span></div>
      </div>
      <div class="th-axis">{th_axis}</div>
      {th_rows}
      <div class="th-legend">
        <span><b style="background:var(--bl)"></b>Asia\u2013Pacific</span>
        <span><b style="background:linear-gradient(90deg,var(--bl),var(--tq))"></b>Gulf bridge</span>
        <span><b style="background:var(--tq)"></b>Europe</span>
        <span><b style="background:var(--or)"></b>Americas</span>
        <span><b style="background:#fff"></b>Now ({th_utc} UTC)</span>
      </div>
      <div style="font-size:12px;color:var(--tx);margin-top:12px;line-height:1.7;border-top:1px solid var(--b);padding-top:10px">
        Bars run 08:00\u201318:00 local mapped onto one UTC day; a bar crossing midnight UTC is drawn in two pieces \u2014 the same window split by the date line, not two sessions.
        Dubai is shaded blue-to-turquoise because the Gulf sits between the Asian close and the European open, carrying flow that would otherwise fall into a gap.
        Offsets are read live from the time-zone database, so daylight saving in London, Zurich and New York is already accounted for.
        <strong style="color:var(--br)">Breadth, not volume:</strong> four of these eight hubs sit in Asia\u2013Pacific and only one in the Americas, so the widest overlap is not the heaviest flow \u2014 the later London\u2013New York window carries far more. Not financial advice.
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
      <div style="height:520px;border-radius:8px;overflow:hidden;border:1px solid var(--b)">
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
      <div class="am-panel" style="margin-top:10px">
        <div class="am-title" style="color:var(--tq)">\U0001F4A7 Liquidity Map</div>
        <div class="am-sub">Bid vs. ask value in the visible order book</div>
        {liq_html}
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

    _B['newsnav'] = f"""    <!-- SECTION 10b: NEWS -> MAIN QUICK MARKERS (V135) -->
    <div class="srow" style="margin:10px 0 14px">
      <a class="si nav-marker" href="/#brief">
        <span><span class="sic" style="font-size:17px">\U0001F4F0</span> <b style="color:var(--br)">Intelligence Brief</b><br><span style="font-size:12px;color:var(--tx)">4 editions daily on Main</span></span>
        <span style="color:var(--hdr);font-weight:800">&rarr;</span>
      </a>
      <a class="si nav-marker" href="/">
        <span><span class="sic" style="font-size:17px">\u26A1</span> <b style="color:var(--br)">Breaking News</b><br><span style="font-size:12px;color:var(--tx)">Live ticker at top of Main</span></span>
        <span style="color:var(--hdr);font-weight:800">&rarr;</span>
      </a>
      <a class="si nav-marker" href="/#newdeals">
        <span><span class="sic" style="font-size:17px">\U0001F91D</span> <b style="color:var(--br)">New Deals This Week</b><br><span style="font-size:12px;color:var(--tx)">Partnerships on Main</span></span>
        <span style="color:var(--hdr);font-weight:800">&rarr;</span>
      </a>
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
          {us_stats}
          <div class="intel-row"><b>Regulatory</b><br>{us_regulatory}</div>
          <div class="intel-row"><b>Institutional</b><br>{us_institutional}</div>
          <div class="intel-sub">Coverage breakdown</div>
          {us_bars}
          <div class="intel-sub">Latest US headlines</div>
          {us_heads}
          <div class="intel-foot">{us_srcline}</div>
        </div>
      </div>
      <div class="intel" style="border-color:rgba(72,255,130,.35)">
        <div class="intel-h">
          <span class="intel-t" style="color:var(--hdr)"><span class="sic">\U0001F310</span> Global Pulse</span>
          <span style="font-size:15px;font-family:var(--mn);color:var(--tx)">{gl_ts}</span>
        </div>
        <div class="intel-b">
          <div class="intel-pulse">{gl_pulse}</div>
          {gl_stats}
          <div class="intel-row"><b>Thesis</b><br>{gl_thesis}</div>
          <div class="sig-row">{gl_signals_html}</div>
          <div class="intel-sub">Stories by region</div>
          {gl_bars}
          <div class="intel-sub">Latest global headlines</div>
          {gl_heads}
          <div class="intel-foot">{gl_srcline}</div>
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

    _B['brief'] = f"""    <!-- SECTION 17: XRP INTELLIGENCE BRIEF (four editions daily — 06:00, 11:55, 18:00, 23:55 UTC) -->
    <div id="brief" class="acct" style="border-color:rgba(255,204,0,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr);margin-bottom:10px"><span class="sic">\U0001F52E</span> XRP Intelligence Brief</div>

      <div class="brf-teaser">
        <div class="brf-teaser-line">\U0001F52E Next Proprietary Briefing in <span id="brf-countdown">\u2014</span></div>
        <div class="brf-teaser-sub">Four editions daily \u2014 06:00 &bull; 11:55 &bull; 18:00 &bull; 23:55 UTC \u2014 see World Clocks below</div>
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
      <div class="brf-note">\u26A0\uFE0F Informational only \u2014 not financial advice. Editions publish at 06:00, 11:55, 18:00 and 23:55 UTC and are derived from the live news feed.</div>
    </div>
    <script type="application/json" id="brief-archive-data">{_archive_json}</script>

"""

    _B['clocks'] = f"""    <!-- SECTION 18: WORLD BRIEFING CLOCKS -->
    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">\U0001F310</span> World Briefing Clocks</div>
      <div class="trk-tag" style="color:var(--tx)">Local time across major crypto hubs, showing all four daily briefing editions (06:00 &bull; 11:55 &bull; 18:00 &bull; 23:55 UTC) in each city's own time \u2014 orange by day, gray by night.</div>
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
    <div id="regradar" class="acct" style="border-color:rgba(255,153,0,.35);margin:10px 0">
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

    _B['newdeals'] = f"""    <!-- SECTION 27b: NEW PARTNERSHIPS & DEALS \u2014 LAST 7 DAYS (V132) -->
    <div id="newdeals" class="acct" style="border-color:rgba(72,255,130,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--gr)"><span class="sic">\U0001F91D</span> New Partnerships &amp; Deals \u2014 This Week</div>
      <div class="trk-tag" style="color:var(--tx)">Only partnerships and traditional-finance deals detected in the last 7 days \u2014 {nd_count} currently listed. Updates automatically as the feed runs; entries older than a week roll into the <a href="/institutional" style="color:var(--hdr)">Global Partnership Directory</a>.</div>
      <div class="pl-list" style="margin-top:10px">
        {nd_html}
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

    _ORDER = {'main': ['status', 'liquidity', 'onchain', 'ecosystem', 'mainstream', 'tradfi', 'brief', 'clocks', 'competitive', 'regradar', 'clarity', 'newdeals', 'advmetrics', 'regledger'], 'markets': ['tradinghub', 'rsi', 'chart', 'analytics', 'longitudinal', 'practical', 'dca', 'hist30'], 'institutional': ['instpart', 'enterprise', 'execdev', 'exclusive'], 'news': ['newsnav', 'top20', 'usintel', 'regdisc', 'heatmap', 'nmv', 'newsfeed', 'sentiment'], 'community': ['scoreboard', 'leaderboard', 'unique', 'community'], 'regulatory': ['regnew']}

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
