---
title: Using Pybricks on Linux
tags:
  - Python
  - Block Coding
  - Technic
  - City
  - Boost
  - SPIKE Prime
  - MINDSTORMS Robot Inventor
  - SPIKE Essential
toc: true
excerpt: >
  Tips and tricks for using Pybricks successfully on Linux. With udev rules and
  snap configurations for Chromium.
header:
  teaser: /assets/images/pybricks-code-linux.png
redirect_from:
- /projects/tutorials/dev/tools/linux/
---

![Pybricks on Linux](/assets/images/pybricks-code-linux.png)

You can [create programs](/learn/getting-started/pybricks-environment/) on
Windows 10 or 11, macOS, Linux, Android, or ChromeOS. This page covers the
additional configuration you'll need to use Pybricks effectively on Linux.

The Pybricks developers use Linux daily, so we definitely wanted to make sure
this works well!

# Choosing an editor or browser

The simplest way to get started is to use the web-based Pybricks Code editor at
<a href="https://code.pybricks.com/" target="_blank">code.pybricks.com</a>. You
can also use [your preferred local editor](/project/pybricks-other-editors/).

If you use the web-based interface, we recommend using Chromium. You can
install it using your preferred package manager. On Ubuntu for example, you
can do:

```
sudo snap install chromium
```

Google Chrome works as well. Other Chromium-based web-browser may or may not
support Web Bluetooth. Notably, Opera, Vivaldi and Brave do not support Web
Bluetooth.

Web Bluetooth is not officially supported on Linux and requires Experimental
Web Platform features to be enabled. Copy and paste the following in the
address bar, set it to _Enabled_ and restart the browser.

```
chrome://flags/#enable-experimental-web-platform-features
```

If you use Chromium as a snap package, you may get an error when you try to
install the firmware on a SPIKE Prime, SPIKE Essential, or MINDSTORMS Robot
Inventor hub via USB. To resolve this, enable access to USB devices:

```
sudo snap connect chromium:raw-usb
```

# Adding udev rules on Linux

This step is only needed for LEGO hubs with USB, such as SPIKE Prime, SPIKE
Essential, and MINDSTORMS Robot Inventor.

By default, Linux does not allow the use of unknown USB devices, so you need to
add `udev` rules for your hubs. Pybricks provides a couple of ways to do this.

If you are using an Ubuntu-based Linux distro, you can install the
`pbrick-rules` package from the Pybricks PPA. This method has the advantage of
automatic updates.

{% include copy-code.html %}
```
sudo add-apt-repository --update ppa:pybricks/ppa
sudo apt install pbrick-rules
```

You can alternately install the rules using the `pybricksdev` command line tool:

{% include copy-code.html %}
```
pipx run pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules
```

If neither of these options is suitable, you can manually copy [this
file](https://github.com/pybricks/pybricksdev/blob/master/pybricksdev/resources/99-pybricksdev.rules)
to `/etc/udev/rules.d/99-pybricksdev.rules`.

After installing the `udev` rules, disconnect any affected devices and plug them back in. 
If this doesn't seem to work, try rebooting.




