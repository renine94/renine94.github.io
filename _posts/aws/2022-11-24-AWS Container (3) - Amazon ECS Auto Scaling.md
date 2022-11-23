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

title: "[aws] Container ECS, Fargate, ECR, EKS (3) - Amazon ECS Auto Scaling"
excerpt: "🚀 AWS Container, ECS, Auto Scaling, LanchType, EC2, Fargate"

categories: aws
tag: [aws, container, docker, ecs, auto, scaling, fargate, launchType]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# 01. ECS Service Auto Scaling

> ECS 서비스 오토스케일링에 대해 알아보자.

- ECS Task 수를 수동으로 늘릴수도있지만, **자동으로 늘리거나 줄일수도 있다.**
- AWS 의 Auto Scaling 이라는 서비스를 사용하면 3가지 지표에 대해 확장이 가능해진다.
  - 평균 CPU 사용률
  - 평균 메모리 사용률 (RAM)
  - ALB 관련 지표인 타겟당 요청 수 (request count)



- `Target Tracking`: 특정 타겟을 추적하는 대상추적 스케일링
- `Step Scaling`: 특정 CloudWatch 알람에 따라 스케일링
- `Scheduled Scaling`: 미리 ECS 서비스 확장을 설정하는 예약 스케일링



- ECS Service Auto Scaling (Task Level) != EC2 Auto Scaling (EC2 Instance Level)
  - ECS 오토 스케일링과  EC2 오토 스케일링은 서로 다르다. (시작유형이 EC2 인스턴스일때) LaunchType
    - Task(Process) 레벨이냐, EC2 인스턴스 레벨이냐의 차이가 있다.
- Fargate 시작유형의 Auto Scaling 이 더욱 세팅하기가 쉽다. (서버리스 이기 때문)
  - 시험에서도 Fargate 사용을 권장한다.



# 02. EC2 LaunchType - Auto Scaling EC2 Instances

> EC2 시작유형에서는 백엔드의 EC2 인스턴스를 어떻게 자동으로 확장하는가

스케일링에는 여러가지 방법이 있는데, 그 중 하나가 **오토 스케일링 그룹(ASG)** 이다.

- **Auto Scaling Group Scaling**
  - CPU 사용량에 따라 ASG 그룹을 스케일링 한다.
  - CPU 사용률이 급등할 때 EC2 인스턴스를 추가할 수 있다.
- **ECS Cluster Capacity Provider** (더 최신기능)
  - ECS 클러스터 용량 공급자를 사용하자. 아주 똑똑한 서비스이다.
  - 새 Task 를 실행할 용량이 부족하면 자동으로 ASG를 확장한다.
  - Capacity Provider 는 ASG 과 함께 사용된다.
  - RAM or CPU 가 모자랄 때 EC2 인스턴스를 추가합니다.



ASG 와 ECS Cluster Provider 중에 LaunchType이 EC2 인 경우에는 EC2 ECS Cluster Provider 를 사용하는것을 권장한다.



# 03. CPU Usage Example

> 위에 배운 서비스 예시를 살펴보자

![image-20221124010602894](../../assets/images/posts/2022-11-24-AWS Container (3) - Amazon ECS Auto Scaling//image-20221124010602894.png)



- 서비스 A 에 Task 가 2개 실행중이었으며, CPU 사용량은 초록색 상태이다.
- 이 서비스는 AWS Application Auto Scaling 으로 자동확장된다.
- 사용자가 많아져서 CPU 사용량이 급증하면 ECS Service Level 에서 CPU 사용량을 모니터링하는 CloudWatch 지표가 CloudWatch Alarm을 Trigger 한다.
- 이 알람이 Auto Scaling을 또 Tigger 하면 ECS 서비스의 희망용량이 증가하고, 새 Task 가 생성된다.

- 또한, LaunchType이 EC2 라면, (fargate가 아니라면) EC2 용량 공급자가 EC2 인스턴스를 추가해 ECS 클러스터를 확장하게 될 것이다.
