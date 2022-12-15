# "term: 6 x 9 was completely eliminated by analyzer"
# edgeNgram 때문에 이 같은 현상이 나타나며, min_gram, max_gram 을 설정을 잘해줘야 한다. 스택오버플로우 댓글
# https://stackoverflow.com/questions/72315212/elastic-search-synonym-completely-eliminated-by-analyzer


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
            "synonyms": [
              "치악, 치액, 치억 => 치약"
            ],                                        # 유사어 사전 인라인으로 정의할때, 위에 path 둘중 하나만 사용
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