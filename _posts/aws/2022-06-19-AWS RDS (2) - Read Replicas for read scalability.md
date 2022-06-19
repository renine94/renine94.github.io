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

title: "[aws] RDS (2) - Read Replicas for read scalability"
excerpt: "🚀 RDS, DB, Read Replicas, read scalability, mulity AZ"

categories: aws
tag: [aws, rds, db, sql, read, replica]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# AWS RDS - 읽기전용 복제본과 다중AZ

🚀 RDS 읽기 전용 복제본과 다중 AZ 차이를 이해하자!<br>🚀 각각의 사용 사례를 제대로 이해하자.
{: .notice--success}



## 01. Read Replica

> 읽기 전용 인스턴스 (읽기 전용 복제본)

![image-20220620000126015](../../assets/images/posts/2022-06-19-AWS RDS (2) - Read Replicas for read scalability/image-20220620000126015.png)



- 읽기 전용 복제본을 최대 5개 까지 생성할 수 있다.
- 이들은 동일한 가용영역(AZ) 또는 가용영역이나 리전에 걸쳐서 생성될 수 있다. (Cross AZ or Cross Region)
- 2개의 Read, 1개의 Master 가 있다고 가정하자.
  - 1개의 Master DB 와 2개의 Read DB 인스턴스 사이에 **비동기식 복제**가 이루어진다.
  - 비동기식이란 결국 읽기가 일관적으로 유지된다는 뜻
  - Read DB 를 읽어들이면 모든 데이터를 얻을 수 있다는 뜻이다.
- Read DB (Replica) 를 자체 DB (master) 로도 승격할 수 있다.
- 애플리케이션은 읽기 복제본을 활용하도록 연결 문자열을 업데이트해야 합니다.



## 02. 사용사례

> 언제 Read Replica 를 사용하게 될까?

![image-20220620001525404](../../assets/images/posts/2022-06-19-AWS RDS (2) - Read Replicas for read scalability/image-20220620001525404.png)

- 평균적인 로드 (트래픽?) 이 발생하고있는 prod DB 가 있다고 가정한다.
- 이때 새로운 팀이와서 나의 데이터를 기반으로 몇 가지 보고와 분석을 실시한다고 한다.
- 보고와 분석을 메인 RDS DB 에 연결하면 오버로드가 발생하고, 생산 애플리케이션의 속도가 느려진다.
- 이런 상황을 피하고자, 새로운 워크로드에 대한 읽기전용 복제본 (read replica) 를 생성한다.
- read replica 는 오직 SELECT (read) 만 요청을 하며, Insert, Create, Delete 의 작업은 하지않는다.



## 03. RDS Read Replioca - Network Cost

> RDS 읽기전용 복제본과 관련된 네트워킹 비용을 살펴보자.
>
> AZ 와 Region 에 따라서 비용이 발생할수도 있고, 무료인 경우의 차이점을 알아보자.

![image-20220620001959346](../../assets/images/posts/2022-06-19-AWS RDS (2) - Read Replicas for read scalability/image-20220620001959346.png)



- AWS 에서는, 하나의 AZ 에서 다른 AZ 로 데이터가 이동할때에 비용이 발생한다.
- 하지만 예외가 존재하며, 이 예외는 관리형 서비스 (managed service) 에서 나타난다.
- RDS 읽기 전용 복제본은 관리형 서비스입니다.
- **Read Replica DB 가 다른 AZ 상이지만 동일 Region 에 있을 때는 비용이 발생하지 않는다.**
  - ap-northest-2a 에 Master DB 가 있고, ap-northest-2b 에 Read DB 가 있다고 치면<br>이는 비동기식 복제로 Read DB 의 복제 트래픽이 하나의 AZ 에서 다른 AZ 로 넘어가더라도<br>RDS 는 관리형 서비스이기 때문에 해당 트래픽은 비용 없이 무료로 이동할 수 있습니다.
- 하지만, 서로 다른 Region 에 복제본이 존재하는 경우에는 비용이 발생합니다.



## 04. RDS Multi AZ

> RDS 다중 AZ 에 대해 알아보자.
>
> 다중 AZ 는 주로 재해 복구에 사용된다.

![image-20220620002802440](../../assets/images/posts/2022-06-19-AWS RDS (2) - Read Replicas for read scalability/image-20220620002802440.png)

- 가용영역(AZ) A 는 읽기와 쓰기를 수행하는 Master DB 인스턴스
- 동기식으로 AZ B 에 스탠바이 인스턴스로 복제한다.
- Master의 변경사항이 대기(standby) 인스턴스에도 그대로 복제된다는것을 의미
- 하나의 DNS 이름을 갖고 애플리케이션 또한 하나의 DNS 이름으로 통신하며<br>마스터에 문제가 생길 때에도 스탠바이 DB에 자동으로 장애조치가 수행된다.
- 하나의 DNS 이름을 갖기 때문에 가능하다.
- 이를 통해 가용성을 높일 수 있기 때문에 Multi AZ 이라고 불린다.

전체 AZ 또는 네트워크가 손실될 때를 대비한 장애 조치이자 Master DB 또는 Storage에 장애가 발생할 때<br>스탠바이 DB가 새로운 Master가 될 수 있도록 하는 것이다.

따로 수동으로 설정할 필요가 없다. 자동으로 데이터베이스에 연결이 시도되고 장애 조치가 필요하게 될 때에도<br>스탠바이가 마스터로 승격되는 과정이 자동으로 이루어지기 때문이다.

- 스탠바이 DB 는 오직 대기 목적 하나만 수행한다.
- 누구도 이를 Read/Write 할 수 없다.
- master DB 에 문제가 발생할 경우를 대비한 장애 조치일 뿐이다.
- 재해 복구를 대비해서 Read DB 를 다중AZ 로 설정가능하다.



## 05. 단일 AZ에서 다중AZ 설정

![image-20220620003647538](../../assets/images/posts/2022-06-19-AWS RDS (2) - Read Replicas for read scalability/image-20220620003647538.png)

- DB 중지할 필요 없다.
- AWS 에서 설정을 수정하기만 하면 된다.
- 내부동작
  - 사진참조



