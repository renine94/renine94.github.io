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

title: "[aws] Integration & Messaging (5) - SQS Dead Letter Queue"
excerpt: "🚀 Simple Queue Service, Dead Letter Queue, DLQ, 배달 못한 편지열"

categories: aws
tag: [aws, sqs, queue, dlq, visibility, timeout]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# SQS - Dead Letter Queue

- 소비자가 "가시성 시간 초과" 내에 메시지를 처리하지 못하는 시나리오를 예로 들어보자
  - 메시지가 자동으로 대기열로 돌아간다.
  - 소비자는 메시지를 읽는다. 오류가 있을수도 있고, 시간이 충분하지 않을수도 있다.
  - 이런 경우 메시지는 대기열로 다싣 ㅗㄹ아간다.
- 위와 같은 일이 자주 일어난다면 문제가 될 수 있다.
- 메시지를 다시 읽게 되어서 메시지에 문제가 있을 수 있다.
- 소비자가 메시지를 이해하지 못하거나, 처리하지 못할 수도 있다.



메시지가 다시 대기열에 들어가고, 이 과정이 반복됩니다.

- SQS 에서 메시지를 다시 읽고 다시 메시지가 대기열로 가는 무한루프를 겪게 된다.
  - 여기서 몇번 이나 반복할지 임계값을 설정할 수 있다.
  - 해당 임계값을 초과하면 SQS에는 메시지에 문제가 있다고 판단하고, DLQ 에 전달 할 수 있다.
  - 많은 처리 시도가 있었지만, 성공하지 못했기 때문에 메시지를 DLQ로 보내는 것이다.
- DLQ 에는 나중에 처리할 수 있게 메시지를 포함하고, 그 메시지는 첫 번째 대기열에서 제거되고 두 번째 대기열로 보내집니다.



**DLQ 목적**

- 디버깅
- 일부 메시지를 처리하지 못하여 DLQ, 즉 데드 레터 대기열로 보낼 수 없으면 애플리케이션을 통해 이 메시지를 분석하거나 다른 이가 이 **메시지를 분석하여 애플리케이션이 멈춘 이유나 메시지를 제대로 처리하지 못한 이유를 파악**하는데 유용
- DLQ 는 14일 정도의 높은 보존 기간을 설정하는 것이 좋다.
  -  SQS가 메시지 보관기간제한이 있기 때문에 일정시점에 만료되기 때문
  - 메시지를 읽고 처리하고 실패로 인해 발생한 일을 파악할 시간이 필요하기 때문

# SQS DLQ - Redrive to Source

> DLQ 관리를 위한 기능

- DLQ 메시지를 사용해 무엇이 잘못되었는지 이해하는 데 도움이 되는 기능
- 메시지가 표시되면 소스대기열에서 메시지가 처리되지 않은것을 알게 된다.
  - 따라서 DLQ에 메시지가 있다는 의미
- 메시지를 수동으로 검사하고, 디버깅합니다.
- 메시지가 처리되지 못한 이유를 파악한 후 소비자 코드를 수정하고 메시지가 올바르게 나오는 경우 DLQ에서 Source Queue로 해당 메시지를 reDrive 합니다.
- 장점
  - 소비자의 경우 메시지가 다른 대기열로 들어갔었고 메시지 처리가 발생했다는 사실조차 모른 채 해당 메시지를 다시 처리할 수 있기 때문이다.



## AWS Console



- Queue 를 두개 생성한다.
  - 1개 - 일반 Queue
  - 1개 - DLQ

![image-20221005003121587](../../assets/images/posts/2022-10-03-AWS Integration & Messaging (5) - SQS Dead Letter Queue//image-20221005003121587.png)



- 일반 Queue의 수정탭에 들어간다.
- 배달 못한 편지 대기열 (Dead Letter Queue)를 활성화 시킨뒤 만들었던 DLQ를 선택한다.
- 최대 수신 수가 3이면, 최대 3번 재시도하고 4번째 메시지 처리가 실패하면 DLQ로 보낸다는 의미

![image-20221005003311630](../../assets/images/posts/2022-10-03-AWS Integration & Messaging (5) - SQS Dead Letter Queue//image-20221005003311630.png)



- 일반 Queue 수정 전체 화면

![image-20221005003354797](../../assets/images/posts/2022-10-03-AWS Integration & Messaging (5) - SQS Dead Letter Queue//image-20221005003354797.png)



이제 첫번째 대기열에 메시지를 전송하고, Polling을 하여 <br>처리를 4번째 재시도할때 DLQ 로 메시지가 전송되는것을 확인할 수 있다.