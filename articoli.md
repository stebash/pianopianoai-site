---
layout: default
title: Articoli
permalink: /articoli/
---

# Articoli

{% for post in site.posts %}

## [{{ post.title }}]({{ post.url | relative_url }})

{{ post.date | date: "%d/%m/%Y" }}

{% if post.subtitle %}
{{ post.subtitle }}
{% endif %}

---

{% endfor %}
