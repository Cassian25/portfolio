from pathlib import Path

from dpr_layouts import LAYOUT_CSS, build_document_body

OUTPUT_DIR = Path(__file__).parent

PAGE_WIDTH = "100%"
PAGE_MIN_HEIGHT = "340mm"
PAGE_PAD_LEFT = "4mm"
PAGE_PAD_RIGHT = "4mm"
PAGE_PAD_TOP = "6mm"
PAGE_PAD_BOTTOM = "6mm"

WHITE_SURFACE = "#ffffff"
VISIBLE_BORDER = "#cbd5e1"
READABLE_MUTED = "#475569"

READABILITY_ON_WHITE = {
    "first-design": {
        "text": "#0f172a",
        "muted": READABLE_MUTED,
        "card": "#ffffff",
        "border": VISIBLE_BORDER,
    },
    "fifth-design": {
        "text": "#0f172a",
        "muted": READABLE_MUTED,
        "card": "#ffffff",
        "border": VISIBLE_BORDER,
        "banner": "linear-gradient(135deg, #0891b2 0%, #7c3aed 100%)",
    },
}

WHITE_SURFACE_CSS = """
    body { background: #ffffff !important; background-image: none !important; color: var(--text) !important; }
    .page { background: #ffffff !important; backdrop-filter: none !important; border: 1px solid var(--border) !important; box-shadow: 0 1px 4px rgba(15,23,42,0.06) !important; }
    .page-main { background: #ffffff !important; backdrop-filter: none !important; border: 1px solid var(--border) !important; }
    .page-fill-tail { background: #f8fafc !important; border: 1px dashed var(--border) !important; }
    .delay-cards.fill-grow { background: transparent !important; }
"""

READABLE_TEXT_CSS = """
    .kpi { background: var(--card) !important; color: var(--text) !important; backdrop-filter: none !important; }
    .kpi-value, .kpi-label, .kpi-sub { color: var(--text) !important; }
    .kpi-label, .kpi-sub { opacity: 0.85 !important; color: var(--muted) !important; }
    .health-card, .panel, .delays-panel, .people-card, .delay-card, .status-item, .pulse,
    .rollup-stat, .activity-card, .mini-panel { background: var(--card) !important; backdrop-filter: none !important; }
    .delay-title, .delay-card-title, .activity-card-title, .section-name, .people-row span:last-child,
    .health-sub, .health-meta, .mini-panel, .mini-panel strong, .rollup-stat .val, tbody td,
    .empty-state, .delay-item, .health-bar-score, .health-wave-score, .health-seg-score,
    .health-orbit-score, .health-dots-score, .health-stack-score, .health-steps-score,
    .health-ticker-score, .health-spiral-wrap > span, .health-ripple-wrap > span { color: var(--text) !important; }
    .health-bar-score small, .health-wave-score small, .health-orbit-score small,
    .health-dots-score small, .health-stack-score small, .health-steps-score small,
    .health-ticker-score small, .health-spiral-wrap > span small, .health-ripple-wrap > span small,
    .kpi-label, .status-item .lbl, .status-item .pct, .pulse .lbl, .pulse .chg,
    .rollup-stat .lbl, .footer, .delay-meta, .section-meta, .people-row span:first-child,
    .page-title-row span, .activity-card-meta { color: var(--muted) !important; opacity: 1 !important; }
    .status-item .num, .pulse .val, .kpi-value { color: var(--text) !important; }
    .panel h3, .page-title-row h2 { color: var(--accent) !important; }
    .health-badge { color: #ffffff !important; }
    .alert-bar { color: var(--danger) !important; background: rgba(220,38,38,0.08) !important; border: 1px solid rgba(220,38,38,0.25) !important; border-left: 4px solid var(--danger) !important; }
    .success-box { background: rgba(22,163,74,0.08) !important; border: 1px solid rgba(22,163,74,0.35) !important; }
    .success-box, .success-box p { color: #166534 !important; opacity: 1 !important; }
    .success-box h3 { color: var(--ok) !important; opacity: 1 !important; }
    thead th { color: #ffffff !important; background: var(--accent) !important; backdrop-filter: none !important; border-bottom: 2px solid color-mix(in srgb, var(--accent) 70%, #000) !important; }
    tbody tr:nth-child(even) { background: rgba(0,0,0,0.03) !important; }
    tbody td { border-bottom: 1px solid var(--border) !important; }
"""

VISIBLE_BORDERS_CSS = """
    .kpi, .panel, .health-card, .delays-panel, .people-card, .delay-card, .status-item,
    .pulse, .rollup-stat, .activity-card, .mini-panel {
      border: 1px solid var(--border) !important;
      border-style: solid !important;
    }
    .kpi { border-top-width: 3px !important; border-top-color: var(--accent) !important; }
    .kpi.danger { border-top-color: var(--danger) !important; }
    .kpi.warn { border-top-color: var(--warn) !important; }
    .kpi.ok { border-top-color: var(--ok) !important; }
    .kpi.neutral { border-top-color: var(--muted) !important; }
    .delay-card { border-left-width: 4px !important; border-left-color: var(--warn) !important; }
    .delay-card.severe { border-left-color: var(--danger) !important; }
    .activity-card { border-left-width: 4px !important; }
    .panel h3 { border-bottom: 1px solid var(--border) !important; }
    .people-row, .delay-item { border-bottom: 1px solid var(--border) !important; }
    .footer { border-top: 1px solid var(--border) !important; }
    .health-card { border: 2px solid var(--warn) !important; }
"""


def _hex_luminance(color):
    value = (color or "").strip().lower()
    if not value.startswith("#"):
        return 1.0
    digits = value[1:]
    if len(digits) == 3:
        digits = "".join(ch * 2 for ch in digits)
    if len(digits) != 6:
        return 1.0
    red = int(digits[0:2], 16)
    green = int(digits[2:4], 16)
    blue = int(digits[4:6], 16)
    return (0.299 * red + 0.587 * green + 0.114 * blue) / 255


def _needs_dark_text(color):
    return _hex_luminance(color) > 0.65


def _needs_light_card(color):
    value = (color or "").strip().lower()
    if value.startswith("rgba") or value.startswith("linear"):
        return True
    return _hex_luminance(value) < 0.92


def _needs_visible_border(color):
    value = (color or "").strip().lower()
    if value.startswith("rgba") or value.startswith("linear"):
        return True
    return _hex_luminance(value) > 0.72


def prepare_theme(slug, theme):
    prepared = dict(theme)
    prepared["bg"] = WHITE_SURFACE
    prepared["page"] = WHITE_SURFACE
    if slug in READABILITY_ON_WHITE:
        prepared.update(READABILITY_ON_WHITE[slug])
    if _needs_dark_text(prepared.get("text", "#0f172a")):
        prepared["text"] = "#0f172a"
    prepared["muted"] = READABLE_MUTED if _hex_luminance(prepared.get("muted", READABLE_MUTED)) > 0.65 else prepared.get("muted", READABLE_MUTED)
    if _needs_light_card(prepared.get("card", "#ffffff")):
        prepared["card"] = "#ffffff"
    if _needs_visible_border(prepared.get("border", VISIBLE_BORDER)):
        prepared["border"] = VISIBLE_BORDER
    prepared["style_extra"] = (
        prepared.get("style_extra", "")
        + WHITE_SURFACE_CSS
        + READABLE_TEXT_CSS
        + VISIBLE_BORDERS_CSS
    )
    return prepared

