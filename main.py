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
from flask import Flask, Response, jsonify, abort

# ─────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────────────
APP_VERSION = "149"

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
    "exsq30dI+v8AW2m+vX+oHalRI5b/AKo38kmaigN5VpQF1L/h9GMoFl5hrbYbg7R04NRM/SnG76T7hCQQ9Bc+0Za09Z6kDrOm3+sE"
    "IC7/AIinWEbJ5FrPUvQS25YgRBDO+ia+koZPQPWIAfx5nSywWvU+iFiPJDRHhziA2NrZE6SrDlv0mvNG1Kro0Gz+/IwJH3NHtLjW"
    "OPOrgmEZ7glYM9wlfb1SybMwk3soy9cm5R7aRRw3h7IpMNaTEt1HclGQwlrLX8ISxeXjIRnCkaTxNUYL5n4mgQVuMBOSBCtHb2m+"
    "gx0Pr1IQMwVPce8pRfBo95WPUFkrXT2Z8xNHrFn8vDrKwlpFB1IOSCzVUBh0B6Dz/fiL7oUwTMMWCssFLWInXUHD38XYx7xGoX+k"
    "xgtPZZULq9ZalhYw5j+VNqZWuqr1WPv4sA0flWXMAlOSnEqDvgTRtv7VCFB2L8n6l2K79fjMSlWoKfAY0ihZ30gLR3MmWAVbzDJC"
    "LcadvEJocr8xSMJuyvPRg50lNeeyxzUDkli47me+ZQw82MsFza/gf3DnbP7AzvpmP3+uogUe8uzMwqtYLv2bxLkUR2WJHVD7kV9m"
    "+30cv1TEwhvJlKoT6LIIEr1ph2sK8g7MpunUkYrnqfjEvFuPzD9RB43OgveX/P0an/CX4qU3qbU+0VHWiES0Ln1jXRQ1YcS8M654"
    "GbZcjKEOiIALf6sSkL3dTGXDlWRGw33iOZGLFurKTJeXuwV+fFrIFBmcCWWmpQxra51EcugjYf7VBrX136lryPk9mKV1pg9/Bfum"
    "GEVRuNj8S6wGi7rp9F8DVcQ2v74fGJNeA+yWKyrkMNiIV/cGKavjCYI2dJRIXrBOmYgOW9d8TIMNKRLD+RQYkKzdVe8Zqfbv8Ypc"
    "G3aaR3c3NEXtj9fHcL7VC1HITRWn0mYAdJp+kc7NIkSvsrNunRHFIcu4iW3ElFkejccwfZguuC7Gh1hKo7VULxKCBkTK23YNjyaT"
    "NVu5xHGw4g0EwhTbWZEvtezGCN47y3XHar8SzANmLX2NldvD4HK8RihK5biVFufcSRxLuTW+StRVjCf9uuBWQWY4ZII0obcQjP2Z"
    "QWO43Ld4H8AxSZ1M9f1LSxTar9JDgAy4msBo+evl1tE+YVavnTfHH0q5q9snR5J2SiMDvKENvfgiK8OpX7Yiqqq2vM0wVQ/CPLOf"
    "midRPmUrRiOLIMSrtjsA5Nnr+kwzRjBVPwQYk1ZUExrwijeb/PBkBokASPGj1eIWXQx0/m8uVR0dD6FxKi5y/OxStNp/wFMU1NHr"
    "CgTVWq9f1FCW3fosi28S1ltNVS5MZLXfbrGQImo+eaDWIYP7lHOhuL9xkTbMIR1YVpJ9EK6JrbNXRlESX9q9Y6FaQyebqoMppuLK"
    "BmGHcZl1f0c+grV4l66ffGLacRDoGt0I7A6RcpLCO/eCDX+n5jqW0hk8sJDT7rCgd6hwjstYstVH2iOuo/LZlFfdh9VXBIInpIxo"
    "LNEAy2uI+AODZEQKTCeUQRJ9Yv5+Y8ldq7xhVqZZarJ/5yh7rBWp6Y3XessWJ0RWpNoNSqZOGD9YVOVEmw4mpQ0WV5LQy+hO3rpL"
    "/SKeg/SMoqdroTWkd6la6SLmznn8iZ0buvxKPP0nduSRoh4OUisVAE72JhbXzRISPQzTyD7ku2X9zLNxQi8xvoQUE9x79kFoHoEV"
    "3RbvhNzR/W+n6GAw6XA4hRMaJXgRb93SfFce4eDlmJhhTQMYUxKmrPu5jPnQ3Y9ZKkNb0KuqsBY3XfyFtfvCZjPJ6Fhbq7SqAljK"
    "VLQjbY+K8sAXvmLZizIEvMpqvp04oLlNhO9X5mQG7j4mqfuAfeEZ5Rv8g/ddbjqB6Rq/PGcp37DGazZy22MPqll28OH4Sl1jX9Cc"
    "xmIbK2mM0l27/KPYNUzXC7YmonqlfMo2vW4zRuxNIv1jdA9IwDnLG8AqNGKNrxXKklp2a+BgdSiurQH08CCNF3YbT2kt0v61NCD5"
    "m5DtiagPfwovbxBVDSCDUtFWUdtH7+BAAJVdIMFFxMQqYE3WPLyy9BVtLnBprP8A2If60rPDZen/ABjWk/8AWn/rT/3Ip1X/AKv/"
    "2gAMAwEAAgADAAAAEPN+PPPPPM/PPPOOfPPNvAYfPPLhn2cjngjfPPP1hOCoYTnPPPPL658tTxOPPPPPDN60/vPPPPPPIaqAWvPP"
    "PNPMXR5/+97PPPLBL+QAd+F7PPJsBKexXgwXPPLVGtM7Al9/PLAWbv8AiLmanzzwavL9h5QsHzzy5hNOKdau7zzzz1FRXyRfzzzz"
    "z9uJjN8/zzzzzzwb2zTzzzzzxzChaaHfzzzzw0htrv2nzzzz+ej6Uf8A/d888LSSRJvsvG88/lpM7R98pIX8vwR88888hU988888"
    "88888888/8QAKBEBAAECAwgDAQEBAAAAAAAAAQARMSFh8CBBUXGBobHRkcHhEDDx/9oACAEDAQE/EJTOHgsoLLwHadoESoFdinxh"
    "r6lX7Vp84bF1Ul9deJXOPXiYNwq9qfewihVxdN/vpMQLmCjMGNHfLPFrrC5X5/52lio7Q0RpXdXrESqe/A5GwglGV8cT06RCPeBX"
    "5wmClXl7hShhy87iMwdXfllCPqDjLLBssOk8HjFQ4ncjwCQ30vCkqHP6KRehHL3v5zAjFWInNbLLboK5O8gkEG8u5Bx48M46h8jz"
    "YHGqgOvU+DI9/wCAVXHXbP4lUUVNQ1ovKBPSEk6/T73+do94Nf8Af2XKLMaZ49spSQ4fjEGeKWeZuYrLnKcuO7PXc2QR7o+kIIvu"
    "hYFG8w7W8SpVEdzrxE1T+T33iJGYeoMsTxCA7DUjfrXOJuhYSuLXj+Q+rq+T33mE9TLH97SmJrXKLSvg69VlJDVMOkrCtax+NitH"
    "DX1F0cRrjlF2Tl++4TX5dUgiVJa2vGz8zt69j1BNQoU8zn7XvYNAcu8ZWqd5Wn5PZ6jFFplj4x7SoCnbXWLQY9ZepgC07/vaJAuH"
    "3HUM9jg6O5+QSDZj8KDrV4bXRztMPQ6MxBrycO8qgCdH1EIXF5TcthE8YdN3WU6lE7xEF7CbnH3H6J7PrvClWnGle5MBHXP3K6C+"
    "HPLf1ylaqcYiljZy2agX3PT5lHJHt8QQ7n7WU+E18/Uegc0JbMBgHA1eBq4C/rrDQUDZQHUY1c8efuCEg8TLUXmGBK+sLG4gaAUF"
    "DbftkxGPY5HHxCk3WVj1S+WuO6FBw2zkO3oNafjiqwEdAOcV6KKv+xaNGZ9nxBEqbT1jnrPxznClKlGXSur3F6mZRBsPYkvvE1Xl"
    "x4XtbYJt6OlbmUAxHC8QUenQi7OmdfEF0qeVfqhD9QTupEZ4kGpc1Tp4psYNt5QIVlJvsbQ++NPFJwSvL7lv11lWI+MOX3+RMtKO"
    "BudfkAAs/wAAKxKuKsxm9DqKS435grv5S3sfrgLzBxCFvAw14/mJNKifMpJty/Zadx4bR4Qq1t+zVP2b/bKlP9v/xAAoEQEAAQEG"
    "BgMBAQEAAAAAAAABABEhMUFRYfAgcYGhsdGRweHxEDD/2gAIAQIBAT8Qlc5MwlRYM04jawDqKcFfIO/uU7vpX4t4LhVl2m/MomXf"
    "mWtnQ71+uAzShY64eussJuERC2rK5S92N9I3XPj+95eFXeIotdadIKUTwtebwCjUlBWR7dYQHAWn3LVanP1HtXMKRiwlpoYa6xj7"
    "hyl6Q8JTrGZlDy2PZgtoFwrdENgjT3WF1Z0fWHKWmwF7lB5Ka68dVPMwYqFVg3Gq5ZZ6Q1X4DkRGtBHFOh8ur6/4PUbPH7p8yiKA"
    "ii723SgTrFQdPs9Yca4A3/PyXFAlje8+iV9C5/pAumK3nLM0gvXKVYbMd7pwoRxhTCjqMsxj7QrBt73+ZQqqMTfmCgj8PrtBZaD7"
    "jS8PmMj4CrWG98oO5HSALCmX7fE6Gj4fXaW30dbPzvKwG984Qa6037pKySg29cu8oIN7s+XgpTnv7haWiUs1gS0Gv56jNPh3WIjR"
    "l+oZXnxO9r0fcQ1SrXxA02/NOC0xr2hJra9rpTD4PT7hFU62ebO8oAr330gFbu9fcuAr2/O8rSM/qGiuXBn6uz+xqBeQ9tBvd0dp"
    "v8yvmXUljEOpb2lIQ3qe4DW43e5Vdd/fAQ0j1x6SvRqPaBkHcHEs9QuqO577RBRjzp2Za6N8qeIwput5a+tZSoCyELWXufDTK+p7"
    "PEVqBOVvzEF2dKMrbbv4+4NQaC/ykvi1Wrm7uialquPvpHSVXhAPRINdefL1KIYqV10Q5La9JT95vcWPrSHSVXjPl6Gwjjm89PMa"
    "zcEonoN2u8sY0W3jeQTOq3s+cgSpg24coHqqC78gVbNH6ejERo8R0Dkby88pny2QJcAdHqA1d1gJeHcMulY7pzyzuvv4ELBv+9oY"
    "0uEqTYc7pUVOvVgb3bSkQVoOdPurH9BBjWADsYtG53Xr5rwHW3+G6Ra0mWiy+P1Qr5rLGtTn9Ev3TetIJ2Sa78wcFaEjib/YiVef"
    "4iAgFgKSwYI5UCXPfERcmUJfLBaWo8RLBiYQ278/5YRWiPxKy7+v5LwxmfEloKFL/wAm6/kwdta1/wC3/8QAKRABAAIBAgYBBAMB"
    "AQAAAAAAAQARITFBUWFxgZGhsSAwwfAQ0eHxQP/aAAgBAQABPxD/ANLpV2Al1lebKa1cm+hen98MILURZVidPt1d1Ouw6pcBkmK0"
    "JhfyQE8LCIOImH6mxoPXFoPhg9FEbwsbvrGFbK7gD5ftucbF5svQipHGsQynbuyfUUyuoF8CxWBZfaMrHiPbhoa0qHhvt9YAFXQJ"
    "s8Z7OK9ws2rWo8rHRw9Tfb+JR+JpcKaABjSLcPSzr57Su/Ko+R9bWcDkfKEC0eJxSoWBE8MKVspXM7hUCsGgLWK7OD40D3DFprYE"
    "QICNA8W/iEG6AieymfSaP+aX7l+ezSCUKd9bYxjUuBTXsFsbND6IVLOsLSBoajZfEcVcs4Ih4r6ynjvdg08h1CEGbCgR0wlSyHI4"
    "sJhwAMHFoDV7yvV0J/IL9wA6NUiZT65Fj8icV8XcaaT4m7tEeRI0H4i2ODuileWPw25r6g/KNK27nEUch4y5yxqkZUopg7c9zTv9"
    "gMDw6g2ME2xd0dHS8nJIhQD1BMgS9AlH5qyeGC8aM8JvYoqQlS7xUjd61S33OewOeAwLf+QHePqK3Gv7uc4MUgCDyoLnrKWIJoSg"
    "DhRLXGId+pGf0CUei0uAPteq+y6PT62+wcS88SyFgpRsJkp3/qDYi1msAlg82XZ0Q/Eqt60qPQB7j0s1Vfl7m32io809Spv4Dp2A"
    "hso9zM5aDpxh8Gqwc9dV1S8/jSIZckq9y+byl5lKrOi9HR5cPt1SkputvebTh0l6Ig1N+cbWO1oK6S6JbAinWhR2I8qBwgTu5iao"
    "2SvwReQxV/govgh60Qdr7hdzuHlpoJxZeNyu4Fp0jnOqVbPH7RnhE52rgNhwAwH2zEoCvDW2gnwxUW1WDfpGxa82Wyje4XdfI4Zh"
    "RplMnQPQ+4sMQ9h2txcuxvK5NegnL8rLLVlfOL0pLVcQ9IcnXaA3vY33xErN8L/qWq/yFtfaFERpJb8QrPV5RFU7SxuZxV7A4mg5"
    "sAHQ5AMlure7tUq7TuG6ruy9FWQMJWql4uYBy7AbvLzAzqmtweLxW7/4GtPhVHiHd9G8T3NbVxbj0TX8cqDVbdZgwmZmFc2RgNz0"
    "xuxleMMYuAfn/wAGtCg0jd+XV24w5CAGqNgNCEVwSy01vKnD4sWL8s1HXXanP+o8ud4ByrgbJNEdA1WgT50++W+jg+QPQ+EDoXTx"
    "YaL/AFBA4G20EgDNuJqkhVYmPNrbeKcI65ewsTrFVnmGimoWJuvWOvexyp/edt/uuCaaR8ouvFxxleCsFgxuDf4ijO8EIAZuB2pR"
    "X7cAMtEkeLs+Ilq9HD76vUwb+ZDqseJS6Ou64JsysopM01GJMNfh8XXzFeccZv38uD2/kw2l8voaxj6Kg+paG6X2DztAj8gVor5n"
    "DzGozneJgAF5jhkKhar93mjCA9UdI+P/AB6GPaJN5QVGE8THLegj5ta6MqTG7y9dUCfTWEqzdHOZxevAPwj4SKPYsNzR5NH7JvQD"
    "WpaA5xjKkGQYtwDDu7xzslMrOc26hVdHSB6hrvJXz4uNzylgPMYKIjSRsGfvOTtLIaXs8hrK6M2rPX/ENCx2wgLShs3G5LbbB/U/"
    "MQYJuoTU8HR7cIMiDKWUj3/lqinO/wBIWuSC+dNfEvzI60DYOQYjKFjR9dWFzumz5jYB704l8kwE7AZ9xqoyfEHJ3GPP+uDR5m3O"
    "ExvIlJBxoqm1ddYr9utsDFn+bA13Hi4MniHGEwnuDAMr0Z6j9ZAOar0XfdAeI3bGPerYgaFkZ/1+CBhFs/JGf+scNT3AXf47kQFv"
    "MxEWFKFQ7wbJygR4ut4Ifsl31HXh7MQ6NLF2ZSCCjbcHkk1mny3Jk6jZ2iCsko81HqomoxjkjrVd4k95GomEjVtFGx9IGSgcC2+D"
    "CFihtMKOxOOl1kG5C31HKcqPAdiv5LkWihJWV3pPZ+Yt3czpBnU2goUiufKSjWisb0tQ9I9AZAeiaHuImMorGhMiJdNaxHgNE3x/"
    "kYwCvZyeLg6jqjFWnoo+oLsLnYTvZYrPatrzjHCUcpVu6mnxFYE3r4sfUToGoVuppFjGYU9GkCOMqvzrFXXCOPMWrs4vB28wkirB"
    "mBLalbQR19WS9F9TBlBXks+I2VYVDdgW2t0ErGwLLF15K18bwe5HTrIz+SDdRYHiweJrYiQOzK/lKFImiQcNdI/Eu9tvKBdTRuhv"
    "jiXC7OLEmY04IH2H01i4orTKbVFioBGQDqyquIv5ByPWE2t+kwIepAhheeTSRMK3CV01xRDouTsxHIwGi+Wuka2Ci7PB4YpQm5F0"
    "0Pn+bj7mnGsttQvagIgb7IhrULfG36hvurio/MS3WE5TSfCaMCzjgfj+A/Io3wcRI3I+RMeozwLe7P6nFZI2nTWHQ5uCIRV2o20g"
    "oj20mqxlMnGsncjRi7K9Jk92gmFVGQo3CUpRBnq5/MaVnBMjyKzrRfj6iaONtXSAQqRo4MC6qbY1QpL60CxA6jbpwjwAar5k/gq8"
    "6fwNJNEDLlB2Qrq59wIb3dju/uHhGafs0iC2eS5dyAB+Bo+Jf9QQuxmoj1d7GylxpErVBbtJ+uH1MciKuA59XEuAC0b/AEjKVNWQ"
    "CCWLKirtYCtNxBGuc8g9Rgg6APSy3zDARkCI7L4uO6Vux4U+ZX8lOfh6aRMuASy7Z3SkdjLL5bcsHaUrFcmXqkodTLClFGwX50O3"
    "13HbU6v+GO0JOapcA2cIpnDZrcHn+sNuwxkfSQuCebl+4IK2FWeSIBRsOF1AyOInXcy/jdXzH3SIvbp9spkJZkPCe4QJ1OeKz3Lg"
    "AWjDzfM1daILdmnhsIrXbMD6JbTQwfjvGWuV4q/rfFhQ6W37QJVRBpTBhrReL1nykr685erF8baP+Rt63YiMEoTjhFwo9q3yQDuJ"
    "R+H+5ei+IveJzS6YlI4bA6WdRn6NI0VJDs7oGKHXnKCnqR+rNUAw6vCnZc3VzXI+yroCyz/UicpijtMST7MAQEz0X2gl3zRhe4eK"
    "momAjylj6n/UJE2jvVYCJL+bmkVprOUOpNBA/wAx6jWXk8DY5zRK733gqCjjH/4Y07Y6/Fy6xvCOAcjT7NWIC1GG8UOrwcmX2l15"
    "Qu2PBmJMO2pTbMESx6e8YlynwFq5v9ekX68Zl2qIy2eANj1Yj5VbFd2NWEoNJRq0q0CV1IIvkub8fbcErJsNxnC5Gc8TpM1C0prN"
    "m5CQay3IA/sIMQ48cQDWadqZY+Ca9dCCFwDcm9Psic6Ib6nnCtlwbxKYDbeDuwWgNrd8XlwJtd/cRfrjYcEg65rhycziRrIJC4JK"
    "AMrwOMIogFiU0TjyZ48IzpHfMDQo8BOPAFoCGBAZnELilyXPVy5ffXX9opI5lKK6GqaA3XEBv2UNdaB05vPCpmS2R/1ecsKXPzEw"
    "QbspVJau+yEc2Tbt15vF/wDBoJ5G80vg1YHryr/QBsMG+Yp+7VtlEuy5k5dBqwJiN6jkuBt8IABfFzD2iF3QFI8H7qU1/DRFn+q6"
    "2N+kA0/lDVpb3XHQ0ItdG23Kxoyx1QnqJxuu3lW8QgqoYTRIwwSKQ6Lejgd4+lNSQ1E+7VI0Ziv+I3aIfGNsO4I3d+GhFxlb3iKN"
    "IINAtXAjyQwu/Xy5Q4FtNbHYMKKnMWNWtqLZbyGzDcG5DPVSxQ2eLw7GP0zUkNRPtnbAW11BBKP1gRhtgtDu6sQHKKZvEcjUYwDd"
    "XYN2E3NOLdzPiNAhu3oUQdR1Fp8SrrcYE67LVEoXQZRuMedrqJuJuPCcbytganF4O+msbq9QUibfaBvpuVKo4uhyh42HrU6sAzBV"
    "p6KiwOijk5QGa/OMrtHGW2X5Yw/pDQg6hdTyxmOZSxNyHAOR13COhT1vo7yoZgfqFyiYurzh0Pfnj9l2azojX24rDqu0CkpMdgCj"
    "nUreSZRLb6lpfOqDpwAUepZTtmT4h42WlJ5pKKlb/CD8xJPXKQ9qyljmVo9iiKgHJTb3YL+LPROkcNvTojGk1Ba8XXEv5JmVXKI5"
    "U8rxy+wNKMv0Kdmxvulim7nDY9FCLXY4yswmsLlgX3M4yaXv2ZwgWGepxpeGJYsjuuI4C703EwlbI+5bRnjQeIcpyBuxKfGCAs61"
    "mBRHoLSyV+6KQrxCVkavp9TGsbZZa9iu8usocLUCVYzEOEqFlq5VeeAr4JVAGzfLDLc/rogqVdqb8tzwV2D1H7Q4rcQoFeBC1m0V"
    "HmqlQXA1A0xa8YKCpgznqOQJQTRjLySaiOIcWi3QMvivH1GX5IrmHaoqjm/4OsGIAyMNC6v8XnjRbexE0PS94rKfcnCdhXuOlaz7"
    "QS+oCQHAHsU9QYFNL3kl+48pGqIBEo8k423RM1KsMA2S6xC0xXg714jk2g4qvpYE47joX2qKneZb1jCUTbwjKtQAueR+YDHMjfaG"
    "wpoD4QNDOC/CZ5bgpjBrDjpLyHVXeo8+E/mLuU5k+I0MFo84NSqVBZLOkv8AqI7MeiIhpUHclPn6BHsJ1UIANQ5wBUW+kTOZerFa"
    "S/eiJAUBdhmUmj8wIh5m1LqzcP6IpaPNf00ov4MYJVKbDaGglLFxCUiHUf6On0Jh/wDoU3nxEu9UJkiDRPMscp5lSgK5U5Qx9u13"
    "wVIjJFA7QQVgjpepENUHRDIXdJm1e6+m3jLeMFNFirqr9tFaR5T/AKiK6t3z/tIFSjm/+r//2Q=="
)
LOGO_BYTES = base64.b64decode(LOGO_B64)

