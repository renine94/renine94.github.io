# https://blog.naver.com/PostView.nhn?blogId=occidere&logNo=222102329176
# https://joonable.tistory.com/38

# ES에 쓰이는 Painless 스크립트 언어가 무엇인가....

# GET /product_to_search_v5/_search
{
  "explain": true,
  "size": 1,
  "query": {
    "script": {
      "script": "doc['weight'].value == 100"
    }
  },
  "script_fields": {
    "custom_fields_1": {
      "script": {
        "source": "Math.random() * 100"
      }
    },
    "custom_fields_2": {
      "script": {
        "source": "Math.random()"
      }
    }
  }
}

# prop : %제거 → int 변환 → 0.01 곱셈 → 0.5보다 작은 경우 리턴
# GET product_to_search_v5/_search
{
  "query": {
    "script": {
      "script": "Integer.parseInt(doc['prop'].value.replace('%', '')) * 0.01 < 0.5"
    }
  }
}