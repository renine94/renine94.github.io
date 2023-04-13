---
layout: single

header:
  teaser: /assets/images/logo/spring.png
  overlay_image: /assets/images/logo/spring.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[spring] 스프링 JPA 객체지향 쿼리언어 JPQL 고급 - 페치 조인 2 한계"
excerpt: "🚀 spring, JPA, JPQL, 페치조인, 성능최적화"

categories: spring
tag: [spring, model, jpa, jpql, join, fetch]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# 객체지향 쿼리 언어9 Advanced - 페치 조인 2 한계

- 경로표현식
- 페치 조인 1 - 기본
- **페치 조인 2 - 한계**
- 다형성 쿼리
- 엔티티 직접 사용
- Named 쿼리
- 벌크 연산

<br><br>



# TL; DR

- `@BatchSize(size = 100)`
- 1 쪽에서 N 개를 조회할 때, 페치조인.. 사용 조심 (OneToMany)
- 글로벌 세팅 `hibernate.default_batch_fetch_size`





## 01. 페치조인 특징과 한계

- 페치 조인 대상에는 별칭을 줄 수 없다.
  - 하이버네이트는 가능, 가급적 사용X
- 둘 이상의 컬렉션은 페치 조인 할 수 없다.
- 컬렉션을 페치 조인하면 페이징 API 를 사용할 수 없다.
  - setFirstResult
  - setMaxResults
  - 일대일, 다대일 같은 단일 값 연관 필드들은 페치 조인해도 페이징 가능
  - 하이버네이트는 경고 로그를 남기고 메모리에서 페이징 (매우 위험)



## 02. 페치 조인 - 정리

- 모든 것을 페치 조인으로 해결할 수는 없음
- 페치 조인은 객체 그래프를 유지할 때 사용하면 효과적
- 여러 테이블을 조인해서 엔티티가 가진 모양이 아닌 전혀 다른 결과를 내야 한다면, 페치 조인 보다는 일반 조인을 사용하고 필요한 데이터들만 조회해서 DTO로 반환하는 것이 효과적









































