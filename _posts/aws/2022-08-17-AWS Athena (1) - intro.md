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

title: "[aws] Athena (1) - Intro & Practice"
excerpt: "🚀 Athena, Basic, S3에 저장된 객체에 대한 분석수행 서버리스 쿼리 서비스"

categories: aws
tag: [aws, athena, s3, query]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Amazon Athena

- **S3 객체에 대해 분석을 수행하는 서버리스 쿼리 서비스**
- 즉, SQL 언어로 이러한 파일들을 쿼리하지만 로드할 필요는 없다.
- 파일들은 S3 에 있고, 나머지는 Athena 가 처리해준다.
- **CSV, Json**, ORC, Avro, Parguet 등 다양한 파일의 포맷을 지원한다. (Athena는 Presto 엔진 기반)



- 사용자들이 데이터들을 아마존 S3에 로드하면 Athena는 이러한 데이터를 쿼리하고 분석한다.
- Amazon QuickSight 서비스를 이용하면 보고서도 받아볼 수 있다.



- **가격은 스캔된 데이터 TB 당 5달러 이다.**
- 압축되거나 컬럼형으로 저장된 데이터를 사용할 경우 비용을 절감할 수 있다.
  - 데이터를 스캔하는 양이 적어지기 때문
- UseCase (사용사례)
  - BI (비즈니스 인텔리전스), 분석, 보고, VPC나 ELB 로그의 Flow Logs 분석
  - CloudTrail 로그, 플랫폼 로그 등의 AWS의 로그를 사용할 경우 Athena가 유용하다.



SQL 을 사용하며, 데이터 분석 서버리스 등의 키워드가 나오면 Amazon Athena 를 떠올리면 된다.



## 1. 실습

> 비용이 발생할 수 있는 부분이어, 사내 학습용 Dev AWS 에서 진행하려 했으나, IAM 권한이 없어서 사진을 많이 스샷을 많이 첨부하지 못하는점 양해바랍니다. ( _ _ )....

![image-20220817011253770](../../assets/images/posts/2022-08-17-AWS Athena (1) - intro/image-20220817011253770.png)



```sql
create database s3_access_logs_db;

# 테이블 생성 
CREATE EXTERNAL TABLE IF NOT EXISTS s3_access_logs_db.mybucket_logs(
         BucketOwner STRING,
         Bucket STRING,
         RequestDateTime STRING,
         RemoteIP STRING,
         Requester STRING,
         RequestID STRING,
         Operation STRING,
         Key STRING,
         RequestURI_operation STRING,
         RequestURI_key STRING,
         RequestURI_httpProtoversion STRING,
         HTTPstatus STRING,
         ErrorCode STRING,
         BytesSent BIGINT,
         ObjectSize BIGINT,
         TotalTime STRING,
         TurnAroundTime STRING,
         Referrer STRING,
         UserAgent STRING,
         VersionId STRING,
         HostId STRING,
         SigV STRING,
         CipherSuite STRING,
         AuthType STRING,
         EndPoint STRING,
         TLSVersion STRING
) 
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES (
         'serialization.format' = '1', 'input.regex' = '([^ ]*) ([^ ]*) \\[(.*?)\\] ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) \\\"([^ ]*) ([^ ]*) (- |[^ ]*)\\\" (-|[0-9]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) (\"[^\"]*\") ([^ ]*)(?: ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*) ([^ ]*))?.*$' )
LOCATION 's3://target-bucket-name/prefix/';


# HTTP Method 별 200, 404 등이 몇번 발생했는 지 집계SQL 조회
SELECT requesturi_operation, httpstatus, count(*) FROM "s3_access_logs_db"."mybucket_logs" 
GROUP BY requesturi_operation, httpstatus;

# 권한이 없는사람이 S3 Objects 에 접근한 횟수 세고 누구인지 확인
SELECT * FROM "s3_access_logs_db"."mybucket_logs"
where httpstatus='403';
```



**Athena 장점**

- S3 의 데이터를 쿼리해 서버 설정과 데이터의 변형 없이도 적절한 데이터 포맷을 설정함으로써 복잡한 쿼리를 직접 실행해 데이터를 특정할 수 있다
- 최근 쿼리와 저장된 쿼리도 확인 가능
- 쿼리 결과를 대상 버킷에 암호화하기 위해 설정을 편집할 수도 있다.
- 서버리스 서비스이다. (따로 DB설정이나 할 필요 없음)



