# https://brunch.co.kr/@alden/36
# https://repost.aws/knowledge-center/opensearch-resolve-429-error
# https://www.google.com/search?q=Amazon+OpenSearch+Deep+dive+-+%EB%82%B4%EB%B6%80%EA%B5%AC%EC%A1%B0%2C+%EC%84%B1%EB%8A%A5%EC%B5%9C%EC%A0%81%ED%99%94+%EA%B7%B8%EB%A6%AC%EA%B3%A0+%EC%8A%A4%EC%BC%80%EC%9D%BC%EB%A7%81%0A#fpstate=ive&vld=cid:65011440,vid:e9GpbaT18Mk
# ES 에 스레드풀. bulk API 요청시, 요청 처리할 수 있는 스레드가 없을때 발생하는 문제

# 스레드풀 상태보기
# GET /_cat/thread_pool/write,search?v&h=id,name,active,queue,rejected,completed

# 1. 노드 증설
# 2. 큐 사이즈 증가 (임시방편)