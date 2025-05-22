---
title: "Advanced multitasking"
excerpt: >
  Dive deeper into the possibilities of the Multitask block.
---
This section covers several more advanced uses of the Multitask block.
You don't need these techniques for most programs, but they can be powerful and
help simplify your code in certain situations.

# Multitasking until one task is done

In the [previous section](/learn/flow-basics/multitasking/), all Multitask
blocks were configured to keep running until _all_ tasks (stacks of blocks)
placed in them had completed. Instead, you can make the Multitask block do things
simultaneously until _one_ task is done—whichever completes first.

This technique is useful for doing something in the background while you wait
for something else to finish, as shown in the following program.

{% include block-program.html
path="L04_4_multitask_one"
caption="Multitasking until one task is done. The light blinks until the motor is done moving."
width="80%"
%}

As before, the Multitask block will run the motor back and forth while at the
same time blinking the light. The light is set to blink forever, but the
Multitask block stops as soon as one task completes. So it stops when the motor
finishes moving back and forth. Then the Multitask block takes care of stopping
the other stack too, so the light stops blinking. Your program then continues
to run the blocks after the Multitask block, so you hear the sound. The light
has stopped blinking, but it is still red or green at this point. This example
adds a block to turn the light off.

This example may not seem very convincing, but this technique becomes very
useful when used with sensors. You can wait on two or more sensors at the same
time, but stop waiting as soon as one of them triggers. You'll learn to do this
in the next chapter.

# When tasks are cancelled

When you configure the Multitask block to run until only one task completes, it
will _cancel_ its remaining tasks that aren't complete yet. If such a task was
waiting on a motor movement to complete, the motor is stopped. The following
example does two things simultaneously:
- Run the motor one rotation and then print "Complete"
- Wait two seconds and then print "I got stuck!"

{% include block-program.html
path="L04_4_multitask_timeout"
caption="When you multitask until one task is done, the other incomplete
         task is cancelled. This technique is used here to move normally in
         most cases but stop the motor if it took too long to complete one rotation."
width="80%"
%}

Normally, the motor should complete the rotation in about a second. You'll see
only "Complete!" in the output window. The other task is cancelled in the
middle of the Wait block, so you never get the message about being stuck. But
if you slow or block the motor with your hands, it won't be ready after two
seconds. So the second task completes first. It will say "I got stuck" and
cancel the motor movement in the first task. This can be very useful if you
want to move a fixed distance but don't keep trying forever if you hit a
physical endpoint.

Likewise, Wait blocks or Beep blocks are stopped immediately. The stack of
blocks then stops running. This is unlike a Repeat block, which always runs
until the end. Any other block that doesn't have to wait on anything is allowed
to finish rather than forcefully cancelled. For example, if your code was doing
some math to add three numbers, it won't get cancelled somewhere in the middle.
If you're not entirely sure what gets cancelled or not, you can still control
what happens afterward. In the example above, you explicitly turned off the
light.

**Challenge #4.4.A: Backing up!** ⸺ Create a program similar to the example
above, but make a drive base drive backwards for 250 mm instead of turning
a single motor. The robot should back up by 250 mm but stop trying if it
doesn't get there in two seconds.
**Discuss** ⸺ When is this technique useful in robotics competitions? How is
this different from just driving in reverse for two seconds? What are
the pros and cons of either approach?
{: .notice--primary}

# Nested Multitask blocks

The Multitask block can be used like any other block, which means that it can
also be placed within another Multitask block, as shown below.

{% include block-program.html
path="L04_4_multitask_mixed"
caption="You can use a Multitask block within another Multitask block."
width="80%"
%}

**Challenge #4.4.B: Everything at once** ⸺ Analyze the example above before
you run it. What will it do? Can you definitively say which order the printed
messages will be in? If not, what does it depend on? Is it possible to use
multiple Start blocks instead of Multitask blocks? If not, how close can you
get to the same output? Which differences remain?
{: .notice--primary}
