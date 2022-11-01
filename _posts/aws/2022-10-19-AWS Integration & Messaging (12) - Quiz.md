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

title: "[aws] Integration & Messaging (12) - Quiz"
excerpt: "🚀 Integration & Messaging Quiz - 문제풀이 및 해석"

categories: aws
tag: [aws, quiz, integration, messaging]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"







---

# Quiz



1.일년 중 최대 세일 기간인 블랙 프라이데이를 준비하고 있는 전자 상거래 웹사이트가 있습니다. 트래픽은 100배가 증가할 것으로 예상됩니다. 이 웹사이트는 이미 SQS 표준 대기열을 사용하고 있습니다. SQS 대기열은 어떻게 준비해야 할까요?

- AWS 지원 센터에 연락해 SQS 표준 대기열을 준비해줄 것을 요청
- SQS 대기열에 오토 스케일링 활성화
- SQS 대기열 용량 늘리기
- <span style="color: red;">SQS이 자동으로 스케일링해줄 것이므로 아무 조치도 취하지 않음</span>



<br>

2. SQS 메시지가 SQS 대기열에 게시된 지 5분이 지난 후에만 소비자들에 의해 처리되도록 하기 위해서는 어떻게 해야할까요?

- <span style="color: red;">`DelaySeconds` 파라미터 늘리기</span>
- 가시성 시간초과 변경
- 롱 풀링 활성화
- Amazon SQS Extended Client 사용

> SQS 대기열 지연은 Amazon SQS가 소비자들에게 새로운 SQS 메시지가 보이지 않도록 유지하는 기간입니다. SQS대기열 지연은 대기열로 처음 추가된 메시지를 감춤 처리합니다. (기본 0분, 최대 15분)

<br>

3. 소비자들이 한 번에 10개의 메시지를 폴링하고 1분 내로 이에대한 처리를 완료하는 SQS대기열이 있습니다. 잠시 후, 여러분은 동일한 SQS메시지를 다른 소비자들도 수신하여 메시지가 한 번이상 처리되었음을 알게되었습니다. 이 문제를 해결하기 위해서는 어떻게 해야 할까요?

- 롱 풀링 활성화
- 메시지 생성 시 메시지에 `DelaySeconds` 파라미터 추가
- <span style="color: red;">가시성 시간 초과 늘리기</span>
- 가시성 시간 초과 줄이기

> SQS 가시성 시간초과는 Amazon SQS가 다른 소비자들의 메시지 재수신 및 재처리를 막는기간입니다.
>
> 가시성 시간초과는 대기열에서 소모된 메시지만을 감춤 처리합니다. 
>
> 가시성 시간초과를 증가시키면, 소비자들이 더 오랜 시간 동안 메시지를 처리할 수 있게 해주며, 메시지의 중복 읽기를 방지합니다. (기본: 30초, 최소:0초, 최대 12시간)

<br>

4. SQS 표준대기열에서 메시지를 처리하던, 오토 스케일링 그룹의 관리 하에 있는 EC2 인스턴스 플릿(소비자)이 있습니다. 최근 많은 메시지들이 두 번 처리되었다는 점을 발견해 조사를 해본 결과, 이 메시지들을 성공적으로 처리할 수 없음을 알게 되었습니다. 이러한 메시지 실패의 원인은 어떻게 해결(디버깅)해야 할까요?

- SQS 표준대기열
- <span style="color: red;">SQS 데드 레터 대기열 (DLQ)</span>
- SQS 대기열 지연
- SQS FIFO 대기열

> Dead Letter Queue 는 다른 SQS대기열(소스 대기열)들이 처리(소비)될 수 없는 메시지를 보낼 수 있는 곳입니다.
>
> 이를 통해 문제가 되는 메시지들을 분리하여 처리가 실패한 이유를 디버깅할 수 있으므로, 디버깅에 유용합니다.

<br>

5. 다음 중 어떤 SQS대기열 유형을 사용해야 메시지가 순차적으로, 단 한번만 처리될까요?

- SQS 표준대기열
- SQS 데드 레터 대기열 (DLQ)
- SQS 대기열 지연
- <span style="color: red;">SQS FIFO 대기열</span>

> SQS FIFO(First-In-First-Out) 대기열은 SQS 표준 대기열의 모든 기능을 가지고 있으며, 다음과 같은 두 기능이 추가됩니다. 첫 번째, 어떤 메시지를 보내고 수신했는지에 대한 오더가 엄격하게 보존됩니다. 메시지는 한 번만 전송되며, 소비자가 해당 메시지를 처리하고 삭제할 때까지 사용할 수 있습니다. 두 번째, 복제된 메시지는 대기열에 들어오지 않습니다.

<br>

6. 3개의 서로 다른 애플리케이션으로 동일한 메시지를 보내려 합니다. 3개의 애플리케이션 모두 SQS를 사용하고 있습니다. 이를 위해 어떤 접근법을 선택하는 것이 가장 적절할까요?

- SQS 복제 기능을 사용
- <span style="color: red;">SNS + SQS 팬아웃 패턴을 사용</span>
- 3개의 SQS 대기열에 개별적으로 메시지 전송하기

> 흔히 사용되는 패턴으로, 단 하나의 메시지를 SNS 주제로 전송한 뒤, 다수의 SQS 대기열로 ‘팬 아웃’합니다. 이 방식에는 다음의 기능이 포함되어 있습니다: 완전히 분리되어 있고, 데이터 손실이 없으며, 향후 더 많은 SQS 대기열(더 많은 애플리케이션)을 추가할 수 있습니다.

