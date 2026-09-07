import { useEffect, useState } from 'react'
import gsap from 'gsap'
import { useIsomorphicLayoutEffect } from '../hooks/useGsap'

const NAV_ITEMS = [
  { label: 'About', href: '#about' },
  { label: 'Projects', href: '#projects' },
  { label: 'Resume', href: '#resume' },
  { label: 'Contact', href: '#contact' },
]

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false)
  const [open, setOpen] = useState(false)

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24)
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  useIsomorphicLayoutEffect(() => {
    gsap.from('[data-nav-item]', {
      y: -12,
      opacity: 0,
      duration: 0.6,
      ease: 'power3.out',
      stagger: 0.06,
      delay: 0.2,
    })
    gsap.from('[data-nav-logo]', {
      y: -12,
      opacity: 0,
      duration: 0.6,
      ease: 'power3.out',
    })
  }, [])

  const handleNav = (href) => {
    setOpen(false)
    const el = document.querySelector(href)
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  return (
    <header
      className={[
        'fixed inset-x-0 top-0 z-50 transition-all duration-500',
        scrolled
          ? 'backdrop-blur-md bg-ink-950/70 border-b border-white/5'
          : 'bg-transparent',
      ].join(' ')}
    >
      <nav
        className="container-max flex items-center justify-between h-16 px-4 md:px-8"
        aria-label="Primary"
      >
        <a
          href="#hero"
          onClick={(e) => {
            e.preventDefault()
            handleNav('#hero')
          }}
          data-nav-logo
          className="group flex items-center gap-2 font-display font-semibold text-white"
        >
          <span className="grid place-items-center w-8 h-8 rounded-lg bg-gradient-to-br from-accent to-cyan-neon shadow-glow">
            <span className="font-mono text-xs">K</span>
          </span>
          <span className="tracking-tight">
            karthikeya<span className="text-accent">.</span>dev
          </span>
        </a>

        <ul className="hidden md:flex items-center gap-1">
          {NAV_ITEMS.map((item) => (
            <li key={item.href} data-nav-item>
              <a
                href={item.href}
                onClick={(e) => {
                  e.preventDefault()
                  handleNav(item.href)
                }}
                className="px-3 py-2 text-sm text-slate-300 hover:text-white transition-colors rounded-md relative group"
              >
                {item.label}
                <span className="absolute inset-x-3 -bottom-0.5 h-px bg-accent scale-x-0 group-hover:scale-x-100 origin-left transition-transform" />
              </a>
            </li>
          ))}
          <li data-nav-item className="ml-2">
            <a
              href="#contact"
              onClick={(e) => {
                e.preventDefault()
                handleNav('#contact')
              }}
              className="btn btn-primary text-sm px-4 py-2"
            >
              Let&apos;s talk
            </a>
          </li>
        </ul>

        <button
          type="button"
          aria-label={open ? 'Close menu' : 'Open menu'}
          aria-expanded={open}
          onClick={() => setOpen((o) => !o)}
          className="md:hidden p-2 rounded-md border border-white/10 bg-white/5"
        >
          <span
            className={[
              'block w-5 h-0.5 bg-white transition-transform',
              open ? 'translate-y-1.5 rotate-45' : '',
            ].join(' ')}
          />
          <span
            className={[
              'block w-5 h-0.5 bg-white mt-1 transition-opacity',
              open ? 'opacity-0' : 'opacity-100',
            ].join(' ')}
          />
          <span
            className={[
              'block w-5 h-0.5 bg-white mt-1 transition-transform',
              open ? '-translate-y-1.5 -rotate-45' : '',
            ].join(' ')}
          />
        </button>
      </nav>

      <div
        className={[
          'md:hidden overflow-hidden transition-[max-height,opacity] duration-500 ease-out',
          open ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0',
        ].join(' ')}
      >
        <ul className="flex flex-col gap-1 px-4 pb-4 pt-2 bg-ink-900/90 backdrop-blur border-t border-white/5">
          {NAV_ITEMS.map((item) => (
            <li key={item.href}>
              <a
                href={item.href}
                onClick={(e) => {
                  e.preventDefault()
                  handleNav(item.href)
                }}
                className="block px-3 py-3 rounded-md text-slate-200 hover:bg-white/5"
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </header>
  )
}
