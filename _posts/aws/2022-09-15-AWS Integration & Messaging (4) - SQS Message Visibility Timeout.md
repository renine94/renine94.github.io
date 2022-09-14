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

title: "[aws] Integration & Messaging (4) - SQS Message Visibility Timeout"
excerpt: "🚀 Simple Queue Service, Message Visibility Timeout"

categories: aws
tag: [aws, sqs, queue, visibility, timeout]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Message Visibility Timeout

> 메시지 가시성 초과

![image-20220915003819642](../../assets/images/posts/2022-09-15-AWS Integration & Messaging (4) - SQS Message Visibility Timeout/image-20220915003819642.png)

- **소비자가 메시지를 폴링하면 그 메시지는 다른 소비자들에게 보이지 않게 됩니다.**
- 기본적으로, "메시지 가시성 초과" 는 30초이다.
  - 즉, 메시지를 Consume하면, 그 메시지는 30초동안 다른 소비자(Worker)에게 보이지 않게 된다.
- 그 말인 즉슨, 이 30초 동안 메시지가 처리되어야 한다.
  - 동일한 or 다른 소비자가 메시지 요청 API를 호출하면 메시지가 반환되지 않습니다.
  - 시간 초과 기간 내에 또 다른 요청이 들어와도 메시지가 반환되지 않는다.
- **가시성 시간 초과가 경과되고 메시지가 삭제되지 않았다면 메시지는 대기열에 다시 넣습니다.**
  - 30초 동안 작업이 완료되지 않으면, 다시 SQS에 넣는다.
  - 그러면, 다른 / 동일한 소비자가 또 ReceiveMessage API를 호출하면 이전의 그 메시지를 또 받게 된다.
- 메시지를 빧는 동안 가시성 시간 초과 기간 동안 보이지 않게 된다.



- 가시성 시간 초과 기간 내에 메시지를 처리하지 않으면 메시지가 두 번 처리될수도 있다.
- 두 명의 다른 소비자가 수신하거나, 동일한 소비자가 두 번 수신하기 때문이다.
- 소비자가 메시지를 적극적으로 처리하고 있지만, **30초안에 처리할 수 없어 시간이 더 필요하다면 `ChangeMessageVisibility` 라는 API 를 호출하여 SQS에 알려야 한다.**



- Message Visibility TImeout 을 매우 높게 설정하면 (hour), 
  - 소비자가 메시지 처리도중에 에러가 발생하면,  이 메시지가 다시 나타날 때까지 즉, SQS 대기열에 보이기까지 몇 시간이 걸립니다.
- 반대로 시간을 매우 낮게 설정하면 (second),
  - 소비자가 어떤 이유로든 해당 메시지를 처리할 시간이 충분하지 않으므로 다른 소비자가 메시지를 여러 번 읽을 것이며 중복 처리될 수도 있습니다.
- 즉, 우리의 App 상황에 맞게끔 적절한 시간으로 설정하는 것이 중요하다.
  - 처리도중에 시간이 부족하다면 ChangeMessageVisibility API를 호출하도록 프로그래밍해야 한다.





---



AWS

![image-20220915005246649](../../assets/images/posts/2022-09-15-AWS Integration & Messaging (4) - SQS Message Visibility Timeout/image-20220915005246649.png)



SQS 를 생성하거나, 편집할 때, Message Visibility Timeout (메시지 가시성 초과) 는, "표시 제한 시간" 이라고 번역되어 있는 모습을 볼 수 있다. 기본값 30초로 설정되어있으니, 상황에 맞게 적절하게 수정하면 됩니다.



Message Visibility Timeout == 메시지 가시성 초과 == 표시 제한 시간

같은 뜻인듯..



