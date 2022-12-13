# https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html?icmpid=docs_console_unmapped#custom-packages-gs
# 인덱스 분석기를 자주 업데이트하는 경우 인덱스 별칭을 사용한다.
# 최신 인덱스에 대한 일관된 경로를 유지하려면 다음을 수행하면 된다.

# POST _aliases
{
  "actions": [
    {
      "remove": {
        "index": "my-index",
        "alias": "latest-index"
      }
    },
    {
      "add": {
        "index": "my-new-index",
        "alias": "latest-index"
      }
    }
  ]
}