THEMES = {
    "first-design": {
        "health_a": "#fbbf24",
        "health_b": "#818cf8",
        "name": "Midnight Executive",
        "font": "Syne:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600",
        "font_family": "'Syne', sans-serif",
        "mono": "'JetBrains Mono', monospace",
        "bg": "#0a0e17",
        "page": "#111827",
        "text": "#f1f5f9",
        "muted": "#94a3b8",
        "accent": "#38bdf8",
        "accent2": "#818cf8",
        "danger": "#f87171",
        "warn": "#fbbf24",
        "ok": "#34d399",
        "card": "#1e293b",
        "border": "#334155",
        "banner": "linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #312e81 100%)",
        "style_extra": """
          .page { box-shadow: 0 0 60px rgba(56,189,248,0.08); border: 1px solid #334155; }
          .kpi { background: linear-gradient(145deg, #1e293b, #0f172a); }
          .alert-bar { background: rgba(248,113,113,0.15); border-left-color: #f87171; color: #fecaca; }
          thead th { background: linear-gradient(90deg, #1e3a8a, #4338ca); }
          .success-box { background: rgba(52,211,153,0.12); border-color: #34d399; color: #a7f3d0; }
        """,
    },
    "second-design": {
        "health_a": "#ca8a04",
        "health_b": "#ef4444",
        "name": "Swiss Minimal",
        "font": "Inter:wght@400;500;600;700;800",
        "font_family": "'Inter', sans-serif",
        "mono": "'Inter', sans-serif",
        "bg": "#ffffff",
        "page": "#ffffff",
        "text": "#111827",
        "muted": "#6b7280",
        "accent": "#111827",
        "accent2": "#ef4444",
        "danger": "#dc2626",
        "warn": "#ca8a04",
        "ok": "#059669",
        "card": "#ffffff",
        "border": "#e5e7eb",
        "banner": "#111827",
        "style_extra": """
          .page { box-shadow: none; border: 2px solid #111827; border-radius: 0; }
          .banner { border-radius: 0; }
          .kpi { border-radius: 0; border: 2px solid #111827; border-top-width: 6px; background: #fff; }
          .panel, .health-card, .delays-panel, .people-card { border-radius: 0; border-width: 2px; }
          h1, h2, h3 { letter-spacing: -0.04em; }
          .alert-bar { border-radius: 0; background: #fef2f2; border-left-width: 8px; }
          thead th { background: #111827; border-radius: 0; }
        """,
    },
    "third-design": {
        "health_a": "#d97706",
        "health_b": "#c026d3",
        "name": "Sunset Gradient",
        "font": "Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700",
        "font_family": "'Outfit', sans-serif",
        "mono": "'Space Grotesk', sans-serif",
        "bg": "linear-gradient(160deg, #fff7ed 0%, #fce7f3 50%, #ede9fe 100%)",
        "page": "#ffffff",
        "text": "#1c1917",
        "muted": "#78716c",
        "accent": "#ea580c",
        "accent2": "#c026d3",
        "danger": "#e11d48",
        "warn": "#d97706",
        "ok": "#059669",
        "card": "#ffffff",
        "border": "#fed7aa",
        "banner": "linear-gradient(120deg, #ea580c 0%, #db2777 50%, #7c3aed 100%)",
        "style_extra": """
          body { background: linear-gradient(160deg, #fff7ed, #fce7f3, #ede9fe); background-attachment: fixed; }
          .page { box-shadow: 0 20px 60px rgba(234,88,12,0.12); border-radius: 20px; }
          .banner { border-radius: 16px; }
          .kpi { border-radius: 16px; background: linear-gradient(135deg, #fff7ed, #fff); }
          .kpi.danger { border-top-color: #e11d48; }
          .panel h3 { color: #ea580c; }
          .alert-bar { background: linear-gradient(90deg, #fff1f2, #ffe4e6); border-left-color: #e11d48; border-radius: 12px; }
          thead th { background: linear-gradient(90deg, #ea580c, #db2777); }
        """,
    },
    "fourth-design": {
        "health_a": "#d97706",
        "health_b": "#eab308",
        "name": "Construction Pro",
        "font": "Barlow+Condensed:wght@400;600;700;800&family=Barlow:wght@400;500;600;700",
        "font_family": "'Barlow', sans-serif",
        "mono": "'Barlow Condensed', sans-serif",
        "bg": "#1a1a1a",
        "page": "#f5f5f0",
        "text": "#1a1a1a",
        "muted": "#525252",
        "accent": "#f59e0b",
        "accent2": "#eab308",
        "danger": "#dc2626",
        "warn": "#d97706",
        "ok": "#16a34a",
        "card": "#ffffff",
        "border": "#d4d4d4",
        "banner": "repeating-linear-gradient(-45deg, #f59e0b, #f59e0b 12px, #1a1a1a 12px, #1a1a1a 24px)",
        "style_extra": """
          body { background: #1a1a1a; }
          .page { border-top: 8px solid #f59e0b; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
          .banner { color: #1a1a1a; border-radius: 4px; padding: 18px; }
          .banner-left h1 { text-transform: uppercase; font-family: 'Barlow Condensed', sans-serif; font-size: 28px; }
          .kpi { border-left: 4px solid #f59e0b; border-top: none; border-radius: 4px; }
          .alert-bar { background: #fef3c7; border-left: 6px solid #dc2626; color: #92400e; font-family: 'Barlow Condensed', sans-serif; font-size: 13px; text-transform: uppercase; }
          thead th { background: #1a1a1a; text-transform: uppercase; font-family: 'Barlow Condensed', sans-serif; letter-spacing: 0.1em; }
          .delay-badge.critical { background: #dc2626; }
          .panel h3 { color: #1a1a1a; font-family: 'Barlow Condensed', sans-serif; text-transform: uppercase; }
        """,
    },
    "fifth-design": {
        "health_a": "#fcd34d",
        "health_b": "#a78bfa",
        "name": "Glass Aurora",
        "font": "Plus+Jakarta+Sans:wght@400;500;600;700;800",
        "font_family": "'Plus Jakarta Sans', sans-serif",
        "mono": "'Plus Jakarta Sans', sans-serif",
        "bg": "#0c1222",
        "page": "rgba(255,255,255,0.06)",
        "text": "#f8fafc",
        "muted": "#94a3b8",
        "accent": "#22d3ee",
        "accent2": "#a78bfa",
        "danger": "#fb7185",
        "warn": "#fcd34d",
        "ok": "#4ade80",
        "card": "rgba(255,255,255,0.08)",
        "border": "rgba(255,255,255,0.15)",
        "banner": "linear-gradient(135deg, rgba(34,211,238,0.25), rgba(167,139,250,0.25))",
        "style_extra": """
          body { background: radial-gradient(ellipse at 20% 20%, #1e1b4b, #0c1222 60%), radial-gradient(ellipse at 80% 80%, #164e63, transparent 50%); background-attachment: fixed; }
          .page { backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.12); border-radius: 24px; box-shadow: 0 25px 50px rgba(0,0,0,0.4); }
          .banner { backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.2); border-radius: 16px; }
          .kpi, .panel, .health-card, .delays-panel, .people-card, .delay-card, .pulse, .status-item { backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.12); border-radius: 16px; }
          .alert-bar { background: rgba(251,113,133,0.15); border-left-color: #fb7185; color: #fecdd3; border-radius: 12px; }
          thead th { background: rgba(34,211,238,0.2); backdrop-filter: blur(8px); }
          tbody tr:nth-child(even) { background: rgba(255,255,255,0.03); }
          .success-box { background: rgba(74,222,128,0.12); border-color: rgba(74,222,128,0.4); color: #bbf7d0; }
        """,
    },
    "sixth-design": {
        "health_a": "#f4a261",
        "health_b": "#7209b7",
        "name": "Infographic Dash",
        "font": "Manrope:wght@400;500;600;700;800",
        "font_family": "'Manrope', sans-serif",
        "mono": "'Manrope', sans-serif",
        "bg": "#f0f4f8",
        "page": "#ffffff",
        "text": "#0d1b2a",
        "muted": "#5c677d",
        "accent": "#0066cc",
        "accent2": "#7209b7",
        "danger": "#e63946",
        "warn": "#f4a261",
        "ok": "#2a9d8f",
        "card": "#ffffff",
        "border": "#dee2e6",
        "banner": "linear-gradient(90deg, #0066cc, #7209b7)",
        "style_extra": """
          .page { border-radius: 12px; box-shadow: 0 4px 20px rgba(0,102,204,0.08); }
          .kpi-value { font-size: 32px !important; }
          .kpi { text-align: center; padding: 16px 10px; border-radius: 12px; }
          .kpi-icon { font-size: 24px !important; }
          .hero-compact-top { gap: 16px; }
          .status-item .num { font-size: 28px; color: var(--accent); }
          .pulse .val { font-size: 28px; color: var(--accent); }
          .alert-bar { font-size: 13px; padding: 14px 18px; border-radius: 10px; display: flex; align-items: center; gap: 10px; }
          .alert-bar::before { content: '🚨'; font-size: 20px; }
          .section-bar { margin-bottom: 12px; }
          .progress-track { height: 14px; border-radius: 7px; }
          thead th { background: var(--accent); font-size: 11px; }
          .delay-badge { font-size: 13px; padding: 6px 10px; }
        """,
    },
    "seventh-design": {
        "health_a": "#b7791f",
        "health_b": "#2c5282",
        "name": "Editorial Brief",
        "font": "Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Source+Sans+3:wght@400;600;700",
        "font_family": "'Source Sans 3', sans-serif",
        "mono": "'Fraunces', serif",
        "bg": "#faf9f6",
        "page": "#faf9f6",
        "text": "#2c2c2c",
        "muted": "#6b6b6b",
        "accent": "#8b2942",
        "accent2": "#2c5282",
        "danger": "#9b2335",
        "warn": "#b7791f",
        "ok": "#276749",
        "card": "#ffffff",
        "border": "#d9d5cc",
        "banner": "#faf9f6",
        "style_extra": """
          .page { box-shadow: none; border-bottom: 3px double #2c2c2c; border-radius: 0; padding: 18mm 20mm; }
          .banner { background: transparent; color: #2c2c2c; border-bottom: 4px solid #8b2942; border-radius: 0; padding: 0 0 16px; }
          .banner-left h1 { font-family: 'Fraunces', serif; font-size: 36px; font-weight: 700; color: #8b2942; }
          .banner-left .subtitle { color: #6b6b6b; font-size: 11px; letter-spacing: 0.15em; }
          .banner-right { color: #6b6b6b; }
          .banner-right .date { font-family: 'Fraunces', serif; font-size: 18px; color: #2c2c2c; }
          .kpi { background: transparent; border: none; border-bottom: 1px solid #d9d5cc; border-radius: 0; border-top: none; }
          .kpi-value { font-family: 'Fraunces', serif; }
          .panel h3, .page-title-row h2 { font-family: 'Fraunces', serif; color: #8b2942; text-transform: none; font-size: 16px; letter-spacing: 0; }
          .alert-bar { background: #fff5f5; border-left: none; border-top: 3px solid #9b2335; border-radius: 0; font-family: 'Fraunces', serif; font-style: italic; color: #9b2335; }
          thead th { background: #8b2942; font-family: 'Source Sans 3', sans-serif; }
          .two-col { gap: 24px; }
        """,
    },
    "eighth-design": {
        "health_a": "#b8860b",
        "health_b": "#4a7c78",
        "name": "McKinsey Teal",
        "font": "Inter:wght@400;500;600;700&family=EB+Garamond:ital,wght@0,500;0,600;0,700;1,400",
        "font_family": "'Inter', sans-serif",
        "mono": "'EB Garamond', serif",
        "bg": "#f7f7f5",
        "page": "#ffffff",
        "text": "#1a1a1a",
        "muted": "#9B9B9B",
        "accent": "#034641",
        "accent2": "#4a7c78",
        "danger": "#c0392b",
        "warn": "#b8860b",
        "ok": "#034641",
        "card": "#ffffff",
        "border": "#e8e8e6",
        "banner": "#034641",
        "style_extra": """
          .banner-left h1 { font-family: 'EB Garamond', serif; font-size: 26px; font-weight: 600; }
          .page { box-shadow: 0 2px 16px rgba(3,70,65,0.06); border-radius: 4px; }
          .kpi { border-top: none; border-left: 3px solid #034641; border-radius: 0; }
          .kpi.danger { border-left-color: #c0392b; }
          .panel h3, .page-title-row h2 { font-family: 'EB Garamond', serif; color: #034641; text-transform: none; font-size: 14px; }
          .alert-bar { background: #fdf6f5; border-left-color: #c0392b; color: #922b21; }
          thead th { background: #034641; }
          .progress-fill.low { background: #c0392b; }
          .progress-fill.mid { background: #9B9B9B; }
        """,
    },
    "ninth-design": {
        "health_a": "#e87722",
        "health_b": "#0066b3",
        "name": "BCG Strategy Navy",
        "font": "Libre+Franklin:wght@400;500;600;700;800",
        "font_family": "'Libre Franklin', sans-serif",
        "mono": "'Libre Franklin', sans-serif",
        "bg": "#eef2f7",
        "page": "#ffffff",
        "text": "#1a2332",
        "muted": "#5a6578",
        "accent": "#003366",
        "accent2": "#0066b3",
        "danger": "#c8102e",
        "warn": "#e87722",
        "ok": "#2e7d32",
        "card": "#ffffff",
        "border": "#d0d9e4",
        "banner": "linear-gradient(135deg, #003366 0%, #004d99 100%)",
        "style_extra": """
          .page { border-top: 5px solid #003366; border-radius: 8px; box-shadow: 0 4px 24px rgba(0,51,102,0.1); }
          .kpi { border-top: 3px solid #003366; }
          .kpi.danger { border-top-color: #c8102e; }
          .kpi.warn { border-top-color: #0066b3; }
          .panel h3 { color: #003366; }
          thead th { background: linear-gradient(180deg, #003366, #004d99); }
          .progress-fill.mid { background: #0066b3; }
          .progress-fill.low { background: #c8102e; }
          .alert-bar { background: #fff5f5; border-left-color: #c8102e; color: #8b0018; }
        """,
    },
    "tenth-design": {
        "health_a": "#d97706",
        "health_b": "#333333",
        "name": "Bain Advisory",
        "font": "Work+Sans:wght@400;500;600;700;800",
        "font_family": "'Work Sans', sans-serif",
        "mono": "'Work Sans', sans-serif",
        "bg": "#ffffff",
        "page": "#ffffff",
        "text": "#222222",
        "muted": "#666666",
        "accent": "#CC0000",
        "accent2": "#333333",
        "danger": "#CC0000",
        "warn": "#d97706",
        "ok": "#059669",
        "card": "#ffffff",
        "border": "#eeeeee",
        "banner": "#CC0000",
        "style_extra": """
          .page { box-shadow: none; border: 1px solid #eee; }
          .banner { border-radius: 0; }
          .banner-left h1 { font-weight: 800; letter-spacing: -0.03em; }
          .kpi { border-top: 4px solid #CC0000; border-radius: 0; }
          .kpi.neutral { border-top-color: #ccc; }
          .kpi.ok { border-top-color: #059669; }
          .panel { border-radius: 0; border-left: 3px solid #CC0000; }
          thead th { background: #CC0000; }
          .alert-bar { background: #fff; border: 2px solid #CC0000; border-left-width: 6px; color: #CC0000; border-radius: 0; }
          .page-title-row h2 { color: #CC0000; font-weight: 800; }
        """,
    },
    "eleventh-design": {
        "health_a": "#c2410c",
        "health_b": "#E08BD5",
        "name": "Accenture LifeTrends",
        "font": "DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700",
        "font_family": "'DM Sans', sans-serif",
        "mono": "'DM Sans', sans-serif",
        "bg": "#fafafa",
        "page": "#ffffff",
        "text": "#1a1a2e",
        "muted": "#6b7280",
        "accent": "#700C47",
        "accent2": "#E08BD5",
        "danger": "#be123c",
        "warn": "#c2410c",
        "ok": "#047857",
        "card": "#ffffff",
        "border": "#f0e6f0",
        "banner": "linear-gradient(135deg, #700C47 0%, #9d174d 50%, #E08BD5 100%)",
        "style_extra": """
          .page { border-radius: 16px; box-shadow: 0 8px 40px rgba(112,12,71,0.08); overflow: hidden; }
          .banner { border-radius: 12px; position: relative; }
          .banner::after { content: ''; position: absolute; inset: 0; background: radial-gradient(circle at 80% 20%, rgba(224,139,213,0.3), transparent 60%); pointer-events: none; border-radius: 12px; }
          .kpi { border-radius: 12px; background: linear-gradient(135deg, #fff, #fdf4ff); border-top-color: #700C47; }
          .panel h3 { color: #700C47; }
          thead th { background: linear-gradient(90deg, #700C47, #E08BD5); }
          .alert-bar { background: linear-gradient(90deg, #fff1f2, #fdf4ff); border-left-color: #be123c; border-radius: 12px; }
          .progress-fill.mid { background: #E08BD5; }
        """,
    },
    "twelfth-design": {
        "health_a": "#f0ab00",
        "health_b": "#000000",
        "name": "Deloitte Green Dot",
        "font": "Open+Sans:wght@400;500;600;700;800",
        "font_family": "'Open Sans', sans-serif",
        "mono": "'Open Sans', sans-serif",
        "bg": "#f4f4f4",
        "page": "#ffffff",
        "text": "#000000",
        "muted": "#53565a",
        "accent": "#86BC25",
        "accent2": "#000000",
        "danger": "#da291c",
        "warn": "#f0ab00",
        "ok": "#86BC25",
        "card": "#ffffff",
        "border": "#e0e0e0",
        "banner": "#000000",
        "style_extra": """
          .banner { border-left: 8px solid #86BC25; border-radius: 0; }
          .banner-left .subtitle { color: #86BC25; opacity: 1; font-weight: 600; }
          .page { border-radius: 0; box-shadow: 0 2px 12px rgba(0,0,0,0.06); }
          .kpi { border-top: 4px solid #86BC25; border-radius: 0; }
          .kpi.danger { border-top-color: #da291c; }
          thead th { background: #000; border-bottom: 3px solid #86BC25; }
          .panel h3 { color: #000; border-bottom-color: #86BC25; border-bottom-width: 2px; }
          .alert-bar { background: #fff8e6; border-left-color: #da291c; color: #7a1a12; }
          .success-box { background: #f0fae0; border-color: #86BC25; color: #3d5c12; }
          .success-box h3 { color: #86BC25; }
        """,
    },
    "thirteenth-design": {
        "health_a": "#f1c21b",
        "health_b": "#001d6c",
        "name": "IBM Enterprise",
        "font": "IBM+Plex+Sans:wght@400;500;600;700",
        "font_family": "'IBM Plex Sans', sans-serif",
        "mono": "'IBM Plex Sans', sans-serif",
        "bg": "#161616",
        "page": "#ffffff",
        "text": "#161616",
        "muted": "#525252",
        "accent": "#0f62fe",
        "accent2": "#001d6c",
        "danger": "#da1e28",
        "warn": "#f1c21b",
        "ok": "#24a148",
        "card": "#f4f4f4",
        "border": "#e0e0e0",
        "banner": "linear-gradient(90deg, #001d6c, #0f62fe)",
        "style_extra": """
          body { background: #161616; }
          .page { border-radius: 0; box-shadow: 0 8px 32px rgba(0,0,0,0.4); }
          .banner { border-radius: 0; }
          .kpi { background: #f4f4f4; border-top: 3px solid #0f62fe; border-radius: 0; }
          .kpi.danger { border-top-color: #da1e28; }
          .panel { border-radius: 0; border-left: 4px solid #0f62fe; }
          thead th { background: #001d6c; border-radius: 0; }
          .alert-bar { background: #fff1f1; border-left-color: #da1e28; border-radius: 0; color: #750e13; }
          .page-title-row h2 { color: #001d6c; }
        """,
    },
    "fourteenth-design": {
        "health_a": "#fe9339",
        "health_b": "#1b96ff",
        "name": "Salesforce Cloud",
        "font": "Salesforce+Sans:wght@400;500;600;700&family=Inter:wght@400;600;700",
        "font_family": "'Inter', sans-serif",
        "mono": "'Inter', sans-serif",
        "bg": "#eef4ff",
        "page": "#ffffff",
        "text": "#032d60",
        "muted": "#5c6b7a",
        "accent": "#0176d3",
        "accent2": "#1b96ff",
        "danger": "#ea001e",
        "warn": "#fe9339",
        "ok": "#2e844a",
        "card": "#ffffff",
        "border": "#c9d7eb",
        "banner": "linear-gradient(135deg, #032d60 0%, #0176d3 100%)",
        "style_extra": """
          .page { border-radius: 12px; box-shadow: 0 4px 24px rgba(1,118,211,0.12); }
          .banner { border-radius: 12px 12px 0 0; margin-bottom: 0; }
          .alert-bar { border-radius: 0; margin-top: 0; border-left: none; border-top: 3px solid #ea001e; background: #fef0f3; }
          .kpi { border-radius: 8px; box-shadow: 0 2px 8px rgba(1,118,211,0.08); border-top-color: #0176d3; }
          thead th { background: #0176d3; border-radius: 0; }
          .panel { border-radius: 8px; }
          .pill.progress { background: #eef4ff; color: #0176d3; }
        """,
    },
    "fifteenth-design": {
        "health_a": "#FFB600",
        "health_b": "#EB8C00",
        "name": "PwC Advisory",
        "font": "Georgia:ital,wght@0,400;0,700;1,400&family=Arial:wght@400;700",
        "font_family": "Arial, Helvetica, sans-serif",
        "mono": "Georgia, serif",
        "bg": "#ffffff",
        "page": "#ffffff",
        "text": "#2D2D2D",
        "muted": "#7D7D7D",
        "accent": "#D04A02",
        "accent2": "#EB8C00",
        "danger": "#E0301E",
        "warn": "#FFB600",
        "ok": "#2D2D2D",
        "card": "#ffffff",
        "border": "#DEDEDE",
        "banner": "#D04A02",
        "style_extra": """
          .banner-left h1 { font-family: Georgia, serif; font-size: 24px; }
          .page { border: 1px solid #DEDEDE; box-shadow: none; }
          .kpi { border-top: 5px solid #D04A02; border-radius: 0; }
          .kpi.warn { border-top-color: #FFB600; }
          .kpi.danger { border-top-color: #E0301E; }
          thead th { background: #2D2D2D; }
          .panel h3 { color: #D04A02; }
          .alert-bar { background: #fff8f0; border-left-color: #E0301E; color: #922b21; }
          .page-title-row h2 { font-family: Georgia, serif; color: #2D2D2D; }
        """,
    },
    "sixteenth-design": {
        "health_a": "#f0ab00",
        "health_b": "#0091DA",
        "name": "KPMG Assurance",
        "font": "Univers+Next+Pro:wght@400;600;700&family=Inter:wght@400;600;700",
        "font_family": "'Inter', sans-serif",
        "mono": "'Inter', sans-serif",
        "bg": "#f0f4fa",
        "page": "#ffffff",
        "text": "#1a1a2e",
        "muted": "#64748b",
        "accent": "#00338D",
        "accent2": "#0091DA",
        "danger": "#e03c31",
        "warn": "#f0ab00",
        "ok": "#00A3A1",
        "card": "#ffffff",
        "border": "#cbd5e1",
        "banner": "linear-gradient(90deg, #00338D 60%, #0091DA 100%)",
        "style_extra": """
          .page { border-left: 6px solid #00338D; border-radius: 4px; box-shadow: 0 4px 20px rgba(0,51,141,0.08); }
          .kpi { border-top-color: #00338D; }
          .kpi.ok { border-top-color: #00A3A1; }
          thead th { background: #00338D; }
          .panel h3 { color: #00338D; }
          .alert-bar { background: #eff6ff; border-left-color: #e03c31; color: #991b1b; }
          .progress-fill.mid { background: #0091DA; }
        """,
    },
    "seventeenth-design": {
        "health_a": "#FFE600",
        "health_b": "#2E2E38",
        "name": "EY Insights",
        "font": "Noto+Sans:wght@400;500;600;700&family=Noto+Serif:wght@400;600;700",
        "font_family": "'Noto Sans', sans-serif",
        "mono": "'Noto Serif', serif",
        "bg": "#2E2E38",
        "page": "#ffffff",
        "text": "#2E2E38",
        "muted": "#747480",
        "accent": "#FFE600",
        "accent2": "#2E2E38",
        "danger": "#ff4136",
        "warn": "#FFE600",
        "ok": "#2e7d32",
        "card": "#ffffff",
        "border": "#e4e4e8",
        "banner": "#2E2E38",
        "style_extra": """
          body { background: #2E2E38; }
          .banner { border-bottom: 4px solid #FFE600; border-radius: 0; }
          .banner-left .subtitle { color: #FFE600; opacity: 1; }
          .page { border-radius: 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3); }
          .kpi { border-top: 4px solid #FFE600; border-radius: 0; }
          .kpi-value { color: #2E2E38; }
          .kpi.danger .kpi-value { color: #ff4136; }
          thead th { background: #2E2E38; border-bottom: 3px solid #FFE600; color: #FFE600; }
          .panel h3 { color: #2E2E38; border-bottom: 2px solid #FFE600; }
          .alert-bar { background: #fffef0; border-left-color: #ff4136; color: #7f1d1d; }
          .page-title-row h2 { font-family: 'Noto Serif', serif; }
        """,
    },
    "eighteenth-design": {
        "health_a": "#ff6d00",
        "health_b": "#12ABDB",
        "name": "Capgemini Digital",
        "font": "Ubuntu:wght@400;500;700&family=Ubuntu+Mono:wght@400;700",
        "font_family": "'Ubuntu', sans-serif",
        "mono": "'Ubuntu Mono', monospace",
        "bg": "#f5f9fc",
        "page": "#ffffff",
        "text": "#1f2937",
        "muted": "#6b7280",
        "accent": "#0070AD",
        "accent2": "#12ABDB",
        "danger": "#e30613",
        "warn": "#ff6d00",
        "ok": "#00875a",
        "card": "#ffffff",
        "border": "#dbeafe",
        "banner": "linear-gradient(135deg, #0070AD, #12ABDB)",
        "style_extra": """
          .page { border-radius: 10px; box-shadow: 0 6px 30px rgba(0,112,173,0.1); }
          .banner { border-radius: 10px; }
          .kpi { border-radius: 10px; border-top-color: #0070AD; background: linear-gradient(180deg, #f5f9fc, #fff); }
          thead th { background: linear-gradient(90deg, #0070AD, #12ABDB); }
          .panel h3 { color: #0070AD; }
          .alert-bar { background: #fff5f5; border-left-color: #e30613; border-radius: 8px; }
          .delay-badge.critical { background: #e30613; }
        """,
    },
    "nineteenth-design": {
        "health_a": "#f57c00",
        "health_b": "#0066cc",
        "name": "TCS Enterprise",
        "font": "Roboto:wght@400;500;700&family=Roboto+Slab:wght@400;600;700",
        "font_family": "'Roboto', sans-serif",
        "mono": "'Roboto Slab', serif",
        "bg": "#f8f9fc",
        "page": "#ffffff",
        "text": "#212121",
        "muted": "#616161",
        "accent": "#001489",
        "accent2": "#0066cc",
        "danger": "#d32f2f",
        "warn": "#f57c00",
        "ok": "#388e3c",
        "card": "#ffffff",
        "border": "#e0e0e0",
        "banner": "#001489",
        "style_extra": """
          .banner-left h1 { font-family: 'Roboto Slab', serif; }
          .page { box-shadow: 0 2px 16px rgba(0,20,137,0.08); border-radius: 6px; border-top: 4px solid #001489; }
          .kpi { border-left: 4px solid #001489; border-top: none; border-radius: 4px; }
          .kpi.danger { border-left-color: #d32f2f; }
          thead th { background: #001489; }
          .panel h3 { color: #001489; font-family: 'Roboto Slab', serif; text-transform: none; }
          .alert-bar { background: #fce4ec; border-left-color: #d32f2f; color: #b71c1c; }
          .page-title-row h2 { font-family: 'Roboto Slab', serif; color: #001489; }
        """,
    },
    "twentieth-design": {
        "health_a": "#c4a35a",
        "health_b": "#87a878",
        "name": "Warm Sage Corporate",
        "font": "Lato:wght@400;700&family=Playfair+Display:wght@500;600;700",
        "font_family": "'Lato', sans-serif",
        "mono": "'Playfair Display', serif",
        "bg": "#faf8f5",
        "page": "#faf8f5",
        "text": "#3d3d3d",
        "muted": "#8a8580",
        "accent": "#5c7a6b",
        "accent2": "#87a878",
        "danger": "#b54a4a",
        "warn": "#c4a35a",
        "ok": "#5c7a6b",
        "card": "#ffffff",
        "border": "#e8e4df",
        "banner": "linear-gradient(135deg, #5c7a6b 0%, #87a878 100%)",
        "style_extra": """
          body { background: #faf8f5; }
          .page { background: #faf8f5; box-shadow: none; border: 1px solid #e8e4df; border-radius: 12px; }
          .banner { border-radius: 12px; }
          .banner-left h1 { font-family: 'Playfair Display', serif; font-weight: 600; }
          .kpi { background: #fff; border-radius: 12px; border-top-color: #87a878; box-shadow: 0 2px 8px rgba(92,122,107,0.06); }
          .kpi.danger { border-top-color: #b54a4a; }
          .panel { border-radius: 12px; background: #fff; }
          .panel h3, .page-title-row h2 { font-family: 'Playfair Display', serif; color: #5c7a6b; text-transform: none; }
          thead th { background: #5c7a6b; border-radius: 0; }
          .alert-bar { background: #fdf8f6; border-left-color: #b54a4a; color: #7a3a3a; border-radius: 8px; }
          .people-card, .delays-panel { background: #fff; }
          .success-box { background: #f0f7f2; border-color: #87a878; color: #3d5c4a; }
        """,
    },
}

