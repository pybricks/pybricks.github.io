---
title: "Making your own task blocks"
excerpt: >
  Learn to build your own code blocks.
img_flow_blocks:
  image: /learn/flow-basics/task-blocks.png
  alt: Task blocks
  width: 100%
  caption: >
    Tasks combine multiple blocks to do
    something useful. This can help you organize your code.
  labels:
    - text: |
        Drag a new Task block
        onto the canvas.
      x: 32%
      y: 32%
      location: below
    - text: |
        Main program.
      x: 61%
      y: 58%
      location: right
    - text: |
        Call your task
        in your program.
      x: 28%
      y: 67%
      location: below
    - text: |
        The Task Caller block runs
        all the blocks of your task.
      x: 62%
      y: 78%
      location: below
    - text: |
        Add actions 
        to your task.
      x: 73%
      y: 45%
      location: right
    - text: |
        Choose a name
        and optional icon
      x: 65%
      y: 29%
      location: right
---

In addition to using the ready-made blocks, you can make your own blocks. This
lets you combine multiple blocks to perform a useful _task_. You can then use
your task multiple times in your program.
This technique helps you organize your programs as they get bigger.

# Creating tasks

You create a new task by placing an empty Task block on the canvas, a shown
below. You can drag one or more blocks into it that together make up your
desired task. For example, you can make a task that prints "Hello World" with
two pauses.

{% include diagram.html data=page.img_flow_blocks %}

You can give your task any name, but it's best to choose something brief and
descriptive. You can choose from several icons to help you better recognize
each of your tasks, but it doesn't change what the task does.

Once created, the task doesn't run all by itself. Rather, you decide when it
runs by placing the corresponding Task Caller block somewhere in your main
program. You can find it on the block palette, as shown above.

The simple tasks on this page work like so-called "My Blocks" as found in other
apps. As you'll see in the next sections, tasks can do a lot more
than just combining multiple actions.

# A closer look at program flow

To get some practice in making your own tasks, you'll now combine everything
you've learned so far. The next example sets up your drive base, makes the
robot drive straight and turn, and repeats it all to Square. You'll
create a task to drive in such a square so you can call it multiple times in
your program.

{% include block-program.html
path="L04_2_task_square"
caption="??."
width="100%"
%}

Your robot should now drive in a square, pause for two seconds, and drive in
another square.

**Challenge #4.2.??: Tracing your steps** ⸺  To get a better understanding of
how this program runs all of its blocks, insert Print blocks as shown below.
Before you try to it, write down the expected output and verify your
prediction. **Discuss** ⸺ Did you get it exactly right? If not, which steps did
you miss?
{: .notice--primary}


{% include block-program.html
path="L04_2_task_square_verbose"
caption="Program for challenge #4.2.??. Placing Print blocks throughout your
program can help you verify that it works as intended. If not, it helps you
find out where it goes wrong. The result should be as follows."
width="100%"
%}

```
Let's go!
---- Starting square ----
Straight
Turn
Straight
Turn
Straight
Turn
Straight
Turn
---- Completed a square ----
Let's go again!
---- Starting square ----
Straight
Turn
Straight
Turn
Straight
Turn
Straight
Turn
---- Completed a square ----
```
# Using multiple tasks

You can create as many tasks as you need to organize your program. It does not
matter where you place each task on the canvas. The following example program
keeps the _Square_ task and adds a task called _Twinkle_ that plays a well-known
melody.

{% include block-program.html
path="L04_2_task_twinkle"
caption="You can make more than one task to organize your code."
width="100%"
%}

A task may also call _other tasks_. In this example, the Twinkle task calls the
Square task at the end. How many times do you hear the melody when you run this
program? How many squares does the robot drive? Run the program to verify your
prediction.

**Challenge #4.2.??: Fast mode and slow mode** ⸺ Create two new tasks called
_Slow_ and _Fast_, each with a collection of Drive Base Configuration blocks.
The _Slow_ block should set low acceleration and speed values for straights and
turns. The _Fast_ block should set high values. Now you can conveniently change
speed profile midway throughout your program. Test it by driving one square
very slowly and one square very quickly. Where do you place the Task Caller
blocks?
{: .notice--primary}

# A task must not call itself

A task _should not call itself_. To see why, let's do a thought experiment.
Imagine putting up post-its for all of today's tasks and
then start doing your chores one by one. So far, so good.

But now imagine that one of your post-its said _put up another post-it with
this text and act on it right away_. With no chance to take it down, you'll
end up putting up more and more post-its until you run out of paper or space on
the wall!

How is this different from repeating actions forever? In a Repeat Forever block,
actions complete before they repeat. In this case, you'll be able to take your
post-it off the wall since the task is complete. You'll still be putting it
back on the wall until the end of time, but at least you won't run out of
paper!

**Challenge #4.2.??: An excursion into recursion** ⸺ Modify the _Square_ task
to make it call _itself_ as shown below. What do you think will happen? After
many laps, you should see an error in the output pane. **Research** ⸺ Read the error message and determine which word to search for online. What is
this technique called? Is it ever useful? Does this phenomenon occur anywhere in daily life?
{: .notice--primary}


{% include block-program.html
path="L04_2_task_square_recurse"
caption="Program for challenge #4.2.??. This task calls itself, which is
(almost) never a good idea."
width="80%"
%}




