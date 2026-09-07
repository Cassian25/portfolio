import { useState } from 'react'
import { HiEnvelope, HiArrowRight } from 'react-icons/hi2'
import { FaGithub, FaLinkedin } from 'react-icons/fa6'
import { useScrollReveal } from '../hooks/useScrollReveal'
import { profile } from '../data/profile'

export default function Contact() {
  const ref = useScrollReveal({ selector: '[data-reveal]', stagger: 0.09 })
  const [form, setForm] = useState({ name: '', email: '', message: '' })
  const [status, setStatus] = useState('idle')

  const handleChange = (e) =>
    setForm((f) => ({ ...f, [e.target.name]: e.target.value }))

  const handleSubmit = (e) => {
    e.preventDefault()
    setStatus('sending')
    const subject = encodeURIComponent(
      `Hello from ${form.name || 'your portfolio'}`
    )
    const body = encodeURIComponent(
      `${form.message}\n\n— ${form.name}${form.email ? ` (${form.email})` : ''}`
    )
    window.location.href = `mailto:${profile.email}?subject=${subject}&body=${body}`
    setTimeout(() => setStatus('sent'), 400)
  }

  return (
    <section
      id="contact"
      ref={ref}
      className="section relative"
      aria-labelledby="contact-heading"
    >
      <div className="container-max grid lg:grid-cols-2 gap-12 lg:gap-16 items-start">
        <div>
          <span data-reveal className="eyebrow">
            <span>04 · Contact</span>
          </span>
          <h2
            id="contact-heading"
            data-reveal
            className="mt-6 font-display text-4xl md:text-5xl font-semibold leading-tight text-white"
          >
            Have something interesting to{' '}
            <span className="text-gradient">build?</span>
          </h2>
          <p
            data-reveal
            className="mt-5 max-w-lg text-slate-400 leading-relaxed"
          >
            I&apos;m open to opportunities in digitalization, automation, IoT
            platforms, and frontend engineering. Drop a note and I&apos;ll get
            back within a couple of days.
          </p>

          <ul className="mt-10 grid gap-3 max-w-md">
            <li data-reveal>
              <a
                href={`mailto:${profile.email}`}
                className="card p-5 flex items-center gap-4 group"
              >
                <span className="grid place-items-center w-11 h-11 rounded-xl bg-accent/15 text-accent">
                  <HiEnvelope aria-hidden="true" />
                </span>
                <span className="flex-1">
                  <div className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    Email
                  </div>
                  <div className="text-slate-100">{profile.email}</div>
                </span>
                <HiArrowRight
                  aria-hidden="true"
                  className="text-slate-500 group-hover:text-white group-hover:translate-x-1 transition"
                />
              </a>
            </li>
            <li data-reveal>
              <a
                href={profile.socials.linkedin}
                target="_blank"
                rel="noreferrer"
                className="card p-5 flex items-center gap-4 group"
              >
                <span className="grid place-items-center w-11 h-11 rounded-xl bg-cyan-neon/15 text-cyan-neon">
                  <FaLinkedin aria-hidden="true" />
                </span>
                <span className="flex-1">
                  <div className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    LinkedIn
                  </div>
                  <div className="text-slate-100">Connect professionally</div>
                </span>
                <HiArrowRight
                  aria-hidden="true"
                  className="text-slate-500 group-hover:text-white group-hover:translate-x-1 transition"
                />
              </a>
            </li>
            <li data-reveal>
              <a
                href={profile.socials.github}
                target="_blank"
                rel="noreferrer"
                className="card p-5 flex items-center gap-4 group"
              >
                <span className="grid place-items-center w-11 h-11 rounded-xl bg-white/10 text-white">
                  <FaGithub aria-hidden="true" />
                </span>
                <span className="flex-1">
                  <div className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    GitHub
                  </div>
                  <div className="text-slate-100">See the code</div>
                </span>
                <HiArrowRight
                  aria-hidden="true"
                  className="text-slate-500 group-hover:text-white group-hover:translate-x-1 transition"
                />
              </a>
            </li>
          </ul>
        </div>

        <form
          data-reveal
          onSubmit={handleSubmit}
          className="card p-6 sm:p-8 relative"
          aria-label="Contact form"
        >
          <div className="grid gap-5">
            <label className="grid gap-2">
              <span className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                Name
              </span>
              <input
                type="text"
                name="name"
                required
                value={form.name}
                onChange={handleChange}
                autoComplete="name"
                className="w-full bg-ink-900/60 border border-white/10 rounded-lg px-4 py-3 text-slate-100 placeholder:text-slate-600 focus:border-accent focus:ring-0 outline-none transition"
                placeholder="Your name"
              />
            </label>

            <label className="grid gap-2">
              <span className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                Email
              </span>
              <input
                type="email"
                name="email"
                required
                value={form.email}
                onChange={handleChange}
                autoComplete="email"
                className="w-full bg-ink-900/60 border border-white/10 rounded-lg px-4 py-3 text-slate-100 placeholder:text-slate-600 focus:border-accent outline-none transition"
                placeholder="you@company.com"
              />
            </label>

            <label className="grid gap-2">
              <span className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                Message
              </span>
              <textarea
                name="message"
                required
                value={form.message}
                onChange={handleChange}
                rows={5}
                className="w-full bg-ink-900/60 border border-white/10 rounded-lg px-4 py-3 text-slate-100 placeholder:text-slate-600 focus:border-accent outline-none transition resize-y"
                placeholder="What are you working on?"
              />
            </label>

            <button
              type="submit"
              disabled={status === 'sending'}
              className="btn btn-primary w-full sm:w-auto justify-self-start disabled:opacity-60"
            >
              {status === 'sending' ? 'Opening mail…' : 'Send message'}
              <HiArrowRight aria-hidden="true" />
            </button>

            {status === 'sent' && (
              <p
                role="status"
                className="text-sm text-emerald-300"
              >
                Your mail client should be open. If not, email me directly at{' '}
                <a
                  href={`mailto:${profile.email}`}
                  className="underline"
                >
                  {profile.email}
                </a>
                .
              </p>
            )}
          </div>
        </form>
      </div>
    </section>
  )
}
