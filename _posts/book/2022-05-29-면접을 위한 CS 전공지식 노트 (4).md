---
layout: single

header:
  teaser: /assets/images/logo/book.jpg
  overlay_image: /assets/images/logo/book.jpg
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "면접을 위한 CS 전공지식 노트 (4) - TCP/IP 4계층 모델"
excerpt: "🚀 네트워크 기초, TCP/IP 4계층모델, 네트워크 기기, IP주소, HTTP"

categories: book
tag: [cs, network, tcp, ip]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# TCP/IP 4계층 모델

인터넷 프로토콜 스위트는 인터넷에서 컴퓨터들이 서로 정보를 주고 받는 데 쓰이는 프로토콜의 집합이며,<br>이를 TCP/IP 4계층 모델로 설명하거나 OSI 7계층 모델로 설명하기도 합니다.<br>이 책에서는 TCP/IP (Transmission Control Protocol/Internet Protocol) 4계층 중심으로 설명한다.<br>이 계층 모델은 네트워크에서 사용되는 통신 프로토콜의 집합으로 계층들은 프로토콜의<br>네트워킹 범위에 따라 네 개의 추상화 계층으로 구성됩니다.
{: .notice--success}



## 🚀 계층 구조

> TCP/IP 계층은 네 개의 계층을 가지고 있으며, OSI 7계층과 많이 비교합니다.

- TCP/IP 4계층과 OSI 7계층 비교

![image-20220529175237650](assets/images/posts/2022-05-29-면접을 위한 CS 전공지식 노트 (4)/image-20220529175237650.png)

- 이 계층들은 특정 계층이 변경되었을 때, 다른 계층이 영향받지 않도록 설계
- 전송 계층에서 TCP를 UDP로 변경했다고 해서 인터넷 웹 브라우저를 다시 설치해야 하는것은 아니듯 유연하게 설계됨
- 각 계층을 대표하는 스택
  - 애플리케이션 계층
    - FTP/HTTP/SSH/SMTP/DNS
  - 전송 계층
    - TCP/UDP/QUIC
  - 인터넷 계층
    - IP/ARP/ICMP
  - 링크 계층
    - 이더넷



**애플리케이션 계층**

- FTP, HTTPS, SSH, SMTP, DNS 등 응용 프로그램이 사용되는 프로토콜 계층
- 웹 서비스, 이메일 등 서비스를 실질적으로 사람들에게 제공하는 층
- `FTP`: 장치와 장치 간의 파일전송 사용되는 표준 통신 프로토콜
- `SSH`: 보안되지 않은 네트워크에서 네트워크 서비스를 안전하게 운영하기위한 암호화 네트워크 프로토콜
- `HTTP`: www을 위한 데이터 통신의 기초이자 웹 사이트를 이용하는 데 쓰는 프로토콜
- `SMTP`: 전자 메일 전송을 위한 인터넷 표준 통신 프로토콜
- `DNS`: 도메인 이름과 IP 주소를 매핑해주는 서버, 아이피주소가 바뀌어도 똑같은 도메인으로 접속가능

**전송 계층**

- 송신자와 수신자를 연결하는 통신 서비스를 제공하며 연결지향 데이터 스트림 지원
- 애플리케이션과 인터넷 계층 사이의 데이터가 전달될 때의 중계 역할을 합니다.
- TCP / UDP 등이 있다.
  - TCP : 패킷 순서 보장, 연결지향, 신뢰성
  - UDP : 패킷 순서 보장안함, 수신여부 확인안함, 단순히 데이터만 주고받음 (실시간 화상채팅)
  - TCP 연결 성립 과정
    - 신뢰성을 확보할 때, `3-way-handshake` 라는 작업을 진행
      ![image-20220529180756148](../../assets/images/posts/2022-05-29-면접을 위한 CS 전공지식 노트 (4)/image-20220529180756148.png)

**인터넷 계층**

- 장치로부터 받은 네트워크 패킷을 IP 주소로 지정된 목적지로 전송하기 위해 사용되는 계층
- IP, ARP, ICMP 등이 있으며, 패킷을 수신해야 할 상대의 주소를 지정하여 데이터를 전달
- 상대방이 제대로 받았는지 보장하지 않는 비연결형적인 특징이 있다.

**링크 계층**

- 전선, 광섬유, 무선 등으로 실질적으로 데이터를 전달
- 장치 간에 신호를 주고받는 '규칙' 을 정하는 계층
- 네트워크 접근 계층이라고도 한다.
- 물리 계층과 데이터 계층으로 나눈다.
  - 물리계층: 유/무선 LAN을 통해 0과 1로 이루어진 데이터 보내는 계층
  - 데이터 링크 계층: 이더넷 프레임을 통해 에러확인, 흐름 제어, 접근 제어를 담당

