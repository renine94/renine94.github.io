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

title: "[aws] CloudFront (3) - Signed URL & Cookies"
excerpt: "🚀 CloudFront, URL, Cookies"

categories: aws
tag: [aws, cloudfront, cdn, origin, content, cache]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# CloudFront Signed URL & Cookies

- CloudFront 분산을 비공개로 만들기 위해서는 세계 각지의 사람들에게 프리미엄 유료 콘텐츠에 대한 액세스를 주어야 한다.
- 누가, 어떤 CloudFront 분산에 액세스하는지 알기 위해 Signed URL & Cookies를 사용한다.
  - URL과 Cookies를 생성할 떄는 정책을 연결한다.
  - 해당 URL & Cookies 가 언제 만료되는지 설정한다.
  - 이 데이터에 액세스할 수 있는 IP 범위를 지정한다. (클라이언트의 대상IP를 알 경우 사용 가능)
  - 어떤 AWS 계정이 서명된 URL 을 생성할 수 있는지를 의미하는 신뢰할 수 있는 서명자를 지정한다.
- URL 은 얼마나 오래 유효해야 하는가?
  - 영화나 음악과 같은 콘텐츠를 공유할 때는 몇 분 정도로 짧아도 될 것
  - 사용자가 장기간 액세스할 수 있어야 하는 비공개 컨텐츠의 경우에는 URL 이나 Cookies가 수 년간 지속되게 할 수도 있다.



- URL vs Cookies 차이
  1. **Signed URL**
     - 개별 파일에 대한 액세스를 준다.
     - 파일 별로 하나의 URL이 있다.
     - 파일이 100개면 100개의 URL이 있다.
  2. **Signed Cookies**
     - 다수의 파일에 액세스를 주고 해당 쿠키는 재사용이 가능하다
     - 즉, 다수의 파일에 서명된 쿠키는 하나인 것



상황에 따라 적절히 URL or Cookies 방식을 사용하면 된다.



## 01. CloudFront Signed URL Diagram

![image-20220823021252005](../../assets/images/posts/2022-08-23-AWS CloudFront (3) - Signed URL & Cookies/image-20220823021252005.png)



CloudFront Distribute 가 있고, 여러 개의 EdgeLocation이 있다. 그리고 예를 들어 보안을 위해 오리진액세스신분(OAI)을 이용해 S3 Bucket에 액세스한다고 한다. 즉, 오직 CloudFront를 이용해서만 S3 버킷 내의 객체에 액세스할 수 있는 것이다. 하지만 여전히 클라우드 프론트를 통해 사람들에게 객체에 대한 액세스를 제공하고자 한다.

즉, 

1. 클라이언트는 애플리케이션으로 허가 및 승인요청을 보낼 것
2. 애플리케이션은 AWS SDK 를 사용해 CloudFront로부터 직접 Signed URL을 생성한다.
3. 서명된 URL은 Client 에게 반환될 것이다.
4. Clients는 이 Signed URL 을 이용하여 데이터와 파일 객체 등 CloudFrontd에서 원하는 것을 직접 얻을 수 있게됨
5. 서명된 URL 뿐 아니라 Signed Cookies도 방식은 동일하다.





## 02. CloudFront Signed URL vs S3 Pre-Signed URL

> - CloudFront Signed URL
> - S3 Pre-Signed URL 
>
> 위 2개의 차이점에 대해 알아보자

![image-20220823022441405](../../assets/images/posts/2022-08-23-AWS CloudFront (3) - Signed URL & Cookies/image-20220823022441405.png)



CloudFront Signed URL 과 S3 Pre-Signed URL 중 어느 것을 사용해야 하는가?

- **CloudFront Signed URL**

  - 위의 2개는 용도자체가 다르다.

  - CloudFront에 Signed URL은 Origin에 상관 없이 경로에 대한 액세스를 허용하기 때문에 URL 은 S3 Origin뿐만 아니라 원하시는 모든 HTTP 백엔드 오리진에서 작동한다.

  - 계정 내 키 페어이기 때문에 root만 관리할 수 있고 IP, 경로, 날짜, 만료 등으로 필터링 가능하다.

  - CloudFront에 있는 모든 캐싱 기능을 활용할 수 있다.

- **S3 Pre-Signed URL**

  - URL 에 미리 서명한 사람으로서 요청을 발행한다.
  - 나만의 IAM 원칙으로 URL에 서명하고 서명을 위해 제 IAM 키를 사용하게 한다.
    - 해당 URL을 가진사람은 나와 같은 권한을 가지게 된다.
  - 수명이 제한적이다. 이 Pre-Signed URL 을 사용해 클라이언트가 직접 S3 Bucket에 액세스 가능

<br><br>

만약 사람들이 우리의 CloudFront분산에 액세스하길 원하고, S3 앞에 있는 경우라면 의도한 대로 S3 버킷에 액세스할 수 없으므로 Signed URL 을 사용해야 한다.

이를 OAI 로 제한하는 버킷 정책 때문이다.

하지만 CloudFront를 사용하지않고 사용자들이 직접 S3버킷으로 액세스해 파일을 사용하길 원하시면 Pre-Signed URL이 더 적합할 것이다.

