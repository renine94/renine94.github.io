# https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html?icmpid=docs_console_unmapped#custom-packages-gs
# https://devpouch.tistory.com/105 - 다른 원격 클러스터에서 현재 클러스터로 reindex


# 새로운 인덱스를 만들고 재색인을 할 때 사용한다.


# POST _reindex
{
  "source": {
    "index": "my-index"
  },
  "dest": {
    "index": "my-new-index"
  }
}


# POST _reindex?wait_for_completion=true
{
  "source": {
    "remote": {
      "host": "http://otherhost:9200",  # 443
      "username": "user",
      "password": "pass"
    },
    "index": "machine_log",
    "query": {
      "match": {
        "test": "data"
      }
    }
  },
  "dest": {
    "index": "another_machine_log"
  }
}