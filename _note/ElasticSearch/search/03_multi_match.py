"""
ES 에 multi_match 쿼리에 대해 알아보자.
참고블로그 : https://jangseongwoo.github.io/elasticsearch/elasticsearch_multi_match/

# multi_match
- type
1. `base_fields`: (Default) 모든 Field에 대해 Match되는 Field를 찾는다. 가장 잘 Match되는 1개의 Field를 기준으로 Score를 계산한다.
2. `mast_fields`: 모든 Field에 대해 Match되는 각 각의 field에 대해 점수를 계산하고 모두 합한다. 합한 점수를 field 개수로 나눠서 최종 스코어를 계산한다.
3. ... 위 링크 참고

"""

# GET {index}/_search
{
  "multi_match": {
    "query": "잇츄",
    "fields": [
      "categories.name.standard",
      "brand.name.standard",
      "search_keywords.ngram"
    ],
    "type": "most_fields"  # best_fields (default), most_fields, cross_fields, phrase, phrase_prefix, bool_prefix
  }
}


# multi_match 와일드 카드 지원
# Multi_match는 Wildcards를 지원한다. 다음은 예시이다. 예시에서는 “*_name”로 Field를 지정해 _name으로 끝나는 Field를 대상 Field로 지정한다.
# GET {index}/_search
{
  "query": {
    "multi_match" : {
      "query": "Will Smith",
      "fields": [ "title", "*_name" ]
    }
  }
}

# 가중치 지정 가능
# subject 필드가 3배 더 중요 가중치
# GET /_search
{
  "query": {
    "multi_match" : {
      "query" : "this is a test",
      "fields" : [ "subject^3", "message" ]
    }
  }
}