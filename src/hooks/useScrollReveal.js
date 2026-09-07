import { useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

gsap.registerPlugin(ScrollTrigger)

export function useScrollReveal({
  selector = '.reveal',
  y = 40,
  duration = 0.9,
  stagger = 0.12,
  start = 'top 85%',
  once = true,
} = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    if (!ref.current) return
    const reduced = prefersReducedMotion()

    const ctx = gsap.context(() => {
      const targets = gsap.utils.toArray(selector)
      if (!targets.length) return

      gsap.set(targets, { opacity: 0, y: reduced ? 0 : y })

      gsap.to(targets, {
        opacity: 1,
        y: 0,
        duration: reduced ? 0 : duration,
        ease: 'power3.out',
        stagger: reduced ? 0 : stagger,
        scrollTrigger: {
          trigger: ref.current,
          start,
          toggleActions: once ? 'play none none none' : 'play none none reverse',
        },
      })
    }, ref)

    return () => ctx.revert()
  }, [selector, y, duration, stagger, start, once])

  return ref
}
