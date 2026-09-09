BANNER = """
  <header class="banner">
    <div class="banner-left">
      <h1>Daily Progress Report</h1>
      <div class="subtitle">LEAP INDIA · Site Operations Briefing</div>
      <div class="project">Bharuch_R4_Leaptaskflow</div>
    </div>
    <div class="banner-right">
      <div class="date">Tue, 08 Sept, 2026</div>
      <div>Generated 08 Sept 2026, 09:51 am</div>
    </div>
  </header>"""

ALERT = """
  <div class="alert-bar">Schedule at risk — immediate intervention required. · 0 workers onsite · 0 activities moved today · 7 blockers open.</div>"""

KPI_GRID = """
  <div class="kpi-grid">
    <div class="kpi danger"><div class="kpi-icon">📈</div><div class="kpi-value">0.03</div><div class="kpi-label">Schedule SPI</div><div class="kpi-sub">Behind plan</div></div>
    <div class="kpi warn"><div class="kpi-icon">📊</div><div class="kpi-value">2%</div><div class="kpi-label">Average Progress</div><div class="kpi-sub">across 11 active</div></div>
    <div class="kpi neutral"><div class="kpi-icon">👷</div><div class="kpi-value">0</div><div class="kpi-label">Manpower Today</div><div class="kpi-sub">no data for yesterday · 1 report</div></div>
    <div class="kpi danger"><div class="kpi-icon">⛔</div><div class="kpi-value">7</div><div class="kpi-label">Open Blockers</div><div class="kpi-sub">1 overdue · 6 not started yet</div></div>
    <div class="kpi neutral"><div class="kpi-icon">⏰</div><div class="kpi-value">0</div><div class="kpi-label">Slipped Activities</div><div class="kpi-sub">started, past planned finish</div></div>
    <div class="kpi neutral"><div class="kpi-icon">⚡</div><div class="kpi-value">0</div><div class="kpi-label">Moved Today</div><div class="kpi-sub">logged quantity</div></div>
    <div class="kpi ok"><div class="kpi-icon">✓</div><div class="kpi-value small">446 / 1135</div><div class="kpi-label">Completed</div><div class="kpi-sub">of 1135 tasks</div></div>
    <div class="kpi neutral"><div class="kpi-icon">🏗</div><div class="kpi-value">11</div><div class="kpi-label">Active Activities</div><div class="kpi-sub">2 sections</div></div>
  </div>"""

KPI_GRID_4 = """
  <div class="kpi-grid kpi-grid-4">
    <div class="kpi danger"><div class="kpi-icon">📈</div><div class="kpi-value">0.03</div><div class="kpi-label">Schedule SPI</div><div class="kpi-sub">Behind plan</div></div>
    <div class="kpi warn"><div class="kpi-icon">📊</div><div class="kpi-value">2%</div><div class="kpi-label">Average Progress</div><div class="kpi-sub">across 11 active</div></div>
    <div class="kpi danger"><div class="kpi-icon">⛔</div><div class="kpi-value">7</div><div class="kpi-label">Open Blockers</div><div class="kpi-sub">1 overdue · 6 not started yet</div></div>
    <div class="kpi neutral"><div class="kpi-icon">🏗</div><div class="kpi-value">11</div><div class="kpi-label">Active Activities</div><div class="kpi-sub">2 sections</div></div>
  </div>"""

KPI_GRID_BIG = """
  <div class="kpi-grid kpi-grid-big">
    <div class="kpi danger"><div class="kpi-icon">📈</div><div class="kpi-value">0.03</div><div class="kpi-label">Schedule SPI</div><div class="kpi-sub">Behind plan</div></div>
    <div class="kpi warn"><div class="kpi-icon">📊</div><div class="kpi-value">2%</div><div class="kpi-label">Average Progress</div><div class="kpi-sub">across 11 active</div></div>
    <div class="kpi danger"><div class="kpi-icon">⛔</div><div class="kpi-value">7</div><div class="kpi-label">Open Blockers</div><div class="kpi-sub">1 overdue · 6 not started yet</div></div>
    <div class="kpi ok"><div class="kpi-icon">✓</div><div class="kpi-value small">446 / 1135</div><div class="kpi-label">Completed</div><div class="kpi-sub">of 1135 tasks</div></div>
  </div>"""

KPI_BAND = f'<div class="kpi-band">{KPI_GRID}</div>'
KPI_BAND_4 = f'<div class="kpi-band kpi-band-4">{KPI_GRID_4}</div>'
KPI_BAND_BIG = f'<div class="kpi-band kpi-band-big">{KPI_GRID_BIG}</div>'

SECTION_PANEL = """
    <div class="panel">
      <h3>A · Section Progress — 2 sections · sorted worst SPI first</h3>
      <div class="panel-body">
      <div class="section-bar"><span class="section-name">2 - Concession Development…</span><div class="progress-track"><div class="progress-fill low"></div></div><span class="section-meta">⛔ 6 · 64%</span></div>
      <div class="section-bar"><span class="section-name">3 - Project Execution</span><div class="progress-track"><div class="progress-fill mid"></div></div><span class="section-meta">⛔ 1 · 78%</span></div>
      </div>
    </div>"""

