---
title: "Installing Pybricks"
excerpt: >
  How to install Pybricks on LEGO SPIKE Prime, SPIKE Essential, Technic, City,
  and BOOST. On Windows, Mac, Linux and Chromebook.
redirect_from:
  - /install/technic-boost-city
  - /install/spike-mindstorms
  - /learn-python
  - /install/todo
  - /install/
offline_use:
  image: /learn/getting-started/offline.png
  alt: Install the Pybricks firmware.
  width: 100%
  labels:
    - text: Tools
      x: 6%
      y: 42%
      location: above
    - text: Create app shortcut
      x: 29%
      y: 42%
      location: right
    - text: Ready for offline use
      x: 29%
      y: 75.5%
      location: right
beta_version:
  image: /learn/getting-started/offline.png
  alt: Install the Pybricks firmware.
  width: 100%
  labels:
    - text: Tools
      x: 6%
      y: 42%
      location: above
    - text: Check version
      x: 19%
      y: 70%
      location: below
    - text: Try new beta features
      x: 37%
      y: 58%
      location: right
firmware_restore:
  image: /learn/getting-started/install.png
  alt: Install the Pybricks firmware.
  width: 100%
  labels:
    - text: Tools
      x: 8%
      y: 40%
      location: right
    - text: Restore official LEGO firmware
      x: 36%
      y: 73%
      location: right
---

Now that you've decided to use Pybricks, it's time to open the Pybricks app
and install the Pybricks firmware on your hub.

If you prefer to get going right away, go
to <a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>.
Just follow the _Welcome Tour_ under _Help_ via the
menu (<i class="fas fa-cog"></i>). Otherwise, stick around and we'll take you through the steps.

If you are using EV3, please visit
the [legacy instructions](/install/mindstorms-ev3/installation/) instead.
{: .notice}

# The Pybricks "App"

The Pybricks Code editor
at <a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>
is a web page that looks and feels like an app. It includes everything you need
to create and run and programs, and manage your LEGO hub.

Once the page is fully loaded, you can use Pybricks offline.
For more convenience, you can click to _install as app_. This creates an app
shortcut for easy access to Pybricks.

Pybricks is saved offline in your browser. If you delete your
browser data, you need internet access again to load Pybricks.

{% include diagram.html data=page.offline_use %}



# Why update the firmware?

You can think of your LEGO hub as a small computer. Just like your computer
has an _operating system_ (like Windows or MacOS) to run _programs_ (like apps),
the hub has _firmware_ to run the programs that you make.

Out of the box, all LEGO hubs work in a different way. Pybricks makes them work
the same using the Pybricks firmware.

This enables all the unique features that Pybricks is known for, such as
compatibility with all motors and sensors, improved robot navigation, saving
your program on the hub, and so on.

{% include diagram.html data="diagram-hubs" %}

Fortunately, installing the Pybricks firmware is easy. You can recover to the
original firmware at any time. If you have any doubts about the installation process,
you can always try the [recovery process](#restoring-the-original-firmware)
first, just to be sure.

# Installing Pybricks on the hub

You can install Pybricks on any of the hubs shown above. To get started,
go to <a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>,
open the tools menu (<i class="fas fa-cog"></i>), and click _install Pybricks firmware_:

{% include diagram.html data="diagram-install" %}

Then follow the on-screen instructions in five steps:

1. Select your hub type and click _next_.
2. Here you'll see the various software licenses used in the firmware. Once
   you've read and accepted them, click _next_.
3. If you have more than one hub, choose a unique name to tell them apart
   later. Click _next_. (Classroom tip: Use easy to remember names such as
   animals or city names. Add matching stickers or labels to each hub.)
4. Here you'll see the instructions to put your hub in update mode. You can
   watch the video to see what each step looks like. On some computers, you'll
   see additional instructions to install an extra driver. Click _install_.
5. You'll get a popup window to connect to your device. Once you do, the update
   begins and you'll see an installation progress bar.

# Restoring the original firmware

The Pybricks installation process works just like a normal LEGO firmware
update. This is why restoring the original is so easy.

To recover the LEGO firmware, go to <a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>,
open the tools menu (<i class="fas fa-cog"></i>), and click _Restore official LEGO firmware_. Choose
your hub and follow the on-screen instructions.

{% include diagram.html data=page.firmware_restore %}

# Troubleshooting connectivity

If connectivity issues arise, you'll usually see a notification popup that
describes the problem. Be sure to follow the indicated instructions. If that
does not help, follow the instructions below.

- You should *not* attempt to connect to the hub via your computer's settings
menu. If you already did, just remove the hub from there and try again via the
app instead.

- You can refresh the app by pressing <kbd>Ctrl</kbd> + <kbd>F5</kbd>.

- If connection issues continue to persist, please describe the problem on our
  [forum](https://github.com/orgs/pybricks/discussions). Additional Bluetooth
  troubleshooting advice is available [here][ble trouble].

- Using other Bluetooth devices at the same time can cause interference
  resulting in errors in Pybricks Code, particularly Bluetooth keyboards/mice.
  Be sure to turn off any unused devices for the best experience.

- Many Bluetooth adapters on Windows have compatibility issues. We have had the
  best results with adapters that used the generic Microsoft Bluetooth drivers
  such as adapters that use Cambridge Silicon Radio (CSR 4.0) chips. You can
  help by reporting known working (and not working) adapters [here][win ble issue].

[win ble issue]: https://github.com/pybricks/support/issues/921
[ble trouble]: https://github.com/pybricks/support/discussions/270

# Trying new beta features (optional)

Most users should use <a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>, which is the stable version.
If you are connected to the internet, app updates will automatically
load when they become available.

If you are curious about trying the latest fixes or features before they are
finished, you can do so by clicking on _try new beta features_. This opens
a separate window, with separate projects.

{% include diagram.html data=page.beta_version %}

If you use block coding with a license code, you can sign in to both versions
at the same time.

You may be prompted to install a new beta firmware version as well. The
installation procedure works the same. When you go back to the stable version,
you can install its corresponding firmware again.

# Trying the nightly version (optional)

Advanced users and contributors who want to help test the latest features can
install a custom firmware. To do so, first start the firmware installation as
[usual](#installing-pybricks-on-the-hub).

Instead of selecting a hub on the
first dialog, choose _Advanced_ and select your _zip_ file with
the firmware. You can use the latest [_experimental_ firmware](https://nightly.link/pybricks/pybricks-micropython/workflows/build/master) files or the [source code](https://github.com/pybricks/pybricks-micropython) to build your own.