# BLOG AD (V141) - header advertisement for XRP Complete Blog. 430x70 banner
# (embedded at 860x140 for retina crispness, displayed at 430x70): satellite
# photo left, "XRP COMPLETE BLOG" wordmark, bold tagline, domain, Template D
# palette. V141 widened it 375->430 so its left edge lines up with the ABOUT US
# button above it; artwork regenerated at true 430x70 proportions (wider photo
# zone) rather than stretched, so it fills the slot instead of letterboxing.
# Served at /blog_ad.png; the <img> src carries ?v={APP_VERSION} (V129) so a
# cached copy of a previous banner can never be served after a swap.
BLOG_AD_B64 = (
    "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"
    "6fvfzF13fQtFq83dH3ofD3z0nSwe+YcUxSL9zUusHjnA2bMXEW7M8WtPUDkoqzP0FpbY3tghr/c49cCXOXT4CDd0FH/+52/jW970"
    "DykH28zNtTh7bh1RV1xz3TGsVwyHNQu9OS5duMTewav47u96NX/s/pCTDz1EuzsH0NipOwf40BRZSomzFp8WQuJqvDUVx6++joVe"
    "h029Qi40uZI8Nq5ZbTmOqIKR97RakvmFLsPBmNMXt1nutjm42GKM4My95xEHn0shDddctcDWrmF9a8TScsGRlYJH1x3ruyPa45JO"
    "u426/uWsXPoKw8c+zfrmFlopfFyfC33FQh1Xck9Msr6J/FhMWJ2G5bJNnU/jwhixRXJwJP7c9DWP4WPT9dQoWchpyV4AOyIyXT7K"
    "GNN20utKJWMH0QC+ffVeKSHFTzWnnoCrkAbKxllxsnNhzKmKtKnUYD9IY+q3NG5jNjIZ8HGffrKX/yrCOUdvrsv/8R/fxrfe9QJu"
    "vem6hs10IiwK/vw/+wd89gv3MBqNKfKc9c1tfu7v/yi33nQd1rnGgVZKycX1TX7+//wlWkXB5el1YkwvZ6IuP/Qkmddx3tTGcOTQ"
    "Af7zv/5nfPeb/rsACuWErXjCcS8b2MV9hTBvrHW86bXfwRe+fB//31/8TRYX5rBfQ0Mm8FROciAv+d9v/Tw3dods1wFcpCTaI8iE"
    "bwCHjWBLCN9I/7ZqwfPmd/jfbv0Lfu6e57FT5+jYMiadk9Qy5p/c+GW+/cAldurwnkzb8QItPQqPkIFVM5FdSwn+rhEsZxX/6y1f"
    "4v91/zP50MbhK4IuMfXf9GvGw8tWL/D7F048KWDxXtCWlpetXmj2+/Kxnujbgitvf5rB8fE8Cnwjpds1goXM8I+u+yr/4KvPZ2RV"
    "8/3Lx3uy7T/VfZICFrRv/kRNj2e8ZzWHtppAlLYyrOZhRmiRGHnP2MHI7v++B9rK01YTQOOATEIm6iueSzH13a72tOTjwdATjfF0"
    "z0HazpzQtKRk+i6pvGPo7b6Fq0u24js7q7xhfJi37Z1hReRXHPfruS5BcCX4l8u38OruQbZcUHeF8prwPNdIVKzNdRFseTxphmy5"
    "mlWV8x9Xb+cfbdzLnw4vMS/3gy6FYNcbfnT+Kv7Z0g0MnKXvTRxjYr4hpradqusSGCu9pfTwt+evxgP/avsk3VjfNov/tqE398bs"
    "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"
    "9jh8oMO40myMPOyWFB6MzjkzNCx1LEVW8MCFPt2FRXZGG/i527lwYYuFuYzrripY3ynZ2K7otQTzXclc0eHSzgg5gLluTlftsnf6"
    "PFtbO4388XKKxsd7MEntAjBTE4DWGE34IJ0ksF2pZ9Z0jy1rbWMzH78MwodFmFjvFuaqb+SFiZVQSk3GI4BASO6ESYziw3MlgsLE"
    "KfkEjCKgmzgMRup9mnaKx98wV48DUvGdhLpSBtUYa/ipcaa/OpG4PN4k468faE3H/5+9/463JLvKu/HvDlV18s2dpycnZRAggRIK"
    "VhwFQMgEY7ABg7ENGCdeHLEN2MbG2DI/25hosg0IEKCAUEJppJFGo5E0mtA9nbtvPvlU2OH9Y1edc26HUY9GI/H+Pr3m03PvPadq"
    "1z51qnatZ61nPcs5R6vZ4N//l1/kxS/4Gm6/9YY9QilKKf7pP/he4iTim1//ilmtog8OymSS8i9+6uemPdY+nwBF9fb6xjaf/dwx"
    "1laWMDZ40e/7wD1sbO7wS//tX0+3qzKkt99yA512MzQff4zxJ5OU3V5gFRhr2dzu8vf/6U9z5NB+7nrFi6bArFLbvO2WG/iDP31P"
    "yNpeoe2X8YLFOOcbD56kmMvABkfb8+lBh3/54DM5n9apKzvN8qxnNX7l9M3c11vi3975SVaiYrq/w6MEvPHQST6ws4+KmJUox7ce"
    "Po4qz5UUs+M8PGryrx58JsfHbRrKlNQ7T24093RX+Gh3le84cozvvf4YuQvXpxKekRU8e6HHC1fWeefmIRaj/PNeF0p4Jg6es7TJ"
    "kdqI9fxS8YzCSfbFKV+3tEHqnnh2K3waGBg9VRQEePfWAfpG8zNP/XgIsBDWIOPgSH1EQxmG9upaD3whJoVnKcrJ5JVVDh2z/mB1"
    "ZWhW4sWEcymBhr64MqqiFBoW4oylKH9c9Wa+HHOpbBHwWHVmT8Q80BSaRRWzVAIuQchk/cF4ne/sHGFNxRRVvS0hI/TFWukcnppU"
    "fE/nuvJ+CBRBh6chFA8UA/7+1gM8XIxoCDWlFObe8KF0lw9Mdvn+haP80MKN5GXwUyHoO8NzkyX+Sn2Vt443WJQRA1vwDe39PDVu"
    "0XNmT2arKTTvmmzxE7uPcMpMQvCmXOut9/zq4Aw/uHgj39u+rqQ/zub/dbUlXlJf4a3XslxPuunxJGe7VzDJDXlhGWc5zsNonDEu"
    "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"
    "k89f5g//t/+QP/4jH+F9D9/L8sIs2hiuXN/kV37rK/zHX/1CEXqsDvFwH35fa50yurPb5x/+i1/iH/7f/hSjcUIY+lX7yzA6oAh3"
    "qixpcqORQjrSjEpZcyF/jzz+Eg+95Q52ewOajYgnn7vM+uZulftyfX2XZ1+6yj3nTzAcxSgpeeTxFxiNEmbbjVuQo7IO2IP3nOHj"
    "3/sert3Yph4F/Oonv8qvf/pxGvUIKQWPP3OBf/a//xr//Z/6frZ3trnzjmP8+Mc/zN/7yZ8ny3L2+iN6/RH9wRhtDFEU8NKFNf7t"
    "f/wd/vwf+x6u3ejx1vvu4Ds+8CD/4Rc/7c7pTc55o/7z24+9fcNzAQuqMKr+4t/5af7Sn/o+3nbfWdqtOr3BiFwb6jU31q89V1zO"
    "nTGHt+N27Tv4fZpkYCGKAv4///a/8Mrlm/yxH/4Id58/Tp5rLly+yf/jn/4nPvSe+/i29z3Abnewb3w8T/H3fuo/8uiTL/MjH3sf"
    "d549RqMW0u0NeeypV/jXP/9JnnvpWpGjk0zG5ZDncdgaBOeo7+4N+bP/wz/lj3z8w3zXBx/ixOoCUgpubuzy2S8/w7/9xU+x0x1Q"
    "i/yipIz3utrVakS3hOIaY2jWI377c1/nR//c/4s//qPfxtsfOMfCXBtjDGs3d/idLz7Jz/ynzzAYxYS+y7Fr1CN+7lc+B9byB3/w"
    "Ayx2ZvB9zzkmQp/r69v8ib/6T/izP/5RPvLe+5lp1dnpDvjk57/Oz/3K5/j3P/lXqrpxcZErFb+J8QoDn+s3d6p7ffi99zHbarC7"
    "N+C3P/8k/8cvf45/95N/ubpXOQfqtZCf/pnf4NLVDf7oD3/EkeVow6VrG1Xo8v33nKa7N6A/xVTYG4zd3nJgHbj188bbc/AaR/LG"
    "Rfz7n/8lK4WrSWNyA0V9IvdyB2Ep6JwnYS/l7461ySFZRmtHYV0aC2ZioLlaNHJiIQuBwBQhhBMFpES5SlFFDlSJHqjCeFJlQTej"
    "idMcIRVR4JEkOeN4XBlR3lQOiamMReUY64t7+p4LicjzvHgRO6Qg1wUJgfQKmk4XDiVw4RdJkpEWC8l12iLUBO0oycby3EHhFrh2"
    "fR2pFHmecP3aVe48d4peb8Qrl65zpZ+hrcfG7hjpRwibO0PrAEQsqvEr1K1COXNkCQaji7FUMDPboBaG9IcDRiPtwrkkxMMUWY5J"
    "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"
    "18WfhVKYNJFrH4JQ6JKEVqsVwYzCGo01CmuU1NLE9SiKQmpM4lWqqio636GhIFprY1Q9UgS1iUDQxPOQerh56mVNa6wpgjpSEOfr"
    "U0Dmb43U2lljSeP49TjGmiabkqYJ1hqGozFJannx5Uu8+93v4qEHz7O3vw1pnwc3V1haX+UtZ9bp+wl7BxOG45LTGxt0shavXn6N"
    "5bV1PvD2h1m1Jd/54DJLaaAIqqGC6VpxLdJeiZQwP5/5DBCqislowmAon2G15sxmn/vWRUI2L6Zkiea+jT79Tov9QS6NSFMT6xCh"
    "9kalAa7Qs7wLTIcT8vGU0aQizz33n1ji/s1lbKJZX+rQ6rW5vj3in/zq8/zM515m66Cg383IEpFtb5rmKsVkMolgfSYTfzS7VdMQ"
    "jzYVF+CbcDAYNHWJ4mQbMqtJrUIvn+XqoOT5K7d5/NnX2BlM+dJL1zFGsdzpCJhqt6QhpoaqChid0G4npKkhENBG4WNA5NW9MT/z"
    "60/wsU/8Nleu3mJtucef+IHv54N/+oO85S2P0O8v0el2yVotATsxg62UopwckO9f4/JLX2N5ZY1Ou40PUvuVthL6G2tybQZDxoN9"
    "klaL/uo6SgeUz7l28zYrqxvo6TYmSdG2hU5bUsNlUnRiUSYRGXwttVzEzGdQWhSsVJ0Br/cNswbIDXVwBowCdYa/BmYzCuJ8naGO"
    "KoGKWfa13o9NRkzNesHVGa3DpprX6gPrFhXxA5tnjBKe4BwLIQ5RP0sjl1Ch57JRqjlwNvf4+ztskcJa2MIWtrCFLez31AJOGQOK"
    "z1qj9WdHo2GuFElNf6qjnYrDEfha7rwsCmqgVTf+jX5IQy90zsd6JNsAJwFsvnEygwqUpYsAQMfGrTJmDXzq2pKqrIS+pBXWGpzz"
    "Taat3W6hAR/nEryIRSTWEoInz3PaLYnGEzxl5UhSqU0i9hWrC+Ir53C5E1CoQIW6sbHUe5lYg1F5F1tEhdg3C1o2AaVxVRn7cKlm"
    "bXTtlEUwKmshTEjvPC44lNakWQYhiIhJQxk0MUMldL8avNb0Q5T03JpXWNOxJmzeyZtRpOreVyJDX0vbC67RTYQ9BBH+qAGlNuLw"
    "Bx9wVoBYS7WpXEWr1cW5wDSf8oM//Cf5nuGIaVXyjre/nZ3dPbIko9tNycuS3/nsFzl39n5evb3H2x++wGuXL3H69CkePXeathtx"
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
    "top10": [], "top10_updated": None,
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


TOP10_CATEGORIES = {
    "BTC":  ("Store of Value",        "var(--yl)"),
    "ETH":  ("Smart Contract Platform","var(--bl)"),
    "XRP":  ("Cross-Border Payments", "var(--hdr)"),
    "USDT": ("Stablecoin",            "var(--tq)"),
    "USDC": ("Stablecoin",            "var(--tq)"),
    "BNB":  ("Exchange Token",        "var(--or)"),
    "SOL":  ("Smart Contract Platform","var(--bl)"),
    "DOGE": ("Payments / Meme",       "var(--gr)"),
    "TRX":  ("Payments Infrastructure","var(--gr)"),
    "ADA":  ("Smart Contract Platform","var(--bl)"),
    "STETH":("Liquid Staking",        "var(--tq)"),
    "AVAX": ("Smart Contract Platform","var(--bl)"),
    "SHIB": ("Payments / Meme",       "var(--gr)"),
    "TON":  ("Smart Contract Platform","var(--bl)"),
    "DOT":  ("Interoperability",      "var(--br)"),
    "LINK": ("Oracle Network",        "var(--br)"),
    "LTC":  ("Payments",              "var(--gr)"),
    "BCH":  ("Payments",              "var(--gr)"),
    "XLM":  ("Cross-Border Payments", "var(--hdr)"),
    "HBAR": ("Enterprise Ledger",     "var(--br)"),
    "SUI":  ("Smart Contract Platform","var(--bl)"),
    "WBTC": ("Store of Value",        "var(--yl)"),
}
TOP10_CATEGORY_DEFAULT = ("Digital Asset", "var(--tx)")


def fetch_top10():
    """V149: Top 10 Cryptocurrencies by market cap \u2014 checked, listed, categorized,
    10 data points each. One lightweight, purpose-built call for exactly a top-N
    ranking (fixed from an earlier draft that pulled the full multi-thousand-coin
    CoinPaprika tickers list and filtered client-side)."""
    hdr = {"User-Agent": "XRPComplete/4"}
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/coins/markets",
            params={
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": 10,
                "page": 1,
                "price_change_percentage": "1h,24h,7d",
            },
            headers=hdr, timeout=8,
        )
        rows = r.json()
        if not isinstance(rows, list) or not rows:
            return
        parsed = []
        total_mcap = 0.0
        for i, c in enumerate(rows[:10]):
            price = float(c.get("current_price") or 0)
            mcap = float(c.get("market_cap") or 0)
            if not price:
                continue
            sym = (c.get("symbol") or "").upper()
            entry = {
                "rank": c.get("market_cap_rank") or (i + 1),
                "name": c.get("name", sym),
                "symbol": sym,
                "price": price,
                "mcap": mcap,
                "vol24": float(c.get("total_volume") or 0),
                "chg1h": float(c.get("price_change_percentage_1h_in_currency") or 0),
                "chg24h": float(c.get("price_change_percentage_24h_in_currency")
                                or c.get("price_change_percentage_24h") or 0),
                "chg7d": float(c.get("price_change_percentage_7d_in_currency") or 0),
                "supply": float(c.get("circulating_supply") or 0),
                "max_supply": float(c.get("max_supply") or 0),
                "ath_price": float(c.get("ath") or 0),
                "pct_from_ath": float(c.get("ath_change_percentage") or 0),
            }
            cat, cat_color = TOP10_CATEGORIES.get(sym, TOP10_CATEGORY_DEFAULT)
            entry["category"] = cat
            entry["cat_color"] = cat_color
            total_mcap += mcap
            parsed.append(entry)
        for e in parsed:
            e["dominance"] = (e["mcap"] / total_mcap * 100) if total_mcap else 0
        if parsed:
            MARKET["top10"] = parsed
            MARKET["top10_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
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
                fetch_top10()
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
                "Africa": "\U0001F30D", "SEA": "\U0001F30F",
                # V148: US isn't in REGIONS/REGION_DISPLAY (it has its own dedicated
                # "US Intelligence" panel elsewhere), but stories can still carry
                # region="US" via keyword detection -- and this dict had no fallback,
                # so REGION_FLAGS.get("US","") silently returned nothing wherever a
                # region flag was rendered (e.g. the Brief's Regional section).
                "US": "\U0001F1FA\U0001F1F8"}
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


