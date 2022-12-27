---
layout: single

header:
  teaser: /assets/images/logo/elasticSearch.png
  overlay_image: /assets/images/logo/elasticSearch.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[ES] CRUD, 입력, 조회, 수정, 삭제 문법에 대해 알아보자"
excerpt: "🚀 ES 에서 사용하는 CRUD 문법에 대해 학습한다."

categories: elasticSearch
tag: [es, elasticSearch, crud, bulk]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# ES CRUD

> ES 에서는 단일 Document 별로 고유한 URL 을 갖는다.



- ES 6.x 이전
  - `http://<호스트>:<포트>/<인덱스>/<도큐먼트 타입>/<도튜먼트 id>`
- ES 7.0 이후
  - `http://<호스트>:<포트>/<인덱스>/_doc/<도큐먼트 id>`



ES 7.0 이후 버전부터는 도큐먼트 타입 개념이 사라지고, `_doc` 으로 접근해야 합니다.

```sh
# my_index/_doc/1 에 도큐먼트 입력
$ curl -XPUT "http://localhost:9200/my_index/_doc/1" -H 'Content-Type: application/json' -d'
{
  "name": "Jongmin Kim",
  "message": "안녕하세요 Elasticsearch"
}'
{"_index":"my_index","_type":"_doc","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```





## 01. Create

> 데이터를 입력할 때는 **PUT** 메서드를 사용합니다.



```json
// my_index/_doc/1 최초 입력

PUT my_index/_doc/1
{
  "name": "Jaegu Kang",
  "message": "Hello world!"
}
```



처음 데이터를 입력하게되면 `created` 이고, 이후 같은 도큐먼트 ID 로 다시 입력하게되면,<br>기존 도큐먼트는 삭제되고 새로운 도큐먼트로 덮어씌워지게 됩니다.<br>이 때는 결과가 `created` 가 아닌 `updated` 로 표시됩니다.



### _bulk

> 데이터를 대량으로 CRUD 해야 하는 경우 사용합니다.
>
> delete 를 제외하고는, 명령문과 데이터문을 한 줄씩 순서대로 입력해야 합니다.
>
> Delete 는 내용 입력이 필요 없기 때문에 명령문만 있습니다.

```json
// _bulk 명령 실행

POST <index이름>/_bulk
{"index":{"_index":"test", "_id":"1"}}
{"field":"value one"}
{"index":{"_index":"test", "_id":"2"}}
{"field":"value two"}
{"delete":{"_index":"test", "_id":"2"}} // 명령문만 있음
{"create":{"_index":"test", "_id":"3"}}
{"field":"value three"}
{"update":{"_index":"test", "_id":"1"}}
{"doc":{"field":"value two"}}
```



- 파일내용 읽어서 bulk API 사용

```json
// bulk.json

{"index":{"_index":"test","_id":"1"}}
{"field":"value one"}
{"index":{"_index":"test","_id":"2"}}
{"field":"value two"}
{"delete":{"_index":"test","_id":"2"}}
{"create":{"_index":"test","_id":"3"}}
{"field":"value three"}
{"update":{"_index":"test","_id":"1"}}
{"doc":{"field":"value two"}}

// bulk_json 파일 내용을 _bulk 로 실행

$ curl -XPOST "http://localhost:9200/_bulk" -H 'Content-Type: application/json' --data-binary @bulk.json

```









<br>

---



## 02. Read

> GET 메서드로 가져올 도큐먼트의 URL 입력하면 도큐먼트 내용을 가져오게 됩니다.



```json
// 인덱스 Document 전체 조회 (전체 조회)

GET my_index/_search


// 인덱스 개별 Document 조회 (단일 조회)

GET my_index/_doc/<도큐먼트_id>

// 다양한 검색 쿼리 방법들 (제일 중요!!!)

GET my_index/_search
{
  "query": {
    "match": {
      "name": "검색할 단어"
    }
  }
}
```



<br>

---

## 03. Delete

> DELETE 메서드를 이용해서 `Document or Index` 단위의 삭제가 가능합니다.



- 인덱스 삭제

```json
// my_index 인덱스 삭제

DELETE my_index
```





- 도큐먼트 삭제

```json
// my_index/_doc/1 도큐먼트 삭제

DELETE my_index/_doc/1
```





<br>

---

## 04. Update (수정)

> POST 메서드는 PUT 메서드와 유사하게 데이터 입력에 사용이 가능하다



도큐먼트를 입력할 때 POST 메서드로 `<인덱스>/_doc` 까지만 입력하게 되면 자동으로 임의의 도큐먼트id 가 생성됩니다. 도큐먼트id 자동생성은 PUT 메서드로는 동작하지 않습니다.



```json
// POST 명령으로 my_index/_doc 도큐먼트 입력

POST my_index/_doc
{
  "name": "jaegu kang",
  "message": "hello world!"
}
```



위 결과에서 도큐먼트 id 는 자동으로 생성된것을 확인할 수 있다.



- _update
  - 도큐먼트 수정은 기존 도큐먼트 URL 에 변경될 내용의 도큐먼트 내용을 다시 PUT 하는것으로 대치 가능
  - 필드가 여럿 있는 도큐먼트에서 필드 하나만 바꾸기 위해 전체 내용을 매번 다시 입력하는것은 번거로움
  - 이 때 `POST <인덱스>/_update/<도큐먼트 id>` 명령을 이용해 원하는 필드의 내용만 업데이트 가능
  - 업데이트 할 내용에 "doc" 이라는 지정자 사용

```json
// my_index/_update/1 도큐먼트의 message 필드 업데이트

POST my_index/_update/1
{
  "doc": {
    "message": "이것은 수정된 메시지 내용입니다."
  }
}
```





































