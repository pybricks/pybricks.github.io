---
title: "Driving the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with the Powered Up Remote"
tags:
  - Technic
  - LEGO 42129
  - Steering Car
  - Remote Control
  - Powered Up Remote
  - Block Coding
  - Python
redirect_from:
  - /projects/sets/technic/42129-mercedes-benz-zetros/powered-up-remote/
header:
  teaser: /project/lego-42129/lego-technic-4x4-mercedes-benz-42129-powered-up.jpg
  og_image: /project/lego-42129/lego-technic-4x4-mercedes-benz-42129-powered-up-og.jpg
excerpt: >
  Control the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with
  the Powered Up Remote. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic 4x4
Mercedes-Benz Zetros Trial Truck (42129) with the Powered Up (Train) Remote.

This is a fun way to drive the truck around without having to look at your
phone screen all time time. You can also use this setup to create your own
remote-controlled cars with Pybricks.

You'll also use the remote to lock and unlock the differentials.

{% include scaled.html
  path="/project/lego-42129/lego-technic-4x4-mercedes-benz-42129-powered-up.jpg"
  caption="Driving the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with the Powered Up Train Remote."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42129 %}
- {% include setlink.html id=88010 %}

# Understanding the code

This Technic truck drive motors on Ports A and B and has one steering motor on
Port D. It also has a DC Motor on Port C that controls the locking mechanism
for the differentials. The program starts by setting up these motors accordingly.


{% include block-program.html path="set_42129_pup_remote"
  caption="This program lets you drive the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129)
  with the Powered Up Remote. First, you set up the car, and then you can
  control the steering and power level using the buttons on the remote." %}

## Driving and steering

{% include snippets/pup-remote-car.md %}

{% include scaled.html
  path="/project/lego-42129/ex_steering.jpg"
  caption="Close up of the steering mechanism."
%}

## Locking and unlocking the differentials

The center button of the remote is used to lock and unlock the differentials.
When the differentials are locked, the truck will have better traction on rough
terrain. When they are unlocked, the truck can make tighter turns.

The locking mechanism is controlled by a DC Motor on Port C. Running it
clockwise unlocks the differentials, and running it counterclockwise locks
them.

Since this motor does not have position sensors, we use a variable to store the
current state of the differentials. The comments throughout the program explain
how this works.

{% include scaled.html
  path="/project/lego-42129/ex_main_lock.jpg"
  caption="Central differential lock mechanism."
%}

{% include scaled.html
  path="/project/lego-42129/ex_rear_lock.jpg"
  caption="Rear differential lock mechanism."
%}

{% include snippets/pybricks-intro.md %}

# The truck in action

When you're ready, you can drive the truck as shown below. Make sure to turn
on the remote when you start the truck program, so that the hub can find it.

{% include youtube.html videoid="-YuvEUQPGnM" %}

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42129_pup_remote"
%}


# More about the Zetros Trial Truck

The photographs in this article were contributed by Jim van Gulik. Used with
permission. For more great pictures of this set and details of its intricate 
mechanics, check out
Jim’s <a href="https://www.eurobricks.com/forum/index.php?/forums/topic/186660-review-42129-4x4-mercedes-benz-zetros-trial-truck/" target="_blank">review over at Eurobricks</a>.


