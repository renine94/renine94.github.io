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

title: "[python] slots을 이용하여 코드를 최적화 하는 방법에 대해 알아보자"
excerpt: "🚀 python, slots, profiler, speed, memory"

categories: python
tag: [python, profiler, memory, performance, speed]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Python Performance Check

> 사내에서 동료개발자분께서 파이썬 퍼포먼스 측정 관련 내용을 알려주어 메모를 남기고자 포스팅합니다.



## 0.  개요

Python에서는 Object attribute에 대해서 메모리는 더 적게 사용, 접근 속도는 더 빠르게 하는 방법이 있습니다. 
바로, `__slots__` 를 사용하는 방법 입니다.

기본적으로 Python은 객체 인스턴스 속성을 Dict를 사용 생성하며 Dict 형은 메모리를 추가적으로 필요로 합니다. `slots` 을 사용 하는 경우  `class`는 `__dict__`, `__weakref__` 생성을 하지 않습니다.  

```
It restricts the valid set of attribute names on an object to exactly those names listed.
Since the attributes are now fixed, it is no longer necessary to store attributes in an instance dictionary.
Attributes can be stored in predetermined locations within an array.
```



## 1.  기대 효과

- 보다 **적은 메모리 사용**
- `Attribute`에 보다 **빠른 접근 속도**
- Data Attribute **제어에 있어서 비교적 안전적**



## 2.  Sample Code

### init_test.py

`10만 row` * `10만 col` 을 가진 `총 100만개의 cell`을 가진 csv 파일을 랜덤 생성합니다.

```python
import random

from faker import Faker
from pandas import DataFrame, Series

faker = Faker()
Faker.seed(0)

def create_df(create_size=10):
    dataset = {
        'name': [faker.name() for _ in range(create_size)],
        'first_name': [faker.first_name() for _ in range(create_size)],
        'last_name': [faker.last_name() for _ in range(create_size)],
        'country': [faker.country() for _ in range(create_size)],
        'postcode': [faker.postcode() for _ in range(create_size)],
        'city': [faker.city() for _ in range(create_size)],
        'age': [random.randint(1, 100) for _ in range(create_size)],
        'company': [faker.company() for _ in range(create_size)],
        'job': [faker.job() for _ in range(create_size)],
        'credit_card': [faker.credit_card_number() for _ in range(create_size)],
    }

    df = DataFrame()
    for key, data in dataset.items():
        df[key] = Series(data)

    return df

df = create_df(100000)
df.to_csv("huge_file.csv", header=False, index=False)
```



### file_read_normally.py

일반적인 방법으로 VO 생성합니다.

```python
from typing import List

import pandas
from memory_profiler import profile
from line_profiler_decorator import profiler as line_profile

class Person:

    def __init__(self, name, first_name, last_name, country, postcode, city, age, company, job, credit_card):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.postcode = postcode
        self.city = city
        self.age = age
        self.company = company
        self.job = job
        self.credit_card = credit_card

def read_csv(file_name="huge_file.csv"):
    df = pandas.read_csv(file_name)

    persons = [
        Person(
            row[1][0], row[1][1], row[1][2], row[1][3], row[1][4],
            row[1][5], row[1][6], row[1][7], row[1][8], row[1][9],
        )
        for row in df.iterrows()
    ]
    return persons

def manipulate_persons(persons: List[Person]):
    for p in persons:
        p.name = f"{p.first_name}-{p.last_name}"
        p.job = f"{p.company} - {p.job}"

@line_profile
def client():
    persons = read_csv()
    manipulate_persons(persons)

client()
```



### file_read_with_slot.py

slots를 사용하여 VO를 생성합니다.

```python
from typing import List

import pandas
from memory_profiler import profile
from line_profiler_decorator import profiler as line_profile

class Person:
    __slots__ = [
        'name', 'first_name', 'last_name', 'country', 'postcode', 'city', 'age', 'company', 'job', 'credit_card',
    ]

    def __init__(self, name, first_name, last_name, country, postcode, city, age, company, job, credit_card):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.postcode = postcode
        self.city = city
        self.age = age
        self.company = company
        self.job = job
        self.credit_card = credit_card

def read_csv(file_name="huge_file.csv"):
    df = pandas.read_csv(file_name)

    persons = [
        Person(
            row[1][0], row[1][1], row[1][2], row[1][3], row[1][4],
            row[1][5], row[1][6], row[1][7], row[1][8], row[1][9],
        )
        for row in df.iterrows()
    ]
    return persons

def manipulate_persons(persons: List[Person]):
    for p in persons:
        p.name = f"{p.first_name}-{p.last_name}"
        p.job = f"{p.company} - {p.job}"

@line_profile
def client():
    persons = read_csv()
    manipulate_persons(persons)

client()
```





## 3.  Sample Code Profiling

프로파일링은 `line-profiler`, `memory-profiler` 를 사용했습니다.

| 구분                    | Create 메모리 | Create 시간 | Manipulate 시간 |
| ----------------------- | ------------- | ----------- | --------------- |
| Slot                    | 35.8613 MB    | 135931848   | 743313          |
| Normal                  | 42.46733 MB   | 174077001   | 1287511         |
| Compare (slot / normal) | 0.84 %        | 0.78 %      | 0.58 %          |



- 보다 `적은 메모리` 사용 확인
- 보다 `빠른 VO 생성 및 조작` 시간 확인

### 3.1. Noraml

```
## Normally
```shell
Timer unit: 1e-07 s

Total time: 17.5365 s
File: G:\Script_Project\my_study\Python\Magic-Method\slots\file_read_test\file_read_normally.py
Function: client at line 45

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    45                                           @line_profile
    46                                           def client():
    47         1  174077001.0 174077001.0     99.3      persons = read_csv()
    48         1    1287511.0 1287511.0      0.7      manipulate_persons(persons)

Filename: G:\Script_Project\my_study\Python\Magic-Method\slots\file_read_test\file_read_normally.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    44     54.7 MiB     54.7 MiB           1   @profile
    45                                         def client():
    46     95.3 MiB     40.5 MiB           1       persons = read_csv()
    47    105.7 MiB     10.5 MiB           1       manipulate_persons(persons)
```

### 3.2.  Using `__slots__`

```
## Using Slots
```shell
Timer unit: 1e-07 s

Total time: 13.6675 s
File: G:\Script_Project\my_study\Python\Magic-Method\slots\file_read_test\file_read_with_slot.py
Function: client at line 46

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    46                                           @line_profile
    47                                           def client():
    48         1  135931848.0 135931848.0     99.5      persons = read_csv()
    49         1     743313.0 743313.0      0.5      manipulate_persons(persons)

Filename: G:\Script_Project\my_study\Python\Magic-Method\slots\file_read_test\file_read_with_slot.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     54.8 MiB     54.8 MiB           1   @profile
    48                                         def client():
    49     89.0 MiB     34.2 MiB           1       persons = read_csv()
    50     99.4 MiB     10.4 MiB           1       manipulate_persons(persons)
```

### Ref

- [https://wiki.python.org/moin/UsingSlots](https://wiki.python.org/moin/UsingSlots)