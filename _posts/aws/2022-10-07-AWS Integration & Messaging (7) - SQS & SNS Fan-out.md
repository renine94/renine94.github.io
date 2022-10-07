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

title: "[aws] Integration & Messaging (7) - SQS & SNS Fan Out"
excerpt: "🚀 SQS, SNS, Fan Out, "

categories: aws
tag: [aws, sns, pub/sub, message]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# SNS + SQS: Fan Out



- 여러 SQS Queue에 Message를 전송하려 할 때 모든 SQS 대기열에 메시지를 개별적으로 보내면 문제가 발생할 수 있다.
  - 예를 들어 앱이 중도에 갑자기 종료되거나, 전송이 실패하거나 또는 나중에 SQS Queue를 추가할 수 있습니다.
- 위와 같은 상황일 때 팬아웃 패턴을 사용하면 SNS Topic에 한 번만 push해도 원하는 만큼의 SNS Topic의 여러 SQS 대기열을 구독할 수 있습니다.
- 이때 Queue대기열은 구독자(Subscriber)가 되며, 그들 모두 SNS에 전송된 메시지를 받게 됩니다.
  - 예를 들어, 구매 서비스에서 2개의 SQS 대기열로 메시지를 보낼 때, 하나의 SNS Topic에 한번만 메시지를 전송하면 SNS Topic의 구독자인 대기열에서 연결된 사기서비스와 운송서비스로 메시지를 전달할 수 있습니다.
- 팬아웃은 완전히 분리된 모델이므로 데이터 손실이 발생하지 않는다.
- SQS를 통해 데이터 지속성, 지연처리 작업 재시도가 가능
- 팬아웃패턴으로 더 많은 SQS대기열을 SNS Topic에 구독시킬 수 있다.
- **이를 위해서는 SQS 대기열 액세스 정책을 통해 SNS Topic이 SQS대기열에 메시지를 전송하도록 허용해야 한다.**

![image-20221007125557772](../../assets/images/posts/2022-10-07-AWS Integration & Messaging (7) - SQS & SNS Fan-out//image-20221007125557772.png)



# S3 Events to multiple queues

> S3 이벤트를 여러 대기열로 보내고 싶을 때

- S3 이벤트 규칙에는 제약조건이 있는데, 같은 이벤트 유형
  - 예를들면, 객체 생성과 같은 이벤트 유형이나 images/ 등 같은 접두어의 조합에서는 하나의 S3 이벤트 규칙만을 적용할 수 있다.
- 여러 SQS 대기열로 동일한 S3 이벤트 알림을 보내기 위해서는 팬아웃 패턴을 사용하면 된다.
- S3 버킷에 이벤트인 S3객체가 있다고 가정하고 이 이벤트를 SNS Topic으로 전송하기 위해, 여러 Queue를 SNS Topic에 구독시키면 된다.
- 앱, 이메일, 람다 함수 등도 SNS Topic에 구독시킬 수 있다.
- 팬아웃 패턴을 사용해서 S3에서 발생한 이벤트를 여러 목적지로 보낼 수 있다.

![image-20221007130205672](../../assets/images/posts/2022-10-07-AWS Integration & Messaging (7) - SQS & SNS Fan-out//image-20221007130205672.png)



# SNS to S3 through Kinesis Data Firehose

> 데이터 전송을 위한 또다른 아키텍처로
>
> Kinesis Data Firehose (KDF) 를 통해 SNS 를 Amazon S3 로 보내는 방식

- SNS 는 KDF와 통합되어 있어 구매 서비스에서 SNS Topic으로 데이터를 전송하면 KDF에서 그 정보를 수신하고,<br>KDF에서는 데이터를 다시 S3버킷으로 전송하거나 KDF에서 지원하는 다른 목적지로 데이터를 전송
- 더 넓은 범위까지 메시지를 지속하고 SNS Topi으로 전송할 수 있게 된다.
- 팬아웃패턴은 FIFO Topic에도 적용가능하다.
- **SNS에는 FIFO, 즉 선입선출 기능이 있어 Topic 내의 메시지에 순서를 지정하여 생산자가 1, 2, 3, 4 순서로 메시지를 전송**
  - **이때 구독은 SQS FIFO Queue만 할 수 있고, 순서대로 1, 2, 3, 4 라는 메시지를 수신하게 된다.**

![image-20221007132533539](../../assets/images/posts/2022-10-07-AWS Integration & Messaging (7) - SQS & SNS Fan-out//image-20221007132533539.png)

