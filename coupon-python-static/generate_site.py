from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"
DIST_ASSETS = DIST / "assets"

SCREENS = [
    ("screen_01_default.jpg", "기본 화면"),
    ("screen_02_button_click.jpg", "버튼 클릭 반응"),
    ("screen_03_box_open.jpg", "상자 열림"),
    ("screen_04_coupon_appear.jpg", "쿠폰 등장"),
    ("screen_05_message_show.jpg", "메시지 노출"),
    ("screen_06_cta_show.jpg", "CTA 노출"),
]

HTML = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>깜짝 선물 쿠폰 (made 하진 & 현지)</title>
  <style>
    * { box-sizing: border-box; }
    html, body { margin: 0; width: 100%; min-height: 100%; background: #eef0f5; font-family: -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif; }
    body { display: flex; justify-content: center; }
    .stage { position: relative; width: min(100vw, 402px); height: min(100dvh, 874px); min-height: 720px; overflow: hidden; background: #eef0f5; }
    .screen { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0; transform: scale(1); transition: opacity 280ms ease, transform 280ms ease; pointer-events: none; }
    .screen.active { opacity: 1; pointer-events: auto; }
    .screen.pop { transform: scale(1.03); }
    .screen.float { animation: softFloat 2s ease-in-out infinite; }
    .open-button { position: absolute; left: 20px; right: 20px; bottom: max(36px, env(safe-area-inset-bottom)); height: 60px; border: 0; border-radius: 12px; background: transparent; cursor: pointer; z-index: 10; }
    .confirm-button { display: none; position: absolute; left: 20px; right: 20px; bottom: max(36px, env(safe-area-inset-bottom)); height: 60px; border: 0; border-radius: 12px; background: transparent; cursor: pointer; z-index: 10; }
    .confirm-button.show { display: block; }
    @keyframes softFloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
    @media (min-width: 403px) { .stage { box-shadow: 0 0 30px rgba(0,0,0,.08); } }
  </style>
</head>
<body>
  <main class="stage" aria-label="집들이 축하용 이거사줘 쿠폰 선물 오픈 인터랙션">
    __IMAGES__
    <button class="open-button" aria-label="선물상자 열기"></button>
    <button class="confirm-button" aria-label="확인"></button>
  </main>
  <script>
    const screens = Array.from(document.querySelectorAll('.screen'));
    const openButton = document.querySelector('.open-button');
    const confirmButton = document.querySelector('.confirm-button');
    let timers = [];

    function clearTimers() { timers.forEach(clearTimeout); timers = []; }
    function show(index, className = '') {
      screens.forEach((screen, i) => {
        screen.className = 'screen' + (i === index ? ' active ' + className : '');
      });
    }
    function start() {
      clearTimers();
      confirmButton.classList.remove('show');
      openButton.style.display = 'block';
      show(0, 'float');
    }
    function play() {
      clearTimers();
      openButton.style.display = 'none';
      show(1, 'pop');
      timers.push(setTimeout(() => show(2), 360));
      timers.push(setTimeout(() => show(3), 1050));
      timers.push(setTimeout(() => show(4), 1900));
      timers.push(setTimeout(() => {
        show(5);
        confirmButton.classList.add('show');
      }, 2500));
    }
    openButton.addEventListener('click', play);
    confirmButton.addEventListener('click', () => alert('쿠폰 확인 완료!'));
    start();
  </script>
</body>
</html>
"""

def build() -> None:
    DIST.mkdir(exist_ok=True)
    DIST_ASSETS.mkdir(exist_ok=True)
    for filename, _ in SCREENS:
        shutil.copy2(ASSETS / filename, DIST_ASSETS / filename)
    image_tags = "\n    ".join(
        f'<img class="screen" src="assets/{filename}" alt="{alt}" />'
        for filename, alt in SCREENS
    )
    (DIST / "index.html").write_text(HTML.replace("__IMAGES__", image_tags), encoding="utf-8")
    print(f"Generated: {DIST / 'index.html'}")

if __name__ == "__main__":
    build()
