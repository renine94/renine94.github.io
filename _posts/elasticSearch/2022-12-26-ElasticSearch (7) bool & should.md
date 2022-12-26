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

title: "[ES] bool 복합쿼리에서 should 사용법에 대해 알아보자."
excerpt: "🚀 ES 에서 여러 조건을 복합적으로 사용가능하게 해주는 bool 에서 should 로 가중치를 높이는 방법 "

categories: elasticSearch
tag: [es, elasticSearch, bool, should, match_phrase]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Bool

> must, must_not, **should**, filter
>
> should 에 대해 알아보겠습니다.



**bool**쿼리의 **should** 는 검색 점수를 조정하기 위해 사용될 수 있다.

match 쿼리로 fox 를 포함하고 있는 Document를 검색한 결과.

- query

```json
// match 쿼리로 fox 검색
GET my_index/_search
{
  "query": {
    "match": {
      "message": "fox"
    }
  }
}
```



- Response

```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
		...
  },
  "hits" : {
    "total" : {
      ...
    },
    "max_score" : 0.32951736,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "The quick brown fox"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "Brown fox brown dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the lazy dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the quick dog"
        }
      }
    ]
  }
}
```



이 결과들 중 **lazy** 가 포함된 결과에 가중치를 줘서 결과를 상위에 올리고 싶으면 다음과 같이 **should** 안에 **lazy** 를 찾는 검색을 추가한다.

- query

```json
// fox 검색 결과 중 lazy 를 포함한 결과에 가중치 부여

GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "fox"
          }
        }
      ],
      "should": [
        {
          "match": {
            "message": "lazy"
          }
        }
      ]
    }
  }
}
```



- response

```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    ...
  },
  "hits" : {
    "total" : {
      ...
    },
    "max_score" : 0.9489644,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.9489644,
        "_source" : {
          "message" : "The quick brown fox jumps over the lazy dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "The quick brown fox"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 0.32951736,
        "_source" : {
          "message" : "Brown fox brown dog"
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.23470737,
        "_source" : {
          "message" : "The quick brown fox jumps over the quick dog"
        }
      }
    ]
  }
}
```



새로운 검색 결과에서 fox만 포함하고 있던 "The quick brown fox"는 점수가 `0.3295...` 로 이전 match 쿼리와 동일하지만, **lazy** 를 함께 포함하고 있는 "The quick brown fox jumps over the lazy dog" 는 점수가 `0.9489...` 로 가중되어 가장 상위에 나타납니다.

**should** 는 **match_phrase** 와 함께 유용하게 사용가능하다. 보통 쇼핑몰 검색에서 검색어로 입력된 단어가 하나라도 포함된 결과들은 모두 가져오도록 되어있다. 이 때 검색 결과 중에서 입력한 검색어 전체 문장이 정확히 일치하는 결과를 맨 상위에 위치시키면 다른 결과들을 누락시키지 않으면서 사용자가 원하는 수준 높은 품질의 결과를 제공할 수 있을것이다.



- **lazy** or **dog** 중 하나라도 포함된 도큐먼트를 모두 검색
- 그 중에 **lazy dog** 구문을 정확히 포함하는 결과를 가장 상위로 노출

```json
GET my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": {
              "query": "lazy dog"
            }
          }
        }
      ],
      "should": [
        {
          "match_phrase": {
            "message": "lazy dog",
            "slop": 1
          }
        }
      ]
    }
  }
}
```



`slop: 1` 값을 주게되면, 

"스키 장갑" 으로 검색 시, "스키 벙어리 장갑" 같이 스키와 장갑 사이에 다른 값이 들어간 결과에도 가중치를 부여할 수 있습니다.
