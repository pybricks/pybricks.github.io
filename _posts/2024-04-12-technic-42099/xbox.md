---
title: "Driving the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Xbox Controller"
tags:
  - Technic
  - LEGO 42099
  - Steering Car
  - Remote Control
  - Xbox Controller
  - Block Coding
  - Python
header:
  teaser: /project/lego-42099/lego-technic-4x4-xtreme-off-roader-42099-xbox.jpg
  og_image: /project/lego-42099/lego-technic-4x4-xtreme-off-roader-42099-xbox-og.jpg
excerpt: >
  Control the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Xbox
  Controller. Drive smoothly and precisely with the analog inputs.
---

In this project, we will show you how to control the LEGO® Technic 4X4 X-treme
Off-Roader (42099) with the Xbox Controller.

This is a fun way to drive the truck around without having to look at your
phone screen all time time. You can use all of the analog inputs to drive,
which allows for smooth and precise control.

You can also use this setup to
create your own remote-controlled cars with Pybricks.

{% include scaled.html
  path="/project/lego-42099/lego-technic-4x4-xtreme-off-roader-42099-xbox.jpg"
  caption="Driving the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Xbox Controller."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42099 %}
- {% include setlink.html id="xbox" %} or {% include setlink.html id="xbox-elite-2" %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.

# Understanding the code

This Technic truck has one steering motor on Port C. It has drive motors on
Ports A and B. Both have to run _counterclockwise_ to move the truck
_forward_. The program starts by setting up these motors accordingly.

{% include block-program.html path="set_42099_xbox"
  caption="This program lets you drive the LEGO® Technic 4X4 X-treme Off-Roader (42099)
  with the Xbox Controller. First, you set up the car, and then you can
  control the steering and power level using the analog inputs." %}

{% include snippets/xbox-car.md %}

{% include snippets/pybricks-intro.md %}

{% include snippets/xbox-pairing.md technic=true %}

# The truck in action

When you're ready, you can drive the truck as shown below!

{% include youtube.html videoid="VNWHJSq6h14" %}

{% include snippets/xbox-further-exploration.md %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42099_xbox"
%}




