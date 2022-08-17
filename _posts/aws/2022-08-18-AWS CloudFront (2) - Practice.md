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

title: "[aws] CloudFront (2) - Practice"
excerpt: "🚀 CloudFront, CDN 실습"

categories: aws
tag: [aws, cloudfront, cdn, origin, content, cache]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# AWS CloudFront



1. CloudFront 를 생성하기 위해서는 먼저 S3 Bucket 이 만들어져 있어야 한다.
   - 웹사이트를 호스트할 버킷이 된다.

2. S3 버킷을 생성후, CloudFront Console UI 로 접근한다. 
3. CloudFront 는 Global Service 이다. 전세계에 배포되야 하기 때문이다. (region이 없음)

![image-20220818004728612](../../assets/images/posts/2022-08-18-AWS CloudFront (2) - Practice/image-20220818004728612.png)





1. 배포를 생성한다.
2. 원본 도메인을 선택한다.
   - S3
   - EC2
   - ALB
   - Gateway ... 등등
3. OAI 사용여부를 선택
   - CloudFront 가 S3 에 접근할때 보안을 활성화할것인지 말것인지 결정
   - CloudFront가 생성한 OAI 신분을 이용해서 S3 Bucket에 액세스할 수 있게 된다.

![image-20220818005139019](../../assets/images/posts/2022-08-18-AWS CloudFront (2) - Practice/image-20220818005139019.png)



클라우드 프론트는 Amazon S3에 있는 콘텐츠를 배포한다.

- S3 버킷이 현재 public 접근이 불가능하기 때문에 CloudFront를 통해서만 접근해야된다.
  - S3 Bucket 생성시 public 접근 허용안했음
  - 고로 OAI 를 사용해서 CloudFront --> S3 로 데이터를 받아와야함
  - CloudFront 가 제공하는 도메인주소로 들어가게되면 처음엔 S3 에서 데이터를 가져오고
  - 그 뒤부터는 CloudFront EdgeLocation에 있는 캐시에 저장된 컨텐츠를 불러오게 된다. (CDN)
- 아래 사진에서는 원본을 S3 버킷말고 ALB 에서 가져오도록 설정한 사례이다.

![image-20220818010448944](../../assets/images/posts/2022-08-18-AWS CloudFront (2) - Practice/image-20220818010448944.png)

![image-20220818010516486](../../assets/images/posts/2022-08-18-AWS CloudFront (2) - Practice/image-20220818010516486.png)