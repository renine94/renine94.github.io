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

title: "[spring] 스프링에서 쓰이는 용어에 대해 정리해보자."
excerpt: "🚀 spring, django 두개 프레임워크를 비교하는 형식으로 포스팅"

categories: spring
tag: [spring, word]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Spring 에서 쓰이는 용어 비교

> Spring, Django 프레임워크에서 쓰이는 용어 정리



서로 쓰이는 용어가 계속 다르다보니, 직접 정리할겸 도표형식으로 만들어봤습니다.



|                |                Spring                 |           Django            |
| :------------: | :-----------------------------------: | :-------------------------: |
|      orm       |                  JPA                  |          djangoORM          |
|    template    |          thymeleaf, mustache          |            Jinja            |
|     redis      |                lettue                 |            redis            |
| elasticsearch  |       spring-data-elasticsearch       |        elasticsearch        |
|     model      |                entity                 |            model            |
|  http client   |          restTemplate, Feign          |          requests           |
|      설정      | Application.yml, application.property | settings (local.py, etc...) |
| packageManager |             Maven, gradle             |             pip             |
|     build      |                complie                |         interpreter         |
|      was       |                tomcat                 |      gnicorn, uvicorn       |
|                |              annotation               |          decorator          |
|                |                rombok                 |                             |
|                |                  dto                  |                             |
|                |    controller, service, repository    |                             |
|                |                 bean                  |                             |
|                |               singleton               |                             |
|                |                                       |         Serializer          |
|      Test      |            Junit4, Junit5             |      Unittest, Pytest       |
|                |          Interceptor, Filter          |    Middleware, (signal)     |





## Spring

- 출처
  - [velog](https://velog.io/@juhyeon1114/%EC%8A%A4%ED%94%84%EB%A7%81%EC%9D%98-%EA%B5%AC%EC%A1%B0%EC%99%80-%EC%9A%94%EC%B2%AD-%ED%9D%90%EB%A6%84)

![img](https://velog.velcdn.com/images/juhyeon1114/post/a1287592-e665-4476-9c53-2533a832100e/image.jpg)

## Django

![image-20230202120017653](../../assets/images/posts/2023-02-02-summary word in spring/image-20230202120017653.png)