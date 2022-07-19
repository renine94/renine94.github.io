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

title: "[aws] Classic Architecture (2) - MyClothes.com"
excerpt: "🚀 Classic Architecture, MyClothes.com, Commerce, App"

categories: aws
tag: [aws, architecture, commerce]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Stateful Web App - MyClothes.com

> 이전 포스팅에서는 Stateless(무상태) 웹 어플리케이션 WhatIsTheTime.com 을 다루었다.
>
> 단순히 시간을 알려주고, 이를 위한 어떠한 DB나 정보 또는 외부 정보가 필요없었다.
>
> - **이번 포스팅에서 다루게 될 내용**
>   - 상태 유지 웹 어플리케이션인 MyClothes.com 웹사이트를 만들어보자.
>   - 사람들이 온라인으로 옷을 살 수 있게 해주고, 장바구니 기능이 있다.
>   - 동시에 수백만명의 사용자가 이용중이다.
>   - 확장 가능해야 하며, 수평 확장성을 유지한다.
>   - App의 웹 티어를 최대한 무상태(stateless)로 유지하고 싶다.
>   - 장바구니 상태가 존재하지만, 웹 App을 최대한 쉽게 확장할 수 있어야 한다.
>     - 사용자들이 웹을 둘러볼 때 장바구니를 잃어버리면 안된다는 뜻
>   - 주소 나 사용자의 정보를 DB에 저장시킨다.



---

![image-20220714023058953](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220714023058953.png)

- 이전 포스팅과 같은 종류의 아키텍처가 있다.
- User, Route53, Multi AZ, ELB, ASG, 등으로 구성되어 있다.
- App이 ELB에 접근하고, ELB는 어떤 인스턴스에 트래픽을 주고받을 지 정해준다.
- **장바구니를 생성하고, 그 다음 요청은 같은 EC2 인스턴스가 아니라 다른 EC2 인스턴스로 간다.**
  - 그러면 장바구니가 사라지게 된다.
  - 사용자는 버그로 착각하고, 다시 장바구니를 담고, 이번에는 3번째 EC2 로 리다이렉션 된다.
  - 또 다시 장바구니가 사라지게 된다.
  - 사용자 불편을 야기한다. 장바구니가 자꾸 사라지게 느껴지게 된다.
  - 고객 이탈로 이어진다.





- 해결법
  - 고착도, 즉 **세션 밀접성을 도입** (Session Sticky)
  - 사용자 **쿠키**를 사용한다.
  - **NoSQL** 사용 (redis, dynamoDB)
  - **DB** 사용

아래에 하나하나 설명해보도록 한다.



## Stickiness (Session Affinity)

> 세션 밀접성을 도입하여, 장바구니에 담은 물건들이 사라지지 않게 해보자

![image-20220720005003197](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720005003197.png)



- ELB 의 기능중 하나인 **Session Stickiness** 를 활성화 한다.
- 첫번째 사용자가 인스턴스에 접속하여 뭔가를 장바구니에 담는다.
- 두번째 요청도 동일한 인스턴스로 가게되고, 세번 째 요청 또한 마찬가지로 같은 인스턴스로 가게된다.



모든 요청이 고착도 덕분에 동일한 인스턴스로 가게 될 것이다.<br>다만, EC2 인스턴스가 어떤 이유로든 종료가되면 장바구니를 잃어버리게 된다.

다만 고착도와 세션 밀접성 덕분에 조금은 개선되었다.<br>또 다른 접근 방법인 **사용자 쿠키**를 사용하여 이 문제를 다시 해결해보자.



## User Cookies

![image-20220720005318513](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720005318513.png)



EC2 인스턴스가 장바구니 내용을 저장하는 대신, **사용자쪽에서 장바구니 내용을 저장**하도록 하는 것이다.

- 로드 밸런서에 접속할 때마다 "내 장바구니에는 이런 것들이 있다." 라고 말하는 것이다.
- 웹 쿠키를 통해 이루어진다.
- 첫번째 EC2 or 두번째, 세번째 EC2 에 접속하더라도, 사용자가 직접 EC2 인스턴스로 장바구니 내용을 보내주기 때문에 각각의 서버가 장바구니의 내용을 알 수 있게 됩니다.
- 각각의 EC2 인스턴스가 이전에 있었던 일을 알 필요가 없는 무상태 가 되었다.
- 이전에 있었던 일은 사용자(클라이언트)쪽에서 말해주게 될 것이다.



- 단점
  - HTTP 요청이 점점 더 무거워지게 된다.
  - 웹 쿠키를 통해 장바구니 내용을 보낼 때, 장바구니에 뭔가를 추가할수록 점점 더 많은 데이터를 보내기 때문
  - 쿠키가 공격자에 의해 변경됨으로써 사용자 장바구니가 갑자기 수정될 수 있다. (보안 위험 존재)



- 해결법
  - EC2 인스턴스가 사용자 쿠키의 내용을 검증해야 한다.
  - 전체 쿠키의 크기는 4KB 이하까지만 가능해 쿠키 내에는 작은 정보만 저장 가능
  - 대량의 데이터셋은 저장할 수 없다.



쿠키를 사용하는 아키텍처는 실제로 많은 웹 어플리케이션 프레임워크에서 실제로 사용하는 패턴이다.<br>그러나, 서버 Session 개념을 도입하여 다시한번 해결해보자!



## Server Session

![image-20220720005903188](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720005903188.png)



