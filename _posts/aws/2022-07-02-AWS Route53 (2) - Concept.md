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

title: "[aws] Route53 (2) - Route53 & Records"
excerpt: "π Route53, Records Type, Hosted Zones"

categories: aws
tag: [aws, route, records]

toc: true
toc_label: "π λͺ©μ°¨"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"





---

# Amazon Route53

[μ§λ ν¬μ€ν](https://renine94.github.io/aws/AWS-Route53-(1)-Basic/)μμλ DNS κ° λ¬΄μμΈμ§ μμμΌλ,<br>μ΄λ²μκ°μλ Amazon Route53 μ λν΄ μμλ³΄λλ‘ νμ.
{: .notice--success}

![image-20220703144312323](../../assets/images/posts/2022-07-02-AWS Route53 (2) - Concept/image-20220703144312323.png)

- κ³ κ°μ©μ±, νμ₯μ±μ κ°μΆ μμ ν κ΄λ¦¬λλ©° κΆνμλ DNS μ΄λ€.
  - μ¬κΈ°μ κΆνμ΄ μλ€λΌλ λ»μ, μ¬μ©μκ° DNS records λ₯Ό μλ°μ΄νΈν  μ μλ€λ μλ―Έμ΄λ€.
  - μ¦, DNS μ λν μμ ν μ μ΄ν  μ μλ€.
- Route53 λν Domain Registrar μ€ νλμ΄λ€.
- λ¦¬μμ€ κ΄λ ¨ μν νμΈμ ν  μ μλ€. (ν¬μ€μ²΄ν¬)
- 100% SLA κ°μ©μ±μ μ κ³΅νλ μ μΌν AWS μλΉμ€μ΄λ€.
- Route53 μ΄λΌλ μ΄λ¦μ μ΄μ 
  - DNS Port κ° μ ν΅μ μΌλ‘ 53λ² ν¬νΈλ₯Ό μ¬μ©νκΈ° λλ¬Έμ΄λ€.



## Route53 - Records

- Route53 μμ μ¬λ¬ DNS Records λ₯Ό μ μνκ³ , λ μ½λλ₯Ό ν΅ν΄ νΉμ  DomainμΌλ‘ λΌμ°ννλ λ°©λ²μ μ μνλ€.
- κ°κ°μ Records λ€μ μλλ€μ ν¬ν¨νλ€.
  - **Domain/subDomain Name** - ex) example.com
  - **Record Type** - ex) A or AAAA or CNAME, etc....
  - **Value** - ex) 12.34.56.78
  - **Routing Policy** - Route53μ΄ Queryμ μλ΅νλ λ°©μ
  - **TTL** - DNS Resolverμμ Recordsκ° Caching λλ μκ°μ μλ―Ένλ€.
- Route53 μ μλμ **DNS Records Type** λ€μ μ§μνλ€.
  - **(νμ) A, AAAA, CNAME, NS**
  - (κ³ κΈ) CAA, DS, MX, NARTR, PTR, SOA, TXT, SPF, SRV



## Record Types

> Records μ μ’λ₯λ€μ μμλ³΄μ.

- A
  - νΈμ€νΈ μ΄λ¦κ³Ό IPv4 λ₯Ό Mapping νλ€.
  - ex) example.com μ 1.2.3.4 λ‘ λ°λ‘ μ°κ²°λλ€.
- AAAA
  - A μ λΉμ·ν μμ΄λμ΄
  - νΈμ€νΈ μ΄λ¦κ³Ό IPv6 μ£Όμλ₯Ό λ§€ννλ€.
- CNAME
  - νΈμ€νΈ μ΄λ¦κ³Ό λ€λ₯Έ νΈμ€νΈ μ΄λ¦κ³Ό λ§€ννλ€.
  - λμ νΈμ€νΈ μ΄λ¦μ A or AAAA Record κ° λ  μλ μλ€.
  - Route53 μμ DNS μ΄λ¦ κ³΅κ° λλ Zone Apexμ μμ λΈλμ λν CNAMESλ₯Ό μμ±ν μ μλ€.
    - example.com μ CNAME μ λ§λ€μλ μμ§λ§ www.example.comμ λν CNAME<br>Recordλ λ§λ€ μ μλ€.
- NS
  - νΈμ€ν μ‘΄μ μ΄λ¦ μλ²(Name Server)μ΄λ€.
  - μλ²μ DNS μ΄λ¦ or IPμ£Όμλ‘ νΈμ€ν μ‘΄μ λν DNS μΏΌλ¦¬μ μλ΅ν  μ μλ€.
  - νΈλν½μ΄ λλ©μΈμΌλ‘ λΌμ°ν λλ λ°©μμ μ μ΄νλ€.



