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

title: "[aws] Route53 (7) - Routing Policy - Latency Based"
excerpt: "🚀 Route53, Routing, Policy, Latency Based"

categories: aws
tag: [aws, route, policy, latency]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# Routing Policies - Latency-based

> 지연 시간 기반 라우팅 정책을 알아보자.

![image-20220706014424327](../../assets/images/posts/2022-07-06-AWS Route53 (7) - Routing Policies - Latency Based/image-20220706014424327.png)

- 지연 시간이 가장 짧은, 즉 가장 가까운 리소스로 리다이렉팅 하는 정책
- 지연시간에 민감한 웹사이트나 App이 있을 경우 유용한 정책
- **지연시간은 유저가 레코드로 가장 가까이 식별된 AWS Region에 연결하기까지 걸리는 시간을 기반으로 측정**
- 독일유저들이 미국에 있는 resource의 지연시간이 가장 짧다면,<br>해당 유저들은 미국 리전으로 리다이렉팅 될 것
- 상태 확인과 연결이 가능하다.



- 두 개의 Region에 App을 배포한다고 가정
- ap-southeast-1 과 us-east-1
- 유저들은 세계 각지에 있으며, Route53이 지연시간을 측정
- 지연시간이 가장 짧은 가까운 거리의 유저들이 us-east-1 의 ALB로 연결되고<br>다른 유저들은 ap-southeast-1 으로 연결된다.



## 실습



![image-20220706015004602](../../assets/images/posts/2022-07-06-AWS Route53 (7) - Routing Policies - Latency Based/image-20220706015004602.png)



- VPN 을 켜서 다른 국가로 IP를 변경한 후, 테스트하면 가장 지연시간이 짧은 리전에서의 응답을 받을 수 있게 된다.



