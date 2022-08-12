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

title: "[aws] S3 Advanced (8) - Event Notifications"
excerpt: "🚀 S3 Event Notification, SNS, SQS, Lambda 로 이벤트 전송"

categories: aws
tag: [aws, s3, notification, sns, sqs, lambda, event]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# S3 Event Notifications

> S3 이벤트 알림에 대해 알아보자



- S3 에서는 여러가지 이벤트가 발생한다.
  1. 객체 생성
  2. 객체 삭제
  3. 객체 복원
  4. 객체 복제
- 이러한 이벤트들을 필터링 할 수도 있다.
  - `*.jpg` 로 끝나는 객체를 필터링 할 수도 있다.
- 사용 사례
  - S3 에서 발생하는 특정 이벤트에 자동으로 반응하게 할 수 있다.
  - S3 에 업로드되는 사진의 섬네일을 생성하려고 한다면 이에 대한 이벤트 알림을 만들어서<br> 몇가지 서비스에 보낼 수 있다.
    1. SNS 토픽
    2. SQS
    3. Lambda
- 원하는 만큼 S3 이벤트를 생성하고 원하는 대상(sns, sqs, lambda)로 보낼 수 있다.
  - 이벤트가 전달되는 시간은 일반적으로 초단위 지만 가끔 1분이상 걸릴 수도 있다.
- 이벤트를 보내는 4번째 목적지(서비스) 가 추가되었다.
  - `Amazon EventBridge`



## 1. Event Notifications with Amazon EventBridge

> 이벤트 알림의 새로운 기능으로 Amazon EventBridge와 통합되었다.
>
> 이벤트가 S3 버킷으로 이동하면 이벤트 종류와 상관없이 모든 이벤트는 EventBridge로 모인다.

![image-20220813025526685](../../assets/images/posts/2022-08-13-AWS S3 advanced (8) - Event Notifications/image-20220813025526685.png)

EventBridge 에서는 규칙을 설정할 수 있고, 설정한 규칙을 통해 18개가 넘는 AWS 서비스에 이벤트 알림을 보낼 수 있다. S3 이벤트 알림 기능을 크게 향상시켜 준다. 

- EventBridge 가 있으면 고급 필터링 옵션을 이전보다 훨씬 더 많이 사용할 수 있다.
- 메타데이터, 객체 크기, 이름 등으로 필터할 수 있고 동시에 여러 수신지에 보낼 수도 있다.
  - Step Functions (단계 함수)
  - Kinesis Streams / Firehose
- 이벤트를 보관하거나 재생할 수 있고 보다 안정적으로 전송할 수 있다.



EventBridge 는 비교적 최근에 출시되어 아직 잘 모르는 내용이 많으므로,<br>지금은 S3 Event Notification 에만 집중하도록 하자, 요점은 S3 에서 발생하는 이벤트에 반응할 수 있다는 것이다.

SQS, SNS, Lambda, EventBridge 등으로 알림을 보내는 것이다.





## 2. 실습

![image-20220813030222581](../../assets/images/posts/2022-08-13-AWS S3 advanced (8) - Event Notifications/image-20220813030222581.png)

- Bucket 의 Property (속성) 탭에 들어간다.
- 아래의 이벤트알림 (Event Notifications) 가 있다.
- 2 가지 옵션이 있다.
  1. Event Notification을 생성하는 것
  2. Amazon EventBridge 통합을 활성화 하는 것
     - 이 버킷에서 발생하는 모든 이벤트를 EventBridge 로 보내는 것



![image-20220813030557791](../../assets/images/posts/2022-08-13-AWS S3 advanced (8) - Event Notifications/image-20220813030557791.png)

- 이벤트 이름을 정한다.
- 필터링
  - prefix (접두사) 를 선택적으로 입력할 수 있다.
  - suffix (접미사) 를 선택적으로 입력할 수 있다.



![image-20220813030744524](../../assets/images/posts/2022-08-13-AWS S3 advanced (8) - Event Notifications/image-20220813030744524.png)

- 발생시킬 이벤트의 유형을 선택한다
- 생성/ 삭제/ 복원/ 등등의 여러가지 이벤트 유형을 설정할 수 있다.
- 디테일하게 설정할 수도 있지만, 일단 여기서는 객체가 생성될 때 이벤트를 보내는것으로 설정하였다.



![image-20220813031047184](../../assets/images/posts/2022-08-13-AWS S3 advanced (8) - Event Notifications/image-20220813031047184.png)

- 이벤트 알림을 보낼 대상을 선택한다
  - Lambda
  - SNS Topic
  - SQS Queue
- 그전에 Topic 이나 Queue 가 만들어져 있어야 선택이 가능하다
- SQS 의 Queue를 만들어서 선택을 해도 오류가 발생하는 경우가 있다.
  - Unknown Error : An unexpected error occurred.
    - API Response: Unable to validate the following destination configurations
  - 위와 같은 **에러의 원인은 만들어진 SQS Queue가 S3 Bucket의 메시지를 수락하지 않기 때문**이다.



누구나 SQS Queue에 작성할 수 있는 정책을 설정해줘야 한다.

```json
{
  "id": "Policy23151212312",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt16234141242",
      "Action": [
        "sqs:SendMessage"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:sqs:ap-northest-2:123123123:{QueueName}",
      "Principal": "*"
    }
  ]
}
```

















