---
title: "Driving the LEGO® Technic Cat D11 Bulldozer (42131) with the Xbox Controller"
tags:
  - Technic
  - LEGO 42131
  - Steering Car
  - Remote Control
  - Xbox Controller
  - Block Coding
  - Python
header:
  teaser: /project/lego-42131/lego-technic-cat-d11-bulldozer-42131-xbox.jpg
  og_image: /project/lego-42131/lego-technic-cat-d11-bulldozer-42131-xbox-og.jpg
excerpt: >
  Control the LEGO® Technic Cat D11 Bulldozer (42131) with
  the Xbox Controller. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic Cat D11
Bulldozer (42131) with the Xbox Controller.

This is a fun way to drive the bulldozer around without having to look at your
phone screen all time time. You'll also use the controller to switch between the
functions of the blade, ripper, and ladder.

{% include scaled.html
  path="/project/lego-42131/lego-technic-cat-d11-bulldozer-42131-xbox.jpg"
  caption="Driving the LEGO® Technic Cat D11 Bulldozer (42131) with the Xbox Controller."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42131 %}
- {% include setlink.html id="xbox" %} or {% include setlink.html id="xbox-elite-2" %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.

# Understanding the code

The program consists of two main tasks that run in parallel. The first task
handles the driving and steering of the bulldozer, as well as powering the
function motor.

The second task controls the position of the motor that selects which function
is being operated. The details are included as comments in the program below.

When the program begins, it resets the function selector to the zero position,
corresponding to the blade up and down movement. You can select any function
by pressing the *A/B/X/Y* buttons. This will switch the function selector as follows:

* X (blue): Moves the blade up and down.
* B (red): Tilts the blade back and forth.
* Y (yellow): Moves the ladder up and down.
* A (green): Moves the ripper up and down.

Once the function is selected, use the bumper buttons to control the motor that
powers the selected function.

Use the direction pad to control the tracks. You can change
the drive acceleration in the main program to a lower value to make the
vehicle start and stop driving more gradually. You can also change the speed
values corresponding the `left` and `right` motor blocks.

{% include block-program.html path="set_42131_xbox"
  caption="This program lets you drive the LEGO® Technic Cat D11 Bulldozer (42131)
  with the Xbox Controller." %}

{% include snippets/pybricks-intro.md %}

{% include snippets/xbox-pairing.md technic=true %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42131_xbox"
%}
