---
title: "Driving the LEGO® Technic 4X4 X-treme Off-Roader (42099) with the Powered Up Remote"
last_modified_at: 2021-03-09T16:20:02-05:00
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

The car setup block takes care of centering the steering motor and makes it
easy to drive later on. Finally, we add the setup block for the Powered Up
remote.

{% include block-program.html path="set_42099_pup_remote"
  caption="This program lets you drive the LEGO® Technic 4X4 X-treme Off-Roader (42099)
  with the Powered Up Remote. First, you set up the car, and then you can
  control the steering and power level using the buttons on the remote." %}

The main program is quite simple. There is an infinite loop that sets the
steering and drive power based on the buttons you press. It uses the _ternary
block_ to set the steering to:
- 100% when you press the left **+** button,
- otherwise to -100% when you press the left **-** button,
- otherwise to 0%

Similarly, it sets the drive power to:
- 100% when you press the right **+** button,
- otherwise to -100% when you press the right **-** button,
- otherwise to 0%

You could achieve the same effect using conventional if-else blocks. You can
see this in the video below. The ternary block makes the code more compact and
easier to read.

{% include pybricks-intro.md %}

# The truck in action

When you're ready, you can drive the truck as shown below. Make sure to turn
on the remote when you start the truck program, so that the hub can find it.

{% include youtube.html videoid="eUNr36tyokc" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42099_pup_remote"
%}




