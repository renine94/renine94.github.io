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

title: "[aws] Global Accelerator (1) - Intro"
excerpt: "🚀 Global Accelerator, Intro"

categories: aws
tag: [aws, global, accelerator, unicast, anycast, ip, cloudfront]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

## 01. Global users for our application

![image-20220825011941014](../../assets/images/posts/2022-08-25-AWS Global Accelerator (1) - Intro/image-20220825011941014.png)

- 현재 App을 배포한 상태이며, 이는 글로벌 애플리케이션이고, 글로벌 사용자들이 직접 접근하려고 하는 상황
- 그러나 우리의 애플리케이션은 오직 한 Region에 배포되어 있다.
- 예를들어, 인도에서 public ALB 를 배치한 상태이고, 반면에 사용자들은 전 세계에 걸쳐 있다.
  - 미국에도 있고, 유럽과 오스트레일리아에도 있다.
- 사용자들이 애플리케이션에 접근할 때 공용인터넷을 통하게 되는데 라우터를 거치는 동안의 수 많은 홉으로 인해 상당한 지연이 발생할 수 있다.
  - 이 수 많은 홉들은 위험요소가 될 수 있다. 연결이 끊길 수 있기 때문이다.
  - 또한 지연시간도 발생한다.
  - AWS Infra에 최대한 직접적으로 접근하는 것도 아니다.
- 따라서 지연시간을 최소화하기 위해 최대한 빨리 AWS 네트워크를 통하는 것이 좋다.
- **이를 위해 Global Accelerator 를 사용하게 된다.**





## 02. Unicast IP vs Anycast IP

> Global Accelerator 를 이해하기위해선 유니캐스트와 애니캐스트 IP 개념을 이해해야 한다.

- Unicast IP
  - 하나의 서버가 하나의 IP주소를 가진다.
  - 클라이언트가 두 개의 서버와 통신할 때 왼편 서버의 IP주소는 12로 시작하고, 오른쪽은 98로 시작한다.
  - 12로 시작하는 IP주소를 참조한다면 왼편의 서버로 연결되고 반대편IP를 사용하면 오른편의 서버로 연결될 것
- Anicast IP
  - 모든 서버가 동일한 IP주소를 가진다.
  - 클라이언트는 가장 가까운 서버로 라우팅된다.
  - 직관적이진 않지만 아래사진처럼 동작한다.

![image-20220825012252367](../../assets/images/posts/2022-08-25-AWS Global Accelerator (1) - Intro/image-20220825012252367.png)



**그리고, Global Accelerator 는 이 Anycast IP 개념을 사용한다.**



# AWS Global Accelerator

- 애플리케이션을 라우팅하기 위해 AWS 내부 글로벌 네트워크를 활용한다.
- 사용자들이 전세계에 있고 우리는 인도로 라우팅 하고 싶어한다.
- 그리고 미국의 공용 인터넷을 거쳐서 보내는 대신에 가장 가까운 EdgeLocation과 통신할 것
- EdgeLocation으로부터 내부 AWS네트워크를 거쳐 ALB로 곧장 연결된다.
- 오스트레일리아도 동일, 오스트레일리아 인근 EdgeLocation으로 가서 Private AWS 네트워크를 거쳐 ALB에 도달
- 즉, 요점은 Anycast IP를 사용한다는 것이다.
- 사실, 애플리케이션을 위해 두 개가 생성되는데 둘 다 글로벌하다.
- 그리고 anycast IP는 사용자와 가장 가까운 EdgeLocation으로 트래픽을 직접 전송한다.

![image-20220825013118551](../../assets/images/posts/2022-08-25-AWS Global Accelerator (1) - Intro/image-20220825013118551.png)

이것이 anycast IP의 장점이다. 그러면 EdgeLocation은 훨씬 안정적이고 지연 시간이 적은 Private AWS 네트워크를 거쳐  ALB 로 트래픽을 전송한다.



Global Accelerator는 어떤 애플리케이션에 대해서도 전 세계의 유저들에게 두 개의 고정 IP주소를 제공할 수 있도록 해준다는 점에서 매우 독특하다.



---

- 탄력적IP, EC2, ALB, NLB, public or private 과 함께 작동한다.
- 네트워크를 거치기 때문에 안정적인 성능을 보여준다.
  - 지능형 라우팅으로 지연시간이 가장 짧은 EdgeLocation 으로 연결되며, 뭔가 잘못될 경우에는 신속한 리전 장애조치가 이루어질 것이다.
  - 아무것도 캐시하지 않기에 클라이언트 캐시와도 문제가 없다.
  - 우리가 사용하는 두 개의 anycast IP는 변하지 않습니다.
  - EdgeLocation 다음에 내부 AWS 네트워크가 오기 때문이다.
- 상태 확인 (Health Check)
  - Global Accelerator 는 우리의 어플리케이션에 대해 헬스체크를 수행한다.
  - 애플리케이션이 글로벌한지도 확인한다. 한 Region에 있는 한 ALB에 대해 상태확인 실패하면 자동화된 장애 조치가 1분 안에 정상 엔드포인트로 실행된다.
  - 상태확인 덕분에 재해 복구에도 뛰어나다.
- 보안(Security)
  - 단 두 개의 외부 IP만 존재하기 때문에 보안측면에서도 매우 안전하다.
  - Global Accelerator 를 통해 DDos 보호도 자동으로 받게 된다.
    - 보안 섹션에서 살펴볼 AWS Shield 덕분이다.



## Global Accelerator vs CloudFront

> 두 서비스의 차이를 비교해보자

- 두 서비스 모두 AWS 글로벌 네트워크를 사용하며, 둘 다 AWS가 생성한 전 세계의 EdgeLocation 을 사용
- 두 서비스 모두 DDos보호를 위해 AWS Shield 와 통합된다.



- **CloudFront**
  - 캐시가능한 컨텐츠 (이미지 or 비디오) 를 위한 퍼포먼스 향상에 적합하다.
  - 동적 컨텐츠 (API 가속 또는 동적 사이트 전달) 동적 내용 모두에 대해 성능을 향상시킨다.
  - 이러한 내용(콘텐츠)들은 EdgeLocation 으로부터 제공된다. (서빙된다)
    - 따라서 EdgeLocation은 가끔 한번씩 Origin로부터 Content를 가져올 것이다. (캐싱하기 위해)
  - 대부분의 경우 CloudFront는 캐시된 내용을 Edge로부터 가져와서 전달한다.
    - 즉, 사용자들은 엣지로부터 내용을 받는 것이다.
- **Global Accelerator**
  - TCP or UDP 상의 다양한 애플리케이션 성능을 향상시킨다.
  - 패킷은 EdgeLocation으로부터 하나 이상의 AWS Region에서 실행되는 애플리케이션으로 프록시된다.
  - 모든 요청이 애플리케이션쪽으로 전달된다.
  - 캐싱은 불가능하다.
  - 게임이나 IoT 또는 Voice over IP 같은 비HTTP 를 사용할 경우에 매우 적합
  - 글로벌하게 고정 IP를 요구하는 HTTP를 사용할떄도 유용하다
  - 결정적이고 신속한 리전장애조치가 필요할떄도 좋다.

