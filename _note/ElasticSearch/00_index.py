# 인덱스 생성 API
'PUT /{index_name}'
{
  "settings": {
    "index": {
      # 인덱스 생성시 샤드, 레플리카 개수 정의
      "number_of_shards": 3,
      "number_of_replicas": 1,
      # 분석기
      "analysis": {
        "analyzer": {

          "analyzer_test1": {
            "type": "custom",  # ES 에서 기본적으로 제공해주는 아이 써도 가능
            "char_filter": {},
            "tokenizer": {},
            "filter": {},  # token filter
          },


        }
      },
      # 캐릭터 필터
      "char_filter": {
        "char_filter_test1": {
          "type": "...",

        }
      },
      # 토크나이저
      "tokenizer": {
        "tokenizer_test1": {
          "type": "custom",  # standard, etc....
        }
      },
      # 토큰 필터
      "filter": {
        "filter_test1": {
          "type": "custom", # uppercase, etc....
        }
      },
      # ngram setting
      "max_gram_diff": "10",
    },
  },
  "mappings": {
    # 컬럼 정의
    "properties": {

      "field_name_01": {
        "type": "text",  # keyword
        "index": false,  # TODO 무엇인지 찾아볼것
      },

      "field_name_02": {
        "type": "keyword",  # text
      },

      "field_name_03": {
        "type": "text",
        "fields": {
          "<multi_field_name>": {
            "type": "text",
            "analyzer": "...",
            "search_analyzer": "...",
          },
          "<multi_field_name>": {
            "type": "keyword",
            "analyzer": "...",
            "search_analyzer": "...",
          }
        }
      }

    },
  },
}