STATUS_PANEL = """
    <div class="panel">
      <h3>B · Activity Status Mix — 11 active leaves split by start status</h3>
      <div class="panel-body">
      <div class="status-grid compact">
        <div class="status-item"><div class="num">4</div><div class="lbl">Started On Time</div><div class="pct">36% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Started Early</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Started Late</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">9</div><div class="lbl">Not Started Yet</div><div class="pct">82% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Overdue</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Critical Behind</div><div class="pct">0% of 11</div></div>
      </div>
      </div>
    </div>"""

STATUS_PANEL_WIDE = """
    <div class="panel panel-status-wide">
      <h3>B · Activity Status Mix — 11 active leaves split by start status</h3>
      <div class="panel-body">
      <div class="status-grid status-row-6">
        <div class="status-item"><div class="num">4</div><div class="lbl">Started On Time</div><div class="pct">36% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Started Early</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Started Late</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">9</div><div class="lbl">Not Started Yet</div><div class="pct">82% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Overdue</div><div class="pct">0% of 11</div></div>
        <div class="status-item"><div class="num">0</div><div class="lbl">Critical Behind</div><div class="pct">0% of 11</div></div>
      </div>
      </div>
    </div>"""

PULSE_PANEL = """
  <div class="panel fill-grow panel-pulse">
    <h3>Today's Pulse</h3>
    <div class="pulse-row">
      <div class="pulse"><div class="val">0</div><div class="lbl">Started Today</div><div class="chg">→ No change</div></div>
      <div class="pulse"><div class="val">0</div><div class="lbl">Completed Today</div><div class="chg">→ No change</div></div>
      <div class="pulse"><div class="val">0</div><div class="lbl">Manpower</div><div class="chg">→ No change</div></div>
      <div class="pulse"><div class="val">0</div><div class="lbl">New Blockers</div><div class="chg">→ No change</div></div>
    </div>
  </div>"""

TAIL = '<div class="page-fill-tail"></div>'

DELAY_CARDS = """
  <div class="delay-card severe"><div class="delay-card-header"><div class="delay-card-title">Ramp (Excavation, Levelling, GSB, Compaction, Brickwork, PCC&amp;CC)</div><span class="delay-badge critical">+199d</span></div><div class="delay-meta">3 - Project Execution · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 21 Feb → 21 Feb · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">Advance Payment</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 01 Sept → 14 Sept · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">Release of Order (Cost Comparision , NFA &amp; PO/SO Approvals)</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">🔗 Blocked by: Advance Payment</div><div class="delay-meta">Plan: 01 Sept → 20 Sept · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">Advance Payment</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 01 Sept → 14 Sept · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">Fire Fighting System with BOQ</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 01 Sept → 08 Sept · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">Power Connection - Application &amp; Approval</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 01 Sept → 30 Sept · Progress: 0%</div></div>
  <div class="delay-card"><div class="delay-card-header"><div class="delay-card-title">NoC - Initial - Application &amp; Approval</div><span class="delay-badge warning">+7d</span></div><div class="delay-meta">2 - Concession Development Phase · Unassigned</div><div class="delay-meta">⏰ Past planned start date — work not yet begun</div><div class="delay-meta">Plan: 01 Sept → 15 Sept · Progress: 0%</div></div>"""

SITE_BLOCK = """
  <div class="site-grid fill-row">
    <div><div class="photo-placeholder"><span class="icon">📷</span><strong>1 - Silo 1</strong><span>Tue, 08 Sept, 2026</span><span class="photo-meta">📅 09:44:41 am · 📍 Bharuch · 📱 Android Phone</span></div></div>
    <div class="panel panel-table-wrap">
      <h3>B · Manpower Deployment 9/8/2026 — 1 report · 0 contractors</h3>
      <table><thead><tr><th>Sl.No</th><th>Contractor / Agency</th><th>Skilled</th><th>Unskilled</th><th>Operators</th><th>Supervisors</th><th>Total</th><th>Remarks</th></tr></thead>
      <tbody><tr><td colspan="8" class="empty-state">No contractor entries today — submit field reports with worker counts to populate this table.</td></tr>
      <tr style="font-weight:700;background:var(--border)!important;"><td colspan="2">TOTAL</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr></tbody></table>
    </div>
  </div>
  <div class="panel panel-table-wrap">
    <h3>C · Plant &amp; Machinery — 3 registered · 0 working today</h3>
    <table><thead><tr><th>Equipment</th><th>Make / Company</th><th>Capacity</th><th>Qty</th><th>Status Today</th></tr></thead>
    <tbody>
      <tr><td>Excavator</td><td>Schwing</td><td>120</td><td>3</td><td><span class="pill idle">○ IDLE</span></td></tr>
      <tr><td>Transit Mixer</td><td>Tata</td><td>130</td><td>2</td><td><span class="pill idle">○ IDLE</span></td></tr>
      <tr><td>Vibrator</td><td>Cummins</td><td>65</td><td>2</td><td><span class="pill idle">○ IDLE</span></td></tr>
    </tbody></table>
  </div>
  <div class="mini-panels">
    <div class="mini-panel"><strong>D · NFA Approval Status — 0 NFAs tracked</strong>No NFAs available — import the latest data from admin settings.</div>
    <div class="mini-panel"><strong>E · Drawing Status — 0 categories tracked</strong>No drawing status available — import the latest data from admin settings.</div>
  </div>"""

