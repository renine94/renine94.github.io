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

title: "[aws] Global Accelerator (2) - Quiz"
excerpt: "🚀 CloudFront, Global Accelerator Quiz 6문제"

categories: aws
tag: [aws, cloudfront, globalAccelerator, quiz]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Quiz



1. S3 버킷에 유료 콘텐츠가 저장되어 있습니다. 이 콘텐츠를 전역적으로 분배하기 위해 CloudFront 배포를 설정하고 S3 버킷이 CloudFront 배포에서만 데이터를 교환하도록 구성했습니다. 다음 CloudFront 기능 중 유료 콘텐츠를 안전하게 분배하기 위해서는 무엇을 사용해야 할까요?
   - 원본 액세스 ID
   - S3 미리 서명된 URL
   - <span style="color: red;">CloudFront 서명된 URL</span>
   - CloudFront 무효화

<br>

CloudFront 서명된 URL은 일반적으로 동적으로 생성된 URL을 통해 유료 콘텐츠를 배포하는 데 사용됩니다.

<br><br>



2. Application Load Balancer가 관리하는 EC2 인스턴스 플릿에 호스팅된 웹사이트를 제공하는 CloudFront 배포가 있습니다. 모든 클라이언트가 미국에 있는데도 불구하고, 타 국가로부터 일부 악성 요청이 들어오고 있다는 점을 발견했습니다. 오직 미국으로부터의 사용자들만을 허가하고, 다른 국가는 차단하려면 어떻게 해야 할까요?
   - <span style="color: red;">CloudFront 지리적 제한 사용하기</span>
   - 원본 액세스 ID 사용하기
   - 보안 그룹을 설정한 뒤 이를 CloudFront 배포에 연결하기
   - Route53 지연 시간을 이용해 이를 CloudFront 분배로 연결하기

<br><br>

3. S3 버킷 상에 호스팅된 정적 웹사이트가 있습니다. 요청을 더 잘 처리하고 성능을 향상시키기 위해 S3 버킷을 가리키는 CloudFront 배포를 생성했습니다. 얼마 후, 여러분은 아직도 사용자들이 S3 버킷에서 웹사이트로 직접 액세스할 수 있다는 것을 알게 되었습니다. 여러분은 사용자들이 CloudFront만을 통해서 웹사이트로 액세스하게끔 하려 합니다. 이를 위해서는 어떻게 해야 할까요?
   - 클라이언트들에게 이메일을 보내 S3 엔드 포인트를 사용하지 말 것을 요청
   - <span style="color: red;">CloudFront 배포를 구성해 원본 액세스 ID를 생성한 후, 오직 CloudFront 배포 OAI 사용자들이 보내는 요청만을 수락하도록 업데이트</span>
   - 클라이언트가 CloudFront로 리다이렉팅되도록 S3 액세스 포인트 사용



<br><br>

4. Application Load Balancer가 관리하는 한 세트의 EC2 인스턴스에 웹사이트가 호스팅되어 있습니다. 여러분은 CloudFront 배포를 생성해 그 오리진이 ALB를 가리키도록 설정했습니다. CloudFront 배포를 통해 제공되는 수백 개의 사설 파일에 대한 액세스를 제공하려면 무엇을 사용해야 할까요?
   - CloudFront 서명된 URL
   - CloudFront 원본 액세스 ID
   - <span style="color: red;">CloudFront 서명된 쿠키</span>
   - CloudFront HTTPS 암호화

<br>

서명된 쿠키는 다수의 파일에 액세스하는 데에 유용하고, 서명된 URL은 개별 파일에 액세스하는 데에 유용

<br><br>

5. HTTP REST API를 노출시킬 애플리케이션을 생성하고 있습니다. 요청 라우팅 규칙을 HTTL 레벨에서 제공해야 할 필요가 있습니다. 보안 요구 사항 때문에, 애플리케이션은 두 개의 정적 IP 주소를 통해서만 노출될 수 있습니다. 이러한 요구 사항을 충족시키기 위한 솔루션을 생성하려면 어떻게 해야 할까요?
   - NLB 를 사용하고 탄력적IP 를 여기에 연결
   - <span style="color: red;">AWS Global Accelerator 와 ALB 사용</span>
   - ALB 사용하고 탄력적 IP를 여기에 연결
   - CloudFront 를 탄력적IP와 ALB와 함께 사용



<br>

AWS Global Accelerator는 두 개의 정적 IP 주소를 제공하며, ALB는 HTTP 라우팅 규칙을 제공합니다.

<br><br>

6. 이 S3 버킷 정책이 하는 역할이 무엇일까요?

```json
{
    "Version": "2012-10-17",
    "Id": "Mystery policy",
    "Statement": [{
         "Sid": "What could it be?",
         "Effect": "Allow",
         "Principal": {
             "CanonicalUser": "CloudFront Origin Identity Canonical User ID"
         },
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::examplebucket/*"
    }]
}
```

- CloudFront 에서 GetObject 요청이 있을 경우, 이를 암호화하도록 강제
- <span style="color: red;">CloudFront 배포 원본 액세스ID 에서 오는 S3버킷 콘텐츠만이 평가될수 있도록 허가</span>
- S3 버킷에 대한 GetObject 유형의 요청만을 허가