THEME_LAYOUT = {
    "first-design": {"health_variant": "loader-ring", "hero_layout": "strip"},
    "second-design": {"health_variant": "loader-bar", "hero_layout": "strip"},
    "third-design": {"health_variant": "loader-wave", "hero_layout": "strip"},
    "fourth-design": {"health_variant": "loader-segments", "hero_layout": "strip"},
    "fifth-design": {"health_variant": "loader-pill", "hero_layout": "strip"},
    "sixth-design": {"health_variant": "loader-radial", "hero_layout": "strip"},
    "seventh-design": {"health_variant": "loader-gauge", "hero_layout": "strip"},
    "eighth-design": {"health_variant": "loader-orbit", "hero_layout": "strip"},
    "ninth-design": {"health_variant": "loader-dots", "hero_layout": "strip"},
    "tenth-design": {"health_variant": "loader-vertical", "hero_layout": "strip"},
    "eleventh-design": {"health_variant": "loader-stack", "hero_layout": "strip"},
    "twelfth-design": {"health_variant": "loader-pulse-bar", "hero_layout": "strip"},
    "thirteenth-design": {"health_variant": "loader-dual", "hero_layout": "strip"},
    "fourteenth-design": {"health_variant": "loader-steps", "hero_layout": "strip"},
    "fifteenth-design": {"health_variant": "loader-arc-bar", "hero_layout": "strip"},
    "sixteenth-design": {"health_variant": "loader-battery", "hero_layout": "strip"},
    "seventeenth-design": {"health_variant": "loader-ripple", "hero_layout": "strip"},
    "eighteenth-design": {"health_variant": "loader-ticker", "hero_layout": "strip"},
    "nineteenth-design": {"health_variant": "loader-spiral", "hero_layout": "strip"},
    "twentieth-design": {"health_variant": "loader-ladder", "hero_layout": "strip"},
}

