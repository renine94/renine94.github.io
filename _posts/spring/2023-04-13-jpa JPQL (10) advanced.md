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

title: "[spring] 스프링 JPA 객체지향 쿼리언어 JPQL 고급 - 엔티티 직접 사용"
excerpt: "🚀 spring, JPA, JPQL, 페치조인, 성능최적화, Django와 비교"

categories: spring
tag: [spring, model, jpa, jpql, join, fetch]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# 객체지향 쿼리 언어10 Advanced - 엔티티직접사용

- 경로표현식
- 페치 조인 1 - 기본
- 페치 조인 2 - 한계
- 다형성 쿼리
- **엔티티 직접 사용**
- **Named 쿼리**
- **벌크 연산**

<br><br>



# TL; DR

| Django                                                       | Spring                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Article.objects.filter(user=user)<br /><br />Article.objects.filter(user_id=user.id) | String jpql = "SELECT m FROM Member m WHERE m = :member";<br /><br />String jpql = 'SELECT m FROM Member m WHERE m.id = :memberId' |





## 01. 엔티티 직접 사용 - 기본 키 값

- Entity 를 파라미터로 전달

```java
String jpql = "SELECT m FROM Member m WHERE m = :member";
List resultList = em.createQuery(jpql)
  .setParameter("member", member)
  .getResultList();
```



- 식별자(id) 직접 전달

```java
String jpql = "SELECT m FROM Member m WHERE m.id = :memberId";
List resultList = em.createQuery(jpql)
  .setParameter("memberId", member.getId())
  .getResultList();
```



실행된 SQL

```sql
SELECT m.*
FROM Member m
WHERE m.id = ?
```





## 02. 엔티티 직접 사용 - 외래키 값

```java
Team team = em.find(Team.class, 1L);

// 1
String qlString = "SELECT m FROM Member m WHERE m.team = :team";
List resultList = em.createQuery(qlString)
  .setParameter("team", team)
  .getResultList();

// 2
String qlString = "SELECT m FROM Member m WHERE m.team.id = :teamId";
List resultList = em.createQuery(qlString)
  .setParameter("teamId", teamId)
  .getResultList();
```



실행된 SQL

```sql
SELECT m.*
FROM Member m
WHERE m.team_id = ?
```



<br><br>

# JPQL Named 쿼리 - 정적쿼리

- 미리 정의해서 이름을 부여해두고 사용하는 JPQL
- 정적 쿼리
- 어노테이션, XML 재정의
- 애플리케이션 로딩 시점에 초기화 후 재사용
- **애플리케이션 로딩 시점에 쿼리를 검증**



```java
@Entity
@NamedQuery(
	name = "Member.findByUsername",
  query = "SELECT m FROM Member m WHERE m.username = :username"
)
public class Member {
  ...
}


List<Member> resultList = em.createNamedQuery("Member.findByUsername", Member.class)
  .setParameter("username", "회원1")
  .getResultList();
```





## 01. Named 쿼리 - XML 에 정의

```xml
# [META-INF/persistence.xml]
<persistence-unit name="jpabook">
  <mapping-file>META-INF/ormMember.xml</mapping-file>
  
# [META-INF/ormMember.xml]
<entity-mappings xmlns="http://xmlns.jcp.org/xml/ns/persistence/orm" version="2.1">
	
  <named-query name="Member.findByUsername">
  	<query>
    	SELECT m FROM Member m WHERE m.username= :username
    </query>
  </named-query>
  
  <named-query name="Member.count">
  	<query>
    	SELECT count(m) FROM Member m
    </query>
  </named-query>
  
</entity-mappings>
```



추후 Spring-Data-JPA 를 사용하게되면, 아래와 같이 namedQuery 대신 쓸 수 있다.

```java
public interface UserRepository extends JpaRepository<User, Long> {
  
  @Query("select u from User u where u.emailAddress = ?1")
  User findByEmailAddress(String emailAddress);
  
}
```



# 벌크연산 (Bulk)

- 재고가 10개 미만인 모든 상품의 가격을 10% 상승하려면?
- JPA 변경 감지 기능(더티체킹) 으로 실행하려면 너무 많은 SQL 실행
  - 재고가 10개 미만인 상품을 리스트로 조회한다.
  - 상품 엔티티의 가격을 10% 증가한다.
  - 트랜잭션 커밋 시점에 변경감지가 동작한다.
- 변경된 데이터가 100건이라면 100번의 Update SQL 실행





## 01. 벌크 연산 예제

- 쿼리 한번으로 여러 테이블 로우 변경(엔티티)
- `executeUpdate()` 의 결과는 영향받은 엔티티 수 반환
- Update, Delete 지원
- Insert (insert into ... select, 하이버네이트 지원)

```java
String jpql = "update Product p " +
  "set p.price = p.price * 1.1 " +
  "where p.stockAmount < :stockAmount";

int resultCount = em.createQuery(jpql)
  .setParameter("stockAmount", 10)
  .executeUpdate();
```





## 02. 벌크 연산 주의

- 벌크 연산은 영속성 컨텍스트를 무시하고 데이터베이스에 직접 쿼리
  - 벌크 연산을 먼저 수행
  - **벌크 연산 수행 후 영속성 컨텍스트 초기화**

```java
Member member1 = new Member();
member1.setUsername("member1");
member1.setAge(0);
em.persist(member1);

Member member2 = new Member();
member1.setUsername("member2");
member1.setAge(0);
em.persist(member2);

// flush
int resultCount = em.createQuery("update Member m set m.age = 20")
  .executeUpdate();

em.clear(); // 영속성 컨텍스트를 초기화

Member findMember = em.find(Member.class, member1.getId());

System.out.println("findMember = " + findMember.getAge());  // 20 (em.clear()를 안해주면 0이 나옴)
```





















































