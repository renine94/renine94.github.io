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

title: "[aws] S3 Advanced (4) - Storage Classes & Glacier"
excerpt: "🚀 S3, 각각의 Storage Class, Glacier 등을 알아보고 비교해보자!"

categories: aws
tag: [aws, s3, storage, class, glacier, tier, price]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# S3 Storage Classes

- Amazon S3 Standard - General Purpose
- Amazon S3 Standard-Infrequent Access (IA)
- Amazon S3 One-Zone-Infrequent Access
- Amazon S3 Glacier Instant Retrieval
- Amazon S3 Glacier Flexible Retrieval
- Amazon S3 Glacier Deep Archive
- Amazon S3 Intelligent Tiering



Amazon S3에서 Object를 생성할 때 Class를 선택할 수도 있고, Storage  Class를 수동으로 수정할 수도 있습니다. 혹은 Amazon S3 Lifecycle configurations 를 사용하여 스토리지 클래스 간에 객체를 자동으로 이동할 수도 있습니다.



## 1. S3 내구성과 가용성

> Durability and Availability

- 내구성
  - Amazon S3로 인해 객체가 손실되는 횟수를 나타낸다.
  - S3는 매우 뛰어난 내구성을 제공한다. 99.999999% 의 내구성을 보장한다.
  - S3에 천만 개의 객체를 저장했을 때, 평균적으로 10,000년에 한 번 객체 손실이 예상됩니다.
  - **모든 스토리지 클래스의 내구성은 동일**하다.
- 가용성
  - 가용성은 서비스가 얼마나 용이하게 제공되는지를 나타낸다
  - 스토리지 클래스에 따라 다르다.
  - S3 Standard 의 가용성은 99.99% 이어서 즉, 1년에 약 53분동안은 서비스를 사용할 수 없다는 의미이다.
  - 다시말해, 서비스를 사용할 때 몇 가지 에러가 발생한다는 뜻



## 2. S3 Standard - General Purpose

- 99.99% 가용성
- 자주 액세스하는 데이터에 사용
- 지연 시간이 짧고, 처리량이 높다.
- AWS에서 두 개의 기능 장애를 동시에 버틸 수 있다.
- 사용사례
  - 빅데이터 분석
  - 모바일과 게임 애플리케이션 그리고 콘텐츠 배포



## 3. S3 Storage Classes - Infrequent Access (IA)

- 자주 액세스하지는 않지만, 필요한 경우 빠르게 액세스해야 하는 데이터를 말한다.
- S3 Standard 보다 비용이 적게 들지만, 검색 비용이 발생한다.



- S3 Standard-Inrequent Access (S3 Standard-IA()
  - 가용성 99.9% 로 standard 보다 약간 떨어진다.
  - 사용사례
    - 재해 복구, 백업
- S3 One Zone-Infrequent Access (S3 One Zone-IA)
  - 단일 AZ내에서는 높은 내구성을 갖지만 AZ가 파괴된 경우 데이터를 잃게 된다.
  - 가용성은 더 낮은 수준인 99.5%
  - 사용사례
    - 온프레미스 데이터를 2차 백업하거나 재생성 가능한 데이터를 저장하는 데 쓰인다.



## 4. S3 Glacier Storage Classes

> 이름에서 알 수 있듯이 콜드 스토리지이다.

- 아카이빙과 백업을 위한 저비용 객체 스토리지
- 가격: 저장비용 + 검색비용



Glacier 스토리지에는 3가지 클래스가 존재한다.

1. **Amazon S3 Glacier Instant Retrieval**
   - 밀리초 단위로 검색이 가능하다.
     - 분기(90일)에 한번 액세스하는 데이터에 아주 적합하다
   - 최소 보관 기간이 90일
     - 백업데이터 이지만, 밀리초 이내에 액세스해야 하는 경우 적합하다.
   - Instant : 즉시 처리된다는 의미
2. **Amazon S3 Glacier Flexible Retrieval (옛날이름: Amazon S3 Glacier)**
   - 3가지 옵션이 있다.
     1. Expedited : 데이터를 1~5분 이내에 받을 수 있다.
     2. Standard : 데이터를 돌려받는 데 3~5시간 소요
     3. Bulk : 무료지만 데이터 돌려받는데 5~12시간 소요
   - 최소 보관 기간 90일
   - Flexible : 데이터를 검색하는데 최대12시간까지 기다려야 한다는 의미
3. **Amazon S3 Glacier Deep Archive - for long term storage**
   - 데이터를 장기간 보관하기 위한 스토리지 클래스
   - 2가지 티어가 존재한다.
     1. Standard : 12시간
     2. Bulk : 48시간
   - 데이터를 검색하는데 오래 걸리긴 하지만 비용이 가장 저렴
   - 최소 보관 기간 180일



## 5. S3 Intelligent - Tiering

> 사용 패턴에 따라 액세스된 티어 간에 객체를 이동할 수 있게해준다.

- 소액의 월별 모니터링 비용과 티어링 비용이 발생
- 검색 비용이 없다!!



- **Frequent Access 티어**가 자동이며 기본값
- **Infrequent Access 티어**는 자동이며 30일 동안 액세스하지 않은 객체 전용 티어
- **Archive Instant Access 티어**도 자동이며 90일 동안 액세스 하지 않은 티어
- **Archive Access 티어**는 선택이며, 90일에서 700일 이상까지 구성가능
- **Deep Archive Access 티어**는 선택이며, 180일에서 700일 이상 액세스하지않은 객체에 구성가능



S3 Intelligent Tiering은 알아서 객체를 이동시켜 주기 때문에 편하게 스토리지를 관리할 수 있다.



## 6. Storage Classes Comparison

> 모든 스토리지 클래스를 비교해보자



![image-20220811015158215](../../assets/images/posts/2022-08-08-AWS S3 advanced (4) - Storage Classes/image-20220811015158215.png)



모든 숫자를 기억할 필요는 없지만, 각 클래스가 무엇인지만 이해하면 좋다.

내구성은 모두 9가 11개정도 있는정도이고, 가용성은 AZ가 적을수록 낮아진다.<br>그리고, 최소저장기간 등도 위의 표에서 참고할 수 있다.



아래의 사진은 us-east-1 리전에서의 스토리지 클래스 가격 비교표이다.

![image-20220811015401865](../../assets/images/posts/2022-08-08-AWS S3 advanced (4) - Storage Classes/image-20220811015401865.png)