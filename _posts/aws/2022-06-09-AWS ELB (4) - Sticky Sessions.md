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

title: "[aws] ELB - Sticky Sessions"
excerpt: "🚀 sticky session, session affinity"

categories: aws
tag: [aws, elb, sticky, session]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# ELB - Sticky Sessions (Session Affinity)

> 고정세션 & 세션 밀접성 에 대해 알아보자.
>
> Target Group 에서 설정하는 옵션이다.
>
> 해당 옵션을 켜게되면, 부하 불균형이 생길 수 있으니 유의할 것

![image-20220609021957426](../../assets/images/posts/2022-06-09-AWS ELB (4) - Sticky Sessions/image-20220609021957426.png)

**특징**

로드 밸런서에 2가지 요청을 수행하는 클라이언트가 요청에 응답하기 위해 백엔드에 동일한 인스턴스를 갖는 것<br>**다시말해, 유저1 이 한번 요청을 보내면, 그 요청이 EC2 1번으로 갔다면, 다음 요청도 EC2 1번으로 가게된다.**<br>해당 동작은 CLB 와 ALB 에서 모두 설정 가능하다.



**원리**

**이 원리는 쿠키때문**인데, 클라이언트에서 로드 밸런서로 요청의 일부로서 쿠키가 전송된다.<br>**고정성**과 **만료 기간**도 있다. 즉, 쿠키가 만료되면 클라이언트가 다른 EC2 인스턴스로 리다이렉션 된다는것이다.

세션 만료를 사용 시에는 사용자의 로그인과 같은 중요한 정보를 취하는 세션 데이터를 잃지 않기 위해<br>사용자가 동일한 백엔드 인스턴스에 연결됩니다.



**단점**

고정성을 활성화하면 백엔드 EC2 인스턴스 부하에 불균형을 초래할 수도 있습니다.<br>일부 인스턴스는 고정 사용자를 갖게 된다.



**쿠키란?**

고정 세션(Sticky Session) 에는 2가지 유형의 쿠키가 있다.

- 애플리케이션 기반 쿠키 (Application-based Cookies)
  - 사용자 정의 쿠키
    - Target 에 의해 생성된다.
    - 애플리케이션에 필요한 모든 사용자 정의 속성을 포함할 수 있다.
    - 쿠키 이름은 각 TargetGroup 별로 개별적으로 지정해야 한다.
    - AWSALB, AWSALBAPP, AWSALBTG 와 같은 이름은 사용해서는 안된다. (이미 ELB가 사용중인 이름)
  - 애플리케이션 쿠키
    - 로드밸런서 자체에서 생성된다.
    - 쿠키이름은 `AWSALBAPP` 이다.
- 기간 기반의 쿠키 (Duration-based Cookies)
  - **로드밸런서에 의해 생성되는 쿠키이다.**
  - 쿠키 이름은 `alb - AWSALB` 이고, `clb - AWSELB` 이다.



## 실습

- 고정 세션을 활성화 하는법
  - Load Balancer - Target Groups - Action - Edit attributes
  - Load balancing algorithm
    - round robin
    - least outstanding requests
    - **Stickness** (고정성)
      - Load Balancer generated cookie (기간 유형)
      - Application-based cookie 
      - 쿠키 범위는 1초 ~ 7일 이다 (설정한 기간만큼 요청이 동일한 EC2 로 가게될 거라는 뜻)



![image-20220609023803491](../../assets/images/posts/2022-06-09-AWS ELB (4) - Sticky Sessions/image-20220609023803491.png)

![image-20220609023827852](../../assets/images/posts/2022-06-09-AWS ELB (4) - Sticky Sessions/image-20220609023827852.png)

