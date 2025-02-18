---
title: "Your first robot program"
excerpt: >
  What does it take to build a program? Learn to set up your hub, motors and
  sensors and make your robot move with precision.
header:
  teaser: /learn/making-programs/basics-motor-setup-3.png
redirect_from:
  - /learn/making-programs/
img_setup_1:
  image: /learn/making-programs/basics-motor-setup-1.png
  alt: Setup step 1
  width: 100%
  caption: >
    1. Create a new program called 'setup_demo'. From the setup tab, pick two motor
    setup blocks on and place them on the canvas.
  labels:
    - text: Setup blocks
      x: 10%
      y: 26%
      location: below
    - text: Motor setup
      x: 50%
      y: 82%
      location: right
    - text: Set up two motors
      x: 75%
      y: 30%
      location: above
img_setup_2:
  image: /learn/making-programs/basics-motor-setup-2.png
  alt: Setup step 2
  width: 100%
  caption: >
    2. Give each motor a name. Since they'll be driving the wheels on the
    StarterBot, let's call the one on port A <i>left wheel</i> and the one on
    port B <i>right wheel</i>. If you look at the left wheel, you'll notice that it
    must turn <i>counterclockwise</i> to make the robot drive forward. Change
    the setting as shown above.
  labels:
    - text: | 
        Give each
        motor a name.
      x: 35%
      y: 40%
      location: above
    - text: |
        Left motor turns
        <i>counterclockwise</i>
        to make the robot
        drive forward.
      x: 68%
      y: 35%
      location: right
    - text: |
        You can delete
        the Print block.
      x: 56%
      y: 70%
      location: right
img_setup_3:
  image: /learn/making-programs/basics-motor-setup-3.png
  alt: Setup step 3
  width: 100%
  caption: >
    3. Place the drive base setup on the canvas. Configure it to use the left and
    right wheels. Measure the diameter of your wheels and and the distance between
    the wheels and enter them as shown. Delete the existing <i>Print block</i>.
  labels:
    - text: Drive base setup block
      x: 68%
      y: 35%
      location: above
    - text: |
        Select left and
        right motor
      x: 35%
      y: 72%
      location: below
    - text: |
        Set wheel diameter and distance
        between wheel ground contacts.
      x: 70%
      y: 72%
      location: below
img_setup_4:
  image: /learn/making-programs/basics-motor-setup-4.png
  alt: Setup step 4
  width: 100%
  caption: >
    4. From the output tab, pick two <i>Drive blocks</i> and attach them to the main 
    program block. Leave the first one unchanged. In the second block, change
    the distance to <i>-250</i> millimeters.
  labels:
    - text: Drive block
      x: 62%
      y: 29%
      location: right
    - text: Drive forward by 250 mm
      x: 48%
      y: 74%
      location: above
    - text: Enter <i>-250</i> to <i>reverse</i> by 250 mm
      x: 48%
      y: 81%
      location: below

img_setup_5:
  image: /learn/making-programs/basics-motor-setup-5.png
  alt: Setup step 5
  width: 100%
  caption: >
    5. Error messages can help you find some mistakes early. Even if it worked
    right away, try doing it wrong on purpose to familiarize yourself with
    reading error messages.
  labels:
    - text: |
        A motor is not
        connected correctly
      x: 62%
      y: 62%
      location: right

img_setup_6:
  image: /learn/making-programs/basics-motor-setup-6.png
  alt: Setup step 6
  width: 100%
  caption: >
    You can change the options on a block to change what that block does.
  labels:
    - text: |
        Choose different
        drive methods
      x: 58%
      y: 75%
      location: right


---

In this chapter, you'll learn how to set up your programs for the StarterBot
you've just built. You'll also experiment with basic movements and learn
to verify the results.

Remember that you can also use your own design or competition robot. You'll
learn to adapt the code to your design along the way.

# Setup and the main program

Each Pybricks programs consists of two parts:
- **Device setup**: This part describes how your robot _is built_ and how the
  devices are connected to the hub.
- **Program**: This part describes what the robot _should do_.

To better understand how this works, let's build an example program using the
steps below.

{% include diagram.html data=page.img_setup_1 %}

{% include diagram.html data=page.img_setup_2 %}

{% include diagram.html data=page.img_setup_3 %}

{% include diagram.html data=page.img_setup_4 %}

# Verifying and troubleshooting
Connect to the robot using the Bluetooth button and run your program. Your
robot should drive forward by
250 mm (about 10") and then reverse, ending up where it started. Otherwise:

- If it didn't move at all, be sure to check the cables and the ports you selected, as
shown below.
- If it started by turning or reversing instead of moving straight
forward and back, check the directions in step 2 above.
- Place a ruler next to the robot. If it drove much too far or not far enough,
  measure the wheel diameter again.
  
Don't worry if it's only slightly off for now. You'll learn to improve accuracy
in the next chapters.

{% include diagram.html data=page.img_setup_5 %}

Running a very basic program with just a few movements is a good way to check
that your setup is configured properly.

This setup will be a big time saver when you create larger programs later on.
If you change your design including the cables, all you have to do is change
one setup block, rather than changing it throughout your entire program.

# Changing parameters

The blocks you've placed under the yellow _program_ block run one by one, from
top to bottom. Each block is one command for the robot to execute. Different
blocks make the robot do different things. Each block has _parameters_ that
change _how_ it executes that command. For example, you can change how far it
drives and use a negative value to reverse.

We'll get to each of these settings in the chapters to come,
but this is a good time to give some of the other options a try.
For example, you can change the Drive block to make a turn, as shown below.

{% include diagram.html data=page.img_setup_6 %}

Once you've changed settings, you can see what that block does by reading it
from _left to right_: The _robot_ (that you've set up) drives _straight_ (your
choice) for `250 mm` (your distance value) and then actively _holds_ the
motors in place (your choice).

When changing the settings, it's best to do so from left to right as well,
because other settings may be added or removed as you go. For example, if you
select _straight_, an option appears to choose how many millimeters. But if you
select _turn_, an option appears to choose how many degrees to turn.

# Further exploration

In this chapter, you've learned to build a program to make your robot move.
You used setup blocks to describe your robot. Then you added program blocks to
make make your robot move, and changed settings to change what each block did.
The following challenges will help you practice your skills.

**Challenge #3.1.A: Living on the edge** ⸺ Pick a fixed starting point on your
desk and measure the distance to the edge of your desk. Tell the robot to drive
exactly that distance and back again. _Tip:_  On your first try, to reduce
the value slightly. Be prepared to catch you robot if it falls. Safety first!
When you're away from the computer, you can stop the program using the hub
button.
{: .notice--primary}

**Challenge #3.1.B: Spell your name** ⸺ Can you put together a sequence of Drive
blocks so that it drives along the first letter of your name? What about your
whole name? _Hint:_ Besides in-place turns, you can also choose a curve with
a given angle and radius. When you're satisfied with the result, try attaching
a pen to the robot so it draws your name as it moves.
{: .notice--primary}

**Challenge #3.1.C: Satnav subtitles** ⸺ Previously, you've experimented with
the Print block. Add print blocks to your program to make the robot indicate
exactly what it will do. For example, make it say "Turning 90 degrees!" Where
do you put these Print blocks? Should they go before or after each Drive block?
{: .notice--primary}
