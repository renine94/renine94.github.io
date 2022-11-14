# https://minu0807.tistory.com/40
# https://findstar.pe.kr/2018/01/17/understanding-whildcard-query-on-elasticsearch/
# https://findstar.pe.kr/2018/07/14/elasticsearch-wildcard-to-ngram/ ---> wildcard 대신 ngram 을 이용하는 방법 (속도 더 빠름 카카오개발자 글))
# 특정필드에 단어가 있는지 없는지 확인하는 쿼리

search_keyword = '검색할 단어'
pet_type = 'DOG'
{
    "sort": [
        "_score",
        {"_id": {"order": "asc"}}
    ],
    "query": {
        "bool": {
            "must": [
                {"wildcard": {"search_keyword": f'*{search_keyword}*'}},
                {"match": {"pet_type": pet_type}}
            ]
        }
    }
}


# 여러개의 와일드카드 단어로, 여러개의 필드를 검색
# USER_ID, USER_EMAIL 중에 admin을 포함하거나 nct가 포함된 정보를 찾아준다.
{
    "query":{
        "query_string":{
            "fields":["USER_ID", "USER_EMAIL"],
            "query":"*admin* *nct* "
        }
    }
}