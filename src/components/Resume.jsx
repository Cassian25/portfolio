import { useState } from 'react'
import { HiArrowDownTray, HiEye, HiXMark } from 'react-icons/hi2'
import { useScrollReveal } from '../hooks/useScrollReveal'
import { profile } from '../data/profile'

export default function Resume() {
  const ref = useScrollReveal({ selector: '[data-reveal]', stagger: 0.1 })
  const [previewOpen, setPreviewOpen] = useState(false)

  const resumeHref = `${import.meta.env.BASE_URL}${profile.resumeFile}`

  return (
    <section
      id="resume"
      ref={ref}
      className="section relative"
      aria-labelledby="resume-heading"
    >
      <div className="container-max">
        <div className="card p-8 md:p-14 relative overflow-hidden">
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -top-32 -right-24 w-[420px] h-[420px] rounded-full bg-accent/20 blur-3xl"
          />
          <div
            aria-hidden="true"
            className="pointer-events-none absolute -bottom-32 -left-24 w-[380px] h-[380px] rounded-full bg-cyan-neon/15 blur-3xl"
          />

          <div className="relative grid lg:grid-cols-[minmax(0,1fr)_auto] gap-10 items-center">
            <div>
              <span data-reveal className="eyebrow">
                <span>03 · Resume</span>
              </span>
              <h2
                id="resume-heading"
                data-reveal
                className="mt-6 font-display text-4xl md:text-5xl font-semibold leading-tight text-white"
              >
                The <span className="text-gradient">short version</span>, in a
                PDF.
              </h2>
              <p
                data-reveal
                className="mt-5 max-w-xl text-slate-300 leading-relaxed"
              >
                Download the latest resume or preview it inline. Includes work
                history, education, and the tech I&apos;ve shipped with in
                production.
              </p>

              <div data-reveal className="mt-8 flex flex-wrap gap-3">
                <a
                  href={resumeHref}
                  download
                  className="btn btn-primary"
                  aria-label="Download resume as PDF"
                >
                  <HiArrowDownTray aria-hidden="true" />
                  Download Resume
                </a>
                <button
                  type="button"
                  onClick={() => setPreviewOpen(true)}
                  className="btn btn-ghost"
                  aria-haspopup="dialog"
                  aria-expanded={previewOpen}
                >
                  <HiEye aria-hidden="true" />
                  Preview inline
                </button>
              </div>

              <dl
                data-reveal
                className="mt-10 grid sm:grid-cols-2 gap-x-8 gap-y-4 text-sm"
              >
                <div className="border-l border-white/10 pl-4">
                  <dt className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    Currently
                  </dt>
                  <dd className="mt-1 text-slate-200">
                    {profile.currentCompany}
                  </dd>
                </div>
                <div className="border-l border-white/10 pl-4">
                  <dt className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    Previously
                  </dt>
                  <dd className="mt-1 text-slate-200">
                    {profile.previousCompany}
                  </dd>
                </div>
                <div className="border-l border-white/10 pl-4">
                  <dt className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    Education
                  </dt>
                  <dd className="mt-1 text-slate-200">
                    {profile.education.degree}
                  </dd>
                </div>
                <div className="border-l border-white/10 pl-4">
                  <dt className="text-xs uppercase tracking-widest text-slate-500 font-mono">
                    Location
                  </dt>
                  <dd className="mt-1 text-slate-200">{profile.location}</dd>
                </div>
              </dl>
            </div>

            <div
              data-reveal
              className="hidden lg:flex flex-col items-center gap-3 p-6 rounded-2xl border border-white/10 bg-white/[0.02] w-56"
              aria-hidden="true"
            >
              <div className="aspect-[3/4] w-full rounded-lg bg-gradient-to-br from-ink-700 to-ink-900 relative overflow-hidden">
                <div className="absolute inset-4 border border-white/10 rounded" />
                <div className="absolute top-8 left-6 right-6 h-3 rounded bg-white/10" />
                <div className="absolute top-14 left-6 w-24 h-2 rounded bg-white/10" />
                <div className="absolute top-24 left-6 right-6 space-y-2">
                  <div className="h-1.5 rounded bg-white/10" />
                  <div className="h-1.5 rounded bg-white/10 w-5/6" />
                  <div className="h-1.5 rounded bg-white/10 w-2/3" />
                  <div className="h-1.5 rounded bg-white/10 w-3/4" />
                </div>
              </div>
              <div className="text-xs text-slate-500 font-mono">resume.pdf</div>
            </div>
          </div>
        </div>
      </div>

      {previewOpen && (
        <div
          role="dialog"
          aria-modal="true"
          aria-label="Resume preview"
          className="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-8 bg-ink-950/85 backdrop-blur-md animate-[fadein_0.25s_ease-out]"
          onClick={(e) => {
            if (e.target === e.currentTarget) setPreviewOpen(false)
          }}
        >
          <div className="relative w-full max-w-5xl h-[85vh] bg-ink-900 rounded-2xl border border-white/10 overflow-hidden shadow-card">
            <div className="flex items-center justify-between px-4 py-3 border-b border-white/10 bg-ink-800">
              <div className="text-sm text-slate-300 font-mono">
                resume.pdf — preview
              </div>
              <div className="flex items-center gap-2">
                <a
                  href={resumeHref}
                  download
                  className="btn btn-ghost text-xs px-3 py-1.5"
                >
                  <HiArrowDownTray aria-hidden="true" />
                  Download
                </a>
                <button
                  type="button"
                  onClick={() => setPreviewOpen(false)}
                  aria-label="Close preview"
                  className="p-2 rounded-md border border-white/10 bg-white/5 hover:bg-white/10 transition"
                >
                  <HiXMark aria-hidden="true" />
                </button>
              </div>
            </div>
            <object
              data={resumeHref}
              type="application/pdf"
              className="w-full h-[calc(100%-49px)]"
              aria-label="Embedded resume PDF"
            >
              <div className="p-10 text-center text-slate-400">
                Your browser can&apos;t display PDFs inline.{' '}
                <a
                  href={resumeHref}
                  className="text-accent underline"
                  download
                >
                  Download the resume instead
                </a>
                .
              </div>
            </object>
          </div>
        </div>
      )}
    </section>
  )
}
