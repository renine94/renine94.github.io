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

title: "[spring] 스프링 JPA 값 타입 - 임베디드 타입"
excerpt: "🚀 spring, 값 타입, 임베디드 타입"

categories: spring
tag: [spring, model, jpa, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA 값 타입 : 임베디드 타입

- 기본값 타입
- **임베디드 타입**
- 값 타입과 불변 객체
- 값 타입의 비교
- 값 타입 컬렉션

<br><br>

## 임베디드 타입

- 새로운 값 타입을 직접 정의할 수 있음
- JPA는 임베디드 타입(embedded type) 이라 함
- 주로 기본 값 타입을 모아서 만들어서 복합 값 타입이라고도 함
- int, String과 같은 값 타입

<br>

- 회원 엔티티는 이름, 근무 시작일, 근무 종료일, 주소 도시, 주소 번지, 주소 우편번호를 가진다.



**임베디드 타입 사용X**

```java
@Entity
public class Member extends BaseEntity {
  
  @Id
  @GeneratedValue
  @Column(name = "MEMBER_ID")
  private Long id;
  
  @Column(name = "USERNAME")
  private String username;
  
  // 기간 Period
  private LocalDateTime startDate;
  private LocalDateTime endDate;
  
  // 주소 address
  private String city;
  private String street;
  private String zipcode;
}
```



**임베디드 타입 사용O**

```java
@Embeddable
public class Period {
  private LocalDateTime startDate;
  private LocalDateTime endDate;
  
  public boolean isWork() {
    // 현재 일하는 중인지에 대한 비즈니스 로직 작성 가능
  }
}

@Embeddable
public class Address {
  private String city;
  private String street;
  private String zipcode;
}


@Entity
public class Member extends BaseEntity {
  
  @Id
  @GeneratedValue
  @Column(name = "MEMBER_ID")
  private Long id;
  
  @Column(name = "USERNAME")
  private String username;
  
  // 기간 Period
  @Embedded
  private Period period;
  
  // 주소 address
  @Embedded
	private Address address;
}
```

<br><br>

## 임베디드 타입과 테이블 매핑

- 임베디드 타입은 엔티티의 값일 뿐이다.
- 임베디드 타입을 사용하기 전과 후에 **매핑하는 테이블은 같다.**
- 객체와 테이블을 아주 세밀하게 매핑하는 것이 가능
- 잘 설계한 ORM 애플리케이션은 매핑한 테이블의 수보다 클래스의 수가 더 많음





## @AttributeOverride : 속성 재정의

- 하나의 엔티티에서 같은 값 타입을 사용하면?
- 컬럼 명이 중복됨
- @AttributeOverrides, @AttributeOverride 를 사용해서 컬럼명 속성을 재정의

```java
@Embeddable
public class Period {
  private LocalDateTime startDate;
  private LocalDateTime endDate;
  
  public boolean isWork() {
    // 현재 일하는 중인지에 대한 비즈니스 로직 작성 가능
  }
}

@Embeddable
public class Address {
  private String city;
  private String street;
  private String zipcode;
}


@Entity
public class Member extends BaseEntity {
  
  @Id
  @GeneratedValue
  @Column(name = "MEMBER_ID")
  private Long id;
  
  @Column(name = "USERNAME")
  private String username;
  
  // 주소 address
  @Embedded
	private Address workAddress;
  
  @Embedded
  @AttributeOverrides({
    @AttributeOverride(name="city", column=@Column(name = "home_city")),
    @AttributeOverride(name="street", column=@Column(name = "home_street")),
    @AttributeOverride(name="zipcode", column=@Column(name = "home_zipcode")),
  })
	private Address homeAddress;
}
```





<br><br>

---

# Django 와 비교

- 위에서 배운 내용을 Django 에서 정의한다면 아래와 같이 될 것이다.

```python
class BaseModel(models.Model):
  class Meta:
    abstract = True
  
  created_at = ...
  updated_at = ...
  
  
class BaseWorkModel(models.Model):
  class Meta:
    abstract = True
  
  started_at = ...
  ended_at = ...
  
  
class BaseAddressModel(models.Model):
  class Meta:
    abstract = True
  
  city = ...
  street = ...
  zipcode = ...
  
  
class User(BaseModel, BaseWorkModel, BaseAddressModel, models.Model):
  ...
```









