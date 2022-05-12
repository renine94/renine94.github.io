---
title: "Django"
layout: archive
permalink: /django/
author_profile: true
sidebar:
  nav: "docs"
---


{% assign posts = site.categories.Cpp %}
{% for post in posts %} {% include archive-single.html type=page.entries_layout %} {% endfor %}