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

title: "[aws] Route53 (5) - Routing Policy - Simple"
excerpt: "🚀 Route53, Routing, Policy, Simple"

categories: aws
tag: [aws, route, policy, simple]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Routing Policies

> Route53 라우팅 정책에 대해 알아보자.



- 라우팅 정책은 Route53 가 DNS 쿼리에 어떻게 응답하는 지를 정의한다.
- **"라우팅" 이라는 단어를 혼동해서는 안된다.**
  - 로드밸런서가 트래픽을 Backend EC2 Instance 로 routing 하는 것과는 다른 상황이다.
  - 여기서의 라우팅은 DNS 관점이다.
  - DNS 는 트래픽을 라우팅하지 않는다. 트래픽은 DNS 를 통과하지 않는다.
  - DNS 는 DNS Query에만 응답하게되고, Client 들은 이를 통해 HTTP 쿼리 등을 어떻게<br>처리해야 하는지를 알 수 있게 된다.
- 실제 사용 가능한 Endpoint로 변환하는 것을 돕는다.



- Route53 이 지원하는 라우팅 정책은 아래와 같습니다.
  - Simple
  - Weighted
  - Failover
  - Latency Based
  - Geolocation
  - Multi-Value Answer
  - Geoproximity (using Route53 Traffic Flow feature)





## Routing Policies - Simple

> 단순 라우팅 정책

![image-20220706005953806](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706005953806.png)

- 일반적으로, traffic 을 단일 resource 로 보내는 방식입니다.
  - ex) 클라이언트가 foo.example.com 으로 가고자 한다면, Route53 이 IP주소를 알려준다.
  - 이는 A 레코드 주소이다.
- 동일한 Record 에 여러 개의 값을 지정하는 것도 가능하다.
  - ex) client 가 foo.example.com로 가기를 요청하면, Route53은 3개의 IP주소를 반환한다.
  - A 레코드에 임베딩된 주소들이다.
  - client가 3개중 1개를 골라서 라우팅에 적용하게 된다.
- Simple Routing 정책에 Alias Record 를 함께 사용하면 하나의 Resource만을 대상으로 지정가능
  - 단순 정책이라고 하는건 간단해서 붙여진 것이다.
- 상태 확인은 할 수 없다.



## 실습

- 레코드 생성을 클릭

![image-20220706010420766](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010420766.png)



- 라우팅정책 - 단순 라우팅
- **값(Value) 에 IP주소를 여러개 설정 할 수 도 있다. (mulitiple value)**

![image-20220706010541411](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010541411.png)



- terminal 에서 dig / nslookup 으로 해당 Record 를 호출하면 IP주소가 1개이상 반환되는것을 확인 가능

![image-20220706010937521](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010937521.png)



![image-20220706011002572](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706011002572.png)