DELAYS_HTML = """
    <div class="delays-panel">
      <h3>⚠ Top 5 of 7 Late Tasks — Requires immediate attention</h3>
      <div class="delay-item"><span class="delay-badge critical">+199</span><div><div class="delay-title">Ramp (Excavation, Levelling, GSB, Compaction, Brickwork, PCC&amp;CC)</div><div class="delay-meta">3 - Project Execution · Unassigned · Past planned start date — work not yet begun</div></div></div>
      <div class="delay-item"><span class="delay-badge warning">+7</span><div><div class="delay-title">Advance Payment</div><div class="delay-meta">2 - Concession Development Phase · Unassigned · Past planned start date — work not yet begun</div></div></div>
      <div class="delay-item"><span class="delay-badge warning">+7</span><div><div class="delay-title">Release of Order (Cost Comparision , NFA &amp; PO/SO Approvals)</div><div class="delay-meta">2 - Concession Development Phase · Unassigned · Blocked by: Advance Payment</div></div></div>
      <div class="delay-item"><span class="delay-badge warning">+7</span><div><div class="delay-title">Advance Payment</div><div class="delay-meta">2 - Concession Development Phase · Unassigned · Past planned start date — work not yet begun</div></div></div>
      <div class="delay-item"><span class="delay-badge warning">+7</span><div><div class="delay-title">Fire Fighting System with BOQ</div><div class="delay-meta">2 - Concession Development Phase · Unassigned · Past planned start date — work not yet begun</div></div></div>
    </div>"""

PEOPLE_HTML = """
    <div class="people-card">
      <div class="people-row"><span>Project Manager</span><span>Prasant Jaiswal</span></div>
      <div class="people-row"><span>Cluster Head</span><span>—</span></div>
      <div class="people-row"><span>Site Team</span><span>0 crew</span></div>
      <div class="people-row"><span>Weather</span><span>Drizzle · 33°C / 27°C</span></div>
    </div>"""

HEALTH_BLOCKS = {
    "loader-ring": """
    <div class="health-card health-v-loader">
      <div class="health-loader-wrap health-loader-wrap-lg">
        <svg class="health-loader-svg" viewBox="0 0 60 60" aria-hidden="true">
          <circle class="health-loader-track" cx="30" cy="30" r="26"/>
          <circle class="health-loader-arc" cx="30" cy="30" r="26"/>
        </svg>
        <div class="health-loader-num"><span>52</span><small>/100</small></div>
      </div>
      <div class="health-meta health-meta-grow">
        <span class="health-badge">Needs Attention</span>
        <div class="health-mini-track"><div class="health-mini-fill"></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-bar": """
    <div class="health-card health-v-bar">
      <div class="health-bar-left">
        <div class="health-bar-score">52<small>/100</small></div>
        <span class="health-badge">Needs Attention</span>
      </div>
      <div class="health-bar-right">
        <div class="health-bar-head">
          <span class="health-bar-title">Project Health Index</span>
          <span class="health-bar-pct">52%</span>
        </div>
        <div class="health-bar-track-lg"><div class="health-bar-fill-lg"></div></div>
        <div class="health-bar-ticks"><span></span><span></span><span></span><span></span><span></span></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
      <div class="health-bar-spinner" aria-hidden="true"></div>
    </div>""",
    "loader-pill": """
    <div class="health-card health-v-pill">
      <div class="health-pill-loader"><span>52</span></div>
      <div class="health-pill-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-pill-track"><div class="health-pill-fill"></div></div>
        <span class="health-sub">52 of 100 · Slipping — action needed.</span>
      </div>
      <div class="health-pill-dots"><i></i><i></i><i></i></div>
    </div>""",
    "loader-wave": """
    <div class="health-card health-v-wave">
      <div class="health-wave-score">52<small>/100</small></div>
      <div class="health-wave-body">
        <div class="health-wave-head"><span class="health-badge">Needs Attention</span><span class="health-bar-pct">52%</span></div>
        <div class="health-wave-track"><div class="health-wave-fill"></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-segments": """
    <div class="health-card health-v-segments">
      <div class="health-seg-left"><div class="health-bar-score">52<small>/100</small></div><span class="health-badge">Needs Attention</span></div>
      <div class="health-seg-body">
        <div class="health-seg-row"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="half"></i><i></i><i></i><i></i></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-radial": """
    <div class="health-card health-v-radial">
      <div class="health-radial-bars"><span style="--h:52%"></span><span style="--h:38%"></span><span style="--h:62%"></span><span style="--h:45%"></span><span style="--h:70%"></span><span style="--h:52%"></span><span style="--h:40%"></span><span style="--h:55%"></span><span style="--h:48%"></span><span style="--h:52%"></span></div>
      <div class="health-radial-meta"><div class="health-bar-score">52<small>/100</small></div><span class="health-badge">Needs Attention</span><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-gauge": """
    <div class="health-card health-v-gauge">
      <div class="health-gauge-wrap">
        <svg viewBox="0 0 120 70" aria-hidden="true"><path class="health-gauge-track" d="M10 65 A55 55 0 0 1 110 65"/><path class="health-gauge-arc" d="M10 65 A55 55 0 0 1 110 65"/></svg>
        <div class="health-gauge-num">52</div>
      </div>
      <div class="health-gauge-meta"><span class="health-badge">Needs Attention</span><span class="health-sub">52 of 100 · Slipping — action needed.</span></div>
    </div>""",
    "loader-orbit": """
    <div class="health-card health-v-orbit">
      <div class="health-orbit-wrap"><div class="health-orbit-ring"></div><div class="health-orbit-dot d1"></div><div class="health-orbit-dot d2"></div><div class="health-orbit-dot d3"></div><div class="health-orbit-score">52<small>/100</small></div></div>
      <div class="health-orbit-meta"><span class="health-badge">Needs Attention</span><div class="health-mini-track"><div class="health-mini-fill"></div></div><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-dots": """
    <div class="health-card health-v-dots">
      <div class="health-dots-score">52<small>/100</small></div>
      <div class="health-dots-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-dots-row"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="half"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-vertical": """
    <div class="health-card health-v-vertical">
      <div class="health-vert-track"><div class="health-vert-fill"></div><span>52</span></div>
      <div class="health-vert-meta"><span class="health-badge">Needs Attention</span><div class="health-bar-score sm">52<small>/100</small></div><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-stack": """
    <div class="health-card health-v-stack">
      <div class="health-stack-score">52<small>/100</small></div>
      <div class="health-stack-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-stack-row"><label>Health</label><div class="health-stack-track"><div class="health-stack-fill s1"></div></div><span>52%</span></div>
        <div class="health-stack-row"><label>SPI</label><div class="health-stack-track"><div class="health-stack-fill s2"></div></div><span>3%</span></div>
        <div class="health-stack-row"><label>Progress</label><div class="health-stack-track"><div class="health-stack-fill s3"></div></div><span>2%</span></div>
      </div>
    </div>""",
    "loader-pulse-bar": """
    <div class="health-card health-v-pulse-bar">
      <div class="health-bar-score">52<small>/100</small></div>
      <div class="health-pulse-bar-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-pulse-track"><div class="health-pulse-fill"></div><div class="health-pulse-marker"></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-dual": """
    <div class="health-card health-v-dual">
      <div class="health-dual-ring"><svg viewBox="0 0 60 60"><circle class="health-loader-track" cx="30" cy="30" r="24"/><circle class="health-loader-arc" cx="30" cy="30" r="24"/></svg><span>52</span></div>
      <div class="health-dual-bars">
        <span class="health-badge">Needs Attention</span>
        <div class="health-dual-row"><span>Health</span><div class="health-mini-track wide"><div class="health-mini-fill"></div></div></div>
        <div class="health-dual-row"><span>Risk</span><div class="health-mini-track wide"><div class="health-mini-fill risk"></div></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-steps": """
    <div class="health-card health-v-steps">
      <div class="health-steps-score">52<small>/100</small></div>
      <div class="health-steps-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-steps-row"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-arc-bar": """
    <div class="health-card health-v-arc-bar">
      <div class="health-arc-mini"><svg viewBox="0 0 60 60"><circle class="health-loader-track" cx="30" cy="30" r="22"/><circle class="health-loader-arc" cx="30" cy="30" r="22"/></svg><span>52</span></div>
      <div class="health-arc-bar-body">
        <div class="health-bar-head"><span class="health-badge">Needs Attention</span><span class="health-bar-pct">52%</span></div>
        <div class="health-bar-track-lg striped"><div class="health-bar-fill-lg"></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-battery": """
    <div class="health-card health-v-battery">
      <div class="health-battery-shell"><div class="health-battery-fill"></div><span>52%</span></div>
      <div class="health-battery-meta"><div class="health-bar-score sm">52<small>/100</small></div><span class="health-badge">Needs Attention</span><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-ripple": """
    <div class="health-card health-v-ripple">
      <div class="health-ripple-wrap"><div class="health-ripple r1"></div><div class="health-ripple r2"></div><div class="health-ripple r3"></div><span>52<small>/100</small></span></div>
      <div class="health-ripple-meta"><span class="health-badge">Needs Attention</span><div class="health-mini-track"><div class="health-mini-fill"></div></div><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-ticker": """
    <div class="health-card health-v-ticker">
      <div class="health-ticker-score">52<small>/100</small></div>
      <div class="health-ticker-body">
        <span class="health-badge">Needs Attention</span>
        <div class="health-ticker-track"><div class="health-ticker-fill"></div><div class="health-ticker-scan"></div></div>
        <span class="health-sub">Slipping — action needed.</span>
      </div>
    </div>""",
    "loader-spiral": """
    <div class="health-card health-v-spiral">
      <div class="health-spiral-wrap"><div class="health-spiral"></div><span>52<small>/100</small></span></div>
      <div class="health-spiral-meta"><span class="health-badge">Needs Attention</span><div class="health-bar-track-lg"><div class="health-bar-fill-lg"></div></div><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
    "loader-ladder": """
    <div class="health-card health-v-ladder">
      <div class="health-ladder-col"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="health-ladder-meta"><div class="health-bar-score sm">52<small>/100</small></div><span class="health-badge">Needs Attention</span><span class="health-sub">Slipping — action needed.</span></div>
    </div>""",
}


