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

title: "[spring] 스프링에서 요청 데이터를 받는 여러가지 방법에 대해 알아보자."
excerpt: "🚀 spring, pathVariable, RequestParam, RequestBody"

categories: spring
tag: [spring, request]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Spring 요청 데이터 받기

> - url 경로로 데이터 받기
> - query_string (= query_parameter) 로 데이터 받기
> - body 에 보낸 데이터 받기



클라이언트 쪽에서 스프링으로 데이터를 보내는 방법 3가지에 대해 소개한다.



## 00. TL; DR

| @PathVariable |    @RequestParam    |          @RequestBody           |
| :-----------: | :-----------------: | :-----------------------------: |
|  /user/{id}   | /user?name=renine94 |              /user              |
|               |                     | {"name": "renine94", "age": 30} |







## 01. URL 경로에서 데이터 받기

- `@PathVariable`
  - required = false

```java
// https://localhost:8080/api/v1/user/777


@RestController
@RequestMapping("api/v1")
public class UserController {
  
  @GetMapping("/user/{id}")
  public String getUser(@PathVariable int id) {
    
    return "hello world! userId: " + id
  }
}
```





## 02. 쿼리파라미터로 데이터 받기

> 어느곳에서는 query_string 으로도 부르는 곳이 있다.

- `@RequestParam`
  - required = false
  - ex) ?name=jaegu&age=30



```java
// https://localhost:8080/api/v1/user?name=jaegu&age=30


@RestController
@RequestMapping("api/v1")
public class UserController {
  
  @GetMapping("/user")
  public String getUser(@RequestParam String name, @RequestParam int age) {

    return "hello world! name: " + name + " age: " + age
  }
}
```



## 03. 요청 Body에 데이터보낸 데이터 받기

- `@RequestBody`
- 받는데이터가 복잡할때 사용된다. 예를 들어 오브젝트 자료형처럼 통쨰로 요청에 보내고 싶은 경우가 이에 해당한다.
- 보통 DTO 형태로 데이터를 받기 때문에 DTO 를 미리 만들어두어야 한다.

```java
// https://localhost:8080/api/v1/user
{
  "name": "renine94",
  "age": 30
}


@RestController
@RequestMapping("api/v1")
public class UserController {
  
  @GetMapping("/user")
  public String getUser(@RequestBody RequestDTO requestDTO) {
		String name = requestDTO.getName()
    int age = requestDTO.getAge()
    return "hello world! name: " + name + " age: " + age
  }
}
```



