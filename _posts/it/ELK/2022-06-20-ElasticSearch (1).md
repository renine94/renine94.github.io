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
> [무신사 데이터 사이언스 엔지니어 블로그](https://danthetech.netlify.app/Backend/basic-tutorial-of-python-package-elasticsearch-dsl/){: .btn .btn--success}

![ES](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/2560px-Elasticsearch_logo.svg.png)

## 01. 개요

**Elasticsearch** (ES) 는 확장성이 뛰어난 **오픈소스 풀텍스트 검색 및 분석 엔진**이다. **방대한 양의 데이터를 신속하게,<br> 거의 실시간으로 저장, 검색, 분석할 수 있도록 지원**합니다. 일반적으로 복잡한 검색 기능 및 요구 사항이 있는<br> 애플리케이션을 위한 기본 엔진/기술로 사용됩니다.

Elasticsearch는 다음을 비롯한 다양한 활용 사례에 효과적입니다.

- 고객이 판매 제품을 검색할 수 있는 커머스 웹을 운영하는경우, Elasticsearch를 사용하여 전체 제품 카탈로그 및 재고 정보를 저장하고 그에 대한 검색 및 자동 완성 제안 기능을 제공할 수 있습니다.
- Log or Transaction 데이터를 수집하고 이 데이터를 분석하고 마이닝하여 추이, 통계, 요약 정보를 얻거나,<br>이상 요인을 알아내려 합니다. 이 경우에는 Logstash (ELK 스택의 일부) 를 사용하여 데이터 수집, 집계, 파싱을 수행한 다음 Logstash에서 ES 에 이 데이터를 피드 형태로 전달<br>데이터가 ES에 적재되면 검색 및 집계를 실행하여 관심 있는 어떤 정보도 마이닝할 수 있습니다.
- 고객이 어떤 셀러의 제품이든 가격이 $?? 아래로 내려가면 알림을 받을 수 있다.<br>고객에게 푸시 방식으로 알릴 수 있다.
- BI 기능이 필요하며 방대한데이터를 대상으로 신속하게 조사, 분석, 시각화, 임시 질의를 수행<br>ES 를 사용하여 데이터저장후 Kibana 를 사용하여 데이터 중 중요한 요소를 시각화한다.



## 02. 기본 개념

- NRT (Near Realtime)
  - ES 는 NRT 검색 플랫폼이다. 즉, 문서를 색인화(index)하는 시점부터 문서가 검색 가능해지는<br>시점까지의 대기시간(대게 1초)이 있습니다.
- 클러스터 (Cluster)
  - 클러스터는 하나 이상의 노드(서버)가 모인 것
  - 전체 데이터를 저장하고, 모든 노드를 포괄하는 통합 색인화 및 검색 기능을 제공
  - 클러스터는 고유한 이름으로 식별되며, 기본값은 elasticsearch 이다.
  - 이름이 중요한 이유는, 어떤 노드가 어느 **클러스터에 포함되기 위해서는 이름에 의해 클러스터 구성원이 되도록 설정**되기 때문이다.
  - 동일한 클러스터 이름을 서로 다른 환경에서 재사용 X
  - 노드가 잘못된 클러스터에 포함될 위험이 있다. 예를들어
  - 개발, 스테이징, 프로덕션 클러스터에 `logging-dev`, `logging-stage`, `logging-prod` 가능
  - 클러스터에 하나의 노드만 있는 것도 가능하며, 또한 각자 고유한 클러스터 이름을 가진 독립적인 클러스 여러 개를 둘 수도 있다.
- 노드 (Node)
  - **노드는 클러스터에 포함된 단일 서버로서 데이터를 저장하고 클러스터의 색인화 및 검색 기능에 참여**
  - 노드는 클러스터처럼 이름으로 식별되며, 기본 이름은 시작 시 노드에 지정된 임의 UUID
  - 기본이름 대신 Custom 노드이름을 정의 가능
  - 이름은 관리목적에서 중요하다. 네트워크의 어떤 서버가 ES 클러스터의 어떤 노드에 해당하는지 식별필요!!
  - 노드는 클러스터 이름을 통해 어떤 클러스터의 일부로 구성될 수 있다.
  - 기본적으로 각 노드는 elasticsearch 라는 이름의 클러스터에 포함되도록 설정된다.
  - 네트워크에서 다수의 노드를 시작할 경우 (각각을 검색할 수 있다고 가정) 이 노드가 모두 자동으로 Elasticsearch 라는 단일 클러스터를 형성하고 이 클러스터의 일부가 됩니다.
  - 하나의 클러스터에서 원하는 개수의 노드를 포함할 수 있다.
  - ES 에 노드가 하나도없을 시, 단일 노드로 시작하면 기본적으로 elasticsearch 라는 이름의 단일노드 클러스터가 만들어진다.
- 인덱스 (Index)
  - 색인은 다소 비슷한 특성을 가진 문서의 모음
  - 고객 데이터에 대한 색인, 제품 카탈로그에 대한 색인, 주문 데이터에 대한 색인 등등..
  - 색인은 모두 소문자이름으로 식별되며, 이 이름은 색인에 포함된 문서에 대한 색인화, 검색, 업데이트, 삭제 작업에서 해당 색인을 가리키는 데 쓰인다.
  - 단일 클러스터에서 원하는 개수의 색인을 정의할 수 있다.
  - **RDB로 비유하면 Table과 비슷한 느낌?**
- 타입 (Type)
  - 하나의 색인에서 하나 이상의 유형을 정의할 수 있다.
  - Type(유형) 이란, Index(색인)을 논리적으로 분류/구분한 것, 그 의미 체계는 사용자가 결정
  - 일반적으로 여러 공통된 필드를 갖는 문서에 대해 유형이 정의된다.
  - **예를 들어, 블로그 플랫폼을 운영하고 있는데 모든 데이터를 하나의 Index(색인)에 저장하게 된다면,<br>이 Index 에서 사용자 데이터, 블로그 데이터, 댓글 데이터에 대한 유형(Type)을 각각 정의할 수 있다.**
- 도큐먼트 (Document)
  - 도큐먼트(문서)는 Index화할 수 있는 기본 정보 단위
  - 단일 고객, 단일 제품, 단일 주문에 대한 문서가 각각 존재할 수 있다.
  - **이 문서는 Json형식이다.**
  - **하나의 Index/Type 에 원하는 개수의 Document를 저장할 수 있다.**
  - 도큐먼트가 물리적으로는 어떤 Index내에 있더라도 도큐먼트는 Index화되어 색인에 포함된 어떤 유형으로 지정되어야 한다
- 샤드/레플리카 (Shard/Replica)
  - index는 방대한 양의 데이터를 저장할 수 있다.
  - 이 데이터가 단일 노드의 하드웨어 한도를 초과할 수도 있다.
    - 10억 개의 도큐먼트로 구성된 하나의 색인에 1TB 디스크 공간이 필요한 경우
    - 단일 노드의 디스크에서 수용하지 못하거나, 단일 노드에서 검색 요청 처리 시 속도가 너무 느려질수있다.
  - **ES 는 이러한 문제를 해결하고자 Index 를 Shard 샤드라는 조각으로 분할하는 기능을 제공**한다.
  - Index를 생성시, 원하는 샤드 수를 설정 가능
  - **각 샤드는 그 자체가 온전한 기능을 가진 독립적인 Index이며, 클러스터의 어떤 노드에서도 호스팅할수있다.**
  - 샤딩이 중요한 2가지 이유
    - 콘텐츠 볼륨의 수평 분할/확장이 가능해진다.
    - 작업을 (여러 노드에 위치한) 여러 샤드에 분산 배치하고 병렬화함으로써 성능/처리량 늘릴 수 있다.
  - 샤드가 분산 배치되는 방식 및 그 문서가 다시 검색 요청으로 집계되는 방식의 메커니즘은 모두 ES에서<br>관리하며 사용자에게는 투명하게 이루어진다.
  - 언제든 오류가 일어날 수 있는 네트워크/클라우드 환경에서는 어떤 이유에서든 샤드/노드가 오프라인 상태가 되거나 사라지게 될 경우에 대비하여 FailOver 메커니즘을 마련하는 것이 유익하고 바람직하다.
  - 이러한 취지에서 ES에서는 Index의 Shard에 대해 1개 이상의 복사본을 생성할 수 있는데, 이를 Replica Shard 줄여서 리플리카라고 한다.
  - 리플리카를 만드는 복제가 중요한 2가지 이유
    - 샤드/노드 오류가 발생하더라도 고가용성을 제공한다. 따라서 리플리카 샤드는 그 원본인 기본 샤드와 동일한 노드에 배정되지 않는다.
    - 모든 리플리카에서 병렬 방식으로 검색을 실행할 수 있으므로 검색 볼륨/처리량을 확장 할 수 있다.
  - 요약
    - 각 Index 는 N개의 Shard 로 분할할 수 있다.
    - 하나의 Index는 복제하지 않거나(리플리카 없음) 1회 이상 복제할 수 있다.
    - 복제되면 각 Index는 기본 샤드(복제원본 샤드)와 리플리카 샤드(기본 샤드의 복제본)를 갖습니다.
    - Shard 및 Replica의 수는 Index별로, Index 생성 시점에 정의 가능하다.
    - **Index 생성 이후 탄력적으로 Replica의 수를 변경할 수 있으나, Shard 수는 변경 불가능하다.**
  - 기본적으로 ES 의 각 Index는 기본 Shard 5개, Replica 1개를 갖습니다.
  - 따라서 클러스터에 최소한 2개의 노드가 있다면 Index는 기본Shard 5개 Replica Shard 5개 (완전한 리플리카 1개) 를 가지므로 Index 당 총 10개의 Shard 가 존재하게 된다.



## 03. 참고 이미지

>  ELK = elasticsearch + logstash + kibana

![ELK Flow](https://t1.daumcdn.net/cfile/tistory/993B7E495C98CAA706)



![ES Structure](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/images%2Fjjongbumeee%2Fpost%2F12049edd-7849-4f51-9f62-4f35e5bbe83c%2Fimage.png)



![chart](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/99A97A355C98D42D2E.png)



![chart2](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/1*Polksm7wIAGlCG-d9ZR7aA.png)



![chart3](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/1*_OzAe3SEwnZ6qfc-4urQ1Q.png)



![chart4](../../../assets/images/posts/2022-06-20-ElasticSearch (1)/998444375C98CC021F.jpeg)
