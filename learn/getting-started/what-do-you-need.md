---
title: "What do you need?"
excerpt: >
  What do you need to build and program a robot? Learn about hubs, motors,
  sensors, and the device you need for coding.
redirect_from:
  - /learn/getting-started/
header:
  teaser: /learn/getting-started/tablet.jpg
requirements:
  image: /learn/getting-started/tablet.jpg
  alt: Install the Pybricks firmware.
  width: 100%
  labels:
    - text: Sensor
      x: 18%
      y: 28%
      location: above
    - text: Hub
      x: 20%
      y: 45%
      location: left
    - text: Motor
      x: 25%
      y: 75%
      location: below
    - text: LEGO elements
      x: 65%
      y: 80%
      location: below
    - text: Device to make programs
      x: 73%
      y: 19%
      location: above
  caption: >
      Example of a LEGO robot with a device for coding. This picture shows a
      SPIKE Prime robot with an Android tablet, but you can use other hubs
      and smart devices, as you'll see below.
---

Put simply, you'll need a LEGO hub, elements to build a robot, and a
computer or tablet to create programs. This page helps you find everything you
need. For each of these requirements, you'll have several options to choose
from. 

{% include diagram.html data=page.requirements %}

**Tip**: If you've worked with SPIKE Prime (45678) or MINDSTORMS (51515)
before, you'll have everything you need. Still, read on to get a good overview
of the required components. You'll find other more budget friendly options
below too.
{: .notice--info}

# Choosing a device for programming

You can create programs on Windows 10 or 11, macOS,
[Linux](/project/pybricks-on-linux/), Android, or ChromeOS. You can use a PC,
laptop or tablet. Phones work too, but they are often too small to be useful.

Almost all modern laptops and tablets have builtin Bluetooth support. If your
device does not support Bluetooth or if it does not work well, you can buy a
low cost USB Bluetooth dongle. If you use SPIKE Prime, SPIKE Essential, or
MINDSTORMS Robot Inventor, you'll also need a USB cable (microUSB) to install
the Pybricks firmware.

You'll also need a browser with Bluetooth support. We recommend using 
<a href="https://www.google.com/chrome/" target="_blank">Google Chrome</a> or
<a href="https://www.microsoft.com/en-us/edge" target="_blank">Microsoft Edge</a>.
If you prefer open source tools, you can
use [Chromium](/project/pybricks-on-linux/).

Note that the Apple iPad and iPhone are **_not_** supported, because the iOS
Safari browser and Chrome for iOS do not support Bluetooth connectivity.
Similarly, Firefox does **_not_** support Bluetooth on any platform.

# Choosing a LEGO hub

You can learn to code with Pybricks using any of the hubs shown below. Since many
LEGO apps support just one kind of hub, that hub is usually just called "the
hub". This can be a bit confusing, so we'll use the indicated names
consistently throughout this user guide when required.

{% include diagram.html data="diagram-hubs" %}


Because Pybricks makes the coding interface the same for all hubs, you can
select a hub based on your budget and needs for your own project. The
differences are outlined below.

You'll use just two motors for most of the example projects in this
introductory guide, so any hub will do.

