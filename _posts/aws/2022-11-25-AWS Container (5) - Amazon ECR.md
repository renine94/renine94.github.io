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

title: "[aws] Container ECS, Fargate, ECR, EKS (5) - Amazon ECR"
excerpt: "🚀 AWS Container, ECR, Elastic Container Registry, DockerHub 비슷"

categories: aws
tag: [aws, container, docker, ecr, dockerhub, registry, image]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. Amazon ECR

> Elastic Container Registry 의 줄임말 ECR

- AWS 에 Docker Image 를 저장하고, 관리하는데 사용된다.
- Docker Hub, Amazon ECR 등 역할이 같으며, ECR 에도 이미지를 저장할 수 있다.

![image-20221125020134051](../../assets/images/posts/2022-11-25-AWS Container (5) - Amazon ECR//image-20221125020134051.png)





- ECR 에는 2가지 옵션이 있다.
  1. 계정에 한해 **이미지를 비공개로 저장**, 여러 계정으로 설정할 수도 있다.
  2. **public 저장소**를 사용해 Amazon ECR Public Gallery 에 게시하는 방법
- **ECR 은 Amazon ECS 와 완전히 통합**되어 있다.
- **Image는 Background에서 Amazon S3 에 저장**됩니다.



- ECS 클러스터의 EC2 인스턴스 (or Fargate) 에 이미지를 끌어오기 위해서는 EC2 인스턴스에 IAM 역할을 지정하면 된다.
- IAM Role 이 Docker Image를 인스턴스에 끌어올 것이다.
- ECR에 대한 모든 접근은 IAM이 보호하고 있다.
- ECR에 권한 에러가 생긴다면 정책을 살펴봐야 한다.



- EC2 인스턴스에 이미지를 끌어온 후에는 컨테이너가 시작된다.
- ECS와 ECR이 이런 식으로 함께 작동한다.
- Amazon ECR은 단순히 저장하는 리포지토리에 그치지않고, 이미지의 취약점 스캐닝, 버저닝 태그 및 수명 주기 확인을 지원합니다.



**결론**

- 도커 이미지를 저장할 때는 ECR을 기억하면 된다. (DockerHub 같은 곳임)
- 여기다 저장하고, ECS 에서 ECR에 저장된 도커이미지 끌어와서 컨테이너 실행할수 있음 (IAM 역할 필요)
- ECR 에 저장되는 이미지는 S3 에 저장됨
