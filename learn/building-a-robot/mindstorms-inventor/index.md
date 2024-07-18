---
title: "MINDSTORMS StarterBot"
excerpt: >
  Learn to build a vehicle robot with MINDSTORMS Robot Inventor. Use the hub buttons as extra
  sensors and combine them with the color sensor and ultrasonic sensor.
header:
  teaser: /learn/building-a-robot/mindstorms-inventor/starterbot-mindstorms-inventor.jpg
starter_bot_inventor:
  image: /learn/building-a-robot/mindstorms-inventor/starterbot-mindstorms-inventor.jpg
  alt: The StarterBot with MINDSTORMS Robot Inventor.
  caption: >
    The StarterBot is very effective at avoiding obstacles. The left and
    right bumpers press the buttons on the hub when running into an obstacle
    that the Ultrasonic Sensor did not see. This robot can also follow lines
    or square the line with the Color Sensor.
  width: 100%
  labels:
    - text: Color Sensor
      x: 30%
      y: 80%
      location: left
    - text: Ultrasonic Sensor
      x: 65%
      y: 15%
      location: right
    - text: Inventor Hub
      x: 62%
      y: 35%
      location: right
    - text: Left bumper
      x: 50%
      y: 80%
      location: right
    - text: Right bumper
      x: 30%
      y: 65%
      location: left
    - text: Right motor
      x: 30%
      y: 52%
      location: left
    - text: Left motor
      x: 63%
      y: 60%
      location: right
---

The MINDSTORMS Robot Inventor version of the StarterBot has everything you need to
follow along with the lessons and activities in this guide.

You'll start by building a drive base and you'll add various sensor attachments
along the way. This robot makes creative use of the left and right hub
buttons to create working bumpers that can independently detect obstacles in
its path.

This provides lots of interesting learning opportunities, such as monitoring
multiple sensors at the same time.

{% include diagram.html data=page.starter_bot_inventor %}

You can build this version of StarterBot with just the elements in the {%
include setlink.html id=51515 %} set.

This design is almost entirely the same as
the [SPIKE Prime](/learn/building-a-robot/spike-prime/) version,
but it uses a swivel wheel instead of a ball caster.

# Building the base

This sturdy base consists of just the hub and two motors. Each motor drives a
wheel and a ball caster in the back is used for support. You can use this drive
base throughout chapters 3 and 4 to learn the basics of programming and robot
navigation.

<figure class="half">
{% for i in (1..14) %}
      <a href="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>

# Adding the distance sensor

The Ultrasonic Sensor measures distance. You'll use it to learn the essentials
of working with sensors. You can build it now, or return here when you get to
chapter 5 and onwards.

<figure class="half">
{% for i in (15..18) %}
      <a href="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
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
{% for i in (19..27) %}
      <a href="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-{{ i | prepend: '0' | slice: -2, 2 }}.png">
          <img src="/learn/building-a-robot/mindstorms-inventor/starterbot-inventor-thumb-{{ i | prepend: '0' | slice: -2, 2 }}.png">
      </a>
  {% endfor %}
</figure>

# Setup blocks

If you use the design shown above, you can use the following setup blocks in
your program. This can be a useful starting point for many of your programs.

Don't worry if you're not sure what each of these blocks do. We'll introduce
them one by one in the next chapters.

{% include block-program.html
path="setup_prime"
caption="Setup blocks for the MINDSTORMS StarterBot. This it drive in a square."
%}
