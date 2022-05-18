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

title: "[aws] EC2 Purchasing"
excerpt: "🚀 Purchasing Option 알아보기!"

categories: aws
tag: [aws, ec2, cloud]

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



## 1. Options

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



## 02. 어떤 Purchasing option 이 나에게 맞을까?

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
