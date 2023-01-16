# https://minu0807.tistory.com/60
# 특정필드가 있는 도큐먼트만 검색하는 쿼리
{
  "query": {
    "bool": {
      "must": [  # 특정필드가 없는데이터만 검색하려면 must_not
        {
          "exists": {
            "field": "{field_name}"
          }
        }
      ]
    }
  }
}