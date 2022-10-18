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

title: "[aws] Integration & Messaging (10) - SQS & SNS & Kinesis 비교"
excerpt: "🚀 SQS, SNS, Kinesis 에 차이점을 알아보자!"

categories: aws
tag: [aws, sqs, sns, kinesis]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# SQS vs SNS vs Kinesis

![image-20221018011611803](../../assets/images/posts/2022-10-18-AWS Integration & Messaging (10) - SQS & SNS & Kinesis//image-20221018011611803.png)



**SQS**

- 소비자가 SQS 대기열에서 메시지를 요청해서 데이터를 가져오는(pull) 모델이다.
- 데이터를 처리한 후 소비자가 대기열에서 삭제해서 다른 소비자가 읽을 수 없도록 한다.
- 작업자나, 소비자 수는 제한이 없다.
  - 작업자와 소비자가 함께 소비하고 대기열에서 삭제하기 때문
- AWS에서 관리되는 서비스이므로 처리량을 프로비저닝할 필요가 없고, 빠르게 수백 수천 개 메시지로 확장가능
- 순서를 보장하려면 FIFO 대기열 즉, 선입선출 대기열을 활성화해야 한다.
- 각 메시지에는 지연 기능이 있어 30초 등 일정 시간 뒤에 대기열에 나타나도록 할 수 있다.



**SNS**

- **pub/sub 모델이다.** (Kafka 마찬가지)
- 다수의 구독자에게 데이터를 push하면 메시지의 복사본을 받게 된다.
- SNS Topic별로 1,250만 명의 구독자까지 가능하며 데이터가 한 번 SNS에 전송되면 지속되지 않는다.
- 즉, 제대로 전달되지 않는다면 데이터를 잃을 가능성이 있다.
- pub/sub 모델은 최대 10만 개의 Topic으로 확장 가능하다.
- 역시 처리량을 프로비저닝하지 않아도 되고, 원한다면 SQS와 결합할 수 있다.
- 팬아웃 아키텍쳐 패턴을 이용하면 SNS와 SQS를 결합하거나, SNS FIFO Topic을 SQS FIFO와 결합할수 있다.



**Kinesis**

- 두 가지 소비 모드가 있다.
- **소비자가 Kinesis로부터 데이터를 가져오는(pull) 표준모드**는 샤드당 2MB/s 를 지원
- 반면 **향상된 팬아웃 유형 소비의 메커니즘**에서는 Kinesis가 소비자에게 데이터를 push하며 샤드 하나에 소비자당 2MB/s 의 속도가 나옵니다.
  - 처리량이 훨씬 높을테니 Kinesis Data Stream에서 더 많은 애플리케이션 읽기가 가능하다.
- Kinesis 데이터 스트림에서는 데이터가 지속되기 때문에 데이터를 다시 재생할 수 있다.
- 따라서 실시간 빅데이터 분석, ETL 등에 활용된다.
- 샤드 레벨에서 정할 수 있어 미리 Kinesis 데이터 스트림마다 원하는 샤드 양을 지정해야 한다.
- 샤드를 직접 확장해서 데이터가 언제 만료될지 정한다.
- 1일에서 365일까지 데이터를 보존할 수 있다.
- 용량 모드에는 2가지가 있다.
  - 프로비저닝 용량모드
    - Kinesis 데이터 스트림으로부터 원하는 샤드 양을 미리 지정
  - 온디맨드 용량 모드
    - 샤드 수가 Kinesis데이터 스트림에 따라 자동으로 조정



