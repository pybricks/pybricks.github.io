---
permalink: /install/mindstorms-ev3/beyond-micropython
title: "Using EV3 Beyond MicroPython"
sidebar:
  nav: "install"
toc: true
---

MicroPython runs on top of [ev3dev][ev3dev], which is a specific version of
Linux. Linux is an *operating system*. (Other popular operating
systems are Microsoft Windows and Apple macOS.) This means that your EV3 is
almost like a real computer, just much smaller.

## The Linux command line

Although your EV3 Brick is quite like a real computer, you do not interact with
it using a big screen and a mouse. Instead, you can access files and programs
on it using the *command line*. It is also called the *terminal*.

Follow the steps shown below to access the command line. Now
you can enter commands by typing them in and pressing enter.

![](/assets/images/terminal_label.png)

### Running basic commands

For example, if you type the following command and press enter::

```
ls
```

then you will see the contents of the current folder. The figure above
shows the result: it listed the project folder of the ``getting_started``
project that we just ran.

If you type the following command and press enter::

```
exit
```

then the command line will be closed. Alternatively, click the garbage icon
in the terminal menu.

You can copy text from the command line by selecting it and
then pressing ``ctrl`` + ``shift`` + ``c``.
You can paste text into the command line
using ``ctrl`` + ``shift`` + ``v``.

### Running commands as an administrator

Some commands require a password to run. This is similar to administrative
tasks on your computer or tablet, such as installing a new app. These commands
work like any other command, but you add ``sudo`` in front of
them.

As an exercise, you can run the following command to turn the EV3 Brick off:

```
sudo poweroff
```

You will be prompted for a password. Type ``maker`` and then press ``Enter``.

Only run commands with ``sudo`` if you know what you are doing!

### Learning more about the command line

To learn more about the command line and many of the available commands, we
recommend reading the beginner-friendly free ebook
called [The Linux Command Line][tlcl].

To learn more about ev3dev-specific tips and tricks, visit the [ev3dev][ev3dev]
website.

## Changing the EV3 Brick name

When you search for your EV3 using Visual Studio Code, you see all EV3 Bricks
listed by their name. By default, all EV3 Bricks are named *ev3dev*. Follow
these steps to change that name:

   1. Open Visual Studio Code and connect to your EV3 as usual.
   2. Read the steps above about running commands as an administrator.
   3. Think of a good name. In this example, we'll
      call it ``autonomous-vehicle2``
   4. Enter the following command and press enter:
      ```
      sudo hostnamectl set-hostname autonomous-vehicle2
      ```

   5. Reboot the EV3 Brick for the change to take effect.
   6. You may need to reboot your computer as well.

EV3 Brick names should only contain lowercase letters ``a`` through ``z``,
the digits ``0`` through ``9``, and the hyphen ``-``. It must start with a
letter or digit. It cannot include spaces or other symbols.

[ev3dev]: https://www.ev3dev.org/
[tlcl]: http://linuxcommand.org/tlcl.php
