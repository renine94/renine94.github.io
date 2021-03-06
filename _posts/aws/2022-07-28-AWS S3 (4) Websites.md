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

title: "[aws] S3 (4) - WebSites"
excerpt: "π S3 Websites, Hosting"

categories: aws
tag: [aws, s3, websites, hosting]

toc: true
toc_label: "π λͺ©μ°¨"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"

---

# S3 Websites

> S3 μΉμ¬μ΄νΈμ λν΄ μμλ³΄μ.



- S3 λ μ μ  μΉμ¬μ΄νΈλ₯Ό νΈμ€ν ν  μ μκ³ , wwwμμ μ κ·Όμ΄ κ°λ₯νλλ‘ νμ©νλ©° μΉμ¬μ΄νΈ URLλ κ°λ¨νλ€.
- HTTP μλ ν¬μΈνΈλ μλμ κ°μ λͺ¨μ΅μ΄λ€.
  - <bucket-name>.s3-website-<AWS-region>.amazoneaws.com
  - λ²ν· μ΄λ¦μΌλ‘ μμνκ³ , μ€κ°μ region μ΄λ¦μ΄ λ€μ΄κ°κ² λλ€.



- μΉμ¬μ΄νΈλ₯Ό νμ±ν νμΌλ, 403 Forbidden μ€λ₯κ° λ°μνλ€λ©΄, λ²ν· μ μ±μ public read λ‘ λ³κ²½ν΄μΌ νλ€.



- μμ±ν S3 Buckets μ μΉμ¬μ΄νΈλ‘ νμ±ν

  - Bucket μ μ μ  μΉμ¬μ΄νΈλ‘ λ§λλ κ²
  - λ²ν· - μμ± - μ μ  μΉ μ¬μ΄νΈ νΈμ€ν

  ![image-20220727015141871](../../assets/images/posts/2022-07-28-AWS S3 (4) Websites/image-20220727015141871.png)



μ μ¬μ§μμ μ μ  μΉμ¬μ΄νΈ νΈμ€νμ νμ±νλ‘ λ³κ²½ν



![image-20220727015219546](../../assets/images/posts/2022-07-28-AWS S3 (4) Websites/image-20220727015219546.png)



- μμμ μΈλ±μ€λ¬Έμ, μ€λ₯ λ¬Έμ λ₯Ό λͺ¨λ μ§μ ν΄μ€λ€.

  - λ²ν·μ index.html, error.html νμΌμ λͺ¨λ μλ‘λν μνμ

- μμ±λ URL μ£Όμμ μ κ·Όνλ€.

  - 403 μλ¬κ° λνλ  κ²

- μλ¬ λ°μμ

  - ν΄λΉ Bucketμ public μνλ‘ λ°κΎΌλ€.

    1. Block public access λ₯Ό μ²΄ν¬ ν΄μ νλ€.
    2. λ²ν·μ μ±μμ Json λ¬Έμλ‘ λͺ¨λ μ μ κ° ν΄λΉ κ°μ²΄λ₯Ό getObject ν μμλ κΆνμ λ§λ λ€.

    ```json
    {
      "Id": "asdgasgasd",
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "asdfasdf",
          "Action": [
            "s3:GetObject"
          ],
          "Effect": "Allow",
          "Resource": "arn:aws:s3:::demo-my-bucket-name/*",
          "Principal": "*"
        }
      ]
    }
    ```

    

    