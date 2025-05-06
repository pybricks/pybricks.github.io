---
title: "Waiting and repeating"
excerpt: >
  Learn to use the Wait Time block and the Repeat Times block to control the
  flow of your program.
img_inventor_square:
  image: waiting-repeating/inventor-square.svg
  width: 80%
  caption: >
      Driving in a square means driving four straights and making four 90-degree
      turns. You could use eight Drive blocks, but is there a better way?
img_inventor_square_rounded:
  image: waiting-repeating/inventor-square-rounded.svg
  width: 80%
  caption: >
      Can you change the square program to make it drive rounded corners? How
      long should the straights be, given the desired square width W and corner
      radius R?
img_flow_palette:
  image: /learn/flow-basics/flow-blocks.png
  alt: Flow blocks
  width: 100%
  caption: >
    Flow blocks include wait blocks and repeat blocks. They control how your
    program flows from top to bottom. You'll learn to use some of these blocks
    later, when we introduce sensors.
  labels:
    - text: Wait for a fixed duration
      x: 37%
      y: 28%
      location: right
    - text: Wait for a condition (see next chapter)
      x: 37%
      y: 38%
      location: right
    - text: Wait forever
      x: 33%
      y: 48%
      location: right
    - text: Repeat several times
      x: 33%
      y: 60%
      location: right
    - text: Repeat with a condition, or forever
      x: 39%
      y: 78%
      location: right
    - text: |
        Flow
        blocks
      x: 12%
      y: 50%
      location: left
---

So far, you've built programs as a stack of blocks for the robot to run.
In these programs, blocks run one by one, as the execution flows from top to bottom.

In practice, robots rarely execute a long, fixed list of actions from start to
finish. Robots often need to repeat some actions or decide to skip actions
depending on what their sensors see. You control how the code execution flows
from top to bottom with _Flow blocks_. A few Flow blocks are shown
below.

{% include diagram.html data=page.img_flow_palette %}

You've already learned to use the Wait Time block. It pauses the stack of blocks for
the specified duration. This chapter introduces the Wait Forever block as well.

You'll then learn to use the Repeat Times block to execute several actions
multiple times. In the next sections of this chapter, you'll learn how to
[group frequently used actions](/learn/flow-basics/tasks-functions/)
in a dedicated task block. You'll also learn how to run multiple actions [at
the same time](/learn/flow-basics/multitasking/).

# Waiting forever

In Pybricks, the program ends when the last block in your program completes.
Motors will be stopped, and the hub menu reappears. To keep your program
running even after it completes, add the Wait Forever block to your program, as
shown below. This mimics the standard behavior in Scratch.

{% include block-program.html
path="L05_1_wait_forever"
caption="The Wait Forever block keeps the program going when all other blocks are complete."
width="60%"
%}

In this example, the hub light turns red for a second and then turns green.
Because of the Wait Forever block, it stays green forever, until you press
the stop button. Without this block, the program would end immediately after
turning the light green, leaving no time for you to see it.

You cannot attach any blocks to the bottom of the Wait Forever block, as they
would never run.

# Repeating actions several times

Imagine you're walking along a square-shaped path, as shown below. As you walk,
you follow a certain pattern over and over again: go straight, then turn right,
go straight, turn right, and so on.

{% include diagram.html data=page.img_inventor_square %}

To create this sort of behavior with your robot, you could use one Drive block
to go straight and another to turn right. To make one complete square and return
to its starting position, you would need to use these two blocks four times, for
a total of eight blocks.

Rather than using eight blocks, it's much easier to use the Repeat Times block, which
lets you repeat sequences of blocks that are placed within it. The following
program creates the square pattern by repeating a straight and a turn four
times.

{% include block-program.html
path="L05_1_square"
caption="Drive in a square shape by repeating the straight and the turn four times. This example uses the Repeat Times block."
width="100%"
%}

**Challenge #4.1.A: Chicken or the egg** ⸺ Should the straight come first or
the turn? Will the robot follow a different path if you swap them?
Draw your prediction on a piece of paper and swap the blocks to test your hypothesis.
{: .notice--primary}

