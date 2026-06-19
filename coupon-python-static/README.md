# Coupon Event React Interaction

이 프로젝트는 Python 정적 생성 방식 대신 React + Vite로 바꿔서,
선물상자 오픈 → 쿠폰 등장 → 메시지/CTA 노출 흐름을 더 부드럽게 표현하도록 구성했습니다.

## 화면 구성

- 기본 화면: 닫힌 선물상자
- 버튼 클릭 반응: 살짝 눌림 효과
- 상자 열림: 다음 화면으로 전환
- 쿠폰 등장: 감성형 fade + bounce 느낌
- 헤드라인/CTA: 순차 노출

## 로컬 실행

```bash
npm install
npm run dev
```

브라우저에서 `http://localhost:5173` 으로 접속합니다.

## 빌드

```bash
npm run build
```

## 참고

- 이미지 에셋은 `assets/` 폴더의 화면 연출용 파일을 사용합니다.
- 애니메이션은 React 상태 전환과 CSS로 제어합니다.

