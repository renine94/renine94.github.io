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

title: "[aws] Integration & Messaging (2) - SQS Queue Access Policy"
excerpt: "🚀 Simple Queue Service, Access Policy"

categories: aws
tag: [aws, sqs, queue, access-policy]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# SQS Queue Access Policy

![image-20220907012457381](../../assets/images/posts/2022-09-07-AWS Integration & Messaging (3) - SQS Access Policy/image-20220907012457381.png)



SQS 대기열 액세스 정책에 대한 좋은 사용사례가 두 개 있습니다. 리소스 정책이라는 점에서 S3 버킷정책과 유사합니다. 즉 JSON IAM정책을 SQS대기열에 직접 추가하면 됩니다.

1. **교차 계정 액세스를 허용**

어떤 계정에 대기열이 있고 다른 계쩡이 그 대기열에 액세스 해야 한다고 하고, EC2 인스턴스가 하나 있다고 가정한다. 그 EC2 Instance가 계정 간 메시지를 가져올 수 있으려면 다음과 같이 생긴 대기열 액세스 정책을 생성하고 이를 첫 번째 계쩡의 SQS대기열에 첨부해야 한다.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": ["111122223333"]},
    "Action": ["sqs:ReceiveMessage"],
    "Resource": "arn:aws:sqs:us-east-1:444455556666:queue1"
  }]
}
```

위의 Queue Access Policy 는 AWS의 보안 주체가 11112222333이 될 수 있게 허용한다. 따라서 이 정책은 EC2 인스턴스가 다른 계정의 SQS 대기열에서 가져올 수 있게 합니다. 



2. **S3 이벤트 알림 게시**

S3 버킷에 객체를 업로드하면 SQS대기열에 자동으로 메시지를 보냅니다. SQS대기열은 S3버킷이 메시지를 작성할 수 있는 권한을 부여해야 합니다. 따라서 아래와 같이 생긴 SQS Queue Access Policy 를 생성해야 합니다.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "*"},
    "Action": ["sqs:SendMessage"],
    "Resource": "arn:aws:sqs:<region_name>:<bucket1_owner_account_id>:<queue_name>",
    "Condition": {
      "ArnLike": {"aws:SourceArn": "arn:aws:s3:*:*:<bucket_name>"},
      "StringEquals": {"aws:SourceAccount": "<bucket1_owner_account_id>"},
    }
  }]
}
```

자세히 살펴보면 Action은 sqs:SendMessage이고 Principal은 모든(*) 계정의 AWS 입니다. Condition은 버킷의 ARN소스가 'bucket1' 이라는 이름의 S3버킷이어야 합니다. 소스 계정은 S3 버킷의 계정 소유자여야 합니다. 그러면 S3버킷은 SQS대기열에 작성할 수 있게 됩니다.





- S3 에 Object 들을 생성/수정/삭제 등등의 작업을 하게되면 S3 => SQS Queue 로 이벤트를 전송하게 하는 정책이다.
- 이를 활용하면 여러가지 상황에 맞는 로직을 작성해서 원하는 작업을 수행할 수 있게 될 것이다.
- 구글링 키워드 : [How to send message S3 to SQS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html)
- 아래 동영상을 참고해도 좋음

{% include video id="ZDHy3pwJnyo" provider="youtube" %}

