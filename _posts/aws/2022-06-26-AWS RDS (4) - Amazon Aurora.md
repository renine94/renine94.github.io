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

title: "[aws] RDS (4) - Amazon Aurora"
excerpt: "🚀 RDS, DB, Aurora"

categories: aws
tag: [aws, rds, db, sql, aurora]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# RDS - Amazon Aurora

- AWS Aurora 는 AWS의 사유기술이며, 오픈소스가 아니다.
- MySQL, PostgreSQL 과 호환이 된다. (Aurora DB에 호환드라이버가 있어 저 DB들에 연결하면 실행됨)
- Aurora DB 는 클라우드에 최적화 되어 있다. MySQL 대비 5배, PostgreSQL 대비 3배이상 성능 좋다.
- Aurora 스토리지는 자동으로 늘어나며, 10GB로 시작하여 최대 128TB 까지 확장 가능하다.
- Aurora 는  읽기전용 Replica도 15개까지 가질 수 있고, MySQL은 최대 5개이다.
- 복제하는 속도도 훨씬 빠르다.
- Aurora 에서는 장애 조치도 즉각적이다.
- MySQL RDS의 다중AZ에서 장애 조치보다 속도가 훨씬 빠르다.
- 클라우드 네이티브라서 가용성이 높기 때문이다.
- 일반 RDS보다 비용이 20% 정도 비싸지만 규모면에서 더 효율적이어서 비용을 많이 절약할 수 있다.



## Aurora 고가용성, Read 스케일링

![image-20220626212417253](../../assets/images/posts/2022-06-26-AWS RDS (4) - Amazon Aurora/image-20220626212417253.png)

- 3개의 AZ에 대한 6개의 복제본을 생성한다.
  - 쓰기에는 6개중 4개가 필요 (한개의 AZ가 다운돼도 괜찮은것을 의미)
  - 읽기에는 6개중 3개가 필요
  - 자가복구 과정이 있다. 일부 데이터 손상되거나 잘못된경우 백엔드에서 P2P 복제로 자가복구를 한다.
- 하나의 오로라 인스턴스가 쓰기권한 (master) 를 가진다.
  - 기록을 하는 인스턴스는 한 개만 있다.
- 마스터가 작동하지 않으면 평균적으로 30초 안에 장애조치가 실행된다.
- 마스터에는 최대 15개의 읽기전용 복제본이 있을 수 있다. (MySQL은 5개)
- 모든 읽기전용 레플리카는 마스터 장애 시 마스터가 될 수 있다. (마스터로 승격가능)
- 읽기전용 복제본이 장점은 Cross Region 을 지원한다.



그림에서 기억해야 할 것은, 하나의 Master 와 여러 개의 읽기 전용 Replica, 그리고 스토리지가 복제되며,<br>작은 블록별로 자가 복구와 자동 확장이 실행된다는 점이다.



## Aurora DB Cluster

> 클러스터로서의 오로라는 어떤지 살펴보자

![image-20220626212503371](../../assets/images/posts/2022-06-26-AWS RDS (4) - Amazon Aurora/image-20220626212503371.png)



모든 인스턴스와 어떻게 연결 원리

- 고융된 스토리지 볼륨이 있어, 10GB 에서 최대 128TB 로 자동 확장
- 마스터는 유일하게 스토리지에 기록할 수 있다.
- 변경과 장애조치가 가능하기 때문에 Aurora는 Write Endpoint를 제공한다.
  - 이것은 DNS 이름으로 라이터 엔드 포인트는 늘 Master 를 향해서 마스터 장애 시에도 클라이언트는 Write Endpoint와 통신해 올바른 인스턴스로 자동으로 리다이렉션 된다.
  - 그렇기 때문에 읽기 전용 복제본을 많이 갖게 되는 것
- 읽기 전용 Replica에 오토스케일링을 적용할 수 있다.
- 최대 15개의 읽기전용레플리카에 일정 수의 읽기전용 레플리카를 오토 스케일링을 통해 설정 가능
- Read Endpoint 로 요청을 보내면, 자동으로 로드밸런싱의 연결을 돕고 모든 읽기DB에 자동으로 연결
- **Client => Read Endpoint => 읽기전용DB 중 하나에 자동 연결**



## Aurora 의 기능

1. 자동 장애 조치
2. 백업 및 복원
3. 격리 와 보안
4. 산업 규정 준수 기능
5. 오토 스케일링을 통한 푸시 버튼식 스케일링
6. 제로 다운타임의 자동 패치
7. 고급 모니터링
8. 정기 유지 보수
9. 백트랙기능 : 언제든지 데이터 복원
   - 어제 오후4시로 복원하려 했다가 갑자기 어제 5시로 복원하고자하면 아주 잘 실행된다.



## Aurora 보안

1. 같은 엔진을 사용하므로 보안은 RDS와 비슷하다.
2. PostgreSQL, MySQL 이 있고, KMS로 미사용 데이터를 암호화 한다.
3. 자동 백업, 스냅샷 그리고 Replica 또한 암호화 된다.
4. 전송중 암호화에는 SSL을 사용한다.
5. IAM 토큰을 사용하여 인증도 가능하다. (RDS 도 같은 방법)
6. 보안 그룹으로 인스턴스를 보호해야 한다. (나의 책임)
7. SSH 로 인스턴스에 연결할 수 없다.
8. 오로라의 보안은 RDS의 보안과 완전히 동일하다.



