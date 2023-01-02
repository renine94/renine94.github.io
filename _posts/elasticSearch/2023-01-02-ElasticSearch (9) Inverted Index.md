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

title: "[ES] 역색인 구조에 대해 알아보자"
excerpt: "🚀 ES 에서 데이터를 저장하는 방식인 역색인 구조에 대해 알아본다."

categories: elasticSearch
tag: [es, elasticSearch, inverted index]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---

# Inverted Index

> 역 인덱스.
>
> 출처 : [참조블로그](https://esbook.kimjmin.net/06-text-analysis/6.1-indexing-data)



일반적으로 오라클이나 RDBMS 같은 관계형 DB 에서는 데이터를 테이블 구조로 저장하게 되는데, 테이블에서 특정컬럼에 `fox` 라는 단어가 포함된 행들을 가져온다고 하면 컬럼을 한 줄 씩 찾아 내려가면서 `fox` 가 있으면 가져오고 없으면 넘어가는식으로 가져오게 된다.

![es](../../assets/images/posts/2023-01-02-ElasticSearch (9) Inverted Index/assets%2F-Ln04DaYZaDjdiR_ZsKo%2F-Lo--uX4jUMQUTUvBgeF%2F-LntIdlIDXEduASJCXRm%2F6.1-02.png)



- DB
  - `like` 검색을 사용하기 때문에 데이터가 늘어날수록 검색해야 할 대상이 늘어남
  - 시간이 오래 걸린다.
  - row 안에 내용을 모두 읽어야 하기 때문에, 기본적으로 속도가 느리다.
- ES
  - 데이터를 저장할 때 **역 인덱스(inverted index)** 구조를 만들어 저장

<br>

---



역인덱스 저장 방식

![img](../../assets/images/posts/2023-01-02-ElasticSearch (9) Inverted Index/assets%2F-Ln04DaYZaDjdiR_ZsKo%2F-LntL_BGpuFbNXy_sFtK%2F-LntLbibpXHABupWvXtu%2F6.1-03.png)



- **역 인덱스**는 책의 맨 뒤에 있는 주요 키워드에 대한 내용이 몇 페이지에 있는지 볼 수 있는 **찾아보기 페이지에 비유**할 수 있다.
- ES 에서 추출된 각 키워드를 **텀(Term)** 이라고 부른다.
- 역 인덱스가 있으면 `fox` 를 포함하고 있는 도큐먼트들의 id를 바로 얻어올 수 있다.



![img](../../assets/images/posts/2023-01-02-ElasticSearch (9) Inverted Index/assets%2F-Ln04DaYZaDjdiR_ZsKo%2F-LntS3nPGQlmuCtaIVJt%2F-LntS6M5Y65sfxz435rP%2F6.1-04.png)





- ES 는 데이터가 늘어나도 찾아가야 할 행이 늘어나는것이 아니라, 역 인덱스가 가리키는 id의 배열값이 추가되는 것 뿐
- 큰 속도 저하 없이 빠른 속도로 검색이 가능하다



역 인덱스는 데이터가 저장되는 과정에서 만들기 때문에 ES 는 데이터를 입력할 때 저장이 아닌 **색인**을 한다고 표현한다.
{: .notice--danger}













