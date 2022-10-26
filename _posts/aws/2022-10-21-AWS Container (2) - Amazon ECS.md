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

title: "[aws] Container ECS, Fargate, ECR, EKS (2) - Amazon ECS"
excerpt: "🚀 AWS Container, ECS, Elastic Container Service, EC2, Fargate"

categories: aws
tag: [aws, container, docker, ecs, fargate]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. Amazon ECS - EC2 Launch Type

> EC2 시작유형에 대해 살펴보자.

![image-20221020020140062](../../assets/images/posts/2022-10-21-AWS Container (2) - Amazon ECS//image-20221020020140062.png)

- ECS = Elastic Container Service
- **AWS 에서 컨테이너를 실행하면 ECS 클러스터에, 이른바 ECS Task(태스크) 를 실행하는 것**
- EC2 클러스터에는 EC2 시작유형, 바로 EC2 인스턴스이다.
- EC2 시작유형으로 EC2 클러스터를 사용할 때는 인프라를 직접 프로비저닝하고 유지해야 한다.
- 즉, ECS 및 **ECS클러스터가 여러 EC2 인스턴스로 구성**되게 된다.

<br>

- 이때, ECS 인스턴스는 특별하게 각각 ECS Agent 를 실행해야 한다.
- 그럼 **ECS Agent가 각각의 EC2 인스턴스를 Amazon ECS 서비스와 지정된 ECS 클러스터에 등록**한다.
- 이후에 ECS Task 를 수행하기 시작하면, AWS가 컨테이너를 시작하거나 멈출 것이다.
- 즉, 새 도커 컨테이너가 생기면 사진에서 볼 수 있듯 시간에 따라 EC2 인스턴스가 지정될것이다.
- ECS Task 를 시작하거나, 멈추면 자동으로 위치가 지정된다. 바로 이게 EC2 Launch Type 이다. (시작유형)
- 도커 컨테이너는 미리 프로비저닝한 Amazon EC2 인스턴스에 위치한다.



# 02. Amazon ECS - Fargate Launch Type

> 두번째 유형으로는 Fargate 시작유형에 대해 알아보자.

![image-20221020020351777](../../assets/images/posts/2022-10-21-AWS Container (2) - Amazon ECS//image-20221020020351777.png)



- 마찬가지로 AWS에 도커 컨테이너를 실행하는데, 이번에는 인프라를 프로비저닝하지 않아 관리할 EC2 인스턴스가 없다.
- 즉 서버리스 이다.
- 서버를 관리하지 않아 서버리스라 부르는데, 서버가 없는것은 아니다.
- Fargate 유형은 ECS 클러스터가 있을 때 ECS Task를 정의하는 Task Definition (태스크 정의)만 생성하면 AWS가 필요한 CPU나 RAM에 따라 ECS 태스크를 대신 실행합니다.
- 즉, 새 도커 컨테이너를 실행하면 어디서 실행되는지 알리지 않고 그냥 실행됩니다.
- 작업을 위해 백엔드에 EC2 인스턴스가 생성될 필요도 없다. (아주 신기함 ㅎ)
- **확장하려면 간단하게 Task 수만 늘리면 된다.**
- EC2 인스턴스를 관리할 필요가 없다.



- 시험에서는 서버리스인 Fargate 를 사용하라는게 자주 나온다.
- EC2 시작유형보다 관리가 쉽기 때문이다.

# 03. Amazon ECS - IAM Roles for ECS

> Amazon ECS 의 2가지 시작유형을 알아보았으니, ECS Task에 IAM 역할에 대해 알아보도록 하자

![image-20221020020949349](../../assets/images/posts/2022-10-21-AWS Container (2) - Amazon ECS//image-20221020020949349.png)

- **EC2 Instance Profile**

  - EC2 시작유형에서만 사용됨 (Fargate 는 사용안함)
  - EC2 인스턴스가 Docker, ECS Agent 2개를 실행한다고 하고, EC2 시작유형을 사용한다면
  - EC2 인스턴스 프로파일을 생성하게 된다.
  - ECS Agent가 EC2 인스턴스 프로파일을 이용해 API 호출을 만들게 된다.
  - 그럼 인스턴스가 저장된 ECS 서비스가 CloudWatch 로그에 API 호출을 해서 컨테이너 로그를 보내고,<br>ECR 로부터 도커 이미지를 가져온다.
  - Secret Manager 또는 SSM Parameter Store 에서 환경변수 or 민감데이터를 참고하기도 한다.

  <br>

- **ECS Task Role**

  - ECS Task는 각각 ECS Task Role 를 가지게 된다.
  - 이것은 EC2 와 Fargate 시작유형 모두 해당되며 두 개의 태스크가 있다면 각자의 특정 역할을 만들수있다.
  - 위의 그림에 모자처럼 태스크A 는 EC2 태스크 A 역할을 맡고, 태스크B는 EC2 태스크 B역할을 맡는다.
  - 역할을 다르게 하는 이유
    - 역할이 각자 다른 ECS 서비스에 연결할 수 있게 하기 때문
    - 예를들어, EC2 태스크 A역할은 태스크 A가 S3에 API 호출을 실행할수 있또록 한다면
    - 태스크 B는, DynamoDB에 API를 호출을 실행할 수 있도록 한다.

  - ECS 서비스의 Task Definition 에서 Task Role 을 정의할 수 있다.

  

  EC2 프로파일 역할과 ECS 태스크 역할의 차이점을 기억해야 한다.

  

  

  # 04. Amazon ECS - Load Balancer Integrations

  > ECS 로드밸런서 통합에 대해 알아보자.

![image-20221025000629403](../../assets/images/posts/2022-10-21-AWS Container (2) - Amazon ECS//image-20221025000629403.png)

- EC2 시작유형으로 예시를 들어 설명하지만, Fargate 시작유형도 마찬가지이다.
- 여기 여러 ECS 태스크들이 실행되며, ECS 클러스터 안에 있습니다.
- HTTP나 HTTPS 엔드 포인트로 태스크를 사용하기 위해 ALB 를 앞에서 실행하면 모든 사용자들이 ALB 및 백엔드의 ECS 태스크에 바로 도달한다.
- ALB 는 이런 경우를 포함해 대부분의 사용사례를 지원한다.



- 네트워크 로드 밸런서(NBL) 는 처리량이 매우 많거나 높은 성능이 요구될 때만 권장한다.
- AWS Private Link와 사용할 떄도 권장한다.
- 오래된 세대인 ELB는 사용할수 있지만 권장하지 않는다.
  - 고급 기능이 없을뿐더러 Fargate 와는 연결할 수가 없다.
  - 반면 ALB 는 Fargate 와도 사용할 수 있다.



# 05. Amazon ECS - Data Volumes (EFS)

> ECS 의 데이터 지속성에 대해 알아보자

![image-20221025001025211](../../assets/images/posts/2022-10-21-AWS Container (2) - Amazon ECS//image-20221025001025211.png)

- 데이터 볼륨이 필요하며 여러 종류가 있는데 그 중 하나가 EFS에서 자주 사용된다.
- ECS 클러스터에 EC2 인스턴스와 Fargate 시작유형 둘다 구현했다고 가정한다.
- EC2 태스크에 파일 시스템을 마운트해서 데이터를 공유하려고 한다.
  - EFS 파일 시스템을 사용하는게 좋다
  - 네트워크 파일 시스템이라 EC2 와 Fargate 모두 호환이 되고,
  - EC2 태스크에 파일 시스템을 직접 마운트할 수 있다.
- 어느 AZ에 실행되는 태스크든 Amazon EFS 에 연결되어 있다면 데이터를 공유할거고 원한다면 파일시스템을 통해 다른 태스크와 연결할 수 있기 때문이다.
- **따라서 Fargate 로 서버리스방식으로 ECS 태스크를 실행하고 파일 시스템 지속성을 위해 Amazon EFS 를 사용하는게 가장 좋다.**



- EFS 역시 서버리스이기 때문에 서버를 관리할 필요가 없고 미리 비용을 지불한다.
- 미리 프로비저닝하면 문제가 없다.
- 사용사례로는 EFS 와 ECS를 함께 사용해서 다중 AZ가 공유하는 컨테이너의 영구 스토리지가 있다.
- 시험에서 주의할점은 현재 ECS 가 Lustre용 FSx는 지원하지 않는다.
- **또 ECS 태스크의 파일 시스템으로 Amazon S3 버킷을 마운트할수 없다.**



