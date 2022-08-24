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

title: "[aws] CloudFront (4) - Pricing"
excerpt: "🚀 CloudFront, Pricing, Price Class, Multiple Origin, Origin Groups"

categories: aws
tag: [aws, cloudfront, cdn, pricing, origin]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# CloudFront - Pricing

> - 고급옵션
>   1. 요금
>   2. 가격 등급

- CloudFront의 EdgeLocation이 전 세계에 퍼져있다.
- 전세계에 걸쳐 존재하기에 EdgeLocation에 따른 데이터 전송 비용도 다르다.

아래는 클라우드프론트의 요금(가격)표이다.

![image-20220825003833307](../../assets/images/posts/2022-08-25-AWS CloudFront (4) - Pricing/image-20220825003833307.png)



위의 사진을 보면, EdgeLocation 이 위치한 대륙 또는 지리적 위치에 따라 요금이 달라진다.<br>맥시코 및 미국, 캐나다의 경우 첫 10TB에 대한 요금은 1GB 당 0.085달러 이지만,<br>인도의 경우에는 1GB당 0.17$ 로 약 2배정도 비싼것을 볼 수 있다.

CloudFront에서 많은 데이터가 전송될수록 요금은 낮아지므로, 만약 클라우드프론트에서 5PB의 데이터를 전송하는 경우에 미국의 경우에는 0.02달러의 요금을 지불하면 된다.

오른쪽의 지역으로 갈수록 가격이 비싸지는것을 볼 수 있고, 아래에서 배울 "가격 등급" 이라는 개념으로 지어진다.



## 01. CloudFront - Price Class

- 전 세계에 걸쳐 CloudFront 분산에 사용할 EdgeLocation 수를 줄여 가격을 낮출 수 있다.
- 가격등급(price class) 은 총 3가지 이다.
  1. **Price Class All**
     - 모든 지역, 가장 성능이 좋으나 비용이 다소 높다.
     - 전 세계의 엣지로케이션을 이용 가능
  2. **Price Class 200**
     - 가장 비싼 지역을 제외한 대부분의 지역을 제공
  3. **Price Class 100**
     - 가장 저렴한 지역만을 제공한다.
     - 미국, 북미 및 유럽 제공

![image-20220825004734691](../../assets/images/posts/2022-08-25-AWS CloudFront (4) - Pricing/image-20220825004734691.png)





## 02. CloudFront - Multiple Origin

> 다중 오리진과 오리진 그룹을 알아보자

- 콘텐츠의 유형이나 경로에 따라 CloudFront를 거치는 라우트나 경로를 리다이렉팅해 다른 오리진으로 라우팅하고 싶은 경우
- 이미지용 경로 or API용 경로 or 그외의 모든 경로
- 어느 경로건 CloudFront에서는 정해진 경로는 통해 다양한 캐시 작업을 설정할 수 있다.
  - ex)
  - `/images/*`
  - `/api/*`
  - `/*`

![image-20220825005400943](../../assets/images/posts/2022-08-25-AWS CloudFront (4) - Pricing/image-20220825005400943.png)

/api/* 경로를 사용중인 경우 App의 ALB가 되는 오리진으로부터의 회신이 필요하다고 할 수 있다. 하지만, 그 외의 모든 경로인 /* 를 호출할 경우 /* 가 변함없는 콘텐츠라면 해당 콘텐츠를 S3 Bucket에서 가져와야 할것이다.

이런식으로 CloudFront에서 사용되는 경로를 기반으로 다중 Origin이 정의된다.<br>마찬가지로 Origin Group을 설정할 수도 있는데, 이 경우에는 용례가 다르다.



## 03. CloudFront - Origin Groups

- 고가용성과 장애조치를 향상시키고 싶은 경우
- Origin Groups 는 하나의 primary(주) origin과 하나의 secondary(보조) origin 으로 구성된다.
- 만약 primary origin에 문제가 발생하면 CloudFront가 secondary origin을 사용하는 것으로 대체를 한다.

![image-20220825005631183](../../assets/images/posts/2022-08-25-AWS CloudFront (4) - Pricing/image-20220825005631183.png)





## 04. CloudFront - Field Level Encryption

> 필드 수준의 암호화에 대해 살펴보자

- 어플리케이션 스택을 통한 민감한 정보를 보호하는 기능
- HTTPS 를 사용하는 in-flight 암호화와 더불어 추가적인 보안을 더해 준다.
- 즉, 사용자가 민감한 정보를 전송할 때마다 EdgeLocation이 이를 암호화하고 개인 키에 대한 권한을 지닌 사용자만이 이 정보를 해독할 수 있도록 하는 개념
  - 따라서 이 기능은 비대칭 암호화를 사용하게 된다.
- 사용 사례
  - CloudFront로 보내는 POST요청의 경우 암호화를 원하는 필드를 최대 10개까지 지정 가능
    - 신용카드 등을 예로 들 수 있다.
  - 이 필드를 해독할 공용 키도 함께 지정된다.
    - HTTPS를 EdgeLocation으로 전달하는 클라이언트가 있다고 가정한다.
    - EdgeLocation은 다시 HTTPS를 통해 CloudFront로 전달하고, 이는 App LB 를 통해 HTTPS를 사용해 Origin 까지 전달될 것이다.
    - 그 다음, 모든 데이터가 HTTPS를 통해 웹서버로 전달된다.
    - 전송 과정에서 모든 정보는 암호화되어 있으나, 우리는 필드 수준의 암호화를 설정하려고 한다.

![image-20220825010534173](../../assets/images/posts/2022-08-25-AWS CloudFront (4) - Pricing/image-20220825010534173.png)



1. 한 사용자가 우리에게 신용카드 정보를 전달한다고 가정
2. 위 사진에서 주황색으로 표시된 정보이다.
3. 우리가 이 신용카드 정보에 대한 필드 수준 암호화를 지정하려 하면 EdgeLocation이 공용 키를 이용해 이 필드를 암호화한다.
4. EdgeLocation을 지나 CloudFront, 그리고 Origin으로 전달되는 데이터의 신용카드 정보는 공용키를 이용해 암호화가 되어 있는 상태
5. 암호화된 정보가 웹서버까지 전달된다.
6. 데이터가 도착하면 웹 서버는 개인 키에 대한 권한을 갖게 될 것이며 개인 키를 사용해 이 암호화된 단위를 해독하여 신용카드 번호를 얻게 될 것

<br>

스택 전반에 걸쳐 확인할 수 있듯 CloudFront 지역과 애플리케이션 로드밸런서는 이 필드를 해독할 수 없다.<br>오직, 웹서버만이 필드를 해독할 수 있는 커스텀 애플리케이션 논리를 가지고 있다.

