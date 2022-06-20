---
title: "🖥 IT 포스팅 모음"
layout: archive
permalink: /it/
author_profile: true
sidebar:
  nav: "docs"
---


{% assign posts = site.categories.it %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}