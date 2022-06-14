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

title: "[aws] ELB - SSL/TLS Basic"
excerpt: "🚀 ELB, SSL, TLS"

categories: aws
tag: [aws, elb, ssl, tls]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# SSL/TLS - Basics

여기서 다루게 될 SSL/TLS 의 개념은 굉장히 단순화된 버전이다.<br>실제로는 굉장히 복잡한 내용이므로 따로 찾아보길 추천드립니다.
{: .notice--success}



**SSL 인증서를 사용하면 클라이언트와 로드밸런서 사이에서 전송 중에 있는 트래픽을 암호화 할 수 있다.**

- In-Flight 암호화라고 불리는 과정으로,<br> 즉 데이터가 네트워크를 통과하는 중에 암호화되고 발신자와 수신자만이 이를 해독할 수 있는 것
- **SSL**은 **보안 소켓 계층**을 뜻하며 연결을 암호화하는데에 사용된다.
- **TLS**는 **SSL의 최신 버전으로서 전송 계층 보안을 의미**한다.
- 요즘에 주로 사용되는건 TLC 인증서지만, 대부분 사람들은 이를 여전히 SSL 이라고 부르고 있다.
- 공용 SSL 인증서는 `Comodo, Symantec, GoDaddy, GlobalSign, Letencrypt` <br>등의 인증기관에서 발급된다.
- 로드밸런서(ELB) 와 연결된 공용 SSL 인증서를 사용하면 클라이언트와 로드밸런서 사이에 연결을 암호화
- SSL 인증서에는 설정한 유효 기간이 있고, 인증을 위해 주기적으로 갱신해야 한다.



**로드밸런서 관점에서 인증서가 어떻게 작동하는가?**

![image-20220615013948441](../../assets/images/posts/2022-06-15-AWS ELB (6) - SSL & TLS/image-20220615013948441.png)

1. 유저가 HTTPS를 통해 연결
2. 이때 S는 SSL 인증서를 사용하고 있다는 의미, 암호화되어 안전한 상태
3. 공용 인터넷을 통해 로드 밸런서와 연결된다.
4. 이때 로드밸런서는 내부적으로 SSL 인증서 종료라는 작업을 수행한다.
5. 백엔드에서는 EC2 인스턴스와 통신할 수 있는데, HTTP를 사용하기 때문에 암호화는 되어있지 않다.<br>하지만 트래픽은 어느정도의 안전성을 보장하는 사설 네트워크 VPC를 통해 전송된다.
6. ELB가 X.509 인증서를 불러온다. (SSL or TLS 서버 인증서라고 불리는 인증서)
7. AWS 에서 ACM 을 사용해 SSL 인증서를 관리할 수 있다.
   - ACM 은 AWS 인증서 관리자의 약자이다. (AWS Certification Management)
8. 우리들의 인증서도 ACM에 업로드할 수 있다.
9. HTTPS 리스너를 설정할 때는 기본 인증서를 지정해야 한다.
10. 다수의 도메인을 지원하는 인증서 선택 목록을 추가할 수도 있다.
11. 클라이언트는 SNI, 즉 서버 이름 표시를 사용해서 도달하는 호스트 이름을 지정할 수 있다.



<br><br>



## 🚀 SNI 개념

> Server Name Indication (SNI)

![image-20220615014317375](../../assets/images/posts/2022-06-15-AWS ELB (6) - SSL & TLS/image-20220615014317375.png)

원하는 경우 HTTPS에 대해 특정한 보안 정책을 설정할 수 있다는 의미<br>레거시 클라이언트로 불리는 구형 TLS SLS를 지원하도록 지정할 수 있다.<br>**SNI 를 사용하면 한 웹 서버 상에 다수의 SSL 인증서를 발급해 단일 웹서버가 여러 개의 웹사이트를 제공하도록<br>하는 문제를 해결해 줍니다.**

이는 최신 프로토콜이며 이를 위해서는 클라이언트가 초기 SSL핸드셰이크에서 대상 서버의<br>호스트이름을 명시해야 합니다.<br>즉, 클라이언트가 해결하고자 하는 웹사이트의 이름을 얘기하면 서버가 어떤 인증서를 불러올지 알 수 있다.<br>최신 프로토콜이기 때문에 모든 클라이언트가 이를 지원하지 않는다.

**이 프로토콜은 ALB와 NLB 와 같은 최신버전의 로드밸런서나 CloudFront 에서만 작동**한다.<br>따라서 ELB 에 SSL 인증서가 여러개가 있다면 ALB 또는 NLB 둘중 하나라고 생각하면 된다.



**SSL 인증서를 어디에서 지원될까**

로드밸런서의 `Listners` 탭에서 리스너를 추가할 수 있다.

- CLB
  - 하나의 SSL 인증서만 지원한다.
  - 여러개의 SSL 인증서가 있을경우 여러개의 클래식로드밸런서를 사용하면 된다.
- ALB
  - v2 라고도하며, 다중 SSL 인증서를 가진 다수의 리스너를 지원할 수 있어서 유용하다.
  - 그리고 이때는 방금 살펴본 SNI 를 사용한다.
  - 다양한 대상그룹에 대해 다수의 SSL 인증서를 가질 수 있다.
- NLB
  - 다중 SSL 인증서를 가진 다수의 리스너를 지원하며 역시 SNI 를 사용한다.





## 실습

![image-20220615020334474](../../assets/images/posts/2022-06-15-AWS ELB (6) - SSL & TLS/image-20220615020334474.png)



![image-20220615020523082](../../assets/images/posts/2022-06-15-AWS ELB (6) - SSL & TLS/image-20220615020523082.png)