# 유사어 필터 (토큰 필터에 정의)

# PUT my-index
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {                                 # es 기본 분석기 (https://www.elastic.co/guide/en/elasticsearch/reference/7.17/analysis-analyzers.html)
          "my_analyzer": {
            "type": "custom",
            "tokenizer": "standard",                  # es 기본 토크나이저 (https://www.elastic.co/guide/en/elasticsearch/reference/7.17/analysis-tokenizers.html)
            "filter": ["my_filter"]
          }
        },
        "filter": {                                   # 토큰 필터
          "my_filter": {
            "type": "synonym",                        # 동의어(유사어)
            "synonyms_path": "analyzers/F111111111",  # aws opensearch 사용자정의 패키지 (s3 업로드후 도메인 적용 필요)
            "updateable": True                        # 이 옵션 정확히 어떤 의미인지 확인필요
          }
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "standard",
        "search_analyzer": "my_analyzer"
      }
    }
  }
}