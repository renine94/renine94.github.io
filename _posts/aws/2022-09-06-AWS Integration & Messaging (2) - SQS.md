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

title: "[aws] Integration & Messaging (2) - SQS (Standard Queue)"
excerpt: "🚀 Simple Queue Service, Queue, Producer, Consumer, Polling, Decouple"

categories: aws
tag: [aws, sqs, queue, producer, consumer, polling, decouple]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Amazon SQS

> SQS의 핵심은 대기열

![image-20220906002121408](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906002121408.png)

- SQS 는 간단한 대기 서비스이다.
- SQS 대기열에는 메시지를 포함할 수 있다.
- 메시지를 담기 위해서는 누군가가 Queue대기열에 메시지를 전송해야 한다.
  - **생산자(producer)**
    - SQS대기열에 메시지를 보내는 주체
    - 생산자는 한 개 or 그 이상이 될 수 있다.
    - 여러 생산자가 여러 개의 메시지를 SQS 대기열에 보낼 수 있다.
    - 메시지는 무엇이든 상관없다.
      - 오더를 처리해라, 비디오를 처리해라.. 등등 etc...
    - 생성한 모든 메시지는 대기열에 들어간다.
  - **소비자(consumer)**
    - 대기열에서 메시지를 처리하고 수신해야 하는 대상
    - 대기열Queue에서 메시지를 폴링(polling) 한다.
      - 대기열에게 소비자 앞으로 온 메시지가 있는지를 물어보는 것
    - 대기열에 메시지가 있으면 소비자는 이 메시지를 폴링해서 정보를 얻는다.
    - 메시지를 처리하고 대기열에서 그 메시지를 삭제
    - 여러 소비자가 SQS대기열에서 메시지를 소비할 수 있도록 할 수도 있다.
- **Queue대기열 서비스는 생산자(Producer)와 소비자(Consumer) 사이를 분리하는 버퍼 역할을 한다.**





## 01. SQS - Standard Queue

- 표준 대기열용 Amazon SQS
- SQS는 AWS에서 제공하는 가장 오래된 서비스
- AWS의 첫 번째 서비스 중 하나였음 (10년 넘게 서비스중이어서 작동방식이 확실히 구축되어있음)
- 완전관리형 서비스이며, 애플리케이션을 분리하는 데 사용됨



- Standard SQS의 특별한 점
  - 무제한 처리량을 얻을 수 있다.
  - 초당 원하는만큼 메시지를 보낼 수 있다.
  - 대기열(Queue)에도 원하는 만큼 메시지를 포함시킬 수 있다.
  - **처리량에 제한이 없고, 대기열에 있는 메시지 수에도 제한이 없다.**
  - 메시지 수명이 짧다.
    - 메시지는 기본적으로 **4일동안 대기열에 남아있다**. (최대 시간 14일)
  - 메시지를 보내자마자 소비자가 읽고 해당 보존 기간 내에 처리한 후 대기열에서 삭제해야 한다.
    - 그렇지 않으면 소실된다.
  - 지연시간이 짧아서 SQS는 메시지를 보내거나, 메시지를 읽을 때마다 게시 및 수신이 **10ms이내**로 매우 빠르게 응답을 받게 된다.
  - SQS의 메시지는 작아야 한다.
    - 전송된 메시지당 256KB 미만이어야 한다.
  - SQS는 대기열 서비스이므로 높은 처리량, 높은 볼륨등이 있어서 중복 메시지가 있을 수 있다.
    - **메시지가 두번 전송되는 경우가 있다. (적어도 한번의 전송)**
  - 최선의 오더라는 뜻으로 품절 메시지를 보낼 수도 있다.



그 제한을 처리할 수 있는 SQS의 또다른 유형의 제품이 있지만 뒷부분에 설명하도록 한다.



## 02. SQS - Producing Messages

> 메시지 생산자

![image-20220906003708754](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906003708754.png)

- 최대 256KB의 메시지가 생산자에 의해 SQS로 전송 (using SDK, SendMessage API)
- 메시지가 작성되면 소비자가 해당 메시지를 읽고 삭제할 때까지 SQS대기열에 유지된다.
  - 메시지가 삭제되었다는 것은 메시지가 처리됐다라는 뜻
- **메시지 보존기간 4일~14일 (default, 4일)**



- 메시지 생성은 어떨때 하는가?
  - 패킷과 같은 오더를 처리한 다음 센터로 배송하려고 한다.
  - 원하는 시간에 이 작업을 수행하여 OrderId, ConsumerId 와 원하는 속성 등의 일부 정보가 포함된 메시지를 SQS대기열로 보낸다.
    - 주소, 휴대폰번호 등 원하는 속성도 들어갈 수 있다.
  - 애플리케이션 권한에 있는 소비자는 해당 메시지 자체를 처리해야 한다.



- **Standard SQS는 무제한의 처리량을 가지고 있다.**



## 03. SQS - Consuming Messages

> 메시지 소비자

![image-20220906004933768](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906004933768.png)

- 소비자는 일부 코드로 작성해야 하는 애플리케이션이다.

- 이러한 애플리케이션은 EC2, 즉 AWS상의 가상 서버에서 실행될 수 있다.

  - **EC2**, Server, **Lambda**. ,,, etc
  - 람다에서 메시지를 바로 읽을 수도 있다.

  

