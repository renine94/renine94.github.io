# https://www.skyer9.pe.kr/wordpress/?p=962
# https://heesutory.tistory.com/30
# https://kazaana2009.tistory.com/6 (스코어 결합하기, score_mode, boost_mode)
# https://ksk-developer.tistory.com/27

GET /product_to_search_v5/_search
{
    "query": {
        "function_score": {
            "query": {
                "match": {
                    "itemname": "아이폰 케이스"
                }
            },
            "boost": "5",
            "functions": [
                {
                    "filter": {
                        "match": {
                            "viewKeywords": "아이폰 케이스"
                        }
                    },
                    "random_score": {},
                    "weight": 23
                },
                {
                    "filter": {
                        "match": {
                            "buyKeywords": "아이폰 케이스"
                        }
                    },
                    "weight": 42
                }
            ],
            "max_boost": 42,
            "score_mode": "max",
            "boost_mode": "multiply",
            "min_score": 0
        }
    }
}


#
{
  "function_score": {
    "query": {
        "multi_match": {
            "query": None,
            "fields": [
                "name^5",
                "category"
            ]
        }
    },
    "script_score": {
        "script": {
            "source": "cosineSimilarity(params.query_vector, 'name_vector') + 1.0",
            "params": {
                "query_vector": None
            }
        }
    }
  }
}