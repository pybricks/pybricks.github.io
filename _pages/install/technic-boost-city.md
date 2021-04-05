---
permalink: /install/technic-boost-city/
title: "Installing Pybricks on the Technic Hub, BOOST Move Hub, and City Hub"
sidebar:
  nav: "install"
toc: true
---

![Powered Up hubs](https://docs.pybricks.com/en/latest/_images/powereduphubs.png){:width="75%"}

This page shows how you can install Pybricks on the BOOST *Move Hub*, the *City
Hub*, and the *Technic Hub* using the [Pybricks Code][Pybricks Code] interface.

You can reinstall the [original firmware][restoring] at any time
using the official Powered Up app.

# Requirements

* A BOOST Move Hub, City Hub, or Technic Hub.
* A Windows, Mac, Linux, or Android device.
* Bluetooth Low Energy (BLE). Make sure that Bluetooth is on.

If you don't have BLE, the coding interface will inform you during the
installation step. In that case, you can try using a low-cost USB Bluetooth
Dongle that supports Bluetooth Low Energy.

# Installing a compatible browser

Writing Pybricks programs requires a web browser with web Bluetooth
functionality, such as:

* [Google Chrome][Google Chrome]
* [Microsoft Edge][Microsoft Edge]
* Chromium

If you use Linux, enable *Experimental Web Platform features* on
the ``chrome://flags/`` page. It's already enabled on Windows and Mac.

# Installing the Pybricks firmware

Before you begin, turn the hub off. The update works best with fresh batteries.
If you use the City Hub, you must unplug all motors and sensors. Follow these
steps:

1. Go to [Pybricks Code][Pybricks Code].
2. Press and hold the hub button. Wait for a blinking pink light.
3. While you hold it, click the *firmware update* button.
4. Select the *LEGO Bootloader* and click *Pair*.
5. Wait until the light turns off, and then blinks red/green/blue.
6. Release the button and wait for the installation to finish.

These steps are summarized in this video:

<video controls src="/assets/videos/install.mp4" width="100%"></video><br />


# Running programs

Once the firmware is installed, you can start coding! Use the *Bluetooth*
button to connect to your *Pybricks Hub*. Then press run to
start your program. 

![Pybricks Code](https://docs.pybricks.com/en/latest/_images/pybrickscode.png)


To get started, just copy and paste this snippet::

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

# Next steps

Now that you've learned how to install Pybricks and run programs, check out
the steps below to make Pybricks coding even easier. We'll also show you how
you can restore the original firmware.

## Saving a program on the hub

The Move Hub, City Hub, and Technic Hub do not have separate storage space
for user programs. This means your program is erased after it is done running.
Fortunately, you can still save one program on the hub, by including it in the
firmware. To do so:

1. Open the settings tab with the ⚙ icon.
2. Activate the *Include current program* switch.
3. Update the firmware as you did before. Now, your current program will be
   included.
4. Now can start and stop your program with the green button.
   No connection required!
5. You can still download and run new programs with the run button as usual.

This is a bit of a slow process to do each time. We recommend to
use the run button to run your code most of the time. When you are
happy with your final program, follow the steps above to save it on the hub.

## Using Pybricks offline

Instead of working in your browser, you can install Pybricks locally:

1. Open the settings tab with the ⚙ icon.
2. Click on *Install as App* and follow the on-screen instructions.

To uninstall, click the ⋮ menu in the top and
click *Uninstall*. Note that this only removes the app from your computer.
To restore the original firmware on the hub, see the next section.

## Restoring the original firmware

Pybricks uses the same update procedure as the LEGO apps. The only difference
is which firmware file we upload. This means you can go back to the original
firmware any time. As shown in the video below, just put the hub in update mode
and connect using a LEGO app.

<video controls src="/assets/videos/restore.mp4" width="100%"></video><br />

This video shows the Powered Up app in *create* mode. It has firmware for all
hubs. As usual, you may need to restart the app to detect the hub. If it fails,
try again with fresh batteries.

## Installing the latest build

*This section is only intended for developers who want to try the
latest features. Some features may not work. To revert
to a stable version, just install the firmware as you normally would.*

Pybricks Code automatically provides the latest stable and tested firmware.
To get a more recent version, log in to GitHub and go to
our [latest builds][latest builds].
Click on the desired build and go to `Artifacts`.
Download the firmware ZIP archive for your hub. To install it, drag this file
*onto* the firmware update button in Pybricks Code. The update now proceeds as
usual.

[restoring]: #restoring-the-original-firmware
[latest builds]: https://github.com/pybricks/pybricks-micropython/actions?query=is%3Asuccess+branch%3Amaster+workflow%3ABuild
[support page]: https://github.com/pybricks/support/issues/
[Pybricks Code]: http://code.pybricks.com/
[Google Chrome]: https://www.google.com/chrome/
[Microsoft Edge]: https://www.microsoft.com/en-us/edge

