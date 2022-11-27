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

title: "[aws] Container ECS, Fargate, ECR, EKS (7) - Quiz"
excerpt: "🚀 AWS Container, Quiz, summary"

categories: aws
tag: [aws, container, docker, quiz]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. Quiz



- 온프레미스로 호스팅된 다중 도커 기반의 애플리케이션이 있으며, 이를 AWS로 이전시키려 합니다. 여러분은 인프라를 프로비저닝하거나 관리할 의향이 없으며, 그냥 컨테이너를 AWS 상에서 실행하려고 합니다. 이 경우, 다음 중 어떤 AWS 서비스를 선택해야 할까요?

1. ECS
2. ECR
3. **AWS Fargate**
   - AWS Fargate를 사용하면 서버를 관리할 필요 없이 AWS 상에서 컨테이너를 실행할 수 있습니다.
4. EKS

<br>

---

- Amazon Elastic Container에는 두가지 시작(실행) 유형이 있다. ??? 와 ??? 입니다.

1. **Amazon EC2 실행 유형과 Fargate 실행 유형**
   - EC2, Fargate(serverless)
2. Amazon EC2 실행 유형과 EKS 실행유형
3. Fargate 실행유형과 EKS 실행유형

<br>

---

- ECS 클러스터(EC2 실행 유형) 상에 호스팅된 애플리케이션이 있습니다. 여러분은 ECS 태스크가 S3 버킷으로 파일을 업로드하게 하려 합니다. 이를 위해서는 다음 중 어떤 ECS 태스크 용 IAM 역할을 수정해야 할까요?

1. EC2 인스턴스 프로파일
2. **ECS 태스크 역할**
   - ECS 태스크 역할은 ECS 태스크 자체가 사용하는 IAM 역할입니다. 컨테이너가 S3, SQS 등의 다른 AWS 서비스를 호출하려 할 때 사용합니다.

  <br>

---

- 도커 컨테이너 상에서 실행 중인 WordPress 웹사이트를 온프레미스에서 AWS로 이전하려 합니다. ECS 클러스터에서 애플리케이션을 실행하기로 했으나, 도커 컨테이너가 웹사이트 파일, 이미지, 영상을 비롯한 동일한 WordPress 웹사이트 콘텐츠에 액세스할 수 있게끔 하려 합니다. 이를 위해서는 어떤 방법이 권장될까요?

1. **EFS 볼륨 마운트**
   - EFS 볼륨은 서로 다른 EC2 인스턴스와 서로 다른 ECS 태스크간의 공유가 가능
   - 컨테이너의 영구적인 다중 AZ 공유 스토리지로 사용될 수 있다.
2. EBS 볼륨 마운트
3. EC2 인스턴스 스토어 사용

  <br>

---

- EC2 인스턴스로 구성된 ECS 클러스터 상에 애플리케이션을 배포하려 합니다. 현재, 클러스터는 DynamoDB에 대한 API 호출을 성공적으로 발행한 애플리케이션 하나를 호스팅하고 있습니다. S3로의 API 호출을 발행하는 두 번째 애플리케이션을 추가하려는데, 권한 부여 관련 문제가 발생했습니다. 이 문제를 해결하고 적절한 보안을 유지하기 위해서는 어떤 방법을 사용해야 할까요?

1. EC2 인스턴스 역할을 수정해 S3에 대한 권한추가
2. **새 애플리케이션을 위한 IAM 역할 생성**
3. Fargate 모드 활성화
4. ECS 태스크를 허용하도록 S3 버킷 정책 수정



<br>

---

- Application Load Balancer (ALB) 가 동일한 ECS 컨테이너 인스턴스에서 실행중인 다수의 ECS 태스크로 트래픽을 리다이렉트하게 만들기 위해서는 다음 중 어떤 기능이 사용해야 될까요?

1. **동적 포트 매핑**
2. 자동 포트 매핑
3. ECS 태스크 정의
4. ECS 서비스



<br>

---

- 온프레미스 도커 기반 애플리케이션을 Amazon ECS 로 이전하려 한다. 여러분은 도커 허브 컨테이너 이미지 라이브러리를 컨테이너 이미지 리포지토리로 사용하고 있었다. 다음의 대체 AWS 서비스들중 Amazon ECS 와 완전히 통합되어 있는 서비스는 무엇일까요?

1. AWS Fargate
2. **Elastic Container Registry (ECR)**
3. Elastic Kubernetes Services (EKS)
4. Amazon EC2



