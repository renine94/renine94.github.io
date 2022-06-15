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

title: "[aws] ASG (1) - Basic"
excerpt: "🚀 ASG (Auto Scaling Group)"

categories: aws
tag: [aws, elb, connection draining]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Auto Scaling Group (ASG)

오토스케일링그룹
{: .notice--success}

![image-20220615024245132](../../assets/images/posts/2022-06-16-AWS ASG (1) - Auto Scaling Group/image-20220615024245132.png)

- 보통 현실에서는 웹사이트와 애플리케이션이 변경되기 마련이며, 받는 부하도 다르다.
- 사용자가 많아지고 유명해질수록 더 많은 부하가 걸리게 된다.
- 클라우드 내에서는 서버를 빠르게 생성 및 제거할 수 있다.

 

## 🚀 ASG 의 목표 및 기능

- 부하가 증가하면 EC2 인스턴스를 추가한다. (스케일 아웃)
- 부하가 감소하면 EC2 인스턴스를 제거한다. (스케일 인)
- EC2 인스턴스가 일정량만큼만 증가 or 감소 하도록 만들 수 있다.
  - 머신의 최소, 최대 숫자를 지정(설정) 할 수 있다.
- **로드 밸런서에 자동으로 새 인스턴스를 등록해주는 기능**

![image-20220615024428657](../../assets/images/posts/2022-06-16-AWS ASG (1) - Auto Scaling Group/image-20220615024428657.png)





## 🚀 ASG 속성

- A launch configuration (시작 구성)
  - AMI + Instance Type
  - EC2 User Data (EC2 시작 시 실행할 스크립트)
  - EBS Volumes
  - Security Groups
  - SSH Key Pair
- Min / Max Size, Initial Capacity (최초 용량, 기대 용량)
- Network + Subnets Information
- Load Balancer information
- **Scaling policies** (스케일링 정책)
  - 무엇이 스케일 아웃, 스케일 인을 촉발하는지 등의 대한 정책



## 🚀 ASG 알람

![image-20220615025341202](../../assets/images/posts/2022-06-16-AWS ASG (1) - Auto Scaling Group/image-20220615025341202.png)

- CloudWatch 알람을 기반으로 ASG을 스케일링 하는것이 가능
- 알람 모니터링은 지표(metric) 이다. (ex. 평균 CPU 사용량)
  - 매트릭이 올라가서 알람이 울리면 인스턴스 추가 (스케일 아웃)
  - 매트릭이 내려가서 알람이 울리면 인스턴스 제거 (스케일 인)
- 매트릭이 필요하면 뭐든 알람이 될 수 있다. (커스텀 매트릭 생성 가능)
  - 알람은 평균 CPU 같은 지표를 모니터링
  - 지표는 전반적인 평균으로 계산된다.
  - 최소나 최대가 없다. 지표의 평균만 보는 것
  - 알람을 기반으로 스케일아웃 및 스케일인 정책 생성 가능



## 🚀 Auto Scaling 새로운 규칙

- 오토스케일링 그룹에 대상의 평균 CPU 사용량을 원하는 것으로 지정하면<br>대상 CPU 사용량을 충족하는 부하를 기반으로 스케일 인/아웃 을 할겁니다.
- 인스턴스당 ELB 요청 개수 기반으로 규칙을 만들 수도 있다.
- 평균 네트워크 인/아웃 등 애플리케이션에 더욱 적절한것으로 판단되는 정책이 있다면 그걸 사용하면 된다.





## 🚀 Auto Scaling Custom Metric

- 커스텀 지표 기반으로 오토스케일을 할 수 있다.
  - ex. 유저의 연결 수
- 애플리케이션에서 이 커스텀 메트릭을 생성해야 한다.
  - PutMatric API 사용해서 CloudWatch에 보낸다.
  - CloudWatch 알람을 생성해서 지표값의 높낮이에 반응하도록 만든다.
  - 커스텀 지표로 인한 CloudWatch 알람을 사용하여 ASG의 오토스케일링을 실행한다.



## 🚀 ASG Summary (요약)

1. ASG 스케일링 정책은 어떤 정책으로든 만들 수 있다.
   - CPU, Network, Custom..... etc..
   - 고객이 언제 방문할지 미리 알고있다면 일정에 따라 정할수도 있다.
2. ASG는 시작 구성(launch configurations) 이나 시작 템플릿(launch templates)을 사용 할 수 있다.
3. 시작 템플릿은 시작 구성의 최신버전 입니다. 최신버전 사용 권장
   - 오토스케일링그룹을 업데이트하려면 새로운 버전의 시작 구성, 또는 시작 템플릿이 필요하다.
4. ASG에 IAM 역할을 연결시키면 IAM 역할은 자동적으로 실행한 EC2 인스턴스에 할당된다.
5. **ASG는 무료이다. 하지만, 실행된 리소스, 즉 EBS볼륨에 연결된 EC2 인스턴스 등은 유료로 구매 필요**
6. 장점
   - **인스턴스가 종료될경우, ASG가 그 사실을 파악후 자동으로 새 인스턴스 생성해서 교체해줌**
   - 이러한 추가적인 안전성의 보장이 ASG 사용의 주된 목적
   - 혹시라도 잘못되었을때 자동으로 새로운 인스턴스가 생성될 것
   - 인스턴스가 종료되는 경우는 로드밸런서가 헬스체크후 특정EC2가 비정상이면<br>종료후 새 인스턴스를 생성해 교체하는 판단
   - ASG 재시작이 필요없다.
   - 인스턴스의 중단도 없이, 말 그대로 해당 인스턴스 종료후 새 인스턴스 생성해서 교체한다.



