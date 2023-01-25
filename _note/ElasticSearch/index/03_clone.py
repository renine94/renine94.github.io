
# index 를 복제하고 싶을때 명령어.
# POST /{source_index}/_clone/{target_index}


# 위 명령어가 오류날때, index 가 read_only 상태면 clone 이 되지 않으므로 아래 설정으로 write True 옵션을 주면 해결
# PUT {source_index}/_settings
{
  "index": {
    "blocks.write": true
  }
}