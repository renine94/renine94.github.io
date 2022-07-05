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

title: "[aws] Route53 (6) - Routing Policy - Weighted"
excerpt: "🚀 Route53, Routing, Policy, Weighted"

categories: aws
tag: [aws, route, policy, weighted]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Routing Policies - Weighted

> 가중치 기반 라우팅 정책에 대해 알아보자
>
> 아래 그림의 Route53 이미지 오류 무시하세용.

![image-20220706011345980](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706011345980.png)

- 이 정책을 사용하면, 가중치를 활용해 **요청의 일부 비율을 특정 리소스로 보내는 식의 제어가 가능**해진다.
  - 위 그림을 보면, Route53 이 있고, EC2가 3개 실행중일때, 70, 50, 10 으로 가중치를 할당받는다.
  - 가중치의 합이 꼭 100이 될 필요는 없다.
  - Route53에서 오는 DNS 응답의 70% 가 첫 번째 EC2 인스턴스로 리다이렉팅 된다.
  - 20%는 2번째, 10%는 3번 째 인스턴스로 갑니다.
  - 따라가서 각 Record 에 상대적으로 가중치를 할당하게 된다.
- 각 Record로 보내지는 트래픽(traffic)의 양은<br>traffic = Weight for a specific record / sum of all Weights for all records 로 계산 가능하다.
  - traffic = 70 / 100 = 70% 의 트래픽이 첫 번째 EC2 로 가게 된다.
  - 한 DNS 이름 하에 있는 다른 Record들과 비교했을때, 해당 Record로 트래픽을 얼마나 보낼지 나타내는 값
- **DNS Records 들은 모두 같은 이름과 타입(유형)이어야 한다.**
- 상태 확인과도 관련될 수 있다.
- 사용사례
  - 서로 다른 Region들에 걸쳐 로드밸런싱을 할 때나, 적은 양의 트래픽을 보내 새 App을 테스트하는 경우 사용
- 가중치 0 의 값을 보내게 되면 특정 Resource에 트래픽 보내기를 중단해 가중치를 바꿀 수 있다.
- **만약, 모든 resource record의 가중치의 값이 0인 경우에는 모든 Record가 다시 동일한 가중치를 갖게 된다.**



## 실습

![image-20220706013159426](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706013159426.png)





- 가중치 기반 레코드는 레코드의 이름과 타입을 동일한 것을 여러개 만들고 가중치를 다르게 주어야 한다.

![image-20220706013509882](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706013509882.png)