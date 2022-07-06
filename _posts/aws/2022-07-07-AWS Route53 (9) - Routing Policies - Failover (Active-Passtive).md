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

title: "[aws] Route53 (9) - Routing Policy - Failover (Active-Passive)"
excerpt: "🚀 Route53, Routing, Policy, Failover"

categories: aws
tag: [aws, route, policy, failover]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Routing Policies - Failover (Active-Passive)

> 장애 조치에 관한 라우팅 정책

![image-20220707003611914](../../assets/images/posts/2022-07-07-AWS Route53 (9) - Routing Policies - Failover (Active-Passtive)/image-20220707003611914.png)

- Route53 과 2개의 EC2 인스턴스가 있고, 그중 하나는 재해 복구 EC2 이다.
- 상태 확인과 기본 레코드로 연결하는데, 이는 필수적이다.
- 상태 확인(health check)가 비정상이면 자동으로 Route53은 2번째의 EC2 인스턴스로 장애조치
- 보조 EC2 인스턴스도 Health Check를 연결할수 있지만 기본과 보조 각각 하나씩만 있을 수 있다.
- Client 의 DNS 요청은 정상으로 생각되는 리소스를 자동으로 얻는다.
- 기본 인스턴스가 정상이면 Route53 도 기본 레코드로 응답한다.
- 하지만 health check가 비정상이면 장애 조치에 도움이 되는 두번째 레코드의 응답을 자동으로 얻는다.



---

- 같은 도메인으로 두개 연결시키고, 상태 확인 ID 도 넣어줘야하는데 안만들어서 선택불가능한 상태



![image-20220707010706541](../../assets/images/posts/2022-07-07-AWS Route53 (9) - Routing Policies - Failover (Active-Passtive)/image-20220707010706541.png)