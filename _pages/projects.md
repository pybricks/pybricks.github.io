---
permalink: /projects/
title: "Pybricks Projects"
toc: false
layout: single
---

<p>
{% for tpage in site.pages %}
    {% if tpage.url contains "/_pages/" %}
    {% else %}
    {% if tpage.url contains "/projects/sets" %}
        
        <a href="{{ tpage.url}}">
        
        <h2>{{tpage.title}}</h2>
        <img src="/_pages/{{ tpage.permalink }}{{ tpage.image.local }}" width="400">     
        
        
        </a>
        <br/>
        
        <br/>
        {{ tpage.description }}

    {% endif %}
    {% endif %}
{% endfor %}
</p>

