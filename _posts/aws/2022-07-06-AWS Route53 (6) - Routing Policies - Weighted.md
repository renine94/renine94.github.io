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

title: "[aws] Route53 (6) - Routing Policy - Weighted"
excerpt: "๐ Route53, Routing, Policy, Weighted"

categories: aws
tag: [aws, route, policy, weighted]

toc: true
toc_label: "๐ ๋ชฉ์ฐจ"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"



---

# Routing Policies - Weighted

> ๊ฐ์ค์น ๊ธฐ๋ฐ ๋ผ์ฐํ ์ ์ฑ์ ๋ํด ์์๋ณด์
>
> ์๋ ๊ทธ๋ฆผ์ Route53 ์ด๋ฏธ์ง ์ค๋ฅ ๋ฌด์ํ์ธ์ฉ.

![image-20220706011345980](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706011345980.png)

- ์ด ์ ์ฑ์ ์ฌ์ฉํ๋ฉด, ๊ฐ์ค์น๋ฅผ ํ์ฉํด **์์ฒญ์ ์ผ๋ถ ๋น์จ์ ํน์  ๋ฆฌ์์ค๋ก ๋ณด๋ด๋ ์์ ์ ์ด๊ฐ ๊ฐ๋ฅ**ํด์ง๋ค.
  - ์ ๊ทธ๋ฆผ์ ๋ณด๋ฉด, Route53 ์ด ์๊ณ , EC2๊ฐ 3๊ฐ ์คํ์ค์ผ๋, 70, 50, 10 ์ผ๋ก ๊ฐ์ค์น๋ฅผ ํ ๋น๋ฐ๋๋ค.
  - ๊ฐ์ค์น์ ํฉ์ด ๊ผญ 100์ด ๋  ํ์๋ ์๋ค.
  - Route53์์ ์ค๋ DNS ์๋ต์ 70% ๊ฐ ์ฒซ ๋ฒ์งธ EC2 ์ธ์คํด์ค๋ก ๋ฆฌ๋ค์ด๋ ํ ๋๋ค.
  - 20%๋ 2๋ฒ์งธ, 10%๋ 3๋ฒ ์งธ ์ธ์คํด์ค๋ก ๊ฐ๋๋ค.
  - ๋ฐ๋ผ๊ฐ์ ๊ฐ Record ์ ์๋์ ์ผ๋ก ๊ฐ์ค์น๋ฅผ ํ ๋นํ๊ฒ ๋๋ค.
- ๊ฐ Record๋ก ๋ณด๋ด์ง๋ ํธ๋ํฝ(traffic)์ ์์<br>traffic = Weight for a specific record / sum of all Weights for all records ๋ก ๊ณ์ฐ ๊ฐ๋ฅํ๋ค.
  - traffic = 70 / 100 = 70% ์ ํธ๋ํฝ์ด ์ฒซ ๋ฒ์งธ EC2 ๋ก ๊ฐ๊ฒ ๋๋ค.
  - ํ DNS ์ด๋ฆ ํ์ ์๋ ๋ค๋ฅธ Record๋ค๊ณผ ๋น๊ตํ์๋, ํด๋น Record๋ก ํธ๋ํฝ์ ์ผ๋ง๋ ๋ณด๋ผ์ง ๋ํ๋ด๋ ๊ฐ
- **DNS Records ๋ค์ ๋ชจ๋ ๊ฐ์ ์ด๋ฆ๊ณผ ํ์(์ ํ)์ด์ด์ผ ํ๋ค.**
- ์ํ ํ์ธ๊ณผ๋ ๊ด๋ จ๋  ์ ์๋ค.
- ์ฌ์ฉ์ฌ๋ก
  - ์๋ก ๋ค๋ฅธ Region๋ค์ ๊ฑธ์ณ ๋ก๋๋ฐธ๋ฐ์ฑ์ ํ  ๋๋, ์ ์ ์์ ํธ๋ํฝ์ ๋ณด๋ด ์ App์ ํ์คํธํ๋ ๊ฒฝ์ฐ ์ฌ์ฉ
- ๊ฐ์ค์น 0 ์ ๊ฐ์ ๋ณด๋ด๊ฒ ๋๋ฉด ํน์  Resource์ ํธ๋ํฝ ๋ณด๋ด๊ธฐ๋ฅผ ์ค๋จํด ๊ฐ์ค์น๋ฅผ ๋ฐ๊ฟ ์ ์๋ค.
- **๋ง์ฝ, ๋ชจ๋  resource record์ ๊ฐ์ค์น์ ๊ฐ์ด 0์ธ ๊ฒฝ์ฐ์๋ ๋ชจ๋  Record๊ฐ ๋ค์ ๋์ผํ ๊ฐ์ค์น๋ฅผ ๊ฐ๊ฒ ๋๋ค.**



## ์ค์ต

![image-20220706013159426](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706013159426.png)





- ๊ฐ์ค์น ๊ธฐ๋ฐ ๋ ์ฝ๋๋ ๋ ์ฝ๋์ ์ด๋ฆ๊ณผ ํ์์ ๋์ผํ ๊ฒ์ ์ฌ๋ฌ๊ฐ ๋ง๋ค๊ณ  ๊ฐ์ค์น๋ฅผ ๋ค๋ฅด๊ฒ ์ฃผ์ด์ผ ํ๋ค.

![image-20220706013509882](../../assets/images/posts/2022-07-06-AWS Route53 (6) - Routing Policies - Weighted/image-20220706013509882.png)