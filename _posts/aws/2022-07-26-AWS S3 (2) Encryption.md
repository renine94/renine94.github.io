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

title: "[aws] S3 (2) - Encryption"
excerpt: "🚀 S3 Encryption"

categories: aws
tag: [aws, s3, objects, encryption]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# S3 Encryption for Objects

S3 에서 Objects 를 암호화하는 방법에는 4가지가 있다.

- **SSE-S3** : AWS가 처리 및 관리하는 key를 사용해 S3 객체를 암호화하는 방법
- **SSE-KMS** : AWS 키관리 서비스를 사용해서 암호화 키를 관리하는 방법
- **SSE-C** : 사용자가 만든 암호화 키를 관리할 때 쓰이는 방식
- **Client Side Encryption** : 클라이언트측 암호화



어느 상황에 어느 암호화 방법을 사용해야 하는지 살펴보자



## S3 암호화1 (SSE-S3)

![image-20220726014949590](../../assets/images/posts/2022-07-26-AWS S3 (2) Encryption/image-20220726014949590.png)

- 이 암호화 방법은 Amazon S3 에서 처리하고 관리하는 키를 암호화에 사용하는 방식
- 객체는 서버측에서 암호화 된다.
- SSE 가 서버 측 암호화를 뜻한다.
- 암호화 유형은 AES-256 알고리즘
- 객체를 업로드하고, SSE-S3 암호화를 설정하려면 `"x-amz-server-side-encryption": "AES256"` <br>으로 헤더를 설정해야 한다.
- S3 에서 데이터 키를 전부 소유 및 관리하고 있게 된다.





## S3 암호화2 (SSE-KMS)

![image-20220726015045444](../../assets/images/posts/2022-07-26-AWS S3 (2) Encryption/image-20220726015045444.png)

- KMS 는 키 관리 서비스를 의미하며, 암호화 서비스들 중 하나
- SSE-KMS 에서 암호화 키는 KMS 서비스에서 처리 및 관리 한다.
- SSE-S3 대신 이 방법을 택하는 이유
  - 누가 어떤 키에 접근할 수 있는지 제어 가능
  - 감사 추적을 할 수 있다
- 각각 객체는 서버측에서 암호화된다.
- 헤더설정할때 `"x-amz-server-side-encryption": "aws:kms"` 라고 설정 필요
- 서버 측 암호화이므로 원리는 이전과 동일
- KMS 고객 마스터 키를 사용하여 암호화를 진행하여 S3 버킷에 저장된다.



## S3 암호화3 (SSE-C)

![image-20220726015554440](../../assets/images/posts/2022-07-26-AWS S3 (2) Encryption/image-20220726015554440.png)

- 서버 측 암호화 방식
- AWS가 외부에서 고객이 관리하는 키를 사용
- S3 는 고객이 제공한 암호화 키를 저장하지 않는다.
- 암호화를 위해서는 당연히 키를 사용하겠지만 그 후에는 키를 폐기한다.
- 데이터를 AWS로 전송할때는 HTTPS 사용해야 하며, AWS로 암호를 전달할 테니 전송되는동안 암호화 필요
- 암호화 키가 HTTP Header에 제공되어야 한다.
  - 모든 HTTP 요청마다 매번 제공되어야 함
  - 항상 사용후, 폐기 되기 때문



- 만약, SSE-C를통해 Amazon S3 로부터 파일을 다시 다운받으려고 하면,
  - 사용된 것과 동일한 클라이언트 측 데이터 키를 제공받아야 한다.
  - 클라이언트가 키를 제공 및 관리하기 때문이다.
  - AWS 는 사용자가 어떤 데이터 키를 사용했는지 알 수 없기 때문



## S3 암호화4 (Client Side Encryption)

![image-20220726015756299](../../assets/images/posts/2022-07-26-AWS S3 (2) Encryption/image-20220726015756299.png)

- 이 방법은, 객체를 업로드하기 전, 클라이언트 즉, 우리가 객체를 암호화 하는 것
- 클라이언트 라이브러리를 사용할 수 있다.
  - Amazon S3 Encryption Client 등으로 클라이언트 측 암호화를 수행할 수 있다.
- 클라이언트는 데이터를 S3 로 보내기 전에 암호화 해야 한다.
- 전달받은 데이터가 CSE 를 사용해 암호화 되었다며느, 데이터를 복호화할 책임도 사용자에게 달려있게 된다.
  - 따라서 올바른 키가 준비되어 있어야 한다. (키 분실하면 안됨)





# Encryption in transit (SSL/TLS)

> 통신 중 암호화
>
> SSL/TLS 연결이 여기에 해당한다.

![image-20220726020045233](../../assets/images/posts/2022-07-26-AWS S3 (2) Encryption/image-20220726020045233.png)

- HTTP
  - 암호화 되지 않은 엔드포인트 노출
- HTTPS
  - 암호화된 엔드포인트 노출하여 전송 중 암호화 서비스를 제공
  - 이 때, SSL/TLS 인증서의 도움을 받게 된다.



- 원하는 엔드포인트를 사용해도 무방하지만, HTTPS 를 추천하고 많이 사용된다.
- HTTPS 를 사용하게 되면 Client 와 S3 사이를 이동하는 데이터가 모두 암호화 된다.



- SSE-C 암호화방식을 사용하면 HTTPS 통신방식이 필수(의무)이다.
- 전송 중 암호화는 SSL/TLS 라고도 불리운다. (SSL/TLS 인증서를 사용하기 때문)