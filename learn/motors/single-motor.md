---
title: "Using individual motors"
excerpt: >
  Learn how to control a single motor precisely and how to change its settings.
header:
  teaser: /learn/motors/single-motor-palette.png
single-motor-palette:
  image: /learn/motors/single-motor-palette.png
  alt: Single motor blocks
  width: 100%
  caption: >
    These blocks can be used to control a single motor.
  labels:
    - text: |
        <b>Run</b> with a controlled acceleration and speed.
        By a given amount of degrees, or forever.
      x: 45%
      y: 28%
      location: above
    - text: |
        <b>Track</b> a new angle right away,
        without smooth acceleration.
      x: 38%
      y: 41%
      location: right
    - text: <b>Stop</b> moving.
      x: 38%
      y: 58%
      location: right
    - text: <b>Configure</b> motion settings
      x: 55%
      y: 67%
      location: right
    - text: <b>Power</b> the motor without speed or position control
      x: 45%
      y: 80%
      location: below
angle-line-overview:
  image: /learn/motors/angle-line-overview.svg
  alt: Angle line overview
  width: 100%
  caption: >
    Motor angles represented on a line, increasing
    or decreasing when the motor turns.
  labels:
    - text: Turning clockwise increases the angle
      x: 70%
      y: 15%
      location: left
      hideline: true
    - text: Turning counterclockwise decreases the angle
      x: 70%
      y: 80%
      location: left
      hideline: true
angle-line-zoom:
  image: /learn/motors/angle-line-zoom.svg
  alt: Angle line zoom
  width: 100%
  caption: >
    Different motor positions with their corresponding angles. Some motors have
    a ○ marker to indicate 0°, 360°, and so on.
  labels:
    - text: When the program starts, the angle is between -180° and 180°
      x: 50%
      y: 61%
      location: below
angle-line-run-by-angle:
  image: /learn/motors/angle-line-run-by-angle.svg
  alt: Visualization of running by a given angle.
  width: 100%
  caption: >
    If the motor starts at 45° and you tell it to turn <i>by</i> 90°, it should
    arrive close to 135°, within a few degrees of error. Because the final
    angle is the initial for the next move, errors accumulate.
  labels:
    - text: Run <i>by</i> 90°
      x: 50%
      y: 25%
      location: above
      hideline: true
    - text: Initial angle
      x: 30%
      y: 54%
      location: left
      hideline: true
    - text: Final angle
      x: 75%
      y: 54%
      location: right
      hideline: true
angle-line-run-towards-angle:
  image: /learn/motors/angle-line-run-towards-angle.svg
  alt: Visualization of running towards a given angle.
  width: 100%
  caption: >
    If you tell the motor to turn <i>towards</i> 135°, it should
    arrive close to 135° within a few degrees of error, no matter the initial
    position. This is true for every move, so errors do not accumulate.
  labels:
    - text: Run <i>towards</i> 135°
      x: 50%
      y: 25%
      location: above
      hideline: true
    - text: |
        Initial angle
        does not matter
      x: 30%
      y: 54%
      location: left
      hideline: true
    - text: Final angle
      x: 75%
      y: 54%
      location: right
      hideline: true
---

A robot like the StarterBot has two motors for driving. In this chapter you'll
take a closer look at just one motor. This is useful for many mechanisms, such
as robot arms, automatic doors or attachments on an FLL robot.

You'll learn how to accurately control the motor speed and
angle, and how to configure motor parameters such as acceleration. 
Understanding these techniques for one motor will help you master similar
techniques applied to a drive base with two motors later on.


We'll cover each of the following blocks in this chapter.




{% include diagram.html data=page.single-motor-palette %}



# Understanding motor angles

