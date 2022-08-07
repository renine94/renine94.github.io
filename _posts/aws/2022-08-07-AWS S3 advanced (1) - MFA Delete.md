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

title: "[aws] S3 Advanced (1) - MFA Delete"
excerpt: "🚀 S3, MFA Delete, CLI 설정"

categories: aws
tag: [aws, s3, mfa, cli]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# S3 MFA-Delete

- MFA 라고 불리는 다요소 인증을 사용해 사용자의 장치에서 코드를 생성하도록 한다.
  - 장치는 모바일폰이나, 하드웨어 키 등이 된다.
  - S3 에서 중요한 작업 전 이루어지는 과정이다.
- **MFA 삭제 기능을 사용하기 위해서는 S3 버킷에서 버저닝을 활성화 해야 한다.**
- MFA 가 필요한 경우
  1. 영구적으로 객체 버전을 삭제할 때,
  2. 버킷에서 버저닝을 중단하는 경우
- MFA 가 불필요한 경우
  1. 버저닝을 활성화 하거나,
  2. 삭제된 버전을 목록화 할 때



- 오직 루트 계정인 버킷 소유자만이 MFA삭제기능을 활성화 및 비활성화를 할 수 있다.
  - 즉, 관리자 계정이 있어도 MFA 삭제를 활성화 하지 못한다.
  - **Root 계정만 가능**하다
- 현재는 CLI 를 통해서만 MFA-삭제기능을 사용한다.



- MFA 기능을 현재 사용중이어야 한다.



## 1. 실습

```sh
# generate root access keys
$ aws configure --profile [원하는 profile name]
AWS Access Key ID [None]: ???
AWS Secret Access Key [None]: ???
Default region name [None]: ap-northest-2
Default output format [None]: json

# enable mfa delete
$ aws s3api put-bucket-versioning --bucket [bucket_name] --versioning-configuration Status=Enable,MFADelete=Enabled --mfa "arn-of-mfa-device [mfa-code]" --profile [내가만든 profile name]

# disable mfa delete
$ aws s3api put-bucket-versioning --bucket [bucket_name] --versioning-configuration Status=Enable,MFADelete=Disabled --mfa "arn-of-mfa-device [mfa-code]" --profile [내가만든 profile name]

# delete the root credentials in the IAM console!!!
```



- MFA 삭제 기능이 활성화되어있으면 AWS Console 상에 UI 에서는 이제 버킷안의 객체들을 삭제할수없다.
  - UI 상에서 삭제하려면 MFA삭제 기능을 다시 비활성화 해야 한다.