---
title: Playing Tic Tac Toe with SPIKE Essential
tags:
  - Block Coding
  - Python
  - SPIKE Essential
toc: true
excerpt: >
  Learn to build and program a simple Tic Tac Toe game and get inspired to
  make your programs to play games.
header:
  teaser: /project/spike-essential/spike-tic-tac-toe_small.jpg
  og_image: /project/spike-essential/spike-tic-tac-toe-og.jpg
---

A good way to practice more interesting coding concepts is to mimic a well
known board game. There's no stress to get a robot mission right, and it's
easy to check if your code behaves according to the rules of the game.

{% include scaled.html
  path="/project/spike-essential/spike-tic-tac-toe.jpg"
  path_small="/project/spike-essential/spike-tic-tac-toe_small.jpg"
%}

In this article, we'll show you how you can make Tic Tac Toe game for two
players!

{% include youtube.html videoid="lTucJIUhj3k" %}

# Requirements

If you want to build exactly the same Tic Tac Toe game, you'll need the
{% include setlink.html id=45345 %} set.

However, you can build it with any hub if you combine it with the Color Light
Matrix to display the game.

To build, place the motor and the hub on the base plate using some bricks and
pins, as shown above. Add a beam to the motor to indicate whose turn it is.

## Running and playing the game

Instead of noughts and crosses, you'll use the blue and green colors
to indicate each player's turn on the SPIKE Color Light Matrix.

You'll use the hub button to choose your position, and then confirm your choice
by handing the flag to the other player for their turn. You can see this in the
video above.

The example below includes numerous comment blocks to help you illustrate how
this program works. Have fun!

{% include block-program.html
path="tic_tac_toe"
path_small="/assets/programs/tic_tac_toe_small.png"
caption="The Tic Tac Toe program."
%}

{% include snippets/pybricks-intro.md %}

{%
  include block-program-as-python.html
  show_intro=true
  path="tic_tac_toe"
%}
