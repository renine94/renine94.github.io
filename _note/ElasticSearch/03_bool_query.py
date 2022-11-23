# https://stdhsw.tistory.com/entry/Elasticsearch-%EA%B2%80%EC%83%89%ED%95%98%EA%B8%B02-bool-must-mustnot-should

# level 이라는 keyword 타입의 field 의 값이 'info' 값을 가지는 모든 도큐먼트 검색
GET /{index_name}/_search
{
  "query":{
    "bool":{
      "must":{
        "match":{
          "level":"info"
        }
      }
    }
  }
}

# Text Field 의 값이 "aaa", "open" 모든 값을 가지는 도큐먼트 검색
GET /{index_name}/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "message": "aaa"
          }
        },
        {
          "match": {
            "message": "open"
          }
        }
      ]
    }
  }
}


