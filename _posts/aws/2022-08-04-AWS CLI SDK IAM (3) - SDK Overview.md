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

title: "[aws] CLI SDK IAM role policy (3) - SDK & Quiz"
excerpt: "🚀 SDK, boto3, quiz"

categories: aws
tag: [aws, sdk, boto3, quiz]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# SDK Overview

- 만약 지금까지 사용했던 CLI 를 사용하지 않고 Application code 에서 직접 AWS 작업을 하려면 어떻게 해야 할까?
- 그럴때 우리는 AWS SDK 를 사용할 수 있다. (software development kit)
- 다양한 언어의 AWS용 공식 SDK 가 있다.
  - java
  - **python => boto3**
  - node.js
  - go
  - php
  - ruby
  - .NET
  - .....등등



CLI 를 사용할 때는 python sdk 를 사용했었다.<br>왜냐하면 CLI 가 python 언어를 사용하고 Boto3 SDK 를 사용하기 때문이다.

- SDK 는 DynamoDB 나 Amazon S3 와 같은 Amazon Service에서 API 호출을 발행할때 사용한다.
- 하지만 CLI도 python sdk (boto3) 를 사용합니다.
- 언제 sdk 를 쓰는지를 아는것이 중요하다.



**SDK 를 사용할 때, default region 을 설정하지 않으면 기본적으로 `us-east-1` 으로 자동설정되므로 유의하고,<br>ap-northest-2 (서울) 로 바꿔주는것을 잊지말자!**





# Quiz



- EC2 인스턴스에 호스팅된 애플리케이션이 PutObject API 호출을 사용해 S3 버킷에 객체를 업로드하려 합니다. 하지만 요구되는 권한을 가지고 있지 않은 상황입니다. 어떻게 해야 할까요?
  - EC2 인스턴스 내부에서 `aws configure` 을 실행해 필요한 API를 호출하기 위한 액세스를 보유한 개인 IAM 자격 증명 삽입
  - <span style="color: red;">필요한 API를 호출할 수 있도록 허가해 주는 IAM 정책을 EC2 인스턴스에 있는 IAM 역할과 연결해 줄 것을 관리자에게 요청</span>
  - EC2 인스턴스의 IAM 자격 증명을 가진 환경 변수를 내보내기
  - EC2 메타데이터 API 호출 사용

**IAM 역할은 EC2 인스턴스에 자격 증명 및 권한를 부여하기 위해 사용할 수 있는 적절한 방법입니다.**

<br><br>

- 여러분은 동료와 함께 API 호출을 만들어 AWS 서비스와 상호작용하는 애플리케이션을 개발하고 있습니다. 동료는 아무 문제 없이 자신의 기기에서 애플리케이션을 실행할 수 있으나, 여러분에게는 API 인증 예외 처리가 발생합니다. 어떻게 해야 할까요?
  - AWS 액세스 키 및 암호 액세스 키를 동료에게 보내 동료의 기기에 동일한 문제를 복제할 수 있도록 하기
  - 아무 문제 없이 작업할 수 있도록 동료의 IAM 자격 증명을 보내달라고 요청
  - <span style="color: red;">AWS 정책 시뮬레이터에서 자신의 IAM 정책을 동료의 IAM 정책과 비교해 차이점 찾아 보기</span>
  - 동료에게 EC2 인스턴스를 생성할 것을 요청하고, 동료의 IAM 자격 증명을 삽입하여 EC2 인스턴스에서 애플리케이션을 실행

<br><br>

- 관리자가 Linux EC2 인스턴스를 실행하여 여러분이 SSH를 할 수 있도록 EC2 키 쌍을 제공했습니다. EC2 인스턴스로 들어간 여러분은 EC2 인스턴스 ID를 받으려 합니다. 이를 위한 최선의 방법은 무엇인가요?
  - IAM 역할을 생성하고 이를 EC2 인스턴스에 연결하여 `describe-instances API` 호출하기
  - `http://169.254.169.254/latest/user-data` 에서 사용자 데이터를 쿼리하기
  - <span style="color: red;">`http://169.254.169.254/latest/meta-data` 에서 메타데이터를 쿼리하기</span>
  - `http://254.169.254.169/latest/meta-data` 에서 메타데이터를 쿼리하기