def build_hero_section(slug):
    layout = THEME_LAYOUT.get(slug, {"health_variant": "loader-ring", "hero_layout": "classic"})
    health = HEALTH_BLOCKS[layout["health_variant"]]
    delays = DELAYS_HTML
    people = PEOPLE_HTML
    mode = layout["hero_layout"]
    if mode == "strip":
        return f'<div class="hero hero-strip">{health}<div class="hero-strip-body">{delays}{people}</div></div>'
    if mode == "compact-row":
        return f'<div class="hero hero-compact"><div class="hero-compact-top">{health}{people}</div>{delays}</div>'
    return f'<div class="hero hero-classic">{health}{delays}{people}</div>'

BASE_CSS = """
    :root {{
      --bg: {bg};
      --page: {page};
      --text: {text};
      --muted: {muted};
      --accent: {accent};
      --accent2: {accent2};
      --danger: {danger};
      --warn: {warn};
      --ok: {ok};
      --card: {card};
      --border: {border};
      --banner: {banner};
      --health-a: {health_a};
      --health-b: {health_b};
      --page-width: {page_width};
      --page-min-height: {page_min_height};
      --page-pad-left: {page_pad_left};
      --page-pad-right: {page_pad_right};
      --page-pad-top: {page_pad_top};
      --page-pad-bottom: {page_pad_bottom};
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    .page, .page-main, .panel, .kpi, .status-item, .delay-card, .health-card,
    .people-card, .delays-panel, .two-col, .kpi-grid, .status-grid, .pulse-row {{
      min-width: 0;
    }}
    body, .page, .page-main, .panel, table, th, td, .delay-title, .delay-meta,
    .panel h3, .kpi-label, .kpi-sub, .status-item .lbl, .status-item .pct, .pulse .lbl,
    .pulse .chg, .banner-left, .alert-bar, .footer, .mini-panel, .activity-card-title,
    .delay-card-title, .section-name, .people-row span, .rollup-stat .lbl, .section-meta,
    .page-title-row h2, .page-title-row span, .health-sub, .health-meta {{
      overflow-wrap: break-word;
      word-break: normal;
      hyphens: none;
      white-space: normal;
    }}
    body {{
      font-family: 'Inter', {font_family}, 'Segoe UI', system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      font-size: 13px;
      line-height: 1.55;
      letter-spacing: 0.01em;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
      overflow-x: auto;
      margin: 0;
      padding: 0;
    }}
    .page {{
      width: var(--page-width);
      max-width: 100%;
      min-height: var(--page-min-height);
      margin: 0;
      background: var(--page);
      padding: var(--page-pad-top) var(--page-pad-right) var(--page-pad-bottom) var(--page-pad-left);
      page-break-after: always;
      position: relative;
      display: flex;
      flex-direction: column;
      border: 1px solid var(--border);
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.06);
      overflow: visible;
    }}
    .page:last-child {{ page-break-after: auto; margin-bottom: 0; }}
    .page-main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 6px;
      min-height: 0;
      padding: 4px 4px 8mm;
      background: var(--page);
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: visible;
    }}
    .page-fill-tail {{
      flex: 1 1 auto;
      min-height: 28px;
      border-radius: 8px;
      background: #f9fafb;
      border: 1px dashed var(--border);
    }}
    .fill-row {{ flex: 1; min-height: 0; display: flex; flex-direction: column; }}
    .fill-grow {{
      flex: 1;
      display: flex;
      flex-direction: column;
      min-height: 0;
    }}
    .kpi-band {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 4px;
    }}
    .banner {{
      background: var(--banner);
      color: #fff;
      border-radius: 8px;
      padding: 10px 12px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 8px;
    }}
    .banner-left h1 {{ font-size: 24px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.2; }}
    .banner-left .subtitle {{ font-size: 12px; opacity: 0.9; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.06em; font-weight: 600; }}
    .banner-left .project {{ font-size: 17px; font-weight: 600; margin-top: 8px; }}
    .banner-right {{ text-align: right; font-size: 12px; opacity: 0.95; }}
    .banner-right .date {{ font-size: 15px; font-weight: 700; }}
    .alert-bar {{
      background: rgba(220,38,38,0.08);
      border-left: 4px solid var(--danger);
      border-radius: 0 6px 6px 0;
      padding: 8px 10px;
      margin-bottom: 8px;
      font-size: 13px;
      font-weight: 600;
      line-height: 1.5;
      color: var(--danger);
    }}
    .hero {{ margin-bottom: 0; }}
    .hero-classic {{ display: grid; grid-template-columns: 152px 1fr minmax(130px, 16%); gap: 6px; align-items: start; }}
    .hero-classic .delays-panel, .hero-classic .people-card {{ align-self: stretch; }}
    .hero-strip {{ display: flex; flex-direction: column; gap: 6px; }}
    .hero-strip > .health-card {{ width: 100%; flex-shrink: 0; }}
    .hero-strip-body {{ display: grid; grid-template-columns: 1fr minmax(130px, 16%); gap: 6px; align-items: stretch; }}
    .hero-strip-body .delays-panel {{ min-height: 0; }}
    .hero-strip-body .people-card {{ align-self: stretch; }}
    .hero-compact {{ display: flex; flex-direction: column; gap: 6px; }}
    .hero-compact-top {{ display: flex; gap: 6px; align-items: start; }}
    .hero-compact-top .people-card {{ flex: 1; align-self: stretch; }}
    .hero-compact .delays-panel {{ flex: 1; }}
    .health-card {{
      align-self: start;
      width: 100%;
      height: fit-content;
      border-radius: 12px;
      overflow: hidden;
    }}
    @keyframes health-load {{
      from {{ stroke-dashoffset: 163.36; }}
      to {{ stroke-dashoffset: 78.41; }}
    }}
    @keyframes health-fill {{
      from {{ width: 0; }}
      to {{ width: 52%; }}
    }}
    @keyframes health-shimmer {{
      0% {{ transform: translateX(-120%); }}
      100% {{ transform: translateX(220%); }}
    }}
    @keyframes health-spin {{
      to {{ transform: rotate(360deg); }}
    }}
    @keyframes health-glow {{
      0%, 100% {{ box-shadow: 0 0 0 0 rgba(245,158,11,0.45); }}
      50% {{ box-shadow: 0 0 0 7px rgba(245,158,11,0); }}
    }}
    @keyframes health-dot {{
      0%, 80%, 100% {{ opacity: 0.25; transform: scale(0.85); }}
      40% {{ opacity: 1; transform: scale(1.1); }}
    }}
    .health-v-loader, .health-v-bar, .health-v-pill, .health-v-wave, .health-v-segments,
    .health-v-radial, .health-v-gauge, .health-v-orbit, .health-v-dots, .health-v-vertical,
    .health-v-stack, .health-v-pulse-bar, .health-v-dual, .health-v-steps, .health-v-arc-bar,
    .health-v-battery, .health-v-ripple, .health-v-ticker, .health-v-spiral, .health-v-ladder {{
      min-height: 78px;
      width: 100%;
    }}
    .health-v-loader {{
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 14px;
      padding: 12px 16px;
      background: linear-gradient(135deg, color-mix(in srgb, var(--health-a) 14%, transparent), color-mix(in srgb, var(--health-b) 7%, transparent));
      border: 1px solid color-mix(in srgb, var(--health-a) 40%, transparent);
      border-left: 5px solid var(--health-a);
    }}
    .health-loader-wrap {{
      position: relative;
      width: 56px;
      height: 56px;
      flex-shrink: 0;
    }}
    .health-loader-wrap-lg {{
      width: 64px;
      height: 64px;
    }}
    .health-loader-wrap-lg .health-loader-svg {{
      width: 64px;
      height: 64px;
    }}
    .health-loader-wrap-lg .health-loader-num span {{
      font-size: 20px;
    }}
    .health-meta-grow {{
      flex: 1;
      min-width: 0;
    }}
    .health-mini-track {{
      height: 10px;
      background: rgba(128,128,128,0.15);
      border-radius: 5px;
      overflow: hidden;
      margin: 6px 0;
    }}
    .health-mini-track.wide {{
      flex: 1;
      margin: 0;
    }}
    .health-mini-fill {{
      height: 100%;
      width: 52%;
      border-radius: 5px;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-fill 1.3s ease forwards;
    }}
    .health-mini-fill.risk {{
      width: 78%;
      background: linear-gradient(90deg, var(--danger), var(--health-a));
    }}
    .health-loader-svg {{
      width: 56px;
      height: 56px;
      transform: rotate(-90deg);
    }}
    .health-loader-track {{
      fill: none;
      stroke: rgba(128,128,128,0.18);
      stroke-width: 5;
    }}
    .health-loader-arc {{
      fill: none;
      stroke: var(--health-a);
      stroke-width: 5;
      stroke-linecap: round;
      stroke-dasharray: 163.36;
      stroke-dashoffset: 78.41;
      animation: health-load 1.3s cubic-bezier(0.34, 1.2, 0.64, 1) forwards;
    }}
    .health-loader-num {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      line-height: 1;
    }}
    .health-loader-num span {{
      font-size: 17px;
      font-weight: 800;
      color: var(--health-b);
    }}
    .health-loader-num small {{
      font-size: 10px;
      font-weight: 600;
      color: var(--muted);
      margin-top: 1px;
    }}
    .health-meta {{
      display: flex;
      flex-direction: column;
      gap: 4px;
      min-width: 0;
    }}
    .health-badge {{
      display: inline-block;
      width: fit-content;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      color: #fff;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 5px 11px;
      border-radius: 999px;
      animation: health-glow 2.4s ease-in-out infinite;
    }}
    .health-sub {{
      font-size: 12px;
      color: var(--text);
      opacity: 0.85;
      line-height: 1.45;
      font-weight: 500;
    }}
    .health-v-bar {{
      display: flex;
      align-items: stretch;
      gap: 16px;
      padding: 12px 16px;
      min-height: 78px;
      position: relative;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 14%, transparent), color-mix(in srgb, var(--health-b) 6%, transparent));
      border: 1px solid color-mix(in srgb, var(--health-a) 38%, transparent);
      border-left: 5px solid var(--health-a);
    }}
    .health-bar-left {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 6px;
      flex-shrink: 0;
      min-width: 88px;
      padding-right: 12px;
      border-right: 1px dashed color-mix(in srgb, var(--health-a) 30%, var(--border));
    }}
    .health-bar-score {{
      font-size: 36px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
    }}
    .health-bar-score small {{
      font-size: 14px;
      font-weight: 600;
      color: var(--muted);
    }}
    .health-bar-right {{
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      gap: 6px;
    }}
    .health-bar-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .health-bar-title {{
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text);
      opacity: 0.75;
    }}
    .health-bar-pct {{
      font-size: 14px;
      font-weight: 800;
      color: var(--health-b);
    }}
    .health-bar-track-lg {{
      height: 18px;
      background: repeating-linear-gradient(90deg, rgba(128,128,128,0.08) 0, rgba(128,128,128,0.08) calc(20% - 1px), rgba(128,128,128,0.18) calc(20% - 1px), rgba(128,128,128,0.18) 20%);
      border-radius: 9px;
      overflow: hidden;
      border: 1px solid rgba(128,128,128,0.15);
    }}
    .health-bar-fill-lg {{
      height: 100%;
      width: 52%;
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      background: linear-gradient(90deg, #fbbf24, var(--health-a), var(--health-b));
      animation: health-fill 1.4s cubic-bezier(0.34, 1.2, 0.64, 1) forwards;
      box-shadow: 0 0 12px color-mix(in srgb, var(--health-a) 55%, transparent);
    }}
    .health-bar-fill-lg::after {{
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.45), transparent);
      animation: health-shimmer 2.2s ease-in-out infinite;
    }}
    .health-bar-ticks {{
      display: flex;
      justify-content: space-between;
      padding: 0 2px;
    }}
    .health-bar-ticks span {{
      font-size: 10px;
      color: var(--muted);
      width: 20%;
      text-align: center;
    }}
    .health-bar-ticks span::before {{
      content: "▪";
      display: block;
      font-size: 8px;
      line-height: 1;
      opacity: 0.6;
    }}
    .health-bar-spinner {{
      position: absolute;
      top: 10px;
      right: 10px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      border: 2px solid color-mix(in srgb, var(--health-a) 25%, transparent);
      border-top-color: var(--health-a);
      animation: health-spin 1.1s linear infinite;
      opacity: 0.85;
    }}
    .health-v-pill {{
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), color-mix(in srgb, var(--health-b) 6%, transparent));
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
      border-radius: 999px;
      width: 100%;
    }}
    .health-pill-loader {{
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--health-a), var(--health-b));
      color: #fff;
      font-size: 18px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 0 12px color-mix(in srgb, var(--health-a) 50%, transparent);
      animation: health-glow 2.4s ease-in-out infinite;
    }}
    .health-pill-track {{
      height: 8px;
      background: rgba(128,128,128,0.15);
      border-radius: 4px;
      overflow: hidden;
      margin: 5px 0;
    }}
    .health-pill-fill {{
      height: 100%;
      width: 52%;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-fill 1.2s ease forwards;
    }}
    .health-pill-body {{
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 3px;
      min-width: 0;
    }}
    .health-pill-dots {{
      display: flex;
      gap: 5px;
      flex-shrink: 0;
    }}
    .health-pill-dots i {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--health-a);
      display: block;
      animation: health-dot 1.2s ease-in-out infinite;
    }}
    .health-pill-dots i:nth-child(2) {{ animation-delay: 0.15s; }}
    .health-pill-dots i:nth-child(3) {{ animation-delay: 0.3s; }}
    .health-v-wave {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), color-mix(in srgb, var(--health-b) 8%, transparent));
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
      border-left: 5px solid var(--health-a);
    }}
    .health-wave-score {{
      font-size: 36px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
      flex-shrink: 0;
      min-width: 88px;
      text-align: center;
    }}
    .health-wave-score small {{ font-size: 14px; color: var(--muted); font-weight: 600; }}
    .health-wave-body {{ flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 6px; }}
    .health-wave-head {{ display: flex; justify-content: space-between; align-items: center; gap: 8px; }}
    .health-wave-track {{
      height: 22px;
      background: rgba(128,128,128,0.12);
      border-radius: 11px;
      overflow: hidden;
      position: relative;
    }}
    .health-wave-fill {{
      height: 100%;
      width: 52%;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-fill 1.3s ease forwards;
      position: relative;
      overflow: hidden;
    }}
    .health-wave-fill::after {{
      content: "";
      position: absolute;
      inset: 0;
      background: repeating-linear-gradient(90deg, transparent 0 8px, rgba(255,255,255,0.25) 8px 16px);
      animation: health-wave-move 1.8s linear infinite;
    }}
    @keyframes health-wave-move {{
      from {{ transform: translateX(0); }}
      to {{ transform: translateX(16px); }}
    }}
    .health-v-segments {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), color-mix(in srgb, var(--health-b) 6%, transparent));
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
    }}
    .health-seg-left {{ flex-shrink: 0; display: flex; flex-direction: column; align-items: center; gap: 6px; min-width: 88px; }}
    .health-seg-body {{ flex: 1; min-width: 0; }}
    .health-seg-row {{
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      gap: 5px;
      margin-bottom: 6px;
    }}
    .health-seg-row i {{
      display: block;
      height: 22px;
      border-radius: 4px;
      background: rgba(128,128,128,0.15);
      animation: health-seg-pop 0.5s ease backwards;
    }}
    .health-seg-row i.on {{
      background: linear-gradient(180deg, var(--health-a), var(--health-b));
      box-shadow: 0 0 8px color-mix(in srgb, var(--health-a) 40%, transparent);
    }}
    .health-seg-row i.half {{
      background: linear-gradient(90deg, var(--health-a) 50%, rgba(128,128,128,0.15) 50%);
    }}
    .health-seg-row i:nth-child(1) {{ animation-delay: 0.05s; }}
    .health-seg-row i:nth-child(2) {{ animation-delay: 0.1s; }}
    .health-seg-row i:nth-child(3) {{ animation-delay: 0.15s; }}
    .health-seg-row i:nth-child(4) {{ animation-delay: 0.2s; }}
    .health-seg-row i:nth-child(5) {{ animation-delay: 0.25s; }}
    .health-seg-row i:nth-child(6) {{ animation-delay: 0.3s; }}
    .health-seg-row i:nth-child(7) {{ animation-delay: 0.35s; }}
    @keyframes health-seg-pop {{
      from {{ transform: scaleY(0.2); opacity: 0.3; }}
      to {{ transform: scaleY(1); opacity: 1; }}
    }}
    .health-v-radial {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-radial-bars {{
      display: flex;
      align-items: flex-end;
      gap: 4px;
      height: 52px;
      flex-shrink: 0;
    }}
    .health-radial-bars span {{
      width: 8px;
      height: var(--h);
      border-radius: 4px 4px 0 0;
      background: linear-gradient(180deg, var(--health-a), var(--health-b));
      animation: health-radial-grow 1s ease backwards;
    }}
    .health-radial-bars span:nth-child(odd) {{ animation-delay: 0.1s; }}
    @keyframes health-radial-grow {{
      from {{ height: 0; }}
      to {{ height: var(--h); }}
    }}
    .health-radial-meta {{ flex: 1; display: flex; flex-direction: column; gap: 5px; align-items: flex-start; }}
    .health-v-gauge {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 10px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
      border-left: 5px solid var(--health-a);
    }}
    .health-gauge-wrap {{
      position: relative;
      width: 120px;
      height: 70px;
      flex-shrink: 0;
    }}
    .health-gauge-wrap svg {{ width: 100%; height: 100%; }}
    .health-gauge-track {{
      fill: none;
      stroke: rgba(128,128,128,0.2);
      stroke-width: 8;
      stroke-linecap: round;
    }}
    .health-gauge-arc {{
      fill: none;
      stroke: var(--health-a);
      stroke-width: 8;
      stroke-linecap: round;
      stroke-dasharray: 172.79;
      stroke-dashoffset: 82.94;
      animation: health-gauge-load 1.4s ease forwards;
    }}
    .health-dual-ring .health-loader-arc,
    .health-arc-mini .health-loader-arc {{
      stroke-dasharray: 150.8;
      stroke-dashoffset: 72.38;
      animation: health-load-sm 1.3s cubic-bezier(0.34, 1.2, 0.64, 1) forwards;
    }}
    .health-arc-mini .health-loader-arc {{
      stroke-dasharray: 138.23;
      stroke-dashoffset: 66.35;
      animation: health-load-xs 1.3s cubic-bezier(0.34, 1.2, 0.64, 1) forwards;
    }}
    @keyframes health-load-sm {{
      from {{ stroke-dashoffset: 150.8; }}
      to {{ stroke-dashoffset: 72.38; }}
    }}
    @keyframes health-load-xs {{
      from {{ stroke-dashoffset: 138.23; }}
      to {{ stroke-dashoffset: 66.35; }}
    }}
    @keyframes health-gauge-load {{
      from {{ stroke-dashoffset: 172.79; }}
      to {{ stroke-dashoffset: 82.94; }}
    }}
    .health-gauge-num {{
      position: absolute;
      left: 50%;
      bottom: 4px;
      transform: translateX(-50%);
      font-size: 22px;
      font-weight: 800;
      color: var(--health-b);
    }}
    .health-gauge-meta {{ flex: 1; display: flex; flex-direction: column; gap: 5px; }}
    .health-v-orbit {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-orbit-wrap {{
      position: relative;
      width: 64px;
      height: 64px;
      flex-shrink: 0;
    }}
    .health-orbit-ring {{
      position: absolute;
      inset: 4px;
      border: 2px dashed color-mix(in srgb, var(--health-a) 40%, transparent);
      border-radius: 50%;
      animation: health-spin 8s linear infinite;
    }}
    .health-orbit-dot {{
      position: absolute;
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--health-a);
      top: 50%;
      left: 50%;
      margin: -4px 0 0 -4px;
      animation: health-orbit 2s linear infinite;
    }}
    .health-orbit-dot.d2 {{ animation-duration: 2.6s; background: var(--health-b); }}
    .health-orbit-dot.d3 {{ animation-duration: 3.2s; }}
    @keyframes health-orbit {{
      from {{ transform: rotate(0deg) translateX(28px); }}
      to {{ transform: rotate(360deg) translateX(28px); }}
    }}
    .health-orbit-score {{
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
    }}
    .health-orbit-score small {{ font-size: 9px; color: var(--muted); }}
    .health-orbit-meta {{ flex: 1; display: flex; flex-direction: column; gap: 4px; }}
    .health-v-dots {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-dots-score {{
      font-size: 32px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
      flex-shrink: 0;
      min-width: 80px;
      text-align: center;
    }}
    .health-dots-score small {{ font-size: 13px; color: var(--muted); }}
    .health-dots-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-dots-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
    }}
    .health-dots-row i {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: rgba(128,128,128,0.2);
      display: block;
    }}
    .health-dots-row i.on {{ background: var(--health-a); animation: health-dot 1.5s ease infinite; }}
    .health-dots-row i.half {{ background: linear-gradient(90deg, var(--health-a) 50%, rgba(128,128,128,0.2) 50%); }}
    .health-v-vertical {{
      display: flex;
      align-items: stretch;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-vert-track {{
      width: 36px;
      height: 64px;
      background: rgba(128,128,128,0.15);
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
      display: flex;
      align-items: flex-end;
      justify-content: center;
    }}
    .health-vert-fill {{
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 52%;
      background: linear-gradient(180deg, var(--health-b), var(--health-a));
      animation: health-vert-rise 1.3s ease forwards;
    }}
    @keyframes health-vert-rise {{
      from {{ height: 0; }}
      to {{ height: 52%; }}
    }}
    .health-vert-track > span {{
      position: relative;
      z-index: 1;
      font-size: 13px;
      font-weight: 800;
      color: #fff;
      padding-bottom: 6px;
      text-shadow: 0 1px 3px rgba(0,0,0,0.4);
    }}
    .health-vert-meta {{ flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 6px; }}
    .health-bar-score.sm {{ font-size: 28px; }}
    .health-v-stack {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-stack-score {{ font-size: 32px; font-weight: 800; color: var(--health-b); line-height: 1; flex-shrink: 0; min-width: 76px; text-align: center; }}
    .health-stack-score small {{ font-size: 13px; color: var(--muted); }}
    .health-stack-body {{ flex: 1; display: flex; flex-direction: column; gap: 5px; }}
    .health-stack-row {{
      display: grid;
      grid-template-columns: 52px 1fr 36px;
      gap: 8px;
      align-items: center;
      font-size: 11px;
      font-weight: 600;
      color: var(--text);
      opacity: 0.8;
    }}
    .health-stack-track {{
      height: 8px;
      background: rgba(128,128,128,0.15);
      border-radius: 4px;
      overflow: hidden;
    }}
    .health-stack-fill {{
      height: 100%;
      border-radius: 4px;
      animation: health-fill 1.2s ease forwards;
    }}
    .health-stack-fill.s1 {{ width: 52%; background: linear-gradient(90deg, var(--health-a), var(--health-b)); }}
    .health-stack-fill.s2 {{ width: 3%; background: var(--danger); animation-delay: 0.2s; }}
    .health-stack-fill.s3 {{ width: 2%; background: var(--warn); animation-delay: 0.35s; }}
    .health-v-pulse-bar {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
      border-left: 5px solid var(--health-a);
    }}
    .health-pulse-bar-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-pulse-track {{
      height: 16px;
      background: rgba(128,128,128,0.15);
      border-radius: 8px;
      position: relative;
      overflow: visible;
    }}
    .health-pulse-fill {{
      height: 100%;
      width: 52%;
      border-radius: 8px;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-fill 1.2s ease forwards;
    }}
    .health-pulse-marker {{
      position: absolute;
      top: -4px;
      left: 52%;
      width: 12px;
      height: 24px;
      margin-left: -6px;
      background: var(--health-b);
      border-radius: 3px;
      animation: health-pulse-blink 1.2s ease-in-out infinite;
    }}
    @keyframes health-pulse-blink {{
      0%, 100% {{ opacity: 1; transform: scaleY(1); }}
      50% {{ opacity: 0.6; transform: scaleY(0.85); }}
    }}
    .health-v-dual {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-dual-ring {{
      position: relative;
      width: 58px;
      height: 58px;
      flex-shrink: 0;
    }}
    .health-dual-ring svg {{
      width: 100%;
      height: 100%;
      transform: rotate(-90deg);
    }}
    .health-dual-ring span {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      font-weight: 800;
      color: var(--health-b);
    }}
    .health-dual-bars {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-dual-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 11px;
      font-weight: 600;
      color: var(--text);
      opacity: 0.75;
    }}
    .health-dual-row span {{ min-width: 42px; }}
    .health-v-steps {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-steps-score {{ font-size: 32px; font-weight: 800; color: var(--health-b); line-height: 1; flex-shrink: 0; min-width: 76px; text-align: center; }}
    .health-steps-score small {{ font-size: 13px; color: var(--muted); }}
    .health-steps-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-steps-row {{
      display: flex;
      gap: 3px;
      flex-wrap: wrap;
    }}
    .health-steps-row i {{
      width: 14px;
      height: 8px;
      border-radius: 2px;
      background: rgba(128,128,128,0.15);
      display: block;
      transform: skewX(-12deg);
    }}
    .health-steps-row i.on {{
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-seg-pop 0.4s ease backwards;
    }}
    .health-v-arc-bar {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
    }}
    .health-arc-mini {{
      position: relative;
      width: 56px;
      height: 56px;
      flex-shrink: 0;
    }}
    .health-arc-mini svg {{
      width: 100%;
      height: 100%;
      transform: rotate(-90deg);
    }}
    .health-arc-mini span {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 15px;
      font-weight: 800;
      color: var(--health-b);
    }}
    .health-arc-bar-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-bar-track-lg.striped {{
      background: repeating-linear-gradient(90deg, rgba(128,128,128,0.1) 0 10px, rgba(128,128,128,0.2) 10px 20px);
    }}
    .health-v-battery {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-battery-shell {{
      width: 72px;
      height: 34px;
      border: 3px solid var(--health-a);
      border-radius: 6px;
      position: relative;
      flex-shrink: 0;
      padding: 3px;
      overflow: hidden;
    }}
    .health-battery-shell::after {{
      content: "";
      position: absolute;
      right: -8px;
      top: 8px;
      width: 6px;
      height: 14px;
      background: var(--health-a);
      border-radius: 0 3px 3px 0;
    }}
    .health-battery-fill {{
      height: 100%;
      width: 52%;
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      border-radius: 3px;
      animation: health-fill 1.3s ease forwards;
    }}
    .health-battery-shell > span {{
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 800;
      color: var(--text);
      z-index: 1;
    }}
    .health-battery-meta {{ flex: 1; display: flex; flex-direction: column; gap: 5px; }}
    .health-v-ripple {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-ripple-wrap {{
      position: relative;
      width: 64px;
      height: 64px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .health-ripple {{
      position: absolute;
      inset: 0;
      border: 2px solid var(--health-a);
      border-radius: 50%;
      animation: health-ripple-out 2s ease-out infinite;
    }}
    .health-ripple.r2 {{ animation-delay: 0.6s; }}
    .health-ripple.r3 {{ animation-delay: 1.2s; }}
    @keyframes health-ripple-out {{
      0% {{ transform: scale(0.4); opacity: 0.9; }}
      100% {{ transform: scale(1.2); opacity: 0; }}
    }}
    .health-ripple-wrap > span {{
      position: relative;
      z-index: 1;
      font-size: 16px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
      text-align: center;
    }}
    .health-ripple-wrap > span small {{ font-size: 9px; color: var(--muted); display: block; }}
    .health-ripple-meta {{ flex: 1; display: flex; flex-direction: column; gap: 4px; }}
    .health-v-ticker {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 12%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 35%, transparent);
    }}
    .health-ticker-score {{ font-size: 32px; font-weight: 800; color: var(--health-b); line-height: 1; flex-shrink: 0; min-width: 76px; text-align: center; }}
    .health-ticker-score small {{ font-size: 13px; color: var(--muted); }}
    .health-ticker-body {{ flex: 1; display: flex; flex-direction: column; gap: 6px; }}
    .health-ticker-track {{
      height: 18px;
      background: rgba(128,128,128,0.15);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }}
    .health-ticker-fill {{
      height: 100%;
      width: 52%;
      background: var(--health-a);
      animation: health-fill 1.2s ease forwards;
    }}
    .health-ticker-scan {{
      position: absolute;
      top: 0;
      bottom: 0;
      width: 3px;
      background: #fff;
      box-shadow: 0 0 8px var(--health-b);
      animation: health-ticker-scan 2s ease-in-out infinite;
    }}
    @keyframes health-ticker-scan {{
      0% {{ left: 0; }}
      100% {{ left: 52%; }}
    }}
    .health-v-spiral {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-spiral-wrap {{
      position: relative;
      width: 56px;
      height: 56px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .health-spiral {{
      position: absolute;
      inset: 0;
      border: 4px solid transparent;
      border-top-color: var(--health-a);
      border-right-color: var(--health-b);
      border-radius: 50%;
      animation: health-spin 1.4s linear infinite;
    }}
    .health-spiral-wrap > span {{
      position: relative;
      z-index: 1;
      font-size: 14px;
      font-weight: 800;
      color: var(--health-b);
      line-height: 1;
      text-align: center;
    }}
    .health-spiral-wrap > span small {{ font-size: 8px; color: var(--muted); display: block; }}
    .health-spiral-meta {{ flex: 1; display: flex; flex-direction: column; gap: 5px; }}
    .health-v-ladder {{
      display: flex;
      align-items: center;
      gap: 16px;
      padding: 12px 16px;
      background: linear-gradient(90deg, color-mix(in srgb, var(--health-a) 10%, transparent), transparent);
      border: 1px solid color-mix(in srgb, var(--health-a) 30%, transparent);
    }}
    .health-ladder-col {{
      display: flex;
      flex-direction: column-reverse;
      gap: 2px;
      height: 64px;
      flex-shrink: 0;
      justify-content: flex-start;
    }}
    .health-ladder-col i {{
      display: block;
      width: 28px;
      height: 3px;
      border-radius: 2px;
      background: rgba(128,128,128,0.15);
    }}
    .health-ladder-col i.on {{
      background: linear-gradient(90deg, var(--health-a), var(--health-b));
      animation: health-ladder-on 0.3s ease backwards;
    }}
    .health-ladder-col i.on:nth-child(n) {{ animation-delay: calc(var(--i, 0) * 0.03s); }}
    @keyframes health-ladder-on {{
      from {{ transform: translateX(-8px); opacity: 0; }}
      to {{ transform: translateX(0); opacity: 1; }}
    }}
    .health-ladder-meta {{ flex: 1; display: flex; flex-direction: column; gap: 6px; justify-content: center; }}
    @media print {{
      .health-loader-arc, .health-bar-fill-lg, .health-badge, .health-pill-loader, .health-pill-dots i,
      .health-mini-fill, .health-wave-fill, .health-gauge-arc, .health-vert-fill, .health-battery-fill,
      .health-ticker-fill, .health-pulse-fill, .health-pill-fill, .health-stack-fill {{
        animation: none !important;
      }}
      .health-loader-arc {{ stroke-dashoffset: 78.41; }}
      .health-bar-fill-lg, .health-mini-fill, .health-wave-fill, .health-vert-fill,
      .health-battery-fill, .health-ticker-fill, .health-pulse-fill, .health-pill-fill {{ width: 52%; }}
      .health-gauge-arc {{ stroke-dashoffset: 82.94; }}
      .health-vert-fill {{ height: 52%; }}
    }}
    .delays-panel {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; height: 100%; display: flex; flex-direction: column; }}
    .delays-panel h3 {{ flex-shrink: 0; }}
    .delay-item {{ flex-shrink: 0; }}
    .delays-panel h3 {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.05em; color: var(--danger); margin-bottom: 10px; font-weight: 700; white-space: normal; line-height: 1.35; }}
    .delay-item {{ display: grid; grid-template-columns: 46px 1fr; gap: 10px; padding: 8px 0; border-bottom: 1px solid var(--border); }}
    .delay-item:last-child {{ border-bottom: none; }}
    .delay-badge {{ font-size: 13px; font-weight: 700; padding: 5px 8px; border-radius: 6px; text-align: center; }}
    .delay-badge.critical {{ background: var(--danger); color: #fff; }}
    .delay-badge.warning {{ background: rgba(217,119,6,0.15); color: var(--warn); border: 1px solid var(--warn); }}
    .delay-title {{ font-weight: 600; font-size: 13px; line-height: 1.45; }}
    .delay-meta {{ font-size: 12px; color: var(--text); opacity: 0.72; margin-top: 3px; line-height: 1.4; }}
    .people-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; font-size: 13px; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: space-evenly; }}
    .people-row {{ display: flex; justify-content: space-between; padding: 4px 0; border-bottom: 1px solid var(--border); flex: 1; align-items: center; gap: 6px; }}
    .people-row:last-child {{ border-bottom: none; }}
    .people-row span:first-child {{ color: var(--text); opacity: 0.65; font-size: 11px; text-transform: uppercase; letter-spacing: 0.04em; font-weight: 600; flex: 1 1 40%; }}
    .people-row span:last-child {{ font-weight: 600; text-align: right; flex: 1 1 50%; font-size: 13px; white-space: normal; }}
    .kpi-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; }}
    .kpi {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; border-top: 3px solid var(--border); min-height: 64px; display: flex; flex-direction: column; justify-content: center; }}
    .kpi.danger {{ border-top-color: var(--danger); }}
    .kpi.warn {{ border-top-color: var(--warn); }}
    .kpi.neutral {{ border-top-color: var(--muted); }}
    .kpi.ok {{ border-top-color: var(--ok); }}
    .kpi-icon {{ font-size: 18px; margin-bottom: 6px; }}
    .kpi-value {{ font-size: 26px; font-weight: 700; line-height: 1.1; }}
    .kpi-value.small {{ font-size: 18px; }}
    .kpi-label {{ font-size: 10px; text-transform: uppercase; letter-spacing: 0.02em; color: var(--text); opacity: 0.7; margin-top: 4px; font-weight: 600; line-height: 1.2; }}
    .kpi-sub {{ font-size: 11px; color: var(--text); opacity: 0.72; margin-top: 2px; line-height: 1.2; }}
    .two-col {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px; align-items: stretch; }}
    .two-col.fill-row .panel {{ display: flex; flex-direction: column; min-height: 110px; height: 100%; overflow: visible; }}
    .two-col.fill-row .panel-body {{ flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 10px; overflow: visible; }}
    .panel {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; overflow: visible; }}
    .panel.fill-grow {{ flex: 1; }}
    .panel-pulse {{ background: linear-gradient(180deg, color-mix(in srgb, var(--accent) 8%, var(--card)), color-mix(in srgb, var(--accent) 14%, var(--page))); flex: 1; }}
    .panel-pulse .pulse-row {{ flex: 1; align-items: stretch; min-height: 80px; }}
    .panel-pulse .pulse {{ display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 72px; height: 100%; background: color-mix(in srgb, var(--accent) 5%, var(--card)); }}
    .panel h3 {{ font-size: 12px; text-transform: uppercase; letter-spacing: 0.02em; color: var(--accent); margin-bottom: 6px; padding-bottom: 4px; border-bottom: 1px solid var(--border); font-weight: 700; line-height: 1.3; }}
    .section-bar {{ display: flex; align-items: center; gap: 8px; margin-bottom: 0; min-height: 32px; flex-wrap: wrap; }}
    .section-name {{ font-size: 12px; font-weight: 600; min-width: 0; flex: 1 1 auto; line-height: 1.35; white-space: normal; }}
    .progress-track {{ flex: 1; height: 12px; background: var(--border); border-radius: 6px; overflow: hidden; }}
    .progress-fill {{ height: 100%; border-radius: 4px; }}
    .progress-fill.low {{ background: var(--danger); width: 64%; }}
    .progress-fill.mid {{ background: var(--warn); width: 78%; }}
    .section-meta {{ font-size: 11px; color: var(--text); opacity: 0.75; font-weight: 600; flex-shrink: 0; }}
    .status-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px; }}
    .status-grid.compact {{ grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 4px; height: 100%; align-content: stretch; overflow: visible; }}
    .status-item {{ background: var(--card); border: 1px solid var(--border); border-radius: 6px; padding: 4px 4px; text-align: center; min-width: 0; }}
    .status-grid.compact .status-item {{ padding: 4px 3px; display: flex; flex-direction: column; justify-content: center; min-height: 56px; height: 100%; overflow: visible; }}
    .status-item .num {{ font-size: 18px; font-weight: 700; }}
    .status-grid.compact .status-item .num {{ font-size: 16px; }}
    .status-item .lbl {{ font-size: 9px; color: var(--text); opacity: 0.72; text-transform: uppercase; margin-top: 2px; font-weight: 600; line-height: 1.15; }}
    .status-item .pct {{ font-size: 10px; color: var(--text); opacity: 0.68; }}
    .pulse-row {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; }}
    .pulse {{ background: var(--card); border: 1px solid var(--border); border-radius: 6px; padding: 6px 4px; text-align: center; min-width: 0; }}
    .pulse .val {{ font-size: 22px; font-weight: 700; }}
    .pulse .lbl {{ font-size: 9px; color: var(--text); opacity: 0.72; text-transform: uppercase; font-weight: 600; margin-top: 3px; line-height: 1.15; }}
    .pulse .chg {{ font-size: 12px; color: var(--text); opacity: 0.68; margin-top: 2px; }}
    .success-box {{ background: rgba(22,163,74,0.08); border: 1px solid var(--ok); border-radius: 10px; padding: 14px 16px; }}
    .success-box h3 {{ color: var(--ok); font-size: 14px; margin-bottom: 4px; font-weight: 700; line-height: 1.4; }}
    .success-box p {{ font-size: 13px; opacity: 0.9; line-height: 1.45; }}
    .delay-cards {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px; flex: 1; align-content: start; grid-auto-rows: minmax(68px, auto); }}
    .delay-cards.fill-grow {{ flex: 1; min-height: 120px; background: color-mix(in srgb, var(--accent) 4%, transparent); border-radius: 8px; padding: 4px; }}
    .delay-card {{ border: 1px solid var(--border); border-radius: 8px; padding: 6px 8px; border-left: 4px solid var(--warn); background: var(--card); }}
    .delay-card.severe {{ border-left-color: var(--danger); background: rgba(220,38,38,0.06); }}
    .delay-card-header {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 8px; margin-bottom: 6px; flex-wrap: wrap; }}
    .delay-card-title {{ font-weight: 600; font-size: 13px; line-height: 1.45; flex: 1 1 180px; min-width: 0; }}
    .site-grid {{ display: grid; grid-template-columns: minmax(130px, 18%) 1fr; gap: 10px; align-items: stretch; min-height: 130px; }}
    .site-grid.fill-row {{ flex: 1; }}
    .site-grid > div:first-child {{ height: 100%; display: flex; }}
    .photo-placeholder {{
      background: linear-gradient(145deg, var(--muted), var(--accent));
      border-radius: 10px; flex: 1; width: 100%; min-height: 120px;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      color: #fff; font-size: 13px; text-align: center; padding: 10px; line-height: 1.45;
    }}
    .photo-placeholder .icon {{ font-size: 32px; margin-bottom: 6px; }}
    .photo-placeholder strong {{ font-size: 14px; margin-bottom: 4px; }}
    .photo-meta {{ margin-top: 6px; font-size: 12px; opacity: 0.92; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 12px; table-layout: fixed; }}
    thead th {{
      background: var(--accent); color: #fff; font-weight: 700; text-align: left;
      padding: 6px 8px; font-size: 10px; text-transform: uppercase; letter-spacing: 0.02em;
      white-space: normal; line-height: 1.3; vertical-align: top;
    }}
    tbody td {{ padding: 6px 8px; border-bottom: 1px solid var(--border); vertical-align: top; line-height: 1.35; word-break: normal; hyphens: none; }}
    .panel-table-wrap {{ padding: 0; overflow-x: auto; overflow-y: visible; }}
    .panel-table-wrap table {{ min-width: 100%; }}
    .panel-table-wrap h3 {{ margin: 0; padding: 6px 8px; border: none; line-height: 1.25; font-size: 11px; }}
    tbody tr:nth-child(even) {{ background: rgba(128,128,128,0.06); }}
    .empty-state {{ font-style: italic; color: var(--text); opacity: 0.72; padding: 14px 10px; font-size: 12px; min-height: 44px; display: flex; align-items: center; background: rgba(128,128,128,0.06); line-height: 1.45; }}
    .table-panel {{ flex: 1; display: flex; flex-direction: column; min-height: 0; }}
    .pill {{ display: inline-block; padding: 3px 9px; border-radius: 999px; font-size: 11px; font-weight: 600; text-transform: uppercase; }}
    .pill.progress {{ background: rgba(30,64,175,0.12); color: var(--accent); }}
    .pill.blocked {{ background: rgba(220,38,38,0.12); color: var(--danger); }}
    .pill.idle {{ background: rgba(128,128,128,0.12); color: var(--muted); }}
    .delay-tag {{ font-weight: 700; color: var(--danger); font-size: 12px; }}
    .section-header-row {{ background: var(--border) !important; font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.04em; }}
    .section-header-row td {{ padding: 8px; border-bottom: 2px solid var(--border); }}
    .mini-panels {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; flex: 1; align-content: end; }}
    .mini-panel {{ background: color-mix(in srgb, var(--accent) 6%, var(--card)); border: 1px dashed color-mix(in srgb, var(--accent) 20%, var(--border)); border-radius: 8px; padding: 12px; font-size: 12px; color: var(--text); opacity: 0.85; min-height: 72px; display: flex; flex-direction: column; justify-content: center; line-height: 1.45; }}
    .mini-panel strong {{ color: var(--text); display: block; margin-bottom: 4px; font-size: 13px; opacity: 1; }}
    .activity-summary-row {{ display: flex; gap: 12px; font-size: 13px; color: var(--text); opacity: 0.78; font-weight: 500; flex-wrap: wrap; }}
    .footer {{
      position: absolute; bottom: 4mm; left: var(--page-pad-left); right: var(--page-pad-right);
      font-size: 10px; color: var(--text); opacity: 0.72; text-transform: uppercase; letter-spacing: 0.03em;
      border-top: 1px solid var(--border); padding-top: 6px;
      display: flex; justify-content: space-between; gap: 8px; font-weight: 600; flex-wrap: wrap;
    }}
    .page-title-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; gap: 8px; flex-wrap: wrap; }}
    .page-title-row h2 {{ font-size: 16px; color: var(--accent); font-weight: 700; line-height: 1.3; white-space: normal; }}
    .page-title-row span {{ font-size: 12px; color: var(--text); opacity: 0.75; font-weight: 500; white-space: normal; }}
    @media print {{
      body {{ background: #fff; overflow-x: visible; }}
      .page {{
        margin: 0;
        box-shadow: none;
        width: 210mm;
        min-height: 297mm;
        padding: 12mm 16mm 10mm;
        page-break-after: always;
      }}
    }}
    {layout_css}
    {style_extra}
"""

