# 검색결과에서 유니크한 값만 집계한다.

keyword = '강아지'
pet_type = 'DOG'

{
    "size": 0,
    "query": {
        "bool": {
            "must": [
                {"match": {"brand.name.ngram": keyword}},
            ],
            "filter": [
                {"term": {"pet_type": pet_type}},
            ],
        }
    },
    "aggs": {
        "ids": {  # 내가 이름 결정
            "terms": {
                "field": "brand.id",
            },
        },
    },
}
