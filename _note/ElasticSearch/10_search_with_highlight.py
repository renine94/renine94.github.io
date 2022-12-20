GET autocomplete_test_2/_search
{
  "query": {
    "match": {
      "word": "세트"
    }
  },
  "highlight": {
    "fields": {
      "word": {}
    }
  }
}

####
{
  "took" : 27,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 8,
      "relation" : "eq"
    },
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "4",
        "_score" : 0.2876821,
        "_source" : {
          "word" : "여성 속옷 세트"
        },
        "highlight" : {
          "word" : [
            "여성 속옷 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "word" : "추석 선물 세트"
        },
        "highlight" : {
          "word" : [
            "추석 선물 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "6",
        "_score" : 0.21110919,
        "_source" : {
          "word" : "설화수 세트"
        },
        "highlight" : {
          "word" : [
            "설화수 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "5",
        "_score" : 0.19856803,
        "_source" : {
          "word" : "선물 세트"
        },
        "highlight" : {
          "word" : [
            "선물 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "7",
        "_score" : 0.19566217,
        "_source" : {
          "word" : "달고나 만들기 세트"
        },
        "highlight" : {
          "word" : [
            "달고나 만들기 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "8",
        "_score" : 0.17068402,
        "_source" : {
          "word" : "무선 키보드마우스 세트"
        },
        "highlight" : {
          "word" : [
            "무선 키보드마우스 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "3",
        "_score" : 0.16853255,
        "_source" : {
          "word" : "김밥 재료 세트"
        },
        "highlight" : {
          "word" : [
            "김밥 재료 <em>세트</em>"
          ]
        }
      },
      {
        "_index" : "autocomplete_test_2",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 0.160443,
        "_source" : {
          "word" : "여성 트레이닝복 세트"
        },
        "highlight" : {
          "word" : [
            "여성 트레이닝복 <em>세트</em>"
          ]
        }
      }
    ]
  }
}

