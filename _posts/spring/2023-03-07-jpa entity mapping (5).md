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

title: "[spring] 스프링 JPA - 영속성 전이 & 고아 객체"
excerpt: "🚀 spring, 영속성 전이(Cascade), 고아 객체(orphanRemoval) 에 대해 알아보자."

categories: spring
tag: [spring, model, jpa, entity, mapping]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA

- 영속성 전이 : cascade
- 고아객체  : orphanRemoval



# 01. 영속성 전이: CASCADE

- 특정 엔티티를 영속 상태로 만들 때 연관된 엔티티도 함께 영속 상태로 만들고 시을 때,
- 부모 엔티티를 저장할때, 자식 엔티티도 함께 저장
- 종류 (ALL, PERSIST 를 많이 쓴다.)
  - `ALL` : 모두 적용
  - `PERSIST` : 영속
  - `REMOVE` : 삭제
  - `MERGE` : 병합
  - `REFRESH` : refresh
  - `DETACH` : detach





## 1) CASCADE - ALL

- Entity

```java
@Entity
public class Parent {
  
  @Id
  @GeneratedValue
  private Long id;
  
  private String name;
  
  // ALL 로 선언하면 Parent 를 저장할때 Child 에도 persist 를 날려주겠다는 의미이다.
  @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL)
  private List<Child> childList = new ArrayList<>();
  
  public void addChild(Child child) {
    childList.add(child);
    child.setParent(this);
  }
}
```

- Logic

```java
Child child1 = new Child();
Child child2 = new Child();

Parent parent = new Parent();
parent.addChild(child1);
parent.addChild(child2);

em.persist(parent);  // CASCADE ALL 이면 parent 를 저장할때, Child1, 2 도 함께 저장 된다.
```





- 사용 전제
  - Parent 와 Child 의 라이프사이클이 유사할 때,
  - **단일 소유자 - 소유자가 1명일때, Parent 엔티티만 Child를 소유할 때,**





# 02. 고아 객체 : orphanRemoval

- 고아 객체 제거 : 부모 엔티티와 연관관계가 끊어진 자식 엔티티를 자동으로 삭제

- **orphanRemoval = true**

- code

  ```java
  @Entity
  public class Parent {
    
    @Id
    @GeneratedValue
    private Long id;
    
    private String name;
    
    // orphanRemoval = true, 부모 자식 객체 연관관계가 끊기면 자식객체를 삭제시킨다.
    @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Child> childList = new ArrayList<>();
    
    public void addChild(Child child) {
      childList.add(child);
      child.setParent(this);
    }
  }
  
  Parent parent1 = em.find(Parent.class, id);
  parent1.getChildren().remove(0);  // 자식엔티티 컬렉션에서 제거 DELETE FROM child WHERE id = ? 쿼리 발생
  ```



**🚀 주의사항**

- 참조가 제거된 엔티티는 다른 곳에서 참조하지 않는 고아 객체로 보고 삭제하는 기능
- **참조하는 곳이 하나일 때 사용해야함!**
- <span style="color: red;">특정 엔티티가 개인 소유할 때 사용</span>
- @OneToOne, @OneToMany 만 가능
- 참고
  - 개념적으로 부모를 제거하면 자식은 고아가 된다. 따라서 고아 객체 제거 기능을 활성화 하면, 부모를 제거할 때 자식도 함께 제거된다. 이것은 CascadeType.REMOVE 처럼 동작한다.
    - `@OneToMany(mappedBy = "parent", orphanRemoval = true)` 이면 부모삭제시 자식들도 모두 삭제됨
    - `@OneToMany(mappedBy = "parent", cascade = CascadeType.ALL)` 이어도 부모삭제시 자식들도 모두 삭제됨
  - Django의 on_delete=models.CASCADE 와 비슷한것 같다.



*Django*

```python
class Parent(models.Model):
	name = models.CharField(max_length=255)

class Child(models.Model):
	parent = models.ForeignKeyField(Parent, on_delete=models.CASCADE)
```



*Spring*

```java
@Entity
@Table(name = "parent")
public class Parent {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

  	// 부모객체가 삭제되어 자식객체가 고아객체가 되면 삭제
    @OneToMany(mappedBy = "parent", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Child> children;

    // getters and setters
}

@Entity
@Table(name = "child")
public class Child {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "parent_id")
    private Parent parent;

    // getters and setters
}

```



<br>

---





**영속성 전이 + 고아 객체, 생명주기**

- `CascadeType.ALL + orphanRemoval = true`
- 스스로 생명주기를 관리하는 엔티티는 `em.persist()`로 영속화, `em.remove()`로 제거
- **두 옵션을 모두 활성화 하면 부모 엔티티를 통해서 자식의 생명주기를 관리할 수 있음**
- 도메인 주도 설계(DDD)의 Aggregate Root 개념을 구현할 때 유용




