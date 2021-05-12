---
title: "Running Pybricks programs"
sidebar:
  nav: "install"
toc: true
---

Once the firmware is installed, you can start coding.

1. Go to [Pybricks Code](https://code.pybricks.com).
2. Use the *Bluetooth* button to connect to your *Pybricks Hub*.
3. Press run to start your program. 

![Pybricks Code](/assets/images/pybrickscode.png)

## Running an example program

To get started, just copy and paste this snippet:

{% include copy-code.html %}
```python
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# We'll use two motors. One is a dial
# to set the speed of the other motor.
motor = Motor(Port.B)
dial = Motor(Port.A)

# Say hello :)
print("Hello, Pybricks!")

# First, we'll move the dial to zero.
dial.run_target(500, 0, Stop.COAST)

while True:
    # Set the speed based on dial angle
    speed = dial.angle()*3
    if abs(speed) < 100:
        speed = 0

    # Run motor at desired speed
    motor.run(speed)

    # Wait briefly, then repeat
    wait(10)
```


## Using Pybricks offline

Instead of working in your browser, you can install Pybricks locally:

1. Open the settings tab with the ⚙ icon.
2. Click on *Install as App* and follow the on-screen instructions.

To uninstall, click the ⋮ menu in the top and
click *Uninstall*. Note that this only removes the app from your computer.
