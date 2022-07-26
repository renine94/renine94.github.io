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

title: "[aws] S3 (3) - Securty"
excerpt: "🚀 S3 Security, Bucket Policies, Pre-Signed URLs"

categories: aws
tag: [aws, s3, security]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# S3 Security

> S3 의 보안에 대해서 알아보자.

**S3 보안의 종류**

- 사용자 기반
  - IAM 정책 - IAM 콘솔로부터 특정 유저에게만 API 호출을 허용한다.
  - IAM 사용자는 IAM 정책을 가지고 있고, 이 정책은 어떤 API 호출이 허용될지를 결정한다.
  - 유저가 IAM w정책을 통해 Amazon S3 버킷으로의 액세스 방법을 승인받게 되면 실행이 가능해진다.
- 리소스 기반 
  - 버킷 정책 - S3 콘솔에서 설정 가능한 버킷 전반의 규칙
    - S3 버킷에서 보안 주체가 무엇을 할 수 있는지 없는지 결정하는 정책
    - 이를 통해 S3 버킷으로의 교차 계정 액세스가 활성화된다.
  - 세분화된 방식의 ACL 방식 (Access Control List)
    - 객체 레벨에서의 액세스 규칙 설정
    - 버킷 ACL 방식은 더욱 드물다.



- 참고 : IAM 정책에 따라 S3 객체에 접근 가능
  - 유저 권한이 허용되있거나, 또는 리소스 정책이 허용되있거나
  - 그리고, 명시적 거부가 없어야 한다.



## S3 Bucket Policies

> S3 버킷 정책 살펴보기

- Json Based policies

  - Json 기반의 정책이다.

  - ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicRead",
          "Effect": "Allow",
          "Principal": "*",
          "Action": [
            "s3:GetObject"
          ],
          "Resource": [
            "arn:aws:s3:::examplebucket/*"
          ]
        }
      ]
    }
    ```

  - 구성

    - Resource: 버킷과 객체
    - Action: API 를 허용/불허 설정
    - Effect: 허용/불허
    - Principal: 해당 S3버킷의 정책을 적용할 계정 or 유저

  - S3 버킷의 어떤 객체에도 접근이 가능하다는 의미이다.



- S3 Bucket 정책을 사용하는 예시 (UseCase)
  - Bucket에 퍼블릭 액세스 권한을 승인하거나
  - 업로드 시점에 객체를 암호화 시킬 경우
  - 교차 계정 S3 버킷 정책을 사용해서 다른 계정에 액세스 권한을 주는 경우



## Bucket settings for Block Public Access

> 블록 퍼블릭 액세스 버킷 설정
>
> 계정에 제한이 있을 경우에 사용된다.

- 객체가 퍼블릭화 되는 것을 차단하는 새로운 설정이다.
- 4가지 종류의 Public Access 차단 설정
  1. 새 액세스 제어 목록 (New access control lists) ACLs
  2. 모든 액세스 제어 목록 (Any accss control lists) ACLs
  3. 새로운 퍼블릭 버킷
  4. 액세스 포인트 정책



- 기업 데이터 유출을 위해서 만들어졌다.
- 버킷을 퍼블릭으로 두지않으려면 이 설정을 켜면 된다.
- 계정 레벨에서 설정하는 방법을 알아보자



## S3 Security - Other

- Networking
  - VPC 엔드포인트로 S3에 비공개 액세스가 가능
  - 즉, VPC에 EC2 인스턴스가 있고 인터넷 액세스는 없는 경우
  - VPC 엔드포인트를 통해 비공개로 S3에 접근이 가능하다.
- Logging and Audit (로깅 및 감사)
  - S3 액세스 로그를 사용하면 다른 S3 버킷에 해당 로그가 저장된다.
  - API 호출은 CloudTrail 계정에 API 호출을 로깅할 수 있는 서비스에도 로깅이 가능
- User Security (사용자 보안)
  - MFA 삭제 활성화
    - 특정 버전 객체를 버킷에서 삭제하고 싶은 경우 MFA 삭제 활성화
    - **MFA 로 인증이 되어야만 객체를 삭제 할 수 있게 된다.**
  - 사전 서명된 URL
    - AWS 자격 증명으로 서명된 URL
    - 한정된 시간 동안만 유효하고, URL 이 아주 길다.
    - 사용 예시
      - **유저가 서비스로부터 프리미엄 영상을 구매하여, 다운로드 하는 경우 등**



제한된 시간 내에 특정 유저가 특정 파일에 액세스하는 경우에 사용하는 보안은 **사전 서명된 URL** 을 생각하면 된다.