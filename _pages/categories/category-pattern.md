---
title: "🎸 코딩패턴 포스팅 모음"
layout: archive
permalink: /pattern/
author_profile: true
sidebar:
  nav: "docs"
---


{% assign posts = site.categories.pattern %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}