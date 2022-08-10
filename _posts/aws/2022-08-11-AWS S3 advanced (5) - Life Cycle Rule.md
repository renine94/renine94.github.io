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

title: "[aws] S3 Advanced (5) - Life Cycle Rule"
excerpt: "🚀 S3 수명주기규칙을 활용하여 Storage class를 자동 이동시켜보자!"

categories: aws
tag: [aws, s3, life, cycle, rule]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# S3 Lifecycle Rule



# 1. Moving between storage classes

> 바로 전 포스팅에서 확인한 것처럼 스토리지 클래스간 객체의 전환이 가능하다<br>어떤 방식으로 가능한지 알아보자

![image-20220811021446741](../../assets/images/posts/2022-08-11-AWS S3 advanced (5) - Life Cycle Rule/image-20220811021446741.png)

- 스토리지 클래스 간의 객체를 전환(이동)시킬수 있다.

- 자주 액세스하지 않는 객체의 경우 Standard_IA 로 이동한다.
- 아카이빙을 위한 객체에서는 실시간이 필요하지 않기 때문에, Glacier 또는 Deep_Archive를 사용
- 객체 클래스 전환은 **수명주기설정** 을 사용함으로서 자동으로 관리할 수 있다.
  - 수동으로도 객체 간 클래스 이동을 시킬수 있다. (지난 포스팅 실습 참고)



## 2. Lifecycle Rules

> 수명주기규칙 이란?

- 전환 작업 (Transition actions)
  - 객체를 한 스토리지 클래스에서 다른 스토리지 클래스로 전환하는데에 도움을 주는 작업이다.
    - 만약 객체 생성후 60일 경과  --> Standard-IA 로 보낸다
    - 6개월 경과하면 아카이빙을 위해 Glacier 로 보낸다.
- 만료 작업(Expiration actions)
  - 일정 기간이 지난 후 객체를 삭제하는 작업
    - 액세스 로그파일들이 1년이 지나서 더이상 필요가 없어지면 삭제
    - 파일의 오래된 버전을 삭제하는 데에도 사용된다. (versioning 기능을 사용할 경우)
      - 60일 이상 지난 이전의 버전은 필요가 없다면 만료작업을 구성해서 삭제
    - 완료되지 않은 다중 파트 업로드를 정리하는데에도 사용된다.
      - 분할된 파트가 30일동안 떠돌고 있고 절대 완료되지 않을때 이러한 파트를 제거하기 위해 만료작업을 구성한다.



- 특정 접두어에 규칙을 적용할 수도 있다.
  - 만약 모든 MP3 파일이 "MP3" 폴더에 있거나, 접두어를 가지고 있다면 수명주기규칙을 해당 접두어에만 설정할 수도 있다.
  - ex) s3://mybucket/mp3/*
- 특정 객체 태그를 위해 규칙을 생성할 수도 있다.
  - 예를 들어, "Department: Finance"로 태그된 객체에만 규칙을 적용하고 싶다면 그것도 가능
  - ex) Department: Finance



## 3. Lifecycle 시나리오



### 3-1. 시나리오1

프로필 사진이 S3에 업로드된 후 EC2의 App이 썸네일을 생성한다. 이 썸네일은 손쉽게 재생성할 수 있으며 45일간만 보관됩니다. 45일 동안은 원본 사진 파일을 즉시 회수할 수 있으며 이후에는 유저가 최대 6시간까지 기다릴 수 있다. 이러한 솔루션을 어떻게 설계할 수 있을까?

- S3 원본 사진은 Standard 클래스에 두고 수명주기구성을 설정해서 45일 후 Glacier로 보낸다.
- 썸네일은 Onezone_IA 에 두면 된다. 재생성이 가능하기 때문이다. 수명주기구성을 통해 45일 후 만료 혹은 삭제시킬 수도 있다. 45일 후엔 썸네일이 필요없으니 삭제, 원본 사진을 Glacier로 보내고 썸네일은 Onezone_IA에 저장, 비용이 절감되기 때문이다.

AWS에서 전체AZ를 잃을 상황을 대비해 원본 사진으로부터 쉽게 썸네일을 재생성할 수 있습니다.<br>S3 버킷에 대한 비용 효율이 가장 높은 솔루션이 될 것이다.

<br><br>

### 3-2 시나리오2

