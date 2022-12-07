# https://www.elastic.co/guide/en/elasticsearch/reference/current/search-analyzer.html

# 1. Keyword Type 에는 Analyzer 적용이 불가능하다. (Normalizer) 만 적용가능
# Normalizer = Analyzer - Tokenizer
# 즉 필터들만 적용가능한게 노말라이저.


# 인덱스 설정에서 analyzer 와 search_analyzer 차이

# analyzer 는 데이터 색인 시 색인하는 분석기 지정
# search_analyzer 는 검색 시 검색문을 분석하는 분석기 지정
# 한국어 형태소분석기 플러그인 중 하나인 은전한잎(seunjeon)
