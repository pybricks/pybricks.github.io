---
title: "Making basic programs"
excerpt: >
  What does it take to build a program? Learn to set up your hub, motors and
  sensors and make your robot move with precision.
redirect_from:
  - /learn/movement-sound-light/
img_setup_1:
  image: /learn/movement-sound-light/basics-motor-setup-1.png
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
  image: /learn/movement-sound-light/basics-motor-setup-2.png
  alt: Setup step 2
  width: 100%
  caption: >
    2. Give each motor a name. Since they'll be driving the wheels on the Starter
    Bot, let's call the one on port A <i>left wheel</i> and the one on port B
    B <i>right wheel</i>. If you look at the left wheel, you'll notice that it
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
  image: /learn/movement-sound-light/basics-motor-setup-3.png
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
    - text: Select both motors
      x: 31%
      y: 72%
      location: below
    - text: |
        Choose wheel diameter and distance
        between wheel ground contacts.
      x: 70%
      y: 72%
      location: below
img_setup_4:
  image: /learn/movement-sound-light/basics-motor-setup-4.png
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
  image: /learn/movement-sound-light/basics-motor-setup-5.png
  alt: Setup step 5
  width: 100%
  caption: >
    5. Error messages can help you find some mistakes early. To try it,
    run the program again with one of the cables in the wrong port.
  labels:
    - text: |
        A motor is not
        connected correctly
      x: 62%
      y: 62%
      location: right

img_setup_6:
  image: /learn/movement-sound-light/basics-motor-setup-6.png
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

img_setup_comments:
  image: /learn/movement-sound-light/basics-comment-block.png
  alt: Comment block
  width: 100%
  caption: >
    Comments help you document your work. When you review your code later,
    you'll be able to see how it works and why you made it that way.
  labels:
    - text: Other blocks
      x: 12%
      y: 82%
      location: right
    - text: Comment block
      x: 34%
      y: 28%
      location: right
    - text: Document your work
      x: 50%
      y: 65%
      location: left

img_setup_select:
  image: /learn/movement-sound-light/basics-select.png
  alt: Selecting multiple blocks
  width: 100%
  caption: >
    Comments help you document your work. When you review your code later,
    you'll be able to see how it works and why you made it that way.
  labels:
    - text: |
        Hold shift, then drag
        to create a selection.
      x: 75%
      y: 70%
      location: above
    - text: |
       Right-click or
       tap and hold
      x: 25%
      y: 72%
      location: left
    - text: Copy or delete
      x: 40%
      y: 84%
      location: below
---

In this chapter, you'll learn how to set up your programs for the StarterBot
you've just built. You'll also experiment with basic movements and learn
to verify the results.

# Setup and the main program

Each Pybricks programs consists two two parts:
- **Device setup**: Here you describe how your robot _is built_ and how the
  devices are connected to the hub.
- **Program**: Here you describe what the robot _should do_.

To better understand how this works, let's build an example program using the
steps below. Connect to your robot, and run the finished program. 

{% include diagram.html data=page.img_setup_1 %}

{% include diagram.html data=page.img_setup_2 %}

{% include diagram.html data=page.img_setup_3 %}

{% include diagram.html data=page.img_setup_4 %}


# Verifying and troubleshooting
Connect to the robot and run your program. Your robot should drive forward by
250 mm (about 10") and then reverse, ending up where it started. Otherwise:

- If it didn't move at all, be sure to check the cables and the ports you selected, as
shown below.
- If it started by turning or reversing instead of moving straight
forward and back, check the directions in step 2 above.
- Place a ruler next to the robot. If it drove too far or not far enough,
  measure the wheel diameter again.

{% include diagram.html data=page.img_setup_5 %}

Running a very basic program with just a few movements is a good way to check
that your setup is configured properly.

This setup will be a big time saver when you create larger programs later on.
If you change your design including the cables, all you have to do is change
one port in the setup, rather than changing it throughout your entire program.

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

When changing the settings, it's best to do so from left to right as well, because
other settings may change when you do. For example, if you select _straight_,
an option appears to choose how many millimeters. But if you select _turn_, an
option appears to choose how many degrees.

# The comment block

No matter how simple your program is, it is _always_ a good idea to document
your work. Code comments help you document your work for yourself and others.
Even if a design choice appears obvious today, a comment will help you remember
a few weeks later.

{% include diagram.html data=page.img_setup_comments %}

Some comments can be descriptive. They might summarize what a sequence of blocks
do. Other comments can describe _why_ you've done it in a particular way. You
can also describe the required conditions that are needed to run your program.
Comments are filtered out before your code is sent to the robot, so
comments have no impact on performance or robot code size.

It is possible to leave a comment block floating on the canvas if you need to,
but it is best practice to attach it like a normal block. This way, it moves
along with your code automatically when you add other blocks above or below
it.

# Working with the code canvas

You can select a block by clicking or tapping on it. Hold shift and click
additional blocks to select more. You can also hold shift to encircle a larger
group of blocks, as shown below.

{% include diagram.html data=page.img_setup_select %}

You can copy a selection via the right-click context menu, or use familiar
keyboard shortcuts such as <kbd>ctrl</kbd>+<kbd>c</kbd>
and <kbd>ctrl</kbd>+<kbd>v</kbd>.

Use <kbd>Delete</kbd> to delete selected of blocks. Alternatively, drag them
back onto the block palette or into the trash can. If you change your mind,
click on the trashcan to see deleted blocks.
Note that the trash will be emptied when you close your program or switch to
a different program.

Use the familiar shortcuts <kbd>ctrl</kbd>+<kbd>z</kbd> (or similar) to undo
changes you've made.

# Further exploration

In this chapter, you've learned to build a program to make your robot move.
You've learned how to change settings and to document your work with comments.
You've also explored how to select and modify blocks on the canvas. The
following challenge will help you practice your skills.

**Challenge #3A: Living on the edge** ⸺ Pick a fixed starting point on your
desk and measure the distance to the edge of your desk. Tell the robot to drive
exactly that distance and back again. _Tip:_  On your first try, to reduce
the value slightly. Be prepared to catch you robot if it falls. Safety first!
When you're away from the computer, you can stop the program using the hub
button.
{: .notice--primary}

**Challenge #3B: Spell your name** ⸺ Can you put together a sequence of Drive
blocks so that it drives along the first letter of your name? What about your
whole name? _Hint:_ Besides in-place turns, you can also choose a curve with
a given angle and radius. When you're satisfied with the result, try attaching
a pen to the robot so it draws your name as it moves.
{: .notice--primary}

**Challenge #3C: Satnav subtitles** ⸺ Previously, you've experimented with
the Print block. Add print blocks to your program to make the robot indicate
exactly what it will do. For example, make it say "Turning 90 degrees!" Where
do you put these Print blocks? Should they go before or after each Drive block?
{: .notice--primary}