ROLLUP_TABLE = """
  <div class="panel panel-table-wrap">
    <h3>F · Activity Rollup by Section — 2 sections · 11 active leaf activities · sorted worst SPI first</h3>
    <table><thead><tr><th>#</th><th>Section</th><th>Activities</th><th>Done</th><th>In Progress</th><th>Not Started</th><th>Blocked</th><th>Slipped</th><th>Critical Path</th><th>Avg Progress</th><th>SPI</th><th>Avg Delay</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>2 - Concession Development Phase</td><td>7</td><td>—</td><td>1</td><td>6</td><td>6</td><td>6</td><td>—</td><td>64%</td><td style="color:var(--danger);font-weight:700;">0.00</td><td class="delay-tag">+7d</td></tr>
      <tr><td>2</td><td>3 - Project Execution</td><td>4</td><td>—</td><td>3</td><td>1</td><td>1</td><td>1</td><td>—</td><td>78%</td><td style="color:var(--danger);font-weight:700;">0.07</td><td class="delay-tag">+199d</td></tr>
    </tbody></table>
  </div>"""

ACTIVITY_G_CONCESSION = """
  <div class="panel table-panel p3-section-panel fill-grow panel-table-wrap">
    <h3>G · Concession Development Phase — 7 active activities</h3>
    <table><thead><tr><th>#</th><th>Activity</th><th>Status</th><th>Start</th><th>Due</th><th>Progress</th><th>Delay</th><th>Comments</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>1 - Silo Vendor – Manufacturing of silo materials including Clearance</td><td><span class="pill progress">In Progress</span></td><td>14 Jul</td><td>29 Nov</td><td>0%</td><td>—</td><td>—</td></tr>
      <tr><td>2</td><td>Dust Extractor - – Advance Payment</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>14 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
      <tr><td>3</td><td>Tippler – Release of Order (Cost Comparision , NFA &amp; PO/SO Approvals)</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>20 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
      <tr><td>4</td><td>Water tank - Steel - – Advance Payment</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>14 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
      <tr><td>5</td><td>3 - Detailed Drawings – Fire Fighting System with BOQ</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>08 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
      <tr><td>6</td><td>2 - Final / Pre COD Requirement – Power Connection - Application &amp; Approval</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>30 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
      <tr><td>7</td><td>3 - Fire NOC – NoC - Initial - Application &amp; Approval</td><td><span class="pill blocked">Blocked</span></td><td>01 Sept</td><td>15 Sept</td><td>0%</td><td class="delay-tag">+7d</td><td>—</td></tr>
    </tbody></table>
  </div>"""

ACTIVITY_G_EXECUTION = """
  <div class="panel table-panel p3-section-panel fill-grow panel-table-wrap">
    <h3>G · Project Execution — 4 active activities</h3>
    <table><thead><tr><th>#</th><th>Activity</th><th>Status</th><th>Start</th><th>Due</th><th>Progress</th><th>Delay</th><th>Comments</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Mid-Term Milestone – Work Hampered due to mismatch of Cumulative Qty executed</td><td><span class="pill progress">In Progress</span></td><td>31 Jul</td><td>31 Oct</td><td>0%</td><td>—</td><td>—</td></tr>
      <tr><td>2</td><td>2 - Silo 2 – Silo Dismanthling work</td><td><span class="pill progress">In Progress</span></td><td>07 Jul</td><td>13 Nov</td><td>14%</td><td>—</td><td>—</td></tr>
      <tr><td>3</td><td>3 - Silo 3 – Wall (beam) 3rd lift - Reinforcement work</td><td><span class="pill progress">In Progress</span></td><td>03 Aug</td><td>06 Nov</td><td>3%</td><td>—</td><td>—</td></tr>
      <tr><td>4</td><td>9 - Bulk loading Silo - 2*50 MT – Ramp (Excavation, Levelling, GSB, Compaction, Brickwork, PCC&amp;CC)</td><td><span class="pill blocked">Blocked</span></td><td>21 Feb</td><td>21 Feb</td><td>0%</td><td class="delay-tag">+199d</td><td>—</td></tr>
    </tbody></table>
  </div>"""

ACTIVITY_STACK = f"""
  <div class="p3-activity-stack fill-grow">
  {ACTIVITY_G_CONCESSION}
  {ACTIVITY_G_EXECUTION}
  </div>"""

ACTIVITY_SPLIT = f"""
  <div class="p3-activity-split fill-grow">
  {ACTIVITY_G_CONCESSION}
  {ACTIVITY_G_EXECUTION}
  </div>"""

ACTIVITY_EXEC_FIRST = f"""
  <div class="p3-activity-stack fill-grow p3-exec-first">
  {ACTIVITY_G_EXECUTION}
  {ACTIVITY_G_CONCESSION}
  </div>"""

ACTIVITY_SUMMARY = """
  <div class="activity-summary-row">
    <span><strong style="color:var(--text);">7 ACTIVITIES</strong> — 2 - Concession Development Phase</span>
    <span><strong style="color:var(--text);">4 ACTIVITIES</strong> — 3 - Project Execution</span>
  </div>"""

