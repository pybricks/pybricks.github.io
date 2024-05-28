---
title: Building a LEGO MINDSTORMS Robot that balances on a ball
tags:
  - Block Coding
  - Python
  - SPIKE Prime
  - MINDSTORMS Robot Inventor
toc: true
excerpt: >
  In this project you'll build a LEGO MINDSTORMS robot that balances on a ball.
  Includes step-by-step instructions and ready-to-use code.
header:
  teaser: /project/mindstorms-robot-inventor/balancer/balancer-mindstorms.jpg
  og_image: /project/mindstorms-robot-inventor/balancer/balancer-mindstorms-og.jpg
---

I've always been fascinated by robots that can balance on a ball.

It's one of
those builds that looks like magic, but it's ultimately just a fast feedback
loop. The robot constantly measures the tilt of the robot using the gyro
sensor and adjusts the motors to keep the robot upright.

{% include scaled.html
  path="/project/mindstorms-robot-inventor/balancer/balancer-mindstorms.jpg"
%}

In this article, we'll show you how you can build and program your own
balancing robot using the LEGO MINDSTORMS Robot Inventor set.

You'll use
Pybricks to code it, which is much faster and stable than the standard
programming environment, which is crucial for balancing robots.

{% include youtube.html videoid="-T3DuCdERkk" %}


# Building the robot

When this set was initially launched, I was super excited to see that it
included the Duplo ball and some small wheels. I immediately thought about
building a balancing robot with it. After many iterations, it worked!

You can build this robot with the elements of the LEGO MINDSTORMS Robot
Inventor set (51515). Click the image below to download the instructions. Just
follow the steps and you'll have your robot ready in no time.

<a href="/project/mindstorms-robot-inventor/balancer/ball-balancer-mindstorms-robot-inventor.pdf" download>
![Building Instructions](/project/mindstorms-robot-inventor/balancer/ball-balancer-preview.png)
</a>

# The balancing program

The program below balances the robot along two axes at the same time. One motor
is used to control the x axis using the gyro sensor value of the x axis. The
other motor is used to control the y axis.

The feedback to each motor is a weighted sum of all the signals it needs to
keep at zero. This includes the gyro angle, gyro speed, motor angle, and motor
speed. The weights are tuned to make the robot stable.

{% include block-program.html
path="ball_balancer_blocks"
caption="The ball balancing program"
%}

When you turn the hub on, leave it on the desk or the floor for a few seconds.
This gives the gyro sensor a chance to calibrate. Then put the robot on top
of the ball and let it stand upright between your hands. Start the program and
carefully let go.

Naturally, you can keep your hands close to prevent it from falling flat, but
it is generally best to not try to help the robot forcefully. It needs to find
its own path!

You can see how this works in the video above.

{% include snippets/pybricks-intro.md %}

{%
  include block-program-as-python.html
  show_intro=true
  path="ball_balancer_blocks"
%}
