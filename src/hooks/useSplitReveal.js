import { useRef } from 'react'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

gsap.registerPlugin(ScrollTrigger)

export function useSplitReveal({ delay = 0, trigger = 'mount', stagger = 0.06 } = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    if (!ref.current) return
    const el = ref.current
    const reduced = prefersReducedMotion()

    const original = el.getAttribute('data-text') || el.textContent
    el.setAttribute('data-text', original)
    el.setAttribute('aria-label', original)

    const words = original.split(/(\s+)/)
    el.innerHTML = words
      .map((w) => {
        if (/^\s+$/.test(w)) return w
        return `<span class="inline-block overflow-hidden align-baseline"><span class="inline-block will-change-transform">${w}</span></span>`
      })
      .join('')

    const spans = el.querySelectorAll('span > span')

    const ctx = gsap.context(() => {
      gsap.set(spans, { yPercent: reduced ? 0 : 120 })

      const tween = {
        yPercent: 0,
        duration: reduced ? 0 : 1,
        ease: 'power4.out',
        stagger: reduced ? 0 : stagger,
        delay,
      }

      if (trigger === 'scroll') {
        gsap.to(spans, {
          ...tween,
          scrollTrigger: {
            trigger: el,
            start: 'top 85%',
            toggleActions: 'play none none none',
          },
        })
      } else {
        gsap.to(spans, tween)
      }
    }, ref)

    return () => {
      ctx.revert()
      el.textContent = original
    }
  }, [delay, trigger, stagger])

  return ref
}
