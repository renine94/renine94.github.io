---
layout: single

header:
  teaser: /assets/images/logo/elasticSearch.png
  overlay_image: /assets/images/logo/elasticSearch.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[ES] 중간 정리 Summary"
excerpt: "🚀 ES, ELK, OpenSearch, ElasticSearch, Data Structure 명령어"

categories: elasticSearch
tag: [it, es, elasticSearch, elk, search]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# ElasticSearch

> 클러스터 둘러보기

## 1. Cluster

### REST API

노드 및 클러스터와 통신하는 방법을 알아볼 차례이다. ES 는 클러스터와의 상호 작용에 사용할 수 있는 매우 포괄적이고 강력한 `REST API` 를 제공한다. 이 API 에서 다음을 비롯한 다양한 작업을 수행할 수 있다.

- Cluster, Node, Index 의 상태 및 통계 정보 확인
- Cluster, Node, Index 의 데이터 및 메타데이터 관리
- Index에 대한 CRUD 및 검색 작업 수행
- paging, sort, filtering, scripting, aggregation 등 여러 고급 검색 작업 실행



```python
# index(DB/Table 생성)
PUT user

# 현재 index 리스트 확인하기
GET _cat/indices

# index 의 레플리카 개수 0개로 만들어 Yellow > Green 상태로 만들기
PUT _settings
{
  "index": {
    "number_of_replicas": 0
  }
}

# 현재 index 리스트 재확인하기
GET _cat/indices

# index 에 document 추가하기 (ID 포함)
POST user/_doc/1
{
  "name": "kangjaegu"
}

# index 에 document 추가하기 (ID 미포함)
POST user/_doc/
{
  "name": "kangjaegu2"
}

# 모든 Document 조회하기
GET user/_search


# 특정 Document 조회하기
GET user/_doc/1

# document 수정
POST user/_doc/1
{
  "name": "kangjaegu_modified"
}

# 수정된 Document 재확인
GET user/_doc/1

############################################################

# example Index가 없는 상태에서 example 인덱스 데이터를 추가하면 자동으로
# example index가 생성되고, 매핑된다
GET _cat/indices

PUT example/_doc/1
{
  "content": "test"
}

GET example/_doc/1

GET _cat/indices

# 매핑정의
# 동적 매핑 방식으로 가장 넓은 형태의 데이터 타입으로 매핑을 생성하는게 아니라,
# 미리 정의 해놓고 싶다면 아래와 같은 방식을 사용하면 된다.
# 이미 만들어진 매핑에 필드 추가는 가능
# 이미 만들어진 필드를 삭제하거나 필드의 타입 및 설정값을 변경하는 불가능
# (필드의 변경이 필요한 경우 re-indexing 필요)
PUT user
{
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      }
    }
  }
}

# index 새로 만들기 (+mapping 과 함께)
PUT /test_index
{
  "mappings": {
    "properties": {
      "text_name":{
        "type": "text"
      },
      "keyword_name": {
        "type":"keyword"
      }
    }
  }
}

# 새로 만든 test_index 구조 확인하기
GET /test_index


# 만든 index 에 데이터 넣기
PUT /test_index/_doc/1
{
  "text_name":"I am jaegu.",
  "keyword_name":"I am jaegu."
}

# 자료형을 Keyword 로 넣은것은 검색되지 않는다.
GET /test_index/_search
{
   "query": {
      "match": {"keyword_name": "jaegu"}
   }
}

# 자료형을 Text 로 넣은것은 잘 검색된다.
GET /test_index/_search
{
   "query": {
      "match": {"text_name": "jaegu"}
   }
}

############################################################

# Inter 자료형을 저장하기 위한 test_index 를 다시 만들어보자.
# Field 는 long_num 이고, 데이터타입은 long, 숫자로 이해할수있는형식은 숫자로저장 "4" > 4
PUT /test_num
{
  "mappings": {
    "properties": {
      "long_num": {
        "type": "long",
        "coerce": true
      }
    }
  }
}

# index DDL 확인하기
GET /test_num

# index data 확인하기
GET /test_num/_search

# index_num 에 데이터 넣기
PUT /test_num/_doc/1?pretty
{
  "long_num": 4.3
}


# 데이터 가져오기
# long_num 필드의 값이 3 <= data < 4.2 값을 요청하는데, 검색이 된다?
# coerce=True 이기 때문에 4.3 > 4 로 저장되었기 때문이다.
GET /test_num/_search
{
   "query": {
      "range": {
        "long_num": {
          "gte": 3,
          "lt":4.2
        }
      }
   }
}
```



## 2. 자료형의 종류

### 문자열

- Text
  1. 입력된 문자열을 텀 단위로 쪼개어 "역 색인" 구조로 만듬
  2. Full Text 검색에 사용할 문자열 필드
- Keyword
  1. 입력된 문자열을 하나의 토큰으로 저장
  2. Text 타입에 keyword 분석기를 적용한 것과 동일
  3. 집계 또는 정렬에 사용

### 숫자

- long
  - 64비트 정수
- integer
  - 32비트 정수
- short
  - 16비트 정수
- byte
  - 8비트 정수
- double
  - 64비트 실수
- float
  - 32비트 실수
- half_float
  - 16비트 실수
- scaled_float
  - 실수형이지만, 부동소수점이 아니라 long형태로 저장하고 옵션으로 소수점 위치를 지정

### 날짜

- ISO8601 형식을 따라 입력
- "2019-06-02", "2019-06-12T17:13:40", "2019-06-12T17:13:40+09.00" 으로 입력된 경우 자동으로 날짜 타입으로 인식
- 위와 같은 형식이 아닌 경우에는 text, keyword로 저장

### 불리언

- true
- false

### 객체(Object)

- 1번 유저

```python
"user" : [
   {"name" : "soyeon","age" : 21,"phone" : "01012341234"},
   {"name" : "test","age" : 15,"phone" : "01015155555"}
]
```

- 2번 유저

```python
"user" : [
   {"name" : "chae","age" : 30,"phone" : "01012341234"},
   {"name" : "soyeon","age" : 19,"phone" : "01019191919"}
]
```



위와 같이 저장되어 있을 때.  아래와 같은 Query 를 조회하게된다면,

```python
GET /test_game/_search
{
  "query": {
    "bool": {
      "mmust": [
        {
          "match":  {
            "user.name": "jaegu"
          }
        },
        {
          "match": {
            "user.phone": "01012341234"
          }
        }
      ]
    }
  }
}
```

 User.name이 jaegu 이면서, user.phone 이 01012341234 인 Document 만 검색이 되겠지라고 기대하지만,,,

실제로는 2개의 Document 모두 검색되는것을 확인할 수 있다. 

**이유는 역색인 때문** 이다.



### Nested



### Geo

- Geo Point
- Geo Shape



### IP, Range, Binary