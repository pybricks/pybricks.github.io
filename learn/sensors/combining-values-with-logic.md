---
title: "Combining sensor values"
excerpt: >
  Monitor multiple sensors at the same time.
header:
  teaser: /learn/building-a-robot/mindstorms-inventor/starterbot-mindstorms-inventor.jpg
img_logic_palette:
  image: /learn/sensors/blocks-logic.png
  alt: Logic blocks
  width: 100%
  caption: >
    You'll learn to use most of the Logic blocks in this chapter.
  labels:
    - text: Value Compare block
      x: 43%
      y: 29%
      location: right
    - text: Double Value Compare block
      x: 43%
      y: 39%
      location: right
    - text: Conditional Value block
      x: 43%
      y: 49%
      location: right
    - text: |
        Double Conditional
        Value block
      x: 57%
      y: 60%
      location: right
    - text: Binary Logic block
      x: 38%
      y: 72%
      location: right
    - text: Negation block
      x: 32%
      y: 82%
      location: right
---

Robots are more reliable when they combine information from multiple sources.
For example, if the Ultrasonic Sensor on the InventorBot fails to detect a
small obstacle, you can use the hub buttons, pressed by the bumpers, as a backup.

{% include scaled.html
  path="/learn/building-a-robot/spike-prime/"
  path_small="/learn/building-a-robot/spike-prime/starterbot-spike-prime.jpg"
  caption="InventorBot can avoid obstacles more reliably by monitoring multiple
  sensors at once. If you haven't already, attach the bumpers to InventorBot now."
%}

In this section, you'll learn how to monitor multiple sensors at once and
choose the right response with the following blocks. You'll also learn to
choose values conditionally without If-else blocks.

{% include diagram.html data=page.img_logic_palette %}

Due to the robot's design, the right bumper of the robot presses the left
button on the hub. The left bumper presses the right button. This can be a bit
confusing, so we'll only talk about the buttons throughout this chapter.
{: .notice}

# Combining True/False values

You can combine two sensor conditions with the Binary Logic block.
It combines two condition values, each of which may be True or False, into a
single condition value.

Let's explore this with the following example, which combines values from two
Button Pressed blocks. Each of these blocks gives True if the selected button
is pressed, or False if not. The Value Compare block combines them to give True
if one or both buttons are pressed. It is False if neither are pressed. You can
use the resulting value to make the robot drive forward until it bumps into an
obstacle, as shown below.

{% include block-program.html
path="L05_3_wait_or"
caption="This program makes the robot drive forward until the left or right
button (or both) are pressed. You can find the Binary Logic block on the
Data tab, alongside the other dark green logic blocks. You can find the Button
Measure block on the Input tab."
width="100%"
%}

In _or_ mode, the Binary Logic block gives True if at least one condition is True. In _and_
mode, it only gives True if both conditions are True, as summarized in the following table.


| A     | B     |   | (A or B) |   | (A and B) |
|-------|-------|---|----------|---|-----------|
| False | False |   | False    |   | False     |
| False | True  |   | True     |   | False     |
| True  | False |   | True     |   | False     |
| True  | True  |   | True     |   | True      |

To see the difference, change the _or_ option to _and_ in the previous example.
Now the robot will stop only once both bumpers are pressed at the same time
(not very useful in this case).

When the Wait Until block completes, we know that at least one button is pressed.
You can use the If-else block introduced previously to find out which one is
pressed and decide what to do. This is shown in the following example, which
makes the robot drive away from objects that it runs into.

{% include block-program.html
path="L05_3_wait_choose"
width="100%"
%}

