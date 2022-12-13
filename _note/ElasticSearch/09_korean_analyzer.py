# https://gh402.tistory.com/49
# https://gong-story.tistory.com/13
# https://docs.likejazz.com/wiki/Elasticsearch-%EC%9A%B4%EC%98%81/ (은전한잎))
# https://velog.io/@juunini/%EC%9D%80%EC%A0%84%ED%95%9C%EB%8B%A2%EA%B3%BC-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%82%AC%EC%A0%84-%EB%8F%99%EC%9D%98%EC%96%B4-%EC%82%AC%EC%A0%84

# 한글 분석기 중 유명한 것 2가지
# 1. nori_analyzer (es default 한글분석기)





# 2. 은전한잎 (opensearch)
{
  "settings": {
    "analysis": {
      "char_filter": {
        "char_filter_remove_space": {  # 띄어쓰기 모두 제거 필터
          "type": "pattern_replace",
          "pattern": "\\s+",
          "replacement": ""
        }
      },
      # 은전한닢과 노리가 서로 키워드가 다르니까 주의하셔야 합니다.
      "tokenizer": {
        "my_tokenizer": {
          "type": "seunjeon_tokenizer",
          "decompound": "true",         # 삼성전자, 삼성, 전자 모두 저장 true
          "index_poses": ["UNK","EP","I","J","M","N","SL","SH","SN","VCP","XP","XS","XR"],  # 조사 태그 관련(?)
          "user_words": ["내추럴발란스"], # 인라인
          "user_dict_path": {{'AWS_PACKAGE_PATH'}} # 파일 패스 지정  (analyzer/F111111111)
        }
      },
      "filter": {
        "filter_synonym": {
          "type": "synonym",
          "synonyms": ["내츄럴발란스, 네츄럴발란스, 네추럴발란스, 내추럴밸런스, 내츄럴밸런스, 네츄럴밸런스 => 내추럴발란스"],  # 인라인
          "synonyms_path": {{'AWS_PACKAGE_PATH'}}  # 파일 패스 지정 (analyzer/F111111111)
        }
      },
      "analyzer": {
        "analyzer_search_product_name": {
          "type": "custom",
          "char_filter": ["char_filter_remove_space"],
          "tokenizer": "tokenizer_custom_user_dict",
          "filter": ["filter_synonym"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "name": {
        "type": "text",
        "analyzer": "analyzer_search_product_name"
      },
      "search_keywords": {
        "type": "text"
      }
    }
  }
}
