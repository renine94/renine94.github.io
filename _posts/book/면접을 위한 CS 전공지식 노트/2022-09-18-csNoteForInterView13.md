---
layout: single

header:
  teaser: /assets/images/logo/book.jpg
  overlay_image: /assets/images/logo/book.jpg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "면접을 위한 CS 전공지식 노트 (13) - 데이터베이스 종류"
excerpt: "🚀 Database, RDS, MySQL, PostgreSQL, NoSQL, MongoDB"

categories: book
tag: [cs, db]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# 데이터베이스 종류



## 01. 관계형 데이터베이스

관계형 데이터베이스(RDBMS)는 행과 열을 가지는 표 형식 데이터를 저장하는 형태의 데이터베이스를 가리키며 SQL이라는 언어를 써서 조작합니다. MySQL, PostgreSQL, Oracle, SQL Server, MSSQL 등이 있습니다. 참고로 관계형 데이터베이스의 경우 표준 SQL은 지키기는 하지만, 각각의 제품에 특화시킨 SQL을 사용합니다. 예를 들어 오라클의 경우 PL/SQL 이라고 하며, SQL Server에서는 T-SQL, MySQL은 SQL을 씁니다.



### MySQL

MySQL은 대부분의 운영체제와 호환되며 현재 가장 많이 사용하는 데이터베이스입니다.

스택오버플로우에서 조사한 결과(2021)에서 MySQL은 아직도 압도적으로 가장 많이 쓰는 데이터베이스이며, 메타, 트위터 등 많은 기업에서 MySQL을 사용하고 있습니다.

C, C++로 만들어졌으며 MyISAM 인덱스 압축기술, B-트리 기반의 인덱스, 스레드 기반의 메모리 할당 시스템, 매우 빠른 조인, 최대 64개의 인덱스를 제공합니다. 대용량 데이터베이스를 위해 설계되어 있고 롤백, 커밋, 이중 암호 지원 보안 등의 기능을 제공하며 많은 서비스에서 사용합니다.

**MySQL의 스토리지 엔진 아키텍처**는 다음과 같습니다.

![Overview of MySQL Storage  Engine Architecture](../../../assets/images/posts/2022-09-18-csNoteForInterView13/mysql-architecture.png)

**데이터베이스의 심장과도 같은 역할을 하는 곳이 바로 스토리지 엔진인데**, 모듈식 아키텍처로 쉽게 스토리지 엔진을 바꿀 수 있으며 데이터 웨어하우징, 트랜잭션 처리, 고가용성 처리에 강점을 두고 있습니다. 스토리지 엔진 위에는 커넥터 API 및 서비스 계층을 통해 MySQL 데이터베이스와 쉽게 상호 작용할 수 있습니다.

또한, MySQL은 쿼리 캐시를 지원해서 입력된 쿼리문에 대한 전체 결과 집합을 저장하기 때문에 사용자가 작성한 쿼리가 캐시에 있는 쿼리와 동일하면 서버는 단순히 구문 분석, 최적화 및 실행을 건너뛰고 캐시의 출력만 표시합니다.





### PostgreSQL

<img src="../../../assets/images/posts/2022-09-18-csNoteForInterView13/PostgreSQL-Logo.png" alt="PostgreSQL logo and symbol, meaning, history, PNG" style="zoom: 33%;" />

PostgreSQL은 MySQL 다음으로 개발자들이 선호하는 데이터베이스 기술로 널리 인정받고 있습니다.

디스크 조각이 차지하는 영역을 회수할 수 있는 장치인 VACUUM이 특징입니다. 최대 테이블의 크기는 32TB이며 SQL뿐만 아니라 JSON을 이용해서 데이터에 접근할 수 있습니다. 지정 시간에 복구하는 기능, 로깅, 접근 제어, 중첩된 트랜잭션, 백업 등을 할 수 있습니다.

## 02. NoSQL 데이터베이스

NoSQL(Not only SQL) 이라는 슬로건에서 생겨난 데이터베이스입니다. SQL을 사용하지 않는 데이터베이스를 말하며 대표적으로 MongoDB와 redis 등이 있습니다.



### MongoDB

MongoDB는 JSON을 통해 데이터에 접근할 수 있고, Binary JSON 형태 (BJSON)로 데이터가 저장되며 와이어드타이거 엔진이 기본 스토리지 엔진으로 장착된 키-값 데이터 모델에서 확장된 도큐먼트 기반의 데이터베이스입니다. 확장성이 뛰어나며 빅데이터를 저장할 때 성능이 좋고 고가용성과 샤딩, 레플리카셋을 지원합니다. 또한 스키마를 정해 놓지 않고 데이터를 삽입할 수 있기 때문에 다양한 도메인의 데이터베이스를 기반으로 분석하거나 로깅 등을 구현할 때 강점을 보입니다.

또한, MongoDB는 도큐먼트를 생성할 때마다 다른 컬렉션에서 중복된 값을 지니기 힘든 유니크한 값인 ObjectID가 생성됩니다.

![MongoDB 이해하기](../../../assets/images/posts/2022-09-18-csNoteForInterView13/objectid.png)

이는 기본키로 유닉스 시간 기반의 타임스탬프(4바이트), 랜덤 값(5바이트), 카운터(3바이트)로 이루어져 있습니다.



### redis

<img src="../../../assets/images/posts/2022-09-18-csNoteForInterView13/Redis-Logo.wine.png" alt="Download Redis Logo in SVG Vector or PNG File Format - Logo.wine" style="zoom:33%;" />

redis는 **인메모리 데이터베이스이자 키-값 데이터 모델 기반의 데이터베이스**입니다.

기본적인 데이터 타입은 문자열(string)이며 최대 512MB까지 저장할 수 있습니다. 이외에도 셋(set), 해시(hash) 등을 지원합니다.

pub/sub 기능을 통해 채팅 시스템, 다른 데이터베이스 앞단에 두어 사용하는 캐싱 계층, 단순한 키-값이 필요한 세션 정보 관리, 정렬된 셋(sorted set) 자료 구조를 이용한 **실시간 순위표(랭킹) 서비스에 사용**합니다.



