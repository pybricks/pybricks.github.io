---
title: "Installing Pybricks on the SPIKE Prime Hub and the MINDSTORMS Inventor Hub"
sidebar:
  nav: "install"
---

![Powered Up hubs](/assets/images/primeinventorhub.png)

This page shows how you can install Pybricks on the *LEGO Education SPIKE
Prime/Essential*, and *LEGO MINDSTORMS Robot Inventor* using the [Pybricks Code]
interface.

You can reinstall the [original firmware][restoring] at any time
using [Pybricks Code].

## Installing the Pybricks firmware

Before you begin, turn the hub off and disconnect the USB cable. Follow these steps:

1. Go to [Pybricks Code].
2. Click the <i class="fas fa-cog"></i> icon on the left to open the *Settings
   & Help* pane if it is not already open.
3. Click the **Install Pybricks Firmware** button.
4. Follow the instructions on the screen.

## Start coding

With the firmware in place, you're ready to start coding. Check out our guide
on the [next page](/install/running-programs/).

## Additional tips & tricks

The sections below provide some additional tips to make using these hubs even
easier. You'll also learn how to restore the original firmware.

### Saving a program on the hub

Since firmware v3.2 (released at the end of 2022), no special action is needed
to save the program on the hub. The current program stays on the hub until you
download and run a different program.

Once you download and run a program from Pybricks Code, you can use the button
on the hub to start the program again. (Pressing the button will stop a program
if it is already running and start the program if no program is currently
running.)

When you turn off the hub, the program will be saved to flash memory and can
be started again using the button the next time the hub is turned on. (If you
remove the battery instead of using the button to power off, the program will
be lost.)

### Restoring the original firmware

[Pybricks Code] also has the ability to restore the official LEGO firmware to
these hubs.

Before you begin, turn the hub off and disconnect the USB cable. Follow these steps:

1. Go to [Pybricks Code].
2. Click the <i class="fas fa-cog"></i> icon on the left to open the *Settings
   & Help* pane if it is not already open.
3. Click the **Restore Official LEGO Firmware** button.
4. Follow the instructions on the screen.

The firmware version installed by *Pybricks Code* is likely not the most
recent version from LEGO, so the next time you connect to an official LEGO app,
you will be prompted to update the firmware to get the latest version.

### Troubleshooting connectivity issues

When connectivity issues arise, you'll usually see a notification popup that
describes the problem. Be sure to follow the indicated instructions. If that
does not help, follow the instructions below.

- You should *not* attempt to connect to the hub via your computer's settings
menu. If you already did, just remove the hub from there and try again.

- You can try the latest [beta version][Pybricks Beta] of our app.
  This version gets more frequent updates. It's possible we've fixed your
  issue already.

- You can refresh the app by pressing <kbd>Ctrl</kbd> + <kbd>F5</kbd>.

- If connection issues continue to persist, please describe the problem on
  our [support page].

### Trying out new features with Pybricks Beta (easy)

Major and minor updates to [Pybricks][Pybricks Code] are released several times
a year. But we work on new features all the time. To try new features sooner,
use [the latest beta version][Pybricks Beta].

Some features may not work yet, and they may still change before the final
release.

If you try the beta version, please [give us feedback][support page]!

### Installing the latest build (advanced)

*This section is only intended for advanced users who want to try the **very
latest** features or fixes. Many features may not work. To revert
to a stable or beta version, just re-install the firmware as you normally
would.*

Pybricks automatically provides the latest stable and tested firmware.
To get the most recent firmware build, log in to GitHub and go to
our [latest builds].
Download the firmware ZIP archive for your hub. In the firmware install dialog
in *Pybricks Code*, expand the *advanced* arrow. You can either click the box
to get a file open dialog or just click and drag the ZIP file into the box.
Then you can proceed as usual and the custom firmware file will be installed on
the hub.

To confirm that you've installed the version you wanted, run the following
script on your hub:

```python
from pybricks import version

print(version)
```

[restoring]: #restoring-the-original-firmware
[latest builds]: https://nightly.link/pybricks/pybricks-micropython/workflows/build/master
[support page]: https://github.com/orgs/pybricks/discussions
[Pybricks Code]: https://code.pybricks.com
[Pybricks Beta]: https://beta.pybricks.com
[Google Chrome]: https://www.google.com/chrome
[Microsoft Edge]: https://www.microsoft.com/edge

