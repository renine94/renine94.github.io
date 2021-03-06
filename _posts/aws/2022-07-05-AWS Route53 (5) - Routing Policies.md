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

title: "[aws] Route53 (5) - Routing Policy - Simple"
excerpt: "π Route53, Routing, Policy, Simple"

categories: aws
tag: [aws, route, policy, simple]

toc: true
toc_label: "π λͺ©μ°¨"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# Routing Policies

> Route53 λΌμ°ν μ μ±μ λν΄ μμλ³΄μ.



- λΌμ°ν μ μ±μ Route53 κ° DNS μΏΌλ¦¬μ μ΄λ»κ² μλ΅νλ μ§λ₯Ό μ μνλ€.
- **"λΌμ°ν" μ΄λΌλ λ¨μ΄λ₯Ό νΌλν΄μλ μλλ€.**
  - λ‘λλ°Έλ°μκ° νΈλν½μ Backend EC2 Instance λ‘ routing νλ κ²κ³Όλ λ€λ₯Έ μν©μ΄λ€.
  - μ¬κΈ°μμ λΌμ°νμ DNS κ΄μ μ΄λ€.
  - DNS λ νΈλν½μ λΌμ°ννμ§ μλλ€. νΈλν½μ DNS λ₯Ό ν΅κ³Όνμ§ μλλ€.
  - DNS λ DNS Queryμλ§ μλ΅νκ²λκ³ , Client λ€μ μ΄λ₯Ό ν΅ν΄ HTTP μΏΌλ¦¬ λ±μ μ΄λ»κ²<br>μ²λ¦¬ν΄μΌ νλμ§λ₯Ό μ μ μκ² λλ€.
- μ€μ  μ¬μ© κ°λ₯ν Endpointλ‘ λ³ννλ κ²μ λλλ€.



- Route53 μ΄ μ§μνλ λΌμ°ν μ μ±μ μλμ κ°μ΅λλ€.
  - Simple
  - Weighted
  - Failover
  - Latency Based
  - Geolocation
  - Multi-Value Answer
  - Geoproximity (using Route53 Traffic Flow feature)





## Routing Policies - Simple

> λ¨μ λΌμ°ν μ μ±

![image-20220706005953806](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706005953806.png)

- μΌλ°μ μΌλ‘, traffic μ λ¨μΌ resource λ‘ λ³΄λ΄λ λ°©μμλλ€.
  - ex) ν΄λΌμ΄μΈνΈκ° foo.example.com μΌλ‘ κ°κ³ μ νλ€λ©΄, Route53 μ΄ IPμ£Όμλ₯Ό μλ €μ€λ€.
  - μ΄λ A λ μ½λ μ£Όμμ΄λ€.
- λμΌν Record μ μ¬λ¬ κ°μ κ°μ μ§μ νλ κ²λ κ°λ₯νλ€.
  - ex) client κ° foo.example.comλ‘ κ°κΈ°λ₯Ό μμ²­νλ©΄, Route53μ 3κ°μ IPμ£Όμλ₯Ό λ°ννλ€.
  - A λ μ½λμ μλ² λ©λ μ£Όμλ€μ΄λ€.
  - clientκ° 3κ°μ€ 1κ°λ₯Ό κ³¨λΌμ λΌμ°νμ μ μ©νκ² λλ€.
- Simple Routing μ μ±μ Alias Record λ₯Ό ν¨κ» μ¬μ©νλ©΄ νλμ Resourceλ§μ λμμΌλ‘ μ§μ κ°λ₯
  - λ¨μ μ μ±μ΄λΌκ³  νλκ±΄ κ°λ¨ν΄μ λΆμ¬μ§ κ²μ΄λ€.
- μν νμΈμ ν  μ μλ€.



## μ€μ΅

- λ μ½λ μμ±μ ν΄λ¦­

![image-20220706010420766](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010420766.png)



- λΌμ°νμ μ± - λ¨μ λΌμ°ν
- **κ°(Value) μ IPμ£Όμλ₯Ό μ¬λ¬κ° μ€μ  ν  μ λ μλ€. (mulitiple value)**

![image-20220706010541411](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010541411.png)



- terminal μμ dig / nslookup μΌλ‘ ν΄λΉ Record λ₯Ό νΈμΆνλ©΄ IPμ£Όμκ° 1κ°μ΄μ λ°νλλκ²μ νμΈ κ°λ₯

![image-20220706010937521](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706010937521.png)



![image-20220706011002572](../../assets/images/posts/2022-07-05-AWS Route53 (5) - Routing Policies/image-20220706011002572.png)



