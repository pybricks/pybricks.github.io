---
title: "Driving the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with the Xbox Controller"
tags:
  - Technic
  - LEGO 42129
  - Steering Car
  - Remote Control
  - Xbox Controller
  - Block Coding
  - Python
header:
  teaser: /assets/images/project/42129/lego-technic-4x4-mercedes-benz-42129-xbox.jpg
  og_image: /assets/images/project/42129/lego-technic-4x4-mercedes-benz-42129-xbox-og.jpg
excerpt: >
  Control the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with
  the Xbox Controller. No phone needed!
---

In this project, we will show you how to control the LEGO® Technic 4x4
Mercedes-Benz Zetros Trial Truck (42129) with the Xbox Controller.

This is a fun way to drive the truck around without having to look at your
phone screen all time time. You can also use this setup to create your own
remote-controlled cars with Pybricks.

You'll also use the controller to lock and unlock the differentials.

{% include scaled.html
  path="/assets/images/project/42129/lego-technic-4x4-mercedes-benz-42129-xbox.jpg"
  caption="Driving the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129) with the Xbox Controller."
%}

# Requirements

To follow this project, you will need the following:

- {% include setlink.html id=42129 %}
- {% include setlink.html id="xbox" %} or {% include setlink.html id="xbox-elite-2" %}

See <a href="https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html#compatible-controllers" target="_blank">
this overview</a> for all compatible models.

# Understanding the code

This Technic truck drive motors on Ports A and B and has one steering motor on
Port D. It also has a DC Motor on Port C that controls the locking mechanism
for the differentials. The program starts by setting up these motors accordingly.


{% include block-program.html path="set_42129_xbox"
  caption="This program lets you drive the LEGO® Technic 4x4 Mercedes-Benz Zetros Trial Truck (42129)
  with the Xbox Controller. First, you set up the car, and then you can
  control the steering and power level using the analog inputs." %}

## Driving and steering

{% include snippets/xbox-car.md %}

{% include scaled.html
  path="/assets/images/project/42129/ex_steering.jpg"
  caption="Close up of the steering mechanism."
%}

## Locking and unlocking the differentials

The A button of the controller is used to lock and unlock the differentials.
When the differentials are locked, the truck will have better traction on rough
terrain. When they are unlocked, the truck can make tighter turns.

The locking mechanism is controlled by a DC Motor on Port C. Running it
clockwise unlocks the differentials, and running it counterclockwise locks
them.

Since this motor does not have position sensors, we use a variable to store the
current state of the differentials. The comments throughout the program explain
how this works.

{% include scaled.html
  path="/assets/images/project/42129/ex_main_lock.jpg"
  caption="Central differential lock mechanism."
%}

{% include scaled.html
  path="/assets/images/project/42129/ex_rear_lock.jpg"
  caption="Rear differential lock mechanism."
%}

{% include snippets/pybricks-intro.md %}

{% include snippets/xbox-pairing.md technic=true %}

# The truck in action

Operating the differentials with the Xbox controller is similar to operating it
with the [Powered Up remote](../technic-42129-powered-up-remote/#the-truck-in-action),
except you press the A button, and it rumbles instead of changing the light color.
Driving can be seen in example videos for
other [Technic trucks](../technic-42099-xbox/#the-truck-in-action).

{%
  include block-program-as-python.html
  show_intro=true
  path="set_42129_xbox"
%}


# More about the Zetros Trial Truck

The photographs in this article were contributed by Jim van Gulik. Used with
permission. For more great pictures of this set and details of its intricate 
mechanics, check out
Jim’s <a href="https://www.eurobricks.com/forum/index.php?/forums/topic/186660-review-42129-4x4-mercedes-benz-zetros-trial-truck/" target="_blank">review over at Eurobricks</a>.


