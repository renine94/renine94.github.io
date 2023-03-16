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

title: "[spring] 스프링 JPA 값 타입 - 기본값 타입"
excerpt: "🚀 spring, 값 타입, 기본값 타입, 원시자료형, 참조값타입"

categories: spring
tag: [spring, model, jpa, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA 값 타입 : 기본값 타입

- **기본값 타입**
- 임베디드 타입
- 값 타입과 불변 객체
- 값 타입의 비교
- 값 타입 컬렉션



# 01) JPA의 데이터 타입 분류

### 1. 엔티티 타입

- @Entity 로 정의하는 객체
- 데이터가 변해도 식별자로 지속해서 추적 가능
- 예) 회원 엔티티의 키나 나이 값을 변경해도 식별자로 인식 가능

<br>

### 2. 값 타입

- int, Integer, String 처럼 단순히 값으로 사용하는 자바 기본 타입이나 객체
- 식별자가 없고 값만 있으므로 변경시 추적 불가
- 예) 숫자 100을 200으로 변경하면 완전히 다른 값으로 대체

<br><br>



## 02) 값 타입 분류

### 1. 기본값 타입

- 자바 기본 타입 (int, double)
- 래퍼 클래스(Integer, Long)
- String

### 2. 임베디드 타입(embedded type, 복합 값 타입)

- x, y 좌표처럼 하나의 값으로 같이 사용하고 싶을 때

### 3. 컬렉션 값 타입(collection value type)

<br>

<br>

**기본값 타입**

- 예) String name, int age
- 생명주기를 엔티티의 의존
  - 예) 회원을 삭제하면 이름, 나이 필드도 함께 삭제
- 값 타입은 공유하면 X
  - 회원 이름 변경시 다른 회원의 이름도 함께 변경되면 안됨

<br>

- 원시자료형 (Primitive Type)
  - Call by value
  - 기본값 타입이다.
  - 기본값 타입은 항상 값을 "복사" 한다.

```java
int a = 10;
int b = a;

a = 20;

System.out.println("a = ", a);  // 20
System.out.println("b = ", b);  // 10
```

- 참조자료형 (Reference Type)
  - Call by reference

```java
Integer a = new Integer(10);
Integer b = a;

a.setValue(20);

System.out.println("a = ", a);  // 20
System.out.println("b = ", b);  // 20
```











