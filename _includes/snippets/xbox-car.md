
The car setup block takes care of centering the steering motor and makes it
easy to drive later on. Finally, we add the setup block for the Xbox Controller.

The main program is quite simple. There is an infinite loop that sets the
steering and drive power based on the analog inputs.

Steering (-100% to 100%) is controlled with the left horizontal stick. The
drive power is controlled with the right trigger minus the
left trigger. This ranges the power level from -100% (reverse) if the left
trigger is fully pressed, all the way to 100% (forward) if the right trigger
is pressed.