|                                      | Prime hub* Inventor hub | Essential hub | Technic hub | City Hub | BOOST Move Hub     |
|--------------------------------------|-------------------------|---------------|-------------|----------|--------------------|
| MicroPython coding                   | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Block-based coding                   | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Motor/sensor ports                   | 6                       | 2             | 4           | 2        | 2 ports + 2 builtin motors |
| Buttons                              | 4                       | 1             | 1           | 1        | 1                  |
| Battery                              | Builtin                 | Builtin       | 6 AA        | 6 AAA    | 6 AAA              |
| Display                              | 5x5 Lights              | ❌             | ❌           | ❌        | ❌                  |
| Speaker                              | Beeps only              | ❌             | ❌           | ❌        | ❌                  |
| Color status light                   | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Accelerometer                        | ✅                       | ✅             | ✅           | ❌        | ✅                  |
| Gyro                                 | ✅                       | ✅             | ✅           | ❌        | ❌                  |
| Powered Up motors                    | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Powered Up sensors                   | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Powered Up Remote                    | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Hub-to-hub communication             | ✅                       | ✅             | ✅           | ✅        | ✅                  |
| Xbox controller                      | ✅                       | ✅             | ✅           | ❌        | ❌                  |
| Math with decimals or random numbers | ✅                       | ✅             | ✅           | ✅        | ❌                  |
| Total storage**                      | 256Kb                   | 256Kb         | 16Kb        | 16Kb     | 4Kb                |
| Total RAM***                          | 320Kb                   | 320Kb         | 64Kb        | 32Kb     | 16Kb               |
| User data storage                    | 512b                    | 512b          | 128b        | 128b     | 128b               |

(\*) The _SPIKE Prime Hub_ and _MINDSTORMS Robot Inventor Hub_ are identical,
except for the casing color and a device number to tell them apart. With
Pybricks, they work the same. The official apps only connect to hubs with the
correct color.
{: .notice}

(\*\*) The storage is also the maximum size of your program. Technically, the
Prime Hub, Inventor Hub and Essential Hub have more storage space than
this. This is not used by Pybricks, so that any files you had on it
originally remain untouched.
{: .notice}

(\*\*\*) Working memory
holds a copy of your program and system variables. The remainder is available
for variables in your own code.
{: .notice}

# Choosing motors

Motors make your creations move. There are two types: motors that can measure
their position and motors that can't.

Motors that can measure their position are very suitable for robotics
applications. You'll need a pair of them to follow along with this guide.

{% include scaled.html
  path="https://docs.pybricks.com/en/latest/_images/pupdevice-motors.png"
  width="100%"
  caption="These motors can measure their position, so you can choose exactly
           how many degrees they should turn. The hub adjusts the power to these
           motors to keep them running at a steady speed, even when you try to
           slow them down."
%}

Motors that can't measure their position can still be useful in some cases due
to their unique shape, such as the train engine.

If you're a train builder, we recommend that you follow
this guide with one of the motors shown above first, and resume building with
your train motors when you've mastered the essential coding techniques. Most
of it will still apply!

{% include scaled.html
  path="https://docs.pybricks.com/en/latest/_images/pupdevice-dcmotors.png"
  width="75%"
  caption="These simpler motors only run at the power level you choose. If you
           drive a train with many carriages for example, you'll need to pick
           a higher power level yourself to keep it going at the desired speed.
           You can't measure how far they turn exactly."
%}

# Choosing sensors

Sensors make your creation aware of its surroundings. Your robot can then
respond to different measurements. For example, a vehicle could choose to turn
around if it sees an obstacle.

Measuring distance is the simplest way to get familiar with sensors. To follow
along with this guide, you can pick any of the sensors below that can measure
relative distance (0% to 100%) or actual distance (mm).

We'll also have a dedicated chapter for color measurement, calibration, and
line following. You can skip it if you do not have any color sensors.

<table>
<colgroup>
  <col style="width: 25%;">
  <col style="width: 20%;">
  <col>
