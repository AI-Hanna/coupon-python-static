import { useEffect, useState } from 'react'

const BASE_PATH = '/assets'
const SCREENS = [
  {
    id: 'screen_01_default',
    image: `${BASE_PATH}/screen_01_default.jpg`,
    alt: '기본 화면',
  },
  {
    id: 'screen_02_button_click',
    image: `${BASE_PATH}/screen_02_button_click.jpg`,
    alt: '버튼 클릭 반응',
  },
  {
    id: 'screen_03_box_open',
    image: `${BASE_PATH}/screen_03_box_open.jpg`,
    alt: '상자 열림',
  },
  {
    id: 'screen_04_coupon_appear',
    image: `${BASE_PATH}/screen_04_coupon_appear.jpg`,
    alt: '쿠폰 등장',
  },
  {
    id: 'screen_05_message_show',
    image: `${BASE_PATH}/screen_05_message_show.jpg`,
    alt: '메시지 노출',
  },
  {
    id: 'screen_06_cta_show',
    image: `${BASE_PATH}/screen_06_cta_show.jpg`,
    alt: 'CTA 노출',
  },
]

const phaseToIndex = {
  idle: 0,
  pressing: 1,
  opening: 2,
  coupon: 3,
  message: 4,
  done: 5,
  complete: 5,
}

function App() {
  const [phase, setPhase] = useState('idle')
  const [isPressing, setIsPressing] = useState(false)
  const [showSparkle, setShowSparkle] = useState(false)
  const [showConfirm, setShowConfirm] = useState(false)

  useEffect(() => {
    if (phase === 'idle') {
      const timer = window.setTimeout(() => setShowSparkle(true), 900)
      return () => window.clearTimeout(timer)
    }

    if (phase === 'pressing') {
      const timer = window.setTimeout(() => {
        setPhase('opening')
      }, 320)
      return () => window.clearTimeout(timer)
    }

    if (phase === 'opening') {
      setShowSparkle(true)
      const timer = window.setTimeout(() => {
        setPhase('coupon')
      }, 900)
      return () => window.clearTimeout(timer)
    }

    if (phase === 'coupon') {
      const timer = window.setTimeout(() => {
        setPhase('message')
      }, 980)
      return () => window.clearTimeout(timer)
    }

    if (phase === 'message') {
      const timer = window.setTimeout(() => {
        setShowConfirm(true)
        setPhase('done')
      }, 520)
      return () => window.clearTimeout(timer)
    }
  }, [phase])

  const handleOpen = () => {
    if (phase !== 'idle') return
    setIsPressing(true)
    setShowSparkle(false)
    setShowConfirm(false)
    setPhase('pressing')

    window.setTimeout(() => {
      setIsPressing(false)
    }, 240)
  }

  const handleConfirm = () => {
    if (phase !== 'done') return
    setShowConfirm(false)
    setPhase('complete')
  }

  return (
    <main className="stage">
      <div className="scene">
        {SCREENS.map((screen, index) => (
          <img
            key={screen.id}
            className={`screen ${index === phaseToIndex[phase] ? 'active' : ''}`}
            src={screen.image}
            alt={screen.alt}
          />
        ))}

        <div className={`glow-layer ${showSparkle ? 'show' : ''}`} />
        <div className={`sparkle sparkle-1 ${showSparkle ? 'show' : ''}`} />
        <div className={`sparkle sparkle-2 ${showSparkle ? 'show' : ''}`} />
        <div className={`sparkle sparkle-3 ${showSparkle ? 'show' : ''}`} />

        <section className={`headline-wrap ${phase === 'message' || phase === 'done' || phase === 'complete' ? 'show' : ''}`}>
          <h1>새 집 필수템 구매 찬스!</h1>
          <p>갖고 싶었던 그거, 사러 가자</p>
        </section>

        <div className={`success-overlay ${phase === 'complete' ? 'show' : ''}`}>
          쿠폰 확인 완료
        </div>

        <button
          type="button"
          className={`open-button ${isPressing ? 'press' : ''} ${phase !== 'idle' ? 'hide' : ''}`}
          aria-label="선물상자 열기"
          onClick={handleOpen}
        />

        <button
          type="button"
          className={`confirm-button ${showConfirm ? 'show' : ''}`}
          aria-label="확인"
          onClick={handleConfirm}
        />
      </div>
    </main>
  )
}

export default App
