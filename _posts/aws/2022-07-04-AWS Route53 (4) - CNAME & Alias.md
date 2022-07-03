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

title: "[aws] Route53 (4) - CNAME & Alias"
excerpt: "🚀 Route53, CNAME, Alias"

categories: aws
tag: [aws, route, cname, alias]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# CNAME vs Alias

> 이번 포스팅에서는 CNAME 과 Alias 에 대해 알아보자



- LoadBalancer, CloudFront 등 AWS Resource를 사용하는 경우 Host Name이 노출된다.

- 그리고 내가 보유한 도메인에 호스트 이름을 Mapping 하고자 할 수 있다.

- myapp.mydomain.com 에 LB 을 매핑하는 경우

- 2가지 선택지(옵션)이 있다.
	- |             |    CNAME     |        Alias         |
	| :---------- | :----------: | :------------------: |
	| Host        | Host => Host | Host => AWS Resource |
	| Root Domain |      X       |          O           |


  - **CNAME**
    - 호스트 이름이 다른 호스트 이름으로 향하도록 할 수 있다.
    - **ex) app.mydomain.com => blabla.anything.com으로 향하도록 설정 가능**
    - Root Domain이 아닌 경우에만 가능하므로<br>mydomain.com 앞에 뭔가 붙어야 한다. 그냥 mydomain.com 은 안된다.
    - api.mydomain.com 이런식으로 앞에 무언가 붙어야 한다.

  - **Alias**
    - 별칭 Record 는 Route53 에 한정된다.
    - 호스트 이름이 특정 AWS Resource로 향하도록 할 수 있다.
    - **ex) app.mydomain.com => blabla.amazonaws.com 으로 향하도록 설정 가능**
    - Alias Record는 루트 및 비루트 도메인에 모두 작동한다.
    - mydomain.com 을 별칭으로 사용해 AWS Resource로 향하도록 할 수 있기에<br>매우 유용하다.
    - 무료이다.
    - 자체적으로 상태 확인이 가능하다.





## Alias Records

![image-20220704010210560](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704010210560.png)

- AWS Resource에만 호스트이름이 매핑이 되어 있다.
  - 따라서 Route53 에서 `example.com` 을 `A Record` 의 `Alias Record` 로 하고,
  - 그 값은 LB의 `DNS` 이름을 지정하려 한다고 가정하자.
- DNS의 확장 기능으로 시중의 모든 DNS에서 가능하다.
- ALB 에서 IP 가 바뀌면 `Alias Record` 는 자동으로 이것을 인식한다.
- `CNAME` 과는 달리, `Alias Record` 는 `Zone Apex` 라는 `DNS Namespace` 의 상위 노드로 사용될 수 있다.
  - `example.com` 에도 `Alias Record` 를 쓸 수 있는 것 (Root 도 가능)



- **AWS Resource를 위한 Alias Record Type은 항상 A or AAAA 인데,<br>**Resource는 IPv4 또는 IPv6 중 하나이다.
- **Alias Record 를 사용하면, TTL 을 설정할 수 없다.**
- Route53 에 의해 자동으로 설정이 된다.



## Alias Records Targets

> 별칭 레코드의 대상은 무엇일까?

![image-20220704010530204](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704010530204.png)

- 사진상 위의 모든 서비스들

- **S3 Bucket 은 안되고, 버킷들이 웹사이트로 활성화될 시 S3 웹사이트에는 가능하다.**
- 동일 호스트존의 Route53 이 대상으로 가능
- **EC2의 DNS 이름에 대해서는 Alias Record 를 설정할 수 없다.**
  - EC2 DNS Name은 Alias Record의 대상이 될 수 없다.





---



[실습영상 03:08초](https://www.udemy.com/course/best-aws-certified-solutions-architect-associate/learn/lecture/29388902#content)

![image-20220704013156697](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704013156697.png)



내가 구입한 Domain 명 그대로 ALB 로 트래픽을 보내기위해서는 Route53 에서 Alias Record 를 사용해야 한다.
