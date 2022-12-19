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

title: "[ES] 검색에서 사용되는 다양한 Query 예제 정리 (1)"
excerpt: "🚀 ES에서 사용되는 검색 Query 정리 - match_all, match, match_phrase, query_string"

categories: elasticSearch
tag: [es, elasticSearch, elk, search, query, match, match_phrase]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Query Sample

> ES 에서 사용되는 다양한 검색기법 Query 들의 종류들에 대해 알아보고, 그 차이점을 알아봅니다.

<br><br>

## match_all

- 모든 Document 들을 검색합니다.

```json
// GET {{my_index}}/_search
{
  "query":{
    "match_all":{ }
  }
}
```

---

## match

- analyzer, boost, fuzziness, operator 등의 옵션을 설정할 수 있다.
- operator는 `"and", "or"` 의 옵션을 줄 수 있습니다.
  - `and`: query에 들어간 단어 모두 매칭되는 document 검색
  - `or`: query에 들어간 단어중 하나라도 매칭되는 document 검색 (default 값)
- boost는 매칭된 도큐먼트 score에 영향을 얼마나 줄지 가중치를 결정합니다.
- fuzziness 는 약간 단어를 한 두글자 다르게 검색해도 매칭되도록 찾아주는 옵션인데, 조금 더 공부해봐야 할것 같습니다.

```json
GET /product_to_search_v6/_search
{
  "_source": "product_name",
  "query": {
    "match": {
      "product_name": {
        "query": "헤이제리 아이스팝",
        "analyzer": "standard",
        "boost": 1,
        "fuzziness": 1,
        "operator": "or"
      }
    }
  }
}


// 부스팅 점수를 높게주면 score 값이 바뀌게 됩니다.
"hits" : {
    "total" : {
      "value" : 70,
      "relation" : "eq"
    },
    "max_score" : 14.231924,
    "hits" : [
      {
        "_index" : "product_to_search_v6",
        "_type" : "_doc",
        "_id" : "1000013802",
        "_score" : 14.231924,
        "_source" : {
          "product_name" : "헤이제리 아이스팝 리드줄 그린"
        }
      },
      {
        "_index" : "product_to_search_v6",
        "_type" : "_doc",
        "_id" : "1000013800",
        "_score" : 14.015726,
        "_source" : {
          "product_name" : "헤이제리 아이스팝 리드줄 블루"
        }
      }
    ]
  }
```

---

## match_phrase

- query, analyzer, slop 옵션을 넣을 수 있습니다.
- **주로 내가 검색한 단어가 필수적으로 들어가면서 중간에 다른 단어가 들어가는 경우를 검색할 때 사용됩니다.**

```json
GET /product_to_search_v6/_search
{
  "_source": "product_name",
  "query": {
    "match_phrase": {
      "product_name": {
        "query": "헤이제리 그린",
        "slop": 2
      }
    }
  }
}


// slop 2로 설정 했기 때문에 "헤이제리" 와 "그린" 단어 사이에 2개단어가 더 있어도 검색이 됩니다.
"hits" : [
      {
        "_index" : "product_to_search_v6",
        "_score" : 6.0450287,
        "_source" : {
          "product_name" : "헤이제리 아이스팝 리드줄 그린"
        }
      },
      {
        "_index" : "product_to_search_v6",
        "_score" : 4.6740093,
        "_source" : {
          "product_name" : "헤이제리 힙스터 파자마 그린 (S-XXL)"
        }
      }
]
```

---

## query_string

- URL 검색에 사용되는 루씬 검색 문법을 본문 검색에 이용하고 싶을 때 사용
- product_name 필드에서 "헤이제리" 와 "그린" 을 모두 포함하거나, 또는 "잇츄 디즈니" 구문을 포함하는 도큐먼트 검색
- "잇츄 디즈니" 처럼 구문검색을 하기위해서는 `\"검색이 필요합니다.\"`
- **저는 개인적으로 잘 쓰지 않는것 같습니다.**
  - bool, should, match 등을 더 많이 사용하게 되는것 같아요.
  - 위의 예시는 다음 포스팅에서 설명하도록 하겠습니다!

```json
GET /product_to_search_v6/_search
{
  "_source": "product_name", 
  "query": {
    "query_string": {
      "default_field": "product_name.standard",
      "query": "(헤이제리 AND 그린) OR \"잇츄 디즈니\""
    }
  }
}

// 검색결과
"hits" : [
      {
        "_score" : 12.372238,
        "_source" : {
          "product_name" : "it 잇츄 디즈니 (딸기/바나나/블루베리)"
        }
      },
      {
        "_score" : 11.4544525,
        "_source" : {
          "product_name" : "헤이제리 아이스팝 리드줄 그린"
        }
      },
      {
        "_score" : 9.480416,
        "_source" : {
          "product_name" : "헤이제리 힙스터 파자마 그린 (S-XXL)"
        }
      },
      {
        "_score" : 9.249556,
        "_source" : {
          "product_name" : "헤이제리 펌킨 캔디 오버롤 그린 (S-XXL)"
        }
      },
      {
        "_score" : 9.220066,
        "_source" : {
          "product_name" : "헤이제리 썸머 슬리브리스 러브탑 그린 (S-XXL)"
        }
      },
      {
        "_score" : 8.863382,
        "_source" : {
          "product_name" : "헤이제리 아이스팝 하네스 그린 (S/M/L)"
        }
      }
    ]
```

