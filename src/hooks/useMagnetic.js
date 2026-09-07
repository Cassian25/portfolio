import { useRef } from 'react'
import gsap from 'gsap'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

export function useMagnetic({ strength = 0.35, radius = 120 } = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    const el = ref.current
    if (!el) return
    if (prefersReducedMotion()) return

    const xTo = gsap.quickTo(el, 'x', { duration: 0.4, ease: 'power3.out' })
    const yTo = gsap.quickTo(el, 'y', { duration: 0.4, ease: 'power3.out' })

    const onMove = (e) => {
      const rect = el.getBoundingClientRect()
      const cx = rect.left + rect.width / 2
      const cy = rect.top + rect.height / 2
      const dx = e.clientX - cx
      const dy = e.clientY - cy
      const dist = Math.hypot(dx, dy)
      if (dist > radius) {
        xTo(0)
        yTo(0)
        return
      }
      xTo(dx * strength)
      yTo(dy * strength)
    }

    const onLeave = () => {
      xTo(0)
      yTo(0)
    }

    window.addEventListener('mousemove', onMove)
    el.addEventListener('mouseleave', onLeave)
    return () => {
      window.removeEventListener('mousemove', onMove)
      el.removeEventListener('mouseleave', onLeave)
    }
  }, [strength, radius])

  return ref
}
