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

title: "[python] generator comprehension 이용한 코드 속도, 메모리 개선"
excerpt: "🚀 python, generator, comprehension"

categories: python
tag: [python, memory, comprehension, performance, speed]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Python Performance Check

> List Comp 와 Generator Comp 차이 속도차이 비교<br>
> [참고 블로그](https://wikidocs.net/16069)


- 제너레이터 컴프리헨션 표현식

```python
generator_items = (
  expression
  for i in range(100)
)
```



```python
from timeit import timeit
import random
from faker import Faker
import time
from memory_profiler import profile


"""
List Comprehension 과 Generator Comprehension 속도차이 비교를 위해 코드 작성
"""
fake = Faker('ko_KR')

@profile
def test():
    """"List Comprehension"""
    items = [
        {
            'id': i,
            'name': fake.name(),
            'address': fake.address(),
            'age': random.randint(1, 100)
        }
        for i in range(10_000)
    ]
    return items

@profile
def test2():
    """Generator Comprehension"""
    items = (
        {
            'id': i,
            'name': fake.name(),
            'address': fake.address(),
            'age': random.randint(1, 100)
        }
        for i in range(10_000)
    )
    return items

print(timeit(test, number=10))
print(timeit(test2, number=10))


# result = test()
result2 = test2()

for item in result2:
  print(item)
```