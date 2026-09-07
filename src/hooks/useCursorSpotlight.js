import { useRef } from 'react'
import gsap from 'gsap'
import { useIsomorphicLayoutEffect, prefersReducedMotion } from './useGsap'

export function useCursorSpotlight({ targetSelector = '[data-spotlight]' } = {}) {
  const ref = useRef(null)

  useIsomorphicLayoutEffect(() => {
    const root = ref.current
    if (!root) return
    if (prefersReducedMotion()) return

    const target = root.querySelector(targetSelector)
    if (!target) return

    const xTo = gsap.quickTo(target, '--spot-x', { duration: 0.6, ease: 'power2.out' })
    const yTo = gsap.quickTo(target, '--spot-y', { duration: 0.6, ease: 'power2.out' })
    const oTo = gsap.quickTo(target, '--spot-o', { duration: 0.4, ease: 'power2.out' })

    const onMove = (e) => {
      const rect = root.getBoundingClientRect()
      xTo(((e.clientX - rect.left) / rect.width) * 100)
      yTo(((e.clientY - rect.top) / rect.height) * 100)
      oTo(1)
    }

    const onLeave = () => oTo(0)

    root.addEventListener('mousemove', onMove)
    root.addEventListener('mouseleave', onLeave)
    return () => {
      root.removeEventListener('mousemove', onMove)
      root.removeEventListener('mouseleave', onLeave)
    }
  }, [targetSelector])

  return ref
}
