---
title: "Driving the LEGO® Technic Cat D11 Bulldozer (42131) with the Powered Up Remote"
tags:
  - Technic
  - LEGO 42131
  - Remote Control
  - Powered Up Remote
  - Block Coding
  - Python
redirect_from:
  - /projects/sets/technic/42131-cat-bulldozer/powered-up-remote/
header:
  teaser: /project/lego-42131/lego-technic-cat-d11-bulldozer-42131-powered-up.jpg
  og_image: /project/lego-42131/lego-technic-cat-d11-bulldozer-42131-powered-up-og.jpg
excerpt: >
  Control the LEGO® Technic Cat D11 Bulldozer (42131) with
  the Powered Up Remote. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic Cat D11
Bulldozer (42131) with the Powered Up (Train) Remote.

This is a fun way to drive the bulldozer around without having to look at your
phone screen all time time. You'll also use the remote to switch between the
functions of the blade, ripper, and ladder.

{% include scaled.html
  path="/project/lego-42131/lego-technic-cat-d11-bulldozer-42131-powered-up.jpg"
  caption="Driving the LEGO® Technic Cat D11 Bulldozer (42131) with the Powered Up Train Remote."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42131 %}
- {% include setlink.html id=88010 %}

# Understanding the code

The program consists of two main tasks that run in parallel. The first task
handles the driving and steering of the bulldozer, as well as powering the
function motor.

The second task controls the position of the motor that selects which function
is being operated. The details are included as comments in the program below.

When the program begins, it resets the function selector to the zero position,
corresponding to the blade up and down movement. You can select any function
by pressing the *green button* along with one of the gray buttons. This will
change the remote light and switch the function selector as follows:

* Left ＋ (blue): Moves the blade up and down.
* Left − (red): Tilts the blade back and forth.
* Right ＋ (yellow): Moves the ladder up and down.
* Right − (green): Moves the ripper up and down.

Once the function is selected, use the red buttons to control the motor that
powers the selected function.

Use the gray buttons to control the tracks. You can change
the drive acceleration in the main program to a lower value to make the
vehicle start and stop driving more gradually. You can also change the speed
values corresponding the `left` and `right` motor blocks.

{% include block-program.html path="set_42131_pup_remote"
  caption="This program lets you drive the LEGO® Technic Cat D11 Bulldozer (42131)
  with the Powered Up Remote." %}

{% include snippets/pybricks-intro.md %}

# The bulldozer in action

When you're ready, you can drive the bulldozer as shown below. Make sure to turn
on the remote when you start the bulldozer program, so that the hub can find it.

{% include youtube.html videoid="N7OmW-7u8fA" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42131_pup_remote"
%}



