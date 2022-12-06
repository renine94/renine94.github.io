---
layout: single

header:
  teaser: /assets/images/logo/django.png
  overlay_image: /assets/images/logo/django.png
  overlay_filter: linear-gradient(rgba(255, 0, 0, 0.5), rgba(0, 255, 255, 0.5))
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Github"
      url: "https://github.com/renine94"

title: "[Gunicorn] 구니콘 최적화를 통한 성능 향상 시도하기"
excerpt: "🚀 gunicorn, pre-fork, gevent, wsgi"

categories: django
tag: [django, gunicorn, pre-fork, gevent, wsgi, async]

toc: true
toc_label: "📕 목차"
toc_icon: "null"
toc_sticky: true

sidebar:
  nav: "docs"
---



사내 Slack 에서 인프라 채널팀 대화에서 다음과 같은 내용이 흘러들어왔다.

```python
24xlarge의 경우 vCPU 96, memory 192 인데 4대면 cpu 384, memory 768가 됩니다.
현재 테스트 결과 gunicorn worker 15개로 하는경우 대략 3G정도 메모리를 사용하는데
pod을 70개로 셋팅해도 210G로 메모리 유휴가 많은듯해서 더 최적의 조합을 테스트해볼수는 있을듯합니다.
```

위 대화에서 나온 Gunicorn worker 에 대한 궁금증에 생기기도 했고, 평소 인프라에도 관심을 두는터라 해당 내용을 찾아 포스팅해보려 한다.



참조 블로그

- [김징어의 Devlog](https://kimjingo.tistory.com/81){: .btn .btn--danger}
- [Better performance by optimizing Gunicorn config](https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7){: .btn .btn--danger}

# Gunicorn

> Pass
