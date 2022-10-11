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

title: "[aws] Integration & Messaging (8) - Kinesis Overview"
excerpt: "🚀 Kinesis, Data Streams, Firehose, Data Analytics, Video Streams"

categories: aws
tag: [aws, kinesis, streams, firehose, analytics, redshift, datadog]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Kinesis Overview

> 키네시스는 실시간으로 데이터를 수집, 처리, 분석, 스트리밍하는 역할을 한다.
>
> 실시간으로 생성된 데이터를 분석 또는 처리하기 위해 앱으로 보내고자 할 때 사용됨

- 앱 로그, 지표, 웹사이트 클릭스트림, IoT 텔레메트리 데이터 등이 해당
- 컴포넌트의 종류 4가지
  1. **Kinesis Data Streams**
     - 데이터 스트림을 캡쳐, 처리, 저장
  2. **Kinesis Firehose**
     - AWS 데이터 스토어에 데이터스트림을 저장
  3. **Kinesis Data Analytics**
     - SQL이나, Apache Flink로 데이터스트림을 분석
  4. **Kinesis Video Streams**
     - 비디오스트림을 캡처, 처리, 저장 역할



## 01. Kinesis Data Streams

![image-20221012020806235](../../assets/images/posts/2022-10-12-AWS Integration & Messaging (8) - Kinesis Overview//image-20221012020806235.png)



- 중앙에 Kinesis Data Streams가 있고, 그 안에는 스트림이 있다고 가정
- 스트림은 샤드로 구성되어 있으며 각각 번호가 부여되어 있음
- 예를 들어 샤드1, 샤드2, ,,, 샤드30 까지 있다고 해보고, 샤드의 개수는 조절할 수 있다.
- 키네시스 데이터 스트림에 포함된 샤드 수가 많을수록 스트림에서의 처리량을 높일 수 있다.



- Kinesis Data Streams 에서 처리할 데이터는 생산자(producer)가 담당
- 생산자의 유형
  - 애플리케이션, 모바일 클라이언트
  - 내부의 SDK, KPL (Kinesis Producer Library)
  - Kinesis Agent
- 위의 생산자들에 의해 데이터를 생산해 Kinesis Data Streams로 전송
- 전송된 모든 애플리케이션에서 실시간으로 이루어진다.



- 스트림으로 전송되는 레코드는 파티션 키와 최대 1MB 크기의 볼륨으로 이루어져 있다.
- 이러한 레코드를 생성하여 Kinesis Data Streams로 보냅니다.
- 샤드로 스트림을 확장 할 수 있다.
- 각 샤드는 초당 1MB 또는 1,000개의 메시지를 전송합니다.
- 샤드가 30개 들어있다면 초당 30MB or 30,000개의 메시지가 된다.



- 다른쪽에는 Kinesis Data Streams 데이터의 소비자(Consumer)가 있다.
- 소비자 유형
  - Kinesis Client Library (KCL)
  - SDK
  - Lambda 함수
  - Kinesis Data Firehose
  - Kinesis Data Analytics
- 소비자에게 전달되는 레코드에는
  - 동일한 파티션 키
  - 샤드에 포함된 데이터를 구분하는 시퀀스 번호
  - 데이터 블롭 으로 이루어져 있다.



- Kinesis Data Streams 데이터의 소비자가 여러명일 경우에는 Fan-out 패턴을 사용하면 된다.
- Kinesis Data Streams의 pub/sub 패턴인 셈이다.
- 소비 메커니즘은 두 가지로 구분할 수 있다.
  1. 공유 소비 메커니즘
     - 모든 소비자 애플리케이션에 샤드당 2MB/s 로 데이터를 전송
  2. 향상된 팬아웃 소비자 매커니즘
     - 샤드당 2MB/s 에 전송할 수 있다.
- 2번째 방법이 더 비싸고 처리량도 많다.



### Kinesis Data Streams 특징

- 보존기간 1일~365일, 그동안은 데이터를 재처리 or 재생산 가능
- Kinesis에 저장된 데이터는 삭제가 불가능하며, 이러한 특징을 불변성(immutability) 라고 함
- Kinesis Data Streams로 메시지를 전송하면 파티션 키가 생성되고, 같은 파티션키를 갖는 메시지는<br>같은 샤드를 통해 전송되어 키 기반 정렬이 가능
- 생산자는 SDK, KPL, Kinesis Agent를 사용할 수 있음
- 소비자는 원하는대로 KCL, SDK를 직접 만들거나 AWS Lambda, Firehose, Analytics와 같은 관리된 소비자를 사용할 수 있음



## 02. Kinesis Data Streams - Capacity Modes

> 2가지 용량 모드가 있다.

- **프로비저닝된 용량 모드 (전통적 방식)**
  - 프로비저닝할 샤드 수 정하고, 직접 or API를 통해 조정
  - 샤드는 각각 초당 1MB or 1,000개의 레코드를 처리
  - 출력량의 경우에는 초당 2MB를 처리할 수 있음
  - 이 모드는 전통적인 방식 또는 팬아웃 패턴에 적합
  - 시간 단위로 샤드당 비용이 부과하므로 주의해야 함



- **온디맨드 모드**
  - 용량을 프로비저닝하거나 관리할 필요가 없음
  - 시간이 지나면 수요량에 따라 자동으로 조정 (오토 스케일 아웃???)
  - 기본적으로는 초당 4MB or 4,000개의 레코드를 처리
  - 이 용량은 자동으로 최근 30일 간 최대 사용량에 따라 조정됨
  - 시간 단위로 스트림당 데이터량(GB)에 따라 비용이 부과되므로 가격 산정 방식이 다르다.

<br>

- 사용량을 예상하기 어렵다면 **온디맨드**
- 용량을 사전에 계획하고 싶다면 **프로비저닝 모드**를 선택





## 03. Kinesis Data Firehose

> Firehose의 개념은 무척 간단하다.
>
> 목적지까지 전송되는 데이터를 저장하는 것이다.

![image-20221012022743205](../../assets/images/posts/2022-10-12-AWS Integration & Messaging (8) - Kinesis Overview//image-20221012022743205.png)



- 데이터는 생산자가 여러 가지 애플리케이션을 통해 Firehose에 데이터를 전송하거나,
- Firehose가 Kinesis Data Streams나 CloudWatch, IoT 에서 데이터를 불러올 수도 있다.
  - 주로 Kinesis Data Streams에서 데이터를 불러오는 방식으로 진행된다
- 데이터 전송 속도는 초당 최대 1MB
- 레코드를 변형할 때는 Lambda 함수를 통해 데이터에 일부 수정을 가할 수 있다.
- 데이터 배치(batch)를 작성하여 데이터베이스 등의 목적지에 전송
  - 이것을 배치 쓰기라고 한다.
  - 데이터를 바로바로 쓰지(write)않고, 배치로 한 번에 쓰는 효율적인 방식이다.
  - 따라서 Kinesis Data Firehose는 거의 실시간 서비스라 할 수 있다.
- 목적지가 되는 AWS로는 
  - S3
  - Redshift
    - Redshift에 전송하려면 먼저 Firehose에서 S3로 데이터를 보내고 복사 명령어를 통해 Redshift로 보내야함
  - ElasticSearch

<br>



- 타사 목적지
  - **데이터독**
  - Splunk
  - **New Relic**
  - MongoDB
  - etc.... 이 있다.



- 또한 API 형태의 HTTP 엔드포인트를 갖춘 사용자 지정 목적지로도 Firehose를 통해 데이터를 전송할 수 있음
- 마지막으로, 처리에 실패 or 처리된 모든 데이터를 저장하고 싶을 때는 Firehose의 모든 데이터를 S3백업버킷에 저장할 수도 있습니다.

- Firehose는 완전관리형 서비스라서 별도로 관리할 필요가 없고 자동으로 확장되며 서버가 없다는 점에서 Streams와 차별점이 된다.

- 사용할 수 있는 서비스
  1. Redshift, S3, ElasticSearch
  2. 타사 파트너사 (datadog, new Relic, etc...)
  3. 사용자 지정 HTTP Endpoint

- 비용은 Firehose에서 처리한 데이터에만 부과하므로, 미리 프로비저닝 하지않아도 되고,
- 거의 실시간에 가깝다는 이점이 있다.





## 04. Kinesis Data Streams VS Firehose

![image-20221012024108220](../../assets/images/posts/2022-10-12-AWS Integration & Messaging (8) - Kinesis Overview//image-20221012024108220.png)



- Data Streams
  - 대규모로 데이터를 수집하는 스트리밍 서비스
  - 사용자 지정 코드를 작성해 데이터 전송과 소비에 사용가능
  - 200ms 정도의 속도로 실시간 처리
  - 필요에 따라 샤드를 조정하기 위해 샤드추가 및 분할, 감소시키는 샤드 통합 가능
  - 1~365일간 보존되며, 재생기능 지원



- Firehose
  - 원하는 목적지 (s3, Redshift, ES, 타사, HTTP) 로 전송하는것이 목적
  - 완전 관리형 서비스
  - 데이터는 버퍼에서 배치로 쓰이기 때문에 거의 실시간으로 작동
  - 확장은 자동으로 이루어지며 데이터 저장소가 없으므로 Firehose에서 데이터 재생 불가능



## 05. Kinesis Data Analytics

> SQL  앱을 위한 Analytics

![image-20221012024538339](../../assets/images/posts/2022-10-12-AWS Integration & Messaging (8) - Kinesis Overview//image-20221012024538339.png)

- 스트림에 SQL 코드를 적용하려면 먼저, Analytics가 소스에서 데이터를 불러온다.
  - source -> Data Streams, Firehose
- 작성한 SQL 문장을 통해 실시간으로 데이터를 처리한 뒤, 그 쿼리의 결과를 목적지로 전송
  - DataStreams, Firehose
- Firehose는 S3를 통해 Redshift 이나 다른 Firehose 목적지로 데이터를 전송할 수 있다.



- Kinesis Data Analytics는 SQL로 Kinesis Streams에서 실시간 분석을 하고
- 완전 관리형 모델이므로 프로비저닝할 서버가 없다.
- 자동으로 확장되며 실시간 분석이 목적
- 비용은 Kinesis Data Analytics에서 처리된 만큼만 부과
- 실제 사용량에 기반하며, 실시간 쿼리를 통해 스트리밍을 생성할 수 있다.



- 사용사례
  - 시계열 분석
  - 실시간 대시보드
  - 실시간 지표 (metric)











