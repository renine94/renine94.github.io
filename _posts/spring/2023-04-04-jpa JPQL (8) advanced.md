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

title: "[spring] 스프링 JPA 객체지향 쿼리언어 JPQL 고급 - 페치 조인"
excerpt: "🚀 spring, JPA, JPQL, 페치조인, 성능최적화, Django와 비교(select_related)"

categories: spring
tag: [spring, model, jpa, jpql, join, fetch]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# 객체지향 쿼리 언어8 Advanced - 페치 조인 

- 경로표현식
- **페치 조인 1 - 기본**
- 페치 조인 2 - 한계
- 다형성 쿼리
- 엔티티 직접 사용
- Named 쿼리
- 벌크 연산

<br><br>



# TL; DR







## 01. 페치조인 (fetch join)

- SQL 조인 종류 X
- JPQL 에서 **성능 최적화**를 위해 제공하는 기능
- 연관된 엔티티나 컬렉션을 **SQL 한번에 함께 조회**하는 기능
- Join fetch 명령어 사용
- 페치 조인 ::= [ LEFT [OUTER] | INNER ] JOIN FETCH 조인경로





## 02. Entity 페치 조인

- 회원을 조회하면서 연관된 팀도 함께 조회. (SQL 한 번에)

- SQL을 보면 회원 뿐만 아니라 팀(T.*) 도 함께 SELECT

- JPQL

  - `SELECT m FROM Member m join fetch m.team`

- SQL

  - ```sql
    SELECT M.*, T.*
    FROM Member M
    	INNER JOIN TEAM T ON M.Team_id = T.id
    ```



> Django의 select_related() 함수에서 Join 으로 데이터 가져오는거랑 비슷하다고 보면 된다.



- Inner Join
  - 아래 사진에서 회원4 가 안보이는 이유는 이너조인 이기 때문이다.
  - Left Join 시에는 회원4도 출력된다.

![image-20230411180146088](../../assets/images/posts/2023-04-04-jpa JPQL (8) advanced/image-20230411180146088.png)

 

- 정참조 (ManyToOne)
  - 팀1, 멤버N

| SpringBoot                                  | Django                                        |
| ------------------------------------------- | --------------------------------------------- |
| `SELECT m FROM Member m JOIN FETCH m.team;` | `Member.objects.select_related('team').all()` |





## 03. Collection 페치 조인

- 역참조 (일대다 관계일 때,)
  - 1 쪽에서 N개 데이터 가져오는 경우
  - 팀에서 member들 가져올때
  - Django 에서는 prefetch_related 로 해결



- JPQL

```sql
SELECT t
FROM Team t JOIN FETCH t.members
WHERE t.name = '팀A';
```



- SQL

```sql
SELECT T.*, M.*
FROM TEAM T INNER JOIN MEMBER M ON T.ID = M.TEAM_ID
WHERE T.NAME = '팀A'
```





- 데이터가 뻥튀기 되므로 Distinct 옵션 사용해야함 (일대다 관계)

![image-20230411184044872](../../assets/images/posts/2023-04-04-jpa JPQL (8) advanced/image-20230411184044872.png)



중복이 싫으면 `DISTINCT` 사용

1. SQL 에 DISTINCT 를 추가
2. 애플리케이션에서 엔티티 중복 제거



