---
layout: single

header:
  teaser: /assets/images/logo/elasticSearch.png
  overlay_image: /assets/images/logo/elasticSearch.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[ES] Object, Nested, Multi-Field 의 차이점을 알아보자."
excerpt: "🚀 ES에서 사용되는 필드 타입중에 헷갈리는 요소들을 정리하고자 합니다."

categories: elasticSearch
tag: [es, elasticSearch, elk, search, fields, nested]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# ES Field Data Type 비교
> Object, Nested, Multi-Field 간의 차이점에 대해 알아보자

- 참고 블로그
  - [Opster - 2022.11 최신 포스팅](https://opster.com/guides/elasticsearch/data-architecture/elasticsearch-nested-field-object-field/){: .btn .btn--danger}
  - [공식문서 번역한 벨로그](https://velog.io/@rudaks94/elasticsearch-nested-field-type){: .btn .btn--success}



관련 영상입니다.
{: .notice--danger}

{% include video id="yqAKfwGZpE0" provider="youtube" %}

---

# Object

- Object Type 은 값이 여러 필드를 포함할 수 있는 필드를 가질 수 있습니다.
- doc으로 저장되는 데이터가 평탄화(flatten) 작업이 되어서 저장된다.
- query 시 원하는 데이터가 나오지 않을 가능성이 있습니다.





# Nested

> nested 로 생성된 fields 에 doc 데이터를 넣으면 각각 서로 다른 색인을 거쳐서 독립된 doc 으로 저장된다.





# Multi-Fields

> field 마다 서로 다른 Analyzer 를 설정할 수 있다.

