---
title: "Driving the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Powered Up Remote"
tags:
  - Technic
  - LEGO 42099
  - Steering Car
  - Remote Control
  - Powered Up Remote
  - Block Coding
  - Python
redirect_from:
  - /projects/sets/technic/42099-off-roader/powered-up-remote/
header:
  teaser: /assets/images/project/42099/lego-technic-4x4-xtreme-off-roader-42099-powered-up.jpg
  og_image: /assets/images/project/42099/lego-technic-4x4-xtreme-off-roader-42099-powered-up-og.jpg
excerpt: >
  Control the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Powered Up
  Remote. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic 4X4 X-treme
Off-Roader (42099) with the Powered Up (Train) Remote.

This is a fun way to drive the truck around without having to look at your
phone screen all time time. You can also use this setup to create your own
remote-controlled cars with Pybricks.

{% include scaled.html
  path="/assets/images/project/42099/lego-technic-4x4-xtreme-off-roader-42099-powered-up.jpg"
  caption="Driving the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Powered Up Train Remote."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42099 %}
- {% include setlink.html id=88010 %}

# Understanding the code

This Technic truck has one steering motor on Port C. It has drive motors on
Ports A and B. Both have to run _counterclockwise_ to move the truck
_forward_. The program starts by setting up these motors accordingly.

{% include block-program.html path="set_42099_pup_remote"
  caption="This program lets you drive the LEGO® Technic 4X4 X-treme Off-Roader (42099)
  with the Powered Up Remote. First, you set up the car, and then you can
  control the steering and power level using the buttons on the remote." %}

{% include snippets/pup-remote-car.md %}

{% include snippets/pybricks-intro.md %}

# The truck in action

When you're ready, you can drive the truck as shown below. Make sure to turn
on the remote when you start the truck program, so that the hub can find it.

{% include youtube.html videoid="eUNr36tyokc" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42099_pup_remote"
%}




