import { useScrollReveal } from '../hooks/useScrollReveal'
import { skills } from '../data/skills'
import { profile } from '../data/profile'

const MARQUEE_ITEMS = [
  'Available for work',
  'Digitalization',
  'Automation',
  'IoT',
  'Embedded',
  'React · Flutter',
  'ClickHouse · PostgreSQL',
  'Realtime dashboards',
]

export default function About() {
  const ref = useScrollReveal({ selector: '[data-reveal]', stagger: 0.08 })

  return (
    <section
      id="about"
      ref={ref}
      className="section relative"
      aria-labelledby="about-heading"
    >
      <div className="container-max grid lg:grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] gap-12 lg:gap-20">
        <div>
          <span data-reveal className="eyebrow">
            <span>01 · About</span>
          </span>

          <h2
            id="about-heading"
            data-reveal
            className="mt-6 font-display text-4xl md:text-5xl font-semibold leading-tight text-white"
          >
            Software that talks to the{' '}
            <span className="text-gradient">physical world</span>.
          </h2>

          <div className="mt-8 space-y-5 text-slate-300 leading-relaxed max-w-xl">
            <p data-reveal>
              I&apos;m a Junior Software Engineer focused on{' '}
              <span className="text-white">
                digitalization and automation
              </span>{' '}
              — the messy, rewarding intersection of firmware, backend
              services, and the interfaces that make them usable.
            </p>
            <p data-reveal>
              Over{' '}
              <span className="text-white">
                {profile.yearsExperience} years
              </span>{' '}
              I&apos;ve shipped IoT platforms, embedded integrations, and
              production frontends — currently at{' '}
              <span className="text-white">{profile.currentCompany}</span>,
              previously at{' '}
              <span className="text-white">{profile.previousCompany}</span>.
            </p>
            <p data-reveal>
              <span className="text-white">{profile.education.degree}</span> ·{' '}
              {profile.education.school} · {profile.education.years}.
            </p>
          </div>
        </div>

        <div>
          <div data-reveal className="text-xs uppercase tracking-widest text-slate-500 font-mono mb-6">
            Tech I work with
          </div>

          <ul className="grid grid-cols-3 sm:grid-cols-3 gap-3">
            {skills.map(({ name, Icon, color }) => (
              <li
                key={name}
                data-reveal
                className="card p-4 flex flex-col items-center justify-center text-center gap-3 aspect-square group"
              >
                <Icon
                  aria-hidden="true"
                  className="w-8 h-8 md:w-9 md:h-9 transition-transform duration-500 group-hover:scale-110 group-hover:-rotate-6"
                  style={{ color }}
                />
                <span className="text-sm text-slate-200">{name}</span>
              </li>
            ))}
          </ul>

          <ul className="mt-8 grid grid-cols-2 gap-3 text-sm">
            <li data-reveal className="card p-4">
              <div className="text-slate-500 text-xs uppercase tracking-widest font-mono">
                Domains
              </div>
              <div className="mt-2 text-slate-200">
                IoT · Embedded · Frontend · Data
              </div>
            </li>
            <li data-reveal className="card p-4">
              <div className="text-slate-500 text-xs uppercase tracking-widest font-mono">
                Working style
              </div>
              <div className="mt-2 text-slate-200">
                Pragmatic · Reliability-first
              </div>
            </li>
          </ul>
        </div>
      </div>

      <div
        data-reveal
        className="mt-16 relative overflow-hidden border-y border-white/5 py-4 bg-white/[0.015]"
        aria-hidden="true"
      >
        <div className="flex gap-10 whitespace-nowrap animate-marquee w-max">
          {[...MARQUEE_ITEMS, ...MARQUEE_ITEMS].map((item, i) => (
            <span
              key={i}
              className="flex items-center gap-10 text-slate-400 font-mono text-xs uppercase tracking-[0.25em]"
            >
              {item}
              <span className="w-1.5 h-1.5 rounded-full bg-accent/60" />
            </span>
          ))}
        </div>
      </div>
    </section>
  )
}
