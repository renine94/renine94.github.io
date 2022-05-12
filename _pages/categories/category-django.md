---
title: "🚀 Django 포스팅 모음"
layout: archive
permalink: /django/
author_profile: true
sidebar:
  nav: "docs"
---


{% assign posts = site.categories.django %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}