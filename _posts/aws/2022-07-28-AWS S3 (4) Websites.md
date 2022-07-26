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

title: "[aws] S3 (4) - WebSites"
excerpt: "🚀 S3 Websites, Hosting"

categories: aws
tag: [aws, s3, websites, hosting]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# S3 Websites

> S3 웹사이트에 대해 알아보자.



- S3 는 정적 웹사이트를 호스팅 할 수 있고, www에서 접근이 가능하도록 허용하며 웹사이트 URL도 간단하다.
- HTTP 엔드 포인트는 아래와 같은 모습이다.
  - <bucket-name>.s3-website-<AWS-region>.amazoneaws.com
  - 버킷 이름으로 시작하고, 중간에 region 이름이 들어가게 된다.



- 웹사이트를 활성화 했으나, 403 Forbidden 오류가 발생한다면, 버킷 정책을 public read 로 변경해야 한다.



- 생성한 S3 Buckets 을 웹사이트로 활성화

  - Bucket 을 정적 웹사이트로 만드는 것
  - 버킷 - 속성 - 정적 웹 사이트 호스팅

  ![image-20220727015141871](../../assets/images/posts/2022-07-28-AWS S3 (4) Websites/image-20220727015141871.png)



위 사진에서 정적 웹사이트 호스팅을 활성화로 변경후



![image-20220727015219546](../../assets/images/posts/2022-07-28-AWS S3 (4) Websites/image-20220727015219546.png)



- 위에서 인덱스문서, 오류 문서 를 모두 지정해준다.

  - 버킷에 index.html, error.html 파일을 모두 업로드한 상태임

- 생성된 URL 주소에 접근한다.

  - 403 에러가 나타날 것

- 에러 발생시

  - 해당 Bucket을 public 상태로 바꾼다.

    1. Block public access 를 체크 해제한다.
    2. 버킷정책에서 Json 문서로 모든유저가 해당 객체를 getObject 할수있는 권한을 만든다.

    ```json
    {
      "Id": "asdgasgasd",
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "asdfasdf",
          "Action": [
            "s3:GetObject"
          ],
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::demo-my-bucket-name/*",
          "Principal": "*"
        }
      ]
    }
    ```

    

    