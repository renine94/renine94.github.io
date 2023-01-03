---
layout: single

header:
  teaser: /assets/images/logo/pattern.jpeg
  overlay_image: /assets/images/logo/pattern.jpeg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[pattern] Spring 예시를 통해 SOLID 원칙에 대해 다시 학습해보자."
excerpt: "🚀 단일책임, 개방폐쇄, 리스코프치환, 인터페이스분리, 의존관계역전"

categories: pattern
tag: [pattern, solid]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---
# 01. SOLID 원칙
- `SRP` 단일 책임 원칙
- `OCP` 개방-폐쇄 원칙
- `LSP` 리스코프 치환 원칙
- `ISP` 인터페이스 분리 원칙
- `DIP` 의존관계 역전 원칙



## SRP 단일 책임 원칙

> - Single Responsibility Principle
>
> Controller, Service, Repository 처럼 각각의 클래스로 레이어를 나누는것들이 결국 단일책임원칙을 따르기 위한 행동이라고 생각하면 이해하기 쉽다.

- 한 클래스는 하나의 책임만 가져야 한다.
- 하나의 책임이라는 것은 모호하다.
  - 클 수도, 작을 수도 있다.
  - 문매과 상황에 따라 다르다.
- **중요한 기준은 변경**이다. 변경이 있을 때 파급 효과가 **적으면** 단일 책임 원칙을 잘 따른 것
- 예) UI 변경, 객체의 생성과 사용을 분리

<br>

---

## OCP 개방-폐쇄 원칙

> - Open / Close Principle
>
> 인터페이스를 잘 설계하고, 그것을 구현한 클래스들은 Spring 에서 여러군대에서 바꿔 끼울수가 있다.
>
> MemoryRepository, JdbcRepository, JpaRepository, SpringDataJpaRepository 등등 다른 구현체로 갈아 끼우면 됨

- 소프트웨어 요소는 **확장에는 열려 있으나, 변경에는 닫혀** 있어야 한다.
- **다형성을 활용해보자.**
- 인터페이스를 구현한 새로운 클래스를 하나 만들어서 새로운 기능을 구현
- 역할 (인터페이스) 와 구현 (클래스) 의 분리를 생각해보면 이해가 쉽다.
- 배우라는 역할에는 원빈, 장동건과 같은 구현체들이 대체할 수 있다.



```java
public class MemberService {
  private MemberRepository memberRepository = new MemoryMemberRepository;
}
```

<br>

```java
public class MemberService {
  // private MemberRepository memberRepository = new MemoryMemberRepository;
  private MemberRepository memberRepository = new JdbcMemberRepository;
}
```

`JdbcMemberRepository` 로 변경할때, `MemberService` 클라이언트에서 결국 코드를 변경하게 되는데, 그럼 개방폐쇄 원칙이 지켜지지 않는게 아닌가? 생각할수도 있다.

- **객체를 생성하고, 연관관계를 맺어주는 별도의 조립, 설정자가 필요하다.**
  - 스프링의 스프링 컨테이너가 이 역할을 수행해준다.
  - 이 OCP 원칙을 지키기 위해서 스프링에서는 `DI, IoC` 와 같은 기술들이 사용되어 지는 것이다.



<br>

---

## LSP 리스코프 치환 원칙

> - Liskov Substitution Principle
>
> 인터페이스에서 구현하라고 정의한 함수에 의미에 맞게 코드를 작성해야함
>
> 인터페이스를 구현하는 클래스가 있을 때, `getUser()` 함수가 있으면, 유저를 가져와야 한다. 다른 동작하면 안된다.

- 프로그램의 객체는 프로그램의 정확성을 깨뜨리지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다.
- 다형성에서 하위 클래스는 인터페이스 규약을 다 지켜야 한다는 것, 다형성을 지원하기 위한 원칙, 인터페이스를 구현한 구현체는 믿고 사용하려면, 이 원칙이 필요하다.
- 단순히 컴파일에 성공하는 것을 넘어서는 이야기
  - 엑셀은 앞으로 가라는 기능인데, 뒤로 가게 구현을 해도, 컴파일에는 성공하지만, 의미에 맞지 않다.
- 예) 자동차 인터페이스의 엑셀은 앞으로 가라는 기능, 뒤로 가게 구현하면 LSP 위반, 느리더라도 앞으로 가야함



<br>

---

## ISP 인터페이스 분리 원칙

> - Interface Segregation Principle
>
> 기능을 너무 많이 가지고있는 인터페이스 큰걸 하나 만드는것보다, 그 기능을 사용하는 클라이언트 입장에서 기능을 쪼개는게 낫다.
>
> 즉, 인터페이스의 기능을 사용자입장에서 쪼개서 여러개로 분리 시켜라.
>
> 기능이 많으면 복잡하니까, 쪼개라... 대체 가능성이 좋아진다. ㅎ

- 특정 클라이언트를 위한 인터페이스 여러 개가 범용 인터페이스 하나보다 낫다.
- 자동차 인터페이스 -> 운전 인터페이스, 정비 인터페이스로 분리
- 사용자 클라이언트 -> 운전자 클라이언트, 정비사 클라이언트로 분리
- 분리하면 정비 인터페이스 자체가 변해도 운전자 클라이언트에 영향을 주지 않다.
- 인터페이스가 명확해지고, 대체 가능성이 높아진다.



<br>

---

## DIP 의존관계 역전 원칙

> - Dependency Inversion Principle
>
> 한마디로 인터페이스에 의존해야 한다는 것,
>
> 인터페이스를 구현한 클래스에 의존하면 안된다는 것

- 프로그래머는 "추상화에 의존해야지, 구체화에 의존하면 안된다." 의존성 주입은 이 원칙을 따르는 방법 중 하나다.
- 쉽게 이야기해서, 구현 클래스에 의존하지 말고, 인터페이스에 의존하라는 뜻
- 앞에서 이야기한 역할(Role, Interface) 에 의존하게 해야 한다는 것과 같다.
- 객체 세상도 클라이언트가 인터페이스에 의존해야 유연하게 구현체를 변경할 수 있다.
- 구현체에 의존하게 되면 변경이 아주 어려워진다.



`MemberService` 는 `MemberRepository` 인터페이스만 알면되지,<br>`MemberRepository` 를 구현한 `MemoryMemberRepository` 또는 `JdbcMemberRepository`를 몰라도 된다는 뜻



- 위에 OCP 에서 설명한 `MemberService` 는 인터페이스에 의존하지만, 구현 클래스도 동시에 의존한다.

- MemberService 클라이언트가 구현 클래스를 직접 선택

  ```java
  MemberRepository m = new MemoryMemberRepository();
  ```

- **위 코드는 DIP 를 위반하고 있다.**



<br>



# 02. 정리



- 객체 지향의 핵심은 **다형성** 이다.
- 다형성 만으로는 쉽게 부품을 갈아 끼우듯이 개발할 수 없다.
- 다형성 만으로는 구현 객체를 변경할 때 클라이언트 코드도 함께 변경된다.
- **다형성 만으로는 OCP, DIP 를 지킬 수 없다.**
- 뭔가 더 필요하다...
  - 스프링 프레임워크가 도와준다.
  - DI, IoC 같은 개념





