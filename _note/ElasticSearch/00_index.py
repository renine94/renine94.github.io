GET /{index_name}
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
