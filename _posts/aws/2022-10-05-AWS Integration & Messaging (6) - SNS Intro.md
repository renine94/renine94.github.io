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

title: "[aws] Integration & Messaging (6) - SNS Intro"
excerpt: "🚀 Simple Notification Service, Pub/Sub, message"

categories: aws
tag: [aws, sns, pub/sub, message]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Amazon SNS 

- 메시지 하나를 여러 수신자에게 보낸다고 가정
- 이런 경우 직접 통합 (Direct Integration) 쓸 수 있다.
- 구매 서비스 App을 예로 들면 이메일 알림을 보내고 사기탐지 서비스와 배송 서비스 그리고 SQS대기열에도 메시지를 보낼 수 있습니다.
- 하지만 수신 서비스를 새로 추가할 때마다 통합을 생성하고 작성해야 하므로 번거로울 수 있다.
- 대신 Pub/Sub 즉, 게시/구독 이라는 것을 사용할 수 있다.
  - 많은 구독자(subscriber) 가 있으며, 각 구독자는 SNS Topic 에서 해당 message를 수신하고 보관할 수 있다.
  - pub/sub 패턴이라고 한다.

![image-20221005021616018](../../assets/images/posts/2022-10-05-AWS Integration & Messaging (6) - SNS Intro//image-20221005021616018.png)



Pub/Sub

- "이벤트 생산자"는 하나의 SNS Topic 에만 메시지를 보낸다.
- "이벤트 수신자" 또는 구독자는 해당 Topic과 관련한 SNS 알림을 받으려는 사람or서비스 이다.
  - SNS Topic 구독자는 해당 주제로 전송된 메시지를 모두 받게 된다.
  - 메시지를 필터링하는 기능을 사용하는 경우에도 메시지를 받을 수 있다.
- SNS Topic별 최대 구독자 수는 1,200만이상까지 가능하다.
- AWS 계정당 가질 수 있는 Topic 수는 최대 약 10만개 (변동될 수 있으니 대략적임)
- SNS 에서 직접 이메일을 보낼 수도 있고, 모바일 알림을 보낼 수도 있다.
- 지정된 HTTP, HTTPS 엔드 포인트로 직접 데이터를 보낼 수도 있다.
- SQS와 같은 특정 AWS서비스와 통합하여 메시지를 대기열로 직접 보낼수도 있다.
- 메시지를 수신한 후 함수가 코드를 수행하도록 Lambda 에 보내거나 Firehose를 통해 데이터를 S3 나 RedShift 로 보낼수도 있다.

![image-20221007123206551](../../assets/images/posts/2022-10-05-AWS Integration & Messaging (6) - SNS Intro//image-20221007123206551.png)



# SNS Integrates with a lot of AWS Services

> SNS 는 다양한 AWS서비스에서 데이터를 수신하기도 합니다.

- 많은 AWS서비스들은 SNS로 직접 데이터를 보낼 수 있다.
- 아래의 사진과 같이 여러가지 서비스에서 SNS로 메시지를 보낼 수 있다.
- **AWS에서 알림이 발생하면 이러한 서비스가 지정된 SNS Topic으로 알림을 보낸다는것만 기억**하면 된다.

![image-20221007123447173](../../assets/images/posts/2022-10-05-AWS Integration & Messaging (6) - SNS Intro//image-20221007123447173.png)



# SNS - How to publish

> SNS Topic에 데이터를 게시하는 방법을 알아보자

- Topic Publish (using the SDK)
  - 토픽 생성
  - 구독 생성 (하나 또는 여러개)
  - Topic에 publish
- 위와 같이 하게되면 모든 구독자가 자동으로 해당 메시지를 받게 된다.



- Direct Publish (for mobile apps SDK)
  - 모바일 앱 SDK 전용 직접 publish 방법이 있다.
  - 플랫폼 애플리케이션 생성한 뒤,
  - 플랫폼 엔드포인트를 생성하고,
  - 플랫폼 엔드 포인트에 publish 하면 된다.
  - 수신 가능 대상 (구독자)
    - Google
    - GCM
    - Apple APNS
    - Amazon ADM 
- **모두 모바일 애플리케이션으로 알림을 수신하게 된다.**



# SNS - Security

> SNS 보안에 대해 알아보자
>
> 보안측면에서 SNS는 SQS와 동일하다.

- 보안
  - HTTPS API를 사용한 전송중 암호화
  - KMS Keys를 사용한 저장데이터 암호화
  - 클라이언트가 SNS에 암호화된 메시지를 보내려는 경우를 위한 클라이언트 측 암호화
    - 암호화 및 암호 해독은 클라이언트 몫

<br>

- 액세스 제어 (Access Control)
  - IAM 정책 중심
  - 모든 SNS API가 IAM 정책으로 규제된다.

<br>

- SNS 액세스 정책 (S3 버킷 정책과 매우 유사함)
  - SNS Topic에 교차 계정 액세스 권한을 갖거나
  - S3 이벤트와 같은 서비스가 SNS 주제에 작성할 수 있도록 허용하려는 경우 매우 유용





