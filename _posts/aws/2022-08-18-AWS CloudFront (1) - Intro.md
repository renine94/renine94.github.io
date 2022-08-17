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

title: "[aws] CloudFront (1) - CDN & Intro"
excerpt: "🚀 CloudFront, CDN, S3 cross region replication과의 차이점에 대해 알아보자!"

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

> Content Delivery Network (CDN)

![image-20220817233037288](../../assets/images/posts/2022-08-18-AWS CloudFront (1) - Intro/image-20220817233037288.png)

- 읽기 성능을 향상시킨다. 컨텐츠가 Edge Location에서 분배 및 캐시가 되기 때문이다.
- 216개의 엣지 로케이션이 존재하며, 지속적으로 추가되어지고 있다.
  - AWS 내의 리전은 약 30개 정도인데, Region 수보다 훨씬 더 많으며 전 세계에 퍼져있다.
  - Netflix 가 CDN 을 적극 활용하는것으로 알고있음
- 엣지에서의 캐싱 이외에 DDoS 공격으로부터 보호하는 기능도 제공한다.
  - 서비스 거부를 배포하는 이러한 공격으로부터 보호막과 웹App 방화벽을 제공한다.
  - 보안이 철저하고, 애플리케이션을 전 세계적으로 배포하기에 좋은 프론트이다.
- 인증서를 로드하여 외부 HTTPS 엔드포인트를 노출하고, 해당 트래픽을 암호화해야 하는 경우 내부 HTTPS 에서 내부적으로 통신하게끔 해준다.



위에 보이는 그림에 세계지도가 보인다. 몇 개의 주황색 Region과 Edge가 있다. 지도 내에 보이는 지점은 모두 Edge로 보다시피 전 세계에 퍼져 있다. 예를 들어, 호주에서 S3 버킷이 있고 미국의 사용자가 여기로 액세스하려 하면 미국에서 가까운 엣지 로케이션에 액세스를 한 뒤, 해당 네트워크가 사설 AWS 네트워크를 통해 S3 버킷까지 전송이 된다. 그리고 콘텐츠는 캐시됩니다. 즉, 미국에 이러한 사용자가 많아질수록 동일한 읽기를 원하는 사람이 많아질 것이고 그렇게 되면 이런 사용자들은 호주가 아니라 미국에서 직접 제공되는 콘텐츠를 얻게 되는 것이다.

콘텐츠가 미국에서 Fetch 되고 제공되면 현지에서 캐시되기 때문이다. 아시아에 있는 다른 사용자가 아시아에서 가까운 엣지 로케이션으로 통신을 하면, 엣지 로케이션이 S3 버킷으로 트래픽을 지원하여 콘텐츠를 얻고 엣지에서 캐시할 것이다. 즉, CloudFront는 이처럼 다양한 엣지 로케이션에 기반해 읽기를 전 세계에 배포한다.

그렇게 되면 메인 S3 버킷에서 지연 시간과 로드를 줄일 수 있다.



## 1. CloudFront - Origin

> S3 버킷을 포함한 다른 CloudFront의 Origin을 살펴보자

1. **S3 Bucket**
   - S3 앞에서 클라우드프론트를 사용하는 것은 전 세계에 파일을 배포하고 엣지에서 캐시할 때 흔히 보는 패턴
   - OAI (Origin Access Identity) 으로 CloudFront와 S3 Bucket 사이의 보안을 강화해준다.
     - S3 버킷이 오직 CloudFront 하고만 통신할 수 있도록 해준다.
   - CloudFront 를 세계 어디서든 파일을 S3에 업로드할 입구처럼 사용할 수도 있다.
2. **Custom Origin**
   - HTTP 엔드 포인트가 있어야 한다. HTTP 프로토콜을 준수하는 무엇이든 될 수 있다.
     - Application Load Balancer
     - EC2 Instance
     - S3 Website (정적 S3 웹사이트로 버킷을 활성화해야 하며, 이는 S3버킷과는 다르다.)
   - 우리가 원하는 모든 HTTP 백엔드가 가능하다.
     - 사내에 있는 인프라일수도 있다.



## 2. CloudFront - How to work?

> CloudFront의 전반적인 작동방식에 대해 알아보자

![image-20220817234103018](../../assets/images/posts/2022-08-18-AWS CloudFront (1) - Intro/image-20220817234103018.png)



전 세계 여러 곳에 엣지 로케이션이 있고, 이 엣지로케이션들은 우리가 정의한 Origin으로 연결되어 있다. S3 Bucket 등 어떤 HTTP Endpoint도 될 수 있다. 클라이언트가 우리의 CloudFront 분산으로 접근(액세스)하려 하는 경우 클라이언트는 CloudFront에 직접 HTTP 요청을 보낼것이다.

HTTP 요청은 위와 같은 형식인데, URL, QueryString, Header 등으로 이루어져 있다. 그러면 Edge Location이 요청을 Origin으로 전달할 것이다. 이 요청에는 queryString과 header가 포함될 것이며, 이렇게 모든 내용이 origin으로 전달이 되게 된다.

그러면 오리진이 엣지로케이션에 회신해 엣지 로케이션은 정의된 캐시 설정에 따라 회신 내용을 캐시할 것이다. 그리고 다음 번에 클라이언트가 비슷한 **요청을 하면 엣지 로케이션은 요청을 오리진으로 전달하기 전에 우선 캐시부터 살펴볼 것이다. 이런 작업이 바로 CDN의 목적**이다.



## 3. CloudFront - S3 as an Origin

> Origin으로서의 S3를 알아보자!

