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

title: "[aws] Route53 (10) - Routing Policy - GeoLocation"
excerpt: "🚀 Route53, Routing, Policy, GeoLocation"

categories: aws
tag: [aws, route, policy, record, geolocation, geo]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Routing Policies - Geolocation

> 지리 위치 라우팅 정책에 대해 알아보자

- Latency-based 정책과 다르다.
- 사용자의 실제 위치를 기반으로 라우팅이 된다.
- 사용자가 특정 대륙이나 국가 혹은 더 정확하게 미국의 경우, 어떤 주에 있는지 지정하는 것이며,<br>가장 정확한 위치가 선택되어 그 IP로 라우팅 된다.
- 일치하는 위치가 없는 경우는 기본(Default) 레코드를 생성해야 한다.
- 사용 사례
  - 콘텐츠 분산을 제한
  - 로드 밸런싱 등을 실행하는 웹사이트 현지화가 있다.
- GeoLocation Record는 Health Check와 연결할 수 있다.



![image-20220707023213959](../../assets/images/posts/2022-07-07-AWS Route53 (10) - Routing Policies - Geolocation/image-20220707023213959.png)



여러 나라가 있는 유럽의 지도를 보면, 독일의 유저가 독일어 버전의 앱을 포함한 IP로 접속되도록<br>독일의 GeoLocation Record 를 정의할 수 있다. 프랑스의 경우라면 프랑스어의 버전의 앱을 가진 IP로 이동해야 한다.

그 외의 다른 곳은 앱에서 영어 버전이 포함된 기본(Default) IP로 이동해야 한다.



## 실습

![image-20220707024700572](../../assets/images/posts/2022-07-07-AWS Route53 (10) - Routing Policies - Geolocation/image-20220707024700572.png)



- 실제 한국에서 접속할 경우 111.222.333.444 로 요청
- 실제 일본에서 접속할 경우 555.666.777.888 로 요청
- 기타 지역에서 접속할 경우 999.111.222.333 로 요청



추후 글로벌 서비스로 확장될 때 해당 기능을 이용하면 좋을 것 같다.