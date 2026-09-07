import { useRef } from 'react'
import gsap from 'gsap'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

export function useTilt({ max = 8, scale = 1.01, glareSelector } = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    const el = ref.current
    if (!el) return
    if (prefersReducedMotion()) return

    gsap.set(el, { transformPerspective: 900, transformStyle: 'preserve-3d' })

    const rxTo = gsap.quickTo(el, 'rotateX', { duration: 0.5, ease: 'power3.out' })
    const ryTo = gsap.quickTo(el, 'rotateY', { duration: 0.5, ease: 'power3.out' })
    const sTo = gsap.quickTo(el, 'scale', { duration: 0.5, ease: 'power3.out' })

    const glare = glareSelector ? el.querySelector(glareSelector) : null

    const onMove = (e) => {
      const rect = el.getBoundingClientRect()
      const px = (e.clientX - rect.left) / rect.width
      const py = (e.clientY - rect.top) / rect.height
      const rx = (0.5 - py) * (max * 2)
      const ry = (px - 0.5) * (max * 2)
      rxTo(rx)
      ryTo(ry)
      sTo(scale)
      if (glare) {
        glare.style.setProperty('--gx', `${px * 100}%`)
        glare.style.setProperty('--gy', `${py * 100}%`)
      }
    }

    const onLeave = () => {
      rxTo(0)
      ryTo(0)
      sTo(1)
    }

    el.addEventListener('mousemove', onMove)
    el.addEventListener('mouseleave', onLeave)
    return () => {
      el.removeEventListener('mousemove', onMove)
      el.removeEventListener('mouseleave', onLeave)
    }
  }, [max, scale, glareSelector])

  return ref
}