![image-20220817234633755](../../assets/images/posts/2022-08-18-AWS CloudFront (1) - Intro/image-20220817234633755.png)



- Cloud가 있고, Origin 즉, S3 Bucket이 있다.
- Edge Location은 로스엔젤레스에 있다고 하자.
- 이 Edge Location으로부터 데이터를 읽으려 하는 몇몇의 Users이 있으면 엣지로케이션이 private AWS Network를 통해 S3 버킷에서 데이터를 가져와서 해당 엣지 로케이션으로부터 결과를 제공할 것이다.
- 요점은, CloudFront의 EdgeLocaiton이 S3 Bucket에 액세스하면 CloudFront Origin에 대한 IAM역할인 OAI 즉, 오리진 액세스 신분을 사용해야 한다는 것이다.
- IAM 역할을 이용해 S3 Bucket에 액세스한 뒤 버킷 정책이 이 역할의 액세스를 허용하면 파일을 CloudFront로 전달하게 되는 것이다.
- 이는 브라질의 상파울루나 뭄바이나 멜버른과 같은 다른 EdgeLocation에서도 작동한다.
- 즉, 전 세계의 모든 EdgeLocation이 S3 버킷에 캐시된 콘텐츠를 제공하는 것이다.
- 이런 방식을 통해 CloudFront는 CDN으로서 굉장히 유용하게 사용된다.



## 4. CloudFront - ALB or EC2 as an Origin

> Origin이 ALB 또는 EC2 인 경우를 알아보자!

![image-20220817235204789](../../assets/images/posts/2022-08-18-AWS CloudFront (1) - Intro/image-20220817235204789.png)

1. **EC2 Instance**

   - 보안 부분이 조금 달라진다.

   - EC2 인스턴스(들)는 HTTP를 통해 공용액세스가 가능하게끔 공용이어야 하며, 사용자들은 전세계에 퍼져있다.

   - 이들이 EdgeLocation에 접근하면 EdgeLocation은 EC2 인스턴스로 액세스할 것이다.

   - 그럼 위의 사진을 보다시피 SG(Security Group)을 거치게된다.
     - 따라서 보안그룹은 CloudFront EdgeLocation의 IP를 EC2 인스턴스내로 허용해야 한다.
       - 이를 위해서는 [이 웹사이트](http://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips)에서 찾을 수 있는 EdgeLocation의 공용 IP 목록이 있어야 한다

   - 즉, SG이 EdgeLocation의 모든 공용IP에 CloudFront가 EC2 인스턴스로부터 컨텐츠를 가져갈 수 있게끔 허용해야 한다.

2. ALB

   - ALB 에 대한 보안그룹이 있다.
   - CloudFront가 액세스할 수 있게 ALB는 공용이어야 하지만, 이제 백엔드 EC2 는 private 이어도 된다.
   - 따라서 EC2 의 SG 는 ALB 의 SG 를 허용해야 한다.
   - 공용 로케이션인 엣지 로케이션의 경우에는 공용 네트워크를 통해 ALB에 액세스해야 한다.
   - 즉, 우리들의 ALB 보안그룹은 엣지 로케이션의 공용 IP를 허용해야 한다.
   - 아키텍쳐는 다르지만, 개념은 위(EC2)와 동일하다.



CloudFront의 앞이나 뒤에서 S3나 ALB나 EC2를 위한 네트워크 보안을 이해해야 한다. CDN 으로서의 CloudFront에는 몇몇의 훌륭한 기능들이 있다.

1. 지리적 제한



## 5. CloudFront Geo Restriction

> CloudFront CDN 기능중 하나인 지리적 제한에 대해 알아보자



- 분산으로의 액세스에 제한을 둘 수 있다.
  - 화이트리스트
    - 이 리스트에 있는 허용된 국가의 사용자들만이 CloudFront에 접근 가능
  - 블랙리스트
    - 특정 국가 사용자들이 분배에 접근할 수 없도록 한다.
- 제 3자 회사의 지리적 IP데이터베이스를 이용해 국가들의 허용 여부가 결정된다.
  - 수신되는 IP와 리스트를 비교하여 국가를 알아내는 방식이다.
- 사용 예시
  - 특정 콘텐츠에 접근을 제한하는 저작권법이 있을때 이런 제한을 사용할 수 있다.
  - 규제 당국에 예를 들면 미국의 컨텐츠에 프랑스로부터의 액세스를 제한하고 있음을 증명할때 사용 가능
    - 프랑스사람들은 미국콘텐츠 못봄 (제한걸림)



## 6. CloudFront vs S3 Cross Region Replication

> CloudFront 와 S3 리전간 복제와의 차이점을 알아보자!

1. **CloudFront**
   - 세계적인 엣지 네트워크를 사용한다.
   - TTL에 맞춰 파일이 캐시된다. (TTL이 하루일수도 있음)
   - 전 세계에서 이용 가능해야 하는 정적인 콘텐츠에 적합하다. (넷플릭스)
   - 콘텐츠가 약간 오래되어도 괜찮은 경우에 사용할 수 있다고 보면 된다. (옛날 영화?)
   - 전 세계 대상
2. **S3 Cross Region Replication**
   - 복제가 일어나도록 할 각각의 Region에 설정되어야 한다.
   - 파일이 거의 실시간으로 업데이트 된다.
   - 읽기 전용이기 때문에 읽기 성능이 좋다.
   - 적은 수의 Region에서 짧은 지연 시간으로 사용이 가능해야 하는 동적인 콘텐츠에 적합하다.
   - 선택된 리전에 복제하는 용도

