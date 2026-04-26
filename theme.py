

# color palette
BACKGROUND     = "#FAF7F2"
SURFACE        = "#F0EBE3"
TEXT_PRIMARY   = "#1A1A2E"
TEXT_SECONDARY = "#5A5A72"
NAVY           = "#1A3A5C"
GOLD           = "#C9A84C"
RED            = "#C0392B"
GREEN          = "#2D6A4F"
GRAY           = "#9B9B9B"
WHITE          = "#FFFFFF"

CONF_COLORS = {
    "SEC":               "#C9A84C",
    "Big Ten":           "#1A3A5C",
    "ACC":               "#C0392B",
    "Pac-12":            "#2D6A4F",
    "Big 12":            "#6B3FA0",
    "Mountain West":     "#E07B39",
    "American Athletic": "#2980B9",
    "Conference USA":    "#7F8C8D",
    "Mid-American":      "#8B6914",
    "Sun Belt":          "#16A085",
    "FBS Independents":  "#2C3E50",
}

FONT_TITLE = "Georgia"
FONT_BODY  = "Helvetica Neue"

# matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

def set_mpl_theme():
    mpl.rcParams.update({
        "figure.facecolor":     BACKGROUND,
        "figure.edgecolor":     BACKGROUND,
        "figure.dpi":           150,
        "axes.facecolor":       BACKGROUND,
        "axes.edgecolor":       TEXT_SECONDARY,
        "axes.labelcolor":      TEXT_PRIMARY,
        "axes.titlecolor":      TEXT_PRIMARY,
        "axes.titlesize":       14,
        "axes.titleweight":     "bold",
        "axes.titlepad":        12,
        "axes.labelsize":       11,
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        "axes.grid":            True,
        "axes.axisbelow":       True,
        "grid.color":           SURFACE,
        "grid.linewidth":       1.0,
        "grid.alpha":           0.8,
        "xtick.color":          TEXT_SECONDARY,
        "ytick.color":          TEXT_SECONDARY,
        "xtick.labelsize":      10,
        "ytick.labelsize":      10,
        "legend.frameon":       True,
        "legend.framealpha":    0.9,
        "legend.facecolor":     BACKGROUND,
        "legend.edgecolor":     SURFACE,
        "legend.fontsize":      10,
        "lines.linewidth":      2.0,
        "lines.markersize":     6,
        "font.family":          "sans-serif",
        "font.sans-serif":      ["Helvetica Neue", "Arial", "sans-serif"],
        "axes.prop_cycle": mpl.cycler(color=[
            NAVY, GOLD, RED, GREEN, "#6B3FA0", "#E07B39", "#2980B9"
        ]),
    })

# plotly
import plotly.graph_objects as go
import plotly.io as pio

def register_plotly_theme():
    pio.templates["bdt"] = go.layout.Template(
        layout=go.Layout(
            paper_bgcolor=BACKGROUND,
            plot_bgcolor=BACKGROUND,
            font=dict(
                family="Helvetica Neue, Arial, sans-serif",
                color=TEXT_PRIMARY,
                size=12
            ),
            title=dict(
                font=dict(family="Georgia, serif", size=20, color=TEXT_PRIMARY),
                x=0.05,
                xanchor="left"
            ),
            xaxis=dict(
                gridcolor=SURFACE,
                linecolor=TEXT_SECONDARY,
                tickfont=dict(size=10, color=TEXT_SECONDARY),
                title_font=dict(size=12, color=TEXT_PRIMARY),
                showgrid=True,
                zeroline=False,
            ),
            yaxis=dict(
                gridcolor=SURFACE,
                linecolor=TEXT_SECONDARY,
                tickfont=dict(size=10, color=TEXT_SECONDARY),
                title_font=dict(size=12, color=TEXT_PRIMARY),
                showgrid=True,
                zeroline=False,
            ),
            legend=dict(
                bgcolor=BACKGROUND,
                bordercolor=SURFACE,
                borderwidth=1,
                font=dict(size=11, color=TEXT_PRIMARY),
            ),
            colorway=[NAVY, GOLD, RED, GREEN, "#6B3FA0", "#E07B39", "#2980B9"],
            hoverlabel=dict(
                bgcolor=WHITE,
                bordercolor=SURFACE,
                font=dict(size=12, family="Helvetica Neue, Arial"),
            ),
            margin=dict(t=80, r=30, b=60, l=60),
        )
    )
    pio.templates.default = "bdt"

# altair
def bdt_altair_theme():
    return {
        "config": {
            "background": BACKGROUND,
            "view": {"fill": BACKGROUND, "stroke": "transparent"},
            "title": {
                "font": "Georgia, serif",
                "fontSize": 18,
                "fontWeight": "bold",
                "color": TEXT_PRIMARY,
                "anchor": "start",
                "offset": 10,
            },
            "axis": {
                "labelFont": "Helvetica Neue, Arial, sans-serif",
                "labelFontSize": 10,
                "labelColor": TEXT_SECONDARY,
                "titleFont": "Helvetica Neue, Arial, sans-serif",
                "titleFontSize": 12,
                "titleColor": TEXT_PRIMARY,
                "gridColor": SURFACE,
                "gridOpacity": 0.8,
                "domainColor": TEXT_SECONDARY,
                "tickColor": TEXT_SECONDARY,
            },
            "legend": {
                "labelFont": "Helvetica Neue, Arial, sans-serif",
                "labelFontSize": 11,
                "labelColor": TEXT_PRIMARY,
                "titleFont": "Helvetica Neue, Arial, sans-serif",
                "titleFontSize": 12,
                "titleColor": TEXT_PRIMARY,
            },
            "range": {
                "category": [NAVY, GOLD, RED, GREEN,
                             "#6B3FA0", "#E07B39", "#2980B9"],
            },
            "mark":  {"color": NAVY},
            "bar":   {"fill": NAVY},
            "line":  {"color": NAVY, "strokeWidth": 2},
            "point": {"color": NAVY, "size": 60, "opacity": 0.8},
        }
    }

# signature
def add_signature(ax, text="The Billion Dollar Teenagers"):
    ax.annotate(
        text,
        xy=(1, -0.08), xycoords="axes fraction",
        ha="right", fontsize=8,
        color=TEXT_SECONDARY, style="italic"
    )

def format_title(ax, title, subtitle=None):
    ax.set_title(title, fontsize=14, fontweight="bold",
                 color=TEXT_PRIMARY, pad=12, loc="left",
                 fontfamily="Georgia")
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes,
                fontsize=10, color=TEXT_SECONDARY)

# activate all
def activate_all():
    set_mpl_theme()
    register_plotly_theme()
    try:
        import altair as alt
        alt.themes.register("bdt", bdt_altair_theme)
        alt.themes.enable("bdt")
    except ImportError:
        print("Altair not available — skipping")
    print("BDT theme activated")
