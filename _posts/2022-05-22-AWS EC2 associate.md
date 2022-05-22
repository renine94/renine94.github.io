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

title: "[aws] EC2 Associate"
excerpt: "🚀 IP, Placement Groups, ENI 알아보기!"

categories: aws
tag: [aws, ec2, ip, cloud]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# 01. EC2 Assoicate

EC2 와 함께 쓰이는 AWS Service 들에 대해 알아보자
{: .notice--danger}

- IP
- placement groups
- ENI (Elastic Network Interfaces)



## 🚀 IP

> IP 주소에 대해 알아보자!

- IPv4
  - 1.160.10.240
    - [0-255].[0-255].[0-255].[0-255]
  - 가장 흔하게 온라인에서 사용되어 지고 있다.
  - 37억개의 서로 다른 주소를 허용한다.
  - 현재 IoT 의 등장으로 IP 주소가 거의 고갈되어 가고 있다.
    - IPv6 출현으로 해결중
  - 공용IP 는 전체 웹에서 유일해야 한다.
- IPv6
  - 1900:4545:3:200:f8ff:fe21:67cf
  - IoT 에 대한 문제를 해결해준다.

![image-20220522220104821](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522220104821.png)

- Public
  - 모든곳에서 접속 가능하다.
- Private
  - 사설IP로는 사설 네트워크 내에서만 액세스할 수 있다.
  - 사설 네트워크에서는 유니크하다.
  - 서로 다른 사설 네트워크망에서는 같은 아이피 주소를 가질 수 있다.
  - 지정된 범위의 IP만 사설IP로 사용될 수 있다.



**Elastic IPs**

- 우리가 EC2 인스턴스를 켜고 끌때, public IP 가 변경된다.

- 하지만 너가 고정된 IP 주소를 얻고싶다면, `Elastic IPs` 를 사용하면 된다.

- 너가 삭제하기 전까진 Elastic IP는 IPv4 public 상태이다.

- 한 번에 하나의 인스턴스에만 붙일 수 있다.

- AWS 계정 당 5개의 탄력적IP를 사용할 수 있다.

- 탄력적IP주소를 가지고 있는데, 사용하지 않으면 요금이 부과된다.

- 결론적으로는 탄력적 IP는 사용하지 않는 것이 좋다.

  - 이것은 좋지않은 구조적 결정으로 종종 언급된다.
  - **대신에, 임의의 공용 IP를 써서 DNS 이름을 할당하는 것이 좋다.** (Route53)
  - **로드 밸런서를 사용해서 공용IP를 전혀 사용하지 않을 수도 있다.** <span style="color: red;">(Recommanded)</span>

  

### 실습

> AWS 에서 직접 네트워크 실습을 진행해보자!

- 기본값으로 EC2 기기는 내부 AWS 네트워크엔 사설 IP를 사용
- WWW 에는 public IP 를 사용한다.
- EC2 기기에 SSH 를 사용할 때
  - private IP 를 사용할 수 없다.
  - 같은 네트워크안에 있지 않기 때문이다. (VPN 을 쓰지 않는 이상)
  - 공용 IP만 사용가능하다.
- EC2 를 멈췄다가 다시 시작하면 public IP 가 바뀔 수도 있다.

![image-20220522222003304](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522222003304.png)

![image-20220522222421759](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522222421759.png)

public IP 주소를 이용하여 SSH로 연결할 수 있습니다. (사진상 public ip : `54.180.92.252`)<br>private ip 주소로는 접근 할 수 없습니다. (사설 네트워크에 속하기 때문에)
{: .notice--warning}

- public IP를 사용하면 공용 네트워크에서 AWS에 액세스 할 수 있다.
- EC2 를 중지하고 다시 시작하면 public ip 주소가 변경된다.
- 탄력적 IP를 EC2 에 연결시키면 EC2 는 고정된 public IP 주소를 갖게 된다.
  - 사용하지 않으면 EC2 에서 Elastic IP 를 해제한뒤
  - release Elastic IP 를 하여 사용하지 않는 탄력적IP 주소를 완전히 제거해준다.
  - 안하면 요금이 부과되니 주의할 것



## 🚀 Placement Groups

> 배치그룹에 대해 알아보자!