############### Example ###############
{
    "product_to_search_v5": {
        "aliases": {},
        "mappings": {
            "properties": {
                "brand": {
                    "properties": {
                        "id": {
                            "type": "integer",
                            "fields": {
                                "keyword": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "list_image": {
                            "type": "text",
                            "index": false
                        },
                        "name": {
                            "type": "keyword",
                            "fields": {
                                "ngram": {
                                    "type": "text",
                                    "analyzer": "analyzer_product_ngram",
                                    "search_analyzer": "analyzer_search_product_ngram"
                                },
                                "standard": {
                                    "type": "text",
                                    "analyzer": "analyzer_standard",
                                    "search_analyzer": "analyzer_search_standard"
                                }
                            }
                        }
                    }
                },
                "categories": {
                    "properties": {
                        "code": {
                            "type": "keyword"
                        },
                        "id": {
                            "type": "integer",
                            "fields": {
                                "keyword": {
                                    "type": "keyword"
                                }
                            }
                        },
                        "name": {
                            "type": "keyword",
                            "fields": {
                                "ngram": {
                                    "type": "text",
                                    "analyzer": "analyzer_product_ngram",
                                    "search_analyzer": "analyzer_search_product_ngram"
                                },
                                "standard": {
                                    "type": "text",
                                    "analyzer": "analyzer_standard",
                                    "search_analyzer": "analyzer_search_standard"
                                }
                            }
                        }
                    }
                },
                "created_at": {
                    "type": "date"
                },
                "customer_price": {
                    "type": "double"
                },
                "discount_price": {
                    "type": "double"
                },
                "filter_brand": {
                    "type": "keyword"
                },
                "filter_categories": {
                    "type": "keyword"
                },
                "is_real_sold_out": {
                    "type": "boolean"
                },
                "is_sold_out": {
                    "type": "boolean"
                },
                "main_image": {
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "normal": {
                            "type": "text",
                            "index": false
                        },
                        "small": {
                            "type": "text",
                            "index": false
                        }
                    }
                },
                "pet_type": {
                    "type": "keyword"
                },
                "point": {
                    "type": "integer"
                },
                "price": {
                    "type": "double"
                },
                "product_id": {
                    "type": "integer"
                },
                "product_name": {
                    "type": "keyword",
                    "fields": {
                        "back_edge_ngram": {
                            "type": "text",
                            "analyzer": "analyzer_product_back_edge_ngram",
                            "search_analyzer": "analyzer_search_product_ngram"
                        },
                        "front_edge_ngram": {
                            "type": "text",
                            "analyzer": "analyzer_product_front_edge_ngram",
                            "search_analyzer": "analyzer_search_product_ngram"
                        },
                        "ngram": {
                            "type": "text",
                            "analyzer": "analyzer_product_ngram",
                            "search_analyzer": "analyzer_search_product_ngram"
                        },
                        "standard": {
                            "type": "text",
                            "analyzer": "analyzer_standard",
                            "search_analyzer": "analyzer_search_standard"
                        }
                    }
                },
                "product_promotions": {
                    "properties": {
                        "discount_price": {
                            "type": "double"
                        },
                        "ended_at": {
                            "type": "date"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "is_timesale": {
                            "type": "boolean"
                        },
                        "name": {
                            "type": "keyword"
                        },
                        "started_at": {
                            "type": "date"
                        }
                    }
                },
                "search_keywords": {
                    "type": "text",
                    "fields": {
                        "ngram": {
                            "type": "text",
                            "analyzer": "analyzer_product_ngram",
                            "search_analyzer": "analyzer_search_product_ngram"
                        }
                    },
                    "analyzer": "analyzer_standard",
                    "search_analyzer": "analyzer_search_standard"
                },
                "search_promotions": {
                    "type": "keyword"
                },
                "weight": {
                    "type": "integer"
                }
            }
        },
        "settings": {
            "index": {
                "max_ngram_diff": "10",
                "number_of_shards": "2",
                "provided_name": "product_to_search_v5",
                "creation_date": "1663205545012",
                "analysis": {
                    "filter": {
                        "filter_synonym": {
                            "type": "synonym",
                            "synonyms_path": "analyzers/F178422170",
                            "updateable": "true"
                        },
                        "back_edge_ngram": {
                            "min_gram": "1",
                            "side": "back",
                            "type": "edge_ngram",
                            "max_gram": "10"
                        },
                        "front_edge_ngram": {
                            "min_gram": "1",
                            "side": "front",
                            "type": "edge_ngram",
                            "max_gram": "10"
                        }
                    },
                    "analyzer": {
                        "analyzer_korean": {
                            "filter": [
                                "trim",
                                "lowercase"
                            ],
                            "type": "custom",
                            "tokenizer": "seunjeon"
                        },
                        "analyzer_search_standard": {
                            "filter": [
                                "filter_synonym",
                                "trim",
                                "lowercase"
                            ],
                            "type": "custom",
                            "tokenizer": "search_standard"
                        },
                        "analyzer_standard": {
                            "filter": [
                                "trim",
                                "lowercase"
                            ],
                            "type": "custom",
                            "tokenizer": "search_standard"
                        },
                        "analyzer_product_back_edge_ngram": {
                            "filter": [
                                "trim",
                                "lowercase",
                                "back_edge_ngram"
                            ],
                            "type": "custom",
                            "tokenizer": "search_standard"
                        },
                        "analyzer_search_product_ngram": {
                            "filter": [
                                "filter_synonym",
                                "trim",
                                "lowercase"
                            ],
                            "type": "custom",
                            "tokenizer": "search_product_ngram"
                        },
                        "analyzer_product_front_edge_ngram": {
                            "filter": [
                                "trim",
                                "lowercase",
                                "front_edge_ngram"
                            ],
                            "type": "custom",
                            "tokenizer": "search_standard"
                        },
                        "analyzer_product_ngram": {
                            "filter": [
                                "trim",
                                "lowercase"
                            ],
                            "type": "custom",
                            "tokenizer": "product_ngram"
                        }
                    },
                    "tokenizer": {
                        "product_ngram": {
                            "token_chars": [
                                "letter",
                                "digit"
                            ],
                            "min_gram": "2",
                            "type": "ngram",
                            "max_gram": "10"
                        },
                        "search_product_ngram": {
                            "token_chars": [
                                "letter",
                                "digit"
                            ],
                            "min_gram": "1",
                            "type": "ngram",
                            "max_gram": "10"
                        },
                        "seunjeon": {
                            "index_poses": [
                                "UNK",
                                "EP",
                                "I",
                                "J",
                                "M",
                                "N",
                                "SL",
                                "SH",
                                "SN",
                                "VCP",
                                "XP",
                                "XS",
                                "XR"
                            ],
                            "max_unk_length": "6",
                            "pos_tagging": "false",
                            "user_dict_path": "analyzers/F173667885",
                            "index_eojeol": "false",
                            "decompound": "false",
                            "type": "seunjeon_tokenizer"
                        },
                        "search_standard": {
                            "type": "standard"
                        }
                    }
                },
                "number_of_replicas": "1",
                "uuid": "D44UfX-US7Ku5CpzlGYB-Q",
                "version": {
                    "created": "7100299"
                }
            }
        }
    }
}
