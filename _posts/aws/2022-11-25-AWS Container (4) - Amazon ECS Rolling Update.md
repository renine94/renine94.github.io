---
layout: single

header:
  teaser: /assets/images/logo/aws.png
  overlay_image: /assets/images/logo/aws.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[aws] Container ECS, Fargate, ECR, EKS (4) - Amazon ECS Rolling Updates"
excerpt: "🚀 AWS Container, ECS, Rolling Update, 블루그린 배포 등등"

categories: aws
tag: [aws, container, docker, ecs, deploy, rolling, blue_green]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. ECS Rolling Updates

> 배포전략중 하나인 Rolling Updates 에 대해 알아보자.
>
> - Rolling Updates
> - Blue Green Deploy
> - etc....

- ECS Service를 v1에서 v2로 업데이트할 때, Task가 한 번에 얼마나, 어떤 순서로 시작되고 중지되는지 제어 가능
- ECS 업데이트를 보면 새로운 Task Definition 의 개수를 선택하고, ECS 서비스를 업데이트할 때 두 가지 설정이 있다.
  - 최소 정상 백분율 및 최대 백분율 입니다.
  - 기본적으로 100, 200 인데 무슨뜻인지 살펴보자



**Example**

---

**첫번째 예**

- 최소 정상 백분율 : 50%
- 최대 백분율 : 100%
- 실행중인 Task 4개

![image-20221125014415970](../../assets/images/posts/2022-11-25-AWS Container (4) - Amazon ECS Rolling Update//image-20221125014415970.png)

1. v1 Task 4개
2. 2개종료후, 2개 남아있음 (50%)
3. 다시 v2 Task 2개생성 (100%)
   - v1 2개
   - v2 2개
4. 4개

<br>

**두번째 예**

- 최소 정상 백분율: 100%
- 최대 백분율: 150%
- 실행중인 Task 4개

![image-20221125014855508](../../assets/images/posts/2022-11-25-AWS Container (4) - Amazon ECS Rolling Update//image-20221125014855508.png)

1. v1 Task 4개
2. v2 Task 2개 생성 (총 6개 150%)
3. v1 Task 2개 종료 (총 4개, 100%, v1 2개, v2 2개)
4. v2 Task 2개 생성 (총 6개 150%, v1 2개, v2 4개)
5. v1 Task 2개 종료 (총 4개, 100%, v2 4개)



