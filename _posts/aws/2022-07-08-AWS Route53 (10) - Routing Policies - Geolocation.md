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

title: "[aws] Route53 (10) - Routing Policy - GeoLocation"
excerpt: "π Route53, Routing, Policy, GeoLocation"

categories: aws
tag: [aws, route, policy, record, geolocation, geo]

toc: true
toc_label: "π λͺ©μ°¨"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# Routing Policies - Geolocation

> μ§λ¦¬ μμΉ λΌμ°ν μ μ±μ λν΄ μμλ³΄μ

- Latency-based μ μ±κ³Ό λ€λ₯΄λ€.
- μ¬μ©μμ μ€μ  μμΉλ₯Ό κΈ°λ°μΌλ‘ λΌμ°νμ΄ λλ€.
- μ¬μ©μκ° νΉμ  λλ₯μ΄λ κ΅­κ° νΉμ λ μ ννκ² λ―Έκ΅­μ κ²½μ°, μ΄λ€ μ£Όμ μλμ§ μ§μ νλ κ²μ΄λ©°,<br>κ°μ₯ μ νν μμΉκ° μ νλμ΄ κ·Έ IPλ‘ λΌμ°ν λλ€.
- μΌμΉνλ μμΉκ° μλ κ²½μ°λ κΈ°λ³Έ(Default) λ μ½λλ₯Ό μμ±ν΄μΌ νλ€.
- μ¬μ© μ¬λ‘
  - μ½νμΈ  λΆμ°μ μ ν
  - 
  - λ‘λ λ°Έλ°μ± λ±μ μ€ννλ μΉμ¬μ΄νΈ νμ§νκ° μλ€.
- GeoLocation Recordλ Health Checkμ μ°κ²°ν  μ μλ€.



![image-20220707023213959](../../assets/images/posts/2022-07-08-AWS Route53 (10) - Routing Policies - Geolocation/image-20220707023213959.png)



μ¬λ¬ λλΌκ° μλ μ λ½μ μ§λλ₯Ό λ³΄λ©΄, λμΌμ μ μ κ° λμΌμ΄ λ²μ μ μ±μ ν¬ν¨ν IPλ‘ μ μλλλ‘<br>λμΌμ GeoLocation Record λ₯Ό μ μν  μ μλ€. νλμ€μ κ²½μ°λΌλ©΄ νλμ€μ΄μ λ²μ μ μ±μ κ°μ§ IPλ‘ μ΄λν΄μΌ νλ€.

κ·Έ μΈμ λ€λ₯Έ κ³³μ μ±μμ μμ΄ λ²μ μ΄ ν¬ν¨λ κΈ°λ³Έ(Default) IPλ‘ μ΄λν΄μΌ νλ€.



## μ€μ΅

![image-20220707024700572](../../assets/images/posts/2022-07-08-AWS Route53 (10) - Routing Policies - Geolocation/image-20220707024700572.png)



- μ€μ  νκ΅­μμ μ μν  κ²½μ° 111.222.333.444 λ‘ μμ²­
- μ€μ  μΌλ³Έμμ μ μν  κ²½μ° 555.666.777.888 λ‘ μμ²­
- κΈ°ν μ§μ­μμ μ μν  κ²½μ° 999.111.222.333 λ‘ μμ²­



μΆν κΈλ‘λ² μλΉμ€λ‘ νμ₯λ  λ ν΄λΉ κΈ°λ₯μ μ΄μ©νλ©΄ μ’μ κ² κ°λ€.