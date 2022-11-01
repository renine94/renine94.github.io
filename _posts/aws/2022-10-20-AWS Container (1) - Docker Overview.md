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

title: "[aws] Container ECS, Fargate, ECR, EKS (1) - Docker Overview"
excerpt: "🚀 AWS Container Service - Docker 개요 학습"

categories: aws
tag: [aws, container, docker, overview]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# 01. What is Docker?

> 이번 섹션에서는 도커 ECS 및 EKS 를 학습한다.

- 앱 배포를 위한 소프트웨어 개발 플랫폼이다. (컨테이너 기술)
- 컨테이너에 앱이 패키징되는데, 컨테이너는 표준화되어있어 아무 OS 에서나 실행가능
- 앱이 컨테이너에 패키징되면 어느 OS에서든 같은 방식으로 실행된다.
  - Any machine
  - 호환성 문제가 없다.
  - 행위 특성도 예측가능
  - 작업을 덜어준다.
  - 유지 및 배포가 쉽다.
  - 언어, 운영체제, 기술에 상관없이 실행이 가능하다.
- 사용 사례
  - 마이크로서비스 아키텍쳐 MSA
  - 온프레미스에서 클라우드로 앱을 Lift - And - Shift 하기도 함
  - 컨테이너를 실행하는 어떤 경우에도 사용가능



# 02. Docker on an OS

> 도커는 운영체제에서 어떻게 작동하는지 살펴보자.

![image-20221020013506855](../../assets/images/posts/2022-10-20-AWS Container (1) - Docker Overview//image-20221020013506855.png)



- 우선 서버가 있다. (ex. EC2)
  - 어떤 유형의 서버든 똑같다. (EC2 예시)
- 도커 에이전트를 실행하면 도커 컨테이너를 시작할 수 있다.
- 1번 째 도커 컨테이너는 Java App을 포함
- 2번 째 도커 컨테이너는 Node.js App이 있다.
- 다수의 도커 컨테이너가 동시에 실행될 수 있다.

<br>

- Java App을 가진 여러 Docker Container 가 있을 수 있다.
- Node.js를 가진 여러 도커 컨테이너가 있을수도 있다.
- 도커 내에서도 MySQL 등의 DB도 실행가능하니, 아주 다용도로 활용된다.
- **서버 관점에서는 모두 도커 컨테이너로 보인다.**



# 03. Where are Docker images stored?

> 도커 이미지는 어디에 저장되는지 알아보자

- 도커 이미지는 도커 레포지토리 라는 곳에 저장된다.
- 여러 옵션이 있다.
  1. **Docker Hub**
     - 유명한 퍼블릭 레포지토리
     - 많은 기술에 맞는 기본 이미지를 찾을 수 있다.
     - Ubuntu or MySQL 과 같은 OS용 기본 이미지도 마찬가지
  2. **Amazon ECR (Elastic Container Registry)**
     - 프라이빗 레포지토리
     - 비공개 이미지를 실행 할 수 있다.
     - Amazon ECR Public Gallery 라 불리는 퍼블릭 레포지토리 옵션도 있다.



# 04. Docker vs Virtual Machines

> 도커와 가상머신에 차이

- 도커 역시 가상화 기술의 일종이긴 하지만, 순전히 가상화 기술은 아니다.
- 리소스가 호스트와 공유되어 한 서버에서 다수의 컨테이너를 공유할 수 있다.

![image-20221020014137257](../../assets/images/posts/2022-10-20-AWS Container (1) - Docker Overview//image-20221020014137257.png)



1. **가상머신**

   - 가상 머신의 아키텍처를 살펴보면 인프라와 호스트 운영체제가 있으며, 그 위에 하이퍼바이저가 있고 앱과 Guest 운영체제가 있다. EC2의 원리이다.

   - 다시말해, EC2 머신은 하이퍼바이저에 실행되는 가상머신과도 같다.

   - 그래서 Amazon이 EC2 인스턴스를 다양한 소비자에게 제공할 수 있으며, 가상머신의 EC2 인스턴스는 각자 분리되어있다.

   - **리소스를 공유하지 않는다.**

2. **도커**

   - 도커 컨테이너의 경우 인프라와 EC2인스턴스 같은 호스트OS가 있고 도커 Daemon 위에 많은 컨테이너가 있다.
   - 도커 Daemon에서 가볍게 실행되는 컨테이너라 공존할 수 있게 된다.
   - 네트워킹이나 데이터 등을 공유할수도 있다.
   - 소위 말해, 가상머신보다 덜 안전하지만, 하나의 서버에 많은 컨테이너를 실행할 수 있기 때문에 도커컨테이너를 많이 사용한다.



## 05. Getting Started with Docker

> 도커를 시작해보자.

![image-20221020014641443](../../assets/images/posts/2022-10-20-AWS Container (1) - Docker Overview//image-20221020014641443.png)

1. 도커를 시작하려면 우선 Dockerfile 을 작성해야 한다.
   - 도커 컨테이너를 구성하는 파일이다.
2. 베이스 도커 이미지에 몇 가지 파일을 추가해서 구축하면 도커 이미지가 된다.
3. 도커 image는 푸시(push)해서 도커 레포지토리에 저장할 수 있다. (DockerHub, AmazonECR)
4. 도커 레포지토리에서 image를 pull 받아서 컨테이너화 시킨다.



## 06. Docker Containers Management on AWS

> AWS에서 제공하는 도커 컨테이너 서비스를 알아보자.

![image-20221020014925977](../../assets/images/posts/2022-10-20-AWS Container (1) - Docker Overview//image-20221020014925977.png)

1. **Amazon ECS**
   - 도커 관리를 위한 Amazon 전용 플랫폼
   - 다음 포스팅에 자세히 알아보도록 한다.
2. **Amazon EKS**
   - 쿠버네티스 서비스.
   - 쿠버네티스의 관리형 버전으로 오픈소스 프로젝트입니다.
   - 추후 간단히 살펴볼 예정
3. **AWS Fargate**
   - Amazon의 Serverless 컨테이너 플랫폼
   - ECS 와 EKS 둘다 함께 작동할 수 있다.
   - 추후 자세히 포스팅 예정
4. **Amazon ECR**
   - 도커 컨테이너 이미지를 저장하는데 사용







