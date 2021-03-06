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
excerpt: "๐ Route53, CNAME, Alias"

categories: aws
tag: [aws, route, cname, alias]

toc: true
toc_label: "๐ ๋ชฉ์ฐจ"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# CNAME vs Alias

> ์ด๋ฒ ํฌ์คํ์์๋ CNAME ๊ณผ Alias ์ ๋ํด ์์๋ณด์



- LoadBalancer, CloudFront ๋ฑ AWS Resource๋ฅผ ์ฌ์ฉํ๋ ๊ฒฝ์ฐ Host Name์ด ๋ธ์ถ๋๋ค.

- ๊ทธ๋ฆฌ๊ณ  ๋ด๊ฐ ๋ณด์ ํ ๋๋ฉ์ธ์ ํธ์คํธ ์ด๋ฆ์ Mapping ํ๊ณ ์ ํ  ์ ์๋ค.

- myapp.mydomain.com ์ LB ์ ๋งคํํ๋ ๊ฒฝ์ฐ

- 2๊ฐ์ง ์ ํ์ง(์ต์)์ด ์๋ค.
	- |             |    CNAME     |        Alias         |
	| :---------- | :----------: | :------------------: |
	| Host        | Host => Host | Host => AWS Resource |
	| Root Domain |      X       |          O           |


  - **CNAME**
    - ํธ์คํธ ์ด๋ฆ์ด ๋ค๋ฅธ ํธ์คํธ ์ด๋ฆ์ผ๋ก ํฅํ๋๋ก ํ  ์ ์๋ค.
    - **ex) app.mydomain.com => blabla.anything.com์ผ๋ก ํฅํ๋๋ก ์ค์  ๊ฐ๋ฅ**
    - Root Domain์ด ์๋ ๊ฒฝ์ฐ์๋ง ๊ฐ๋ฅํ๋ฏ๋ก<br>mydomain.com ์์ ๋ญ๊ฐ ๋ถ์ด์ผ ํ๋ค. ๊ทธ๋ฅ mydomain.com ์ ์๋๋ค.
    - api.mydomain.com ์ด๋ฐ์์ผ๋ก ์์ ๋ฌด์ธ๊ฐ ๋ถ์ด์ผ ํ๋ค.

  - **Alias**
    - ๋ณ์นญ Record ๋ Route53 ์ ํ์ ๋๋ค.
    - ํธ์คํธ ์ด๋ฆ์ด ํน์  AWS Resource๋ก ํฅํ๋๋ก ํ  ์ ์๋ค.
    - **ex) app.mydomain.com => blabla.amazonaws.com ์ผ๋ก ํฅํ๋๋ก ์ค์  ๊ฐ๋ฅ**
    - Alias Record๋ ๋ฃจํธ ๋ฐ ๋น๋ฃจํธ ๋๋ฉ์ธ์ ๋ชจ๋ ์๋ํ๋ค.
    - mydomain.com ์ ๋ณ์นญ์ผ๋ก ์ฌ์ฉํด AWS Resource๋ก ํฅํ๋๋ก ํ  ์ ์๊ธฐ์<br>๋งค์ฐ ์ ์ฉํ๋ค.
    - ๋ฌด๋ฃ์ด๋ค.
    - ์์ฒด์ ์ผ๋ก ์ํ ํ์ธ์ด ๊ฐ๋ฅํ๋ค.





## Alias Records

![image-20220704010210560](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704010210560.png)

- AWS Resource์๋ง ํธ์คํธ์ด๋ฆ์ด ๋งคํ์ด ๋์ด ์๋ค.
  - ๋ฐ๋ผ์ Route53 ์์ `example.com` ์ `A Record` ์ `Alias Record` ๋ก ํ๊ณ ,
  - ๊ทธ ๊ฐ์ LB์ `DNS` ์ด๋ฆ์ ์ง์ ํ๋ ค ํ๋ค๊ณ  ๊ฐ์ ํ์.
- DNS์ ํ์ฅ ๊ธฐ๋ฅ์ผ๋ก ์์ค์ ๋ชจ๋  DNS์์ ๊ฐ๋ฅํ๋ค.
- ALB ์์ IP ๊ฐ ๋ฐ๋๋ฉด `Alias Record` ๋ ์๋์ผ๋ก ์ด๊ฒ์ ์ธ์ํ๋ค.
- `CNAME` ๊ณผ๋ ๋ฌ๋ฆฌ, `Alias Record` ๋ `Zone Apex` ๋ผ๋ `DNS Namespace` ์ ์์ ๋ธ๋๋ก ์ฌ์ฉ๋  ์ ์๋ค.
  - `example.com` ์๋ `Alias Record` ๋ฅผ ์ธ ์ ์๋ ๊ฒ (Root ๋ ๊ฐ๋ฅ)



- **AWS Resource๋ฅผ ์ํ Alias Record Type์ ํญ์ A or AAAA ์ธ๋ฐ,<br>**Resource๋ IPv4 ๋๋ IPv6 ์ค ํ๋์ด๋ค.
- **Alias Record ๋ฅผ ์ฌ์ฉํ๋ฉด, TTL ์ ์ค์ ํ  ์ ์๋ค.**
- Route53 ์ ์ํด ์๋์ผ๋ก ์ค์ ์ด ๋๋ค.



## Alias Records Targets

> ๋ณ์นญ ๋ ์ฝ๋์ ๋์์ ๋ฌด์์ผ๊น?

![image-20220704010530204](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704010530204.png)

- ์ฌ์ง์ ์์ ๋ชจ๋  ์๋น์ค๋ค

- **S3 Bucket ์ ์๋๊ณ , ๋ฒํท๋ค์ด ์น์ฌ์ดํธ๋ก ํ์ฑํ๋  ์ S3 ์น์ฌ์ดํธ์๋ ๊ฐ๋ฅํ๋ค.**
- ๋์ผ ํธ์คํธ์กด์ Route53 ์ด ๋์์ผ๋ก ๊ฐ๋ฅ
- **EC2์ DNS ์ด๋ฆ์ ๋ํด์๋ Alias Record ๋ฅผ ์ค์ ํ  ์ ์๋ค.**
  - EC2 DNS Name์ Alias Record์ ๋์์ด ๋  ์ ์๋ค.





---



[์ค์ต์์ 03:08์ด](https://www.udemy.com/course/best-aws-certified-solutions-architect-associate/learn/lecture/29388902#content)

![image-20220704013156697](../../assets/images/posts/2022-07-04-AWS Route53 (4) - CNAME & Alias/image-20220704013156697.png)



๋ด๊ฐ ๊ตฌ์ํ Domain ๋ช ๊ทธ๋๋ก ALB ๋ก ํธ๋ํฝ์ ๋ณด๋ด๊ธฐ์ํด์๋ Route53 ์์ Alias Record ๋ฅผ ์ฌ์ฉํด์ผ ํ๋ค.
