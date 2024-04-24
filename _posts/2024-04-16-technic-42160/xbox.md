---
title: "Driving the LEGO® Technic Audi RS Q e-tron (42160) with the Xbox Controller"
tags:
  - Technic
  - LEGO 42160
  - Steering Car
  - Remote Control
  - Xbox Controller
  - Block Coding
  - Python
redirect_from:
  - /projects/sets/technic/42160-audi-rs-q-e-tron/xbox/
header:
  teaser: /project/lego-42160/lego-technic-audi-rs-q-e-tron-42160-xbox.jpg
  og_image: /project/lego-42160/lego-technic-audi-rs-q-e-tron-42160-xbox-og.jpg
excerpt: >
  Control the LEGO® Technic Audi RS Q e-tron (42160) with the Xbox
  Controller. Drive smoothly and precisely with the analog inputs.
---

In this project, we will show you how to control the LEGO® Technic Audi RS Q
e-tron (42160) with the Xbox Controller.

This is a fun way to drive the car around without having to look at your
phone screen all time time. You can use all of the analog inputs to drive,
which allows for smooth and precise control.

You can also use this setup to
create your own remote-controlled cars with Pybricks.

{% include scaled.html
  path="/project/lego-42160/lego-technic-audi-rs-q-e-tron-42160-xbox.jpg"
  caption="Driving the LEGO® Technic Audi RS Q e-tron (42160) with the Xbox Controller."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42160 %}
- {% include setlink.html id="xbox" %} or {% include setlink.html id="xbox-elite-2" %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.


# Understanding the code

This Technic car has one steering motor on Port D. It has drive motors on
Ports A and B. Both have to run _clockwise_ to move the car
_forward_. The program starts by setting up these motors accordingly.

{% include block-program.html path="set_42160_xbox"
  caption="This program lets you drive the LEGO® Technic Technic Audi RS Q e-tron (42160)
  with the Xbox Controller. First, you set up the car, and then you can
  control the steering and power level using the analog inputs." %}

{% include snippets/xbox-car.md %}

{% include snippets/pybricks-intro.md %}

{% include snippets/xbox-pairing.md technic=true %}

# The car in action

When you're ready, you can drive the car as shown below!

{% include youtube.html videoid="LmqpK32jrCs" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42160_xbox"
%}




