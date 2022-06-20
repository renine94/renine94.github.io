---
layout: single

header:
  teaser: /assets/images/logo/it.jpeg
  overlay_image: /assets/images/logo/it.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[it] ElasticSearch (1) - Basic"
excerpt: "🚀 ES, ELK, OpenSearch, ElasticSearch, Basic"

categories: it
tag: [it, es, elasticsearch, elk, search]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# ElasticSearch

> 검색에 최적화된 오픈소스
>
> [공식문서](https://www.elastic.co/guide/kr/elasticsearch/reference/current/getting-started.html) 를 참고하여 해당 내용을 포스팅합니다.

![ES](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/2560px-Elasticsearch_logo.svg.png)

## 01. 개요

**Elasticsearch** (ES) 는 확장성이 뛰어난 **오픈소스 풀텍스트 검색 및 분석 엔진**이다. 방대한 양의 데이터를 신속하게,<br> 거의 실시간으로 저장, 검색, 분석할 수 있도록 지원합니다. 일반적으로 복잡한 검색 기능 및 요구 사항이 있는<br> 애플리케이션을 위한 기본 엔진/기술로 사용됩니다.

Elasticsearch는 다음을 비롯한 다양한 활용 사례에 효과적입니다.

- 고객이 판매 제품을 검색할 수 있는 커머스 웹을 운영하는경우, Elasticsearch를 사용하여 전체 제품 카탈로그 및 재고 정보를 저장하고 그에 대한 검색 및 자동 완성 제안 기능을 제공할 수 있습니다.
- Log or Transaction 데이터를 수집하고 이 데이터를 분석하고 마이닝하여 추이, 통계, 요약 정보를 얻거나,<br>이상 요인을 알아내려 합니다. 이 경우에는 Logstash (ELK 스택의 일부) 를 사용하여 데이터 수집, 집계, 파싱을 수행한 다음 Logstash에서 ES 에 이 데이터를 피드 형태로 전달<br>데이터가 ES에 적재되면 검색 및 집계를 실행하여 관심 있는 어떤 정보도 마이닝할 수 있습니다.
- 고객이 어떤 셀러의 제품이든 가격이 $?? 아래로 내려가면 알림을 받을 수 있다.<br>고객에게 푸시 방식으로 알릴 수 있다.
- BI 기능이 필요하며 방대한데이터를 대상으로 신속하게 조사, 분석, 시각화, 임시 질의를 수행<br>ES 를 사용하여 데이터저장후 Kibana 를 사용하여 데이터 중 중요한 요소를 시각화한다.



## 02. 기본 개념

- NRT (Near Realtime)
  - ES 는 NRT 검색 플랫폼이다. 즉, 문서를 색인화(index)하는 시점부터 문서가 검색 가능해지는 시점까지의 대기시간(대게 1초)이 있습니다.
- 클러스터
  - 클러스터는 하나 이상의 노드(서버)가 모인 것
  - 전체 데이터를 저장하고, 모든 노드를 포괄하는 통합 색인화 및 검색 기능을 제공
  - 클러스터는 고유한 이름으로 식별되며, 기본값은 elasticsearch 이다.
  - 이름이 중요한 이유는, 어떤 노드가 어느 **클러스터에 포함되기 위해서는 이름에 의해 클러스터 구성원이 되도록 설정**되기 때문이다.
  - 동일한 클러스터 이름을 서로 다른 환경에서 재사용 X
  - 노드가 잘못된 클러스터에 포함될 위험이 있다. 예를들어
  - 개발, 스테이징, 프로덕션 클러스터에 `logging-dev`, `logging-stage`, `logging-prod` 가능
  - 클러스터에 하나의 노드만 있는 것도 가능하며, 또한 각자 고유한 클러스터 이름을 가진 독립적인 클러스 여러 개를 둘 수도 있다.
- 노드
  - **노드는 클러스터에 포함된 단일 서버로서 데이터를 저장하고 클러스터의 색인화 및 검색 기능에 참여**
  - 노드는 클러스터처럼 이름으로 식별되며, 기본 이름은 시작 시 노드에 지정된 임의 UUID
  - 기본이름 대신 Custom 노드이름을 정의 가능
  - 이름은 관리목적에서 중요하다. 네트워크의 어떤 서버가 ES 클러스터의 어떤 노드에 해당하는지 식별필요!!
  - 노드는 클러스터 이름을 통해 어떤 클러스터의 일부로 구성될 수 있다.
  - 기본적으로 각 노드는 elasticsearch 라는 이름의 클러스터에 포함되도록 설정된다.
  - 네트워크에서 다수의 노드를 시작할 경우 (각각을 검색할 수 있다고 가정) 이 노드가 모두 자동으로 Elasticsearch 라는 단일 클러스터를 형성하고 이 클러스터의 일부가 됩니다.
  - 하나의 클러스터에서 원하는 개수의 노드를 포함할 수 있다.
  - ES 에 노드가 하나도없을 시, 단일 노드로 시작하면 기본적으로 elasticsearch 라는 이름의 단일노드 클러스터가 만들어진다.
- 인덱스
  - 색인은 다소 비슷한 특성을 가진 문서의 모음
  - 고객 데이터에 대한 색인, 제품 카탈로그에 대한 색인, 주문 데이터에 대한 색인 등등..
  - 색인은 모두 소문자이름으로 식별되며, 이 이름은 색인에 포함된 문서에 대한 색인화, 검색, 업데이트, 삭제 작업에서 해당 색인을 가리키는 데 쓰인다.
  - 단일 클러스터에서 원하는 개수의 색인을 정의할 수 있다.
  - RDB로 비유하면 Table과 비슷한 느낌?
- 타입
- 
