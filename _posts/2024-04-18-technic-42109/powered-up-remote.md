---
title: "Driving the LEGO® Technic Top Gear Rally Car (42109) with the Powered Up Remote"
tags:
  - Technic
  - LEGO 42109
  - Steering Car
  - Remote Control
  - Powered Up Remote
  - Block Coding
  - Python
header:
  teaser: /project/lego-42109/lego-technic-top-gear-rally-car-42109-powered-up.jpg
  og_image: /project/lego-42109/lego-technic-top-gear-rally-car-42109-powered-up-og.jpg
excerpt: >
  Control the LEGO® Technic Top Gear Rally Car (42109) with the Powered Up
  Remote. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic Top Gear
Rally Car (42109) with the Powered Up (Train) Remote.

This is a fun way to drive the car around without having to look at your
phone screen all time time. You can also use this setup to create your own
remote-controlled cars with Pybricks.

{% include scaled.html
  path="/project/lego-42109/lego-technic-top-gear-rally-car-42109-powered-up.jpg"
  caption="Driving the LEGO® Technic Top Gear Rally Car (42109) with the Powered Up Train Remote."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42109 %}
- {% include setlink.html id=88010 %}

# Understanding the code

This Technic car has one steering motor on Port B and a drive motor on
Port D. The program starts by setting up these motors accordingly.

{% include block-program.html path="set_42109_pup_remote"
  caption="This program lets you drive the LEGO® Technic Technic Top Gear Rally Car (42109)
  with the Powered Up Remote. First, you set up the car, and then you can
  control the steering and power level using the buttons on the remote." %}

{% include snippets/pup-remote-car.md %}

{% include snippets/pybricks-intro.md %}

# The car in action

When you're ready, you can drive the car as shown below. Make sure to turn
on the remote when you start the car program, so that the hub can find it.

{% include youtube.html videoid="ChDXympeNAU" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42109_pup_remote"
%}




