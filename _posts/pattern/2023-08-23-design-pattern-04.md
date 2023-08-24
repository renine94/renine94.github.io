---
layout: single

header:
  teaser: /assets/images/logo/pattern.jpeg
  overlay_image: /assets/images/logo/pattern.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[pattern] 디자인패턴(4) - 감마 분류"
excerpt: "🚀 디자인패턴, 생성, 구조, 행동 패턴을 분류하는 기준"

categories: pattern
tag: [pattern, design, gamma]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. Gamma Categorization

- 디자인 패턴은 3가지 범주로 보통 나뉜다.
- 이 것을 `감마분류` 라고 부르는 편이다.

1. 생성패턴
   - 객체 생성(Construction) 처리
   - 명시적(construction, `__init__`) vs 암시적(DI, reflection, etc...)
   - 대량 (단일 상태) vs 구분적으로 (단계별로)
2. 구조패턴
   - 구조 관련 (ex. 클래스 멤버)
   - 대부분 패턴은 기본 클래스의 인터페이스를 모방한 래퍼이다.
   - 좋은 API 설계의 중요성을 강조한다.
3. 생성패턴
   - 전부 다 다르다.
   - 중심 주제가 없다.