# ── PROPRIETARY / OFFICIAL SOURCE FEED (V136) ────────────────────────────────
# Zero added load: every story below already arrives through the existing news
# cycle -- this is a filtered view of the pool, not a new set of HTTP fetches,
# so it adds no requests, no new failure points and no risk to the site.
# Tiers are kept honest and separate: only publications Ripple/XRPL actually
# own are called first-party. Google News queries that track Ripple executives
# are third-party reporting ABOUT official figures and are labelled as such.
FIRST_PARTY_SOURCES = {"Ripple Insights", "XRPL.org Blog"}
OFFICIAL_COVERAGE_SOURCES = {
    "GN: Garlinghouse", "GN: Ripple CEO", "GN: Brad Interview", "GN: David Schwartz",
    "GN: Monica Long", "GN: Ripple Labs", "GN: XRPLF",
}
# Official properties that publish no usable public RSS -- linked, never scraped.
OFFICIAL_DIRECTORY = [
    ("Ripple Insights",      "https://ripple.com/insights/",     "Ripple's own company blog", True),
    ("XRPL.org Blog",        "https://xrpl.org/blog/",           "Core ledger development blog", True),
    ("XRPL Foundation",      "https://www.xrpl.foundation/",     "Foundation (Paris entity, est. 2024)", False),
    ("XRPLF Legacy Site",    "https://xrplf.org/",               "Original foundation site", False),
    ("XRPL Commons",         "https://xrpl-commons.org/",        "Ecosystem-adjacent, not Ripple-owned", False),
    ("XRPLF on GitHub",      "https://github.com/XRPLF",         "Reference implementations & XLS standards", False),
    ("Ripple Newsroom",      "https://ripple.com/press-releases/", "Official press releases", False),
    ("XRPL Dev Portal",      "https://xrpl.org/docs.html",       "Protocol documentation", False),
    ("RippleX",              "https://ripplex.io/",              "Ripple's developer arm", False),
]


