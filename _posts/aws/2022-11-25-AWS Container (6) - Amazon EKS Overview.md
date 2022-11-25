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

title: "[aws] Container ECS, Fargate, ECR, EKS (6) - Amazon EKS Overview"
excerpt: "🚀 AWS Container, EKS, Kubernetes, Pod, Node"

categories: aws
tag: [aws, container, docker, eks, kubernetes, pod]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. Amazon EKS

> AWS 에 컨테이너를 실행하는 다른 방법을 알아보자.

- Amazone Elastic Kubernetes Service
- AWS 에서 관리형 Kubernetes 클러스터를 실행하는 방법 (EKS)
- 쿠버네티스란 오픈소스 시스템으로서, 컨테이너화된 애플리케이션 즉 일반적으로 도커 등을 자동으로 배포, 스케일링, 그리고 관리할 수 있습니다.
- **ECS의 대안으로 사용되는데 컨테이너를 실행하려는 목적은 비슷하지만 API는 아주 다르다.**
- 즉 ECS는 절대 오픈소스가 아니지만 Kubernetes 는 오픈소스이며 일종의 규격화를 제공하는 다양한 클라우드 공급자가 사용한다.



- EKS 는 2가지 실행 모드를 지원합니다.
  1. EC2 실행모드
     - EC2 인스턴스 등 작업자 노드를 배치할 때
  2. Fargate 모드
     - EKS 클러스터에 서버리스 컨테이너를 배치할 때
- EKS의 사용사례

회사가 이미 온프레미스에서 Kubernetes를 사용하거나 다른 클라우드에서 Kubernetes를 쓰는 경우 혹은 그냥 Kubernetes API 를 사용하려는 경우 AWS를 통해 Kubernetes 클러스터를 관리하고자 할 때 Amazon EKS 를 사용할 수 있습니다.



- 시험에서 Kubernetes 특징은 **Cloud-agnostic**이다.
  - Azure 나 Google Cloud 등 어떤 클라우드에서도 가능하다.
- 클라우드나 컨테이너 사이를 옮겨 다니려면 Amazon EKS를 사용하는것이 훨씬 편하다.



# 02. Amazon EKS - Diagram

![image-20221125164936659](../../assets/images/posts/2022-11-25-AWS Container (6) - Amazon EKS Overview//image-20221125164936659.png)

- VPC가 있고, AZ(가용영역) 3개는 public & private 서브넷으로 나뉩니다.
- EKS Worker Node 를 만든다. (그림예시에서는 EC2 인스턴스로 만듬)
- 그리고, 각 Node는 Pod를 실행할 것이다.



- ECS Task 와 비슷하지만 이름을 살펴보면 Pods가 보인다면 쿠버네티스와 관련있는 것이다.
- EKS Pod가 EKS Node에서 실행 중인데, ASG이 이 Node를 관리합니다.
- 그러면 ECS와 비슷하게 EKS서비스를 쿠버네티스 서비스에서 노출하려면 Private LB 를 설정하거나, Public LB 를 설정해서 웹과 연결할 수 있습니다.

