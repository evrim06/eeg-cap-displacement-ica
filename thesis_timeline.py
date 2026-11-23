import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# ---- Phases shown as column titles -------------------------------------
PHASES = ["Pre-thesis", "Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]

# ---- Colours: one per kind of work (checked for colour-blind safety) ----
COLORS = {
    "Preparation": "#1A9BD0",
    "Data and analysis": "#2F5C9E",
    "Writing": "#C9692A",
}

# ---- Tasks: (label, start, end, kind) ----------------------------------
TASKS = [
    ("Code fixes, diagnose failed reconstructions", 0.00, 0.25, "Preparation"),
    ("Recording protocol on the phantom",           0.25, 0.50, "Preparation"),
    ("64-channel pilot (1 participant, 10 videos)", 0.50, 1.00, "Preparation"),
    ("YOLO retraining",                             1.00, 1.75, "Preparation"),
    ("Trial of the induced shift",                  1.75, 2.00, "Preparation"),
    ("Recording sessions",                          2.00, 4.00, "Data and analysis"),
    ("Processing videos and EEG",                   2.00, 4.25, "Data and analysis"),
    ("Validation analysis",                         4.00, 5.00, "Data and analysis"),
    ("ICA analysis",                                5.00, 6.00, "Data and analysis"),
    ("Writing introduction and methods",            2.50, 4.00, "Writing"),
    ("Writing results and discussion",              5.00, 6.50, "Writing"),
    ("Revisions",                                   6.50, 7.00, "Writing"),
]

# ---- Milestones: (label, position) -------------------------------------
MILESTONES = [
    ("Pipeline frozen", 2.0),
    ("Submission", 7.0),
]

# ---- Look ---------------------------------------------------------------
INK, MUTED, GRID = "#1F2933", "#5B6672", "#E3E6EA"
SURFACE, BAND = "#FCFCFB", "#F2F4F6"
FONT = "DejaVu Sans"  # change to "Arial" to match the university template

plt.rcParams["font.family"] = FONT
fig, ax = plt.subplots(figsize=(13.33, 7.5), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

n = len(TASKS)
row_h, bar_h = 1.0, 0.56

# alternating column bands, one per phase
for i, _ in enumerate(PHASES):
    if i % 2 == 0:
        ax.axvspan(i, i + 1, color=BAND, zorder=0, lw=0)
    ax.axvline(i, color=GRID, lw=1, zorder=1)
ax.axvline(len(PHASES), color=GRID, lw=1, zorder=1)

# bars
for row, (label, start, end, kind) in enumerate(TASKS):
    y = n - 1 - row
    ax.add_patch(FancyBboxPatch(
        (start + 0.03, y - bar_h / 2), (end - start) - 0.06, bar_h,
        boxstyle="round,pad=0,rounding_size=0.08",
        facecolor=COLORS[kind], edgecolor="none", zorder=3,
        mutation_aspect=1 / 6))
    ax.text(-0.08, y, label, ha="right", va="center", fontsize=12, color=INK)

# milestones: diamond plus a dashed line down the rows
for label, x in MILESTONES:
    ax.plot([x, x], [-0.7, n - 0.4], ls=(0, (4, 4)), lw=1.2, color=INK, zorder=2)
    ax.plot(x, -0.75, marker="D", markersize=10, color=INK, zorder=4, clip_on=False,
            markeredgecolor=SURFACE, markeredgewidth=2)
    ax.text(x, -1.25, label, ha="center", va="top", fontsize=11, color=INK,
            fontweight="bold", clip_on=False)

# phase titles on top
for i, name in enumerate(PHASES):
    ax.text(i + 0.5, n - 0.1, name, ha="center", va="bottom", fontsize=13,
            fontweight="bold", color=INK)

# legend (identity is never colour alone: the legend names each kind)
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in COLORS.values()]
ax.legend(handles, COLORS.keys(), loc="upper left", bbox_to_anchor=(0, -0.02),
          ncol=len(COLORS), frameon=False, fontsize=12, handlelength=1.2,
          labelcolor=MUTED)

ax.set_xlim(0, len(PHASES))
ax.set_ylim(-1.9, n + 0.5)
ax.axis("off")
plt.subplots_adjust(left=0.30, right=0.93, top=0.95, bottom=0.10)
fig.savefig("thesis_timeline.png", facecolor=SURFACE)
print("Saved thesis_timeline.png")