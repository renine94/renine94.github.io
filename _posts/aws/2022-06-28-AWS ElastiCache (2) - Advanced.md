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

title: "[aws] ElastiCache (2) - Advanced"
excerpt: "🚀 Cache, Redis, Memcached, Security, Patterns, UseCase"

categories: aws
tag: [aws, cache, redis, memcached, elasticache]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# ElastiCache - Cache Security

> 캐시 보안을 알아보자

![image-20220629014159919](../../assets/images/posts/2022-06-28-AWS ElastiCache (2) - Advanced/image-20220629014159919.png)

- ElastiCache 의 모든 캐시들 (redis, memcached)
  - IAM 인증을 지원하지 않는다.
  - 캐시에서 IAM 정책은 AWS API 수준 보안에만 사용된다.
- Redis Auth
  - 레디스 인증을 하려면 Redis Auth를 사용해야 한다.
  - Redis Cluster 를 생성할때, password 또는 token 을 설정할 수 있다.
  - 캐시에 들어갈 때 비밀번호를 사용할 수 있게 된다.
  - 캐시에 사용할 수 있는 보안그룹에 대한 추가적인 수준의 보안이다.
  - 전송 중 암호화를 위해 SSL 보안을 지원할 수 있다.
- Memcached
  - SASL 기반의 인증을 지원한다. (좀더 높은 보안수준)
    - 고급 종류의 인증 매커니즘



EC2 Instance 자체 보안그룹(SG)도 Redis에 Acces할 수 있는 자체 보안 그룹이 있다.<br>그래서 일라스틱 캐시를 사용하면 보안그룹 수준의 보안을 수행할 수 있다.<br>또한 인증을 위해 Cache에서 Redis 종류의 캐시를 사용할때 Redis Auth를 가질 수 있다.



## Patterns for ElastiCache

> 일라스틱 캐시에서 데이터를 불러오는 패턴 3가지를 알아보자

![image-20220629014213313](../../assets/images/posts/2022-06-28-AWS ElastiCache (2) - Advanced/image-20220629014213313.png)

- **Lazy Loading**
  - 모든 읽기 데이터는 캐시되고, 데이터가 캐시에서 부실해질 수 있다.
  - Cache에 캐시가 히트하면 App이 Cache로부터 데이터를 받는다.
  - 만일 Cache 미스가 있으면 DB에서 데이터를 읽고 Cache에 저장시킨다.
  - 캐시 히트가 없을때만 발생하기 때문에 Lazy Loading 이라고 한다.
- Write Through
  - DB에 Write 할때 캐시에서 데이터를 추가하거나 업데이트 하는 것
- Session Store
  - **캐시를 세션저장소로 사용가능**하다. (TTL 속성으로 세션을 만료시킬 수 있다.)
  - TTL (Time to Live)





## ElastiCache - Redis Use Case

> Redis 사용사례

![image-20220629014939481](../../assets/images/posts/2022-06-28-AWS ElastiCache (2) - Advanced/image-20220629014939481.png)

- 게임 리더보드 생성에 대한 것
  - 게임 어느 시점에 누가 1위고 2위고 3위인지 가려내는 개념
  - **일종의 Ranking 시스템**
- 레디스 자료구조중 **고유성과 요소 순서를 모두 보장하는 Sorted Set 자료형을 사용**하게 된다.
- 요소가 추가될 때마다 실시간으로 순위가 매겨진 다음 올바른 순서로 추가된다.
  - Redis Cluster 가 있는 경우 실시간으로 1위, 2위, 3위 플레이어가 있는 실시간 리더보드를 생성한다는 개념
  - 모든 Redis Cache는 동일한 리더보드를 사용할 수 있다.
  - 즉 Redis로 Amazon ElastiCache 와 통신할 때 클라이언트는 실시간 리더보드에 액세스할 수 있고<br>App측에서는 이 기능을 프로그래밍할 필요가 없다.
  - 실시간 리더보드에 액세스 하기 위해 Redis의 Sorted Set 자료형을 사용하면 된다.



