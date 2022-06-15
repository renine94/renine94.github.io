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



- Target Tracking Scaling
  - 설정하는게 대부분 쉽다.
  - 예를들어, 나는 CPU 가 약 40% 수준일때, 오토스케일링을 활성화 하겠다.
- Simple / Step Scaling
  - 클라우드와치 알람이 발생할때, (예를들어 CPU > 70%) 그러면 필요개수만큼 EC2 늘린다.
  - 클라우드와치 알람이 발생할때, (예를들어 CPU < 40%) 그러면 필요개수만큼 EC2 삭제한다.
- Scheduled Actions
  - 알려진 사용패턴에 기반하여 스케일링을 진행한다.
  - 금요일 10:00 ~ 17:00 일때. 오토스케일



