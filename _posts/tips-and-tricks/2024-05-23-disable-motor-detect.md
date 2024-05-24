---
title: How to disable motor checks in multipurpose Pybricks programs
tags:
  - Block Coding
  - Python
  - Technic
  - City
  - Boost
  - SPIKE Prime
  - SPIKE Essential
toc: true
excerpt: >
  This article explains how to disable motor checks in multipurpose programs
  so that they run no matter which motors are connected, if any.
header:
  teaser: /assets/programs/check_override.png
---

If you forget to plug in a motor that you use in your program, you normally
see this tip to remind you, in the output window:

```
A sensor or motor is not connected to the specified port:
--> Check the cables to each motor and sensor.
--> Check the port settings in your script.
```

{% include block-program.html
path="check_motor"
width="75%"
caption="When you use a motor that is not plugged in, you'll see this message
in the output window."
%}

When coding, errors are not _bad_ but they are meant to _help you_ catch
mistakes early on.

# Why disable connection checks?

Most of the time, you'll want to keep it that way. After all, now your robot
won't drive off your desk with one motor still going while the other isn't
plugged in (yep - we've all been there!)

But sometimes you just want to make a general purpose program that runs
whether or not something is plugged in. For example, you might want to make a
single program to test basic motion in all your creations.

In this article we'll show you how to do this. You can do it with blocks or
with Python!

# Adding an extra module

To make this work, you'll import an extra module that lets you override
the usual checks. To do that,
download the file called <a href="/assets/programs/allow_missing_motors.py" download>`allow_missing_motors.py`</a>
and import it into the Pybricks editor so it
shows up under your files:

{% include scaled.html
  path="/assets/images/project/import_module.png"
  caption="Add the 'allow_missing_motors' module to your Pybricks files."
  width="90%"
%}

Because even block-based programs use Python under the hood, we can import this
module using the `import` block from the external tasks
category. This makes it skips the usual checks:

{% include block-program.html
path="check_override"
caption="You can disable motor checks to make multipurpose motor projects."
width="75%"
%}

There's no need to understand all the details in the Python module to use it.
The main things to remember are:
- You only need to add import block once as shown in the example above.
- Only programs that use this import are affected. Every other program works
  as usual and will always check the ports.
- You can setup the motors at the top as usual. For lack of better names, you
  can just call them the same as the respective port.
- If a block you use is not supported by your motor, or nothing is plugged in,
  your program will just ignore that block instead of raising an error.

# Making a simple battery box

Perhaps the simplest but useful example is to turn your hub into a simple
battery box, as shown below.

{% include block-program.html
path="check_battery_box"
caption="A simple 'battery box' program."
width="70%"
%}

This just turns the motors on if they are connected. They keep running until
you stop the program using the button on the hub.

As a result, you can start the motors by clicking the button, and click it
again to turn them off. Just like a good old battery box!

# Further exploration

With that extra module in place, you can easily get creative with your
multipurpose script, no matter what is plugged in. Can you create a program that...

- ... remote controls any of the ports?
- ... controls the motors with the hub button?
- ... changes the motor speed using the angle of motor?

# Using Python for your main script

You can use this same technique if you use Python for your main program instead
of blocks. If you look closely at the block program above, you can probably
guess how this works. Just add the following line _below_ your usual import
statements. That's it!

```python
from allow_missing_motors import Motor
```