- Consumer가 있고, 소비자는 SQS메시지를 폴링한다.

- 소비자가 대기열에 자신의 앞으로 온 메시지가 있는지를 확인한다.

- 소비자는 한 번에 최대 10개의 메시지를 받는다.

- SQS대기열에 메시지가 있으면 "대기열에 유효한 메시지가 있다" 라는 응답을 받는다.

- 이 메시지를 처리하면 된다.

- 메시지 처리후에 SDK DeleteMessage API 를 통해 대기열에서 삭제한다.

  - 다른 소비자들이 이 메시지를 볼 수 없게 된다. (메시지 처리 완료)



## 04. SQS - Multiple EC2 Instances Consumers

> SQS대기열에 메시지가 많아져서, 처리량을 늘려야 하면 소비자(Consumer)를 추가하고 수평 확장을 수행해서 처리량을 개선할 수 있다.

![image-20220906005222573](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906005222573.png)

- **만약 메시지가 소비자에 의해 빠르게 처리되지 않으면 다른 소비자가 수신하게 될 가능성이 있다.**
  - 그렇기 때문에 적어도 한번은 전송이 된다 라고 표현함
  - 여러 소비자를 동시에 가질 수 있다. 



## 05. SQS - with Auto Scaling Group (ASG)

> ASG(Auto Scaling Groups)와 더불어 SQS를 사용하는 완벽한 사례이다.

![image-20220906005515233](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906005515233.png)

- 소비자가 ASG 내부에서 EC2 인스턴스를 실행
- SQS대기열에서 메시지를 폴링
- ASG 일종 지표에 따라 확장되어야 하는데, 사용할 수 있는 지표는 대기열의 길이 이다.
  - **ApproximateNumberOfMessages** 라고 한다.
  - 이는 모든 SQS대기열에서 쓸 수 있는 CloudWatch 지표이다
- 알람을 설정할 수도 있는데 대기열의 길이가 특정 수준을 넘어가면 CloudWatch Alarm 을 설정 가능



만약 웹사이트에 Order주문이 폭주했다거나 ASG이 더 많은 EC2 인스턴스를 제공하면 메시지들을 더 높은 처리량으로 처리할 수 있게 된다. 

- Queue에 메시지 쌓이면 Worker/ Consumer 같은거 늘려서 그냥 처리를 빠르게 하라는 뜻



## 06. SQS - decouple between Application tiers

> SQS는 애플리케이션 계층 간에 분리를 위해 사용된다.

![image-20220906005637125](../../assets/images/posts/2022-09-06-AWS Integration & Messaging (2) - SQS/image-20220906005637125.png)

- 비디오를 처리하는 App이 있다고 가정
- 프론트엔드에서 비디오처리를 요청을 받고 비디오가 처리되어야 할 때, 프론트엔드가 처리를 한 후 S3 버킷에 업로드
  - 문제는 시간이 매우 오래 걸릴 수 있고, 프론트엔드에서 이를 처리하면 웹사이트의 속도가 느려질 수 있다.
- 애플리케이션을 분리하여, 파일처리요청과 실제파일처리가 서로 다른 애플리케이션에서 발생할 수 있도록 하자



파일처리 요청을 받을 때마다 SQS대기열로 메시지를 전송한다. 그럼 처리 요청을 할 때 해당 파일은 SQS대기열에 있게 되며, 자체 ASG에 속할 Backend App이라는 두번쨰 처리 계층을 생성할 수 있고, 이 백엔드에서 메시지를 수신하고 비디오를 처리하고 S3버킷에 이를 업로드할 것이다.

위 이미지에서 볼 수 있듯이 그에 따라 프론트엔드를 확장할 수 있고 그에 따라 백엔드도 확장할 수 있지만 독립적으로 확장할 수 있게 된다. SQS대기열은 처리량이 무제한이고 대기열 측면에서 메시지 수에 제한이 없기 때문에 정말 안전하다.

이는 강력하고 확장 가능한 유형의 아키텍처이다. 또한 프론트엔드의 경우 최적의 유형의 EC2 인스턴스 또는 아키텍처를 프론트엔드에 사용할 수 있으며, 백엔드의 경우 비디오 처리를 수행할 때 그래픽 처리장치 GPU가 있는 일부 EC2 인스턴스를 사용할 수 있게 된다.

이러한 유형의 인스턴스가 해당 워크로드를 수행하는 데에 최적이기 때문이다.



## 07. SQS - Security

- 보안
  - https api 를 사용하여 메시지를 보내고 생성함으로써 전송중에 암호화
  - KMS키를 사용하여 미사용 암호화를 얻고
  - 원한다면 클라이언트 측 암호화를 할 수도 있다.



클라이언트가 자체적으로 암호화 및 암호화 해독을 수행해야 함을 의미한다. SQS에서 기본적으로 지원하는 것은 아니다.  액세스 제어를 위해 IAM 정책은 SQS API 에 대한 액세스를 규제할 수 있고, S3버킷 정책과 유사한 SQS액세스 정책도 있다.

SQS대기열에 대한 교차계정 액세스를 수행하려는 경우나 곧 배울 SNS 혹은 S3 같은 다른 서비스가 SQS대기열에 S3이벤트 같은 것을 쓸 수 있도록 허용하려는 경우에 매우 유용하다.