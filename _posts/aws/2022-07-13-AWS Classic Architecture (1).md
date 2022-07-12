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

title: "[aws] Classic Architecture (1) - What Is The Time"
excerpt: "🚀 Classic Architecture, WhatIsTheTime"

categories: aws
tag: [aws, architecture]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Classic Architecture (1)

> 실제 옛날에 사용되었던 아키텍처를 구성해보자.
>
> 현재 많은 기업들이 사용하고 있는 현대적 웹 아키텍처 구조로 발전시켜보자.
>
> What Is The Time 라는 웹사이트를 만들어보며 실습을 진행해보자



## Section Introduction

- **이 솔루션 아키텍쳐들은 이 AWS 공부코스의 꽃이라고 할 수 있다.**
- 모든 기술들이 어떻게 동작하는지, 같이 살펴보는 시간을 갖는다.
- 여러 가지 샘플케이스를 통해 솔루션 아키텍처들을 살펴본다.
  - What Is The Time.com
  - MyClothes.com
  - MyWordPress.com
  - **Instantiating applications quickly (앱을 빠르게 구동시키는법?)**
  - Beanstalk (엘라스틱 빈스톡)



## Stateless Web App : WhatIsTheTime.com

- WhatIsTheTime.com 사이트는 현재 시간이 몇시 인지 사람들에게 알려주는 사이트이다.
- 데이터베이스가 필요하지 않다.
- 우리는 작게 시작하길 원하고 downtime을 받아들일 수 있다.  ***downtime: 시스템을 이용할 수 없는 시간**
- 다운타임을 제거할수록, 수직 및 수평적으로 확장할 필요가 생긴다.



## Stateless Web App : What time is it?

> 간단하게 시작해보자.

![image-20220713012547447](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713012547447.png)

- User 와 t2.micro EC2 가 있다.
- 사용자가 시간을 물어본다.
- 17:30분이라고 답한다.



- 해당 EC2 는 고정IP주소를 가지고있다. (Elastic IP Address)
  - 무슨 일이 생기면 재시작해도 IP가 변하지 않는 장점이 있다.
  - 탄력적 IP주소를 연결시킨다.



## Scaling vertically

> 해당 웹이 인기가 많아져서 사용자가 늘어났다.
>
> 수직확장을 하는 사례를 살펴보자.

![image-20220713012941388](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713012941388.png)

- 사용자가 많아졌다. (= 트래픽이 증가)
- t2.micro EC2 로는 부하를 처리하기 버거워 성능을 좀 더 큰것으로 교체한다.
  - **수직 확장** 이라고 한다.
  - **CPU, Memory 사용량 등을 근거로 판단**한다.
- t2.micro => m5.large 유형으로 교체를 원한다
- 인스턴스를 중지 시키고, 유형을 바꾸고, 그 후에 인스턴스를 다시 시작한다.
  - 탄력적IP 를 가지고 있기 때문에 동일한 IP를 가지게 되고, 사람들은 여전히 App에 접근가능하다.
  - m5.large 로 변경하는 동안 downtime이 발생
  - 사용자들은 좋아하지 않는다. (해결은 됬으나 잘된 케이스가 아니다.)



## Scaling horizontally (1)

> 해당 웹이 인기가 더욱 많아져서 사용자가 대폭 증가했다.
>
> 이제는 **수평 확장**을 해야 할 때이다.

![image-20220713013544176](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713013544176.png)

- 이 m5.large EC2 는 하나의 public IP를 가지고 있고, Elastic IP가 연결되어 있다.
- 많은 User 가 유입되어, 모두들 현재 시간을 요청한다.
- 수평 확장을 진행한다.
  - 모두 m5.large EC2
  - 이것들 모두 탄력적IP가 연결되어 있다.
- 즉, **3개의 EC2, 3개의 ElasticIP** 가 생기게 된다.
- User들이 EC2 들과 통신하려면, 이 3개의 ElasticIP의 정확한 값을 알고 있어야 한다.
  - 한계가 생긴다.
  - User들은 점점 더 많은 IP를 알아야하는 번거로움이 생긴다.
  - 우리는 더 많은 인프라를 관리해야 되는 일이 발생한다.



