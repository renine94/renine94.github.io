---
layout: single

header:
  teaser: /assets/images/logo/aws.png
  overlay_image: /assets/images/logo/aws.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[aws] Route53 (2) - Route53 & Records"
excerpt: "🚀 Route53, Records Type, Hosted Zones"

categories: aws
tag: [aws, route, records]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Amazon Route53

[지난 포스팅](https://renine94.github.io/aws/AWS-Route53-(1)-Basic/)에서는 DNS 가 무엇인지 알았으니,<br>이번시간에는 Amazon Route53 에 대해 알아보도록 하자.
{: .notice--success}

![image-20220703144312323](../../assets/images/posts/2022-07-02-AWS Route53 (2) - Concept/image-20220703144312323.png)

- 고가용성, 확장성을 갖춘 완전히 관리되며 권한있는 DNS 이다.
  - 여기서 권한이 있다라는 뜻은, 사용자가 DNS records 를 업데이트할 수 있다는 의미이다.
  - 즉, DNS 에 대한 완전히 제어할 수 있다.
- Route53 또한 Domain Registrar 중 하나이다.
- 리소스 관련 상태 확인을 할 수 있다. (헬스체크)
- 100% SLA 가용성을 제공하는 유일한 AWS 서비스이다.
- Route53 이라는 이름의 이유
  - DNS Port 가 전통적으로 53번 포트를 사용하기 때문이다.



## Route53 - Records

- Route53 에서 여러 DNS Records 를 정의하고, 레코드를 통해 특정 Domain으로 라우팅하는 방법을 정의한다.
- 각각의 Records 들은 아래들을 포함한다.
  - **Domain/subDomain Name** - ex) example.com
  - **Record Type** - ex) A or AAAA or CNAME, etc....
  - **Value** - ex) 12.34.56.78
  - **Routing Policy** - Route53이 Query에 응답하는 방식
  - **TTL** - DNS Resolver에서 Records가 Caching 되는 시간을 의미한다.
- Route53 은 아래의 **DNS Records Type** 들을 지원한다.
  - **(필수) A, AAAA, CNAME, NS**
  - (고급) CAA, DS, MX, NARTR, PTR, SOA, TXT, SPF, SRV



## Record Types

> Records 의 종류들을 알아보자.

- A
  - 호스트 이름과 IPv4 를 Mapping 한다.
  - ex) example.com 은 1.2.3.4 로 바로 연결된다.
- AAAA
  - A 와 비슷한 아이디어
  - 호스트 이름과 IPv6 주소를 매핑한다.
- CNAME
  - 호스트 이름과 다른 호스트 이름과 매핑한다.
  - 대상 호스트 이름은 A or AAAA Record 가 될 수도 있다.
  - Route53 에서 DNS 이름 공간 또는 Zone Apex의 상위 노드에 대한 CNAMES를 생성할수 없다.
    - example.com 에 CNAME 을 만들수는 없지만 www.example.com에 대한 CNAME<br>Record는 만들 수 있다.
- NS
  - 호스팅 존의 이름 서버(Name Server)이다.
  - 서버의 DNS 이름 or IP주소로 호스팅 존에 대한 DNS 쿼리에 응답할 수 있다.
  - 트래픽이 도메인으로 라우팅 되는 방식을 제어한다.



## Hosted Zones

> 호스팅 존을 살펴보자

- 호스팅 존은 Record 의 Container 이다.
- Domain 과 subDomain 으로 가는 Traffic 의 Routing 방식을 정의한다.



- 호스팅 존 2가지 종류
  - Public Hosted Zones
    - 퍼블릭 도메인 이름을 살 때마다, mypublicdomain.com이 퍼블릭 도메인 이름이라면,<br>퍼블릭 호스팅 존을 만들 수 있습니다.
    - 퍼블릭 존은 쿼리에 도메인 이름 app1.mypublicdomainname.com의 IP가 무엇인지 알 수 있다.
  - Private Hosted Zones
    - 공개되지 않은 도메인 이름을 지원한다.
    - 가상 프라이빗 클라우드(VPC) 만이 URL을 Resolve 할 수 있다.
    - app1.company.internal 같은 경우
    - 기업에서는 때때로 회사 네트워크 내에서만 접근할 수 있는 URL이 있다.
    - 비공개 URL 이기 때문에 비공개되어 있다. 이면에는 Private DNS Record 가 있다
- AWS에서 만드는 어떤 호스팅존이든 월에 0.5 달러를 지불해야 한다.
  - Route53 사용은 무료가 아니다.
  - 도메인 이름을 등록 및 구입하면 1년에 최소 12$ 를 지불해야 한다. (ex) **renine94.com**



## Public vs Private Hosted Zones

![image-20220703145944285](../../assets/images/posts/2022-07-02-AWS Route53 (2) - Concept/image-20220703145944285.png)

- Public Hosted Zone
  - 공개된 Client 로부터 온 Query에 응답할 수 있다.
  - 웹 브라우저에서 example.com 을 요청하면 IP를 반환한다.
- Private Hosted Zone
  - 해당 VPC 에서만 동작한다.
  - 비공개 도메인 이름의 Private Resource를 식별할 수 있게 한다.
  - ex)
    - EC2 가 1개 있다. webapp.example.internal 을 식별하고자 한다.
    - 또 다른 EC2 에서는 api.example.internal 을 식별하기 원하고
    - DB 에서는 db.example.internal 을 식별하고자 한다.
    - **Private Host Zone에 등록하려고 하는데, 첫 번째 EC2 가 api.example.internal 을 요청하는 경우**
    - private Host Zone은 Private IP 10.0.0.10 이라는 답을 갖고 있다.
    - EC2 는 DB에 연결이 필요할 수도 있는 2번째 EC2 에 연결한다.
    - db.example.internal 이 무엇인지 물어보면 private hosted zone 은 private IP를 알려준다.
    - EC2 인스턴스는 DB에 직접적으로 연결할 수 있다
  - 오직 private resource, 예컨데 VPC 에서만 Query 질의할 수 있다.
- public host zone은 private host zone과 똑같이 동작하지만,<br> public hosted zone은 누구든 우리들의 Record 를 쿼리 할 수 있습니다.



