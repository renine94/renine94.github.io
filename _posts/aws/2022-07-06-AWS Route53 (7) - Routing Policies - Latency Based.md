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

title: "[aws] Route53 (7) - Routing Policy - Latency Based"
excerpt: "๐ Route53, Routing, Policy, Latency Based"

categories: aws
tag: [aws, route, policy, latency]

toc: true
toc_label: "๐ ๋ชฉ์ฐจ"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"




---

# Routing Policies - Latency-based

> ์ง์ฐ ์๊ฐ ๊ธฐ๋ฐ ๋ผ์ฐํ ์ ์ฑ์ ์์๋ณด์.

![image-20220706014424327](../../assets/images/posts/2022-07-06-AWS Route53 (7) - Routing Policies - Latency Based/image-20220706014424327.png)

- ์ง์ฐ ์๊ฐ์ด ๊ฐ์ฅ ์งง์, ์ฆ ๊ฐ์ฅ ๊ฐ๊น์ด ๋ฆฌ์์ค๋ก ๋ฆฌ๋ค์ด๋ ํ ํ๋ ์ ์ฑ
- ์ง์ฐ์๊ฐ์ ๋ฏผ๊ฐํ ์น์ฌ์ดํธ๋ App์ด ์์ ๊ฒฝ์ฐ ์ ์ฉํ ์ ์ฑ
- **์ง์ฐ์๊ฐ์ ์ ์ ๊ฐ ๋ ์ฝ๋๋ก ๊ฐ์ฅ ๊ฐ๊น์ด ์๋ณ๋ AWS Region์ ์ฐ๊ฒฐํ๊ธฐ๊น์ง ๊ฑธ๋ฆฌ๋ ์๊ฐ์ ๊ธฐ๋ฐ์ผ๋ก ์ธก์ **
- ๋์ผ์ ์ ๋ค์ด ๋ฏธ๊ตญ์ ์๋ resource์ ์ง์ฐ์๊ฐ์ด ๊ฐ์ฅ ์งง๋ค๋ฉด,<br>ํด๋น ์ ์ ๋ค์ ๋ฏธ๊ตญ ๋ฆฌ์ ์ผ๋ก ๋ฆฌ๋ค์ด๋ ํ ๋  ๊ฒ
- ์ํ ํ์ธ๊ณผ ์ฐ๊ฒฐ์ด ๊ฐ๋ฅํ๋ค.



- ๋ ๊ฐ์ Region์ App์ ๋ฐฐํฌํ๋ค๊ณ  ๊ฐ์ 
- ap-southeast-1 ๊ณผ us-east-1
- ์ ์ ๋ค์ ์ธ๊ณ ๊ฐ์ง์ ์์ผ๋ฉฐ, Route53์ด ์ง์ฐ์๊ฐ์ ์ธก์ 
- ์ง์ฐ์๊ฐ์ด ๊ฐ์ฅ ์งง์ ๊ฐ๊น์ด ๊ฑฐ๋ฆฌ์ ์ ์ ๋ค์ด us-east-1 ์ ALB๋ก ์ฐ๊ฒฐ๋๊ณ <br>๋ค๋ฅธ ์ ์ ๋ค์ ap-southeast-1 ์ผ๋ก ์ฐ๊ฒฐ๋๋ค.



## ์ค์ต



![image-20220706015004602](../../assets/images/posts/2022-07-06-AWS Route53 (7) - Routing Policies - Latency Based/image-20220706015004602.png)



- VPN ์ ์ผ์ ๋ค๋ฅธ ๊ตญ๊ฐ๋ก IP๋ฅผ ๋ณ๊ฒฝํ ํ, ํ์คํธํ๋ฉด ๊ฐ์ฅ ์ง์ฐ์๊ฐ์ด ์งง์ ๋ฆฌ์ ์์์ ์๋ต์ ๋ฐ์ ์ ์๊ฒ ๋๋ค.



