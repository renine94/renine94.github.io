# 해당 도큐먼트가 어떻게 색인되었는지 확인하기
# GET /{index_name}/_termvectors/{_id}?fields=fields1,fields2,fields3

GET /temp_index_v2/_termvectors/1000016141?fields=name,search_keywords