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

title: "[aws] Route53 (12) - Domain Registar & DNS Service"
excerpt: "๐ Route53, Routing, Domain Registar, DNS Service"

categories: aws
tag: [aws, route, domain, registar, dns, service]

toc: true
toc_label: "๐ ๋ชฉ์ฐจ"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Domain Registar vs  DNS Service

> ๋๋ฉ์ธ ๋ ์ง์คํธ๋ผ์ DNS์๋น์ค๋ฅผ ๊ตฌ๋ณํด๋ณด์

![image-20220708033539748](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708033539748.png)

- ๋๋ฉ์ธ Registar ๋ฅผ ํตํด ์ํ๋ ์ด๋ฆ์ ๋๋ฉ์ธ์ ๊ตฌ๋งคํ  ์ ์๋ค. (ex. www.renine94.com)
  - ๋งค๋ ๋น์ฉ์ ์ง๋ถํ๋ค. (1๋์ ์ฝ 12๋ฌ๋ฌ)
  - Route53 ์ธ์ ๋ค๋ฅธ ๋๋ฉ์ธ Registar๋ฅผ ์ด์ฉํด๋ ๋๋ค. (Godday, Whois, Gabia, etc,,,,) ๋ฌด๋ฃ๋๋ฉ์ธ ๋ฑ๋ฑ
- ๋ ์ง์คํธ๋ผ๋ฅผ ํตํด ๋๋ฉ์ธ์ ๋ฑ๋กํ๋ฉด DNS records ๊ด๋ฆฌ๋ฅผ ์ํ DNS ์๋น์ค๋ฅผ ์ ๊ณตํ๋ค.
- ์ฐ๋ฆฌ์ DNS records๋ฅผ ๊ด๋ฆฌํ๊ธฐ์ํด์ ๋ค๋ฅธ DNS ์๋น์ค๋ฅผ ์ฌ์ฉํ  ์ ์๋ค.
- ์ฌ์ฉ ์์
  - GoDaddy ์์ ๋๋ฉ์ธ์ ๊ตฌ์ํ๊ณ , Route53 ์ ์ด์ฉํ์ฌ DNS records๋ฅผ ๊ด๋ฆฌํ๋ ๊ฒฝ์ฐ



## GoDaddy as Registrar & Route53 as DNS Service

> ๊ณ ๋๋๋ฅผ registrar ๋ก ์ด์ฉํ๊ณ ,<br>Route53 ์ DNS Service๋ก ์ด์ฉํด๋ณด์
>
> - Route53 ์์ ๋๋ฉ์ธ๊ตฌ์ํ๊ณ  DNS Service๋ก๋ ์ฌ์ฉ๊ฐ๋ฅ (Route53์์ ๋์์ ๋๋ค ๊ฐ๋ฅ)

![image-20220708033739372](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708033739372.png)



- GoDaddy ์์ ๋๋ฉ์ธ์ ๊ตฌ์ํ๋ฉด NameServer ์ต์์ด 4๊ฐ ์์ฑ๋๋ค.
- ์ฌ์ฉ์ ์ ์ NS๋ฅผ ์ง์ ํ  ์ ์๋ค.
- ๋ฐฉ๋ฒ
  - Route53 ์์ ์ํ๋ Domain์ Public Hosted Zone์ ์์ฑํ๋ค. (๊ณต์ฉ ํธ์คํ ์์ญ)
  - ํธ์คํ ์์ญ ์์ธ์ ์ค๋ฅธ์ชฝ ๋ถ๋ถ์์ NS ๋ฅผ ์ฐพ๋๋ค.
  - ์ฌ๊ธฐ ์๋ 4๊ฐ์ NS ๋ฅผ GoDaddy ์น์ฌ์ดํธ์์ ๋ณ๊ฒฝํด์ผ ํ๋ค.
- ์ด์  GoDaddy์์ ์ฌ์ฉํ  ์ด๋ฆ ์๋ฒ์ ๊ดํ ์ฟผ๋ฆฌ์ ์๋ตํ๋ฉด NS ๊ฐ Route53 NS ์๋ฒ๋ฅผ ๊ฐ๋ฆฌํจ๋ค.
- Route53 ์ ์ฌ์ฉํด์ ํด๋น ์ฝ์์์ ์ง์  ์ ์ฒด DNS Records๋ฅผ ๊ด๋ฆฌํ  ์ ์๊ฒ ๋๋ค.



## 3rd Party Registrar with Amazon Route53

![image-20220708034436865](../../assets/images/posts/2022-07-08-AWS Route53 (12) - Domain Registar & Service/image-20220708034436865.png)

- ์ ๋ฆฌ
  - ๋๋ฉ์ธ์ ํ์ฌ ๋ฑ๋ก๋ํ์ฌ์์ ๊ตฌ๋งคํด๋ ๋๋ค.
  - DNS์๋น์ค ์ ๊ณต์๋ก Route53์ ์ฌ์ฉ๊ฐ๋ฅํ๋ค.
  - Route53์์ ๊ณต์ฉ ํธ์คํ ์์ญ ์์ฑ
  - ๋๋ฉ์ธ์ ๊ตฌ์ํ(GoDaddy)์ ์น์ฌ์ดํธ์์ NS ๋ฅผ ์๋ฐ์ดํธํ๋ฉด Route53 NS๋ฅผ ๊ฐ๋ฆฌํค๊ฒ ๋๋ค.