</colgroup>
<thead>
  <tr>
    <td></td>
    <td><b>Device</b></td>
    <td><b>Measurement or function</b></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-tilt.png" width="90%" %}</td>
    <td>{% include setlink.html id=45305 %}</td>
    <td><ul>
      <li>Pitch movement: ± °45</li>
      <li>Roll movement: ± °45</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-infrared.png" width="90%" %}</td>
    <td>{% include setlink.html id=45304 %}</td>
    <td><ul>
      <li>Relative distance: 0% to 100%</li>
      <li>Reflected light intensity: 0% to 100%</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-colordistance.png" width="90%" %}</td>
    <td>{% include setlink.html id=88007 %}</td>
    <td><ul>
        <li>Relative distance: 0% to 100%</li>
        <li>Surface color: Hue, saturation, value</li>
        <li>Surface color: Customizable colors</li>
        <li>Reflected light intensity: 0% to 100%</li>
        <li>Ambient light intensity: 0% to 100%</li>
        <li>Red, green, or blue lamp function</li>
        <li>Act as Power Functions 1.0 remote</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-color.png" width="90%" %}</td>
    <td>{% include setlink.html id=45605 %}</td>
    <td><ul>
        <li>Surface color: Hue, saturation, value</li>
        <li>Surface color: Customizable colors</li>
        <li>Reflected light intensity: 0% to 100%</li>
        <li>Ambient light intensity: 0% to 100%</li>
        <li>Three controllable white lights</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-ultrasonic.png" width="100%" %}</td>
    <td>{% include setlink.html id=45604 %}</td>
    <td><ul>
        <li>Distance: 40mm to 1000mm</li>
        <li>Four controllable white lights</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-force.png" width="90%" %}</td>
    <td>{% include setlink.html id=45606 %}</td>
    <td><ul>
        <li>Force: 0.0N to 10.0N</li>
        <li>Button movement in mm</li>
        <li>Button presses</li>
    </ul></td>
  </tr>
</tbody>
</table>

# Technic building pieces

In this guide, you'll build a small robot vehicle consisting of a hub, two
motors, and a sensor. You'll need a small amount of Technic pieces to put this
all together.

If you have any SPIKE, Technic, or MINDSTORMS set, you should have more than
enough pieces. You'll find step by step instructions for a few suggested
designs in the next chapter.

# Lights (optional)

Lights can be used to decorate your design or indicate useful information about
what your code is doing. Each hub also has a builtin light that can be used for
this purpose.

<table>
<colgroup>
  <col style="width: 25%;">
  <col style="width: 20%;">
  <col>
</colgroup>
<thead>
  <tr>
    <td></td>
    <td><b>Device</b></td>
    <td><b>Function</b></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-light.png" width="90%" %}</td>
    <td>{% include setlink.html id=88005 %}</td>
    <td><ul>
      <li>Brightness from 0% to 100%</li>
      <li>Both lights have the same brightness</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/sensor_colorlightmatrix.png" width="90%" %}</td>
    <td>{% include setlink.html id=45608 %}</td>
    <td><ul>
      <li>9 lights, separately controllable</li>
      <li>9 different colors per light</li>
    </ul></td>
  </tr>
</tbody>
</table>


# Remote control (optional)

A remote can be a fun way to _augment_ your autonomous creation. It also lets
you conveniently test the mechanics of your design before
diving into more elaborate programs.

With Pybricks you are not limited to predefined remote configurations. Instead,
you can think of these remotes as wireless sensors. You can
measure button presses or joystick position, and you decide what happens based
on those inputs.

<table>
<colgroup>
  <col style="width: 25%;">
  <col style="width: 20%;">
  <col>
</colgroup>
<thead>
  <tr>
    <td></td>
    <td><b>Device</b></td>
    <td><b>Measurement or function</b></td>
  </tr>
</thead>
<tbody>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/pupdevice-remote.png" width="90%" %}</td>
    <td>{% include setlink.html id=88010 %}</td>
    <td><ul>
      <li>Button presses</li>
      <li>Controllable color light</li>
      <li>Works with all hubs</li>
    </ul></td>
  </tr>
  <tr>
    <td>{% include scaled.html path="https://docs.pybricks.com/en/latest/_images/xboxcontroller.png" width="90%" %}</td>
    <td>{% include setlink.html id="xbox" %} <br/>or<br/> {% include setlink.html id="xbox-elite-2" %}</td>
    <td><ul>
      <li>Button presses and joystick clicks</li>
      <li>Analog joystick and trigger positions</li>
      <li>Rumble function</li>
      <li>Works with SPIKE Prime, SPIKE Essential, MINDSTORMS, and Technic</li>
    </ul></td>
  </tr>
</tbody>
</table>