ACTIVITY_CARDS = """
  <div class="activity-cards fill-grow">
    <div class="activity-card blocked"><div class="activity-card-title">Ramp (Excavation, Levelling, GSB…)</div><div class="activity-card-meta">3 - Project Execution · Blocked · +199d</div><div class="activity-card-progress"><div style="width:0%"></div></div></div>
    <div class="activity-card progress"><div class="activity-card-title">Silo Dismanthling work</div><div class="activity-card-meta">3 - Project Execution · In Progress · 14%</div><div class="activity-card-progress"><div style="width:14%"></div></div></div>
    <div class="activity-card blocked"><div class="activity-card-title">Advance Payment</div><div class="activity-card-meta">2 - Concession Development · Blocked · +7d</div><div class="activity-card-progress"><div style="width:0%"></div></div></div>
    <div class="activity-card blocked"><div class="activity-card-title">Fire Fighting System with BOQ</div><div class="activity-card-meta">2 - Concession Development · Blocked · +7d</div><div class="activity-card-progress"><div style="width:0%"></div></div></div>
    <div class="activity-card progress"><div class="activity-card-title">Wall (beam) 3rd lift - Reinforcement</div><div class="activity-card-meta">3 - Project Execution · In Progress · 3%</div><div class="activity-card-progress"><div style="width:3%"></div></div></div>
    <div class="activity-card progress"><div class="activity-card-title">Silo Vendor – Manufacturing</div><div class="activity-card-meta">2 - Concession Development · In Progress · 0%</div><div class="activity-card-progress"><div style="width:0%"></div></div></div>
  </div>"""

ROLLUP_STATS = """
  <div class="rollup-stats">
    <div class="rollup-stat"><div class="val">11</div><div class="lbl">Active</div></div>
    <div class="rollup-stat"><div class="val">7</div><div class="lbl">Blocked</div></div>
    <div class="rollup-stat"><div class="val">4</div><div class="lbl">In Progress</div></div>
    <div class="rollup-stat danger"><div class="val">0.03</div><div class="lbl">Avg SPI</div></div>
  </div>"""


def _p1_classic(hero):
    return f"""
  <div class="page-main layout-classic">
  {hero}
  {KPI_BAND}
  <div class="two-col fill-row">{SECTION_PANEL}{STATUS_PANEL}</div>
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_sidebar(hero):
    return f"""
  <div class="page-main layout-sidebar">
    <aside class="layout-sidebar-rail">{hero}</aside>
    <div class="layout-sidebar-main">
      {KPI_BAND}
      <div class="two-col fill-row">{SECTION_PANEL}{STATUS_PANEL}</div>
      {PULSE_PANEL}
    </div>
  {TAIL}
  </div>"""


def _p1_kpi_first(hero):
    return f"""
  <div class="page-main layout-kpi-first">
  {KPI_BAND}
  {hero}
  <div class="two-col fill-row">{SECTION_PANEL}{STATUS_PANEL}</div>
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_bento(hero):
    return f"""
  <div class="page-main layout-bento">
    <div class="bento-health">{hero}</div>
    <div class="bento-kpi">{KPI_BAND}</div>
    <div class="bento-section">{SECTION_PANEL}</div>
    <div class="bento-status">{STATUS_PANEL}</div>
    <div class="bento-pulse">{PULSE_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_stack(hero):
    return f"""
  <div class="page-main layout-stack">
  {hero}
  {KPI_BAND}
  {SECTION_PANEL}
  {STATUS_PANEL_WIDE}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_split(hero):
    return f"""
  <div class="page-main layout-split">
    <div class="split-left">
      {hero}
      {SECTION_PANEL}
    </div>
    <div class="split-right">
      {KPI_BAND}
      {STATUS_PANEL}
      {PULSE_PANEL}
    </div>
  {TAIL}
  </div>"""


