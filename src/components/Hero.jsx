import { useRef } from 'react'
import gsap from 'gsap'
import { HiArrowDownTray, HiArrowRight } from 'react-icons/hi2'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from '../hooks/useGsap'
import { useSplitReveal } from '../hooks/useSplitReveal'
import { useMagnetic } from '../hooks/useMagnetic'
import { useCursorSpotlight } from '../hooks/useCursorSpotlight'
import { profile } from '../data/profile'

export default function Hero() {
  const nameRef = useSplitReveal({ delay: 0.15, stagger: 0.08 })
  const rootRef = useCursorSpotlight({ targetSelector: '[data-spotlight]' })
  const timelineRef = useRef(null)
  const primaryCtaRef = useMagnetic({ strength: 0.35, radius: 140 })
  const ghostCtaRef = useMagnetic({ strength: 0.3, radius: 140 })

  useIsomorphicLayoutEffect(() => {
    const reduced = prefersReducedMotion()
    if (reduced || !rootRef.current) return

    const ctx = gsap.context(() => {
      const tl = gsap.timeline({ defaults: { ease: 'power3.out' } })
      tl.from('[data-hero-eyebrow]', { opacity: 0, y: 16, duration: 0.6 }, 0)
        .from(
          '[data-hero-sub]',
          { opacity: 0, y: 20, duration: 0.8 },
          '-=0.2'
        )
        .from(
          '[data-hero-tagline]',
          { opacity: 0, y: 20, duration: 0.8 },
          '-=0.55'
        )
        .from(
          '[data-hero-cta]',
          { opacity: 0, y: 16, duration: 0.7, stagger: 0.1 },
          '-=0.5'
        )
        .from(
          '[data-hero-meta]',
          { opacity: 0, y: 12, duration: 0.6, stagger: 0.05 },
          '-=0.4'
        )
        .from(
          '[data-hero-scroll]',
          { opacity: 0, duration: 0.8 },
          '-=0.2'
        )
      timelineRef.current = tl

      gsap.to('[data-orb]', {
        y: 20,
        duration: 6,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        stagger: { each: 0.8, from: 'random' },
      })

      gsap.to('[data-orb]', {
        xPercent: (i) => (i % 2 === 0 ? 6 : -6),
        duration: 9,
        ease: 'sine.inOut',
        yoyo: true,
        repeat: -1,
        stagger: { each: 1.2, from: 'random' },
      })

      gsap.fromTo(
        '[data-hero-scroll-dot]',
        { y: -12, opacity: 0 },
        {
          y: 40,
          opacity: 1,
          duration: 1.6,
          ease: 'power1.inOut',
          repeat: -1,
          repeatDelay: 0.2,
        }
      )
    }, rootRef)

    return () => ctx.revert()
  }, [])

  const resumeHref = `${import.meta.env.BASE_URL}${profile.resumeFile}`

  return (
    <section
      id="hero"
      ref={rootRef}
      className="relative min-h-[100svh] flex items-center overflow-hidden pt-24"
      aria-label="Introduction"
    >
      <div className="absolute inset-0 -z-10">
        <div className="absolute inset-0 grid-bg opacity-70" />
        <div
          data-orb
          className="glow-orb w-[520px] h-[520px] bg-accent/40 -top-40 -left-32"
        />
        <div
          data-orb
          className="glow-orb w-[420px] h-[420px] bg-cyan-neon/25 top-1/3 -right-24"
        />
        <div
          data-orb
          className="glow-orb w-[360px] h-[360px] bg-fuchsia-500/20 bottom-0 left-1/3"
        />
        <div
          data-spotlight
          aria-hidden="true"
          className="cursor-spotlight"
        />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-ink-950" />
      </div>

      <div className="container-max px-4 md:px-8 w-full">
        <div className="max-w-4xl">
          <span data-hero-eyebrow className="eyebrow mb-8">
            <span>Portfolio · 2026</span>
          </span>

          <h1
            ref={nameRef}
            className="font-display text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-semibold leading-[1.02] tracking-tight text-white"
          >
            {profile.name}
          </h1>

          <p
            data-hero-sub
            className="mt-4 font-display text-2xl sm:text-3xl md:text-4xl font-medium"
          >
            <span className="text-gradient">{profile.role}</span>
            <span className="text-slate-400"> — {profile.focus}</span>
          </p>

          <p
            data-hero-tagline
            className="mt-6 max-w-2xl text-base sm:text-lg text-slate-400 leading-relaxed"
          >
            {profile.tagline}
          </p>

          <div className="mt-10 flex flex-wrap items-center gap-4">
            <a
              ref={primaryCtaRef}
              data-hero-cta
              href={resumeHref}
              target="_blank"
              rel="noreferrer"
              className="btn btn-primary"
            >
              <HiArrowDownTray aria-hidden="true" />
              View Resume
            </a>
            <a
              ref={ghostCtaRef}
              data-hero-cta
              href="#contact"
              onClick={(e) => {
                e.preventDefault()
                document
                  .querySelector('#contact')
                  ?.scrollIntoView({ behavior: 'smooth' })
              }}
              className="btn btn-ghost"
            >
              Contact
              <HiArrowRight aria-hidden="true" />
            </a>
          </div>

          <ul className="mt-14 grid grid-cols-2 sm:grid-cols-4 gap-6 max-w-3xl text-sm">
            {[
              ['Experience', `${profile.yearsExperience} yrs`],
              ['Current', profile.currentCompany],
              ['Previously', profile.previousCompany],
              ['Focus', 'IoT · Embedded · UI'],
            ].map(([label, value]) => (
              <li key={label} data-hero-meta className="border-l border-white/10 pl-4">
                <div className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                  {label}
                </div>
                <div className="mt-1 text-slate-200">{value}</div>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div
        data-hero-scroll
        className="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 text-xs text-slate-500 font-mono"
        aria-hidden="true"
      >
        <span className="tracking-widest uppercase">Scroll</span>
        <span className="relative w-px h-10 overflow-hidden bg-white/10">
          <span
            data-hero-scroll-dot
            className="absolute left-1/2 -translate-x-1/2 top-0 h-3 w-px bg-accent shadow-glow"
          />
        </span>
      </div>
    </section>
  )
}
