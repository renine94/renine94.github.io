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

title: "[aws] Route53 (12) - Domain Registar & DNS Service"
excerpt: "🚀 Route53, Routing, Domain Registar, DNS Service"

categories: aws
tag: [aws, route, domain, registar, dns, service]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Domain Registar vs  DNS Service

> 도메인 레지스트라와 DNS서비스를 구별해보자

![image-20220708033539748](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708033539748.png)

- 도메인 Registar 를 통해 원하는 이름의 도메인을 구매할 수 있다. (ex. www.renine94.com)
  - 매년 비용을 지불한다. (1년에 약 12달러)
  - Route53 외의 다른 도메인 Registar를 이용해도 된다. (Godday, Whois, Gabia, etc,,,,) 무료도메인 등등
- 레지스트라를 통해 도메인을 등록하면 DNS records 관리를 위한 DNS 서비스를 제공한다.
- 우리의 DNS records를 관리하기위해서 다른 DNS 서비스를 사용할 수 있다.
- 사용 예시
  - GoDaddy 에서 도메인을 구입하고, Route53 을 이용하여 DNS records를 관리하는 경우



## GoDaddy as Registrar & Route53 as DNS Service

> 고대디를 registrar 로 이용하고,<br>Route53 을 DNS Service로 이용해보자
>
> - Route53 에서 도메인구입하고 DNS Service로도 사용가능 (Route53에서 동시에 둘다 가능)

![image-20220708033739372](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708033739372.png)



- GoDaddy 에서 도메인을 구입하면 NameServer 옵션이 4개 생성된다.
- 사용자 정의 NS를 지정할 수 있다.
- 방법
  - Route53 에서 원하는 Domain의 Public Hosted Zone을 생성한다. (공용 호스팅 영역)
  - 호스팅 영역 상세의 오른쪽 부분에서 NS 를 찾는다.
  - 여기 있는 4개의 NS 를 GoDaddy 웹사이트에서 변경해야 한다.
- 이제 GoDaddy에서 사용할 이름 서버에 관한 쿼리에 응답하면 NS 가 Route53 NS 서버를 가리킨다.
- Route53 을 사용해서 해당 콘솔에서 직접 전체 DNS Records를 관리할 수 있게 된다.



## 3rd Party Registrar with Amazon Route53

![image-20220708034436865](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708034436865.png)

- 정리
  - 도메인을 타사 등록대행사에서 구매해도 된다.
  - DNS서비스 제공자로 Route53을 사용가능하다.
  - Route53에서 공용 호스팅 영역 생성
  - 도메인을 구입한(GoDaddy)의 웹사이트에서 NS 를 업데이트하면 Route53 NS를 가리키게 된다.





