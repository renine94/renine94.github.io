# _analyze API
# 토크나이저는 tokenizer, 토큰 필터는 filter 항목에 값으로 입력하면 된다.
# 토크나이저는 하나만 적용되기 떄문에 바로 입력하고, 토큰필터는 여러개를 적용할 수 있기 때문에 []안에 배열 형식으로 입력한다.

GET _analyze
{
  "text": "The quick brown fox jumps over the lazy dog",
  "tokenizer": "whitespace",
  "filter": [
    "lowercase",
    "stop",
    "snowball"
  ]
}

GET _analyze
{
  "text": "The quick brown fox jumps over the lazy dog",
  "tokenizer": "whitespace",
  "filter": [
    "stop",
    "lowercase",
    "snowball"
  ]
}

# 위 두가지를 비교해보면 , 필터의 순서가 다른데 lowercase 보다 stop필터를 먼저 사용하게되면 'the'가 정상적으로 지워지지 않는다.
# 그 이유는 'The' 는 stop 필터에 해당되지 않기 때문. 그 다음 lowercase가 적용되어서 'The'가 'the'로 바뀐다.
# 그러므로 [ 여러 개의 토큰 필터를 입력 할 때는 순서가 중요하다 ]


# _analyze API 에서 analyzer 항목으로 적용해서 사용도 가능.
# 캐릭터 필터, 토크나이저, 토큰 필터를 조합해서 사용자 정의 애널라이저를 만들 수도 있고, ES에 사전에 정의되어 있어서 바로 사용 가능한 애널라이저도 있다.
# 예를 들면 whitespace 토크나이저, lowercase-stop-snowball 토큰필터들을 조합한 것이 [ snowball 애널라이저 ] 이다. 바로 사용가능
# 사용자 정의 애널라이저의 방법으로 시도한 위의 코드와 동일한 성능

GET _analyze
{
  "text": "The quick brown fox jumps over the lazy dog",
  "analyzer": "snowball"
}



# 인덱스에 애널라이즈 설정 예시
# 인덱스의 message 필드에 snowball 애널라이저 적용
PUT my_index2
{
  "mappings": {
    "properties": {
      "message": {
        "type": "text",
        "analyzer": "snowball"
      }
    }
  }
}


# jumps를 포함하는 도큐먼트 색인
PUT my_index2/_doc/1
{
  "message": "The quick brown fox jumps over the lazy dog"
}


# match 쿼리로 [ jump, jumps, jumping ]을 검색해도 결과가 동일하다.
# 입력된 검색어는 [ jumping ] 이지만 [ snowball ] 애널라이저를 거쳐 실제로는 [ jump ]로 검색한다.
# 역 인덱스에는 [ jumps ] 가 [ jump ]로 저장되어있다.

GET my_index2/_search
{
  "query": {
    "match": {
      "message": "jumping"
    }
  }
}