## Scaling horizontally (2) - Route53

> 수평확장을 그대로 하되, ElasticIP 를 제거한다.
>
> 많아질수록 관리하기 어렵기 때문이다.
>
> **Elastic IP는 한 계정에서 Region 마다 5개**까지 가질 수 있다.
>
> Route53 을 이용하자!

![image-20220713014223009](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713014223009.png)



- Elastic IP 를 제거하고, Route53 을 활용한다.
- Route53을 이용해 api.whatisthetime.com 의 URL 을 설정했다.
- TTL 은 1시간으로 설정하고, A record 로 설정
- **A record 로 설정했다는건, DNS 로부터 IP리스트를 받는다는 의미**이다.
  - Route53 의 A record 는 IP 를 연결시켜준다



- User 들이 Route53 에게 Query 한다.
- User 들은 IP 주소들을 얻게 된다.
- 이는 시간에 따라 변하고, Route53 이 업데이트될 것이니, 전혀 문제가 되지 않는다.
- User 들은 EC2 인스턴스에 접근할 수 있게 된다.
- 관리할 Elastic IP 도 더이상 존재하지 않게 된다.
- 즉, **Route53 을 사용하여 상당한 개선을 이루었다.**



## Scaling horizontally (3) - adding and removing EC2 Instance

> 이번에는, 상황에 따라 즉시 인스턴스를 추가하고, 제거할 수 있도록 확장하고 싶어졌다.

![image-20220713020603229](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713020603229.png)

- 가장 위쪽 EC2 제거하게되면, 위쪽 사용자들이 이 m5.large EC2 와 통신중이었는데 사라졌다.
- TTL이 1시간이었기 때문에 Route53 에 Query하면 동일한 응답을 1시간동안 받게 된다.
- 따라서, 사용자들이 1시간동안 그 인스턴스에 접속하려 하지만, 인스턴스가 사라져서 존재하지 않는 상태이다.
- User들이 1시간동안 인스턴스에 접속을 못하는 상황이 발생한다.
  - 1시간 이후에는, 다시 접속이 가능하겠지만, 이는 바람직하지 않은 방법
  - 우리의 App이 다운되었다고 생각할 것이기 때문이다.



## Scaling horizontally (4) - with a load balancer

> 로드 밸런서를 추가하여 위의 상황을 해결해보자.

![image-20220713021114384](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713021114384.png)

- Public EC2 는 이제 더이상 존재하지 않는다.
- Private EC2 가 존재하게 된다.
- 이들을 같은 가용영역(AZ) 에서 실행시킨다.
- 3개의 m5.large EC2 가 있다.
- 위와 같이 구성하면, ELB 는 공개되겠지만 private EC2 는 뒤에 숨어있게 된다.
- ELB 에는 Health Check 기능도 제공한다.
  - 한 EC2 가 다운되거나 작동하지 않으면 해당 EC2 로 트래픽을 전송하지 않는다.
- SG (Security Group) 을 활용하여, 이 둘 사이의 트래픽을 제한하게 된다.



- Alias Record (별칭 레코드) 를 사용하여 ELB 와 연결한다.
  - 로드 밸런서가 IP주소를 지속적으로 바꾸기 때문에 A record 를 사용할 수 없다.
  - alias record 를 사용하면 route53 으로부터 ELB를 가리키게 될 것이다.
- 사용자들은 이제 Route53에 DNS Query를 하여 ELB 의 주소를 얻습니다.
- User들은 ELB에 접속하고, ELB는 EC2 인스턴스로 리다이렉트 시킨다.
  - 트래픽의 균형을 잡게 된다.
  - 로드밸런서로 이 인스턴스들을 추가 및 제거하고 정렬할 수 있어진다.
  - Health Check 기능 덕분에 사용자들에게 downtime 도 없어진다.



