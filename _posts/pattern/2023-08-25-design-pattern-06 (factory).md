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

title: "[pattern] 디자인패턴(6) - 팩토리(Factory) 패턴"
excerpt: "🚀 디자인패턴 Factory"

categories: pattern
tag: [pattern, design, factories]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. Factory Pattern
> Factory Method and Abstract Factory

**Motivation**
- Object creation logic becomes too convoluted
- Initializer is not descriptive
  - name is alway __init__
  - Cannot overload with same sets of arguments with different names
  - Can turn into 'optional parameter hell'
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to
  - A separate method (Factory Method)
  - That may exist in a separate class (Factory)
  - Can create hierarchy of factories with Abstract Factory

Factory: `A Component responsible solely for the wholesale (not piecewise) creation of objects`


**동기 부여**
- 객체 생성 로직이 너무 복잡해짐
- 이니셜라이저가 설명적이지 않음
  - 이름은 항상 __init__입니다.
  - 이름이 다른 동일한 인자 집합으로 오버로드할 수 없음
  - '선택적 매개변수 지옥'으로 변할 수 있음
- 도매 객체 생성 (빌더와 달리 조각 단위가 아님)은 다음으로 아웃소싱할 수 있습니다.
  - 별도의 메서드(팩토리 메서드)
  - 별도의 클래스(Factory)에 존재할 수 있습니다.
  - 추상 팩토리로 팩토리의 계층 구조 생성 가cl능

Factory: '객체의 도매 (조각 단위가 아닌) 생성만을 담당하는 컴포넌트'

