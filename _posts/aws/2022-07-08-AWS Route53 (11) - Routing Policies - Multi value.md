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

title: "[aws] Route53 (11) - Routing Policy - Multi Value"
excerpt: "๐ Route53, Routing, Policy, Multi Value"

categories: aws
tag: [aws, route, policy, record, multi value]

toc: true
toc_label: "๐ ๋ชฉ์ฐจ"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Routing Policies - Multi Value

> "๋ค์ค๊ฐ" ๋ผ์ฐํ ์ ์ฑ์ ๋ํด ์์๋ณด์

![image-20220708031629047](../../assets/images/posts/2022-07-08-AWS Route53 (11) - Routing Policies - Multi value/image-20220708031629047.png)

- ํธ๋ํฝ์ ๋ค์ค ๋ฆฌ์์ค๋ก ๋ผ์ฐํํ  ๋ ์ฌ์ฉ
- Route53 ์ ๋ค์ค๊ฐ๊ณผ ๋ฆฌ์์ค๋ฅผ ๋ฐํํ๋ค.
- Health Check์ ์ฐ๊ฒฐํ๋ฉด ๋ค์ค ๊ฐ ์ ์ฑ์์ ๋ฐํ๋๋ ์ ์ผํ Resource๋ Health Check์ ๊ด๋ จ์ด ์๋ค.
- ๊ฐ๊ฐ์ MultiValue ์ฟผ๋ฆฌ์ ์ต๋ 8๊ฐ์ ์ ์ ๋ ์ฝ๋๊ฐ ๋ฐํ๋๋ค.
  - ํด๋ผ์ด์ธํธ๋ 8๊ฐ์ ๋ ์ฝ๋์ค ํ๋๋ฅผ ์ ํ
  - 1๊ฐ ์ด์์ ์ ์ ๋ ์ฝ๋๊ฐ ํฌํจ๋์ด์์ด, ํด๋ผ์ด์ธํธ๋ ์์ ํ ์ฟผ๋ฆฌ๋ฅผ ๊ฐ์ง์ ์๋ค

- **ELB ์ ์ ์ฌํด ๋ณด์ด์ง๋ง, ELB๋ฅผ ๋์ฒดํ  ์๋ ์๋ค.**
  - ํด๋ผ์ด์ธํธ ์ธก๋ฉด์ ๋ก๋๋ฐธ๋ฐ์ฑ ์ด๋ค.




- ํฌ์ค์ฒดํฌ๊ฐ ๋น์ ์์ธ Record ๋ ๋ค์ค๊ฐ์์ ๋ฐํ๋์ง ์๋๋ค 
- www.example.com ์ผ๋ก ์์ฒญ๋ณด๋ด๋ฉด 3๊ฐ์ ๊ฐ์ด ์ค๊ฒ๋๋ค. (์ ์์ธ ๋ ์ฝ๋)





