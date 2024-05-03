---
title: "Operating the LEGO® Technic Liebherr Crawler Crane LR 13000 (42146) with the Powered Up Remote"
tags:
  - Technic
  - LEGO 42146
  - Remote Control
  - Powered Up Remote
  - Block Coding
  - Hub to Hub Communication
  - Python
header:
  teaser: /project/lego-42146/lego-technic-liebherr-crane-42146-powered-up.jpg
  og_image: /project/lego-42146/lego-technic-liebherr-crane-42146-powered-up-og.jpg
excerpt: >
  Control the LEGO® Technic Liebherr Crawler Crane (42146) with
  the Powered Up remote. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic Liebherr
Crawler Crane (42146) with the Powered Up (Train) Remote.

This gives you precise control over each of the crane's functions without
having to use a phone or tablet. You can drive it around with the red and grey
buttons, and use the green button to switch between controlling the base and
the crane functions.

This crane has two hubs, so we'll also show you how to connect them via Bluetooth.

{% include scaled.html
  path="/project/lego-42146/lego-technic-liebherr-crane-42146-powered-up.jpg"
  caption="Driving the LEGO® Technic Liebherr Crawler Crane (42146) with the Powered Up remote."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42146 %}
- {% include setlink.html id=88010 %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.

# Understanding the code

This project has two programs, one for each hub. The hub in the base connects
to the Powered Up remote and drives the vehicle. It also calculates the required
speeds of the crane functions based on your input, and broadcasts these to the
other hub in the crane.

The crane hub receives these messages and controls the crane functions
accordingly. While the order of installation doesn't matter, it's practical
to download and run the crane program first. Because it simply starts and stops
the crane functions based on the incoming signals, you can customize all the
actions in the program for the hub in the base instead.

When sending numbers, communication works best if you send small numbers. So
we just send the speed values as percentages, and multiply them by
a factor in the crane program to get the desired speed.

{% include block-program.html path="set_42146_crane"
  no_program_link=true
  width="75%"
  caption="The program for the hub in the crane receives three values and sets the crane motor speed functions accordingly." %}

{% include block-program.html path="set_42146_base_xbox"
  caption="The program for the hub in the base receives the Powered Up remote input, drives and turns the base, and broadcasts the required speeds for the crane functions to the other hub. Switch to crane mode with the green button." %}

{% include snippets/pybricks-intro.md %}

In this project, you have two hubs. Installation works the same for both.
During installation, you can give each hub a unique name such as `Base` or
`Crane`, which makes it easier to tell them apart when you connect later.

# The crane in action

When you're ready, you can operate the crane as shown below!

Communication between the two hubs works best if you disconnect them from your
computer.

{% include youtube.html videoid="PmV8tBAQz5U" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42146_crane"
  caption="Program for the crane hub."
%}

{%
  include block-program-as-python.html
  show_intro=false
  path="set_42146_base_pup_remote"
  caption="Program for the base hub."
%}