{% include flow-chart.html path="/learn/sensors/L05_3_wait_choose.svg"
caption="The robot starts driving forward and immediately begins monitoring the
buttons. It wait until one or both buttons are pressed. Once that happens, it
checks if the right button is pressed. If so, it will reverse and turn right.
We know that at least one button is pressed. So if it isn't the right button,
it must be the left button. So we can just reverse and turn left otherwise.
Note that unlike in the <i>start driving</i> step at the beginning, we do wait
for the reverse and turn motions to complete before going back to the start of
the loop. " %}


**Challenge #5.3.A: Stuck in a corner** ⸺ With the program above, the robot
has a tendency to get stuck in corners. When does this happen? Can you change
a single setting in this program to ensure it finds a way out with fewer attempts?
{: .notice--primary}

**Challenge #5.3.B: In range** ⸺ Create a program that makes the robot play
sounds while the Ultrasonic Sensor distance is between 300 mm and 600 mm.
**Hint** ⸺ Use two Value Compare blocks. One should check the upper bound and
one should check the lower bound. Use the Binary Logic block to combine both
conditions. It is also possible to do this with just a single Double Value
Compare block. How do you choose its settings to achieve the same result?
{: .notice--primary}

# Combining more than two sensors

Since the Binary Logic block produces a single True/False value, you can use
its result inside another Binary Logic block. This lets you combine sensor
conditions to best suit your application. For example, you could make the robot
wait until it sees an obstacle with the Ultrasonic Sensor or at least one
button is pressed, as shown below.

{% include block-program.html
path="L05_3_wait_all"
width="100%"
%}

{% include flow-chart.html path="/learn/sensors/L05_3_wait_all.svg"
caption="This program waits on any of three sensors to be triggered. Then it
decides what to do by going over the sensor conditions separately. If neither
button is pressed, it must have been the distance measurement that made the
Wait Until stop. We should still be at a fair distance to a wall so we'll just
turn around without reversing first. " %}

# Waiting in parallel

Using the Binary Logic block to combine sensors works well if all you want
to do is wait on the same condition. If you want to change _what_
you wait on or what you do along the way, the Multitask block is more
flexible.

Let's say you want to wait until the distance sensor sees something
or a button is _clicked_. There isn't a way to measure clicks directly,
but you can wait until the button is pressed and then until it is released.
You can monitor the distance at the same time using multitasking.
By choosing to run until _one task_ completes (see
[Chapter&nbsp;4.4](/learn/flow-basics/advanced-multitasking/)), it will stop
waiting as soon as an object is detected or the left button is clicked, as shown
in the following example.

{% include block-program.html path="L05_3_wait_click" width="70%" caption="If
the condition to wait on changes along the way, you can use the Multitask
block. This program plays a high beep if the distance sensor sees something
or a low beep if the left hub button is clicked. 
You can find the green <i>Negation</i> block on the Data tab. It changes True to
False and it changes False to True. So it effectively turns <i>pressed</i> into
<i>released</i>, which is just what we need here. " %}

**Challenge #5.3.C: Eyes on the road** ⸺ Create a program that makes the robot
drive forward for 500 mm unless it runs into an obstacle sooner. Create a solution
with the Wait Until block and multiple Binary Logic blocks. Also create a
solution with the Multitask block. **Presentation** ⸺ Split the two approaches
between team members and present your solutions to each other. Discuss the pros
and cons of both methods.
{: .notice--primary}

**Challenge #5.3.D: Wave to turn** ⸺ Modify the obstacle-avoidance program
in the [previous section](#combining-more-than-two-sensors) to respond to you
waving in front of the sensor instead of any approaching object. **Hint** ⸺ 
When you wave your hand in front of the sensor, it detects a low value and then
a high value. You could wait for these conditions just like waiting for the
button click in the example above.
{: .notice--primary}


# Deciding on a value

Sometimes you end up using an If-else block with two nearly
identical stacks of blocks in them, save for one _value_ that is different.
In the [previous section](/learn/sensors/responding-sensor-values/#using-the-if-else-block) for example,
you've used an If-else block to make the robot drive at 100 mm/s
if the distance is greater than 300 mm and otherwise drive at -100 mm/s.

There is nothing wrong with using an If-else block like that, but it can make
some programs harder to follow as they get bigger. In this case you can use the
Conditional Value block. It gives one value if the condition is True and
another value if it is false, as shown in the updated example below.

{% include block-program.html path="L05_3_ternary" width="100%" caption="The
Conditional Value block selects one of two values based on a condition. You can understand
the resulting value by just reading it from left to right: It drives at a speed
of 100 if the distance if bigger than 300 and at -100 otherwise." %}

In programs related to remote control, you'll find the Double Conditional Value block
useful as well. It has two conditions and three values. It gets value A if one condition is true,
otherwise it gets value B if a second condition true and otherwise it gets value C. 

Let's illustrate why this is useful with the following example. The motor runs
backward (A = -50% power) if the left button is pressed, otherwise forward (B = 50%
power) if the right button is pressed, and otherwise it stops (C = 0% power).

This is a useful test program when you design mechanisms. You can manually
check if your mechanism does what you want, and whether it is sturdy enough.

{% include block-program.html path="L05_3_ternary_double" width="100%"
caption="This program lets you control a motor with the hub buttons. For
comparison, create the same program with If-else blocks and see which one you
prefer." %}



