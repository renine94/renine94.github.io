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

title: "[spring] 스프링에서 Model 설계, Entity 매핑하는 여러가지 방법 (1)"
excerpt: "🚀 spring, @Entity, @Column, @ManyToOne, etc... 모델설계 방법"

categories: spring
tag: [spring, model, jpa, entity, mapping]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA - Entity 매핑

- 객체와 테이블 **@Entity** **Table**
- 필드와 컬럼 **@Column**
- 기본 키 **@Id**
- 연관관계 **@ManyToOne**, **@JoinColumn**



## 00. 데이터베이스 스키마 자동 생성

> 운영환경에서 사용X, 개발단계에서 ok

- DDL 을 애플리케이션 실행 시점에 자동 생성
- 테이블 중심 -> 객체 중심
- 데이터베이스 방언(dialect) 을 활용해서 데이터베이스에 맞는 적절한 DDL 생성
- 이렇게 **생성된 DDL은 개발 장비에서만 사용**
- 생성된 DDL 은 운영서버에서는 사용하지 않거나, 적절히 다듬어서 사용



***application.yml 옵션**

- hibernate.hbmddl.auto
- 개발단계에서는 create 사용가능하나, 운영에서는 사용하지 않는걸 권장

|   Option    |                       Description                       |
| :---------: | :-----------------------------------------------------: |
|   create    |      기존 테이블 삭제 후 다시 생성 (Drop + Create)      |
| create-drop |         create와 같으나 종료시점에 테이블 Drop          |
|   update    | 변경분만 반영 (**운영DB에 사용하면 안됨**) 추가만 된다. |
|  validate   |     **엔티티와 테이블이 정상 매핑되었는지만 확인**      |
|    none     |                      사용하지 않음                      |





## 01. @Entity

- @Entity가 붙은 클래스는 JPA가 관리, 엔티티라 한다.
- JPA를 사용해서 테이블과 매핑할 클래스는 @Entity 필수
- 주의
  - 기본 생성자 필수 (parameter가 없는 public or protected 생성자)
  - Final 클래스, enum, interface, inner 클래스에 사용 X
  - 저장할 필드에 final 사용 X



## 02. @Table

- 지정하면 실제 DB 테이블 이름과 매핑
- 엔티티와 매핑할 테이블 지정
- @Table(name = "table_name01")  으로 설정하면 쿼리조회시 from 절에 table_name01 로 쿼리가 나가게 된다.
- 옵션
  - name : 매핑할 테이블 이름
  - catalog : 데이터베이스 catalog 매핑
  - schema : 데이터베이스 schema 매핑
  - uniqueConstraints : DDL 생성 시 유니크 제약 조건 생성



## 03. @Column

- 제약 조건을 추가할 수 있다.
- 옵션
  - name : 컬럼명 변경
  - unique : true/false
  - length : 최대글자수
  - nullable : null 허용할지 안할지 true/false



DDL 생성 기능은 DDL을 생성할 때만 사용되고 JPA의 실행 로직에는 영향을 주지 않는다.



유니크 제약 조건 추가

```java
@Table(uniqueConstraints = {
  @UniqueConstraint(name = "NAME_AGE_UNIQUE", 
                    columnNames = {"NAME": "AGE"})
})
```



<br>
<br>
<br>


---

여담이지만 python web framework 인 django 에서는 

```python
class User(models.Model):
  name = models.CharField()
  age = models.CharFields()

  class Meta:
    unique_together = ("name", "age")

```



위와 같이 설정할 수 있음. django4.0 이후부터는 unique_together 말고 UniqueConstrains 를 사용하라하는데, 자세한건 직접 찾아보시길 바랍니다...







