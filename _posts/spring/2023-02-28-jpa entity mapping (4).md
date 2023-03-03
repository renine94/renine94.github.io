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

title: "[spring] 스프링 즉시로딩과 지연로딩"
excerpt: "🚀 spring, lazy loading, eager loading, etc.."

categories: spring
tag: [spring, model, jpa, lazy, orm]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA - 즉시로딩과 지연로딩
> [관련 포스팅 추가자료 첨부](https://wwlee94.github.io/category/blog/spring-jpa-n+1-query/)

- Team(1), Member(N) 관계에 테이블이 있다.
- **Member 를 조회할때, 꼭 Team 정보를 같이 가져와야 할까?**
  - 매번 Member 를 조회할때마다 Team을 가져오는것은 불필요하고 낭비
  - Team 데이터를 사용할때만 가져오게 한다.
  - 내부적으로 Lazy 로딩방식을 사용하게되고, 이때 Team객체는 프록시객체로 가져오게 된다.
  - (참고로 Django는 default 값이 Lazy 로딩방식이다.)



## 01. 지연로딩 (Lazy Loading)

**Entity**

```java
@Entity
public class Member {
  @Id
  @GeneratedValue
  private Long id;
  
  @Column(name = "USERNAME")
  private String name;
  
  @ManyToOne(fetch = FetchType.LAZY)  // Lazy 로딩
  @JoinColumn(name = "TEAM_ID")
  private Team team;
  
  ....
}
```



**Logic**

```java
Team team = new Team();
team.setName("teamA");
em.persist(team);

Member member1 = new Member();
member1.setName("member1");
member1.setTeam(team);
em.persist(member1);

em.flush(); // 영속성 컨텍스트에 있는 쿼리문들을 실제 DB로 날린다.
em.clear(); // 영속성 컨텍스트를 비운다.

Member m = em.find(Member.class, member1.getId());

System.out.println("m = " + m.getTeam().getClass());
team.getName(); // 실제 team 데이터를 사용할때 데이터를 가져오게 된다.

tx.commit()
```





## 02. 즉시로딩 (Eager Loading)

- Member를 조회할 때, Team도 같이 데이터를 가져온다. (join)



**Entity**

```java
@Entity
public class Member {
  @Id
  @GeneratedValue
  private Long id;
  
  @Column(name = "USERNAME")
  private String name;
  
  @ManyToOne(fetch = FetchType.EAGER)  // 즉시 로딩
  @JoinColumn(name = "TEAM_ID")
  private Team team;
  
  ....
}
```





## 03. 프록시와 즉시로딩 주의

- **가급적 지연 로딩만 사용 (실무에서)**
- 즉시 로딩을 적용하면 예상치 못한 SQL이 발생
- 즉시 로딩은 JPQL 에서 N+1 문제를 일으킨다.
- @ManyToOne, @OneToOne은 기본이 즉시 로딩이므로, 지연로딩으로 설정하자!
- @OneToMany, @ManyToMany 는 기본이 지연 로딩





## 04. 주의점

- Django 와 Spring 에서의 N+1 문제가 서로 다른 케이스에 발생하는 문제
- Django
  - **Lazy Loading 에서 N+1 문제 발생**
  - `select_related`, `prefetch_related` 로 해결 가능하다. (정참조, 역참조)
- Spring
  - **Eager Loading 에서 N+1 문제 발생 (JPQL 사용시?)**
  - Lazy Loading 으로 설정하고 필요한 데이터는 `fetch join` 으로 가져오면 해결 가능하다.



<br>

**ChatGPT**

```
N+1 문제는 Lazy Loading 방식일 때 발생하는 문제입니다.

Lazy Loading 방식에서는 필요한 시점에 데이터를 가져오는 것이 원칙이기 때문에, 데이터를 사용할 때마다 쿼리를 실행하여 데이터를 가져옵니다. 이 때, 관련된 객체를 함께 가져와야 할 때, 관련된 객체들의 데이터를 가져오는 추가적인 쿼리가 발생할 수 있습니다. 이 때, 쿼리가 N+1번 실행되어 성능 저하가 발생하는데, 이를 N+1 문제라고 합니다.

반면, Eager Loading 방식에서는 필요한 데이터를 한 번에 모두 가져오기 때문에, 추가적인 쿼리가 발생하지 않습니다. 따라서, Eager Loading 방식에서는 N+1 문제가 발생하지 않습니다.
```



N+1 문제는 기본적으로 지연로딩일 때 발생한다고 하지만,  Spring에서 제공해주는 JPQL 에서는 즉시로딩에서 나타나게 되는 문제가 있다.



**이는 제가 Django에서 알고있던 개념과 살짝 달라서 혼동이 오는 부분입니다.**



```java
Team team = new Team();
team.setName("teamA");
em.persist(team);

Member member1 = new Member();
member1.setUsername("member1");
member1.setTeam(team);
em.persist(member1);

em.flush();
em.clear();

List<Member> members = em.createQuery("select m from Member m ", Member.class)
  .getResultList()  // 이 코드에서 JPQL 이 sql문으로 변환되면서 EAGER 로 가져와야하기 때문에 쿼리가 한 번 더 호출되는 문제가 발생한다.
  
  
```









---



## 05. 정리

지연 로딩 활용 - 실무

- 모든 연관관계에 지연로딩 사용할 것
- 실무에서 즉시 로딩 사용 X
- JPQL fetch 조인이나, 엔티티 그래프 기능을 사용해라.
- 즉시 로딩은 상상하지 못한 쿼리가 나간다.
