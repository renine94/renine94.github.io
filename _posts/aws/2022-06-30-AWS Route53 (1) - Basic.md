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

title: "[aws] Route53 (1) - Basic & DNS"
excerpt: "🚀 Route53, DNS, URL, IP, Record, TLD, SLD"

categories: aws
tag: [aws, route, domain, dns, tld, sld, ]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# Route53



## What is DNS ?

DNS 는 Domain Name System 으로 사람에게 친숙한 **호스트 이름을 대상 서버 IP주소로 번역**해 줍니다.

![image-20220630020733122](../../assets/images/posts/2022-06-30-AWS Route53 (1) - Basic/image-20220630020733122.png)

- www.google.com => 172.217.18.36
  - 웹브라우저에 www.google.com을 입력하면 IP주소를 받고 웹브라우저가 여기에 접근하여<br>구글로부터 데이터를 얻습니다.
- DNS 는 인터넷의 중추이다.
  - URL 과 호스트이름을 IP로 변환하는것
- DNS 에는 계층적 이름 구조가 있다.
  - www.google.com 의 근원에는`.com` 이 있고,
  - 좀더 정확하게 `example.com` 이 있습니다.
  - 그리고 `www.example.com` , `api.example.com` 이 있다.



## DNS Terminologies

> DNS 관련 용어를 살펴보자.

- Domain Registrar
  -  Amazon Route53, GoDaddy, Gabia, etc.....
  - 우리들의 도메인 이름을 등록하는 곳
- DNS Records
  -  A, AAAA, CNAME, NS, ...
- Zone File
  - 모든 DNS 레코드를 포함하는 존파일
  - 호스트 이름과 IP 또는 주소를 일치시키는 방법
- Name Server
  - DNS 쿼리를 실제로 해결하는 서버
- Top Level Domain (TLD)
  - .com, .us, .in, .gov, .org, .kr, ......
  - 최상위 도메인
- Second Level Domain (SLD)
  - amazon.com, google.com, naver.com .......
  - 단어 사이에 `.` 가 있다.



**FQDN (Fully Qualified Domain Name)**

![image-20220630021317759](../../assets/images/posts/2022-06-30-AWS Route53 (1) - Basic/image-20220630021317759.png)



## How DNS Works

> DNS 동작원리를 알아보자

![image-20220630021513341](../../assets/images/posts/2022-06-30-AWS Route53 (1) - Basic/image-20220630021513341.png)

- 웹서버가 있고, 공인IP가 있고 예시로 9.10.11.12 라고 하자

- 도메인 이름 example.com 을 이용해서 접근하고자 한다.

- example.com 이라는 도메인 이름을 DNS용 서버에 등록해야 한다

  

- 여러분의 컴퓨터, 웹서버가 어떻게 접근하고 응답을 받는지 알아보자

  1. 웹 브라우저가 example.com 에 접근하기 위해서 로컬 DNS 서버에 물어본다.
     - example.com 이라는 도메인주소를 아는지
     - 로컬 DNS 서버는 보통 회사에 의해 할당되고 관리된다.
     - 또는 인터넷 서비스 제공자(ISP: kt, skt, lgU+, ...) 에 동적으로 할당된다.
  2. 로컬DNS 서버가 이 쿼리를 전에 본 적이 없다면 먼저 ICANN에 의해 관리되는 Root DNS Server에 물어본다.
     - 가장 먼저 요청되는 서버인 Root DNS Server
     - 해당 쿼리(example.com) 을 본적이 없다.
     - 그러나 `.com` 은 알고있다고 답한다.
  3. `.com` 은 이름서버(NS) 레코드로 공인 IP 1.2.3.4 로 가보라고 알려준다.
  4. 로컬DNS서버는 최상단 도메인 서버에 물어본다 (`.com`)
  5. .com TLD DNS Server는 무엇인지 모른다고 한다. 그러나 example.com 이라는 서버는 알고있다.
  6. example.com 서버는 5.6.7.8 이라고 답한다.
  7. 로컬DNS 서버는 최종 서버로 서브도메인의 DNS 서버입니다.
  8. 이는 도메인 이름 레지스트라에 의해 관리되는 서버입니다.
     - 예를들어 Amazon Route53 등등 입니다.
  9. **DNS 서버에 반복적으로 물어보며 가장 구체적인 답을 찾았다.**
  10. **만약 누군가가 다시 example.com 을 물어본다면 바로 답변을 줄 수있게된다. (Local DNS 서버에 캐싱됨)**



따라서 답변을 웹브라우저에 보내고 브라우저는 답변(IP)을 받습니다.<br>이 IP주소를 이용하여 웹 서버에 접근할 수 있게 된다.