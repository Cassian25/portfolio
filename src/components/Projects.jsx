import { useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { HiArrowUpRight } from 'react-icons/hi2'
import { FaGithub } from 'react-icons/fa6'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from '../hooks/useGsap'
import { useTilt } from '../hooks/useTilt'
import { projects } from '../data/projects'

gsap.registerPlugin(ScrollTrigger)

function ProjectCard({ project, index }) {
  const tiltRef = useTilt({ max: 6, scale: 1.015, glareSelector: '[data-glare]' })
  const cardRef = useRef(null)

  useIsomorphicLayoutEffect(() => {
    if (!cardRef.current) return
    const reduced = prefersReducedMotion()

    const ctx = gsap.context(() => {
      gsap.from(cardRef.current, {
        opacity: 0,
        y: reduced ? 0 : 60,
        rotateX: reduced ? 0 : 8,
        transformPerspective: 1000,
        duration: 1,
        ease: 'power3.out',
        scrollTrigger: {
          trigger: cardRef.current,
          start: 'top 82%',
          toggleActions: 'play none none none',
        },
      })

      if (!reduced) {
        gsap.to(cardRef.current.querySelector('[data-halo]'), {
          yPercent: -18,
          ease: 'none',
          scrollTrigger: {
            trigger: cardRef.current,
            start: 'top bottom',
            end: 'bottom top',
            scrub: true,
          },
        })
      }
    }, cardRef)

    return () => ctx.revert()
  }, [])

  const setRefs = (node) => {
    cardRef.current = node
    tiltRef.current = node
  }

  return (
    <article
      ref={setRefs}
      className="card group relative p-5 sm:p-8 md:p-10 overflow-hidden"
      aria-labelledby={`project-${project.id}-title`}
    >
      <div
        data-halo
        aria-hidden="true"
        className={`pointer-events-none absolute -inset-x-10 -top-24 h-72 opacity-70 blur-3xl bg-gradient-to-br ${project.accent}`}
      />

      <div
        data-glare
        aria-hidden="true"
        className="pointer-events-none absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 mix-blend-overlay"
        style={{
          background:
            'radial-gradient(240px circle at var(--gx, 50%) var(--gy, 50%), rgba(255,255,255,0.12), transparent 60%)',
        }}
      />

      <div className="relative grid md:grid-cols-[auto_1fr] gap-4 md:gap-10 items-start">
        <div className="flex items-start gap-4">
          <span
            aria-hidden="true"
            className="font-mono text-xs sm:text-sm text-slate-500 mt-1"
          >
            {String(index + 1).padStart(2, '0')}
          </span>
        </div>

        <div>
          <div className="flex flex-col sm:flex-row sm:flex-wrap sm:items-start sm:justify-between gap-4">
            <div className="min-w-0">
              <h3
                id={`project-${project.id}-title`}
                className="font-display text-xl sm:text-3xl md:text-4xl font-semibold text-white tracking-tight break-words"
              >
                {project.title}
              </h3>
              <p className="mt-1 text-sm sm:text-base text-accent-soft break-words">
                {project.subtitle}
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-2">
              {project.github && (
                <a
                  href={project.github}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-ghost text-xs sm:text-sm px-3 py-1.5"
                  aria-label={`${project.title} on GitHub`}
                >
                  <FaGithub aria-hidden="true" />
                  Code
                </a>
              )}
              {project.live && (
                <a
                  href={project.live}
                  target="_blank"
                  rel="noreferrer"
                  className="btn btn-primary text-xs sm:text-sm px-3 py-1.5"
                  aria-label={`${project.title} live demo`}
                >
                  Live
                  <HiArrowUpRight aria-hidden="true" />
                </a>
              )}
            </div>
          </div>

          <p className="mt-5 sm:mt-6 text-sm sm:text-base text-slate-300 leading-relaxed max-w-3xl">
            {project.description}
          </p>

          {project.highlights?.length > 0 && (
            <ul className="mt-5 sm:mt-6 grid gap-2 max-w-3xl">
              {project.highlights.map((h) => (
                <li
                  key={h}
                  className="flex items-start gap-3 text-xs sm:text-sm text-slate-400"
                >
                  <span
                    aria-hidden="true"
                    className="mt-1.5 sm:mt-2 h-1.5 w-1.5 rounded-full bg-accent shrink-0"
                  />
                  <span>{h}</span>
                </li>
              ))}
            </ul>
          )}

          <ul className="mt-6 sm:mt-8 flex flex-wrap gap-2">
            {project.tags.map((tag) => (
              <li
                key={tag}
                className="text-xs font-mono uppercase tracking-widest px-2.5 py-1 rounded-full border border-white/10 bg-white/[0.03] text-slate-300"
              >
                {tag}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </article>
  )
}

export default function Projects() {
  const headerRef = useRef(null)

  useIsomorphicLayoutEffect(() => {
    if (!headerRef.current) return
    const ctx = gsap.context(() => {
      gsap.from('[data-projects-eyebrow], [data-projects-title], [data-projects-lede]', {
        opacity: 0,
        y: 24,
        duration: 0.9,
        ease: 'power3.out',
        stagger: 0.12,
        scrollTrigger: {
          trigger: headerRef.current,
          start: 'top 85%',
        },
      })
    }, headerRef)
    return () => ctx.revert()
  }, [])

  return (
    <section
      id="projects"
      className="section relative"
      aria-labelledby="projects-heading"
    >
      <div className="container-max">
        <header ref={headerRef} className="max-w-3xl">
          <span data-projects-eyebrow className="eyebrow">
            <span>02 · Selected Work</span>
          </span>
          <h2
            id="projects-heading"
            data-projects-title
            className="mt-6 font-display text-3xl sm:text-4xl md:text-5xl font-semibold leading-tight text-white"
          >
            Projects that shipped in{' '}
            <span className="text-gradient">the real world</span>.
          </h2>
          <p
            data-projects-lede
            className="mt-4 sm:mt-5 text-slate-400 text-sm sm:text-lg leading-relaxed"
          >
            A handful of the systems I&apos;ve built or contributed to — from
            fleet-scale telemetry to safety-critical control interfaces.
          </p>
        </header>

        <div className="mt-10 sm:mt-14 grid gap-6 sm:gap-8">
          {projects.map((p, i) => (
            <ProjectCard key={p.id} project={p} index={i} />
          ))}
        </div>
      </div>
    </section>
  )
}
