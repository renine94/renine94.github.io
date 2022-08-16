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

title: "[aws] S3 & Athena Quiz & Summary"
excerpt: "🚀 S3, Athena 정리 및 퀴즈 문제풀이"

categories: aws
tag: [aws, s3, athena, quiz, summary]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# S3 & Athena Quiz



- **버전 관리를 활성화한 상태에서, S3 버킷 상의 파일을 삭제에 각별한 주의를 기울이려 한다. 실수로 영구 삭제를 하는 일이 없도록 하려면 어떻게 해야 하는가?**

  1. 버킷 정책 사용

  2. <span style="color: red;">MFA 삭제 활성화</span>

  3. 파일 암호화

  4. 버전 관리 비활성화



MFA Delete 는 유저들이 S3 객체를 삭제하기 전에 MFA 코드를 사용하도록 강제합니다. 이는 실수로 여욱 삭제를 하는 일이 없도록 보안을 한 층 더 강화해 줍니다.

<br><br>

- **S3 버킷에 있는 모든 파일이 기본으로 암호화 되었으면 한다. 이를 위한 최적의 방법은 무엇일까?**
  1. HTTPS 연결을 강제하는 버킷 정책 사용
  2. <span style="color: red;">기본 암호화 설정하기</span>
  3. 버전 관리 비활성화하기

<br>

<br>

- **일부 직원들이 액세스 권한이 없는 S3 버킷 내에 있는 파일에 액세스를 시도한 것으로 의심되는 상황이다. 직원들 모르게 이를 확인하기 위해서는 어떤 방법을 사용해야 하는가?**
  1. <span style="color: red;">S3 액세스 로그를 활성화하고 Athena를 사용해 로그를 분석</span>
  2. 직원들의 IAM 정책을 제한하고 CloudTail 로그를 확인
  3. 버킷 정책을 사용



S3 Access Log 는 S3 버킷에 대해 이루어진 모든 요청을 로깅하며, Amazon Athena는 로그 파일 및 서버리스 분석 실행에 사용된다.

<br><br>

- **S3 버킷의 콘텐츠를 다른 AWS 리전에서도 아무 제한 없이 사용할 수 있었으면 한다. 이는 팀이 최소 비용 및 최소 지연 시간으로 데이터 분석을 수행할 수 있게 해줄 것이다. 이 경우, 다음 중 어떤 S3 기능을 사용해야 하는가?**
  1. Amazon CloudFront 배포
  2. S3 버전 관리
  3. S3 정적 웹 사이트 호스팅
  4. <span style="color: red;">S3 복제</span>

S3 복제를 사용하면 S3 버킷에서 동일한/다른 AWS 리전의 다른 버킷으로 데이터를 복제할 수 있습니다.

<br><br>

- **3개의 S3 버킷이 잇습니다. 소스 버킷 A, 그리고 다른 AWS Region에 있는 두 개의 목적지 버킷인 B와 C<br>버킷A에서 버킷 B와 C 양측 모두로 객체를 복제하려면 어떤 방법을 사용해야 하는가?**
  1. <span style="color: red;">버킷 A에서 버킷 B로 복제를 구성한 뒤 버킷 A에서 버킷C로 복제를 구성</span>
  2. 버킷 A에서 버킷 B로 복제를 구성한 뒤 버킷 B 에서 버킷 C로 복제를 구성
  3. 버킷 A에서 버킷 C로 복제를 구성한 뒤 버킷 C 에서 버킷 A로 복제 구성하기

<br><br>

- **다음 중 Glacier Deep Archive 회수모드에 해당하지 "않는" 것을 고르시오.**
  1. <span style="color: red;">Expedited (1-5분)</span>
  2. Standard (12시간)
  3. Bulk (48시간)



<br><br>

- **어떤 방법을 사용해야 S3 버킷으로 객체가 업로드되었음을 알 수 있을까?**
  1. S3 Select
  2. S3 Access Log
  3. <span style="color: red;">S3 Event Notification</span>
  4. S3 Analysis

<br><br>

- **점점 늘어나고 있는 연결된 사용자들의 목록에 임시 URL을 제공하여, 이들이 특정 로케이션에서 S3 버킷으로 파일 업로드를 수행할 수 있도록 허가하려 합니다. 무엇을 사용해야 하는가?**
  1. S3 CORS
  2. S3 Pre-Signed URL
  3. S3 버킷 정책
  4. IAM 사용자

S3 미리 서명된 URL은 S3 버킷에서 특정 조치를 취할 수 있도록 제한된 시간 동안의 액세스를 허용하는 임시 URL입니다.

<br><br>

- **S3 버전 관리가 활성화된 S3 버킷이 잇다. 이 S3 버킷은 여러 객체를 지니고 있으며, 비용 절감을 위해 오래된 버전을 삭제하려 합니다. 오래된 객체 버전의 삭제를 자동화하기 위해서 사용할 수 있는 최선의 방법은 무엇인가?**
  1. S3 수명 주기 규칙 - 만료 조치
  2. <span style="color: red;">S3 수명 주기 규칙 - 전환 조치</span>
  3. S3 액세스 로그

