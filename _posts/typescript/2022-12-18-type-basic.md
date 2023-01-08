---
layout: single

header:
  teaser: /assets/images/logo/typescript.png
  overlay_image: /assets/images/logo/typescript.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[TS] 타입스크립트 기초에 대해 알아보자"
excerpt: "🚀 type, string, number, object, array, tuple, etc..."

categories: typescript
tag: [typescript, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Typescript
> https://joshua1988.github.io/ts/intro.html



## 01. Generics

> 함수에 여러가지 형태의 타입이 올수 있다.



- 기존 쓰이는 방식

```ts
function logText(text) {
  console.log(text);
  return text
}

logText('hello world!')  // 'hello world!'
```



- Generic 을 이용한 방식
  - `text` 파라미터에 여러가지 타입의 데이터를 넣을 수 있다.

```ts
function logText<T>(text: T): T {
  console.log(text);
  return text;
}

logText<string>('hello world!') // 'hello world!'
```



- Union Type
  - 리턴값이 string, number 둘중 하나가 되므로 빌트인API 추천이 이상하게 나옴

```ts
function logText(text: string | number) {
  console.log(text);
  return text
}

logText('hello world!')
logText(10)
```

