<br>

7. 한 Kinesis Data Stream에 6개의 샤드가 프로비저닝되어 있습니다. 이 데이터 스트림은 보통 5MB/s 의 속도로 데이터를 수신하며, 8MB/s의 속도로 데이터를 전송합니다. 이따금 트래픽이 2배까지 증가하여 `ProvisionedThroughputExceededException` 예외처리가 발생합니다. 이 문제를 해결하려면 어떻게 해야 할까요?

- <span style="color: red;">더 많은 샤드 추가</span>
- Kinesis 복제 활성화
- SQS를 Kinesis 버퍼로 활용

> Knesis Data Stream의 용량 제한은 데이터 스트림 내에 있는 샤드의 수에 의해 결정됩니다. 이러한 제한은 데이터 처리량, 혹은 읽기 데이터 호출에 의해 초과될 수 있습니다. 각 샤드는 1MB/초 만큼의 들어오는 데이터와 2MB/초 만큼의 나가는 데이터를 허용합니다. 충분한 용량을 제공하려면 데이터 스트림의 샤드 수를 증가시켜야 합니다.

<br>

8. 한 웹사이트 내에서 사용자들이 클릭하는 순서, 사용자들이 보내는 시간 및 탐색이 어디에서 시작되고 어떻게 종료되는지 등의 클릭스트림 데이터를 분석하고자 합니다. Amazon Kinesis 를 사용하기로 했고, 웹사이트가 이러한 클릭스트림 데이터를 Kinesis Data Stream으로 전송하도록 구성한 상태입니다. Kinesis Data Stream으로 전송된 데이터를 확인하던 중, 데이터가 순서대로 정렬되어 있지 않으며, 한 개별 사용자로부터 온 데이터가 여러 샤드에 분산되어 있다는 것을 알게되었습니다. 이 경우, 어떻게 문제를 해결해야 할까요?

- 샤드가 너무 많으므로 오직 1개의 샤드만을 사용해야 함
- 다수의 소비자를 사용해서는 안되므로, 오직 하나만을 사용하면 데이터가 재정렬될 것
- <span style="color: red;">Kinesis로 보내지는 각 레코드에 사용자의 신원을 나타내는 파티션 키를 추가해야 함</span>

> Kinesis Data Stream은 각 데이터 레코드에 연결된 파티션 키를 사용해 주어진 데이터 레코드가 어느 샤드에 속하는지 판단합니다. 각 사용자의 신원을 파티션 키로 사용할 경우, 각 유저에 대한 데이터가 정렬되어 동일한 샤드로 보낼 수 있습니다.

<br>

9. 데이터 스트림에 대한 실시간 분석을 수행하려는 경우, 다음 AWS 서비스중 어느것이 가장 적절할까요?

- Amazon SQS
- Amazon SNS
- Amazon Kinesis Data Analytics
- <span style="color: red;">Amazon Kinesis Data Firehose</span>

> Kinesis Data Analytics를 사용하려면 Kinesis Data Streams를 기반 데이터 소스로 사용해야 합니다.

<br>

10. 대량의 실시간 데이터를 생성하는 애플리케이션을 실행 중이며, 이 데이터를 S3와 RedShift로 로딩하려 합니다. 또한 이 데이터들은 목적지에 도달하기 전에 변환되어야 합니다. 이를 위해, 선택할 수 있는 가장 적절한 아키텍처는 무엇인가요?

- SQS + AWS Lambda
- SNS + HTTP Endpoint
- <span style="color: red;">Kinesis Data Streams + Kinesis Data Firehose</span>

> 이는 실시간 데이터를 S3와 Redshift로 로딩하기 위한 완벽한 기법 조합입니다. Kinesis 데이터 파이어호스는 AWS Lambda를 사용하는 커스텀 데이터 변환을 지원합니다.

<br>

11. 다음 중 AWS SNS를 지원하지 "않는" 구독자를 고르세요.

- <span style="color: red;">Amazon Kinesis Data Streams</span>
- Amazon SQS
- HTTP(S) Endpoint
- AWS Lambda

> 현재 Kinesis Data Firehose 는 지원하지만, Kinesis Data Stream은 지원되지 않습니다.

<br>

12. 다음 중 사용자들에게 이메일 알림을 보내려 할 때 도움이 되는 AWS 서비스는 무엇인가요?

- AWS Lambda를 갖는 Amazon SQS
- <span style="color: red;">Amazon SNS</span>
- Amazon Kinesis

<br>

13. 여러 마이크로 서비스 애플리케이션을 온프레미스로 실행중이며, 이들은 MQTT 프로토콜을 지원하는 메시지 브로커를 사용해 통신하고 있습니다. 애플리케이션을 새로 엔지니어링하거나 코드를 수정하는 작업 없이, 이 애플리케이션들을 AWS로 이전시키려 합니다. MQTT 프로토콜을 지원하는 관리 메시지 브로커를 활용하기 위해서는 다음 중 어떤 AWS 서비스를 사용해야 할까요?

- Amazon SQS
- Amazon SNS
- Amazon Kinesis
- <span style="color: red;">Amazon MQ</span>

> Amazon MQ는 JMS, NMS와 같은 업계 표준 API를 지원하며 AMQP, STOMP, MQTT 및 WebSocket 등을 비롯한 메시징 프로토콜을 지원합니다.



