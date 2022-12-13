# https://www.skyer9.pe.kr/wordpress/?p=962
# https://heesutory.tistory.com/30
# https://kazaana2009.tistory.com/6 (스코어 결합하기, score_mode, boost_mode)
# https://ksk-developer.tistory.com/27
# https://tech.buzzvil.com/blog/probability-in-es-search/


GET /product_to_search_v5/_search
{
    "query": {
        # function_score 는 기본적으로 Document의 Score 계산 방식을 조작할 수 있게 해주는 쿼리이다.
        # 중요!, 이미 쿼리로 인해 계산되어 나온 score점수에 다시 변화를 줄 때 사용 (weight 기반으로 다시 or 클릭횟수로 다시 점수 더 올리거나)
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
    # 성능이 좋지 않다. painless 문법을 사용할 수 있게 된다.
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