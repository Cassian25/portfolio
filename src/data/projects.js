export const projects = [
  {
    id: 'rdpms',
    title: 'RDPMS',
    subtitle: 'Real-time Sensor & Device Monitoring',
    description:
      'A real-time monitoring platform that ingests high-frequency sensor and device telemetry, visualises live streams, and surfaces anomalies. Built for industrial IoT deployments with a Flutter frontend, Python services, and ClickHouse for time-series storage.',
    highlights: [
      'Sub-second telemetry pipeline with ClickHouse-backed queries',
      'Cross-platform Flutter client for control-room and mobile use',
      'Modular Python services for ingestion, alerts, and health checks',
    ],
    tags: ['Flutter', 'Python', 'ClickHouse', 'IoT', 'Realtime'],
    github: '',
    live: '',
    accent: 'from-violet-500/40 via-fuchsia-500/20 to-cyan-500/10',
  },
  {
    id: 'bcs',
    title: 'BCS · Boiler Control System',
    subtitle: '14-module Navy Boiler Control Frontend',
    description:
      'A mission-critical, 14-module control-system frontend for Navy boiler operations, backed by PostgreSQL. Delivered dense operator interfaces, live process schematics, and safety-oriented interaction patterns validated against strict industrial standards.',
    highlights: [
      'Deep interface for 14 interlinked control modules',
      'PostgreSQL-backed telemetry, alarms, and audit trail',
      'Hardened UX for high-stakes, 24/7 operator workflows',
    ],
    tags: ['Frontend', 'PostgreSQL', 'Industrial', 'SCADA-style'],
    github: '',
    live: '',
    accent: 'from-cyan-500/30 via-sky-500/20 to-indigo-500/10',
  },
  {
    id: 'bi-dashboard',
    title: 'Interactive BI Dashboard',
    subtitle: 'React Analytics Cockpit',
    description:
      'A React-based business intelligence dashboard delivering interactive charts, cross-filtering, and drill-down analytics. Focused on responsive performance with large datasets and a clean, information-dense visual language.',
    highlights: [
      'Composable chart primitives with cross-filtering',
      'Optimised rendering for large, mixed-cardinality datasets',
      'Themeable dark UI tuned for long analyst sessions',
    ],
    tags: ['React', 'Data Viz', 'UX', 'Performance'],
    github: '',
    live: '',
    accent: 'from-emerald-500/30 via-teal-500/20 to-violet-500/10',
  },
]