회사에서는 일어나는 경우가 드물지만, 15일 동안은 삭제된 S3 객체를 즉시 복구할 수 있는 규칙이 있다고 하자. 그리고 그 이후 최대 1년까지는 삭제한 객체 48시간 내에 복구할 수 있다. 이러한 솔루션을 설계하려면 어떻게 해야 할까?

1. S3 버저닝을 허용하고, 파일을 삭제는 하되 복구시키길 원하기 때문이다. 버저닝으로 객체 버전을 가질 수 있으며 삭제된 객체는 삭제 마커를 달고 숨겨져 쉽게 복구할 수 있기 때문이다. 

2. 하지만, 최신이 아닌 버전들, 즉 객체의 이전 버전들도 가지게 될것이다. 그래서 이 오래된 버전들은 S3_IA로 전환을 시킨다. 왜냐하면 오래된 버전에 액세스할 일은 아주 드물지만, 만약 액세스하는 경우 복구가 즉시 이뤄져야 하기 때문

3. 그리고, 이 오래된 버전들을 복구할 수 있는 15일의 기간이 지나면 이들을 Deep_Archive로 전환시켜서 100일or365일 동안 보관시키도록 한다. 이들은 아카이브되어 48시간 내에 복구가 가능해진다.
   - 왜 Glacier를 사용하지 않는걸까?
     - Glacier는 비용이 좀 더 비싸며 48시간이라는 시간이 주어졌기 때문에 티어를 Deep_Archive까지 올려서 비용을 더 절약할 수 있기 때문이다.



## 4. Life Cycle Rules 실습

> 수명주기실습을 진행해보자

S3 의 Bucket에 들어가보면 아래와 같은 화면을 볼 수 있고, 그중 Management(관리) 탭에 들어가면 수명주기규칙을 설정할 수 있다.

![image-20220811024244099](../../assets/images/posts/2022-08-11-AWS S3 advanced (5) - Life Cycle Rule/image-20220811024244099.png)



수명주기 규칙 생성 버튼을 눌러 아래와 같은 정보를 입력하여 수명주기규칙을 생성할 수 있게된다.

- 규칙 범위 선택 (Choose a rule scope)
  - 하나 이상의 필터를 사용하여 이 규칙의 범위 제한 (Limit the scope of this rule using one or more filters)
    - 접두사 필터
    - 객체 태그 필터
  - 버킷의 모든 객체에 적용 (This rule applies to all objects in the bucket)
    - 해당 버킷에 들어가는 모든 객체들에게 수명주기규칙을 적용시킨다



- 수명 주기 규칙 작업 (Lifecycle rule actions)  --> **2번 목차에서 배운 내용**
  - 스토리지 클래스 간의 객체의 현재 버전 이동
    - 현재: 버저닝이 활성화된 경우 객체의 최신 버전을 의미
  - 스토리지 클래스 간의 객체의 이전 버전 이동
    - 이전: 버저닝이 활성화된 경우 현재 객체가 아닌 다른 모든 버전들
  - 객체의 현재 버전 만료
  - 객체의 이전 버전 영구 삭제
  - 만료된 객체 삭제 마커 또는 완료되지 않은 멀티파트 업로드 삭제

![image-20220811025144295](../../assets/images/posts/2022-08-11-AWS S3 advanced (5) - Life Cycle Rule/image-20220811025144295.png)



30일 후 - Standard_IA 로 이동

70일 후 - Intelligent-Tiering 이동

180일 후 - Glacier 이동

365일 후 - Glacier Deep Archive 이동

![image-20220811025526263](../../assets/images/posts/2022-08-11-AWS S3 advanced (5) - Life Cycle Rule/image-20220811025526263.png)





위와 같이 전환작업 / 만료작업을 섞어가며 원하는 시나리오대로 규칙을 만들고 <br>마지막에 규칙을 요약한 내용을 볼 수 있다.

버저닝된 객체파일에서 현재(최신) 버전은 어떻게 할것이고, 이전(현재버전이 아닌 이전 버전들) 버전은 어떻게 작업할 것인지 아래의 사진 처럼 정리가 되어져서 보여진다.

![image-20220811025948017](../../assets/images/posts/2022-08-11-AWS S3 advanced (5) - Life Cycle Rule/image-20220811025948017.png)