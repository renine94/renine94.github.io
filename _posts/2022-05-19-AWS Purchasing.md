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

title: "[aws] EC2 Purchasing & Spot Instance"
excerpt: "🚀 Purchasing Option, Spot Instance 알아보기!"

categories: aws
tag: [aws, ec2, spot, cloud]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# 01. EC2 - Purchasing Options

<div class="notice--success">
  <ul>
    <li> EC2 를 대여(구매) 하는 여러가지 방법을 알아보자 </li>
    <li> 사례에 따라서 비용을 절감할 수 있다. </li>
    <li> 최적의 EC2 인스턴스 구매 옵션을 알아보자 </li>
  </ul>
</div>



## 🚀 Options

- On-Demand Instance
- Reserved
  - Reserved Instances
  - Convertible Reserved Instances
  - Saving Plan (1 & 3 years)
- Spot Instances
- Dedicated Hosts
- Dedicated Instances
- Capacity Reservations



### On-Demand Instance

![image-20220519015219980](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519015219980.png)

- 예측이 가능한 단기 워크로드용 인스턴스
- 사용한 만큼 지불하는 옵션
- 리눅스 or 윈도우 - 1분이후부터 1초당 비용 청구
- 다른 운영체제 - 시간당 가격 청구
- 클라우드에 가장 적합한 방식
- 가격은 높지만, 선결제나 장기 약정이 필요 없다.
- 언제든 원할 때 사용 해지, 중지, 시작이 가능하다.

### Reserved

![image-20220519015310569](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519015310569.png)

- 예약 인스턴스
- 특정 인스턴스 타입을 지정해서 예약한다.
- *<u>온디맨드와 비교하면 최대 70% 이상 비용을 절약할 수 있다.</u>*
- 오랜 시간동안 사용해야되는 인스턴스 (비용 절감)
- 최소 1년이상 사용해야 한다.
- 선결제 여부에 따라서 할인폭이 달라진다.
  - 부분 또는 전체 선결제 가능
- 데이터베이스와 같이 애플리케이션이 안정된 상태로 사용되는 유형에 적합



- Convertible Reserved Instances
  - 전환형 예약 인스턴스
  - 시간이 지난후 다른 유형의 인스턴스로 바꿀 수 있는 유연형 인스턴스
- ~~Scheduled Reserved Instance~~
  - 매일 목요일 15 ~ 18시 예약
  - *<u>현재는 없어 사라진 유형이다.</u>*

### Spot Instances 

![image-20220519020041743](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519020041743.png)

- AWS 에서 할인율이 가장 높은 옵션
- 저렴한 단기 워크로드용
- 손실 가능성이 있으며 신뢰성이 낮다.
- *<u>온디멘드와 비교하면 최대 90% 할인!!</u>*
- *<u>지불하고 하는 가격이 현재 스팟 인스턴스의 가격보다 낮다면 언제든지 중단될 수 있다.</u>*
- 서비스 중단에도 복구가 쉬운 작업에 사용한다.
  - 단발성 데이터 분석 배치 작업
  - 이미지 변환
  - 분산 작업
  - 하나의 서버가 중단되어도 상관없는 작업
- 데이터베이스에는 절대 사용해서는 안된다.

### Dedicated Hosts

![image-20220519020340159](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519020340159.png)

- 전용 호스트
- 물리적 서버 전체를 예약
- 인스턴스 배치를 제어한다.
- EC2 인스턴스를 갖춘 유저 중심의 물리적 서버

### Dedicated Instances

![image-20220519020601111](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519020601111.png)

- 전용 하드웨어에서 실행되는 EC2 인스턴스를 의미
- 같은 계정의 다른 인스턴스와 하드웨어를 공유
- 전용호스트의 약한 버전
- 두 개 차이 오른쪽 도표 참고



## 🚀 어떤 Purchasing option 이 나에게 맞을까?

![image-20220519020758448](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519020758448.png)

- 온디맨드
  - 전액을 지불해야 하지만 원할때 언제나 방을 얻을 수 있다.
- 예약
  - 오랜 기간 호텔에 머무를때 예약해서 할인받는다.
- 스팟 인스턴스
  - 밤에 객실이 빌때 공격적인 할인
  - *<u>다만 나보다 높은 가격을 지불하는 손님이 나타나면 내쫓겨질 수 있다.</u>*
- 전용 호스트
  - 리조트 전체를 혼자서 예약
- ~~Capacity Reservations~~
  - Deprecated





# 02. Spot Instance - Deep Dive!

> 스팟 인스턴스를 제대로 알아보자!

- 스팟 인스턴스를 사용하면 온디멘드와 비교해 최대 90% 할인
- 최고가를 정의해두고 `현재가격 < 최고가` 동안 계속 인스턴스를 사용할 수 있다.
- 만약 `현재가격 > 최고가` 상태가 되면, 2분의 유예기간 동안 2가지 옵션중 선택 할 수 있다.
  - **중단**  - 하고있던 모든 작업 중단후 인스턴스 중단후 다시 `현재가격 < 최고가` 상태가 되면 인스턴스를 받고 작업을 계속 이어서 한다.
  - **종료**  - 업무를 재시작할때마다 완전히 새로운 인스턴스를 띄운다.
- ~~스팟 블록~~
  - ~~미사용 Deprecated~~
- 실패해도 상관없는 단발성 작업에 스팟인스턴스를 사용하는것이 좋다.
  - 데이터베이스와 같은곳에 사용해서는 안된다.



### Pricing

![image-20220519022945609](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519022945609.png)

- 1개의 Region 에 6개의 AZ 이 있다면 가격도 6개가 된다.
- 온디멘드는 시간당 0.1달러
- 스팟인스턴스는 시간당 평균 0.45달러
- 만약 내가 최고가를 0.5달러로 해놓는다면 스팟인스턴스를 계속해서 사용할 수 있을 것
  - 온디맨드보다 그래도 더 저렴하다.



### How to terminate Spot Instances?

> 스팟 인스턴스는 어떻게 종료하는지 알아보자

스팟인스턴스 요청 종류

- 일회성
  - 한번 요청하면 그다음부턴 요청하지 않는다.
- 지속성
  - 지속해서 요청해서 중간에 회수되어도 다시 요청하게 된다.

*<u>스팟 요청을 취소하게 되면 기존에 실행중이던 스팟 인스턴스는 종료가 되지 않는다.</u>*

그러므로 완전히 스팟인스턴스를 종료하기 위해서는

1. 스팟 요청을 먼저 중단한다.
2. 연결중인 또는 실행중인 스팟인스턴스를 종료시킨다.



### Spot Fleets

> 극강의 비용 절감을 위한 방법
>
> 한 세트의 스팟 인스턴스에다가 선택적으로 온디맨드 인스턴스를 조합해 사용하는 방식

집합이라는 뜻의 Fleet

**스팟플릿은 우리가 자동으로 스팟인스턴스 요청을 가장 낮은 비용으로 하게 해준다.**

자동으로 가용영역, 용량등을 지정하게 된다.

![image-20220519031940677](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519031940677.png)

<br>

# 03. EC2 - Summary

![image-20220519031623162](/assets/images/posts/2022-05-19-AWS Purchasing/image-20220519031623162.png)