def build_html(slug, theme):
    theme = prepare_theme(slug, theme)
    style_extra = theme["style_extra"]
    css_keys = ("bg", "page", "text", "muted", "accent", "accent2", "danger", "warn", "ok", "card", "border", "banner", "font_family", "health_a", "health_b")
    css_vals = {k: theme[k] for k in css_keys if k in theme}
    css_vals.setdefault("health_a", theme.get("warn", "#f59e0b"))
    css_vals.setdefault("health_b", theme.get("accent2", theme.get("accent", "#ea580c")))
    css_vals["layout_css"] = LAYOUT_CSS
    css_vals["style_extra"] = style_extra
    css_vals["page_width"] = PAGE_WIDTH
    css_vals["page_min_height"] = PAGE_MIN_HEIGHT
    css_vals["page_pad_left"] = PAGE_PAD_LEFT
    css_vals["page_pad_right"] = PAGE_PAD_RIGHT
    css_vals["page_pad_top"] = PAGE_PAD_TOP
    css_vals["page_pad_bottom"] = PAGE_PAD_BOTTOM
    css = BASE_CSS.format(**css_vals)
    body = build_document_body(slug, build_hero_section(slug))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DPR Bharuch — {theme["name"]}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family={theme["font"]}&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
{body}
</body>
</html>"""


def main():
    for slug, theme in THEMES.items():
        path = OUTPUT_DIR / f"{slug}.html"
        path.write_text(build_html(slug, theme), encoding="utf-8")
        print(f"Created {path.name} — {theme['name']}")


if __name__ == "__main__":
    main()