- 단점
  - 수동으로 인스턴스를 추가하고 제거하는것은 어렵다.
  - 해당 AZ에 지진이 발생하여 다운되면 앱을 사용할 수 없게된다. (단일 AZ 사용중이기 때문)
- 해결
  - ASG (Auto Scaling Group) 을 활용한다.



## Scaling horizontally (5) - with an Auto Scaling Group

> ASG 오토스케일링 그룹을 사용하여 위의 문제점을 해결하자.

![image-20220713021926100](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713021926100.png)

- 이번에는 ASG 이 private EC2 을 관리하게 한다.
- 즉, 기본적으로 ASG이 요청에 따라 확장하도록 한다. (트래픽이 많아지면 확장, 적어지면 축소)
- App이 downtime 이 사라지고, ASG 과 ELB 로 인해 아키텍처가 상당히 안정적이 되었다.



- 지진이 발생하여, 가용영역(AZ) 1번이 다운되었다.
  - 우리의 App도 완전히 다운된다.
  - 사용자들이 불만을 겪는다.
- 가용성을 높이려면 다중AZ 사용을 추천한다.



## Making our App multi-AZ

> 다중AZ 을 활용하여 재난에 대비하자.

![image-20220713022606883](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713022606883.png)

- AZ1, AZ2, AZ3 에 각각 2개, 2개, 1개의 EC2 인스턴스가 있다.
- AZ1 가 다운되더라도, AZ2 AZ3 이 있기 때문에 트래픽을 처리할 수 있게 된다.
- 앱을 Multi AZ 로 만들었고, 높은 가용성을 확보했다.
- 장애 발생에도 대비가 되었다.



## 더 개선할 여지가 있는지 찾아보자

![image-20220713023015725](../../assets/images/posts/2022-07-13-AWS Classic Architecture (1)/image-20220713023015725.png)

- 2개 의 AZ가 있다.
- 각각의 AZ 에는 최소 1개 이상의 EC2 가 실행중
- 용량을 예약하면 어떨까?
- App의 비용을 줄이는것부터 시작한다.
- 1년 내내 2개의 EC2 가 항상 실행될 것이기 때문이다.



- ASG 의 용량을 최소화하기 위해 인스턴스를 예약함으로써 미래에 상당한 **비용절감**을 할 수 있다.
- 새로운 EC2가 실행되더라도, 일시적이며, 트래픽에 따른것은 괜찮다.
- 극단적으로 비용을 절감하기 위해 **스팟 인스턴스**를 사용할 수도 있다.



## Summary

> 이번 포스팅의 핵심 정리

극히 작은 아키텍처부터 다중AZ 를 설정하기 까지 진행된 것을 이해할 수 있어야 한다.<br>이 것이 데브옵스 개발자, 솔루션 아키텍트로서 우리가 나아가야 할 방향이다.

요구사항이 무엇인지 이해하고, 이 요구사항에 어떻게 대응해야 하는지 알아야한다.



- 정리
  - EC2 인스턴스가 public IP와 private IP를 갖는 목적
  - Elastic IP vs Route53 vs ELB 의 사용할때 장/단점 및 차이
  - Route53 TTL, A record, Alias record 차이 및 별칭레코드와 로드밸런서 사용
  - EC2 를 수동으로 관리하는것과 ASG 이 관리하는것 차이
  - 재난에서 살아남기 위한 다중AZ 설정
  - ELB Health Check를 통해 죽은서버로 트래픽 안가게 막는 설정
  - EC2 가 ELB 로부터의 트래픽만 받도록 보안 그룹 규칙을 설정
  - 비용절감을 위한 용량 예약 (항상 2대의 EC2 실행 시, 예약하면 비용 절감 가능)



- AWS 에서의 좋은 아키텍처
  - 비용
    - 수직확장, 수평확장, ASG, 인스턴스 예약
  - 성능
    - 수직 확장, ELB, ASG
  - 신뢰성
    - 트래픽 안정적 전달, Route53, ELB, ASG, Multi AZ
  - 보안
    - SG
  - 운영
    - 수동프로세스 => ASG 완전 자동화



