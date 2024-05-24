---
title: How to download multiple Pybricks programs with your own menu
tags:
  - Block Coding
  - Python
  - SPIKE Prime
  - MINDSTORMS Robot Inventor
toc: true
excerpt: >
  This is how you can install multiple Pybricks programs on the hub, and add
  a simple menu select one to run. This works on the SPIKE Prime Hub and the
  MINDSTORMS Robot Inventor Hub.
header:
  teaser: /project/spike-prime/spike-hubmenu-small.jpg
  og_image: /project/spike-prime/spike-hubmenu-og.jpg
---

Normally, only one program is saved on the hub. This usually makes it easy to
find and start your latest project. And it's especially practical on hubs
without a display.

But the SPIKE Prime Hub and the MINDSTORMS Robot Inventor hub have plenty of
space for multiple programs. Downloading multiple programs is useful in
competitions like FLL or WRO, where you might want to break down your programs into
several missions.

This method differs from the conventional program "slots", but it's easy to
set up and you have much more flexibility in how your mission programs work.

{% include youtube.html videoid="J_mftE2OUdY" %}

This article shows how you can download multiple programs, and add a simple
menu that helps you start your selected program using the buttons on the hub.

You can use numbers in your menu, but also letters and symbols. This is often
way easier to remember on competition day!

# Multiple mission programs

For the purpose of this article, let's assume we have three "mission" programs.
These programs are very simple, but you can do this with programs of any size.

If you prefer to use Python for your missions, that's fine too.

{% include block-program.html
path="hello_world"
caption="The 'hello_world' program"
width="70%"
%}

{% include block-program.html
path="sound"
caption="The 'sound' program"
width="60%"
%}

{% include block-program.html
path="light"
caption="The 'light' program"
width="55%"
%}

# Adding a menu program

The next step is to add a "main program" that acts as your own menu.
In this example, we'll make a menu with the letters:
- ``H`` to start the `hello_world` program
- ``S`` to start the `sound` program
- ``L`` to start the `light` program

To run it, create a new _Python_ program. You can pick any name, such as `menu`
and paste the following code into it.

{%
  include block-program-as-python.html
  show_intro=false
  path="menu"
%}

When you run it, you'll see the letter ``H`` on the hub. You can toggle through
the other letters with the left and right buttons. Press the center button to
start one of them.

You can start this main menu again with the start button.

Although this main menu was made using Python, you'll find that it is very easy
to adapt. Just change the letters or program names to match your mission. You
can also add extra programs or remove a few.

If you'd rather use a dedicated block for this menu instead of Python, feel
free to let us know on the [discussion
forum](https://github.com/orgs/pybricks/discussions).

# How did it work?

The Python program you just ran has two main parts:

- The `hub_menu` function combines the display and the buttons to let you pick
  a symbol. 
- One of the `import` statements will run the respective mission program.

Whenever a Pybricks program contains an import statement, the respective file
is downloaded to the hub along with your main program. So, by downloading your
menu program to the hub, it also downloaded the `hello_world`, `sound` and
`light` programs along with it.

You can still download and run each program separately during testing. Just
remember to download the `menu` program to the hub again afterwards!

# Caveats

This extra section is only needed if you want to write more advanced menus. If
you're happy with the menu technique above, just skip this section.

There is nothing inherently special about this "menu program". It is a Python
program like any other. Import statements work just like they normally do. This
offers great flexibility, but it can result in some surprises if you're new to
Python.

The approach used above works great for a basic menu, but you might want to
organize your code a bit differently in case you want to take this menu
technique even further.

The `import` statement will run a program only the first time, even if you run
the same `import` again in the same program. This is why programmers would
usually write the "mission" as a _function_ (a task) instead. You could import
that function and call it from your menu program as many times as you like.

# Multiple programs on other hubs

You can use this same technique of using `import` statements to combine
multiple programs on any hub. The other hubs don't have a display and multiple
buttons, however, so you may need to get creative to determine the selected
program.

For example, you could make the hub cycle through a set of colors with the hub
button, and then choose a particular program by pressing the button a bit
longer.