def proprietary_feed_html(limit=8):
    """Filtered view of first-party and official-entity stories already in the pool."""
    pool = NEWS.get("pool", [])
    first = sorted((s for s in pool if s.get("source") in FIRST_PARTY_SOURCES),
                   key=lambda s: s["dt"], reverse=True)[:limit]
    cover = sorted((s for s in pool if s.get("source") in OFFICIAL_COVERAGE_SOURCES),
                   key=lambda s: s["dt"], reverse=True)[:limit]

    def rows(stories, empty):
        if not stories:
            return f'<div class="ih-empty">{empty}</div>'
        out = '<div class="intel-heads">'
        for s in stories:
            dot = {"bullish": "var(--gr)", "bearish": "var(--rd)"}.get(s["sentiment"], "var(--tx)")
            out += (f'<a class="ih-item" href="{html.escape(s.get("link") or "#", quote=True)}" '
                    f'target="_blank" rel="noopener">'
                    f'<span class="ih-dot" style="background:{dot}"></span>'
                    f'<span class="ih-t">{html.escape(s["title"][:130])}</span>'
                    f'<span class="ih-m">{html.escape(s["source"])} \u00B7 {_time_ago(s["dt"])}</span></a>')
        return out + '</div>'

    directory = '<div class="pf-dir">' + "".join(
        f'<a class="pf-d" href="{u}" target="_blank" rel="noopener">'
        f'<span class="pf-dn">{html.escape(n)}'
        + ('<span class="pf-badge">LIVE</span>' if live else '')
        + f'</span><span class="pf-dd">{html.escape(d)}</span></a>'
        for n, u, d, live in OFFICIAL_DIRECTORY) + '</div>'

    return (rows(first, "No first-party posts in the current cycle \u2014 Ripple and XRPL.org "
                        "publish less often than the wider media, so a quiet window here is normal "
                        "and is reported as such rather than padded."),
            rows(cover, "No coverage of official Ripple figures in the current cycle."),
            directory, len(first), len(cover))


