---
title: Pybricks 3.5 is here!
tags:
  - News
  - Block Coding
  - Xbox Controller
toc: true
toc_sticky: true
excerpt: >
  What's new in in Pybricks 3.5? Comment block, Xbox Controller rumble,
  keyboard input, and more!
header:
  teaser: /assets/images/news/new-comment-block-og.png
---

We're happy to announce that Pybricks version 3.5 is now available! This
release includes a number of new features and improvements. Here are some
of the highlights.

Even if you're using Pybricks already, you'll get the update automatically. No
action required!

You can find the full firmware [changelog here][changelog]. You can also see
the full overview of open and resolved [issues here][issues]. As always, if you
experience any issues, please let us know by creating a new issue. We'd love
to fix it for you.

# New Comment block

This has been a [much requested feature][request-comment-block], and it's
finally here! You can now add comments to your code to clarify what it does.
This helps you and others understand your code better.

{% include scaled.html
path="/assets/images/news/new-comment-block.png"
caption="The new comment block in Pybricks."
width="75%"
%}

Instead of making it a floating text box, we've opted for a dedicated comment
block. This way, comments will be inserted correctly in the generated code, and
it moves along when you move other blocks around.

# New drive base reset block

Until now, the drive base reset option was only available in Python. By popular
request, we've now made a block available as well. This can be really useful
when re-aligning your robot between runs if you don't want to stop your program.

{% include scaled.html
path="/assets/images/news/new-drivebase-reset-block.png"
caption="The new drive base reset block in Pybricks."
%}

# You can change the stop button

You can now change or disable the stop button. This allows you to use that
button for other purposes in your code. This can be great for making your own
menus in big FLL and WRO programs. It's also useful on hubs with only one
button, so you can still have some user interaction.

For example, the following program disables the stop button on the Essential
Hub. The button is instead used to change the color of the light.

{% include scaled.html
path="/assets/images/news/new-program-stop-block.png"
caption="Now you can disable the stop button and use it for something else."
%}

# Xbox Controller rumble support

We've added support for reading the buttons and joysticks of the Xbox
Controller in the previous release. But now you can also make the controller
rumble in order to create haptic feedback. This can be great for immersive
remote control driving!

{% include scaled.html
path="/assets/images/news/new-xbox-rumble-block.png"
caption="You can make the Xbox Controller rumble to create force feedback."
width="80%"
%}

# New block for keyboard input
To complement the print block, you can now also get input from the keyboard
by typing in the input/output pane. This can be useful to test your creations
by activating different movements depending on which key you press.

{% include scaled.html
path="/assets/images/news/new-input-block.png"
caption="You can now read keyboard input from the input/output pane."
%}


[changelog]: https://github.com/pybricks/pybricks-micropython/releases/tag/v3.5.0
[issues]: https://github.com/pybricks/pybricks-micropython/releases/tag/v3.5.0
[request-comment-block]: https://github.com/pybricks/support/issues/1349