<br><br>

- **서로 다른 티어 간의 S3 객체 전환을 자동화하기 위해서는 어떻게 해야 할까?**
  1. AWS Lambda
  2. CloudWatch Events
  3. <span style="color: red;">S3 수명 주기 규칙</span>

<br><br>

- **다음 중 Glacier Flexible 검색 옵션이 아닌 것은 무엇인가요?**
  1. <span style="color: red;">instant (10초)</span>
  2. Expedited (1~5분)
  3. Standard (3~5시간)
  4. Bulk (5~12시간)



>  이 부분은 한번 더 복습해봐야 겠다... 자주 까먹는다..

<br><br>

- **Multi-Part 업로드를 사용해 S3 버킷으로 크기가 큰 파일을 업로드하던 도중, 네트워크 문제로 인해 완료되지 않은 부분의 상당량이 S3 버킷에 저장되었습니다. 완료되지 않은 부분은 불필요하며, 여러분의 비용을 소모합니다. 완료되지 않은 부분을 삭제하기 위해 사용할 수 있는 최적의 접근법은 무엇인가?**
  1. AWS Lambda로 오래된/완료되지 않은 각 부분을 루프하여 삭제
  2. AWS 지원 센터에 오래된/완료되지 않은 부분을 삭제해 줄 것을 요청
  3. <span style="color: red;">S3 수명 주기 정책을 사용해 오래된/완료되지 않은 부분의 삭제를 자동화</span>

<br><br>

- **다음의 서버리스 데이터 분석 서비스들 중, S3에 있는 데이터를 쿼리하는 데에 사용할수 있는 것은 무엇인가?**
  1. S3 분석
  2. <span style="color: red;">Athena</span>
  3. Redshift
  4. RDS



<br><br>

- **S3 수명 주기 규칙에 대한 추천 사항을 찾고 있다. 서로 다른 스토리지 계층 간의 객체 이동에 필요한 최적의 일수는 어떻게 분석 또는 찾을 수 있을까?**
  1. S3 인벤토리
  2. <span style="color: red;">S3 분석</span>
  3. S3 수명 주기 규칙 관리자



<br><br>

- **Amazon RDS PostgreSQL 을 사용하여 S3에 파일의 인덱스를 구축하려 한다. 인덱스 구축을 위해서는 파일 콘텐츠 자체의 메타데이터를 포함하고 있는 S3에 있는 각 객체의 첫 250바이트를 읽는 작업이 필수적이다. S3 버킷에는 총 50TB에 달하는 100,000개 이상의 파일이 포함되어 있다. 이 경우 인덱스를 구축하기 위한 효율적인 방법은 무엇일까?**
  1. RDS 가져오기 기능을 사용해 S3로부터 PostgreSQL로 데이터를 로드하고, SQL 쿼리를 실행해 인덱스 구축하기
  2. S3 버킷을 트래버스하고, 파일을 하나씩 읽어 들여 첫 250바이트를 추출한 후, RDS에 해당 정보를 저장하는 애플리케이션 생성
  3. <span style="color: red;">S3 버킷을 트래버스하고, 첫 250바이트에 대한 바이트 범위 페치를 실행한 후, RDS에 해당 정보를 저장하는 애플리케이션 생성</span>
  4. S3 버킷을 트래버스하고, S3 Select를 사용해 첫 250바이트를 얻은 후, RDS에 해당 정보를 저장하는 애플리케이션 생성

<br><br>

- **여러분의 기업은 규정 준수를 위해 데이터베이스 백업을 4년 동안 보관해야 한다는 정책을 가지고 있다. 이를 제거하는 것은 불가능해야 한다. 어떤 방법을 사용해야 하는가?**
  1. <span style="color: red;">Vault 잠금 정책을 가진 Glacier Vaults</span>
  2. 제한 Linux 권한을 가진 EFS 네트워크 드라이브
  3. 버킷 정책을 가진 S3



<br><br>

- **S3 버킷으로 업로드하려는 대규모의 데이터셋이 온프레미스로 저장되어 있습니다. 이 데이터셋은 10GB 파일로 분할되어 있습니다. 대역폭은 좋으나, 인터넷 연결은 불안정합니다. 이 경우, 데이터셋을 S3에 업로드하는 프로세스를 빠르게, 그리고 인터넷 연결 문제 없이 처리하려면 어떤 방법을 사용해야 하는가?**
  1. 멀티파트 업로드만 사용
  2. S3 Select와 S3 전송 가속화 사용
  3. <span style="color: red;">S3 멀티파트 업로드와 S3 전송 가속화 사용하기</span>



<br><br>

- **S3 에 저장된 데이터셋의 서브셋을 CSV형식으로 회수하려 합니다. 컴퓨팅 및 네트워크 비용 최소화를 위해 한 달 분의 데이터와 10개 열 중 3개의 열만 회수하려 합니다. 무엇을 사용해야 하는가?**
  1. S3 분석
  2. S3 액세스 로그
  3. <span style="color: red;">S3 Select</span>
  4. S3 인벤토리



