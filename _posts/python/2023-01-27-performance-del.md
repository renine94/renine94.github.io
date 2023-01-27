---
layout: single

header:
  teaser: /assets/images/logo/python.jpeg
  overlay_image: /assets/images/logo/python.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[python] del을 이용하여 코드를 최적화 하는 방법에 대해 알아보자. (with. gc)"
excerpt: "🚀 python, del, memory, gc"

categories: python
tag: [python, memory, performance, gc]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Python Performance Check

> python 가비지 컬렉터 동작과 메모리 사용 방식<br>
> [참조 블로그](https://devguide.python.org/internals/garbage-collector/)

- 가비지 컬렉터나 메모리 측면 관련
  - 대충 비유 하면 집 문 두드려서 계십니까? 안계시나요? 또 올게요 똑똑 계십니까 이거 반복하다가 없네?<br>이집은 이제 제꺼입니다. 같은 방식입니다.
  - 위 참조블로그 문서에 따르면 참조횟수에 따라 메모리 할당을 해제하는것으로 파악됨

`del` 사용 추천 드리는 이유는 아래 샘플 코드와 결과를 보시면 됩니다.

- del 사용
  - 같은 메모리주소
- del 미사용
  - 메모리주소 번갈아가면서 할당됨
- **결론**
  - **del 사용시 메모리 측면에서 2배 퍼포먼스 향상 기대**

```python
res = []

for i in range(10):
    a = {"name": i}
    res.append(id(a))
    #del a


for r in res:
    print(r)

"""
2780826061696
2780826061952
2780826061696
2780826061952
2780826061696
2780826061952
2780826061696
2780826061952
2780826061696
2780826061952

del 주석 해제 후
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
2139291470720
"""
```
