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

title: "[aws] ASG (2) - Scaling Policy"
excerpt: "🚀 scaling policy"

categories: aws
tag: [aws, asg, scaling, policy]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# ASG - Dynamic Scaling Policies

동적으로 스케일 아웃/인 되는 조건들을 정리하는 시간을 가져보자.
{. :notice--success}



- Dynamic Scaling Policies
  - 동적 스케일링
- Predictive Scaling Policies
  - 예측 스케일링
  - 머신러닝을 기반.. 예측을 토대로 스케일링을 수행한다.
- Scheduled Actions
  - 예약된 작업



## 🚀 Dynamic Scaling Policies (동적 스케일링 정책)

- Target Tracking Scaling (대상 추적)

  - 설정하는게 대부분 쉽다.
  - 오토스케일링 그룹의 평균 CPU 사용률을 추적하여 이 수치가 일정 이상 넘어갈 때 
    - 예를들어, 나는 CPU 가 약 40% 수준일때, 오토스케일링을 활성화 하겠다.

- Simple / Step Scaling (단계/단순 스케일링)

  - 클라우드와치 알람이 발생할때, (예를들어 CPU > 70%) 그러면 필요개수만큼 EC2 늘린다.
  - 클라우드와치 알람이 발생할때, (예를들어 CPU < 40%) 그러면 필요개수만큼 EC2 삭제한다.

- Scheduled Actions

  - 알려진 사용패턴에 기반하여 스케일링을 진행한다.
  - 금요일 10:00 ~ 17:00 일때. 오토스케일

  - 금요일 오후5시에 큰 이벤트가 예정되어 있을 때,

  - 유저들이 앱을 사용하는데 대비해 우리의 ASG 최소 용량을 매주 금요일 5주마다 자동으로 10 까지 늘리게 하는것



**예측 스케일링 정책**

![image-20220616031144889](../../assets/images/posts/2022-06-17-AWS ASG (2) - Scaling Policy/image-20220616031144889.png)



- 스케일링이 필요함을 미리 알 때 예정된 작업을 설정하면 된다.
- 스케일링이 필요함에 미리 알 때에 예정된 작업을 설정하면 된다.



## 🚀 스케일에 사용하기 좋은 지표

![image-20220616031910242](../../assets/images/posts/2022-06-17-AWS ASG (2) - Scaling Policy/image-20220616031910242.png)

- 평균 CPU 점유율
- 타겟그룹당 요청 개수
- 평귱 네트워크 인/아웃
- 그밖의 사용자지정 지표들,,,



## 🚀 스케일링 휴지 (Scaling Cooldown)

> 스케일링 작업이 끝날 때마다 인스턴스의 추가 및 삭제를 막론하고,
>
> 기본적으로 5분(300초) 의 휴지 기간을 갖는 것

![image-20220616032855179](../../assets/images/posts/2022-06-17-AWS ASG (2) - Scaling Policy/image-20220616032855179.png)

- 휴지기간에는 ASG가 추가 인스턴스를 실행 또는 종료할 수 없다.
  - 지표를 이용하여 새로운 인스턴스가 안정화될 수 있도록 하며 새로운 지표 양상을 살펴보기 위해서이다.
- **스케일링 작업이 발생할 때, 설정된 CoolDown(휴지) 가 있는지 확인해야 한다.**
- 휴지가 설정되어있으면, 해당 작업을 무시하고, 아닐경우에는 인스턴스를 직접 실행or종료하는 스케일링 작업 수행
- 즉시 사용가능한 AMI 이용하여 EC2 인스턴스 구성시간 단축하여 요청을 좀더 신속히 처리하는것이 좋다.
  - EC2 인스턴스 구성에 할애되는 시간이 적으면 즉시 적용이 가능하기 때문이다.
- ASG 가 1분마다 지표에 접근할 수 있도록 세부 모니터링 기능을 사용하도록 설정하고<br>이와 같은 지표를 업데이트할 필요가 있다.
