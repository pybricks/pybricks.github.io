---
title: "Basic robot navigation"
excerpt: >
  The drive base blocks let you accurately control the movements of your robot.
  Learn how to use each of these blocks and their settings effectively.
img_drive_base_palette:
  image: /learn/making-programs/basic-robot-navigation/drive-blocks.png
  alt: Drive base blocks
  width: 100%
  caption: >
    These blocks can be used to control a drive base.
  labels:
    - text: |
        <b>Drive</b> with a controlled acceleration and speed.
        By a given distance, turn angle, or forever.
      x: 55%
      y: 38%
      location: above
    - text: <b>Stop</b> ongoing movement.
      x: 48%
      y: 50%
      location: right
    - text: |
        <b>Configure</b> drive settings
        like speed and acceleration
      x: 55%
      y: 62%
      location: below
img_inventor_drive:
  image: basic-robot-navigation/inventor-drive.svg
  width: 100%
  caption: >
      When you tell the robot to drive straight or turn (green arrows), it
      works out what the left and right motors should do to make that
      happen (red arrows). A positive angle or turn rate corresponds to a
      clockwise turn when viewed from above.
  labels:
    - text: |
          left
          wheel
      x: 4.5%
      y: 19%
      location: below
    - text: |
          right
          wheel
      x: 34%
      y: 19%
      location: below
    - text: positive distance
      x: 19%
      y: 37%
      location: below
    - text: negative distance
      x: 79%
      y: 37%
      location: below
    - text: positive turn angle
      x: 19%
      y: 85%
      location: below
    - text: negative turn angle
      x: 79%
      y: 85%
      location: below
img_inventor_curve:
  image: basic-robot-navigation/inventor-curve.svg
  width: 100%
  caption: >
    Making curves. The orange arrows indicate the circle radius. The
    green arrows indicate the path of the robot. If you choose a distance
    duration, then you are effectively setting the length of the green arrow.
    If you choose an angle duration, you are setting the angle that the green
    arrow makes between the orange line and the black dashed line. Choosing 360
    degrees would make it go round the whole circle.
  labels:
    - text: |
        negative radius
        positive distance/angle
      x: 24%
      y: 40%
      location: below
    - text: |
        positive radius
        positive distance/angle
      x: 71%
      y: 40%
      location: below
    - text: |
        negative radius
        negative distance/angle
      x: 24%
      y: 88%
      location: below
    - text: |
        positive radius
        negative distance/angle
      x: 71%
      y: 88%
      location: below
img_inventor_wheel:
  image: basic-robot-navigation/inventor-wheel.svg
  width: 100%
  caption: >
      Wheel diameter and wheel base (axle track). You can measure both values
      with a ruler that measures millimeters. If your rules uses inches, take
      the measured value and multiply it by 25.4 to get the millimeter value.
  labels:
    - text: |
          wheel
          diameter
      x: 42%
      y: 38%
      location: left
    - text: wheel base (axle track)
      x: 73%
      y: 20%
      location: above
---

Now that you've built a robot and made some basic programs, let's have a closer
look at how you can make the robot move effectively.

Throughout this chapter, we'll use the angle sensors built into the motors to
drive straight and turn. It's important to have a good understanding of basic
driving and navigation before trying out the gyroscope in later chapters.

You'll learn to use each of the following blocks:

{% include diagram.html data=page.img_drive_base_palette %}

# Driving with two wheels

A typical LEGO robot drives using two wheels, each powered by one motor. A
passive support wheel or ball caster prevents it from tipping over. The robot
drives straight ahead by turning both wheels at the same speed. It turns by
making one wheel go at a different speed or in the opposite direction, as
pictured below.

{% include diagram.html data=page.img_inventor_drive %}

## Wheel diameter and base width

You can tell your robot to drive by a given distance or turn by a given angle.
The robot works out how much it needs to move each wheel to get there.
To calculate this, it needs to know the
_wheel diameter_ and the _wheel base_ or track, as shown below.

{% include diagram.html data=page.img_inventor_wheel %}

To measure the wheel diameter, place your ruler on the wheel. It is the
distance from one end of the rim all the way to the other end. To measure the
wheel base, place your robot on top of the ruler and note the distance
between the points where the wheels touch the ruler.

