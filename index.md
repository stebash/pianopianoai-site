---
layout: default
title: PianopianoAI
---

# Capire l'intelligenza artificiale, piano piano.

PianopianoAI racconta che cos'è l'intelligenza artificiale, come funziona e come usarla, con spiegazioni semplici, esempi concreti, a piccoli passi.

[Iscriviti alla newsletter](https://pianopianoai.substack.com){: .button }

## Ultimi articoli

<div class="articles-list">

{% for post in site.posts limit:6 %}

<article class="article-card">

{% if post.image %}
<a href="{{ post.url | relative_url }}">
<img src="{{ post.image | relative_url }}" alt="{{ post.title }}">
</a>
{% endif %}

<p class="article-date">
{{ post.date | date: "%d/%m/%Y" }}
</p>

<h2>
<a href="{{ post.url | relative_url }}">
{{ post.title }}
</a>
</h2>

{% if post.subtitle %}
<p>{{ post.subtitle }}</p>
{% endif %}

<a href="{{ post.url | relative_url }}">
Leggi →
</a>

</article>

{% endfor %}

</div>
