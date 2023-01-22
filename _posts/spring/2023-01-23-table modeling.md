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

title: "[spring] 스프링에서 Table (Entity) 를 관리하는방법을 알아보자."
excerpt: "🚀 spring, django 두개 프레임워크를 비교하는 형식으로 포스팅"

categories: spring
tag: [spring, model, table, entity]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. Table (Entity)
> 이번 포스팅에서는 Django 에서 테이블을 만드는방법과, Spring 에서 테이블을 만드는 방법에 대해 비교형식으로 공부를 해보고자 한다.
> 둘다 코드로 테이블을 관리한다는점은 동일하고, Django 와 Spring 에서 같은역할을 하지만 코드로 어떻게 다른지 공부해보자.



|      |          Django          |           Spring           |
| :--: | :----------------------: | :------------------------: |
| 1: 1 |  models.OneToOneField()  |         @OneToOne          |
| 1: N |   models.ForeignKey()    | @OneToMany<br />@ManyToOne |
| M: N | models.ManyToManyField() |        @ManyToMany         |



Spring에서 `@OneToMany` 와 `@ManyToOne` 애노테이션의 fetch 방식이 다르기 때문에 잘 이해하고 사용하는 것이 중요하다. 김영한님 강의에서 보면 모두 Lazy 방식으로 변경하라고 권장한다. ( N + 1 ) 문제 연관되어있음 

- @OneToMany
  - default: Lazy
- @ManyToOne
  - default: Eager



Django ORM 에서는 기본적으로 Lazy 로딩 방식이며, 객체가 실제로 평가되기 전까진 DB 에 SQL 을 호출하지 않는다.<br>조인이 필요한 경우

-  정참조
  -  `selected_related()`
- 역참조
  - `prefetch_related()`

그리고 Django에서는 역참조 이름을 `related_name` 옵션을 주어서 설정할 수 있으며, 따로 지정하지않으면 `xxx_set` 와 같은 형식으로 디폴트로 지정된다. 실무에서는 역참조 이름이 중복될수도 있으니 네이밍 규칙을 정해서 "일관성" 있게 사용하는것이 좋다.



또한 김영한님의 스프링부트 강의에서는 ManyToMany 옵션 사용을 지양하고 있는데, 그 이유는 RDBMS 에서는 M: N 관계를 표현하기 위해 중간테이블을 두게 되고, 각각 1:N, M:1 방식으로 연결해서 중간테이블을 만들기 때문이다.

Django 에서도 `ManyToManyField()` 로 M: N 관계를 설정할 수는 있지만, through 옵션을 따로 주지않으면 장고가 내부적으로 fk 컬럼만 있는 테이블을 자동으로 생성시키게 된다.

실무에서는 fk 정보외에도 다른 다양한 데이터들을 더 담아야 할 일이 생기므로 가급적 ManyToMany 사용시 중간테이블을 꼭. 직접 만들어서 사용하는것이 좋다.

- Django
  - ManyToManyField() 사용시 through 옵션 무조건 줘서, 직접 중간테이블을 관리하자.
- Spring
  - @ManyToMany 어노테이션 사용을 지양하고, OneToMany, ManyToOne 어노테이션을 사용해서 직접 중간테이블을 만들자.







**Django**

```python
from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.CharField(max_length=50, null=True)
    poster_path = models.URLField(max_length=1000, blank=True)
    backdrop_path = models.URLField(max_length=1000, blank=True)
    adult = models.BooleanField()
    vote_average = models.IntegerField()

    like_users = models.ManyToManyField(
      settings.AUTH_USER_MODEL,
      related_name='like_movies'
    )
    genre = models.ManyToManyField(Genre, related_name='movies')


class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                              related_name='reviews'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, # 유저가 삭제되면 리뷰도 삭제됨.
                             related_name='reviews'
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews') # related : 유저가 좋아요한 리뷰들


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
```





**Spring**

```java
package jpabook.jpashop.domain;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.ArrayList;
import java.util.List;

import jpabook.jpashop.domain.Address;
import jpabook.jpashop.domain.Order;


@Entity
@Getter @Setter
public class Member {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "member_id")
    private Long id;

    private String name;

    @Embedded
    private Address address;

    @OneToMany(mappedBy = "member")  // order Table(Entity) 에 있는 member field 에 의해 매핑이 되었다. (읽기 전용)
    private List<Order> orders = new ArrayList<>();

}



@Entity
@Getter @Setter
@Table(name = "orders")
public class Order {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "order_id")
    private Long id;

    @ManyToOne
    @JoinColumn(name = "member_id")
    private Member member;

    @OneToMany(mappedBy = "order")
    private List<OrderItem> orderItems = new ArrayList<>();

    @OneToOne
    @JoinColumn(name = "delivery_id")
    private Delivery delivery;

    private LocalDateTime orderDate;

    @Enumerated(value = EnumType.STRING)
    private OrderStatus status;  // 주문상태 (ORDER, CANCEL)
}
```







# 느낀점

- 개인적으로 장고로 커리어를 시작하고, 스프링을 뒤늦게 배우는 입장인지라, Django 코드가 더 눈에 잘들어옵니다.
- 스프링이나 장고나 하는 역할은 비슷한데, 스프링 진영에서는 Annotation 으로 옵션을 지정해줘야 하는곳이 너무 많은것 같습니다.
