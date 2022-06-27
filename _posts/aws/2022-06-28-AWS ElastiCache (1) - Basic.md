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

title: "[aws] ElastiCache (1) - Overview"
excerpt: "🚀 Cache, Redis, Memcached, RabbitMQ"

categories: aws
tag: [aws, rds, db, sql, aurora, advanced]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Amazon ElastiCache Overview

- RDS 와 동일한 방식으로 관계형 데이터베이스를 관리할 수 있다.
- ElastiCache는 Redis 또는 Memcached 와 같은 캐시 기술을 관리할 수 있다.
- 캐시란, 높은 성능과 낮은 지연 시간을 가진 In-Memory DB 이다.
- ElastiCache를 사용하면, Read 집약적인 워크로드의 부하를 줄이는데 도움이 된다.
- 일반적인 쿼리가 캐시 되어 DB가 매번 쿼리되지 않는 것을 의미한다.
- 캐시는 이러한 쿼리의 결과를 검색할 때 사용할 수 있다.
- App의 상태를 ElastiCache에 저장해 App를 무상태(stateless)로 만들 수 있다.
- RDS 와 같은 장점을 갖기 때문에 AWS는 동일한 유지 보수를 수행한다.
  - 운영체제, 패치, 최적화, 설정, 구성, 모니터링, 장애 회복, 백업을 수행한다.
- ElastiCache를 사용할 때 App에 관한 몇 가지 어려운 코드 변경을 요청할 수도 있다.
  - 단순히 활성화를 시키는것이 아니라 진짜로 캐시를 사용해야 한다.
  - 데이터베이스 쿼리 전과 후에 캐시를 쿼리하도록 App의 코드를 변경해야 한다.



## ElastiCache Solution Architecture - DB Cache

![image-20220628014124840](../../assets/images/posts/2022-06-28-AWS ElastiCache (1) - Basic/image-20220628014124840.png)

- ElastiCache, RDS, APP 이 있다.
- App은 Cache에 Query 한다.
- query가 이미 생성됬는지, 이미 생성되어 cache에 저장되있는지 확인하는것은 Cache Hit 캐시히트이다.
- 이는 cache에서 바로 응답을 얻어서 쿼리하기 위해 DB 로 이동하는 시간을 줄여준다.
- cache miss 캐시미스의 경우에는 DB에서 데이터를 가져와서 DB에서 읽습니다.
- 동일한 쿼리가 발생하는 다른 App이나 Instance에서는 데이터를 cache에 다시 기록하여<br>다음에는 같은 쿼리로 Cache Hit 를 얻도록 합니다.
- RDS DB에 부하를 줄이는데 도움을 준다.
- 데이터를 캐시에 저장하기 때문에 캐시 무효화 전략이 있어야 한다.
- 가장 최근 데이터만 사용하는지 확인해야 한다.
  - 이것이 캐싱 기술 사용과 연관된 어려움(단점) 이다.



## ElastiCache Solution Architecture - User Session Store

![image-20220628022747719](../../assets/images/posts/2022-06-28-AWS ElastiCache (1) - Basic/image-20220628022747719.png)

- 사용자 세션을 저장해 애플리케이션을 무상태로 만드는 것
- 사용자가 애플리케이션의 모든 계정에 로그인하면 App이 Cache에 세션데이터를 기록
- 사용자가 App의 다른 Instance로 리다이렉션되면 App은 cache에서 직접 세션 캐시 검색
- 그래서 사용자는 계속 로그인한 상태로 한 번 더 로그인 할 필요가 없다.
- 사용자의 세션 데이터를 cache에 기록해서 App을 무상태(stateless)로 만드는 것



## ElastiCache - Redis vs Memcached

> 레디스와 멤캐시드 차이 비교

![image-20220628022846974](../../assets/images/posts/2022-06-28-AWS ElastiCache (1) - Basic/image-20220628022846974.png)



- 레디스
  - 자동 장애 조치 다중 AZ를 수행하는 기술
  - 읽기 전용 Replica는 읽기 스케일링에 사용되며, 고가용성을 가진다.
  - 지속성으로 인해 데이터 내구성도 있다.
  - 백업과 기능복원도 있다.
  - RDS와 많이 유사하다.
- 멤캐시드
  - 데이터 분할에 다중노드를 사용하고 이를 **샤딩(sharding)** 이라고 합니다.
  - 가용성이 높지않고, 복제도 발생하지 않는다.
  - 지속적인 캐시가 아닙니다.
  - 백업과, 기능복원도 없다.
  - 다중 스레드 아키텍처로, 몇몇 샤딩과 함께 캐시에서 함께 실행되는 여러 인스턴스가 있다.
- 정리
  - 레디스는 고가용성, 백업, 읽기전용 Replica가 있다.
  - 멤캐시드는 데이터를 손실할 수 없는 단순한 분산 캐시이다.
  - 가용성이 높지 않고, 백업과 기능복원도 없다.



이것이 바로 두 기술의 가장 큰 차이점이다.