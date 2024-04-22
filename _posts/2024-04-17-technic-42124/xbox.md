---
title: "Driving the LEGO® Technic Off-Road Buggy (42124) with the Xbox Controller"
tags:
  - Technic
  - LEGO 42124
  - Steering Car
  - Remote Control
  - Xbox Controller
  - Block Coding
  - Python
redirect_from:
  - /projects/sets/technic/42124-off-road-buggy/xbox/
header:
  teaser: /assets/images/project/42124/lego-technic-off-road-buggy-42124-xbox.jpg
  og_image: /assets/images/project/42124/lego-technic-off-road-buggy-42124-xbox-og.jpg
excerpt: >
  Control the LEGO® Technic Off-Road Buggy (42124) with the Xbox
  Controller. Drive smoothly and precisely with the analog inputs.
---

In this project, we will show you how to control the LEGO® Technic Off-Road Buggy (42124) with the Xbox Controller.

This is a fun way to drive the car around without having to look at your
phone screen all time time. You can use all of the analog inputs to drive,
which allows for smooth and precise control.

You can also use this setup to
create your own remote-controlled cars with Pybricks.

{% include scaled.html
  path="/assets/images/project/42124/lego-technic-off-road-buggy-42124-xbox.jpg"
  caption="Driving the LEGO® Technic Off-Road Buggy (42124) with the Xbox Controller."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42124 %}
- {% include setlink.html id="xbox" %} or {% include setlink.html id="xbox-elite-2" %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.


# Understanding the code

This Technic car has one steering motor on Port B and a drive motor on
Port A. The drive motor has to run _counterclockwise_ to move the car
_forward_. The program starts by setting up these motors accordingly.


{% include block-program.html path="set_42124_xbox"
  caption="This program lets you drive the LEGO® Technic Technic Off-Road Buggy (42124)
  with the Xbox Controller. First, you set up the car, and then you can
  control the steering and power level using the analog inputs." %}

{% include snippets/xbox-car.md %}

{% include snippets/pybricks-intro.md %}

{% include snippets/xbox-pairing.md technic=true %}

# The car in action

When you're ready, you can drive the car as shown below!

{% include youtube.html videoid="JpVR_UQvefI" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42124_xbox"
%}




