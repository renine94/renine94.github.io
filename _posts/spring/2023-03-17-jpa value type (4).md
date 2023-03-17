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

title: "[spring] 스프링 JPA 값 타입 - 값 타입의 비교"
excerpt: "🚀 spring, 값 타입, 비교"

categories: spring
tag: [spring, model, jpa, type]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA 값 타입 : 값 타입의 비교

- 기본값 타입
- 임베디드 타입
- 값 타입과 불변 객체
- **값 타입의 비교**
- 값 타입 컬렉션

<br><br>

## 값 타입의 비교

- 값 타입: 인스턴스가 달라도 그 안에 값이 같으면 같은 것으로 봐야 함

```java
int a = 10;
int b = 10;  // a == b # true

Address a = new Address("서울시");
Address b = new Address("서울시");  // a == b # false
```

Java 에서의 == 는 참조값을 비교하기 때문에 인스턴스가 다르면 false 가 나오게 된다.



- **동일성 (identity) 비교** : 인스턴스의 참조 값을 비교, == 사용

- **동등성 (equivalence) 비교** : 인스턴스의 값을 비교. equals()  사용

- 값 타입은 a.equals(b) 를 사용해서 동등성 비교를 해야 함

- 값 타입은 equals() 메소드를 적절하게 재정의 (주로 모든 필드 사용)

  - ```java
    public class Address {
      private String city;
      private String street;
      private String zipcode;
      // 기본 생성자
      public Address() {}
    
      public Address(String city, String street, String zipcode) {
        this.city = city;
        this.street = street;
        this.zipcode = zipcode;
      }
      
      // getter, setter 
      ...
        
      // equals() 메소드 오버라이딩 필요. (동등성 값 비교를 위해)
      @Override
      public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null) || getClass() != o.getClass()) return false;
        Address address = (Address) o;
        return Objects.equals(city, address.city)
          && Objects.equals(street, address.street)
          && Objects.equals(zipcode, address.zipcode);
      }
      
      // hashcode() 메소드도 오버라이딩 필요
      ...
    }
    ```



> Python 에서 메모리 참조값이 같은지 비교할 땐  a is b
>
> 값이 동일한지만 비교하려면  a == b
>
> 자바랑 반대인것 같다.



```java
// java
int a = 10;
int b = 10;

a == b;
a.equlas(b)

// python
a: int = 10
b: int = 10

a is b
a == b
```

























