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

title: "[aws] Route53 (9) - Routing Policy - Failover (Active-Passive)"
excerpt: "π Route53, Routing, Policy, Failover"

categories: aws
tag: [aws, route, policy, failover]

toc: true
toc_label: "π λͺ©μ°¨"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Routing Policies - Failover (Active-Passive)

> μ₯μ  μ‘°μΉμ κ΄ν λΌμ°ν μ μ±

![image-20220707003611914](../../assets/images/posts/2022-07-07-AWS Route53 (9) - Routing Policies - Failover (Active-Passtive)/image-20220707003611914.png)

- Route53 κ³Ό 2κ°μ EC2 μΈμ€ν΄μ€κ° μκ³ , κ·Έμ€ νλλ μ¬ν΄ λ³΅κ΅¬ EC2 μ΄λ€.
- μν νμΈκ³Ό κΈ°λ³Έ λ μ½λλ‘ μ°κ²°νλλ°, μ΄λ νμμ μ΄λ€.
- μν νμΈ(health check)κ° λΉμ μμ΄λ©΄ μλμΌλ‘ Route53μ 2λ²μ§Έμ EC2 μΈμ€ν΄μ€λ‘ μ₯μ μ‘°μΉ
- λ³΄μ‘° EC2 μΈμ€ν΄μ€λ Health Checkλ₯Ό μ°κ²°ν μ μμ§λ§ κΈ°λ³Έκ³Ό λ³΄μ‘° κ°κ° νλμ©λ§ μμ μ μλ€.
- Client μ DNS μμ²­μ μ μμΌλ‘ μκ°λλ λ¦¬μμ€λ₯Ό μλμΌλ‘ μ»λλ€.
- κΈ°λ³Έ μΈμ€ν΄μ€κ° μ μμ΄λ©΄ Route53 λ κΈ°λ³Έ λ μ½λλ‘ μλ΅νλ€.
- νμ§λ§ health checkκ° λΉμ μμ΄λ©΄ μ₯μ  μ‘°μΉμ λμμ΄ λλ λλ²μ§Έ λ μ½λμ μλ΅μ μλμΌλ‘ μ»λλ€.



---

- κ°μ λλ©μΈμΌλ‘ λκ° μ°κ²°μν€κ³ , μν νμΈ ID λ λ£μ΄μ€μΌνλλ° μλ§λ€μ΄μ μ νλΆκ°λ₯ν μν



![image-20220707010706541](../../assets/images/posts/2022-07-07-AWS Route53 (9) - Routing Policies - Failover (Active-Passtive)/image-20220707010706541.png)