**Challenge #4.1.B: Cutting corners** ⸺ Change the square program to drive
with rounded corners instead of in-place turns, as shown below. Use the
_continue_ option in the Drive block to blend the paths together. **Discuss** ⸺
Why do you have to reduce the lengths of the straights to maintain the same
size of the square? Can you come up with a formula to calculate the length of
the straights, given the width (W) and corner radius (R)? Does your formula
still work for large corners or small squares? If not, when does it break down?
What shape does the square turn into at this breaking point?
{: .notice--primary}

{% include diagram.html data=page.img_inventor_square_rounded %}

You can repeat any type of block, not just Drive blocks. The following example
illustrates how you can repeatedly print text or change the hub light color. By
adding Wait Time blocks after changing the light color, you create your own blink
pattern.

{% include block-program.html
path="L05_1_repeat"
caption="Create a blink pattern or repeat other actions."
width="60%"
%}

# Repeating forever

So far, you've repeated actions a fixed number of times. Sometimes, you'll want to repeat
actions over and over without stopping. For example, you might want to keep blinking
a light or keep driving a certain pattern.

You can repeat actions forever with the Conditional Repeat block, as shown below.
You'll learn the meaning of the ``while True`` condition in the next chapters. For
now, just remember that this block repeats any blocks placed within it forever by default.
The actions repeat until you press the hub center button or the stop button in the app.

{% include block-program.html
path="L05_1_repeat_forever"
caption="Blinking the hub light forever with the Conditional Repeat block.
         If you leave the 'while True' condition unchanged, it just
         repeats the blocks placed within it forever."
width="60%"
%}

**Challenge #4.1.C: It's all a blur** ⸺ Reduce the wait duration as shown
below. Now the light changes color hundreds of times per second. What is the
result? This example creates a 50-50 mix of red and green. Why? Can you make it
75% green and 25% red? At what point does the light start to blink instead
of blending smoothly?
 **Research** ⸺ Mixing light colors is very different
from mixing paint colors. Write a one-page essay describing the differences.
What are primary colors, and what happens if you mix them in the case of paint or
light? How can you create a white light? Create a program to try it out.
{: .notice--primary}

{% include block-program.html
path="L05_1_repeat_forever_fast"
caption="Program for challenge #4.1.C. By reducing the duration in the Wait
blocks, the light color changes so quickly that the red and green light appear
to blend together. This technique is also used behind the scenes whenever you
choose a color that isn't a primary color, such as cyan or orange. In that case,
code built into the hub takes care of blinking the color repeatedly, so you don't have to do
it in your own program."
width="60%"
%}

# Repeating... repeatedly

In the square example, the Repeat Times block was used to repeat two Drive blocks four
times, giving a total of eight movements. After that, the program continues with
blocks attached below it. For example, you could add a Beep block so you can
hear it when the square completes.

Repeat blocks can be moved around like normal blocks. Any blocks placed within
it just move along. Likewise, you can place one Repeat Times block inside
another repeat block. Try this out by creating the following program.

{% include block-program.html
path="L05_1_square_repeat"
caption="Drive in a square forever, with beeps before and after each square."
width="100%"
%}

This program makes the robot play a low-pitch sound, drive in a square shape, and then
play a higher-pitch sound. This whole sequence repeats forever.

**Challenge #4.1.D: Chicken or the egg, revisited** ⸺ With the program above,
you'll hear two beeps between successive squares. Perhaps surprisingly, you
hear the higher-pitch beep first. Why is that?
{: .notice--primary}

**Challenge #4.1.E: Try again** ⸺ Replicate the program shown above but 
swap the two repeat blocks. The outer one should repeat 4 times and the inner
one should repeat forever. Now you don't hear a sound after each square, even
though the Beep blocks are still there. Why is that? **Hint** ⸺ Add Print
blocks throughout your program with different text messages to help you see which
blocks are running. Why does it never get to the second Beep block in this case?
{: .notice--primary}