- EC2 인스턴스가 AWS 인프라에 배치되는 방식을 제어하고자 할 때 사용
- 전략들은 배치그룹을 사용함으로써 정의할 수 있다.
- 배치 그룹을 만들 때 3가지 전략을 사용할 수 있다.
  - `클러스터`
    -  단일 가용 영역내에서 지연 시간이 짧은 하드웨어 설정, 인스턴스를 그룹화할 클러스터 배치 그룹
    - 높은 성능을 제공하지만 위험 또한 높다.
  - `스프레드` 
    - 분산배치그룹은 인스턴스가 다른 하드웨어에 분산된다는 의미
    - 가용영역당 최대 7개의 EC2 인스턴스만 가질 수 있다.
    - 따라서, 크리티컬한 애플리케이션이 있는 경우 분산 배치 그룹을 사용한다.
  - 파티션
    - 정말 유용한 새로운 유형의 배치그룹
    - 분할 배치 그룹 이라고 부른다.
    - 분산배치그룹(스프레드)과 비슷하게 인스턴스를 분산하려는 것이다.
    - 이건, 여러 파티션에 인스턴스가 분할되어 있다.
    - 이 파티션은 가용 영역 내의 다양한 하드웨어 랙 세트에 의존한다.
    - 인스턴스가 분산되어 있지만, 다른 실패로부터 격리되지 않았다는 것이다.
    - 그룹당 수백 개의 EC2 인스턴스를 통해 확장할 수 있고, 이를 통해 `Hadoop`, `Cassandra`, `Kafka` 와 같은 애플리케이션을 실행 할 수 있다.



### Cluster

![image-20220522225753101](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522225753101.png)

- 클러스터 배치 그룹의 경우 이는 모든 EC2 인스턴스가 동일한 랙, 동일한 가용영역에 있다
- 이러한 인스턴스는 동일한 하드웨어에 있다.
- 낮은 지연시간을 가지고있고, 높은 네트워크 성능을 자랑한다.
- 하지만, 하드웨어가 고장나면, 모든 인스턴스가 동시에 고장나는 단점이 있다.
- 사용 예시
  - 높은 네트워크 성능이 필요하고, 매우 빨리 완료되어야 할 작 (빅데이터)
  - 극히 짧은 지연시간과 높은 네트워크 처리량을 필요로 하는 곳

### Spread

![image-20220522225815754](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522225815754.png)

- Cluster 배치그룹과는 정반대의 성격을 가지고 있다.
- 분산 배치그룹에서는 실패 위험을 최소화 하려고 한다.
- 모든 EC2 인스턴스가 다른 하드웨어 영역을 가지고 있다.
- 여러 가용 영역에 걸쳐있을 수 있으며, 동시 실패 위험이 감소한다.
- 단점은 하나의 가용영역(AZ)당 7개의 EC2 인스턴스로 제한된다.

### Partition

![image-20220522230039353](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522230039353.png)

- 여러 가용영역의 파티션에 인스턴스를 분산할 수 있다.
- 가용영역당 7개의 파티션을 가질 수 있다.
- 각 파티션은 AWS의 랙(Rack) 을 나타낸다.
- 파티션이 많으면 인스턴스가 여러 하드웨어 랙에 분산되어 서로 랙 실패로부터 안전하다.
- 이러한 파티션은 동일 리전의 여러 가용영역에 걸쳐 있을 수 있다.
- 각 파티션에는 수백개의 EC2 인스턴스를 배치할 수 있다.
- 각각의 파티션은 하드웨어 고장으로부터 독립적이다. (안전하다)
  - partition2 가 고장나도 partition1 에는 영향이없다.
- 사용 사례
  - HDFS, HBase, Cassandra, Kafka

### 실습

![image-20220522231042045](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522231042045.png)

![image-20220522231249680](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522231249680.png)



## 🚀 Elastic Network Interfaces (ENI)

> 탄력적 네트워크 인터페이스

![image-20220522232119536](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522232119536.png)

- VPC 의 논리적 구성 요소이며 가상 네트워크 카드를 나타낸다.
- ENI 는 EC2 인스턴스가 네트워크에 액세스 할 수 있게 해준다.
- 각 ENI 는 VPC의 특정 서브넷 내에 있으며 (따라서 특정 가용영역 내에 있음)
- 각 ENI 는 다음과 같은 속성을 가진다.
  - 주요 Private IPv4 와 하나 이상의 보조 IPv4 를 가질 수 있다.
  - 각 ENI 는 private IPv4 당 탄력적 IPv4 를 갖거나 혹은 하나의 public IPv4 를 가질수있다.
  - ENI 에 하나 이상의 보안 그룹을 연결할 수 있다.
  - Mac address
  - private IPv4
  - 보안 그룹
- EC2 인스턴스와 독립적으로 ENI를 생성하고 즉시 연결하거나, 장애 조치를 위해 EC2 인스턴스에서 이동시킬 수 있다.
  - 한 인스턴스에서 다른 인스턴스로 IPv4 를 연결할 수 있게 된다.
- 특정 가용 영역 즉 AZ에 바인딩된다.
- EC2 인스턴스 생성시 자동으로 ENI 가 생성된다.
  - 인스턴스를 종료시키면 자동으로 생성된 ENI 는 삭제된다.
  - **수동으로 만든 ENI 는 삭제되지 않고 남아 있다.**

### 실습

![image-20220522232832810](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522232832810.png)

![image-20220522235406110](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522235406110.png)

![image-20220522235711572](/assets/images/posts/2022-05-22-AWS EC2 associate/image-20220522235711572.png)
