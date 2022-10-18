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

title: "[aws] Integration & Messaging (11) - MQ"
excerpt: "🚀 MQ, 재설계하지않고, 온프레미스 > 클라우드 마이그레이션"

categories: aws
tag: [aws, mq]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"






---

# Amazon MQ

- SQS와 SNS는 클라우드 네이티브 서비스이다.
- AWS 독점 프로토콜을 사용하기 때문에 현재 시장에서 표준은 아니다.
- 전통적 애플리케이션들은 온프레미스에서 작동한다. 개방형 프로토콜을 사용한다.
- 개방형 프로토콜은 MQTT, AMQP, STOM, Openwire, WSS 등이다.
- 이들은 AWS가 생기기전에 개발된 표준 프로토콜에 가깝다. 온프레미스에서 클라우드로 SQS나 SNS를 사용하는 애플레키에시녀으로 마이그레이션 할 때 전부 재설계하는 대신 메시지 대기열을 클라우드로 그냥 옮기고 싶을 수 있다.
- 그러기 위해 Amazon MQ를 사용한다.

<br>

- Amazon MQ는 클라우드에서 Apache ActiveMQ를 관리한다.
- SQS나 SNS만큼 확장되지 않는데, 프로비저닝되기 때문이다.
- 전용 머신에서 실행되고, 장애 조치에 대해 고가용성을 설정할 수도 있다.
- Amazon MQ는 SQS처럼 대기열 기능도 있고, SNS처럼 Topic 기능도 있다.
- **재설계하지 않고, 온프레미스에서 클라우드로 애플리케이션을 마이그레이션할 때, 그 App이 MQTT나 MQP같은 표준 프로토콜을 사용한다면 AmazonMQ 를 사용해야 한다**는 것이다.



## Amazon MQ - 고가용성(High Availability)

> Amazon MQ에서 고가용성이 어떻게 동작하는가?

![image-20221018013440188](../../assets/images/posts/2022-10-19-AWS Integration & Messaging (11) - MQ//image-20221018013440188.png)

- 예시로 Region이 us-east-1 이라고 가정
- AZ 는 두 개로 us-east-1a 와 us-east-1b
- 영역 하나는 활성화(active), 하나는 대기(standby)
- Amazon MQ Broker를 두 영역에 둔다.
- 하나는 활성화 하나는 대기
- 장애 조치를 작동시키기 위해 백엔드 스토리지에 Amazon EFS를 정의한다.
- EFS는 네트워크 파일 시스템으로 다중 가용 영역에 마운트 할 수 있는 서비스이다.

<br>

- 그러면 장애조치가 작동할 때 Amazon EFS에 대기 역시 마운트 되니까
- 첫 번째 활성화 대기열과 같은 데이터를 얻게 되고,
- 장애 조치가 올바르게 작동하게 되는 것이다.
- 클라이언트가 Amazon MQ 브로커와 통신할 때, 장애 조치가 작동하고 있다면 Amazon EFS덕분에 데이터가 안전하게 지켜진다.



