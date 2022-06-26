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

title: "[aws] RDS (3) - RDS Security"
excerpt: "🚀 RDS, DB, Security, Encryption"

categories: aws
tag: [aws, rds, db, sql, security]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"






---

# RDS Security

암호화에 대해 알아보자.
{: .notice--success}



- At rest encryption
  - AWS KMS 로 마스터 DB 와 읽기 DB 를 암호화 할 수 있다.
  - 암호화 실행시 실행 시간을 정의해야 한다.
  - 마스터 DB 를 암호화 하지 않으면, 복제본도 암호화할 수 없다.
  - Oracle과 SQL Server에서 TDE (Transparent Data Encryption) 라고하는 투명한 데이터 암호화를 활성화 할 수 있으며, 이는 데이터베이스 암호화의 대안을 제공한다.
- In-flight encryption
  - SSL 는 데이터를 전송중에 암호화를 사용한다.
  - 클라이언트에서 데이터베이스로 전송중인 데이터
  - 데이터베이스 연결시 신뢰할 수 있는 인증서로 SSL 옵션을 제공하면 SSL을 연결할 수 있다.
    - PostgreSQL
      - rds.force_ssl=l (파라미터 그룹에서 설정해야함 RDS Console)
      - 메게변수 그룹 (파라미터 그룹) 에서 설정
    - MySQL
      - GRANT USAGE ON *.* TO 'mysqluser'@'%' REQUIRE SSL;
      - 데이터베이스 내에서 SQL 명령문을 실행



## Encryption Operations

- RDS 백업을 암호화 하는 방법
  - 암호화되지 않은 RDS DB 에서 스냅샷을 생성하면, 스냅샷 자체는 암호화X
  - 암호화된 RDS DB dㅔ서 스냅샷을 생성하면, 스냅샷 자체는 암호화O (기본값은 아니다)
  - 암호화되지 않은 스냅샷을 암호화된 스냅샷으로 복제해야 한다.
- 암호화되지 않은 RDS DB를 암호화 하는 방법
  - 암호화되지 않은 DB 의 스냅샷을 생성하여 복제한다.
  - 복제한 스냅샷의 암호화를 활성화 한다.
  - 이 암호화된 스냅샷으로 데이터베이스를 복원할 수 있다.
    - 이는 암호화된 RDS DB 를 제공한다.
  - 애플리케이션에서 이전 DB 에서 암호화된 DB 로 옮긴다.
  - 이전 DB 는 삭제한다.



## Network & IAM

- Network Security
  - RDS 는 대부분 private subnet 에서 배포된다.
  - 따라서 데이터베이스가 www에 노출되지 않도록 해야한다.
  - RDS 보안은 RDS 인스턴스에 연결되어 있는 보안 그룹을 활용해 실행된다.
    - EC2 인스턴스와 동일한 개념
    - RDS 와 통신할 수 있는 IP 또는 보안 그룹을 제어한다.



- Access Management
  - 사용자 관리 등과 권한인 액세스 관리
  - AWS RDS 를 관리하는 사람만 제어할 수 있다.
  - DB 를 생성하고 삭제할 수 있으며 읽기 전용 복제본 생성등을 할 수 있다.
  - 기존방식으로 DB에 로그인하기위해 기존 사용자이름과 암호화를 사용하거나,<br>MySQL, PostgreSQL 과 같은 IAM 기반의 인증을 사용할 수 있다.
  - 결국 DB보안은 주로 DB안에서 이루어진다.



## RDS - IAM Authentication

![image-20220626210434161](../../assets/images/posts/2022-06-26-AWS RDS (3) - RDS Security/image-20220626210434161.png)

- IAM DB 인증은 MySQL, PostgreSQL 에서만 사용가능
- 비밀번호가 필요없으며, IAM RDS API 를 호출하여 인증토큰을 얻기만 하면 된다.
- 인증 토큰은 15분간 유효하다.
- 이점
  - 네트워크 입출력은 SSL 로 암호화 된다.
  - IAM 은 DB 내부에 사용자 관리 대신 중앙에서의 사용자 관리에 사용된다.
  - 중앙 집중화된 인증 유형이다.
  - IAM 역할과 EC2 인스턴스 프로파일로 쉽게 통합할 수 있다.



## RDS Security - 정리

- 미사용 데이터 암호화
  - DB 인스턴스를 처음 생성할 때만 실행된다.
  - 또는 암호화X DB => Snapshot => copy Snapshot as encrypted => create DB from snapshot
- 나의 책임
  - DB 의 보안그룹에서 port, IP, 인바운드 규칙을 체크해야 한다.
  - 내부 데이터베이스의 모든 사용자 생성 및 권한을 관리해야 한다.
  - mySQL, PostgreSQL 용 IAM 으로 관리해야 한다.
  - 또는 퍼블릭 접근권한이 있거나 없는 DB를 생성해 프라이빗 서브넷이나 퍼블릭으로 설계를 한다.
  - 파라미터 그룹과 데이터베이스가 SSL연결만 허용하도록 구성해야 한다.
- AWS의 책임
  - SSH 액세스가 발생하지 않도록 하고,
  - DB 패치나 OS 패치를 할필요가 없어진다. (AWS 에서 해준다)