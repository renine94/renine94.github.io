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

title: "[aws] S3 Advanced (6) - Analytics"
excerpt: "🚀 S3 Analytics 를 사용하여 언제 객체를 이동시킬지 알아내자!"

categories: aws
tag: [aws, s3, analytics, standard]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"


---

# S3 Analytics



Standard 로부터 Standard_IA 로 언제 객체를 보낼지 결정하기 위해 S3 Analytics를 활용할 수 있다.<br>즉, 며칠 후에 객체를 보내는 것이 가장 좋을지 계산하는 것이다.

- Onezone_IA 또는 Glacier 에 대해서는 작동하지 않는다.
- 오직, Standard 로부터 Standard_IA로 작동한다.
- 보고서는 매일(하루마다) 업데이트 된다.
- 처음 활성화 하면 첫 시작까지 24~48시간이 소요된다.



- 며칠 후에 Standard --> Standard_IA 로 객체를 이동시키는 것이 현명할지 알아내기 위해 S3 Analytics 기능을 사용하는 것



끗!