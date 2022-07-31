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

title: "[aws] CLI SDK IAM role policy (1) - intro"
excerpt: "🚀 CLI, SDK and IAM 역할 정책"

categories: aws
tag: [aws, cli, sdk, iam]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# AWS CLI SDK IAM



## IAM Role Policy

- Role (역할)
  - Policy 1 (정책)
  - Policy 2
  - Policy 3

ex) MyFirstEC2 역할에는 AmazonS3FullAccess 정책, 등등 여러가지 정책을 가질 수 있다.





- Policy

  - AmazonS3ReadOnlyAccess

    - 

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "s3:Get*",
            "s3:List*"
          ],
          "Resource": "*"
        }
      ]
    }
    ```

    - Get, List 로 시작하는 API를 모두 사용할 수 있는 권한 정책

    

  - AmazonS3FullAccess

    - ```json
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
          }
        ]
      }
      ```

    - S3 의 모든 API 를 허용하는 정책





## IAM Policy Simulator

> 정책에 관한 시뮬레이션을 할 수 있는 공간

어떤 유저/그룹/역할 마다 연결된 정책(policy) 들을 API 가 사용가능한지 안가능한지 확인해볼 수 있는 공간이다.

User, Group, Role 마다 여러개의 Policy 들을 가지고 있다.

<br><br>

- https://policysim.aws.amazon.com/home/index.jsp

![image-20220731215632215](../../assets/images/posts/2022-08-01-AWS CLI SDK IAM (1) - intro/image-20220731215632215.png)