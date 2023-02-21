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

title: "[spring] 스프링에서 Model 설계, Entity 매핑하는 여러가지 방법 (3)"
excerpt: "🚀 spring, 상속관계 Entity 설정, @MappedSuperclass, BaseDateTime, etc.."

categories: spring
tag: [spring, model, jpa, entity, mapping]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA - Entity 매핑 (3)

- 상속관계 매핑
- @MappedSuperclass
  - 속성만 상속하는 것



## 01. 상속관계 매핑

- 관계형 DB는 상속 관계X
- 슈퍼타입, 서브타입 관계라는 모델링 기법이 객체 상속과 유사
- 상속 관계 매핑: 객체의 상속과 구조와 DB의 슈퍼타입 서브타입 관계를 매핑



**슈퍼타입 서브타입 논리 모델을 실제 물리 모델로 구현하는 방법**

1. `@Inheritance(strategy = InheritanceType.XXX)`
   - <u>JOINED</u> : 조인 전략
   - <u>SINGLE_TABLE</u> : 단일 테이블 전략 (default)
   - <u>TABLE_PER_CLASS</u> : 구현 클래스마다 테이블 전략
2. `@DiscriminatorColumn(name = "DTYPE")`
3. `@DiscriminatorValue("XXX")`



```java
@Entity
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)  // single_table 이 default
@DiscriminatorColumn  // DTYPE, (JOINED 전략에서는 굳이..?, SINGLE_TABLE 전략은 필수)
public abstract class Item {
  @Id @GeneratedValue
  private Long id;
  private String name;
  private int price; 
}

@Entity
@DiscriminatorValue("A")  // DTYPE 에 어떻게 저장될지 지정, (default는 클래스명)
public class Album {
  private String artist;
}

@Entity
@DiscriminatorValue("M")
public class Movie {
  private String director;
  private String actor; 
}

@Entity
@DiscriminatorValue("B")
public class Book {
  private String author;
  private String isbn;
}
```

### 1) 조인전략 (추천)

- 장점
  - 테이블 정규화
  - 외래 키 참조 무결성 제약조건 활용가능
  - 저장공간 효율화
- 단점
  - 조회시 조인을 많이 사용, 성능 저하
  - 조회 쿼리가 복잡함
  - 데이터 저장시 Insert SQL 2번 호출

### 2) 단일 테이블 전략 (default)

- 장점
  - 조인이 필요 없으므로 일반적으로 조회 성능이 빠름
  - 조회 쿼리가 단순함
- 단점
  - 자식 엔티티가 매핑한 컬럼은 모두 null 허용
  - 단일 테이블에 모든 것을 저장하므로 테이블이 커질 수 있다. 상황에 따라서 조회 성능이 오히려 느려질 수 있다.

### 3) 구현 클래스마다 테이블 전략

> Django 에서는 상속을 받아서 구현하게 되면 구현 클래스마다 필드가 생기는것을 볼 수 있음
>
> 하지만 **김영한님의 JPA 강의에서는 추천하지 않는 방식**이라고 함.

- 장점
  - 서브 타입을 명확하게 구분해서 처리할 때 효과적
  - not null 제약조건 사용 가능
- 단점
  - 여러 자식 테이블을 함께 조회할 때 성능이 느림 (Union SQL)
  - 자식 테이블을 통합해서 쿼리하기 어려움





## 02. 장고와 비교

|           |                   Spring                    |           Django            |
| :-------: | :-----------------------------------------: | :-------------------------: |
| 모델 상속 | @Inheritance, @Entity, @DiscriminatorColumn |      JOINED 전략 기본       |
| 필드 상속 |              @MappedSuperclass              | class Meta: abstract = True |



- 모델을 상속하는 경우 Spring의 JOINED 전략처럼 동작한다.
  - Item 테이블이 만들어짐 (id, name, price, dtype)
  - Movie 테이블이 만들어짐 (actor, director)
  - Django에서는 따로 DTYPE 같은게 자동으로 만들어지진 않는것 같다.

```python
"""
Spring 에서의 @MappedSuperclass
"""
class BaseDateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

"""
테이블 상속으로 표현
dtype 같은 경우 자동으로 넣어주는 로직이 필요할것 같음
"""
class Item(BaseDateTime, models.Model):
    dtype_list = [
        ("MOVIE", "MOVIE"),
        ("ALBUM","ALBUM"),
        ("BOOK", "BOOK")
    ]

    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    dtype = models.CharField(max_length=255, choices=dtype_list, null=False, blank=False)

class Album(Item):
    artist = models.CharField(max_length=255)

class Movie(Item):
    director = models.CharField(max_length=255)
    actor = models.CharField(max_length=255)

class Book(Item):
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
```

<br><br>

---

## 03. @MappedSuperclass

> 상속관계 매핑과 별로 관계가 없다.

- 상속관계 매핑X
- 엔티티X, 테이블과 매핑X
- 부모 클래스를 상속 받는 **자식 클래스에 매핑 정보만 제공**
- 조회, 검색 불가 (em.find(BaseDateTime) 불가능)
- 직접 생성해서 사용할 일이 없으므로 **추상 클래스 권장**



```java
@MappedSuperclass
public abstract class BaseDateTime {
  private LocalDateTime createdAt;  // 생성 시간
  private String createdBy;  // 누가 생성
  
  private LocalDateTime updatedAt;  // 수정 시간
  private String updatedBy;  // 누가 수정
}
```



위 처럼 모든 테이블에 공통으로 항상 있는 컬럼(필드) 들을 만들 때 사용된다.



