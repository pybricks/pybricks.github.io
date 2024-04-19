
The car setup block takes care of centering the steering motor and makes it
easy to drive later on. Finally, we add the setup block for the Powered Up
remote.

The main program is quite simple. There is an infinite loop that sets the
steering and drive power based on the buttons you press. It uses the _ternary
block_ to set the steering to:
- 100% when you press the left **+** button,
- otherwise to -100% when you press the left **-** button,
- otherwise to 0%

Similarly, it sets the drive power to:
- 100% when you press the right **+** button,
- otherwise to -100% when you press the right **-** button,
- otherwise to 0%

You could achieve the same effect using conventional if-else blocks. You can
see this in the video below. The ternary block makes the code more compact and
easier to read.
