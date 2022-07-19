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

title: "[aws] Classic Architecture (3) - Summary & Quiz"
excerpt: "🚀 Classic Architecture, quiz"

categories: aws
tag: [aws, architecture, quiz, summary]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Quiz



**1번**

다음 중 "무상태(stateless)" 애플리케이션 티어를 설계하는 데에 <u>도움이 되지 않는 것</u>은?

- 세션 데이터를 Amazon RDS 에 저장하기
- Amazon ElastiCache에 세션데이터 저장하기
- 클라이언트 HTTP 쿠키에 세션 데이터 저장하기
- <i style="color: red">EBS 볼륨에 세션 데이터 저장하기</i>



EBS 볼륨은 특정AZ 에만 저장되며, 한 번에 하나의 EC2 인스턴스에만 연결될 수 있다.



**2번**

관리 중인 Linux EC2 인스턴스 100s에 소프트웨어 업데이트를 설치하려 합니다. 이 업데이트를 EC2 인스턴스로 동적으로 로딩되어야 하며, 많은 양의 연산을 요구해서는 안 되는 공유 스토리지에 저장하고자 합니다. 어떤 방법을 사용해야 할까요?

- EBS에 소프트웨어 업데이트를 저장하고 각 AZ의 한 마스터로부터 데이터 복제 소프트웨어를 사용해 동기화하기
- <i style="color: red">EFS에 소프트웨어 업데이트를 저장하고, 스타트업 시 EFS를 네트워크 드라이브로 마운트하기</i>
- 소프트웨어 업데이트를 EBS 스냅샷으로 패키징하고 새로운 소프트웨어 업데이트 각각에 EBS 볼륨 설정하기
- Amazon RDS에 소프트웨어 업데이트 저장하기



EFS는 EC2 인스턴스의 100s에 동일한 파일 시스템을 마운트할 수 있게 해주는 네트워크 파일 시스템(NFS) 이다.<br>EFS에 소프트웨어 업데이트를 저장하면 각 EC2 인스턴스가 이들을 평가할 수 있게 됩니다.

즉 각각의 EC2 들이 EFS에 저장된 소프트웨어를 사용할 수 있게 된다.



**3번**

솔루션 아키텍트로서, 여러분은 복잡한 ERP 소프트웨어 스위트를 AWS Cloud로 이전하려 합니다. 오토 스케일링 그룹이 관리하는 한 세트의 Linux EC2 인스턴스에 소프트웨어를 호스팅할 계획입니다. 소프트웨어가 Linux 기기를 준비하는 데에는 보통 한 시간 이상이 걸립니다. 스케일 아웃이 발생할 경우, 설치 과정을 빠르게 만들기 위해서는 어떤 방법을 추천할 수 있을까요?

- <i style="color: red">Golden AMI 사용</i>
- EC2 사용자 데이터를 이용해 부트스트랩
- Amazon RDS에 애플리케이션 저장
- EFS로부터 애플리케이션 설치 파일 회수



Golden AMI는 설치되고 구성된 전체 소프트웨어를 포함한 이미지이기 때문에, 향후 이 AMI로부터 EC2 인스턴스를 빠르게 부팅할 수 있습니다.



**4번**

애플리케이션을 개발 중에 있으며, 최소 비용을 사용해 이 애플리케이션을 Elastic Beanstalk으로 배포하려 합니다. 이를 위해서는, 애플리케이션을 .................. 에서 실행해야 합니다.

- <i style="color: red">단일 인스턴스 모드</i>
- 고가용성 모드



문제에서 애플리케이션이 아직 개발 단계에 있으며 비용을 절감하고자 한다고 언급하고 있습니다. 단일 인스턴스 모드는 하나의 EC2 인스턴스와 하나의 탄력적 IP를 생성합니다.



**5번**

애플리케이션을 Elastic Beanstalk으로 배포하던 도중, 배포 프로세스가 극도로 느리다는 것을 알게 되었습니다. 로그를 검토한 결과, 종속성이 매 배포 당 각 EC2 인스턴스로 리졸브된다는 사실을 발견했습니다. 영향을 최소화하면서 배포 프로세스를 빠르게 하려면 어떻게 해야 할까요?

- 코드에서 일부 종속성을 제거
- 종속성을 Amazon EFS 에 두기
- <i style="color: red">종속성을 포함하는 Golden AMI를 생성해 그 이미지를 EC2 인스턴스 실행에 사용</i>



Golden AMI는 전체 소프트웨어, 종속성 및 구성을 포함하는 이미지이기 때문에, 향후 이 AMI로부터 EC2 인스턴스를 빠르게 부팅할 수 있습니다.