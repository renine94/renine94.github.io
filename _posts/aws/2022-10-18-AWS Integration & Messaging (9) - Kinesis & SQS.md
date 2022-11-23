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

title: "[aws] Integration & Messaging (9) - Kinesis & SQS"
excerpt: "🚀 Kinesis, SQS, 차이 비교, 파티션키, SQS FIFO 그룹ID"

categories: aws
tag: [aws, kinesis, sqs, fifo, partition]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# Ordering Data into Kinesis

> Kinesis와 SQS FIFO에서 데이터가 어떻게 정렬되는지 알아보자
>
> 기술이 서로 비슷해보이고, 기능도 비슷한 편이지만, 실제로는 아주 다르다.

![image-20221018005646267](../../assets/images/posts/2022-10-18-AWS Integration & Messaging (9) - Kinesis & SQS//image-20221018005646267.png)

- 도로에 트럭이 100대가 있고, 각각 트럭ID가 있다고 가정한다.
- 트럭1, 트럭2, ... 트럭100 까지 도로에 있으며 GPS위치를 주기적으로 AWS에 보낸다.
- 각 트럭의 순서대로 데이터를 소비해서 트럭의 이동을 정확하게 추적하고 그 경로를 순서대로 확인하려고 한다.
- 어떻게 Kinesis로 전달할 수 있을까?
- **파티션 키**를 사용하면 된다. (파티션 키 값은 트럭ID)
- 트럭1은 트럭1의 파티션키 전송
- 트럭2는 트럭2의 파티션키 전송
- **같은 파티션 키를 지정하면 해당 키가 언제나 동일한 샤드로 전달된다.** (Kafka와 비슷...???)



- Kinesis 데이터 스트림과 샤드 세 개가 1, 2, 3번 있다.
- 간단하게 트럭 100대 대신 5대로 가정한다.
- 총 5대의 트럭이 도로에 있고 Kinesis에 데이터를 전송한다.
- 트럭 ID로 파티션 키를 사용한다.
- **트럭 1이 GPS데이터를 보낼 때 Kinesis로 트럭 1의 파티션키를 보내게 되며, 이 때 Kinesis는 트럭 1의 파티션 키를 해시한다. 다시 말해 계산한다.**
- 트럭 1의 데이터가 샤드 1번으로 가게 된다. 따라서 데이터는 샤드 1번으로 이동한다.
- **트럭 2도 데이터를 전송한다. 트럭 2번의 파티션 키를 전송한다. Kinesis는 해당 파티션 키를 확인하고 해시한 후 해당 값이 샤드 2번에 들어가도록 한다.**
- 트럭 3도 마찬가지고, 트럭 3의 파티션 키를 전송하는데 Kinesis 데이터 스트림이 이번엔 트럭 3의 키가 샤드 1번으로 이동해야 한다고 결정한다.
  - 샤드 3번으로 갈 필요 없이 이 파티션 키는 샤드 1로 이동하면 된다고 한다.
- 트럭 4는 샤드 3번으로 이동, 
- 트럭 5는 샤드 2번으로 이동,
- 이렇게 재분할하는 것을 파티션이라고 하기에 파티션 키라고 부른다.
- **각 트럭의 파티션 키는 거기에 따른 샤드에 속한다.**
- 트럭 1은 계속 트럭1이라는 동일한 파티션 키를 전송하므로 데이터가 언제나 같은 샤드로 이동한다.
- 그러므로 트럭 1의 다음 데이터 지점은 샤드 1로가고, 트럭3의 다음 데이터 지점도 샤드 1번으로 계속 이동한다.



- 그러므로 트럭 100대와 샤드 5개가 있다고 하면 각 샤드는 평균적으로 20대의 트럭을 가지게 될 것이다.
- 하지만 트럭과 각각의 샤드 사이가 직접적으로 연결된 것은 아니다.
- **Kinesis가 파티션 키를 해시해서 어느 샤드로 보낼지 결정한다.**
- 다시말해, 안정된 파티션 키를 얻으면 바로 트럭이 그 데이터를 같은 샤드로 전달하고, 그러면 샤드 레벨에서 각 트럭의 순서에 따른 데이터를 얻을 수 있게 됩니다.



# Ordering data into SQS

> SQS 표준방식에는 순서가 없습니다.
>
> 그래서 SQS FIFO 라는 선입선출 방식이 있습니다.

![image-20221018010448055](../../assets/images/posts/2022-10-18-AWS Integration & Messaging (9) - Kinesis & SQS//image-20221018010448055.png)

- 이 SQS FIFIO의 그룹 ID를 사용하지 않으면 모든 메시지가 소비되는 방식은 보내진 순서에 따르며 소비자는 하나만 존재한다.
- 위의 그림을 보면 옵션이 다양한데, SQS FIFO 대기열에 전송되는 중이다.
- 그러면 **전송되는 순서대로 소비자가 수신받을 것**이다. 보다시피 소비자는 하나이기 때문에 두 배치의 메시지를 소비한
- 따라서 선입선출 방식으로는 판단하기가 쉽다. 소비자도 하나만 가질수 있다.
- 트럭이 있다면, 모든 트럭이 FIFO 대기열로 데이터를 보내더라도 소비자는 하나뿐이다.



- **만약 소비자 숫자를 스케일링하고 서로 연관된 메시지를 그룹화하려는 경우 그룹ID를 사용할 수 있다.**
- Kinesis 의 파티션키와 개념이 비슷하다.
- 그룹 ID를 사용하면 FIFO 대기열은 FIFO 내부에 두 개 그룹이 생기고, 정의한 그룹마다 각각 소비자는 가질 수 있게된다.
- 그룹ID가 많아질수록 소비자도 많아진다.



# Kinesis vs SQS ordering

> Kinesis와 SQS의 차이점에 대해 알아보자

- 트럭 100대가 있고, Kinesis 샤드가 5개, SQS FIFO 대기열이 1개라면,
- **Kinesis Data Streams**
  - Kinesis 데이터 스트림에서 평균적으로 가지는 값은 샤드당 트럭 20대가 될것이다.
  - 해시 기능 덕분에 각 트럭은 하나의 샤드에 지정되고 해당 샤드에 계속 머물것이다.
  - 그리고 트럭 데이터는 각 샤드에 순서대로 정렬된다.
  - 하지만 동시에 가질 수 있는 최대 소비자 개수는 5개뿐이다.
  - **샤드가 5개이고, 샤드마다 하나의 소비자가 필요하기 때문이다.**
  - Kinesis 데이터 스트림은 샤드가 5개인 경우에 초당 최대 5MB의 데이터를 수신가능하며, 처리량이 꽤많은편
- **SQS FIFO**
  - SQS FIFO 대기열은 하나뿐이다.
  - 샤드 및 파티션을 정의할 필요없이 FIFO 대기열이 하나만 있다.
  - 트럭이 100대 있으므로 각 트럭 ID에 상응하는 그룹 ID를 100개 생성한다.
  - **즉 그룹ID가 100개가 되고, 소비자도 최대 100개가 될 수 있다.**
  - 각 소비자가 특정 그룹ID와 연결되기 때문이다.
  - 규모를 보면 SQS FIFO에서 최대 초당 300, 혹은 배치를 사용하면 3,000개의 메시지를 가진다.



이렇듯 서로 다른 소비, 생산 그리고 정렬모델에서 기억해야할것은 이것이다.

- 경우에 따라 적절한 모델은 달라지며, **SQS FIFO는 그룹ID 숫자에 따른 동적 소비자 수를 원할때 좋다.**
- **Kinesis 데이터 스트림을 사용할 경우는 예를 들어 트럭 10,000대가 많은 데이터를 전송하고 또 Kinesis Data Streams에 샤드당 데이터를 정렬할 때**입니다.


