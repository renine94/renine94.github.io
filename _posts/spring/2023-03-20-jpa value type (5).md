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

title: "[spring] 스프링 JPA 값 타입 - 값 타입 컬렉션"
excerpt: "🚀 spring, 값 타입, 컬렉션"

categories: spring
tag: [spring, model, jpa, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA 값 타입 : 값 타입 컬렉션

- 기본값 타입
- 임베디드 타입
- 값 타입과 불변 객체
- 값 타입의 비교
- **값 타입 컬렉션**

<br><br>

## TL; DR

> 값 타입 컬렉션보다는 그냥 Entity 를 사용하자..

 

|                 값 타입                 |     Entity     |
| :-------------------------------------: | :------------: |
|                식별자 X                 |    식별자 O    |
|        생명 주기를 엔티티에 의존        | 생명 주기 관리 |
| 공유하지 않는 것이 안전 (복사해서 사용) |      공유      |
|      불변 객체로 만드는 것이 안전       |                |



## 값 타입 컬렉션

- 값 타입을 하나 이상 저장할 때 사용
- @ElementCollection, @CollectionTable 사용
- 데이터베이스는 컬렉션을 같은 테이블에 저장할 수 없다.
- 컬렉션을 저장하기 위한 별도의 테이블이 필요함



![image-20230320101036330](../../assets/images/posts/2023-03-20-jpa value type (5)/image-20230320101036330.png)

```java
@Entity
public class Member {
  @Id
  @GeneratedValue
  @Column(name = "MEMBER_ID")
  private Long id;
  
  @Column(name = "USERNAME")
  private String username;
  
  @Embedded
  private Address homeAddress;
  
  @ElementCollection
  @CollectionTable(name = "FAVORITE_FOOD",
                  joinColumns = @JoinColumn(name = "MEMBER_ID")
  )
  @Column(name = "FOOD_NAME")  // 예외적으로 가능
  private set<String> favoriteFoods = new HashSet<>();
  
  @ElementCollection
  @CollectionTable(name = "ADDRESS",
                  joinColumns = @JoinColumn(name = "MEMBER_ID")                
  )
  private List<Address> addressHistory = new ArrayList<>();
  
  // getter, setter ...
}
```

<br><br>

## 값 타입 컬렉션 사용

- 값 타입 저장 예제
- 값 타입 조회 예제
  - 값 타입 컬렉션도 지연 로딩 전략 사용
- 값 타입 수정 예제
  - 단순히 setter 로 수정하면안되고, 값타입 자체의 객체를 다시 새롭게 만들어서 갈아끼워야 한다.
- **참고: 값 타입 컬렉션은 영속성 전이(Cascade) + 고아 객체 제거 기능을 필수로 가진다고 볼 수 있다.**



```java
Member member = new Member();
member.setUsername("member1");
member.setHomeAddress(new Address("homeCity", "street", "10000"));

member.getFavoriteFoods().add("치킨");
member.getFavoriteFoods().add("족발");
member.getFavoriteFoods().add("피자");

member.getAddressHistory().add(new Address("old1", "street", "10000"));
member.getAddressHistory().add(new Address("old2", "street", "10000"));

em.persist(member);

em.flush();
em.clear();

Member findMember = em.find(Member.class, member.getId());

Address a = findMember.getHomeAddress();
// 값 타입을 수정할 때는 단순히 값을 바꾸는게 아니라 Address 객체를 새로만들어서 갈아끼워야 한다.
findMember.setHomeAddress(new Address("newCity", a.getStreet(), a.getZipcode()));

// 치킨 > 한식
findMember.getFavoriteFoods().remove("치킨");
findMember.getFavoriteFoods().add("한식");

// equals() 가 제대로 오버라이딩 되어 있어야 한다. 
findMember.getAddressHistory().remove(new Address("old1", "street", "10000"));
findMember.getAddressHistory().add(new Address("newCity1", "street", "10000"));


```



<br><br>

## 값 타입 컬렉션의 제약사항

- 값 타입은 엔티티와 다르게 식별자 개념이 없다.
- 값은 변경하면 추적이 어렵다.
- **값 타입 컬렉션에 변경 사항이 발생하면, 주인 엔티티와 연관된 모든 데이터를 삭제하고, 값 타입 컬렉션에 있는 현재 값을 모두 다시 저장한다.**
- 값 타입 컬렉션을 매핑하는 테이블은 모든 컬럼을 묶어서 기본키를 구성해야 함 : null 입력X, 중복 저장X



## 값 타입 컬렉션 대안

- 실무에서는 상황에 따라 **값 타입 컬렉션 대신에 일대다 관계**를 고려
- 일대다 관계를 위한 엔티티를 만들고, 여기에서 값 타입을 사용
- 영속성 전이(Cascade) + 고아 객체 제거를 사용해서 값 타입 컬렉션 처럼 사용
- Ex) AddressEntity



```java
@Entity
@Table(name = "ADDRESS")
public class AddressEntity {
  private String city;
  private String street;
  private String zipcode;
}

@Entity
public class Member {
  ...
  
  @OneToMany(cascade = CascadeType.ALL, orphanRemoval = true)
  @JoinColumn(name = "MEMBER_ID")
  private List<AddressEntity> addressHistory = new ArrayList<>();
  
  ...
  
}
```



















































