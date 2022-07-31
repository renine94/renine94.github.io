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

title: "[aws] S3 (6) - Summary & Quiz"
excerpt: "🚀 S3 Summary, Quiz"

categories: aws
tag: [aws, s3, summary, quiz]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# S3 Summary & Quiz



1. 25GB 크기의 파일을 S3에 업로드하려 시도 중이지만, 오류가 발생하고 있습니다. 이 경우, 가능성이 있는 원인은 무엇일까요?
   - S3의 파일 크기 제한이 5GB 임
   - 요청된 AWS 리전의 S3 서비스가 차단된 상태
   - <span style="color: red;">5GB보다 크기가 큰 파일을 업로드할 때는 멀티파트 업로드를 사용함</span>

파일 크기가 100MB가 넘는 경우에는 멀티파트 업로드가 권장된다.



2. dev라는 이름의 새로운 S3 버킷을 생성하려 하던 중 오류가 발생했습니다. S3 버킷이 생성된 적이 없는 새로운 AWS 계정을 사용 중입니다. 이 경우, 가능성이 있는 원인은 무엇일까요?
   - S3 버킷 생성에 필요한 IAM 권한의 부재
   - <span style="color: red;">S3 버킷 이름은 전역에서 고유해야 하며 dev는 이미 사용 중임</span>



3. 이미 많은 파일을 포함하고 있는 S3 버킷에 버전 관리를 활성화한 상태입니다. 기존의 파일은 다음 중 어떤 버전을 가지고 있을까요?
   - 1
   - 0
   - -1
   - <span style="color: red;">null</span>



4. 여러분의 고객은 S3에 있는 파일을 암호화하되, 암호화 키를 AWS에 저장하지 않고 직접 관리하기를 원하고 있습니다. 이에 여러분은 고객에게 ............................. 를 추천했습니다.
   - SSE-S3
   - SSE-KMS
   - <span style="color: red;">SSE-C</span>
   - 클라이언트 측 암호화

SSE-C을 사용하면, AWS에서 암호화가 일어나지만 당사자가 암호화 키를 전적으로 관리하게 됩니다.



5. 여러분이 근무 중인 기업이 S3에 저장된 자신들의 데이터를 암호화하고자 합니다. 암호화 키가 AWS에 저장되고 관리되더라도 문제가 없으나, 암호화 키에 대한 교체 정책은 기업이 직접 관리하기를 원하고 있습니다. 이에 여러분은 고객에게 ............................. 를 추천했습니다.
   - SSE-S3
   - <span style="color: red;">SSE-KMS</span>
   - SSE-C
   - 클라이언트 측 암호화

SSE-KMS를 사용하면, AWS에서 암호화가 일어나고 AWS가 암호화 키를 관리하게 되지만, 암호화 키의 교체 정책은 당사자가 전적으로 관리하게 됩니다. AWS에 저장된 암호화 키



6. 기업은 AWS의 암호화 프로세스를 신뢰하지 않으며, 애플리케이션 내에서 프로세스가 이뤄지기를 원하고 있습니다. 이에 여러분은 고객에게 ............................. 를 추천했습니다.

   - SSE-S3

   - SSE-KMS

   - SSE-C

   - <span style="color: red;">클라이언트 측 암호화</span>

클라이언트 측 암호화를 사용하면, 암호화를 직접 수행해야 하며 당사자가 암호화 키를 전적으로 관리하게 됩니다. 암호화를 여러분이 직접 수행하고 암호화된 데이터를 AWS로 보냅니다. AWS는 여러분의 암호화 키에 대해 알지 못하며, 데이터를 복호화할 수 없습니다.



7. S3 버킷 정책을 업데이트해 IAM 사용자들이 S3 버킷 내의 파일을 읽기/쓰기할 수 있도록 허가했으나, 한 명의 사용자가` PutObject` API 호출을 수행할 수 없다며 불만을 토로하고 있습니다. 이 경우, 가능성이 있는 원인은 무엇일까요?
   - S3 버킷 정책에 문제가 있음
   - 사용자에게 권한이 없음
   - <span style="color: red;">연결된 IAM 정책 내에 이 사용자를 부인하는 사항이 명시되어 있음</span>
   - AWS 지원 센터에 연락해 문제를 해결해 줄 것을 요청해야 함

IAM 정책 내의 명시적인 부인(DENY)은 S3 버킷 정책보다 우선적으로 고려됩니다.



8. S3 버킷으로부터 파일을 로딩해 오는 웹사이트가 있습니다. 파일의 URL을 Chrome 브라우저에 직접 입력했을 때에는 정상적으로 작동했으나, 이 웹사이트에서 파일을 로딩하려 할 때는 작동이 되지 않습니다. 무엇이 문제일까요?
   - 버킷 정책에 문제가 있음
   - IAM 정책에 문제가 있음
   - <span style="color: red;">CORS에 문제가 있음</span>
   - 암호화에 문제가 있음

교차 오리진 리소스 공유(CORS)는 한 도메인에서 로딩되는 클라이언트 웹 애플리케이션이 다른 도메인에 있는 리소스와 상호작용하는 방식을 정의합니다. <br>CORS에 대한 더 많은 정보는 다음 URL을 참조하세요: https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html



