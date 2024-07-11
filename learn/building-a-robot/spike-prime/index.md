---
title: "SPIKE Prime StarterBot"
excerpt: >
  Learn to build a vehicle robot with SPIKE Prime. Use the hub buttons as extra
  sensors and combine them with the color sensor and ultrasonic sensor.
starter_bot_prime:
  image: /learn/building-a-robot/spike-prime/starterbot-prime.png
  alt: The StarterBot with SPIKE Prime.
  caption: >
    The StarterBot is very effective at avoiding obstacles. The left and
    right bumpers press the buttons on the hub when running into an obstacle
    that the Ultrasonic Sensor did not see. This robot can also follow lines
    or square the line with the Color Sensor.
  width: 100%
  labels:
    - text: Color Sensor
      x: 70%
      y: 80%
      location: right
    - text: Ultrasonic Sensor
      x: 47%
      y: 5%
      location: right
    - text: SPIKE Prime Hub
      x: 47%
      y: 25%
      location: right
    - text: Left bumper
      x: 78%
      y: 60%
      location: right
    - text: Right bumper
      x: 35%
      y: 95%
      location: left
    - text: Right motor
      x: 32%
      y: 60%
      location: left
    - text: Left motor
      x: 63%
      y: 50%
      location: right
---

The SPIKE Prime version of the StarterBot has everything you need to
follow along with the lessons and activities in this guide.

You'll start by building a drive base and you'll add various sensor attachments
along the way. This robot makes creative use of the SPIKE Prime left and right
buttons to create working bumpers that can independently detect obstacles in
its path.

This provides lots of interesting learning opportunities, such as monitoring
multiple sensors at the same time.

{% include diagram.html data=page.starter_bot_prime %}

You can build this version of StarterBot with just the elements in the {%
include setlink.html id=45678 %} base set.

# Building the base

This sturdy base consists of just the hub and two motors. Each motor drives a
wheel and a ball caster in the back is used for support. You can use this drive
base throughout chapters 3 and 4 to learn the basics of programming and robot
navigation.

<figure class="half">
{% for i in (1..13) %}
      <a href="/learn/building-a-robot/spike-prime/starterbot-prime-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/spike-prime/starterbot-prime-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>

# Adding the distance sensor

The Ultrasonic Sensor measures distance. You'll use it to learn the essentials
of working with sensors. You can build it now, or return here when you get to
chapter 5 and onwards.

<figure class="half">
{% for i in (14..17) %}
      <a href="/learn/building-a-robot/spike-prime/starterbot-prime-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/spike-prime/starterbot-prime-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>

# Adding the color sensor and bumpers

This attachment includes the Color Sensor for line following and line squaring.
It also has two bumpers that press the left and right buttons on the hub when
the robot runs into an obstacle.

You can build it now, but it's better to leave it unattached
until you get to chapter 6 and onwards.

<figure class="half">
{% for i in (18..26) %}
      <a href="/learn/building-a-robot/spike-prime/starterbot-prime-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/spike-prime/starterbot-prime-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>
