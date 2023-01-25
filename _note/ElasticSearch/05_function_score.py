# https://www.skyer9.pe.kr/wordpress/?p=962
# https://heesutory.tistory.com/30
# https://ksk-developer.tistory.com/27
# https://tech.buzzvil.com/blog/probability-in-es-search/



# https://kazaana2009.tistory.com/6 (스코어 결합하기, score_mode, boost_mode)  - 점수 계산법 블로그 좋음
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
            "score_mode": "max",        # functions 배열안에 함수들의 점수를 어떻게 계산할지 정의
            "boost_mode": "multiply",   # score_mode로 구한 점수를 기존에 구해진 _score 와 어떻게 계산할지 정의
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
    # functions 배열안에 정의해도 되고, 바로 적어도 된다. (2개 다는 안됨)
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

########################################################################
# 실제 예제
########################################################################
GET /product_to_search_v6/_search
{
    "min_score": 0.01,  # 검색된 문서가 최소 0.01 점수를 가져야 보여준다.
    "_source": [
        "product_name"
    ],
    "query": {
        "function_score": {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"categories.name.standard": {"query": "내 추 럴 발 란 스","boost": 10}}},
                        {"match": {"brand.name.standard": {"query": "내 추 럴 발 란 스","boost": 10}}},
                        {"match": {"search_keywords.ngram": {"query": "내 추 럴 발 란 스","boost": 5}}},
                        {"match": {"product_name.ngram": {"query": "내 추 럴 발 란 스","boost": 30,"analyzer": "analyzer_search_standard"}}},
                        {"match": {"product_name.ngram": {"query": "내 추 럴 발 란 스","boost": 0.01}}},
                        {"match": {"product_name.front_edge_ngram": {"query": "내 추 럴 발 란 스","boost": 5,"analyzer": "analyzer_search_standard"}}},
                        {"match": {"product_name.back_edge_ngram": {"query": "내 추 럴 발 란 스","boost": 10,"analyzer": "analyzer_search_standard"}}},
                        {"match": {"product_name.whitespace": {"query": "내 추 럴 발 란 스","boost": 150,"analyzer": "analyzer_product_whitespace_search"}}},
                        {"match": {"is_real_sold_out": {"query": false,"boost": 4000}}}
                    ],
                    "minimum_should_match": 2,  # 위에 should 중에 최소 2개는 만족해야 한다.
                    "must_not": [{"term": {"pet_type": "DOG"}}]
                }
            },
            "functions": [    # es에서 제공해주는 기본 function 들이 매우 많다. 그 중에 script_score를 사용한다는 뜻
              {
                "script_score": {
                  "script": {
                    "source": "_score * 0",
                    "params": {
                      "factor": 0
                    }
                  }
                }
              }
            ],
            "score_mode": "sum",        # functions 배열안에 함수들의 점수를 어떻게 계산할지 정의
            "boost_mode": "multiply"    # score_mode로 구한 점수를 기존에 구해진 _score 와 어떻게 계산할지 정의
        }
    },
    "script_fields": {                  # custom fields 를 만들겠다는 뜻
        "kyle_test_field_1": {
            "script": {
                "source": "Math.log(doc['weight'].value + 1) * params.factor",
                "params": {
                    "factor": 10
                }
            }
        },
        "kyle_test_field_2": {
            "script": {
                "source": "params.kyle",
                "params": {
                    "kyle": 2
                }
            }
        }
    }
}
