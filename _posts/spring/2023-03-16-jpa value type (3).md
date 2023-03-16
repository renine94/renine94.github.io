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

title: "[spring] 스프링 JPA 값 타입 - 값 타입과 불변 객체"
excerpt: "🚀 spring, 값 타입, 불변 객체"

categories: spring
tag: [spring, model, jpa, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA 값 타입 : 값 타입과 불변 객체

- 기본값 타입
- 임베디드 타입
- **값 타입과 불변 객체**
- 값 타입의 비교
- 값 타입 컬렉션

<br><br>

## 값 타입과 불변 객체

값 타입은 복잡한 객체 세상을 조금이라도 단순화하려고 만든 개념이다. 따라서 값 타입은 단순하고 안전하게 다룰 수 있어야 한다.



## 값 타입 공유 참조

- 임베디드 타입과 같은 값 타입을 여러 엔티티에서 공유하면 위험함
- 부작용(side effect) 발생



**사이드 이펙트 발생 !!**

```java
@Embeddable
public class Address {
  private String city;
  private String street;
  private String zipcode;
}

Address address = new Address("city", "street", "10000");  // Address 는 값 타입이다.

Member member1 = new Member();
member.setUsername("member1");
member.setHomeAddress(address);
em.persist(member1);

Member member2 = new Member();
member.setUsername("member2");
member.setHomeAddress(address);
em.persist(member2);

// member1 의 주소중 city 값을 변경한다.
member1.getHomeAddress().setCity("newCity") // member1, member2 모두 city가 "newCity"로 변경된다.

```



**해결법**

```java
@Embeddable
public class Address {
  private String city;
  private String street;
  private String zipcode;
}

Address address = new Address("city", "street", "10000");  // Address 는 값 타입이다.

Member member1 = new Member();
member.setUsername("member1");
member.setHomeAddress(address);
em.persist(member1);

// 값을 복사해서 사용해야 함
Address copyAddress = new Address(address.getCity(), address.getStreet(), address.getZipcode());

Member member2 = new Member();
member.setUsername("member2");
member.setHomeAddress(copyAddress);
em.persist(member2);

// member1 의 주소중 city 값을 변경한다.
member1.getHomeAddress().setCity("newCity") // member1, member2 모두 city가 "newCity"로 변경된다.


```



<br><br>

## 객체 타입의 한계

- 항상 값을 복사해서 사용하면 공유 참조로 인해 발생하는 부작용을 피할 수 있다.
- 문제는 임베디드 타입처럼 **직접 정의한 값 타입은 자바의 기본타입이 아니라 객체 타입** 이다.
- 자바 기본 타입(primitive type) 에 값을 대입하면 값을 복사한다.
- 객체 타입은 참조 값을 직접 대입하는 것을 막을 방법이 없다.
- 객체의 공유 참조는 피할 수 없다.

<br>

### 기본타입 (primitive type)

- Call by Value

```java
int a = 10;
int b = a;  // 기본 타입은 값을 복사
b = 4;
```



### 객체 타입

- Call by Reference

```java
Address a = new Address("old");
Address b = a;  // 객체 타입은 참조를 전달
b.setCity("new")  
```





## 불변 객체

- 객체 타입을 수정할 수 없게 만들면 **부작용을 원천 차단**
- **값 타입은 불변 객체(immutable object)로 설계해야함**
- **불변 객체 : 생성 시점 이후 절대 값을 변경할 수 없는 객체**
- 생성자로만 값을 설정하고 **수정자(Setter)를 만들지 않으면 됨**
- 참고: Integer, String 은 자바가 제공하는 대표적인 불변 객체



값을 바꾸려면 어떻게 해야할까?

```java
Address address = new Address("city", "street", "10000");  // Address 는 값 타입이다.

Member member1 = new Member();
member.setUsername("member1");
member.setHomeAddress(address);
em.persist(member1);

Address newAddress = new Address("newCity", address.getStreet(), address.getZipcode());
member.setHomeAddress(newAddress);
```



<br><br>



---



# Python 에서 불변 객체 만드는법

- dataclass (기본 내장 라이브러리)
- pydantic (FastAPI 에서 같이 쓰이는 라이브러리)



## dataclass

- [참고블로그](https://www.daleseo.com/python-dataclasses/)

```python
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)  # 불변
class User:
    id: int
    name: str
    birthdate: date
    admin: bool = False
```





## pydantic

- [참고블로그](https://self-learning-java-tutorial.blogspot.com/2021/10/pydantic-define-immutable-models.html)

```python
from pydantic import BaseModel

class MyDataClass(BaseModel):
    name: str
    age: int

    class Config:
        allow_mutation = False
```







































