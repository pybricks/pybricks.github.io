---
title: How to create force feedback with the Xbox Controller
tags:
  - Block Coding
  - Python
  - Technic
  - SPIKE Prime
  - SPIKE Essential
  - Xbox Controller
  - Remote Control
toc: true
excerpt: >
  With full control over the builtin rumble actuators, you can create force
  feedback with the Xbox Controller to respond to sensors on your robot.
header:
  teaser: /assets/images/project/rumble.jpg
  og_image: /assets/images/project/rumble-og.jpg
---

When you connect the Xbox Controller to your LEGO Technic hub or LEGO Spike
hub, you can read the buttons and analog inputs, but also control the
builtin rumble actuators.

This lets you create haptic feedback, which can be great for immersive
remote control driving!

In this example, we used the rumble block to make the controller vibrate when
the motor experiences load.

{% include block-program.html
path="block_rumble"
caption="You can make the Xbox Controller rumble to create force feedback."
width="80%"
%}

{% include youtube.html videoid="ERWPdf0GllM" %}

# Controlling the actuators separately

The Xbox Controller has 4 builtin actuators. There is a big and a small one in
the main handles, and two smaller ones behind the triggers.

If you give a single power value, the left and right main actuators will both
rumble with that power. For more fine-grained control, set power as a list of
four values: this controls the left main actuator, right main actuator, left
trigger actuator, and the right trigger actuator, respectively.

For example, `(50, 0, 100, 0)` makes the left main actuator run at half power
and the left trigger at full power:

{% include scaled.html
  path="https://docs.pybricks.com/en/latest/_images/pybricks_blockGamepadRumble_default_with_list.svg"
%}

You can also adjust the duration and the number of times the rumble repeats:

{% include scaled.html
  path="https://docs.pybricks.com/en/latest/_images/pybricks_blockGamepadRumble_with_options.svg"
%}

You can find more details in the [documentation](https://docs.pybricks.com/en/latest/iodevices/xboxcontroller.html).

{%
  include block-program-as-python.html
  show_intro=true
  path="block_rumble"
%}
