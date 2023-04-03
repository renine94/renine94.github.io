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

title: "[spring] 스프링 JPA 객체지향 쿼리언어 JPQL 고급 - 경로표현식"
excerpt: "🚀 spring, JPA, JPQL, 객체그래프 탐색, 연관테이블 데이터 탐색, Django비교 포스팅, 명시적&묵시적 조인"

categories: spring
tag: [spring, model, jpa, jpql, graph, join]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# 객체지향 쿼리 언어7 Advanced - 경로표현식

- **경로표현식**
- 페치 조인 1 - 기본
- 페치 조인 2 - 한계
- 다형성 쿼리
- 엔티티 직접 사용
- Named 쿼리
- 벌크 연산

<br><br>



# TL; DR

**그냥 명시적 조인을 쓰세요.**





## 01. 경로표현식

- `. (점)` 을 찍어 객체 그래프를 탐색하는 것

```sql
-- JPQL 표현식
SELECT 
	m.username -- 상태 필드
FROM 
	Member m
	Join m.team t  -- 단일 값 연관필드 (~~ToOne)
	join m.orders o -- 컬렉션 값 연관필드 (~~ToMany)
WHERE
	t.name = '팀A'
```



<br>

## 02. 경로표현식 용어 정리

- 상태필드
  - 단순히 값을 저장하기 위한 필드 (ex. m.username)
- 연관필드
  - 단일 값
    - `@ManyToOne`, `@OneToOne`, 대상이 엔티티 (ex. m.team)
  - 컬렉션 값
    - `@OneToMany`, `@ManyToMany`, 대상이 컬렉션 (ex. m.orders)

<br>

## 03. 경로 표현식 특징

- **상태필드 (state field)** : 경로 탐색의 끝, 탐색X
- **단일 값 연관 경로** : 묵시적 내부 조인(inner join) 발생, 탐색O
- **컬렉션 값 연관 경로** : 묵시적 내부 조인 발생, 탐색X
  - FROM 절에서 명시적 조인을 통해 별칭을 얻으면 별칭을 통해 탐색 가능



> Django ORM 에서 
>
> User (1) < - > Article (N) 관계일때,
>
> article.user.username 으로 객체 그래프 탐색 하는것과 비슷하다.
>
> Django 에서도 article__user 더블 언더스코어로 다른 연관객체에 데이터에 접근할 수 있고, 묵시적 조인이 발생하는점이 비슷하다.



 ## 04. 상태 필드 경로 탐색

- JPQL
  - `SELECT m.username, m.age FROM Member m`
- SQL
  - `SELECT m.username, m.age FROM Member m`



## 05. 단일 값 연관 경로 탐색

- JPQL

  - `SELECT o.member FROM Order o`
  - **묵시적 조인이 발생한다. (위험!)**

- SQL

  - ```sql
    SELECT
    	m.*
    FROM
    	Orders o
    	INNER JOIN Member m on o.member_id = m.id
    ```





## 06. 명시적 조인, 묵시적 조인

- **명시적 조인 ( 권장 )**
  - join 키워드 직접 사용
  - `SELECT m FROM Member m Join m.team t`
- 묵시적 조인
  - 경로 표현식에 의해 묵시적으로 SQL 조인 발생 (내부 조인만 가능)
  - `SELECT m.team FROM Member m`





## 07. 경로 표현식 - 예제

- 성공

```sql
-- 1
SELECT o.member.team FROM Order o


-- 2
SELECT t.members FROM Team

-- 3
SELECT m.username FROM TEAM t join t.members m
```



- 실패
  - ToMany 에서는 Collection 을 가져오므로 username 에 접근할 수 없다.

```sql
SELECT t.members.username FROM Team t
```





## 08. 경로 탐색을 사용한 묵시적 조인 시 주의사항

- 항상 내부 조인
- 컬렉션은 경로 탐색의 끝, 명시적 조인을 통해 별칭을 얻어야한다.
- 경로 탐색은 주로 SELECT, WHERE 절에서 사용하지만 묵시적 조인으로 인해 SQL의 FROM (Join) 절에 영향을 줌









































































