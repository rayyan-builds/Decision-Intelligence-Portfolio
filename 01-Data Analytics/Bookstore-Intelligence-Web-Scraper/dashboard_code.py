"""
Bookstore Intelligence - dark project dashboard (LinkedIn / GitHub portfolio image).

Self-contained: reads the project CSV files from the same folder (or a folder
passed as the first argument), recomputes every figure, re-runs the 0/1 knapsack
for the CEO challenge, and renders a 3840 x 2160 PNG.

Usage:  python make_dashboard.py [data_folder] [output.png]
Needs:  pandas, numpy, matplotlib   (font "Inter" is used if installed)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch

DATA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else DATA / "bookstore_intelligence_dashboard.png"
REPO_URL = ("https://github.com/rayyan-builds/Decision-Intelligence-Portfolio/tree/main/"
            "01-Data%20Analytics/Bookstore-Intelligence-Web-Scraper")

# ----------------------------------------------------------------- palette
BG, PANEL, PANEL2, BORDER = "#0B1220", "#151F32", "#1B2740", "#26364F"
TEAL, BLUE, VIOLET, EMERALD = "#2DD4BF", "#60A5FA", "#A78BFA", "#34D399"
TXT, TXT2, DIM = "#F3F4F6", "#9CA3AF", "#6B7A90"
RAMP = ["#4F6F9F", "#5A86B4", "#4D9BB8", "#2FB5B0", "#2DD4BF"]   # muted blue -> teal

names = {f.name for f in font_manager.fontManager.ttflist}
FONT = "Inter" if "Inter" in names else ("Carlito" if "Carlito" in names else "DejaVu Sans")
plt.rcParams["font.family"] = FONT

# ----------------------------------------------------------------- data (verified from files)
main = pd.read_csv(DATA / "competitor_books.csv")
full = pd.read_csv(DATA / "competitor_books_bonus.csv")
counts = pd.read_csv(DATA / "rating_counts.csv").set_index("Star Rating")["Number of Books"]

assert len(main) == 60 and len(full) == 1000
assert (full["Rating"].value_counts().reindex([1, 2, 3, 4, 5]).values == counts.values).all()

pages_main, pages_full = len(main) // 20, len(full) // 20
avg_price = main["Price"].mean()
hi = main.nlargest(3, "Price")
lo = main.nsmallest(3, "Price")
n5 = int((main["Rating"] == 5).sum())
instock_main = int(main["Availability"].str.contains("In stock", case=False).sum())
instock_full = int(full["Availability"].str.contains("In stock", case=False).sum())
five_cheapest = main[main["Rating"] == 5].nsmallest(5, "Price")

# CEO challenge: same 0/1 knapsack dynamic programme as the notebook
BUDGET = 10_000
ceo = main.copy()
ceo["Pence"] = (ceo["Price"] * 100).round().astype(int)
n = len(ceo)
dp = np.zeros((n + 1, BUDGET + 1), dtype=np.int32)
for i in range(1, n + 1):
    p, r = int(ceo.loc[i - 1, "Pence"]), int(ceo.loc[i - 1, "Rating"])
    dp[i] = dp[i - 1]
    dp[i, p:] = np.maximum(dp[i - 1, p:], dp[i - 1, :BUDGET - p + 1] + r)
sel, rem = [], BUDGET
for i in range(n, 0, -1):
    if dp[i, rem] != dp[i - 1, rem]:
        sel.append(i - 1)
        rem -= int(ceo.loc[i - 1, "Pence"])
basket = ceo.iloc[sorted(sel)].sort_values("Price", ascending=False)
cost = basket["Pence"].sum() / 100
score = int(basket["Rating"].sum())
left = (BUDGET - basket["Pence"].sum()) / 100
assert (len(basket), round(cost, 2), score, round(left, 2)) == (6, 96.59, 26, 3.41)

# ----------------------------------------------------------------- canvas (units = inches)
W, H = 19.2, 10.8
fig = plt.figure(figsize=(W, H), dpi=200, facecolor=BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
renderer = fig.canvas.get_renderer()


def T(x, y, s, size=13, color=TXT, weight="normal", ha="left", va="center", maxw=None, minsize=10.5, **kw):
    """Draw text; shrink (then ellipsize) so it fits maxw inches."""
    t = ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, ha=ha, va=va, **kw)
    if maxw:
        w = lambda: t.get_window_extent(renderer).width / fig.dpi
        while w() > maxw and t.get_fontsize() > minsize:
            t.set_fontsize(t.get_fontsize() - 0.25)
        while w() > maxw and len(t.get_text()) > 4:
            t.set_text(t.get_text()[:-2].rstrip() + "…")
    return t


def box(x, y, w, h, fc=PANEL, ec=BORDER, r=0.14, lw=1.1, z=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=z))


def chip(x, y, s, color, size=10.5, ha="left", h=0.27):
    t = ax.text(0, 0, s, fontsize=size, fontweight="bold")
    tw = t.get_window_extent(renderer).width / fig.dpi + 0.26
    t.remove()
    x0 = x if ha == "left" else x - tw
    box(x0, y - h / 2, tw, h, fc=color + "26", ec=color + "88", r=h / 2, lw=0.9, z=3)
    ax.text(x0 + tw / 2, y + 0.005, s, fontsize=size, color=color, fontweight="bold",
            ha="center", va="center", zorder=4)
    return tw


def ring(cx, cy, ro, ri, frac, color, track=BORDER):
    th = np.linspace(0, 2 * np.pi, 200)
    ax.add_patch(Polygon(np.r_[np.c_[cx + ro * np.cos(th), cy - ro * np.sin(th)],
                               np.c_[cx + ri * np.cos(th[::-1]), cy - ri * np.sin(th[::-1])]],
                         fc=track, ec="none", zorder=3))
    if frac <= 0:
        return
    a = np.pi / 2 - 2 * np.pi * np.linspace(0, min(frac, 0.99999), 200)
    ax.add_patch(Polygon(np.r_[np.c_[cx + ro * np.cos(a), cy - ro * np.sin(a)],
                               np.c_[cx + ri * np.cos(a[::-1]), cy - ri * np.sin(a[::-1])]],
                         fc=color, ec="none", zorder=4))


def panel_head(x, y, w, title, tag, tagcolor):
    T(x + 0.28, y + 0.4, title, 17, TXT, "bold", zorder=5)
    chip(x + w - 0.25, y + 0.4, tag, tagcolor, ha="right")


MAIN_TAG, FULL_TAG = "60-BOOK DATASET", "FULL CATALOGUE · 1,000 BOOKS"

# ----------------------------------------------------------------- header
ax.add_patch(Rectangle((0.5, 0.42), 0.09, 1.2, fc=TEAL, ec="none"))
T(0.78, 0.74, "BOOKSTORE INTELLIGENCE", 40, TXT, "bold")
T(0.78, 1.22, "Web Scraping  |  Retail Analytics  |  Data-Driven Decisions", 17, TEAL, "bold")
T(0.78, 1.58, "Turning raw online catalogue data into structured insights and budget-aware decisions.", 14, TXT2)

badges = ["Python", "Requests", "BeautifulSoup", "Pandas", "Matplotlib", "Jupyter Notebook"]
bcol = [BLUE, TEAL, VIOLET, BLUE, TEAL, VIOLET]
for row, (lo_i, y) in enumerate([(0, 0.82), (3, 1.32)]):
    xr = 18.7
    for s, c in list(zip(badges, bcol))[lo_i:lo_i + 3][::-1]:
        tw = chip(xr, y, s, c, size=13, ha="right", h=0.4)
        xr -= tw + 0.16

# ----------------------------------------------------------------- KPI row
ky, kh, kg = 1.85, 1.1, 0.2
kw = (18.2 - 5 * kg) / 6
kpis = [
    ("60", "Books scraped · 3 pages", MAIN_TAG, TEAL),
    ("1,000", "Books scraped · 50 pages", "FULL CATALOGUE", VIOLET),
    (f"£{avg_price:.2f}", "Average book price", MAIN_TAG, TEAL),
    (f"£{main['Price'].max():.2f}", "Most expensive book", MAIN_TAG, TEAL),
    (f"£{main['Price'].min():.2f}", "Cheapest book", MAIN_TAG, TEAL),
    (f"{n5}  ({n5 / len(main):.1%})", "Five-star books", MAIN_TAG, TEAL),
]
for i, (v, lab, tag, c) in enumerate(kpis):
    x = 0.5 + i * (kw + kg)
    box(x, ky, kw, kh)
    ax.add_patch(Rectangle((x + 0.001, ky + 0.2), 0.06, kh - 0.4, fc=c, ec="none", zorder=3))
    T(x + 0.28, ky + 0.36, v, 27, TXT, "bold", maxw=kw - 0.4)
    T(x + 0.28, ky + 0.7, lab, 12.5, TXT2, maxw=kw - 0.4)
    T(x + 0.28, ky + 0.96, tag, 9.5, c, "bold", maxw=kw - 0.4, minsize=8.5)

# ----------------------------------------------------------------- A: rating distribution
ay, ah = 3.12, 3.2
ax_, aw = 0.5, 6.9
box(ax_, ay, aw, ah)
panel_head(ax_, ay, aw, "Rating Distribution", FULL_TAG, VIOLET)
base, maxh, cw = ay + 2.28, 1.1, 0.74
vmax = counts.max()
slot = (aw - 0.8) / 5
ax.plot([ax_ + 0.4, ax_ + aw - 0.4], [base, base], color=BORDER, lw=1, zorder=2)
for i, (star, v) in enumerate(counts.items()):
    cx = ax_ + 0.4 + slot * (i + 0.5)
    hh = maxh * v / vmax
    ax.add_patch(FancyBboxPatch((cx - cw / 2, base - hh), cw, hh, boxstyle="round,pad=0,rounding_size=0.05",
                                fc=RAMP[i], ec="none", zorder=3))
    T(cx, base - hh - 0.17, f"{v}", 15, TXT, "bold", ha="center")
    T(cx, base + 0.2, f"{star} ★", 12.5, TXT2, ha="center")
pct = counts / counts.sum()
T(ax_ + 0.28, ay + 2.78, f"Fairly even spread: each rating level holds {pct.min():.1%} to {pct.max():.1%} of the 1,000 books.",
  12.5, TXT, maxw=aw - 0.5)
T(ax_ + 0.28, ay + 3.06, "Ratings are randomly assigned on Books to Scrape, so they do not reflect real customer sentiment.",
  11.5, VIOLET, maxw=aw - 0.5, minsize=9.5)

# ----------------------------------------------------------------- B: price analysis
bx, bw = ax_ + aw + 0.25, 6.3
box(bx, ay, bw, ah)
panel_head(bx, ay, bw, "Price Analysis", MAIN_TAG, TEAL)
label_w, bar0, bar_w = 2.8, bx + 3.3, 2.0
scale = bar_w / 60.0
ax.plot([bar0 + avg_price * scale] * 2, [ay + 1.1, ay + 2.9], color=TXT2, lw=1.2, ls=(0, (4, 3)), zorder=2)
T(bar0 + avg_price * scale, ay + 0.88, f"avg £{avg_price:.2f}", 11, TXT2, ha="center", weight="bold")
# legend
lx0 = bx + 0.28
for lab, col in [("Highest priced", BLUE), ("Lowest priced", TEAL)]:
    ax.add_patch(FancyBboxPatch((lx0, ay + 0.8), 0.16, 0.16, boxstyle="round,pad=0,rounding_size=0.03", fc=col, ec="none"))
    tt = T(lx0 + 0.24, ay + 0.88, lab, 11, TXT2)
    lx0 += 0.24 + tt.get_window_extent(renderer).width / fig.dpi + 0.3
yy = ay + 1.25
for df, col in [(hi, BLUE), (lo, TEAL)]:
    for _, r in df.iterrows():
        T(bx + 0.28, yy, r["Title"], 12.5, TXT, maxw=label_w + 0.1, minsize=12.5)
        bw_ = r["Price"] * scale
        ax.add_patch(FancyBboxPatch((bar0, yy - 0.09), bw_, 0.18, boxstyle="round,pad=0,rounding_size=0.04",
                                    fc=col, ec="none", zorder=3))
        T(bar0 + bw_ + 0.1, yy, f"£{r['Price']:.2f}", 12.5, TXT, "bold", zorder=5,
          path_effects=[pe.withStroke(linewidth=5, foreground=PANEL)])
        yy += 0.27
    yy += 0.1
T(bx + 0.28, ay + 3.06, f"Prices range £{main['Price'].min():.2f} to £{main['Price'].max():.2f} across the 60 books.",
  11.5, TXT2, maxw=bw - 0.5)

# ----------------------------------------------------------------- C: availability
cx0 = bx + bw + 0.25
cw_ = 18.7 - cx0
box(cx0, ay, cw_, ah)
T(cx0 + 0.28, ay + 0.4, "Availability", 17, TXT, "bold")
dcx, dcy = cx0 + 1.25, ay + 1.62
ring(dcx, dcy, 0.82, 0.6, instock_main / len(main), EMERALD)
T(dcx, dcy - 0.06, f"{instock_main / len(main):.0%}", 24, TXT, "bold", ha="center")
T(dcx, dcy + 0.27, "in stock", 11.5, TXT2, ha="center")
sx = cx0 + 2.45
T(sx, ay + 1.2, f"{instock_main} of {len(main)}", 20, TXT, "bold", maxw=cw_ - 2.6)
T(sx, ay + 1.5, "60-book dataset", 11.5, TEAL, "bold")
T(sx, ay + 1.95, f"{instock_full:,} of {len(full):,}", 20, TXT, "bold", maxw=cw_ - 2.6)
T(sx, ay + 2.25, "full catalogue", 11.5, VIOLET, "bold")
T(cx0 + 0.28, ay + 2.78, "Every listed book shows as in stock.", 12, TXT, maxw=cw_ - 0.5)
T(cx0 + 0.28, ay + 3.06, "Availability does not indicate sales or demand.", 11.5, TXT2, maxw=cw_ - 0.5)

# ----------------------------------------------------------------- D: five-star shortlist
dy, dh, dw = 6.52, 3.0, 8.0
box(0.5, dy, dw, dh)
panel_head(0.5, dy, dw, "Five-Star Shortlist", MAIN_TAG, TEAL)
T(0.78, dy + 0.78, f"Five cheapest of the {n5} five-star books  ·  ranked by price", 12, TXT2)
lab_w, b0, bws = 4.4, 0.5 + 5.0, 2.1
sc = bws / 30.0
yy = dy + 1.2
for k, (_, r) in enumerate(five_cheapest.iterrows(), 1):
    T(0.78, yy, f"{k}", 12.5, TEAL, "bold")
    T(1.1, yy, r["Title"], 12.5, TXT, maxw=lab_w - 0.5, minsize=12.5)
    ax.add_patch(FancyBboxPatch((b0, yy - 0.09), r["Price"] * sc, 0.18, boxstyle="round,pad=0,rounding_size=0.04",
                                fc=RAMP[k - 1] if k < 5 else TEAL, ec="none", zorder=3))
    T(b0 + r["Price"] * sc + 0.1, yy, f"£{r['Price']:.2f}", 12.5, TXT, "bold")
    yy += 0.3
T(0.78, dy + 2.7, f"All rated 5 stars and priced well below the 60-book average of £{avg_price:.2f}.", 11.5, TXT2, maxw=dw - 0.5)

# ----------------------------------------------------------------- E: CEO challenge
ex, ew = 0.5 + dw + 0.25, 18.7 - (0.5 + dw + 0.25)
box(ex, dy, ew, dh)
panel_head(ex, dy, ew, "£100 CEO Budget Challenge", MAIN_TAG, TEAL)
chip(ex + 0.28, dy + 0.82, "0/1 KNAPSACK OPTIMISATION — DYNAMIC PROGRAMMING", VIOLET, size=10)
rcx, rcy = ex + 1.2, dy + 1.85
ring(rcx, rcy, 0.74, 0.55, cost / 100, TEAL)
T(rcx, rcy - 0.07, f"£{cost:.2f}", 18, TXT, "bold", ha="center")
T(rcx, rcy + 0.22, "of £100", 11, TXT2, ha="center")
stats = [(f"{len(basket)}", "books selected"), (f"{score}", "total star rating"), (f"£{left:.2f}", "budget remaining")]
for i, (v, lab) in enumerate(stats):
    yy = dy + 1.4 + i * 0.5
    T(ex + 2.4, yy, v, 20, EMERALD if i == 2 else TXT, "bold")
    T(ex + 3.25, yy + 0.02, lab, 12, TXT2, maxw=1.55)
T(ex + 0.28, dy + 2.7, "Goal: maximise the combined star rating within £100, not profit.", 11.5, TXT2, maxw=4.45)

lx = ex + 5.05
ax.plot([lx - 0.2, lx - 0.2], [dy + 0.8, dy + 2.8], color=BORDER, lw=1)
T(lx, dy + 0.95, "SELECTED BASKET", 10.5, DIM, "bold")
yy = dy + 1.27
for _, r in basket.iterrows():
    T(lx, yy, r["Title"], 12.5, TXT, maxw=2.75, minsize=12.5)
    T(lx + 2.95, yy, "★" * int(r["Rating"]), 11, VIOLET, ha="left")
    T(ex + ew - 0.28, yy, f"£{r['Price']:.2f}", 12.5, TXT, "bold", ha="right")
    yy += 0.25
ax.plot([lx, ex + ew - 0.28], [yy - 0.08, yy - 0.08], color=BORDER, lw=1)
T(lx, yy + 0.1, "Total basket", 12.5, TXT2, "bold")
T(ex + ew - 0.28, yy + 0.1, f"£{cost:.2f}", 13, TEAL, "bold", ha="right")

# ----------------------------------------------------------------- pipeline strip
py, ph = 9.64, 0.48
steps = ["Website", "HTML Extraction", "Cleaning & Structuring", "Exploratory Analysis", "Visualisation", "Budget Optimisation"]
gap = 0.34
sw = (18.2 - gap * 5) / 6
for i, s in enumerate(steps):
    x = 0.5 + i * (sw + gap)
    box(x, py, sw, ph, fc=PANEL2, r=ph / 2)
    ax.add_patch(plt.Circle((x + 0.3, py + ph / 2), 0.15, fc=TEAL if i % 2 == 0 else BLUE, ec="none", zorder=3))
    T(x + 0.3, py + ph / 2 + 0.01, str(i + 1), 11, BG, "bold", ha="center", zorder=4)
    T(x + 0.56, py + ph / 2, s, 13, TXT, "bold", maxw=sw - 0.7, minsize=10)
    if i < 5:
        ax.add_patch(FancyArrowPatch((x + sw + 0.05, py + ph / 2), (x + sw + gap - 0.05, py + ph / 2),
                                     arrowstyle="-|>", mutation_scale=11, color=DIM, lw=1.3))

# ----------------------------------------------------------------- footer
T(0.5, 10.4, "Rayyan Asim  |  BS Business Analytics  |  FAST-NUCES Islamabad", 14, TXT, "bold")
T(0.5, 10.65, "Explore the notebook, datasets and analysis on GitHub.", 11.5, TXT2)
T(18.7, 10.4, "Practice dataset from books.toscrape.com. Ratings are randomly assigned; findings show technique, not market demand.",
  10.5, DIM, ha="right", maxw=9.5, minsize=9)
T(18.7, 10.65, REPO_URL, 10.5, TEAL, ha="right", maxw=9.5, minsize=8.5)

fig.savefig(OUT, dpi=200, facecolor=BG)
print("saved", OUT, "| font:", FONT)