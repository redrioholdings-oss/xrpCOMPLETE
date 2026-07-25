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
APP_VERSION = "127"

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

# BLOG AD (V123) - header advertisement for XRP Complete Blog, replacing the
# old BLOG button. 320x320 PNG (preserves rounded-corner transparency),
# downscaled from the source graphic. Served at /blog_ad.png.
BLOG_AD_B64 = (
    "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"
    "L31McBZZ6WqF091oupuKc4t1IZVq76kmLnvvm0DjvHPWe19Ipb4ghPy7QskN79w34yWR/7Yg+G8LgBqwWZZdS5L0/+bhfyuEyKVU"
    "1nsvvPdKKtWGt4DRhKUSTqyMQSt8lUKhlKaK6bqUOpw0JMY6QoIhYiEmQMhwM6NAKKyJWJMT4EXMniIkKRRaJXgvEEIDsg2eHhFL"
    "q0U52uAozjWPhzLDO98uWh9LYaVku4O15Wtb1nZ3SvnIkgnCzRcWpMd7h9YqLhaWMhil1MqGEfE4mkUvl4JImxU3N5ZSiO619iyV"
    "E00ga8rNZYjALm7e+DytVXyN1WyoE7Ti4mizVSmXFkv3990NosEGmyy8e8ymrnjuE5/Aezg+PubTn3qeDz/+CGtsG7xVPM9NyShW"
    "MpU24MDShtrdRBblX5MJ+vjRY8YU36sLnbSLUoZF2cILTdm5kom3ZXdnpzHW8uyTTzDYv8zGF/4mW5t7XNlJyNOEuw+OmM1mbdBY"
    "4MLhujnncDGLbsr35YyTdlPqZn7d5zQBvDnmUJG5mEj4uI6WK5puhbGMh3qUVAs8VixDPqqBJ/wioD+Mh3uk1C10Z7xD0mC+Ea7o"
    "wBcixpp4PYT3XoYv3gGFQHxZanXBWfsqcNLBBv+dA6AGTJZlj4H8IyHFV73zJta2UgopRAN8e1AqCbiM0iiZ4B0oqcELPAovVAw0"
    "miTJ8CIENe8lQiYImYTfSQ1CY71AqRSExkuFQyJ1+FnIBJnkOCRa53gUKAkyvI8FEAqhUoTUeJHgfXgsvIZC64xEZ9Q2BGIhdVjo"
    "QiKQEaqL37v4vVQxkMsQOGMWJyIW5r1FSdUpFx9xoWOGsopLrmzDy5hM3F0vnDtkOpu1uFf3hpZLeIroBIDwGdI0XSpjVwNFm+08"
    "9NhyVtO96dsSttOIagLMKnYkV6CQZmE0GfXSzm8t6+vrPP/889y6dYu33nyDa089z6c/+QyvvvJqW0rxU4D07rnzzmGdZzDoo5Si"
    "nM8Xn3dpQREbQg2w4Nvg3AL5zoFYBDlvLb7bxBIC0Sz0zjlrSlc6maHWms99+hPU69eQa1fxvQP6F5/i3GbGwUbCaDTh6OiELE2X"
    "8dwmpWmy5xXoY3Hsi2ZNiznGDXZpo2ixt5gkNLijTpZK+xAwlzPtpkpwsWHZNoMi5tfd2Ftop21GrlZRi6oLQEnVls7d6+ni6y7B"
    "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"
    "eOeD23zhycu8ces+H793wifOPc9f/TXHv/iXvwcRu1qibcRFFLkyi4ZBg5Gx8BtsgqRdBdc7G64XC9OPbvnW6pqNYbC+yfbOBrO1"
    "S9w/k6wlUw53NzkzhgcnE+466OeSXT+HPGdSzrl3VpNvHHK46RnPLTePZnzuqV1unZWcjSo21wvszFLdf4/3332L2ayk6BUL5YR3"
    "7XE0DamWTxcTFOsDpGKNaUt+JSWmqsizjLKug32dlOgkab9vFEXd5kcbkDoyxLar2+FIrurcG9pVN3MO7j++LWWb4OsfQetZ1ZJr"
    "FaSxVVW31DHjl0wu4iUXn02S5HGdb27/PXTqtEicTDIt0xwVKS2oyK3T4auIIDPR8kbIQMYVAowDL3Rg/EeMTuo8UGdIkSpHSBVv"
    "JokQwRUmlCsyUFaEpiG5hW5iyDwFui2/Gy2hd11FQtDhOh8BbxEzLCxKWMq6jk2PClwdGhTO4N0ca8Z4b0JgETXO1qH0dRbfBEtv"
    "WyODULo2WJprS2rpQ7nqYyPDe4u3MZts5UoWa2Ig8448i4HO2pBFxsAHLgbOcAzeuVjKmva5OIfExpLYIOLnDFzBEDjxHmdN4Cb6"
    "GPysQcim4eHwVlNkin6Rc+/+cczcPa1tQNNNlQ0I7toFJaUi1Zp5VT1s0uA9Ml6rrv9i11EF73nm2ec4OT3l5OQYqRSXP/HzVHXF"
    "YHcfTM1rb9+k97nn+I2v9fmH/+gf8em/8vfRacpk8oCjyRZf/eKnGD+4ycnYUyjL99884etf+UX+qhf8zu9+o81Kus4s3QaQXCnF"
    "Gk/IAM26tlPdLdMW+POCN9l15Olmj9bUXLxwHi9yxOZV9jc1Z6OUm0cTrl/ZI1Xw7r0Rm9sD0kSz1k/pj97ltL9F0su5c+8B585v"
    "c26tx+m4oqod53Yzbt2doPMe+fxj7ty6E6zPYvkZ7MZUKyHDQ5YmEdpxUSbp2+trY/bWZnjRsKFLjjZVhZCy9Tt8lOlHc34aY1jv"
    "HHUsubsY4xIe65aNf7sZ4VKzrNOsWs5GFzxZKWRosIhleVyD6bccQueMB+ng72mR5KVO+lJr5UiC/EunWSAfJwUq0kWULhAqi7y4"
    "XvhZ5wjZDzw8oVonFqRCeA1kIJIWU3LOEYRpoTuJtyE6N3idCF3MkKzZ+DwDVBHY9x2MrcsCb7zeAgAqG0kMEiMVUiQBO5DrQTqH"
    "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"
    "a8Gr6dJYlrNP353f8lMHSkXF2OqQpq76pDPI6lHNq2Z41GrGqp549lMvTuc1s/nC3HA2N4xnJc5aqtpgzIL8mSiJ0oqsyFjr52yv"
    "9+n1c0ztUDqUNFoFgqRWkjRNQqfKOmprsLbhAYXAleWaNElYK1KUFGRasrleUBuPVoKtQU6vyBnkCRv9gn4voyprJtM583nNdFZR"
    "lSVVZTDWkqUJRZqwt9lns5exv7NJUSRIIRj0cqraMJuXjCaz1vliNJkxKw1pmnBpfwMtFZNZSZYIpvOKubHMqorhZEqmE1Idboiy"
    "NlhryFIdeJAS0kSys96jlwU50M5agbUehKGfKhLl2einaOHItAwNpkSihGM4meOsoZ9Jeiko6QOFyFZ4U+JdiRbByqvpknsTsUMb"
    "8EMbA6J1FdaWITusy4g3hg6zq5pgWOHsHO9m2PIMW42x1RxEnyS/SNG/RlJsI5UAWUVvyAyt8pjpaWQzR7nJBGXgPjajVIkmuSo+"
    "FsmlYWiUVAHDjRSZ4AW5CIYBM0q58fEH3Llzm69+9Ze5cuUqP/z273H3xntceOpzOGc5enCETgSb633GZ3NIJNV4xGBQMJU9VD2n"
    "nBwznis29q4gJNx/MOTJpy5y7/Yxeb9HpuCdj8649sTTXDsseP31N9FahzKs4/SyOnhnwTGVpHnOJ597mnrnGQ4+8TMU5oRC5JAp"
    "9jZ73L4/Y1wa9jd7GGe4d+qpb/6IfGsfm2xyclayu91ncz1nPJ5zMi7Zvv4cadFj+M7LDMw93nr1L3j33XfDaIpYnns8aZKGymtF"
    "odEOe+/YdXUlfauyMa1U6xbTtffqDko31raZ1kNcvIXbSqDRxHlAgbKywOZUJ1B3DRiWZji74GWZpA1ctQjSXTrMo0rx1QHtbuWY"
    "mtdSP/szX3hxVhnKuo6SLsXGWsH+3ib72+s8ffU8z1w7x7XzO1y/sMfVi/sBHyxyLu5vcPFgm/M7m5QulJZ5qukPemR5SpZm0SFC"
    "B/BTLoZJFzFQ1TYUQEkSHFmmlY2BTPHgbMqstuSJRkhBkaWUxjKeV8zmpt0CjA1/4zxMyyDZsvFkr/VyNvs553Y22FrrcXF/i+2N"
    "AWu9lL2NNZRUjCZzpvOSB2djPHCw3WdnY4AUijsnY9766C53T0YMpxWj2RyPQCsoipRUJyghyJTCeUceHa4Fnv2NHr08Zb2n6aWa"
    "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"
    "8YIWXmuLh19+obtEJfA7Q6RpkGYZJROUglxTl9I5jx4/5v2vf4s8i/ni889xfY+NTc0fTFOdi2JZFhfn50ghuLK7y9jcpTXYJFrM"
    "uX1jlzzNsT2HzNDyxHYQEEY5jmfTsnKiecxZ5jJOurQ2b2oSfTLCWz5lefoChMksFFidHaLzZ1hFihFsEyYJpi05Op3i+TZJFHFj"
    "r4swTTrdLkjdCESYSKXY3XQ4PF5ieC1ezls4m3fYuP4eb3/1HR7cvAJCcHJ0XLtTv86QtHJ4KcptccWgeF2A+loW8KVFRjUl0Hjs"
    "ZhCS7i7VmmlwbdX/K7/21z+wTGtlVCkleaa5YLKRDawJh6JuJSutnrjkeFIJmmTDzWHdx6uhJSzvVCmqUHK1ClyXooxjNOrw7qyo"
    "3O80r8w2JI5t64JomNi2qUPay8czTEPjgIYEpS3iDcuoMwps2155okEdAC9KWo9pGZiWydbmkP39A0zbJnBtTk/PcF1fF7Qi5XQa"
    "kxQSUZ8/6ieGtOju0ChFG6rMAbHY7AfM5iHTaYxtm4RpxmSyIAlT8irD1DCwHYs8gyhKSDNFnuuttevZFEqQpdonTommU/UqaF5K"
    "o5Th5XVoVHXxrS4ecF2bNC/wHRPXtYnTjE7bASWQpqGdTNKC5SLEME06LYcXRxNaLVf7MQpFu+UzaHtEYcqf+/YDvnxxSpYrFmHM"
    "X/7+u2wN2pyeXTAZj+sLudVqkZZSueY/1cHb6/XwPI+joyOmU73s2Njo02p3+NEP/pCvv92i3Rky7HgoYdD3JfPYxHa6zBYRYd7n"
    "5eE53ZZBp+XRbftkaV76Kqo1E2K95Ktci2W5OTcwDIFpWnSH1/nyi88JY+2yY7obKGnS7nRYLhZkSminmwJ2B22ePHrIaLpkeOU+"
    "9+/f5vD5U168eE6/P6Tb6RKVj3Nxfo5hGOzs7VC0rmD4m4ynEbZrMZ5N6ZTqGNPxGPQ8pnGB6Xu0bQtTmNovMInwfcnp1CJzt5Dt"
    "LUDSEecY40dE0xH5fMIizQl27zGbTOi2HVQY43gmo7kOsFrMU4Rp8rV7Q4Zdh8SQTJOcjUGHySxh0HegSIliGIeK0LmC29kgSI95"
    "8XK/vKeL1ya5Vddbs1NUamVzVTQ8/bhkzHqZ0FzVGcuyXuEMNn0Rm/igUgrjN3/rtz/QwdZa36l5VqLO5qx/yDB09KGgLH5lPVXV"
    "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"
    "jNOffziXXXkzy5/cSC6XSUGwWnOxLZOG69HdVeSqn3yYYj7LT393A5Zp8ILjD0Yrxa33rOAr3/8jq9dv5a2vP5VzX3YcWzZsxXEs"
    "rv7ZR7n013/jA5/9GXssnMUbX30KRx68B53FLMOjZa7/x0Nc+uvrm56WlKlXlwCEGX/Pro4cl37prey5eDY/v+JGPvrFX2IYku7O"
    "Au954+kcefBSLMvkrzfdz3ipxhvOPoGG63P2m7/IilWbmDW9jzef+4Idj/+r69k6NMY5LzmGL330tWwZGOXSX1/Pcw9fxrKlc6lU"
    "6vziD7fw08tvwHEsGq7HtP5u3vr6Uzn8gCXkchm2DY1x5TV3ctkVN2GaBp4X8PLTnsPZLz6a2TP68P2Qx5/cyHd/dg33P7qGfC4C"
    "QUHkIZ1z+jF0duRZtXaAb//0ahzH4qJzX8C8+TN49ZnH8sjK9XznM2+kVncpV+u89fUv5KzTjuKlF3ye4bEyLzv1SF5/9gn093ay"
    "ZesIl//5dl5+2lEcsPcCfvCLa3nPR3/A1z/7Zs59+fO496FV/PHauzjzhUcyra+LrUPjfPPHf+H6Wx4kn89SqdY48ej9uei1z2fm"
    "tF5Gxsr8/Mqb0Tryag1DECqFISUfeMtLef7zDiSfzXDXA0/wwKNreOOrT6a7o8AF7/s219/6EL/93n+x9x5z+Nlvb+TBx9byjjec"
    "xoUf/C73P7yak445gLe87lTmzuqnVKrxsytuRCKQhhEpovN/HgAjd/y2e5bTaHh0deZ574Wnk8nYrFo3wOVX3UouazNv9hRMIwqX"
    "X3nGsfT3dOC6PkEY8vqzjifjWLz1w9+no5jjW59+IycdcwC+H1BvuMye0cfB+y1i6cJZXPiB7+yYc5MChCQIQvZYNJO3n3cab/7g"
    "dyPKhRRpzi4JV0zToOF63PvwKnw/CgUq1QYNz+ehx9bynEP2YtHc6VimwdIFM5nW18XQSAkhBAvmTmVqfxedHXn6ezrxg5D7Hlk9"
    "KTeigXwuwyU/+CNHHrwHi+fP4DP/9Wosy6Dh+nzl+39kZLQU52AiYHZsi3seepLLf/N3MCV7LZrFHotm0d2ZJ1/IopTCNAw8P+TK"
    "a+5gwyNrMAzJcUfujW1b9HRHc4Nb37it310IQVdHHkNKzjv7RLpjzygMQ97wihMo5DK8+q2X4FgWGcemVKlhCEGxkMM0JB2FHN/7"
    "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"
    "6rBv4zoaAxZzMgne9uVzWCTH1slOYppFp1+902aGiCh2JVutCkmPpXPV+Fl8v6md97qSXLpoCjukOugXKrKqEOWdrsYKsXnX+tYN"
    "928bQNH1vI9pte0MDefoMEO8293ADjXtjIwWWZKL8HLHAALCpeSqTEl2MTHWg644rCnG+KC7vjLWeUejTvfWZEOwSMHWmZVJsSSf"
    "2CSB+79SAZZ3vJzPXA8osg+zPmd7VQS9P3ekIO9olXrhgOIihMRyFUquWjkcIKQ4BBVnk/WtOVvHlt5uX66VtXx3TEqIal5tLEDR"
    "VSk5CqrwLJ9ylrDkqBiuWlGqYdWpuJllJWK7CsVezxRQ3M+VmxV6VUrE/fYrtcC2DkgCitungiDnaNiud6WXzRPkba8WOKLaBBQX"
    "y1XIOxqu38+oapN1dN9F3Xzdbe95MVyFgqOiCIj2isMVHA3Tr2CI9bKiyxU2IdXrZ3leyi6tlwH2LLfeJVWGq2C4Ko4/9iqSrK2B"
    "8OfYtwJdf+4df+7LG4niK6+SPx+qX7lTno9K5UKvygS9V5203KjPRccby5gf7M/Y5Zptr1/4lSUFx3+PimZ/jtir+AT1kqNUeKhB"
    "1an0XfjJKMNV0HodRiD9MEZZPiOqg0BWKCjl/oaVvvK2sQLcv6mdGd1xfjlvWzK2VolnR3olkza+f5krW5bJslwbrorpr8/eNekl"
    "V8V0lQqFLbxRddbG8h9UHEKbWZP/tQqwPHFlId3UqSe9Py8rINErBtP7895xKvkv3G9z7W7utBJBX6rEpu638TNtyt3sXUXgbFTK"
    "p3zBuPSOT/U+Dab8HJv6/b96/NGm2v2iMfmicf3icfKrMXq1t6n79p0j+iS1vmw+yrWr4ktc/97t9H6WL+rX5mTty/r+fz2OZQV4"
    "pa8AP+6Oc+78bbzY8ybkaHP37y2TZbkRm/l97/GUmxjzvs8Mkv/yWuDNJUH+2c/lv/j5v9uuu1ECoDflxJFfHt/8smfaXBxE/gvj"
    "InslQb7o95vryxc9v/0vjMn/dl42NZb2v9jWl81HeYF+eZ8/387/vl9ffM3/9Tj2jpMHFSqx7I2TNV92/00lI/8V2f3fPPN/tQVY"
    "RRX/v4Rj4Osv1P93nt+Rgn6hIgnNpuAoNJciVBf6/+cW4H8CZXaZ5D9ThP2fvt9/s9Iqv1xH/pvtmFKiCoH6/4kSLPcNPBL8P3Od"
    "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"
    "0UaiISrs/TJdQu9VRmZIt0J0LVt+G9OJCtKrEuh9v7CioCMq1QM2kpLroooNY6H1+j4oFAzp+lUzoH+BFSj9BFXZSioX+JvSxam4"
    "JqKSbCnHMMvPW3ZRo72qLiz/t6r/rGXX0/aTL0F/k1GAgl+ds3F/tXJSzb+unABxgKIvW/ghDQ0/9ibdynN68iYI+lU0m2ItFFzX"
    "f4Wm1w9HenJQjvEKRJ+qn3Kdb7lKR/QiLveWSTa6Tu/F2ctLx6c/bZDRqF/La0iXI2P9GaqHWWkVeTzfTKttsHu4jjsbtiCl6tyU"
    "Xs4felYSFRqGP0MhoX4rEiHfmvMAe598QiW7KiqKr/d15UUjv+Cz8mIruzabO45oU9f0PuFD6bXo5Sb+3hzHcUObm+7H5+8rKwrl"
    "833b8L38X96vdztsdL3s9an4kr5tin/lbjQP/C/move9xUbXys2MXe9Rkr3G74vG8PPPKzbZzj8no+Vj+uVm+/35vm24z8bj8K/K"
    "sYqgx7U4IzmMq+vG0uVYzDJ6aHEMtvBd4qJ0OKZtFovMPOFem3+1EuT/w5jg54/okZu8Tv4Tn208yZsT6y+7xv2Sv7+8zU33Y3P3"
    "3XTf5L99v77tbPp+/4zi+6Jx+KLff9k4901qfdmcbF5O5L8whp//XP6LMir/qV9unLDb8G/5b8mxiySmaNybXUNS0Tgi1p/tQjWE"
    "/MqnNsfkhvQyFpherM/5Fh6oVj0Ruooq/otRtkBL0mWiHmdCIEZU0ci5NjOMtJeJ3+jAjm8TtKoIVFHFfy+k7yJHhcYCK8dsM4P0"
    "q5NCQiUqtG+Nu1tVgFVUUcVmXfmwf4zZhqof+a1WflUFWEUVVVSwoXD0vwdKddqrqKKK/1ZUFWAVVVRRVYBVVFFFFVUFWEUVVVRR"
    "VYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRR"
    "VYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRR"
    "VYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVRRVYBVVFFFFVUFWEUVVVQVYBVVVFFFVQFWUUUVVVQVYBVVVFHFfwO0r10DKwog"
    "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"
    "gxRxAAAAAElFTkSuQmCC"
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
          <img src="/blog_ad.png" alt="XRP Complete Blog" style="display:block;width:250px;height:70px;object-fit:contain">
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