## Hosted Zones

> νΈμ€ν μ‘΄μ μ΄ν΄λ³΄μ

- νΈμ€ν μ‘΄μ Record μ Container μ΄λ€.
- Domain κ³Ό subDomain μΌλ‘ κ°λ Traffic μ Routing λ°©μμ μ μνλ€.



- νΈμ€ν μ‘΄ 2κ°μ§ μ’λ₯
  - Public Hosted Zones
    - νΌλΈλ¦­ λλ©μΈ μ΄λ¦μ μ΄ λλ§λ€, mypublicdomain.comμ΄ νΌλΈλ¦­ λλ©μΈ μ΄λ¦μ΄λΌλ©΄,<br>νΌλΈλ¦­ νΈμ€ν μ‘΄μ λ§λ€ μ μμ΅λλ€.
    - νΌλΈλ¦­ μ‘΄μ μΏΌλ¦¬μ λλ©μΈ μ΄λ¦ app1.mypublicdomainname.comμ IPκ° λ¬΄μμΈμ§ μ μ μλ€.
  - Private Hosted Zones
    - κ³΅κ°λμ§ μμ λλ©μΈ μ΄λ¦μ μ§μνλ€.
    - κ°μ νλΌμ΄λΉ ν΄λΌμ°λ(VPC) λ§μ΄ URLμ Resolve ν  μ μλ€.
    - app1.company.internal κ°μ κ²½μ°
    - κΈ°μμμλ λλλ‘ νμ¬ λ€νΈμν¬ λ΄μμλ§ μ κ·Όν  μ μλ URLμ΄ μλ€.
    - λΉκ³΅κ° URL μ΄κΈ° λλ¬Έμ λΉκ³΅κ°λμ΄ μλ€. μ΄λ©΄μλ Private DNS Record κ° μλ€
- AWSμμ λ§λλ μ΄λ€ νΈμ€νμ‘΄μ΄λ  μμ 0.5 λ¬λ¬λ₯Ό μ§λΆν΄μΌ νλ€.
  - Route53 μ¬μ©μ λ¬΄λ£κ° μλλ€.
  - λλ©μΈ μ΄λ¦μ λ±λ‘ λ° κ΅¬μνλ©΄ 1λμ μ΅μ 12$ λ₯Ό μ§λΆν΄μΌ νλ€. (ex) **renine94.com**



## Public vs Private Hosted Zones

![image-20220703145944285](../../assets/images/posts/2022-07-02-AWS Route53 (2) - Concept/image-20220703145944285.png)

- Public Hosted Zone
  - κ³΅κ°λ Client λ‘λΆν° μ¨ Queryμ μλ΅ν  μ μλ€.
  - μΉ λΈλΌμ°μ μμ example.com μ μμ²­νλ©΄ IPλ₯Ό λ°ννλ€.
- Private Hosted Zone
  - ν΄λΉ VPC μμλ§ λμνλ€.
  - λΉκ³΅κ° λλ©μΈ μ΄λ¦μ Private Resourceλ₯Ό μλ³ν  μ μκ² νλ€.
  - ex)
    - EC2 κ° 1κ° μλ€. webapp.example.internal μ μλ³νκ³ μ νλ€.
    - λ λ€λ₯Έ EC2 μμλ api.example.internal μ μλ³νκΈ° μνκ³ 
    - DB μμλ db.example.internal μ μλ³νκ³ μ νλ€.
    - **Private Host Zoneμ λ±λ‘νλ €κ³  νλλ°, μ²« λ²μ§Έ EC2 κ° api.example.internal μ μμ²­νλ κ²½μ°**
    - private Host Zoneμ Private IP 10.0.0.10 μ΄λΌλ λ΅μ κ°κ³  μλ€.
    - EC2 λ DBμ μ°κ²°μ΄ νμν  μλ μλ 2λ²μ§Έ EC2 μ μ°κ²°νλ€.
    - db.example.internal μ΄ λ¬΄μμΈμ§ λ¬Όμ΄λ³΄λ©΄ private hosted zone μ private IPλ₯Ό μλ €μ€λ€.
    - EC2 μΈμ€ν΄μ€λ DBμ μ§μ μ μΌλ‘ μ°κ²°ν  μ μλ€
  - μ€μ§ private resource, μμ»¨λ° VPC μμλ§ Query μ§μν  μ μλ€.
- public host zoneμ private host zoneκ³Ό λκ°μ΄ λμνμ§λ§,<br> public hosted zoneμ λκ΅¬λ  μ°λ¦¬λ€μ Record λ₯Ό μΏΌλ¦¬ ν  μ μμ΅λλ€.



