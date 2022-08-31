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

title: "[aws] Integration & Messaging (1) - Intro"
excerpt: "🚀 Message Introduction"

categories: aws
tag: [aws, integration, message, queue]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# AWS Integration & Messaging

> AWS 에서 제공하는 통합, 메시징 서비스에 대해 알아보자
>
> - 미들웨어로 다른 서비스간 합동 작업을 하는 방법을 학습

- 애플리케이션을 여러 개 배포하려고 할 때 커뮤니케이션을 할 수 밖에 없다.

- 우리들의 서비스는 정보와 데이터를 공유해야 한다.

- 애플리케이션 커뮤니케이션 방법은 2가지 패턴으로 나뉘어진다. (둘다 현업에서 많이 쓰임)

  1. **동기 커뮤니케이션 유형**
     - 애플리케이션이 또 다른 애플리케이션과 직접적으로 연결되는 것
     - ex) 온라인으로 물건을 사고 파는 서비스가 있다고 하면 물건이 판매가 되면 배송 서비스에 연락해서 방금 판매된 물건을 배송해야 한다. 여기 보실 수 있는 것처럼 "구매 서비스" 와 "배송 서비스"는 직접적으로 연결되어 있기 때문에 동기 커뮤니케이션이 발생하고 있다
     - 구매서비스가 배송서비스에게 사건이 발생했으니 배송을 하라고 얘기하는 것
  2. **비동기 혹은 이벤트 기반 유형** 
     - 대기열 등으로 불리는 미들웨어가 애플리케이션들을 연결한다.
     - 구매서비스가 누군가가 어떤물건을 구매했으니 이를 대기열에 포함시키겠다 라고 하고, 그리고 끝이다.
     - 그럼 배송서비스가 대기열에게 최근 구매 내역이 있는지 확인한다. 대기열(Queue)가 해당요소를 반환하면 배송 서비스는 자기가 원하는 것을 무엇이든지 할 수 있다.
     - "구매서비스" 와 "배송서비스"는 직접적으로 연결되어 있지 않다.
     - 그 사이에 대기열(Queue)가 있다. 서로 직접적으로 소통하지 않기 때문에 비동기적이라고 한다.

  ![image-20220901022718053](../../assets/images/posts/2022-09-01-AWS Integration & Messaging (1) - Intro/image-20220901022718053.png)



---

- 애플리케이션 간의 동기화는 때때로 문제가 될 수 있다.

- 구매가 갑자기 너무 증가하거나, 한 서비스가 다른 서비스를 압도하는 경우 큰 문제가 된다.

- 만일 비디오 인코딩 서비스에서 평소에는 10개만 인코딩 해오고 있다가 갑자기 1,000개의 비디오를 인코딩하게 되면 인코딩 서비스가 압도될 것이고 운용이 정지될 것이다.

- 그래서 트래픽이 갑자기 급증하거나 아무것도 예측할 수 없을 때, 일반적으로 애플리케이션을 분리하고 분리 계층을 확장하는 것이 좋다.

  1. 대기열(Queue) 모델에는 SQS를 사용

  2. Pub/Sub 모델의 경우 SNS를 사용

  3. 실시간 스트리밍을하고 대용량 데이터를 다룬다면 Kinesis 사용

- 이 3가지를 활용하여 독립적으로 서비스를 확장할 수 있음을 배운다.





