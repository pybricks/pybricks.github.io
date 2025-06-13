---
title: "Responding to sensor values"
redirect_from:
  - /learn/sensors/making-decisions/
excerpt: >
  Make your robot respond to sensor values using the Wait block, Conditional Repeat block and If-else block.
img_sensor_compare:
  image: /learn/sensors/compare-block.png
  alt: Using the Value Compare block.
  width: 100%
  caption: >
    Using the Value Compare block to check if the sensor measurement is less than 500 mm.
  labels:
    - text: Data blocks
      x: 10%
      y: 48%
      location: below
    - text: Scroll to Logic blocks
      x: 23%
      y: 16%
      location: above
    - text: Value Compare block
      x: 30%
      y: 20%
      location: right
    - text: |
        1. Add a Value Compare block.
        2. Add a Measure Distance block.
        3. Choose less than (<) 500.
      x: 77%
      y: 63%
      location: below
    - text: |
        Is 493 less than 500? Yes, that is <i>True</i>.
      x: 25%
      y: 83.5%
      location: right
    - text: |
        Is 573 less than 500? No, that is <i>False</i>.
      x: 25%
      y: 94%
      location: right
---

Now that you've learned how to _measure_ sensor values, you'll make your robot
_respond_ to them in this section. You can make your robot respond by comparing
measured values to a _threshold_ value. Then you can trigger an action if your
threshold is crossed.

# Comparing values to a threshold

The Ultrasonic Sensor measures distances between 40 mm and 2000 mm. It would be
impractical to say what the robot should do for each value (40 mm, 41 mm,
42 mm, and so on). It is more practical to say that the robot should do one
thing for "big" distances (like driving) and do something else for "small"
distances (like stopping).

You determine what is big and small by comparing the measurement to a
threshold value that you choose. You do this with the Value Compare block from
the Data category, as shown below.

{% include block-program-download.html path="L05_2_compare" %}
{% include diagram.html data=page.img_sensor_compare %}

In this example, the Value Compare block turns any distance value (from 40 mm to 2000 mm) into
one of the following two values:
- True (if it sees something nearby, closer than 500 mm).
- False (if it sees something farther away or nothing at all).

_True_ and _False_ are precisely the values we need for the Wait Until block, the
Conditional Repeat block, and the If-else block. We'll cover these next.

**Challenge #5.2.A: Comparing the other way** ⸺ You can change how the Compare
block compares the two numbers using the dropdown menu on the block. For
example, if you choose _equals_ (==), then it will say _True_ if the distance
is exactly 500 mm but _False_ for any other distance. How can you get the
same results as in the example above but now without using the _less than_ (<)
option? **Hint** ⸺ You don't need to add any more blocks, but you may need to
move one or more blocks. There are two solutions.
{: .notice--primary}

# Using the Wait Until block

As its name implies, the Wait Until block waits until something happens. More
precisely, it waits until it gets the value _True_. This value is
often called the _condition_. Combined with
what you've just learned, you can make your program wait until a sensor measurement
crosses a threshold, as follows:

{% include block-program.html
path="L05_2_detect"
caption="Driving until an obstacle is detected."
width="100%"
%}

