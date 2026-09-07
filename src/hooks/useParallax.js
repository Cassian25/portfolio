import { useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

gsap.registerPlugin(ScrollTrigger)

export function useParallax({ distance = -80, start = 'top bottom', end = 'bottom top' } = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    if (!ref.current) return
    if (prefersReducedMotion()) return

    const ctx = gsap.context(() => {
      gsap.fromTo(
        ref.current,
        { y: 0 },
        {
          y: distance,
          ease: 'none',
          scrollTrigger: {
            trigger: ref.current,
            start,
            end,
            scrub: true,
          },
        }
      )
    })

    return () => ctx.revert()
  }, [distance, start, end])

  return ref
}
