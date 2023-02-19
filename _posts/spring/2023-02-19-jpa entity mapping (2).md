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

title: "[spring] 스프링에서 Model 설계, Entity 매핑하는 여러가지 방법 (2)"
excerpt: "🚀 spring, 참조관계 설정, 외래키설정, @ManyToOne, @OneToMany, @ManyToMany"

categories: spring
tag: [spring, model, jpa, entity, mapping, fk]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# JPA - Entity 매핑 (2)

- N:1 `@ManyToOne`
- 1:N `@OneToMany`
- 1:1 `@OneToOne`
- N:M `@ManyToMany`



## 01. 1:N 관계
> SpringBoot 에서 1:N 관계를 어떻게 정의하는지 살펴보자.
> Django 에서 related_name 역참조만 주면 알아서 되는데 스프링은 참 불편하다..

- User (N)
- Team (1)

**Spring**
```java
@Entity
class User {
  @Id
  @GeneratedValue(value = "GenerateType.Strategy")
  private Long id;

  @Column(name = "USERNAME")
  private String username;

  @ManyToOne
  @JoinColumn(name = "team_id")
  private Team team;
}

@Entity
class Team {
  @Id
  @GeneratedValue(value = "GenerateType.Strategy")
  private Long id;

  @Column(name = "NAME")
  private String name;

  @OneToMany(mappedBy = "team")
  private List<Team> teams = new ArrayList<Team>();
}
```
<br>

**Django**
Django 에서는 그냥 N 쪽에 FK 필드주고 related_name 걸면 정참조/역참조 이름이 바로 걸어진다.
개인적으로 Spring 보다 설정이 매우... 간편한것 같음..

```python
class User(models.Model):
  username = models.CharField(max_length=50)
  team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="users")

class Team(models.Model):
  name = models.CharField(max_length=50)
```
