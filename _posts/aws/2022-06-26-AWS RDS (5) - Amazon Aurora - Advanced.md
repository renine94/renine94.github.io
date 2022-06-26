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

title: "[aws] RDS (5) - Amazon Aurora Advanced"
excerpt: "🚀 RDS, DB, Aurora, Advanced, Custom Endpoint, Serverless, Multi-Master, Read Auto-Scaling"

categories: aws
tag: [aws, rds, db, sql, aurora, advanced]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# RDS Aurora - 고급기능



## Aurora Replicas - Auto Scaling

![image-20220626215107321](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626215107321.png)



오토 스케일링 복제본에 대해 알아보자.

1. 클라이언트가 있고, 오로라 인스턴스가 3개 있다고 가정한다.
2. 하나는 Write Endpoint 을 통해 쓰고, 다른 2개는 Read Endpoint을 통해 읽는다.
3. Read Endpoint에 너무많은 Read Request가 있어서 Aurora DB의 CPU사용량이 증가했다.
   - 이런 경우, 오토 스케일링 복제본을 설정할 수 있다.
   - 자동으로 Read Enpoint가 새 Replica를 포함할 수 있도록 확장하게 된다.
   - 새로운 Replica는 트래픽을 수신하기 시작하고, 전체 CPU사용량을 낮추기위해 분산된 방식으로 읽기가 수행된다.
   - 이것이 오토 스케일링 복제본이다.



## Aurora - Custom Endpoints

> 사용자 지정 엔드포인트

![image-20220626215417445](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626215417445.png)

- 두 종류의 Replica가 있다고 가정한다.
  - db.r3.large 와 db.r5.2xlarge
  - 일부 Read DB 는 다른것보다 용량이 큰 상황이다.
  - 오로라 DB의 서브셋을 사용자 지정 엔드포인트로 정의한다.
  - 성능이 더 좋은 Read DB 에 사용자지정 Endpoint를 붙여야 이 DB에 대해 분석Query를 실행할 수 있다.



## Aurora Serverless

> 오로라의 서버리스 개념에 대해 알아보자.

![image-20220626220234140](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626220234140.png)

1. 자동화된 데이터베이스 인스턴스와 실제 사용을 기반으로 한 오토스케일링을 제공한다.
2. 드물거나 간헐적이거나 예측할 수 없는 애플리케이션(워크로드)가 있을 때 유용하다.
3. 용량 계획을 수행할 필요가 없다.
4. 초단위로 비용을 지불하고, 경우에 따라서는 좀더 비용면에서 효율적일 수 있다.
5. 작동 원리
   - 클라이언트는 오로라에서 관리하는 프록시플릿과 통신
   - 백엔드에서는 서버리스 방식으로 워크로드를 기반으로 많은 오로라 인스턴스가 생성됨
   - 그래서 미리 용량을 프로비저닝할 필요가 없다.



## Aurora Multi-Master

> 다중 마스터에 대해 알아보자.

![image-20220626220244621](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626220244621.png)

- 라이터 노드에 대한 즉각적인 장애 조치를 원하는 경우 (고가용성 원할때 사용)
- 이 경우 오로라 클러스터에 있는 모든 노드가 읽기와 쓰기 작업을 한다.
  - 쓰기 노드가 하나만 있고 다운돼서 실패하게 되면 읽기 복제본을 새로운 마스터로 승격시킨다.
  - 오로라 인스턴스 3개가 있다.
  - 서로 복제를 수행하고 있으며, 공유 스토리지 볼륨이 있다.
  - 클라이언트는 DB 연결을 여러 개 갖습니다.
  - 모든 Aurora 인스턴스는 쓰기 작업을 수행할 수 있으며, 만일 어떤 오로라 인스턴스가 실패하면 라이터 노드에 대한 즉각적인 장애 조치를 제공하는 다른 노드로 자동 장애 조치를 수행할 수 있다.



## Global Aurora

> 글로벌 오로라에 대해 알아보자.

![image-20220626220603680](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626220603680.png)



- Aurora Region간 Read Replica가 있다면 재해복구에도 유용하고 간단하게 구현 가능하다.
- 오늘날 권장되는 작업방식인 오로라 글로벌 DB를 설정할 수도 있다.
- 모든 읽기 및 쓰기가 발생하는 하나의 기본 Region이 있지만, 최대 5개의 보조 Read전용 Region을 설정할 수도 있다.
- 보조 Region당 Lack (복제지연) 이 1초(1000ms) 미만 이어야 하고, 최대 16개의 읽기전용 Replica를 가질 수 있다.
- 그러면 전 세계의 읽기전용 복제본에 대한 지연시간을 줄일 수 있다.
- 재해 복구 목적으로 다른 리전을 승격하는 어떤 리전에서 DB의 중단이 발생하더라도<br>RTO가 있으므로 복구 시간 목표는 1분 미만이 된다.
- 즉 다른 Region으로 복구하는데 1분 미만이 소요된다.



1. App의 Read/Write 를 수행하는 기본 Region으로 us-east-1이 있다.
2. eu-west-1 에 보조 Region을 설정한다.
3. 여기에서 오로라의 글로벌DB에서 복제가 일부 일어나고 그 리전의 App은 이 설정에서 읽기 작업만 수행할 수 있다.
4. 그러나 us-east-1이 실패하는 경우 eu-west-1를 읽기-쓰기 오로라 클러스터로 승격하여 장애 조치 가능



## Autora Machine Learning

> 오로라는 AWS 내의 머신러닝 서비스와 통합된다.

![image-20220626221630761](../../assets/images/posts/2022-06-26-AWS RDS (5) - Amazon Aurora - Advanced/image-20220626221630761.png)

- 오로라 머신러닝은 SQL 인터페이스를 통해 App에 ML기반 예측을 추가할 수 있는 개념이다.
- 오로라와 다양한 AWS ML Service간의 간단하고 최적화된 안전한 통합이다.
- 지원되는 두 서비스
  - **SageMaker**
    - 모든 종류의 머신 러닝 모델을 사용할 수 있음
  - **Amazon Comprehend**
    - 감정 분석을 수행할 때 쓴다.
- 저 위의 서비스를 잘 모르더라도, Aurora 가 위 서비스들과 통합되어 있다는 사실만 알면된다.
- 오로라 머신러닝을 사용하기 위해 ML 을 경험할 필요는 없다.
- 사용 사례
  - 사기 탐지
  - 광고 타겟팅 감정 분석
  - **제품 추천**

- 오로라는 사용자 프로필 쇼핑 내역 등과 같은 데이터를 머신러닝 서비스로 보낸다.
- 머신러닝서비스가 예측을 오로라에 직접 반환한다.
- 사용자가 빨간셔츠, 파란바지를 구매해야 한다는 예측이 나오면 오로라가 이 SQL쿼리의 결과를 App에 반환한다.