# ── COMMUNITY MEME WALL (V138) ───────────────────────────────────────────────
# Memes are embedded as base64 and served from their own cached routes -- the
# same pattern already used for the header logo and the blog banner. The main
# site deliberately has no POST routes and no user-writable storage, so there
# is no upload form and no new attack surface: Rich sends a meme, it ships in
# the next build.
#
# To add one, append a dict to MEMES:
#   {"id": "short_slug", "caption": "Caption text", "credit": "@handle or None",
#    "added": "2026-07-26", "b64": "<base64 png/jpg>"}
# Newest-first ordering is by list position (append new ones at the top).
MEMES = []


def meme_wall_html():
    if not MEMES:
        return ('<div class="home-base"><div class="home-base-icon">\U0001F5BC\uFE0F</div>'
                '<div class="home-base-title">The Wall Is Empty \u2014 For Now</div>'
                '<div class="home-base-sub">XRP community memes will appear here as they are '
                'added. Nothing is auto-scraped and nothing is placeholder art: every image on '
                'this wall is one Rich has chosen and cleared.</div></div>')
    cards = ""
    for mm in MEMES:
        cap = html.escape(mm.get("caption") or "")
        cred = mm.get("credit")
        meta = html.escape(mm.get("added") or "")
        if cred:
            meta += (" \u00B7 " if meta else "") + html.escape(cred)
        cards += (
            f'<figure class="meme-card">'
            f'<a href="/meme/{html.escape(mm["id"], quote=True)}.png" target="_blank" rel="noopener">'
            f'<img src="/meme/{html.escape(mm["id"], quote=True)}.png?v={APP_VERSION}" '
            f'alt="{cap}" loading="lazy"></a>'
            + (f'<figcaption class="meme-cap">{cap}</figcaption>' if cap else '')
            + (f'<div class="meme-meta">{meta}</div>' if meta else '')
            + '</figure>')
    return f'<div class="meme-grid">{cards}</div>'


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

def _fmt_num(v):
    if not v:
        return "\u2014"
    if v >= 1e9:
        return f"{v / 1e9:.2f}B"
    if v >= 1e6:
        return f"{v / 1e6:.2f}M"
    if v >= 1e3:
        return f"{v / 1e3:.1f}K"
    return f"{v:.2f}"


def _fmt_price(v):
    if not v:
        return "\u2014"
    if v >= 1:
        return f"${v:,.2f}"
    if v >= 0.01:
        return f"${v:.4f}"
    return f"${v:.6f}"


