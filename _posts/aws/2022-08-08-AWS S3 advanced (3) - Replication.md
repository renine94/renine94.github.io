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

title: "[aws] S3 Advanced (3) - Replication & Pre-Signed URLs"
excerpt: "🚀 S3, Replication, CRR, SRR, Pre Signed URLs"

categories: aws
tag: [aws, s3, replica, crr, srr, url, signed]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"






---

# S3 Replication (CRR & SRR)

- S3 복제인 CRR과 SRR 을 알아보자
- CRR: Region간 복제
- SRR: 동일 리전 복제



S3 버킷이 있고, 이 버킷은 eu-west-1 region에 있다. 모든 버킷 콘텐츠를 다른 region인 ap-northest-2 로 지속적으로 복제하려고 한다. 그렇게 하는 이유는 eu-west-1에 재해가 발생할 경우를 대비해 다른 리전에 저장하는 것이다.

- 내부적으로 비동기식 복제가 이루어진다.
- 소스 및 대상버킷에 versioning기능을 활성화 해야 한다.
- **리전간 복제, 즉 다른 리전에서 이동하거나 예를들어 eu-west-1 => ap-northest-2 로 이동하는 것이다.**
- 혹은, 동일 region복제인 SRR로 동일 리전에서 이동할 수 있다.
  - eu-west-1 => eu-west-1 처럼 말이다.
- 버킷이 다른 AWS 계정에 있을수도 있다.
- 복제는 비동기식이므로 백그라운드에서 실행된다.



- 복제를 하려면, S3에 적절한 IAM 권한을 제공해야 한다.
- 그러므로 CRR 사용사례는 규정 준수 및 액세스 시 지연 시간 단축 또는 계정간 복제 등이 있다.
- SRR 사용사례는 여러 계정에 걸친 로그 집계와 프로덕션 및 테스트 계정 간의 실시간 복제 또는 재해복구



## 1. S3 복제시 참고사항

- S3 Replica 기능이 활성화되면, 활성화 시점 이후의 업로드되는 파일들만 복제된다.
  - 기존 객체를 복제하려면 S3 배치 복제라는 기능을 사용하면 된다.
  - 그러면 기존 객체뿐 아니라 S3 복제 메커니즘에서 실패한 모든 객체를 복제할 수 있다.
- S3 버킷에서 Delete작업을 할때는 소스에서 대상 버킷으로 삭제 마커를 복제할지 여부를 선택하는 옵션이 있다.
- 특정 버전ID 를 삭제하려고 한다면 악의적인 삭제를 막기 위해 복제되지 않을것이다
  - 타인이 데이터를 영구 삭제하지 못하도록 하기 위해서이다.

- 연쇄(Chaining) 복제가 존재하지 않는다.
  - 버킷1이 버킷2에 복제되고, 버킷2가 버킷3에 복제되면 버킷1의 객체는 버킷3으로 복제되지 않는다.





버킷의 Management 탭에 들어가서 Replication rules 에서 create replication rule 을 클릭하여 설정할 수 있다.

삭제마커까지는 복제되지 않지만, 옵션에서 설정 체크를 하면 삭제한것도 복제가 된다.



# S3 Pre-signed URLs

> 사전 서명된 URL



- 사전 서명된 URL를 생성하려면 SDK 또는 CLI를 사용해야 한다.
  - 다운로드의 경우 쉬운방법으로 CLI 사용
  - 업로드의 경우 조금더 어려운 SDK 사용
- 사전 서명된 URL를 생성하면 기본적인 만료시간 3,600초, 즉 1시간이다.
  - 시간초과를 변경하려면 명령어 --expires-in 에 파라미터, 인자, 그리고 초 단위로 시간을 지정하면된다.
- 사전 서명된 URL이 사용자에게 제공될 때는 기본적으로 생성한 사람의 권한이 상속된다.
  - 즉 객체를 만든 이의 권한이다.
  - 따라서 사용자들은 상황에 따라 GET이나 PUT 권한을 사용할 수 있다.
- **사용사례**
  - **로그인한 사용자만이 S3 버킷의 프리미엄 영상을 다운로드하도록 승인하거나, 즉 로그인한 프리미엄 사용자에게만 약 15분동안 다운로드가 허용되도록 할 수 있다.**
  - 또는 파일을 다운로드할 사용자들의 목록이 지속적으로 변경될 경우, 사용자가 버킷에 직접 액세스하지 못하게끔 해야 한다.

굉장히 위험하고 유지 관리도 힘들기 때문이다. 항상 새로운 사용자가 몰리기 때문이다. 이런 경우에는 동적으로 URL을 생성해 pre-signed를 한 뒤, 시간이 지나면서 URL을 제공하고자 할 수도 있을것이다.

<br>아니면 사용자가 버킷의 특정 위치에만 파일을 업로드하도록 일시적으로 승인할 수도 있다. 예를 들면 사용자가 여러분의 S3버킷에 프로필 사진을 직접 업로드하도록 하는 식으로 말이다. 그럴때 Pre-Signed URLs 를 생성한다.





## 1. 실습

![image-20220808025147873](../../assets/images/posts/2022-08-08-AWS S3 advanced (3) - Replication/image-20220808025147873.png)

- 특정 버킷에 진입한다.
- Object actions 버튼을 클릭한다.
- Share with a presigned URL 버튼을 클릭한다.



![image-20220808025216953](../../assets/images/posts/2022-08-08-AWS S3 advanced (3) - Replication/image-20220808025216953.png)

- 누구든 지정된 시간동안 private 파일일지라도, URL 을 통해 접근할 수 있게 된다.

