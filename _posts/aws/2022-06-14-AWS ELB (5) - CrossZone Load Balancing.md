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

title: "[aws] ELB - CrossZone LoadBalancing"
excerpt: "🚀 CrossZone LoadBalancing"

categories: aws
tag: [aws, elb, crossZone]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# ELB - Cross Zone LoadBalancing

교차영역 로드밸런싱
{: .notice--success}

![image-20220614171932226](../../assets/images/posts/2022-06-14-AWS ELB (5) - CrossZone Load Balancing/image-20220614171932226.png)

2개의 가용 영역(AZ) 가 있다. 클라이언트는 두 로드 밸런서에 액세스 하고 있는 상황이다.

- 동일한 로드밸런서, 일반적인 로드 밸런서가 있다.

  - 2개의 EC2 인스턴스가 있는 로드 밸런서

  - 8개의 EC2 인스턴스가 있는 로드 밸런서

교차 영역 로드밸런싱을 사용하면

- 각 로드 밸런서 인스턴스는 전체 가용 영역에 등록된 모든 인스턴스에 전반적으로 고르게 분산된다.
- 그러면 클라이언트는 50%의 트래픽을 첫번째 ALB인스턴스에 보내고, 다른 ALB에 나머지를 보낸다.
- 하지만 각 ALB는 가용영역에 상관없이 10개의 EC2 인스턴스에 전반적으로 트래픽을 리다이렉션 한다.
- 두번째 ALB 인스턴스 보면 전체에 수신한 트래픽의 10% 를 보내는데, **그 이유는 인스턴스가 총 10개이기 때문**
- 그래서 각각 10% 의 트래픽을 얻는 것
- 첫 번째 ALB도 동일하다. 전체 인스턴스의 트래픽의 10% 를 보낸다.
- **트래픽을 전체 EC2 인스턴스에 고르게 분산하게 된다.**



**ALB**

- 교차영역 로드밸런싱이 기본적으로 활성화, 비활성화 할 수 없다.
- 보통 데이터가 한 가용영역에서 다른 가용영역으로 이동하면 비용 지불
- 하지만, 비활성화할 수 없기에 AZ간 데이터 전송에 관한 비용이 없다.

**NLB**

- 교차영역 로드밸런싱이 기본적으로 비활성화
- 사용하려면 비용을 지불해야 한다.
- 가용 영역 간 데이터 전송에 비용을 지불한다.

**CLB**

- 교차영역 로드밸런싱 기본적으로 비활성화
- 활성화하면 가용 영역간 데이터 전송 비용이 발생하지 않는다.



모든 로드 밸런서에서 사용가능하고, ALB 에는 기본값으로 활성화 되어 있다.