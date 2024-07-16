---
title: "SPIKE Essential StarterBot"
excerpt: >
  Learn to build a vehicle robot with SPIKE Essential with a hub and two motors.
header:
  teaser: /learn/building-a-robot/spike-essential/starterbot-essential.jpg
---


{% include scaled.html path="/learn/building-a-robot/spike-essential/starterbot-essential.jpg" %}

You can build this version of StarterBot with just the elements in the {%
include setlink.html id=45345 %} base set.

If you prefer, you can also use any of the two-wheeled vehicles from the base
set.

# Adapting the lessons

All coding techniques in this guide also apply to SPIKE Essential. You can use
the same code blocks. But since this hub has only two ports, you cannot drive
with two motors and use the Color Sensor at the same time.

You can still follow most of the early chapters concerning driving and
navigation without many changes. For lessons about sensors, you can modify
the examples to use only one motor.

For example, instead of making a robot drive until a colored line, you could
make a motor spin until the color sensor detects a certain color. This way, you
can still learn about most sensor techniques.

# Instructions

<figure class="half">
{% for i in (1..9) %}
      <a href="/learn/building-a-robot/spike-essential/starterbot-essential-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/spike-essential/starterbot-essential-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>
