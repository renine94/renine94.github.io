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

title: "[aws] Route53 (8) - Health Check"
excerpt: "🚀 Route53, Routing, Health Check, Monitor an Endpoint, Calculated Health Checks, Private Hosted Zones"

categories: aws
tag: [aws, route, health check]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Route53 - Health Check

> 상태 확인에 대해 알아보자.
>
> - Monitor an Endpoint
> - Calculated Health Checks
> - Private Hosted Zones

![image-20220706020313873](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706020313873.png)

- 상태 확인은 주로 public resource 에 대한 상태를 확인하는 방법

- private resource에서도 상태를 확인하는 방법 또한 존재한다.

- Health Check => DNS 의 장애 조치를 자동화하기 위한 작업

  - 3가지의 상태 확인이 가능하다.

    1. **공용 Endpoint 를 모니터링 하는 것 (App, Server, another AWS Resource)**

       - Monitor an Endpoint

    2. **다른 상태 확인을 모니터링하는 상태 확인도 있다. (계산된 상태 확인이라 불린다.)**

       - Calculated Health Checks

    3. **CloudWatch 경보의 상태를 모니터링하는 상태 확인도 있다.**

       - Private Hosted Zones

       - 제어가 쉽고, 개인 리소스들에 유용

- Health Check는 CloudWatch 지표와 통합될 수 있다.

  - 상태 확인들은 각자의 메트릭(지표) 를 사용
  - CloudWatch 의 지표에서도 확인이 가능





- 서로 다른 두 지역에 각 하나씩 로드밸런서가 존재
- 다중 Region 셋업
- Region Level 에서의 고가용성을 원하는 상황이다.
- Route53 을 이용해 DNS Records 를 만들고, mydomain.com 과 같은 URL 이용해 접속하면<br>유저는 가장 가까운 로드밸런서로 연결된다. (Latency-based)
- But.. 만약 한 지역이 사용 불가능 상태가 되면 그곳으로 유저를 보내면 안된다.
- 그러기 위해선 Route53 에서 Health Check를 생성해야 한다.





## Health Checks - Monitor an Endpoint

> 상태확인(health check)이 특정 Endpoint 에서 어떻게 작동하는지 알아보자.

![image-20220706021155356](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706021155356.png)



ALB 에 대한 eu-west-1 의 health check를 한다고하면, AWS의 health check가 전 세계로부터 올겁니다.<br>하나가 아니죠, 전 세계로부터 15개 정도의 health check가 옵니다.

- 우리가 루트를 설정한 공용 엔드 포인트로 모두 요청을 보낸다.
- 200OK 또는 우리가 정의한 코드를 받으면 resource는 정상으로 간주된다.
- 전세계에서 온 15개의 health check가 endpoint의 상태를 확인하고<br>임계값을 정상 혹은 비정상으로 설정한다.
- 간격도 설정 가능하다.
  1. 30초마다 정기적 확인
  2. 10초마다 정기적 확인 (비용이 더들고, 빠른 health check 가능)
- HTTP, HTTPS, TCP 등 많은 프로토콜 지원
- 18% 이상의 health check가 정상이라고 판단하면 Route53 도 이를 정상이라고 간주
- 그렇지않다면 비정상이라고 인식
- health check는 로드밸런서로부터 2xx, 3xx 코드를 받아야만 통과
- **health check는 텍스트 기반 응답일 경우, 응답의 처음 5,120byte 확인하여 응답자체에 해당 텍스트가 있는지 본다.**
- **health check가 가능하려면, health check가 우리의 ALB 나 Endpoint에 접근이 가능해야 한다.**
  - **Route53 Health Check 의 IP 주소범위에서 들어오는 모든 요청을 허용해야 한다.**
  - 이 주소 범위는 위 사진의 오른쪽 아래 링크에서 확인 가능



## Route53 - Calculated Health Checks

> 계산된 상태확인에 대해 알아보자.

![image-20220706022241591](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706022241591.png)	

- 여러 개의 Health Check result를 하나로 합쳐주는 기능
  - Route53에 EC2가 3개 있고, health check 를 3개 생성 가능하다.
  - 이들은  EC2 인스턴스를 하나씩 확인해 주는 **하위 상태확인(Child)** 이 될 것
  - 이 하위 상태확인을 바탕으로 **상위(parent) 상태확인**을 정의할 수 있다.
- 이 Health Check를 모두 합치기 위한 조건은 OR와 AND 또는 NOT 이다.
- 하위 상태확인을 256개까지 모니터링 가능
- 상위 상태 확인이 통과하기 위해 몇 개의 상태 확인을 통과해야 하는지도 지정할 수 있다.
- 사용사례
  - 상태 확인이 실패하는 일 없이 상위 상태 확인이 웹사이트를 관리 유지하도록 하는 경우



## Health Checks - Private Hosted Zones

> 개인 리소스의 상태 확인은 어떻게 하는 지 알아보자.

![image-20220706022731937](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706022731937.png)



- private resource 을 모니터링 하는것은 어려울 수있다.
- Route53 의 Health Check가 공용 웹에 있기 때문에 이들은 VPC 밖에 존재하게 된다.
- 그들은 private endpoint에 접근이 불가능하다.
- **CloudWatch 지표를 만들어 cloudWatch 알람을 할당하는 식으로 이 문제 해결 가능**
  - cloudWatch 경보를 상태 확인에 할당할 수 있다.
  - cloudWatch Metrix(지표)를 이용해 개인 subnet 안에 있는 EC2 인스턴스를 모니터링
  - Metrix(지표)가 침해되는 경우 CloudWatch 알람을 생성하게 된다.
  - **알람이 모두 ALARM 상태가 되면 health check는 자동으로 비정상이 된다.**
  - 이렇게하면, private resource에 대한 health check를 만든 것이나 다름없다.
  - 가장 흔히 사용되는 사례이다.





## 실습

![image-20220706023802216](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706023802216.png)



![image-20220706023835594](../../assets/images/posts/2022-07-06-AWS Route53 (8) - Health Checks/image-20220706023835594.png)



- 실패 임계값
  - 장애로 간주되기 전에 몇 번의 장애가 발생해야 하는지 설정
- 문자열 매칭 (String matching)
  - 응답의 앞 5,120바이트 부분을 먼저 검색하는지 안하는지 여부 체크