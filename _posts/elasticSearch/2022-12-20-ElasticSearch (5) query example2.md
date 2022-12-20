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

title: "[ES] 검색에서 사용되는 다양한 Query 예제 정리 (2)"
excerpt: "🚀 ES에서 사용되는 검색 Query 정리 - bool, must, must_not, should, filter"

categories: elasticSearch
tag: [es, elasticSearch, elk, search, query, bool, must, must_not, filter, should]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Query Sample (2)

> 검색에서 사용되는 복합쿼리인 `bool` 에 대해 학습합니다. <br>
>
> 여러 쿼리를 조합하기 위해서는 상위에 bool 쿼리를 사용하고 그 안에 다른 쿼리를 넣어 복합 쿼리를 완성합니다.
>
> 학습 내용에 대한 [출처](https://esbook.kimjmin.net/05-search/5.2-bool){: .btn .btn--danger} 입니다.

## 01. Bool

- **must** : 쿼리가 True인 도큐먼트를 검색
- **must_not** : 쿼리가 False인 도큐먼트를 검색
- **should** : 검색 결과 중 이 should 에 매칭되는 도큐먼트들의 score 값을 높입니다.
- **filter** : 쿼리가 True인 도큐먼트를 검색하지만 스코어를 계산하지않고, must 보다 빠르고 캐싱이 가능



example

```json
GET {index_name}/_search
{
  "query": {
    "bool": {
      "must": [
        {},
        {}
      ],
      "must_not": [
        {},
        {}
      ],
      "should": [
        {},
        {}
      ],
      "filter": [
        {},
        {}
      ]
    }
  }
}
```

<br><br>

---

`bool` 쿼리로 "잇츄" 와 "내츄럴발란스 울트라" 검색

```json
GET {index_name}/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "잇츄"
          }
        },
        {
          "match_phrase": {
            "message": "내츄럴발란스 울트라"
          }
        }
      ]
    }
  }
}
```

<br>

---

**단어 "quick"** 와 **구문 "lazy dog"** 가 하나도 포함되지 않은 문서 검색

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "match": {
            "message": "quick"
          }
        },
        {
          "match_phrase": {
            "message": "lazy dog"
          }
        }
      ]
    }
  }
}
```

<br><br>



**bool 쿼리를 이용해서 복합적인 검색기능을 구현**할 수 있습니다.

특히 bool 쿼리는, 정확도(Relevancy) 와도 관계가 있기 때문에 알아둬야 합니다.
bool 쿼리의 **must, should** 등을 표준 SQL의 **AND, OR** 등과 유사하지만 정확히 같지는 않습니다. bool 쿼리에는 SQL의 **OR** 와 정확히 일치하게 동작한다고 할 수 있는 연산자는 없어서 처음에는 이해하기가 조금 어렵습니다.

![image-20221220113339764](../../assets/images/posts/2022-12-20-ElasticSearch (5) query example2/image-20221220113339764.png)



`(A or B) and (not C)` 에 대한 쿼리를 하려면 elasticSearch의 경우 다음처럼 A와 B의 OR 조건의 match 쿼리로 하여 must 안에 넣고 C를 must_not에 넣으면 됩니다.

![image-20221220113512730](../../assets/images/posts/2022-12-20-ElasticSearch (5) query example2/image-20221220113512730.png)

