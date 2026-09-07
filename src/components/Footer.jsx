import { FaGithub, FaLinkedin } from 'react-icons/fa6'
import { HiEnvelope } from 'react-icons/hi2'
import { profile } from '../data/profile'

export default function Footer() {
  const year = new Date().getFullYear()

  return (
    <footer className="relative border-t border-white/5 mt-10">
      <div className="container-max px-4 md:px-8 py-8 sm:py-10 flex flex-col sm:flex-row items-center justify-between gap-6">
        <div className="text-sm text-slate-500 text-center sm:text-left">
          <span className="font-display text-slate-300">
            {profile.name}
          </span>
          <span className="mx-2 hidden sm:inline">·</span>
          <span className="block sm:inline mt-1 sm:mt-0">{profile.role}</span>
          <div className="text-xs mt-1 font-mono text-slate-600">
            © {year} · Built with React, Vite &amp; GSAP
          </div>
        </div>

        <ul className="flex items-center gap-2">
          <li>
            <a
              href={`mailto:${profile.email}`}
              aria-label="Email"
              className="p-2.5 rounded-lg border border-white/10 bg-white/[0.03] text-slate-300 hover:text-white hover:border-accent/40 transition"
            >
              <HiEnvelope aria-hidden="true" />
            </a>
          </li>
          <li>
            <a
              href={profile.socials.github}
              target="_blank"
              rel="noreferrer"
              aria-label="GitHub"
              className="p-2.5 rounded-lg border border-white/10 bg-white/[0.03] text-slate-300 hover:text-white hover:border-accent/40 transition"
            >
              <FaGithub aria-hidden="true" />
            </a>
          </li>
          <li>
            <a
              href={profile.socials.linkedin}
              target="_blank"
              rel="noreferrer"
              aria-label="LinkedIn"
              className="p-2.5 rounded-lg border border-white/10 bg-white/[0.03] text-slate-300 hover:text-white hover:border-accent/40 transition"
            >
              <FaLinkedin aria-hidden="true" />
            </a>
          </li>
        </ul>
      </div>
    </footer>
  )
}