On my robot, I measured 56 millimeters for the wheel diameter and 128 for the
wheel base. What did you measure?

**Tip** --- One _LEGO unit_ is exactly 8 millimeters. A LEGO unit is the
distance between two holes or studs. In this example, the wheel diameter is the
same as a length-7 beam. And 7 × 8 makes 56 mm! Similarly, the distance between
the wheel contacts is 16 LEGO units, and 16 × 8 is 128 mm. Use
a ruler for more precision!
{: .notice}


## Basic lines and turns

You enter your measured values in the drive base setup block. Now add three
drive blocks to make it move. Create the program as shown below. Run the
program when you're ready.

{% include block-program.html
path="L03_3_basics"
caption="Driving straight and making turns."
width="100%"
%}

Your robot should now drive forward for 250 mm (25 cm, or about 10"), turn
around, and drive back to where it started.

**Challenge #3.3.A: Square it** ⸺ Can you make your robot drive in a square?
How many drive blocks do you need to do it? When you're ready, change the
program to a rectangle that is 250 mm by 1000 mm. When it drives, place an
object at each of the corners as it passes by. Verify your results with a
measuring tape.
{: .notice--primary}

**Challenge #3.3.B: Hexagons are the Bestagons** ⸺ Modify your solution from
challenge 3G to drive in a hexagonal shape instead. How many degrees should
each turn be? How many blocks do you need this time? **Discuss** ⸺ Draw the
shape that the robot drives on paper and mark the angles that the robot makes.
What do you get if you add up the angles of all turns? Do it for the
square from challenge 3G too. Do you notice anything? Is this also true for
triangles and pentagons? Are there shapes where this does not apply?
{: .notice--primary}

**Challenge #3.3.C: Robomenu** ⸺ Have the robot drive around in the shape of
letters to spell out your favorite food. Can your classmate guess what you
wrote?
{: .notice--primary}

Working with millimeters (mm) may appear awkward at first, especially if you
are used to thinking in centimeters (cm) or inches ("). Instead of converting
every number in your head or using a calculator, we recommend playing with
millimeter values to become familiar with them. Try things out, get it wrong,
and then fix it. It's a useful skill to have. The following table helps place
common numbers in the context of every day objects and values. The rightmost
columns are only there to help you the first time. Try to think in millimeters
directly: Go from _drive along my desk_ to _drive about 600mm_ without
converting. Then try it!
{: .notice}

| mm    | Intuitive examples                           | cm   | m      | imperial  |
|-------|----------------------------------------------|------|--------|-----------|
| 1     | a pencil stroke, fingernail, paperclip       | 0.1  | 0.001  | ~0.04 in  |
| 10    | a small LEGO brick, a small marble           | 1    | 0.01   | ~0.40 in  |
| 100   | a playing card, a large apple, a small phone | 10   | 0.01   | ~4 in     |
| 250   | letter paper, a ruler, a small notebook      | 25   | 0.25   | ~10 in    |
| 500   | half a meter, half a yard, a small step      | 50   | 0.5    | ~1 ½ ft   |
| 1000  | a meter, a yard, a big step                  | 100  | 1      | ~3.3 ft   |
| 10000 | a classroom                                  | 1000 | 10     | ~33 ft    |


## Verifying and adjusting the dimensions

In practice, wheels compress slightly under the weight of your robot.
Especially with soft rubber tyres. To verify, program a single movement to
drive 1000 mm. Measure how far it really traveled with a measuring tape.
Compensate as follows:

 - If your robot does not drive far enough, decrease the wheel diameter value slightly.
 - If your robot drives too far, increase the wheel diameter value slightly.

If you run the program again, the robot should be closer to 1000 mm this time.
Adjust again as needed.

Motor shafts and axles can bend slightly under the load of the robot, causing
the ground contact points to shift slightly. To verify, make your robot turn
360 degrees and check that it is back in the same place.

- If your robot does not turn enough, increase the wheel base value slightly.
- If your robot turns too far, decrease the wheel base value slightly.

If your results are inconsistent, avoid tweaking these numbers endlessly. The
cause might be elsewhere, such as in grip or the robot design. For example,
make sure that the wheels don't slip. After all, the robot only knows how far
the wheels turn, not how far it really drives.

# Making curves

This feature is still under development and will be coming soon. An older
function for making curves is already available. It doesn't exactly match
the diagram below, but you can still use it to make smooth curves. Stay tuned!
{: .notice--warning}

Instead of combining straights and turns to get to your destination, your robot
can drive along an arc. An arc is a curve, a portion of a circle. A single
curve is sometimes faster than a combination of straights and turns. 


{% include diagram.html data=page.img_inventor_curve %}


You choose the _size of the circle_ by setting the radius. A big value means a
big circle with a wide turn. A small value is a tight turn. The value cannot be
zero. To turn in place, just use simpler _turn_ method we used earlier. Choose
a positive radius value to drive along a circle on the robot's right. Choose a
negative radius for a circle on the left, as shown below.

Next, choose how far you want to drive along the circle. Choose a positive
value for forwards along your chosen circle. Choose negative for reverse. You
can specify how far to drive using either an angle or distance, whichever is
more convenient for your program.

To practice with making curves, create the following program that makes your
robot drive in an oval and stop where it started.

{% include block-program.html
path="L03_3_curve"
caption="Drive in an oval shape with two straights and two half-circles."
width="100%"
%}


**Challenge #3.3.D: Squaring the circle** ⸺ In Challenge #3.3.G, you made program to
drive in a square with four straights and four turns. Can you adapt it to
replace two straights and a turn with a single curve? The resulting shape should
be a quarter of a pizza. What do the radius and angle need to be for the curve?
Draw it on paper first and mark the straights, turns, and the curve with the
right parameters.
{: .notice--primary}

# Adjusting speed and acceleration

# Understanding stop modes

# Combine movements without stopping

Instead of choosing one of the stop modes, you can choose _continue moving_.
When you do, the robot won't decelerate as it approaches the block's
destination like it normally does. Instead, it will keep going. This means the
robot is still at speed when it begins to execute the next block. So the next
command does not have to accelerate either and just keeps going. It's as if
sequential moves are blended together.

Try it out by modifying the program for the oval you made earlier. It
should complete the oval much more quickly since it does not have to stop and
accelerate four times.

{% include block-program.html
path="L03_3_continue"
caption="Drive in an oval shape with two straights and two half-circles as before, but don't stop after each movement."
width="100%"
%}

If you use a sequence of movements like this, be sure to have the final block
stop using one of the stop modes as shown above. Otherwise, it would just keep
driving forever until you use another block to stop it.

Using _continue_ is mainly useful to combine straights with curves. Going at
full speed into a tight or in-place turn is not a good idea, as the wheels
would slip.

# Drive forever (until you stop)

# Don't forget the mechanics

When your robot doesn't quite move like it should, it's not always a
coding issue. Your robot design is really important too!

Iterate with your design as much as with your code. If something doesn't work,
document it with pictures, videos, and notes about why it didn't work. Don't be
scared to take things apart! Take pictures as you disassemble it. You can
always view them in reverse if you want to rebuild your previous design.


**Challenge #3.3.E: What's in a diameter?** ⸺ Given a target distance of 1000 mm,
can you work out how far both wheels need to turn how to get there? Write down
your estimate. Try it out with a small program, and count the number of
revolutions of the white marker on the wheel. Did you get it right? **Discuss**
⸺ Why does the robot need to know what the wheel diameter and wheel base is?
What happens if you make one value way too small or way too big? What if you
use bigger wheels?
{: .notice--primary}


**Challenge #3.3.F: Turning point** ⸺ A conventional car is quite different from
your LEGO robot. It drives using an engine or motors and it steers by turning
the front wheels. Can you draw a top-view diagram like the one above, but for a
car? Be sure to draw exactly how the front wheels are positioned and add arrows
to indicate the direction of travel. How is it different from your LEGO robot?
Why can a car not turn in place? Is this also true for a 4x4 vehicle? How could
you modify a car to turn in place? **Discuss** ⸺ In your diagram, draw straight
lines through the front and rear wheel axles. How many intersections do you
get, and what is the meaning of these point(s)? **Deep dive:** Search online
for _Ackermann steering geometry_. Can you build something like it with LEGO
bricks?
{: .notice--primary}
