---
title: "🛠️ 데브옵스 포스팅 모음"
layout: archive
permalink: /devops/
author_profile: true
sidebar:
  nav: "docs"
---


{% assign posts = site.categories.devops %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}