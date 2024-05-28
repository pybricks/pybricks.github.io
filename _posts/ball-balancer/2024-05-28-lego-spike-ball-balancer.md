---
title: Building a LEGO SPIKE Prime Robot that balances on a ball
tags:
  - Block Coding
  - Python
  - SPIKE Prime
toc: true
excerpt: >
  In this project you'll build a LEGO SPIKE Prime robot that balances on a ball.
  Includes step-by-step instructions and ready-to-use code.
header:
  teaser: /project/spike-prime/balancer/spike-balancer.jpg
  og_image: /project/spike-prime/balancer/spike-balancer-og.jpg
---

Just like Technic Hub, the SPIKE Prime Hub has a really accurate gyro sensor.
What better way to show what it can do than to build a balancing robot?

{% include scaled.html
  path="/project/spike-prime/balancer/spike-balancer.jpg"
%}

In this article, we'll show you how you can build and program your own
balancing robot using LEGO SPIKE Prime.


# Building the robot

You can build it with the SPIKE Prime core and expansions sets. It doesn't use
that many pieces, so you may be able to build it from spare pieces even if you
don't have the expansion set. The ball comes in [various LEGO and Duplo
sets](https://brickset.com/sets/containing-part-4156530) and is available on
Bricklink for less than $1.

You can also build this robot with the MINDSTORMS Robot Inventor set. While the hub works
the same, it comes with different building elements. Check
out [these instructions instead](../lego-mindstorms-ball-balancer/).

Click the image below to download the instructions. Just
follow the steps and you'll have your robot ready in no time.

<a href="/project/spike-prime/balancer/ball-balancer-spike-prime.pdf" download>
![Building Instructions](/project/spike-prime/balancer/ball-balancer-spike-prime-preview.png)
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

You can see how this works in the video below.


{% include youtube.html videoid="MlMp89KMYjQ" %}



{% include snippets/pybricks-intro.md %}

{%
  include block-program-as-python.html
  show_intro=true
  path="ball_balancer_blocks"
%}