- 전체 장바구니를 웹 쿠키로 보내는 대신에 단순히 세션ID 만 보낸다.
- 사용자에 대한 Session ID 이다.
- 백그라운드에는 ElastiCache 클러스터가 존재한다.
- session_id 를 보낼 때 EC2 인스턴스에게 "이 물건을 장바구니에 추가한다." 라고 말한다.
- 그러면 EC2 인스턴스는 장바구니 내용을 ElastiCache에 추가하고, 이 장바구니 내용을 불러올 수 있는<br>ID 가 바로 session_id 가 된다.
- 사용자가 session_id 와 함께 두번째 요청을 보내면 이는 다른 EC2 인스턴스로 가게되고, 그 EC2 인스턴스는<br>session_id 를 사용하여 ElastiCache 로부터 장바구니 내용을 찾아서 Session Data를 불러올 수 있게된다.
- 마지막 요청에 대해서도 동일한 패턴이다.



ElastiCache 의 또다른 장점은 속도가 매우 빠르다는 것이다.<br>세션 데이터 저장의 또 다른 방식으로는 DynamoDB (NoSQL) 가 있고, 저 DB 에 저장시켜도 무방하다.

ElastiCache 가 정보의 출처이고 공격자들은 ElastiCache의 내부를 수정할 수 없기 때문에 훨씬 안전해졌다.<br>실제로 많이 사용되는 안전한 패턴이다.

이제 마지막 DB 에 저장하는 방법을 알아보자



## User Data in Database

![image-20220720010654545](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720010654545.png)



- 사용자 데이터를 데이터베이스에 저장하려고 한다.
- 사용자 주소, 등 개인정보를 저장하고자 한다.
- 다시한번 EC2 인스턴스와 통신할텐데, 이번에는 RDS 인스턴스와 통신한다.
- RDS 는 장기적인 저장을 위한 것이라 좋다.
- 각각의 EC2 인스턴스가 RDS 와 통신할 수 있게 된다.



## Scaling Read

![image-20220720011315347](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720011315347.png)

- 사용자가 늘어나고, 대부분의 시간을 웹사이트를 둘러보며 보낸다.
- 대부분 Read 의 행위를 많이 행하기 때문에 읽기를 확장해야 한다.
  - Write 를 하는 RDS 마스터를 사용하고,
  - Replica가 일어나는 RDS Read Replica를 사용할 수 있다.
- 즉, 뭔가를 Read할때는 Read Replica RDS 인스턴스로 요청을 보내서 처리하도록 한다.
- RDS 에서는 5개 의 Read Replica 복제본을 가질 수 있다.
- 이는 RDS DB의 Read를 확장할 수 있도록 해준다.



## Scaling Read (Alternative) - Write Through

> Cache 를 사용하는 쓰기모드도 있다.

![image-20220720011503408](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720011503408.png)

- 데이터를 Read할때, Cache를 먼저 읽어서 정보가 있는지 확인하여, 있으면 Cache Hit 하고,<br>없으면 Cache miss 한다.
- 이때 Cache Miss가 일어날때, RDS 로부터 읽어 들여서 Cache에 저장시킨다.
- 이번에는 ElastiCache와 통신할 때 정보를 얻게 되고 Cache Hit 가 된다.
  - 즉시 응답을 받을 수 있다.
  - RDS 상의 트래픽을 줄일 수 있다.
  - RDS 의 CPU 사용량을 줄이고, 동시에 성능을 향상시킬 수 있게 된다.
- Cache 유지보수가 필요해진다.
  - 꽤 어려운 작업이며, App내에서 이루어져야 한다.



이제 우리의 애플리케이션은 확장이 가능하고, 꽤 많은 읽기 작업이 있습니다.



## Survive Disasters

> 재해에 대비해야 한다.

![image-20220720011837055](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720011837055.png)



재해로 인한 피해를 받지 않으려면 어떻게 해야 할까?

사용자가 Route53과 통신을 하는데, 이제 우리는 Multi AZ ELB가 있다.<br>그런데 Route53 은 이미 가용성이 높다. 무언가를 더 할 필요가 없다

- ELB 를 Multi AZ로 만든다.
- ASG 도 Multi AZ
- RDS 역시 Multi AZ 기능이 있다.
- 재해가 발생할 경우 인계받을 수 있는 대기 복제본이 있다.
- Redis 를 사용한다면 ElastiCache도 Multi AZ 기능을 가지고 있다.



## Security Group

> 보안그룹에 대해서도 안전해야 한다.

![image-20220720012147818](../../assets/images/posts/2022-07-14-AWS Classic Architecture (2)/image-20220720012147818.png)



- ELB 쪽 어디에서나 HTTP/HTTPS 트래픽을 열 수 있어야 한다.
- EC2 인스턴스 측면에서는 ELB 로부터 오는 트래픽만 받도록 제한한다.
- ElastiCache 측면에서는 EC2 보안그룹으로부터 오는 트래픽만 받도록 제안해야 한다.
- RDS 도 마찬가지로 EC2 보안그룹으로부터 오는 트래픽만 받도록 설정해야 한다.





# Summary

> 정리



- ELB Sticky Session 기능 사용
- Cookies 를 사용하여 stateless 무상태로 만들기
- ElastiCache
  - 세션을 저장하기 위해 (다이나모DB 사용도 가능)
  - RDS 로부터 데이터를 Caching
  - Multi AZ
- RDS
  - 유저 데이터 저장
  - 읽기 확장을 위한 Read Replica 사용
  - 재해에 대비하여 Multi AZ 사용
- 서로 참조하는 보안그룹을 위해 철저한 보안을 추가



클라이언트 / 웹 애플리케이션 / 데이터베이스 의 3개의 구조로 이루어져 있다.<br>이것은 매우 보편적인 아키텍처이다. 비용이 다소 증가하긴 했지만, 현대 웹 아키텍처 필수이므로 괜찮다.

- Multi AZ 를 원한다면 비용이 더 추가되지만 재해에 대비할 수 있다.
- 읽기를 확장하고 싶다면 비용을 추가하고 Read Replica 셋을 추가하도록 한다.

