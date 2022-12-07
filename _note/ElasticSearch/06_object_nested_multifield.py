# https://www.elastic.co/guide/en/elasticsearch/reference/current/nested.html
# https://esbook.kimjmin.net/07-settings-and-mappings/7.3-multi-field
# https://velog.io/@rudaks94/elasticsearch-nested-field-type
# https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-nested-field-object-field/
# https://www.youtube.com/watch?v=yqAKfwGZpE0

# object

# 1.데이터를 입력한다.
PUT index-object/_doc/1
{
  "group" : "fans",
  "user" : [
    {
      "first" : "John",
      "last" :  "Smith"
    },
    {
      "first" : "Alice",
      "last" :  "White"
    }
  ]
}
# 2. 아래와 같이 저장된다.
{
  "group" :        "fans",
  "user.first" : [ "alice", "john" ],
  "user.last" :  [ "smith", "white" ]
}
# 3. user.first와 user.last 필드는 multi-value로 변환되고 alice와 white와의 연관성을 없어진다. 이 문서는 alice와 smith에 대한 쿼리를 부정확하게 조회할 것이다.
GET index-object/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "user.first": "Alice" }},
        { "match": { "user.last":  "Smith" }}
      ]
    }
  }
}


# nested

# multi-field