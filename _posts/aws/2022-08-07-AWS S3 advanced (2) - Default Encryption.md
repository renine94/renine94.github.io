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

title: "[aws] S3 Advanced (2) - Default Encryption, Access Logs"
excerpt: "🚀 S3, Default Encryption, Bucket Policies, Access Logs"

categories: aws
tag: [aws, s3, encryption, policies, log]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# S3 Default Encryption vs Bucket Policies

- S3 버킷에 파일을 업로드하고, 파일이 암호화되도록 하기 위해서는<br>버킷 정책을 사용해 암호화를 강제할 수 있다.
- 버킷 정책을 사용하면 API 호출에서 암호화 Header가 지정되지 않은 채 S3에 도달하면, 요청이 거부된다.
- 따라서 사용자의 S3 버킷에 푸시되는 모든 객체를 암호화하는 효과를 가져온다.

<br>

이런 방법 외에 다른 방법도 있다.

- S3의 기본 암호화 옵션을 사용하는 것이다.
- 암호화되지 않은 객체를 S3에 업로드하면 기본 암호화 옵션을 통해 암호화가 이루어진다.
- 다만, 암호화된 객체를 업로드할 때, 재암호화가 되지는 않는다.

<br>

중요한 점

- **버킷 정책 방식이 기본 암호화보다 먼저 고려**된다는 점이다.
- 예를 들어 SSE-S3 이라는 암호화 메커니즘을 강제하려면 버킷 정책을 사용해야 하지만,<br>그저 버킷 내 모든 객체를 암호화하려는 것이 목적이라면 기본 암호화를 사용해도 된다.

<br>

암호화 유형

- SSE-S3
- SSE-KMS
- ...등등



# S3 Access Logs

- 감사 목적으로 모든 Access를 S3버킷에 로깅하는 경우에 사용
- S3로 보내지는 모든 요청은 계정과 승인 여부에 상관없이 다른 S3버킷에 로깅되어 이후에 분석이 가능하다.
- 데이터분석 도구를 이용해서 분석하거나 나중에 학습하게될 `Athena` 를 사용해 분석할 수도 있다.
- 로그 포멧은 [여기에서 확인](https://docs.aws.amazon.com/AmazonS3/latest/userguide/LogFormat.html) 할 수 있다.

<img src="../../assets/images/posts/2022-08-07-AWS S3 advanced (2) - Default Encryption/image-20220808020826988.png" alt="image-20220808020826988" style="zoom:50%;" />





## 1. Access Log 주의사항

- 모니터링중인 버킷을 로깅 버킷으로 설정하면 "절대" 안된다.
- 만약 모니터링 버킷을 로깅 버킷으로 사용하게 되면 **무한 로깅 루프**가 생기게 되고,<br> 버킷의 크기가 기하급수적으로 커진다.
- App이 사용하는 버킷과 Log 버킷을 꼭 구분해서 사용하도록 하자!

![image-20220808021239109](../../assets/images/posts/2022-08-07-AWS S3 advanced (2) - Default Encryption/image-20220808021239109.png)



Server Access Logging 기능을 활성화할 때, Target bucket은 로그가 쌓일 bucket을 선택하면 된다.