Most modern LEGO
[motors](/learn/getting-started/what-do-you-need/#choosing-motors) have a
builtin sensor to measure their position. More precisely, these motors measure
their _rotation angle_. The hub uses this angle information to drive a motor at
a constant speed and stop it at the required point.

The angle value increases when you rotate the motor
clockwise ("forward"), one degree at a time. There are 360 degrees in one
rotation, but the angle doesn't stop there. It just keeps increasing as you
keep turning. When you rotate it counterclockwise ("backward"), the
value decreases, and ultimately turns negative.

{% include diagram.html data=page.angle-line-overview %}

It helps to think of angles as values on a line, as shown above. We'll use this
analogy throughout this chapter. Zooming in around zero reveals more detail
as shown below.

{% include diagram.html data=page.angle-line-zoom %}

When the program starts, the angle value will be between `-180°` and `180°`.
This is practical in many cases, but you can adjust it by resetting the
angle to any other initial value as discussed here.

> LINK TO article about running until stalled etc?

**Are angles on a circle?** ⸺ It may seem intuitive to think of angles as
values on a circle, but this is _incorrect_. This analogy breaks down after one
whole rotation, which can be more confusing than helpful in the long run.
Similarly, the terms "shortest path", "relative position" and "absolute
position" used in other coding apps are misnomers in all but the simplest
applications. You can read more [here](/learn/motors/single-motor-extra/).
{: .notice}

# Rotating _by_ a given angle


{% include diagram.html data=page.angle-line-run-by-angle %}


When you tell a motor to run _by_ a given angle, it will do so from where it
is currently at. So, if the motor is currently at `45°` and
you tell it to turn by `90°`, it is going to aim to arrive at `135°` degrees.
You can choose which speed it moves at. 
You can choose a negative speed or negative angle to rotate in reverse.
If both are negative, it runs forward.

This is simple enough, which is why it is often used first in robotics lessons.
But this approach has a few drawbacks. The end position
depends on the starting position, so you have to ensure that the starting is
where you want it to be. If you have several moves like these in a row, _errors add up_. 
Let's see why.

Suppose you
tell it to move by `90°` and then `-90°` . Suppose you've even carefully
ensured that it starts at `0°`. The first time, it
_arrives_ at `92°`, perhaps because something pushed against the shaft.
If you tell it to move by `-90°` _now_, it is going to
_aim_ for `92 - 90° = 2°`. And it may perhaps arrive at `3°` due to friction.
This gets worse every time you make another move.

While small errors for each individual move are normal, error accumulation
across moves is not inherent to the motor or your design. This error builds up
only because the robot is _just following your instructions_!

It has no way of knowing you actually meant to travel to `0°`.
So if your goal is to go towards `90°` and then towards `0°`, you should tell
your robot to do
exactly that. This is where running _towards_ an angle comes in.

# Rotating _towards_ a given angle

{% include diagram.html data=page.angle-line-run-towards-angle %}

When you tell a motor to run _towards_ a given angle, it will do so no matter
the current position of the motor. If it is currently at `125°` and
you tell it to move _towards_ `425°`, it will turn `300°` forward to
accomplish this. If you tell it to go towards `75°` instead, it will run backward
to get there.

This method figures out the direction by itself, so does not matter whether
the _speed_ value is positive or negative.

Running _towards_ an angle has none of the drawbacks of running _by_ an angle
as illustrated previously. Why is that? If you tell it to go _towards_ `90°`
first and towards `0°` next, it will do so even if the first move was not
perfect. Even if each move is off by several degrees, it doesn't add up over
time.

The only catch is that you have to think a bit more consciously about what
exactly you want your robot to do. This is always a good idea though!













. Instead of lazily turning
in 90-degree increments, you'd have to use a _variable_ to 




 that ultimately leads to
a lot of confusion when you get to application


- explain this is kind of similar to run to abs BUT also works beyond full circle
- and if you do want shortest path in most basic case, that just means you have
  to carefully decide _where_ to go.
- and then the init case?



**TODO**: This is where we should have port view so people can see what the angle
does when you move the motor.
{: .notice--warning}

If you've chosen the positive direction to be counterclockwise as shown earlier,
then the opposite applies. In this case, the angle value goes up when you rotate
counterclockwise, and it goes down when you rotate clockwise.







Some motors have a gray colored marker on the motor casing and the rotating
shaft. This is where the measured angle is 0 degrees or any number of whole
rotations.











**Note**: Other LEGO and robotics applications 
Ultimately, you can achieve similar goals with both approaches
{: .notice--warning}



position. More
accurately, they 

their angle, or "position"/

> 0 to 180 and back several times...


When you choose to rotate _by_ a given angle, it rotates by that amount,
starting from where it is now. So, if the motor is currently at 415 degrees and
you tell it to turn 60 degrees, it is going to aim at 475 degrees.

# Understanding coast, brake, and hold

After the motor smoothly decelerates to standstill, you can choose what it
should do next.

## Resistance to motion

When running ??? above, you might have noticed that the error buildup when
running _by_ an angle doesn't look quite so bad when using _hold_ mode. That is
because the motor is guaranteed to be stationary between moves, and the robot
can make a few assumptions about where to move next, thus avoiding error build up.
Still, it is better to run _towards_ your intended angle so you don't have to
rely on these assumptions, and so that you are not restricted to _hold_ mode.


# Turning forever... until you stop it

# Tracking variable target angles

# Changing the default motor settings
