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

title: "[aws] Route53 (11) - Routing Policy - Multi Value"
excerpt: "🚀 Route53, Routing, Policy, Multi Value"

categories: aws
tag: [aws, route, policy, record, multi value]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Routing Policies - Multi Value

> "다중값" 라우팅 정책에 대해 알아보자

![image-20220708031629047](../../assets/images/posts/2022-07-08-AWS Route53 (11) - Routing Policies - Multi value/image-20220708031629047.png)

- 트래픽을 다중 리소스로 라우팅할 때 사용
- Route53 은 다중값과 리소스를 반환한다.
- Health Check와 연결하면 다중 값 정책에서 반환되는 유일한 Resource는 Health Check와 관련이 있다.
- 각각의 MultiValue 쿼리에 최대 8개의 정상 레코드가 반환된다.
  - 클라이언트는 8개의 레코드중 하나를 선택
  - 1개 이상은 정상 레코드가 포함되어있어, 클라이언트는 안전한 쿼리를 가질수 있다

- **ELB 와 유사해 보이지만, ELB를 대체할 수는 없다.**
  - 클라이언트 측면의 로드밸런싱 이다.




- 헬스체크가 비정상인 Record 는 다중값에서 반환되지 않는다 
- www.example.com 으로 요청보내면 3개의 값이 오게된다. (정상인 레코드)





