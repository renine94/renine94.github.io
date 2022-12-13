# https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html?icmpid=docs_console_unmapped#custom-packages-gs
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