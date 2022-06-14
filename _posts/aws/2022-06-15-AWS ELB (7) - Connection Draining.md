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

title: "[aws] ELB - Connection Draining"
excerpt: "🚀 ELB, Connection Draining"

categories: aws
tag: [aws, elb, connection draining]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Connection Draining

인스턴스가 등록 취소, 또는 비정상인 상태에 있을 때 인스턴스에 어느 정도의 시간을 주어 In-Flight 요청<br>즉, 활성 요청을 완료할 수 있도록 하는 기능이다.
{: .notice--success}

![image-20220615021142411](../../assets/images/posts/2022-06-15-AWS ELB (7) - Connection Draining/image-20220615021142411.png)

- CLB 를 사용하는 경우 `연결 드레이닝` 이라 부른다.
- ALB, NLB 를 사용하는 경우에는 `등록 취소 지연` 이라고 부른다.



- **연결 드레이닝되면 즉, 인스턴스가 드레이닝되면 ELB는 등록 취소 중인 EC2 인스턴스로<br>새로운 요청을 보내지 않게 된다.**
- 인스턴스가 3개중 1개를 드레이닝 모드로 설정한다.
- EC2 인스턴스에 이미 연결된 유저는 충분한 드레이닝 시간을 얻게될것이다.
- 기존 연결 및 기존 요청을 완료할 수 있을 거다.
- 그리고 작업이 끝나면 모든 연결이 정지된다.
- 새로운 유저가 ELB에 연결하려고 하면 ELB는 기존의 EC2 인스턴스가 드레이닝 상태에 있으므로<br>새로운 연결은 다른 EC2 인스턴스와 수립될 거라는 점을 알고있으므로 새로운 연결은<br>두번째나 세번째 EC2 인스턴스를 사용하게 된다.
- 기본값은 300초(5분) 이며, 0 으로 설정시 드레이닝 기능이 비활성화 된다.