def top10_cards_html():
    """V149: Top 10 Cryptocurrencies \u2014 dominance ribbon + per-coin cards,
    10 data points each. 'Precision Ink meets terminal' visual treatment."""
    rows = MARKET.get("top10") or []
    if not rows:
        return ('<div style="padding:22px;text-align:center;color:var(--tx);font-family:var(--mn)">'
                'Live rankings loading \u2014 checking market data now\u2026</div>')

    # Dominance ribbon: one segment per coin, width = share of combined top-10 market cap
    ribbon = "".join(
        f'<div class="t10-rib-seg" style="width:{max(c["dominance"],1.2):.2f}%;background:{c["cat_color"]}" '
        f'title="{c["symbol"]} \u2014 {c["dominance"]:.1f}% of top-10 cap"></div>'
        for c in rows
    )
    ribbon_keys = "".join(
        f'<div class="t10-rib-key"><span class="t10-rib-dot" style="background:{c["cat_color"]}"></span>'
        f'{c["symbol"]} <b>{c["dominance"]:.1f}%</b></div>'
        for c in rows
    )

    cards = []
    for c in rows:
        chg24 = c["chg24h"]
        chg7 = c["chg7d"]
        chg1 = c["chg1h"]
        col24 = "var(--gr)" if chg24 >= 0 else "var(--rd)"
        col7 = "var(--gr)" if chg7 >= 0 else "var(--rd)"
        col1 = "var(--gr)" if chg1 >= 0 else "var(--rd)"
        arrow24 = "\u25B2" if chg24 >= 0 else "\u25BC"
        is_xrp = c["symbol"] == "XRP"
        glow = "box-shadow:0 0 0 1px var(--hdr) inset,0 0 16px rgba(3,177,252,.25);" if is_xrp else ""
        border = "border-color:rgba(3,177,252,.55);" if is_xrp else ""
        supply_pct = None
        if c["max_supply"]:
            supply_pct = min(100, c["supply"] / c["max_supply"] * 100)
        cards.append(f"""
        <div class="t10-card" style="{border}{glow}">
          <div class="t10-card-top">
            <div class="t10-rank">#{c["rank"]}</div>
            <div class="t10-name">
              <div class="t10-sym">{c["symbol"]}{' <span class="t10-xrp-tag">XC FLAGSHIP</span>' if is_xrp else ''}</div>
              <div class="t10-full">{c["name"]}</div>
            </div>
            <div class="t10-cat" style="color:{c["cat_color"]};border-color:{c["cat_color"]}">{c["category"]}</div>
          </div>
          <div class="t10-price-row">
            <div class="t10-price">{_fmt_price(c["price"])}</div>
            <div class="t10-chg" style="color:{col24}">{arrow24} {abs(chg24):.2f}% <span class="t10-chg-lbl">24h</span></div>
          </div>
          <div class="t10-grid">
            <div class="t10-cell"><span class="t10-k">Market Cap</span><span class="t10-v">${_fmt_num(c["mcap"])}</span></div>
            <div class="t10-cell"><span class="t10-k">24h Volume</span><span class="t10-v">${_fmt_num(c["vol24"])}</span></div>
            <div class="t10-cell"><span class="t10-k">1h Change</span><span class="t10-v" style="color:{col1}">{'+' if chg1>=0 else ''}{chg1:.2f}%</span></div>
            <div class="t10-cell"><span class="t10-k">7d Change</span><span class="t10-v" style="color:{col7}">{'+' if chg7>=0 else ''}{chg7:.2f}%</span></div>
            <div class="t10-cell"><span class="t10-k">Circulating Supply</span><span class="t10-v">{_fmt_num(c["supply"])} {c["symbol"]}</span></div>
            <div class="t10-cell"><span class="t10-k">Max Supply</span><span class="t10-v">{_fmt_num(c["max_supply"]) if c["max_supply"] else "Uncapped"}</span></div>
            <div class="t10-cell"><span class="t10-k">All-Time High</span><span class="t10-v">{_fmt_price(c["ath_price"])}</span></div>
            <div class="t10-cell"><span class="t10-k">From ATH</span><span class="t10-v" style="color:var(--rd)">{c["pct_from_ath"]:.1f}%</span></div>
            <div class="t10-cell"><span class="t10-k">Top-10 Dominance</span><span class="t10-v">{c["dominance"]:.2f}%</span></div>
            <div class="t10-cell"><span class="t10-k">Category</span><span class="t10-v" style="color:{c["cat_color"]}">{c["category"]}</span></div>
          </div>
          {f'<div class="t10-supply-track"><div class="t10-supply-fill" style="width:{supply_pct:.1f}%;background:{c["cat_color"]}"></div></div><div class="t10-supply-lbl">{supply_pct:.1f}% of max supply mined</div>' if supply_pct is not None else ''}
        </div>""")

    return f"""
      <div class="t10-rib-wrap">
        <div class="t10-rib-lbl">Combined Top-10 Market-Cap Share</div>
        <div class="t10-rib">{ribbon}</div>
        <div class="t10-rib-keys">{ribbon_keys}</div>
      </div>
      <div class="t10-grid-outer">{''.join(cards)}</div>
      <div class="t10-foot">Ranked live by market capitalization \u2014 {len(rows)} assets checked. Categories are XRP Complete editorial classifications. Updated {MARKET.get("top10_updated") or "\u2014"}. Not financial advice.</div>
"""


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
    neut = total - bull - bear
    lean = "bullish" if bull > bear else "bearish" if bear > bull else "balanced"
    chg = MARKET.get("xrp_chg")
    dir_txt = ("up" if (chg or 0) >= 0 else "down") + (f" {abs(chg):.2f}% over 24h" if chg is not None else "")
    fng = MARKET.get("fng")
    fng_txt = (f"Fear & Greed reads {fng} ({MARKET.get('fng_label', '')})" if fng is not None
               else "Fear & Greed is unavailable")
    n_sources = len({s["source"] for s in pool})
    breaking_n = sum(1 for s in pool if s.get("breaking"))
    cat_rows = _rank_counts([s.get("category") for s in pool if s.get("category")])

    # V147: PULSE \u2014 added source diversity, breaking-story count, and the
    # single busiest coverage category, all real counts over the same pool.
    pulse = (f"The tape carries {total} XRP stor{'y' if total == 1 else 'ies'} this edition across "
             f"{n_sources} distinct source{'s' if n_sources != 1 else ''}, leaning {lean} "
             f"({bull} bullish, {bear} bearish, {neut} neutral). {fng_txt}; XRP is {dir_txt}.")
    if breaking_n:
        pulse += f" {breaking_n} stor{'y is' if breaking_n == 1 else 'ies are'} flagged breaking."
    if cat_rows:
        top_cat, top_cat_n = cat_rows[0]
        pulse += f" Coverage concentrates in {top_cat} ({top_cat_n} of {total})."

    theme_hits = []
    for name, kws in _BRIEF_THEMES.items():
        stories = [s for s in pool if any(k in (s["title"] + " " + s.get("summary", "")).lower() for k in kws)]
        if stories:
            srcs = len({s["source"] for s in stories})
            b = sum(1 for s in stories if s["sentiment"] == "bullish")
            r = sum(1 for s in stories if s["sentiment"] == "bearish")
            lead_story = sorted(stories, key=lambda s: s["influence"], reverse=True)[0]
            theme_hits.append((name, len(stories), srcs, b, r, lead_story))
    theme_hits.sort(key=lambda t: (t[1], t[2]), reverse=True)

    # V147: CONNECTIONS \u2014 now names the actual leading headline behind the
    # dominant thread and gives each runner-up its own sentiment split, instead
    # of just a story/outlet count.
    if theme_hits:
        n, c, sc, b, r, lead_story = theme_hits[0]
        connections = (f"The dominant thread is {n} ({c} stor{'y' if c == 1 else 'ies'} across "
                       f"{sc} outlet{'s' if sc != 1 else ''}, {b} bullish / {r} bearish). "
                       f"Leading it: \u201c{html.escape(lead_story['title'][:100])}\u201d ({html.escape(lead_story['source'])}).")
        if len(theme_hits) > 1:
            runners = "; ".join(
                f"{n2} ({c2}, {'bullish' if b2 > r2 else 'bearish' if r2 > b2 else 'even'})"
                for n2, c2, sc2, b2, r2, _ in theme_hits[1:3])
            connections += f" Also active: {runners}."
        connections += " Cross-outlet convergence suggests the narrative is broadening, not isolated."
    else:
        connections = "Coverage is fragmented with no single dominant thread this edition."

    # V147: DOMINO \u2014 added a concrete numeric trigger condition and, when
    # one exists, names the second-place theme as the alternate catalyst to watch.
    if theme_hits:
        lead = theme_hits[0][0]
        runner_up = theme_hits[1][0] if len(theme_hits) > 1 else None
        if lean == "bullish":
            domino = (f"If {lead} momentum holds ({bull} of {total} stories bullish today), expect follow-through "
                      f"buying and secondary coverage from lagging outlets; watch for confirmation in price and volume.")
        elif lean == "bearish":
            domino = (f"With sentiment tilting bearish around {lead} ({bear} of {total} stories bearish today), "
                      f"near-term downside headlines could compound; a single positive catalyst would be needed "
                      f"to reverse the tone.")
        else:
            domino = (f"{lead} is driving the cycle but sentiment is balanced ({bull} bullish vs {bear} bearish) "
                      f"\u2014 the next major headline likely sets direction; until then, expect a range-bound reaction.")
        if runner_up:
            domino += f" {runner_up} is the clearest alternate catalyst if {lead} stalls."
    else:
        domino = "No clear catalyst chain this edition; the market is between stories and likely to drift."

    reg_rows = _rank_counts([s["region"] for s in pool if s.get("region")])
    # V147: REGIONAL \u2014 each region now cites its own leading headline, and
    # the section states how many of the tracked regions are active vs quiet.
    n_regions_tracked = len(REGIONS)
    n_regions_active = len(reg_rows)
    if reg_rows:
        parts = []
        for reg, cnt in reg_rows[:3]:
            rs = [s for s in pool if s.get("region") == reg]
            b = sum(1 for s in rs if s["sentiment"] == "bullish")
            r = sum(1 for s in rs if s["sentiment"] == "bearish")
            sig = "bullish" if b > r else "bearish" if r > b else "neutral"
            top = sorted(rs, key=lambda s: s["influence"], reverse=True)[0]
            parts.append(f"{REGION_FLAGS.get(reg, '')} {reg} ({cnt}, {sig}) \u2014 "
                        f"\u201c{html.escape(top['title'][:70])}\u201d")
        regional = (f"{n_regions_active} of {n_regions_tracked} tracked regions active this edition. "
                   "Regional activity concentrates in " + "; ".join(parts) + ".")
    else:
        regional = "No regional flashpoints \u2014 coverage is US and global-centric this edition."

    # V147: WATCHLIST \u2014 extended from 4 to 6 stories and each now shows
    # sentiment and recency alongside title/source, not just a bare list.
    watch = sorted(pool, key=lambda s: s["influence"], reverse=True)[:6]
    if watch:
        dot = {"bullish": "\u25B2", "bearish": "\u25BC", "neutral": "\u25CF"}
        items = "; ".join(
            f"({i}) {dot.get(s['sentiment'], '\u25CF')} {html.escape(s['title'])} \u2014 "
            f"{html.escape(s['source'])}, {_time_ago(s['dt'])}"
            for i, s in enumerate(watch, 1))
        watchlist = f"Highest-signal stories to watch ({len(watch)}): " + items + "."
    else:
        watchlist = "No standout stories to flag this edition."

    # V147: TRADFI \u2014 broken into its actual sub-categories (ETF/custody,
    # banking, regulatory/SEC) with real per-bucket counts, plus the leading
    # headline, instead of one aggregate count.
    tradfi_buckets = {
        "ETF & custody": {"etf", "custody", "blackrock", "fidelity", "nasdaq"},
        "Banking & settlement": {"bank", "swift", "settlement"},
        "Regulatory": {"sec", "institutional"},
    }
    tf_all, tf_parts = [], []
    for label, kws in tradfi_buckets.items():
        matched = [s for s in pool if any(k in (s["title"] + " " + s.get("summary", "")).lower() for k in kws)]
        tf_all.extend(matched)
        if matched:
            tf_parts.append(f"{label} ({len(matched)})")
    tf_all = list({s['key']: s for s in tf_all}.values())  # de-dup stories matching multiple buckets
    if tf_all:
        top_tf = sorted(tf_all, key=lambda s: s["influence"], reverse=True)[0]
        tradfi = (f"{len(tf_all)} stor{'y' if len(tf_all) == 1 else 'ies'} touch traditional-finance integration: "
                 + ", ".join(tf_parts) + f". Leading: \u201c{html.escape(top_tf['title'][:90])}\u201d "
                 f"({html.escape(top_tf['source'])}). Institutional plumbing remains the structural story "
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
     "stats": [("Total Supply", "100B XRP"), ("Circulating", "~61.9B XRP"), ("In Escrow", "~38.2B XRP")]},
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
    # V138: community meme wall
    meme_html = meme_wall_html()
    meme_count = len(MEMES)

    # V136: proprietary / official source feed (filtered from existing pool)
    pf_first, pf_cover, pf_dir, pf_nf, pf_nc = proprietary_feed_html()

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
    top10_html = top10_cards_html()
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
  .hdr{{ display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; padding-top:36px; padding-bottom:40px; flex-wrap:wrap; gap:6px; }}
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
  /* V143: the story list runs far longer than the rail, which stranded a tall
     empty column beneath it. Sticky keeps the rail in view while the feed
     scrolls, so the space stays useful instead of blank. Disabled below 900px
     where the grid collapses to one column and the rail sits under the feed. */
  .rail{{ display:flex; flex-direction:column; gap:10px; position:sticky; top:64px;
          align-self:start; max-height:calc(100vh - 80px); overflow-y:auto; }}
  .rail-panel{{ background:var(--s1); border:1px solid var(--b); border-radius:10px; padding:16px 18px; }}
  .rail-h{{ font-size:15px; font-weight:800; font-family:var(--mn); letter-spacing:1.5px; text-transform:uppercase;
    color:var(--hdr); display:flex; align-items:center; gap:10px; margin-bottom:6px; }}
  .rail-h .sic{{ font-size:22px; }}
  .rail-row{{ display:flex; justify-content:space-between; align-items:center; gap:10px; min-height:34px;
    font-family:var(--mn); font-size:15px; border-bottom:1px solid rgba(26,32,48,.35); }}
  .rail-row:last-child{{ border-bottom:none; }}
  .rail-k{{ color:var(--tx); }}
  .rail-v{{ font-weight:700; color:var(--br); text-align:right; white-space:nowrap; }}
  @media(max-width:900px){{ .feed-wrap{{ grid-template-columns:1fr; }}
                           .rail{{ position:static; max-height:none; overflow:visible; }} }}

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

  /* V139: About page content, now on the shared site template */
  .about-body h1{{ color:var(--hdr); font-size:30px; margin:0 0 8px; }}
  .about-body h2{{ color:var(--tq); font-size:19px; margin:28px 0 10px; border-bottom:1px solid var(--b); padding-bottom:7px; }}
  .about-body p{{ font-size:15px; color:var(--br); margin:0 0 13px; line-height:1.7; }}
  .about-body .tagline{{ color:var(--tx); font-size:15px; margin-bottom:26px; }}
  .about-body .contact-box{{ background:var(--s2); border:1px solid var(--b); border-radius:9px; padding:14px 16px; margin:10px 0; }}
  .about-body .fine-print{{ font-size:12.5px; color:var(--tx); margin-top:26px; padding-top:16px; border-top:1px solid var(--b); line-height:1.65; }}
  .about-body ul{{ color:var(--br); font-size:15px; line-height:1.75; }}
  .about-body a{{ color:var(--hdr); }}

  /* V138: community meme wall */
  .meme-grid{{ display:grid; grid-template-columns:repeat(auto-fill,minmax(230px,1fr)); gap:14px; margin-top:12px; }}
  .meme-card{{ margin:0; background:var(--s2); border:1px solid var(--b); border-radius:10px; overflow:hidden; }}
  .meme-card img{{ width:100%; height:auto; display:block; }}
  .meme-card a{{ display:block; }}
  .meme-card:hover{{ border-color:rgba(224,68,124,.65); }}
  .meme-cap{{ font-size:12.5px; color:var(--br); padding:9px 11px 0; line-height:1.45; }}
  .meme-meta{{ font-family:var(--mn); font-size:10px; color:var(--tx); padding:4px 11px 10px; }}

  /* V136: proprietary source directory */
  .pf-dir{{ display:grid; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); gap:8px; }}
  .pf-d{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:9px 11px; text-decoration:none; display:block; }}
  .pf-d:hover{{ border-color:rgba(0,229,204,.6); }}
  .pf-dn{{ display:flex; align-items:center; gap:7px; font-family:var(--mn); font-size:12.5px; font-weight:800; color:var(--br); }}
  .pf-dd{{ display:block; font-size:11px; color:var(--tx); margin-top:2px; }}
  .pf-badge{{ font-family:var(--mn); font-size:8.5px; font-weight:900; letter-spacing:.8px; color:#04121f;
              background:var(--gr); border-radius:3px; padding:1px 4px; }}

  /* V135: expanded US Intelligence / Global Pulse panels */
  .intel-stats{{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin:10px 0 12px; }}
  .intel-stat{{ background:var(--s2); border:1px solid var(--b); border-radius:8px; padding:8px 4px; text-align:center; }}
  .is-n{{ font-family:var(--mn); font-size:20px; font-weight:900; line-height:1; }}
  .is-l{{ font-family:var(--mn); font-size:11px; color:var(--tx); margin-top:3px; letter-spacing:.4px; }}
  .intel-sub{{ font-family:var(--mn); font-size:13px; letter-spacing:1.4px; text-transform:uppercase;
               color:var(--hdr); font-weight:800; margin:14px 0 7px; border-top:1px solid var(--b); padding-top:10px; }}
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

  .srow-2{{ grid-template-columns:repeat(2,1fr); }}
  @media(max-width:700px){{ .srow-2{{ grid-template-columns:1fr; }} }}
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

  /* Top 10 Cryptocurrencies (V149) */
  .t10-rib-wrap{{ margin:4px 0 18px; }}
  .t10-rib-lbl{{ font-size:12px; font-family:var(--mn); letter-spacing:1.5px; text-transform:uppercase; color:var(--tx); margin-bottom:6px; }}
  .t10-rib{{ display:flex; width:100%; height:20px; border-radius:10px; overflow:hidden; border:1px solid var(--b); background:var(--s2); }}
  .t10-rib-seg{{ height:100%; transition:opacity .2s; border-right:1px solid rgba(0,0,0,.35); }}
  .t10-rib-seg:hover{{ opacity:.72; }}
  .t10-rib-seg:last-child{{ border-right:none; }}
  .t10-rib-keys{{ display:flex; flex-wrap:wrap; gap:10px 14px; margin-top:8px; font-family:var(--mn); font-size:12px; color:var(--tx); }}
  .t10-rib-key{{ display:flex; align-items:center; gap:5px; white-space:nowrap; }}
  .t10-rib-key b{{ color:var(--br); }}
  .t10-rib-dot{{ width:9px; height:9px; border-radius:50%; display:inline-block; flex-shrink:0; }}
  .t10-grid-outer{{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; }}
  .t10-card{{ background:linear-gradient(160deg,var(--s1) 0%,#0d1220 100%); border:1px solid var(--b);
    border-radius:12px; padding:14px 15px; position:relative; overflow:hidden; transition:transform .15s,border-color .15s; }}
  .t10-card:hover{{ transform:translateY(-2px); border-color:rgba(117,188,255,.5); }}
  .t10-card-top{{ display:flex; align-items:flex-start; gap:10px; margin-bottom:10px; }}
  .t10-rank{{ font-family:var(--mn); font-weight:900; font-size:15px; color:#000; background:var(--br);
    border-radius:7px; width:32px; height:32px; display:flex; align-items:center; justify-content:center; flex-shrink:0; }}
  .t10-name{{ flex:1; min-width:0; }}
  .t10-sym{{ font-family:var(--mn); font-weight:900; font-size:16px; color:var(--br); letter-spacing:.5px; }}
  .t10-xrp-tag{{ font-size:9px; font-weight:800; letter-spacing:1px; color:var(--hdr); border:1px solid var(--hdr);
    border-radius:4px; padding:1px 5px; margin-left:4px; vertical-align:middle; }}
  .t10-full{{ font-size:12px; color:var(--tx); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
  .t10-cat{{ font-size:10px; font-weight:800; letter-spacing:.5px; text-transform:uppercase; border:1px solid;
    border-radius:20px; padding:3px 9px; white-space:nowrap; flex-shrink:0; }}
  .t10-price-row{{ display:flex; align-items:baseline; justify-content:space-between; margin-bottom:10px;
    padding-bottom:10px; border-bottom:1px solid var(--b); }}
  .t10-price{{ font-family:var(--mn); font-weight:900; font-size:20px; color:#fff; }}
  .t10-chg{{ font-family:var(--mn); font-weight:800; font-size:14px; white-space:nowrap; }}
  .t10-chg-lbl{{ font-size:10px; color:var(--tx); font-weight:600; }}
  .t10-grid{{ display:grid; grid-template-columns:1fr 1fr; gap:7px 12px; }}
  .t10-cell{{ display:flex; flex-direction:column; gap:1px; }}
  .t10-k{{ font-size:10.5px; color:var(--tx); text-transform:uppercase; letter-spacing:.5px; }}
  .t10-v{{ font-family:var(--mn); font-size:13px; font-weight:700; color:var(--br); }}
  .t10-supply-track{{ height:5px; background:var(--s2); border-radius:3px; overflow:hidden; margin-top:12px; }}
  .t10-supply-fill{{ height:100%; }}
  .t10-supply-lbl{{ font-size:10.5px; color:var(--tx); margin-top:4px; font-family:var(--mn); }}
  .t10-foot{{ font-size:11px; color:var(--tx); font-style:italic; margin-top:14px; }}
  @media(max-width:900px){{ .t10-grid-outer{{ grid-template-columns:1fr; }} }}

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
        <a href="https://xrpcompleteblog.com" target="_blank" rel="noopener" style="display:block;width:430px;height:70px">
          <img src="/blog_ad.png?v={APP_VERSION}" alt="XRP Complete Blog" style="display:block;width:430px;height:70px;object-fit:contain">
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

    _B['propfeed'] = f"""    <!-- SECTION 32: PROPRIETARY / OFFICIAL SOURCE FEED (V136) -->
    <div class="acct" style="border-color:rgba(0,229,204,.35);margin:10px 0">
      <div class="sec-title" style="color:var(--tq)"><span class="sic">\U0001F6F0\uFE0F</span> Proprietary &amp; Official Sources</div>
      <div class="trk-tag" style="color:var(--tx)">Straight from the organisations that build XRP and the XRP Ledger. These stories already arrive through the site's existing news cycle \u2014 this is a filtered view of that pool, so it adds no extra requests and no additional load or failure points.</div>
      <div class="intel-sub">First-party publications \u2014 {pf_nf} in this cycle</div>
      <div style="font-size:11.5px;color:var(--tx);margin:-3px 0 8px">Published by Ripple and XRPL.org themselves.</div>
      {pf_first}
      <div class="intel-sub">Official figures in the press \u2014 {pf_nc} in this cycle</div>
      <div style="font-size:11.5px;color:var(--tx);margin:-3px 0 8px">Independent reporting <em>about</em> Ripple leadership and the Foundation \u2014 not first-party material, and labelled separately so the distinction stays clear.</div>
      {pf_cover}
      <div class="intel-sub">Official source directory</div>
      <div style="font-size:11.5px;color:var(--tx);margin:-3px 0 8px">Entries marked LIVE are polled continuously by this site. The rest publish no usable public feed, so they are linked for reference only \u2014 never scraped.</div>
      {pf_dir}
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
          <div class="rail-row"><span class="rail-k">Circulating</span><span class="rail-v" style="color:var(--gr)">~61.9B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Escrow Locked</span><span class="rail-v">~38.2B XRP</span></div>
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
          <div class="rail-row"><span class="rail-k">Cadence</span><span class="rail-v">1st, 00:00 UTC</span></div>
          <div class="rail-row"><span class="rail-k">Locked Dec 2017</span><span class="rail-v">55B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Still Locked</span><span class="rail-v">~38.2B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Net Released</span><span class="rail-v" style="color:var(--gr)">~16.8B XRP</span></div>
          <div class="rail-row"><span class="rail-k">Share of Supply</span><span class="rail-v">~38%</span></div>
          <div class="rail-row"><span class="rail-k">Escrow Drawn</span><span class="rail-v" style="color:var(--bl)">~31%</span></div>
          <div class="rail-row"><span class="rail-k">Unused Portion</span><span class="rail-v">Re-escrowed</span></div>
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
        Fresh deals appear first under <a href="/#newdeals" style="color:var(--hdr)">New Partnerships &amp; Deals \u2014 This Week</a>
        on the Main page and roll into this permanent directory once they pass seven days. Both views read the same ledger,
        so nothing is copied, moved or lost in the handover \u2014 and no entry is ever added by hand.
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
                  <span>Total in escrow</span><span style="color:var(--br);font-weight:700">~38.2B XRP</span>
                </div>
                <div style="display:flex;justify-content:space-between;font-size:12px;color:var(--tx);margin-top:4px">
                  <span>Circulating supply</span><span style="color:var(--br);font-weight:700">~61.9B XRP</span>
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
    <div id="regledger" class="acct" style="border-color:rgba(0,229,204,.4);margin:10px 0">
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

    _B['regnav'] = f"""    <!-- SECTION 33: REGULATORY -> MAIN QUICK MARKERS (V137) -->
    <div class="srow srow-2" style="margin:10px 0 14px">
      <a class="si nav-marker" href="/#regradar">
        <span><span class="sic" style="font-size:17px">\U0001F4E1</span> <b style="color:var(--br)">Regulatory Radar</b><br><span style="font-size:12px;color:var(--tx)">Live regulatory signal tracking \u2014 on Main</span></span>
        <span style="color:var(--hdr);font-weight:800">&rarr;</span>
      </a>
      <a class="si nav-marker" href="/#regledger">
        <span><span class="sic" style="font-size:17px">\U0001F4DC</span> <b style="color:var(--br)">Regulatory &amp; Ledger Watch</b><br><span style="font-size:12px;color:var(--tx)">Rule changes &amp; ledger governance \u2014 on Main</span></span>
        <span style="color:var(--hdr);font-weight:800">&rarr;</span>
      </a>
    </div>

"""

    _B['regnew'] = f"""  <!-- V119: SIX REGULATORY SECTIONS -->
    {_regnew}

"""

    _B['about'] = f"""    <div class="acct" style="border-color:rgba(3,177,252,.35);margin:10px 0">
      <div class="about-body">

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
    Operating XRPComplete.com and XRPCompleteBlog.com<br>
    Email: <a href="mailto:redrioventures@gmail.com" style="color:var(--hdr);font-weight:700">redrioventures@gmail.com</a></p>
  </div>

  <div class="fine-print">
    &copy; 2026 XRP Complete / Red Rio Ventures, LLC. All rights reserved globally. XRP Complete is an independent
    informational service and is not affiliated with, endorsed by, or sponsored by Ripple Labs Inc.
    or the XRP Ledger Foundation. XRP and related marks are property of their respective owners.
  </div>

      </div>
    </div>

"""

    _B['memes'] = f"""    <!-- SECTION 34: COMMUNITY MEME WALL (V138) -->
    <div class="acct" style="border-color:rgba(224,68,124,.35);margin:10px 0">
      <div class="sec-title" style="color:#E0447C"><span class="sic">\U0001F5BC\uFE0F</span> XRP Meme Wall</div>
      <div class="trk-tag" style="color:var(--tx)">The lighter side of the ledger \u2014 community memes, hand-picked. {meme_count} on the wall.</div>
      {meme_html}
    </div>

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

    _B['top10'] = f"""    <!-- SECTION 32: TOP 10 CRYPTOCURRENCIES (V149) -->
    <div class="acct" style="border-color:rgba(255,153,0,.4);margin:10px 0">
      <div class="sec-title" style="color:var(--hdr)"><span class="sic">&#127942;</span> Top 10 Cryptocurrencies</div>
      <div class="trk-tag" style="color:var(--tx)">Checked and ranked live by market capitalization, categorized by role, with ten data points per asset \u2014 price, market cap, volume, 1h/24h/7d change, circulating and max supply, all-time high, distance from ATH, and top-10 dominance share.</div>
      {top10_html}
    </div>

"""

    _ORDER = {'main': ['status', 'liquidity', 'onchain', 'ecosystem', 'mainstream', 'instpart', 'tradfi', 'brief', 'clocks', 'competitive', 'regradar', 'clarity', 'newdeals', 'advmetrics', 'regledger'], 'markets': ['tradinghub', 'rsi', 'chart', 'analytics', 'longitudinal', 'practical', 'dca', 'hist30', 'top10'], 'institutional': ['propfeed', 'enterprise', 'execdev', 'exclusive'], 'news': ['newsnav', 'top20', 'usintel', 'regdisc', 'heatmap', 'nmv', 'newsfeed', 'sentiment'], 'community': ['scoreboard', 'leaderboard', 'unique', 'community', 'memes'], 'about': ['about'], 'regulatory': ['regnav', 'regnew']}

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


@app.route("/meme/<mid>.png")
def meme_png(mid):
    for mm in MEMES:
        if mm["id"] == mid:
            try:
                data = base64.b64decode(mm["b64"])
            except Exception:
                abort(404)
            resp = Response(data, mimetype="image/png")
            resp.headers["Cache-Control"] = "public, max-age=604800"
            return resp
    abort(404)


@app.route("/blog_ad.png")
def blog_ad_png():
    """Header blog advertisement (V123), served as embedded."""
    return Response(BLOG_AD_BYTES, mimetype="image/png",
                    headers={"Cache-Control": "public, max-age=86400"})


@app.route("/about")
def about_us():
    return Response(replace_flags_with_svg(render_page("about")), mimetype="text/html")


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
_COPYRIGHT_ARCHIVE_FILE_D = "copyright_archive_2026_07_26_d.html"

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


@app.route("/copyright7_26_d")
def copyright_archive_2026_07_26_d():
    # Fourth, independent dated snapshot (captured 2026-07-26, V139) — the first
    # documenting the six-page architecture rather than the original single-page
    # site. The three earlier snapshots (2026-07-04, 2026-07-07, 2026-07-12) are
    # untouched and remain the earliest dated proofs of authorship. Like those,
    # this route is frozen: it is served verbatim from disk, never regenerated,
    # never edited and never deleted.
    try:
        with open(_COPYRIGHT_ARCHIVE_FILE_D, "r", encoding="utf-8") as f:
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
        "Disallow: /copyright7_26_d\n"
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
    fetch_top10()
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