The robot starts driving in _forever_ mode. This is useful because we don't
know the distance in advance (see [Chapter&nbsp;3.3](/learn/making-programs/basic-robot-navigation/#drive-forever-until-you-change-course)).
Then it waits until the Value Compare block gives True. In other words, it waits until the
measured distance is 500 mm or less. Then the robot stops because of the Drive Base Stop block.

**Challenge #5.2.B: Don't move** ⸺ Under some conditions, the program above won't
do anything at all. Why and when is that the case? Support your theory by
adding a Print block to reveal the value of the Value Compare block just before and
after the Wait Until block.
{: .notice--primary}

**Challenge #5.2.C: On the threshold** ⸺ Change the example to wait until
the sensor measures exactly 500 mm and try it out. **Discuss** ⸺ What will
the program do now? Does it always do that in practice, or does it run into
the wall more often? Why is that?
{: .notice--primary}

You can expand this program to do something more useful, as shown below.
Instead of stopping when an obstacle is detected, we'll back up and turn around.
By repeating this forever, the robot drives around the room while avoiding
obstacles indefinitely.

{% include block-program.html
path="L05_2_avoid"
caption="Driving around forever while avoiding obstacles."
width="100%"
%}

**Challenge #5.2.D: Left and right turns** ⸺ This example always makes the
robot turn right after seeing an obstacle. Can you make it alternate between
taking left and right turns? **Discuss** ⸺ Is this better or worse in terms of
getting stuck in corners?
{: .notice--primary}

To better understand what programs with sensors do, it is often helpful to
write down the key actions and decisions that your robot makes. You can connect
them with arrows to indicate in which order they happen. This is called a _flow
chart_.

You can make your flow charts as brief or detailed as you like, as long as it is
helpful to yourself and your team members. The following chart sums up how the
previous example works.

{% include flow-chart.html path="/learn/sensors/L05_2_avoid.svg" caption="
Flow chart for the wall avoidance program. Drawing flow charts can help you
better understand your own program and explain it to others.
" %}

# Using the Conditional Repeat block

The Conditional Repeat block repeats the blocks you place within it _while_ its
condition value is True. For example, you can make it repeatedly play a sound
while the sensor sees something up close. Alternatively, you can configure it
to repeat _until_ the condition is True. Both cases are illustrated here:

{% include block-program.html
path="L05_2_conditional_repeat"
caption="Start with the robot close to a wall. It will repeatedly beep while
the sensor value remains below 500 mm. As you move it farther back,
it will repeatedly beep at a lower pitch until the sensor value is bigger than 1000 mm."
width="70%"
%}

{% include flow-chart.html path="/learn/sensors/L05_2_conditional_repeat.svg" caption="
With the <i>while</i> option, it keeps going around while the condition is True.
With the <i>until</i> option, it keeps going around until the condition is True (in other words, while it is False).
" %}

Whether you choose _until_ or _while_ is a matter of preference. You can
achieve the same results with either one by picking the right condition.
For example, repeating `while distance < 500` is the same as repeating `until distance ≥ 500`.

## What does while True mean?

If you don't pass your own condition value to the Conditional Repeat block, you
can see that it has a default value of True. If you choose to repeat _while_ the
condition is True, it will repeat over and over. Now you can see why you've
already used this block in many examples in this guide!

{% include block-program.html
path="L05_2_forever"
caption="This will print <i>Hello, World!</i> forever. Until you stop the program."
width="50%"
%}

**Challenge #5.2.E: Till dead batteries do us part** ⸺ Previously, you have
explored using the Wait Forever block to prevent a program from ending when its
last blocks finished running. Can you replicate its behavior with a Conditional
Repeat block? **Hint** ⸺ For comparison, create a separate program with just
the Wait Forever block directly underneath the Start block and have a peak at
the code by clicking on the `</>` icon. Even if you've never coded before, many
of the things you see should look familiar based on what you've just learned.
Try to achieve the same result with the Conditional Repeat block. You should
now see exactly the same underlying code!
{: .notice--primary}

## When is the condition checked?

The Conditional Repeat block checks the condition value each time _before_ it
runs the blocks inside it. In the sound example
[above](#using-the-conditional-repeat-block), it checks if the distance is less
than 500 mm and plays a beep sound if so. Then it checks the distance again,
and so on. Otherwise, it won't repeat again, and instead your program proceeds
with the blocks after it. If the distance was 500 mm or bigger to begin with,
the sound doesn't play at all.

It won't check the value as it is running the blocks, so it won't stop the
sound halfway through if the sensor value changes. That's fine for this example
because the sound is only short, but it can give unwanted results if the blocks
in the loop take a long time to run.

Consider the following program. It makes the robot move straight and turn to
drive in a square as in the previous chapters. The Conditional Repeat block
keeps doing this while the sensor value is less than 500 mm. Crucially, it
_only_ checks this condition each time the blocks in it start, so just before
the straights. If you wave your hand in front of the sensor while driving or
turning, the robot won't see it (because it's not even looking).

{% include block-program.html
path="L05_2_square_stop"
caption="❌ A Conditional Repeat block only checks the condition each time it
goes around the loop. Here, it only checks the distance just before the straight.
If you wave your hand in front of the sensor while it moves, it just keeps going."
width="100%"
%}

If you want it to stop repeating based on a condition that holds only briefly (like
waving your hand), you need to make sure you are looking all the time. This can
be done with a Multitask block configured to run until one task is done (see
[Chapter&nbsp;4.4](/learn/flow-basics/advanced-multitasking/) if you haven't tried this block before).

The following example illustrates this. One task keeps the robot driving in a
square indefinitely. The other task monitors the sensor all the time and stops
waiting once the distance exceeds 500 mm. This task is then complete, so the
driving task is stopped as well.

{% include block-program.html
path="L05_2_square_multitask"
caption="You can use a Multitask block to keep looking for obstacles all the
time, even while driving. By choosing to run until <i>one task</i> is done,
you can effectively drive in the square until you see an object, even if you
only briefly wave your hand in front of the sensor."
width="100%"
%}

# Using the If-else block

Thus far, you have used conditions to decide _when_ to stop waiting or
repeating. You can also use such a condition to decide _what_ to do, with the
If-else block. It runs one stack of blocks _if_ the condition value is True, or
_else_ the other stack of blocks.

Try it out with the following example, which uses the If-else block to start
going forward if the distance measurement is bigger than 300 mm or else start
going backward. The If-else block is placed inside a Conditional Repeat block
to keep making this decision over and over. If you hold a book in front of the
robot, it should keep a fixed distance to it and follow you as you move it back
and forth. 

{% include block-program.html
path="L05_2_distance_keep"
width="100%"
%}


{% include flow-chart.html path="/learn/sensors/L05_2_distance_keep.svg"
caption="If the distance is greater than 300 mm then go forward, else backwards. By doing this repeatedly, the robot stays within a fixed distance of the object in front of it. The drive blocks in
forever mode just start driving without waiting for any particular distance, so
the program immediately goes on to check the distance again, and so on." %}


**Challenge #5.2.F: If, else, or both?** ⸺ The If-else block and the Multitask
block look a bit alike. They both contain two or more stacks of blocks but
they work quite differently. **Discuss** ⸺ Describe the key differences
between them and explain when either of them are useful.
{: .notice--primary}


## If .. then .. else if .. else ..

The previous program makes the robot keep a fixed distance to an object, but
you'll notice that it is a bit restless. It keeps alternating between back and
forth around the 300 mm distance point. That's because we never told it to
stop. The motors are always on, one way or another.

It would work better if we made it go forward if the wall is far (> 320 mm),
backward if it was close (< 280 mm), and otherwise just stop. The following program
implements this strategy. Click the v-symbol on the If-else block to add this
extra case.

{% include block-program.html
path="L05_2_distance_keep_elseif"
width="100%"
%}

{% include flow-chart.html path="/learn/sensors/L05_2_distance_keep_elseif.svg"
caption="If the distance is greater than 320 mm then go forward, else if the
distance is less than 280 mm then go backwards, else stop. This allows the
robot to stop while it is on target, rather than restlessly going back and
forth." %}


**Challenge #5.2.G: Air guitar** ⸺ Create a program that plays different notes
for different measured distances. Use the table below to determine the frequencies for each note.
For a distance bigger than 300 mm, play C4; else if the distance is bigger than
270 mm, play D4, and so on. Can you play music on your new instrument?
**Discuss** ⸺ Why is the order of the distance comparisons important? Try
mixing them up and determine if you can still hit all notes. Why not?
{: .notice--primary}

|       | C4    | D4    | E4    | F4    | G4    | A4    | B4    |
|-------|-------|-------|-------|-------|-------|-------|-------|
| Hz    | 261.63| 293.66| 329.63| 349.23| 392.00| 440.00| 493.88|


# Putting it all together

The Wait Until block, Conditional Repeat block and If-else blocks all have
different use cases. You can use and combine them as needed to achieve your
goals. You'll get more familiar with this as you continue to follow this guide.

To get some practice, create the following program. First it starts driving
and waits until it sees something at 500 mm or nearer. Once it sees anything
at all, it decides how close the object is. If it is close, it will back up
and turn left. Otherwise, it will back up and turn right. This means you can
control its movement by waving your hand in front of the sensor up close or
further away.

{% include block-program.html
path="L05_2_avoid_choice"
caption="Combining the Wait Until block with the If-else block to make a decision after waiting on something to happen. A Conditional Repeat block keeps repeating it."
width="100%"
%}

**Challenge #5.2.H: In the flow** ⸺ Draw the flow chart for the program above.
Use the flow charts for the wall-avoidance and the wall-following on this page
for inspiration.
{: .notice--primary}


**Challenge #5.2.I: Uphill both ways** ⸺ In the example above, it reverses in
both cases before turning left or right. Could you use just a single block to
reverse by placing it before the If-else block? Try this out. **Discuss** ⸺ You
should find that it is not quite the same. It will mostly turn right if you
wave your hand in front of the sensor, no matter how close. Why is that? Explain
the difference with your flow chart from challenge Challenge #5.2.H.
{: .notice--primary}

**Challenge #5.2.J: Wait until you see it** ⸺ The Wait Until block provides a
simple and effective way to wait on a condition. Under the hood, it is actually
just a Conditional Repeat block without any blocks stacked into it: It
repeatedly does nothing until the condition holds. Replicate the examples from
the [Wait Until section](#using-the-wait-until-block) on this page but replace
the Wait Until block with a Conditional Repeat block. How do you configure the
_until_ option and the condition? Test your programs to verify that they work
just like the originals.
{: .notice--primary}





