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

title: "[aws] RDS (1) - Overview"
excerpt: "🚀 RDS, Database, overview, DB, SQL"

categories: aws
tag: [aws, rds, db, sql, mysql]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# AWS RDS

> AWS 에서 제공하는 관리형 데이터베이스



## 01. Overview

- RDS 는 관계형데이터베이스 서비스이다.
- SQL 을 쿼리언어로 사용하는 데이터베이스를 위한 관리형 데이터베이스



## 02. RDS 종류

- PostgreSQL
- MySQL
- MariaDB
- Oracle
- MSSQL
- Aurora (AWS DB)



## 03. 사용이유

EC2 인스턴스에 자체 DB 를 배포하지 않고 RDS를 사용하는 이유

- RDS 는 관리형 서비스이다.
- 데이터베이스의 프로비저닝이 완전히 자동화 되어 있다.
- 기본 OS 패치 또한 자동으로 이루어진다.
- **지속적인 백업**이 수행되며, 특정 타임스탬프로 복구할 수도 있다.
  - 지정시간복구 PITR 이라고 한다. (Point in Time Restore)
- 모니터링 **대시보드를 통해 데이터베이스 성능을 확인**할 수 있다.
- **Read 성능향상을 위한 읽기전용 복제본 생성 가능**
- DR(Disaster Recovery) 를 위한 다중 AZ 설정
- 스케일링이 가능 (수직, 수평)
- EBS 기반의 스토리지 백업 (gp2 or io1)
- **RDS 인스턴스에는 SSH를 따로 가질 수 없다.**
  - 관리형서비스로 AWS에서 제공되므로 기본 EC2 인스턴스에 대해서는 사용자가<br>따로 접근 권한을 갖지 않기 때문이다.

## 04. 백업

- 백업은 RDS에서 자동으로 활성화되며 자동으로 생성된다.
  - 매일 수행되는 DB 전체에 대한 백업
  - 트랜잭션 로그, 즉 일일 트랜잭션 로그가 5분마다 RDS에 백업된다.
- 위 2가지를 사용하여 어떤 지정 시점으로든 DB를 복원할 수 있게 된다.
  - 가장 오래된 백업에서부터 단 5분전 백업으로까지 자유롭게 롤백 가능하다.
- 자동백업은 기본 7일간 보관, but 35일까지 보관기간 설정 가능
- 데이터베이스 스냅샷이 있는데 **스냅샷은 백업과 약간 다르다.**
  - 스냅샷
    - 사용자가 수동으로 발동시키는 백업
    - 백업 보관 기간을 사용자 임의로 설정 가능
    - 예를들어, 6개월간의 지정 시점 동안 DB 보관도 가능하다

## 05. RDS Storage Auto Scaling

> RDS 데이터베이스를 생성할 때는 원하는 스토리지 용량을 지정해야 한다.
>
> 스토리지를 20GB 로 지정하는것처럼 말이다.

<img src="../../assets/images/posts/2022-06-19-AWS RDS (1) - Basic/image-20220619234416427.png" alt="image-20220619234416427" style="zoom:100%;" />

**데이터베이스 사용이 많고, 사용 가능한 공간이 부족해지는 경우 RDS Storage Auto Scaling이 활성화<br>되어있으면 RDS가 자동으로 Storage에 대한 스케일링을 수행하게 된다.**

따라서 스토리지 확장을 위해 데이터베이스를 중단하는 등의 작업을 따로 수행할 필요가 없다.<br>즉 애플리케이션이 RDS 데이터에 다량의 읽기 및 쓰기 작업을 수행할 때에 자동으로 특정 임계값을 확인하여<br>스토리지에 대한 오토스케일링 작업이 수행되는 RDS기능이다.

- 반드시 최대 스토리지 임계값을 설정해야 한다.
- 자동으로 Storage 가 수정된다.
  - 사용 가능한 공간이 할당된 스토리지의 10% 미만으로 떨어지고,
  - 낮은 스토리지 상태가 5분이상 지속되고,
  - 지난 수정이 6시간이상 지났을 경우에는 자동으로 스토리지를 수정하게 된다.
  - 이 같은 경우 해당 기능이 활성화 된 상태라면 스토리지가 자동으로 증가한다.
- 워크로드를 예측할 수 없는 애플리케이션에 유리하다.
- MariaDB, MySQL, PostgreSQL, SQL Server, Oracle 등 모든 RDS DB 엔진을 지원한다.