def _p1_three_col(hero):
    return f"""
  <div class="page-main layout-three-col">
  {hero}
  {KPI_BAND}
  {SECTION_PANEL}
  {STATUS_PANEL_WIDE}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_magazine(hero):
    return f"""
  <div class="page-main layout-magazine">
    <div class="mag-hero">{hero}</div>
    {KPI_BAND}
    <div class="mag-analytics two-col">{SECTION_PANEL}{STATUS_PANEL}</div>
    {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_pulse_top(hero):
    return f"""
  <div class="page-main layout-pulse-top">
  {PULSE_PANEL}
  {hero}
  {KPI_BAND}
  <div class="two-col fill-row">{SECTION_PANEL}{STATUS_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_executive(hero):
    return f"""
  <div class="page-main layout-executive">
  {hero}
  {KPI_BAND_4}
  {SECTION_PANEL}
  {STATUS_PANEL_WIDE}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_infographic(hero):
    return f"""
  <div class="page-main layout-infographic">
  {KPI_BAND_BIG}
  {hero}
  {SECTION_PANEL}
  {STATUS_PANEL}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_reverse(hero):
    return f"""
  <div class="page-main layout-reverse">
  {STATUS_PANEL_WIDE}
  {SECTION_PANEL}
  {KPI_BAND}
  {hero}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_ribbon(hero):
    return f"""
  <div class="page-main layout-ribbon">
  <div class="ribbon-block">{hero}</div>
  <div class="ribbon-block">{KPI_BAND}</div>
  <div class="ribbon-block two-col">{SECTION_PANEL}{STATUS_PANEL}</div>
  <div class="ribbon-block">{PULSE_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_compact_grid(hero):
    return f"""
  <div class="page-main layout-compact-grid">
    <div class="cg-a">{hero}</div>
    <div class="cg-b">{KPI_BAND}</div>
    <div class="cg-c">{SECTION_PANEL}</div>
    <div class="cg-d">{STATUS_PANEL}</div>
    <div class="cg-e">{PULSE_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_wide_status(hero):
    return f"""
  <div class="page-main layout-wide-status">
  {hero}
  {STATUS_PANEL_WIDE}
  {KPI_BAND}
  {SECTION_PANEL}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_asymmetric(hero):
    return f"""
  <div class="page-main layout-asymmetric">
    <div class="asym-top">{hero}{KPI_BAND}</div>
    <div class="asym-mid">{PULSE_PANEL}</div>
    <div class="asym-bot two-col">{SECTION_PANEL}{STATUS_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_news(hero):
    return f"""
  <div class="page-main layout-news">
    <div class="news-col">{hero}{SECTION_PANEL}</div>
    <div class="news-col news-col-mid">{KPI_BAND}{PULSE_PANEL}</div>
    <div class="news-col">{STATUS_PANEL}</div>
  {TAIL}
  </div>"""


def _p1_dashboard(hero):
    return f"""
  <div class="page-main layout-dashboard">
  {KPI_BAND}
  <div class="dash-mid two-col">
    <div>{hero}{SECTION_PANEL}</div>
    <div>{STATUS_PANEL}{PULSE_PANEL}</div>
  </div>
  {TAIL}
  </div>"""


def _p1_focus(hero):
    return f"""
  <div class="page-main layout-focus">
  <div class="focus-top">{hero}{KPI_BAND}</div>
  {SECTION_PANEL}
  {STATUS_PANEL_WIDE}
  {PULSE_PANEL}
  {TAIL}
  </div>"""


def _p1_minimal(hero):
    return f"""
  <div class="page-main layout-minimal">
  {hero}
  {PULSE_PANEL}
  {KPI_BAND}
  <div class="two-col">{SECTION_PANEL}{STATUS_PANEL}</div>
  {TAIL}
  </div>"""


PAGE1_BUILDERS = {
    "classic": _p1_classic,
    "sidebar": _p1_sidebar,
    "kpi-first": _p1_kpi_first,
    "bento": _p1_bento,
    "stack": _p1_stack,
    "split": _p1_split,
    "three-col": _p1_three_col,
    "magazine": _p1_magazine,
    "pulse-top": _p1_pulse_top,
    "executive": _p1_executive,
    "infographic": _p1_infographic,
    "reverse": _p1_reverse,
    "ribbon": _p1_ribbon,
    "compact-grid": _p1_compact_grid,
    "wide-status": _p1_wide_status,
    "asymmetric": _p1_asymmetric,
    "news": _p1_news,
    "dashboard": _p1_dashboard,
    "minimal": _p1_minimal,
    "focus": _p1_focus,
}


def _p2_grid():
    return f"""
  <div class="page-main layout-p2-grid">
  <div class="page-title-row"><h2>Critical Path &amp; Delays</h2><span>Tue, 08 Sept, 2026 · Bharuch_R4_Leaptaskflow</span></div>
  <div class="success-box"><h3>✓ A · Critical-path activities behind schedule — 0 of 4 critical-path tasks slipping</h3><p>No critical-path activities are behind schedule today — the critical chain is on track.</p></div>
  <div class="panel"><h3>B · Delayed Activities · Ranked by Days Behind — 7 delayed · reasons named · dependencies surfaced</h3></div>
  <div class="delay-cards fill-grow p2-grid-cards">{DELAY_CARDS}</div>
  <div class="page-title-row"><h2>Site Overview</h2><span>Tue, 08 Sept, 2026</span></div>
  {SITE_BLOCK}
  {TAIL}
  </div>"""


def _p2_list():
    return f"""
  <div class="page-main layout-p2-list">
  <div class="page-title-row"><h2>Critical Path &amp; Delays</h2><span>Tue, 08 Sept, 2026 · Bharuch_R4_Leaptaskflow</span></div>
  <div class="success-box"><h3>✓ Critical-path on track — 0 of 4 slipping</h3><p>No critical-path activities are behind schedule today.</p></div>
  <div class="delay-list fill-grow">{DELAY_CARDS.replace('delay-card', 'delay-card delay-list-item')}</div>
  <div class="page-title-row"><h2>Site Overview</h2><span>Tue, 08 Sept, 2026</span></div>
  {SITE_BLOCK}
  {TAIL}
  </div>"""


def _p2_timeline():
    return f"""
  <div class="page-main layout-p2-timeline">
  <div class="page-title-row"><h2>Delay Timeline</h2><span>7 delayed activities · Bharuch_R4_Leaptaskflow</span></div>
  <div class="delay-timeline fill-grow">{DELAY_CARDS.replace('delay-card', 'delay-card timeline-item')}</div>
  <div class="page-title-row"><h2>Site Overview</h2><span>Tue, 08 Sept, 2026</span></div>
  {SITE_BLOCK.replace('site-grid fill-row', 'site-grid site-stack')}
  {TAIL}
  </div>"""


def _p2_compact():
    return f"""
  <div class="page-main layout-p2-compact">
  <div class="p2-compact-head two-col">
    <div class="success-box"><h3>✓ Critical path on track</h3><p>0 of 4 critical-path tasks slipping.</p></div>
    <div class="panel"><h3>7 Delayed Activities</h3></div>
  </div>
  <div class="delay-cards p2-compact-cards fill-grow">{DELAY_CARDS}</div>
  {SITE_BLOCK.replace('site-grid fill-row', 'site-grid site-photo-top')}
  {TAIL}
  </div>"""


def _p2_magazine():
    return f"""
  <div class="page-main layout-p2-magazine">
  <div class="photo-placeholder p2-hero-photo"><span class="icon">📷</span><strong>Site Photo · 1 - Silo 1</strong><span>Tue, 08 Sept, 2026 · Bharuch</span></div>
  <div class="page-title-row"><h2>Delays &amp; Site Intel</h2><span>Tue, 08 Sept, 2026</span></div>
  <div class="delay-cards fill-grow">{DELAY_CARDS}</div>
  <div class="p2-mag-tables">{SITE_BLOCK.replace('site-grid fill-row', 'site-grid site-full').replace('<div><div class="photo-placeholder', '<div style="display:none"><div class="photo-placeholder')}</div>
  {TAIL}
  </div>"""


def _p2_side():
    return f"""
  <div class="page-main layout-p2-side">
  <div class="p2-side-wrap">
    <div class="p2-side-left">
      <div class="page-title-row"><h2>Delays</h2></div>
      <div class="delay-list">{DELAY_CARDS.replace('delay-card', 'delay-card delay-list-item')}</div>
    </div>
    <div class="p2-side-right">
      <div class="success-box"><h3>✓ Critical path OK</h3><p>0 slipping.</p></div>
      {SITE_BLOCK}
    </div>
  </div>
  {TAIL}
  </div>"""


def _p2_table():
    return f"""
  <div class="page-main layout-p2-table">
  <div class="page-title-row"><h2>Delayed Activities Register</h2><span>7 items · ranked by days behind</span></div>
  <div class="panel panel-table-wrap">
    <h3>B · Delayed Activities Register</h3>
    <table><thead><tr><th>Activity</th><th>Section</th><th>Delay</th><th>Reason</th></tr></thead>
    <tbody>
      <tr><td>Ramp (Excavation, Levelling…)</td><td>3 - Project Execution</td><td class="delay-tag">+199d</td><td>Past planned start</td></tr>
      <tr><td>Advance Payment</td><td>2 - Concession Development</td><td class="delay-tag">+7d</td><td>Not started</td></tr>
      <tr><td>Release of Order</td><td>2 - Concession Development</td><td class="delay-tag">+7d</td><td>Blocked</td></tr>
      <tr><td>Fire Fighting System</td><td>2 - Concession Development</td><td class="delay-tag">+7d</td><td>Not started</td></tr>
      <tr><td>Power Connection</td><td>2 - Concession Development</td><td class="delay-tag">+7d</td><td>Not started</td></tr>
      <tr><td>NoC - Initial</td><td>2 - Concession Development</td><td class="delay-tag">+7d</td><td>Not started</td></tr>
    </tbody></table>
  </div>
  {SITE_BLOCK}
  {TAIL}
  </div>"""


PAGE2_BUILDERS = {
    "grid": _p2_grid,
    "list": _p2_list,
    "timeline": _p2_timeline,
    "compact": _p2_compact,
    "magazine": _p2_magazine,
    "side": _p2_side,
    "table": _p2_table,
}


def _p3_stacked():
    return f"""
  <div class="page-main layout-p3-stacked">
  <div class="page-title-row"><h2>Activity Rollup &amp; Register</h2><span>Tue, 08 Sept, 2026 · Bharuch_R4_Leaptaskflow</span></div>
  {ROLLUP_TABLE}
  {ACTIVITY_STACK}
  {ACTIVITY_SUMMARY}
  </div>"""


def _p3_split_sections():
    return f"""
  <div class="page-main layout-p3-split-sections">
  <div class="page-title-row"><h2>Activity Rollup &amp; Register</h2><span>Tue, 08 Sept, 2026</span></div>
  {ROLLUP_TABLE}
  {ACTIVITY_SPLIT}
  {ACTIVITY_SUMMARY}
  </div>"""


def _p3_exec_first():
    return f"""
  <div class="page-main layout-p3-exec-first">
  <div class="page-title-row"><h2>Project Execution Focus</h2><span>11 active · Bharuch_R4_Leaptaskflow</span></div>
  {ROLLUP_TABLE}
  {ACTIVITY_EXEC_FIRST}
  {ACTIVITY_SUMMARY}
  </div>"""


def _p3_standard():
    return _p3_stacked()


def _p3_cards():
    return f"""
  <div class="page-main layout-p3-cards">
  <div class="page-title-row"><h2>Activity Register — Card View</h2><span>11 active · Bharuch_R4_Leaptaskflow</span></div>
  {ROLLUP_STATS}
  {ROLLUP_TABLE}
  {ACTIVITY_CARDS}
  {ACTIVITY_SUMMARY}
  </div>"""


def _p3_split():
    return f"""
  <div class="page-main layout-p3-split">
  <div class="page-title-row"><h2>Activity Rollup &amp; Register</h2><span>Tue, 08 Sept, 2026</span></div>
  <div class="p3-split-wrap">
    <div class="p3-split-left">{ROLLUP_TABLE}{ROLLUP_STATS}</div>
    <div class="p3-split-right">{ACTIVITY_STACK}</div>
  </div>
  {ACTIVITY_SUMMARY}
  </div>"""


def _p3_summary_top():
    return f"""
  <div class="page-main layout-p3-summary">
  {ROLLUP_STATS}
  <div class="page-title-row"><h2>Full Activity Register</h2><span>11 active leaf activities</span></div>
  {ROLLUP_TABLE}
  {ACTIVITY_STACK}
  </div>"""


def _p3_compact():
    return f"""
  <div class="page-main layout-p3-compact">
  <div class="page-title-row"><h2>Activity Rollup</h2><span>Compact register view</span></div>
  {ROLLUP_TABLE}
  {ACTIVITY_SPLIT}
  </div>"""


def _p3_rollup_focus():
    return f"""
  <div class="page-main layout-p3-rollup">
  <div class="page-title-row"><h2>Section Rollup Dashboard</h2><span>Worst SPI first</span></div>
  {ROLLUP_STATS}
  {ROLLUP_TABLE}
  {ACTIVITY_SPLIT}
  {ACTIVITY_SUMMARY}
  </div>"""


PAGE3_BUILDERS = {
    "stacked": _p3_stacked,
    "split-sections": _p3_split_sections,
    "exec-first": _p3_exec_first,
    "standard": _p3_standard,
    "cards": _p3_cards,
    "split": _p3_split,
    "summary-top": _p3_summary_top,
    "compact": _p3_compact,
    "rollup-focus": _p3_rollup_focus,
}


DESIGN_PAGE_LAYOUTS = {
    "first-design": {"page1": "classic", "page2": "grid", "page3": "stacked"},
    "second-design": {"page1": "sidebar", "page2": "list", "page3": "split-sections"},
    "third-design": {"page1": "kpi-first", "page2": "timeline", "page3": "exec-first"},
    "fourth-design": {"page1": "bento", "page2": "compact", "page3": "summary-top"},
    "fifth-design": {"page1": "stack", "page2": "magazine", "page3": "split"},
    "sixth-design": {"page1": "split", "page2": "side", "page3": "compact"},
    "seventh-design": {"page1": "three-col", "page2": "table", "page3": "rollup-focus"},
    "eighth-design": {"page1": "magazine", "page2": "grid", "page3": "cards"},
    "ninth-design": {"page1": "pulse-top", "page2": "list", "page3": "stacked"},
    "tenth-design": {"page1": "executive", "page2": "timeline", "page3": "split-sections"},
    "eleventh-design": {"page1": "infographic", "page2": "compact", "page3": "exec-first"},
    "twelfth-design": {"page1": "reverse", "page2": "magazine", "page3": "summary-top"},
    "thirteenth-design": {"page1": "ribbon", "page2": "side", "page3": "split"},
    "fourteenth-design": {"page1": "compact-grid", "page2": "table", "page3": "compact"},
    "fifteenth-design": {"page1": "wide-status", "page2": "grid", "page3": "rollup-focus"},
    "sixteenth-design": {"page1": "asymmetric", "page2": "list", "page3": "stacked"},
    "seventeenth-design": {"page1": "news", "page2": "timeline", "page3": "split-sections"},
    "eighteenth-design": {"page1": "dashboard", "page2": "compact", "page3": "cards"},
    "nineteenth-design": {"page1": "minimal", "page2": "magazine", "page3": "exec-first"},
    "twentieth-design": {"page1": "focus", "page2": "side", "page3": "summary-top"},
}


def build_document_body(slug, hero_section):
    layouts = DESIGN_PAGE_LAYOUTS.get(slug, {"page1": "classic", "page2": "grid", "page3": "stacked"})
    p1 = PAGE1_BUILDERS[layouts["page1"]](hero_section)
    p2 = PAGE2_BUILDERS[layouts["page2"]]()
    p3 = PAGE3_BUILDERS[layouts["page3"]]()

    return f"""
<section class="page page-layout-{layouts['page1']}">
{BANNER}
{ALERT}
{p1}
  <footer class="footer"><span>Section 1 · Briefing · KPIs · Section &amp; Status Mix</span><span>Bharuch_R4_Leaptaskflow · Tue, 08 Sept, 2026</span></footer>
</section>

<section class="page page-layout-p2-{layouts['page2']}">
{p2}
  <footer class="footer"><span>Section 2 · Critical Path &amp; Delays · Site Overview</span><span>Bharuch_R4_Leaptaskflow · Tue, 08 Sept, 2026</span></footer>
</section>

<section class="page page-layout-p3-{layouts['page3']}">
{p3}
  <footer class="footer"><span>Section 3 · Activity Rollup · Register</span><span>Bharuch_R4_Leaptaskflow · Tue, 08 Sept, 2026 · LEAP INDIA TASKFLOW</span></footer>
</section>"""


LAYOUT_CSS = """
    .status-grid.status-row-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 4px; }
    .layout-sidebar { display: grid; grid-template-columns: minmax(0, 260px) minmax(0, 1fr); gap: 8px; align-items: start; }
    .layout-sidebar-rail { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .layout-sidebar-main { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .layout-sidebar-rail .hero-strip-body { grid-template-columns: 1fr; }
    .layout-sidebar-rail .people-card { margin-top: 8px; }
    .layout-bento { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); gap: 6px; }
    .bento-health { grid-column: span 12; }
    .bento-kpi { grid-column: span 8; }
    .bento-section { grid-column: span 4; }
    .bento-status { grid-column: span 7; }
    .bento-pulse { grid-column: span 5; }
    .layout-stack { display: flex; flex-direction: column; gap: 6px; }
    .layout-split { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px; }
    .split-left, .split-right { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .layout-three-col { display: flex; flex-direction: column; gap: 6px; }
    .layout-magazine .mag-hero { margin-bottom: 4px; }
    .layout-magazine .mag-analytics { margin-top: 4px; }
    .layout-pulse-top { display: flex; flex-direction: column; gap: 6px; }
    .layout-executive .kpi-grid-4 { grid-template-columns: repeat(4, 1fr); }
    .layout-focus .focus-top { display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 8px; align-items: start; }
    .layout-infographic .kpi-grid-big .kpi-value { font-size: 32px; }
    .layout-infographic .kpi-grid-big .kpi { padding: 16px; min-height: 96px; }
    .layout-ribbon .ribbon-block { border-left: 4px solid var(--accent); padding-left: 12px; margin-bottom: 8px; }
    .layout-compact-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); grid-template-rows: auto auto auto; gap: 6px; }
    .layout-compact-grid .cg-e { grid-column: span 2; }
    .layout-wide-status { display: flex; flex-direction: column; gap: 6px; }
    .layout-asymmetric .asym-top { display: grid; grid-template-columns: minmax(0, 1.2fr) minmax(0, 1fr); gap: 8px; }
    .layout-asymmetric .asym-mid { margin: 4px 0; }
    .layout-news { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr) minmax(0, 1fr); gap: 8px; align-items: start; }
    .news-col { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .layout-dashboard .dash-mid { align-items: stretch; }
    .layout-dashboard .dash-mid > div { display: flex; flex-direction: column; gap: 6px; }
    .layout-minimal { display: flex; flex-direction: column; gap: 8px; }
    .delay-list { display: flex; flex-direction: column; gap: 6px; }
    .delay-list-item { width: 100%; }
    .layout-p2-timeline .delay-timeline { display: flex; flex-direction: column; gap: 0; border-left: 3px solid var(--accent); padding-left: 16px; margin-left: 8px; }
    .layout-p2-timeline .timeline-item { position: relative; margin-bottom: 10px; }
    .layout-p2-timeline .timeline-item::before { content: ""; position: absolute; left: -22px; top: 14px; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }
    .p2-compact-cards { grid-template-columns: repeat(3, 1fr); }
    .p2-compact-head { margin-bottom: 10px; }
    .p2-hero-photo { min-height: 140px; margin-bottom: 12px; border-radius: 12px; }
    .layout-p2-side .p2-side-wrap { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.2fr); gap: 8px; }
    .p2-side-left, .p2-side-right { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
    .site-stack { grid-template-columns: 1fr; }
    .site-photo-top { grid-template-columns: 1fr; }
    .site-full { grid-template-columns: 1fr; }
    .rollup-stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px; margin-bottom: 8px; }
    .rollup-stat { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 8px; text-align: center; min-width: 0; }
    .rollup-stat .val { font-size: 28px; font-weight: 800; color: var(--accent); }
    .rollup-stat.danger .val { color: var(--danger); }
    .rollup-stat .lbl { font-size: 10px; text-transform: uppercase; font-weight: 600; opacity: 0.75; margin-top: 4px; line-height: 1.3; white-space: normal; }
    .activity-cards { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px; }
    .activity-card { background: var(--card); border: 1px solid var(--border); border-left: 4px solid var(--warn); border-radius: 8px; padding: 6px 8px; min-width: 0; }
    .activity-card.blocked { border-left-color: var(--danger); }
    .activity-card.progress { border-left-color: var(--ok); }
    .activity-card-title { font-weight: 600; font-size: 12px; margin-bottom: 4px; line-height: 1.35; white-space: normal; }
    .activity-card-meta { font-size: 12px; opacity: 0.75; margin-bottom: 8px; }
    .activity-card-progress { height: 6px; background: var(--border); border-radius: 3px; overflow: hidden; }
    .activity-card-progress div { height: 100%; background: var(--accent); border-radius: 3px; }
    .layout-p3-split .p3-split-wrap { display: grid; grid-template-columns: minmax(0, 320px) minmax(0, 1fr); gap: 8px; align-items: stretch; flex: 1; min-height: 0; }
    .p3-split-left, .p3-split-right { display: flex; flex-direction: column; gap: 6px; min-width: 0; min-height: 0; }
    .layout-p3-stacked, .layout-p3-split-sections, .layout-p3-exec-first, .layout-p3-summary, .layout-p3-rollup, .layout-p3-compact, .layout-p3-split, .layout-p3-cards {
      display: flex; flex-direction: column; gap: 6px; min-height: 0;
    }
    .p3-activity-stack { display: flex; flex-direction: column; gap: 6px; flex: 1; min-height: 0; }
    .p3-activity-split { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 8px; flex: 1; min-height: 0; align-items: stretch; }
    .p3-section-panel { flex: 1; display: flex; flex-direction: column; min-height: 140px; background: var(--card); }
    .p3-section-panel table { flex: 1; }
    .p3-exec-first .p3-section-panel:first-child { border-left: 4px solid var(--danger); }
    .layout-p3-exec-first .p3-section-panel:last-child { opacity: 0.95; }
    .delay-list-item { width: 100%; min-width: 0; }
    .page-title-row { flex-wrap: wrap; gap: 6px; }
    .page-title-row h2, .page-title-row span { min-width: 0; white-space: normal; line-height: 1.35; }
    .health-bar-right, .health-meta, .health-pill-body, .health-wave-body, .health-seg-body { min-width: 0; white-space: normal; line-height: 1.35; }
    .table-compact table { font-size: 11px; }
"""
