---
title: "Simple wireless communication between MicroPython boards via Bluetooth (BLE)"
tags:
  - Hub to Hub Communication
  - Python
header:
  teaser: /project/python/arduino-spike.jpg
  og_image: /project/python/arduino-spike-og.jpg
excerpt: >
  Learn how to install a library that enables simple wireless communication
  between any number of MicroPython boards without setting up connections.
---

The hub-to-hub communication feature in Pybricks MicroPython is not restricted
to LEGO hubs alone.

In this project, we will show you how to install a library that enables simple
wireless communication between any number of MicroPython boards that support
Bluetooth Low Energy (BLE).

If you just need to send small amounts of data, this can be a lot simpler than
setting up dedicated connections between the boards.

{% include scaled.html
  path="/project/python/arduino-spike-og.jpg"
  caption="You can make BLE-enabled MicroPython boards exchange data easily."
%}

# How does it work?

Normally when you want to send data between two devices, you need to establish
a connection first. One device can "advertise" itself to describe what it can
do, and the other can "scan" for it.

This advertisement data normally contains information about the device, like
its name and services. Once a scanning device finds an advertising
device, they can connect and start sending data.

In the technique used here, we put the information we want to exchange in the
advertisement data instead. There isn't much space in the advertisement data,
but it can be enough for simple messages. The advantage is that you don't need
to establish a connection at all, but you can just keep looking for changing
advertising data and react to it.

We've made a library that does this for you, so you can simply send and receive
values without worrying about the details of the Bluetooth protocol.

# What can you make?

This technique works great for broadcasting a few numbers or a small text
message. Since no explicit connection is required, any other BLE-enabled device
can scan for these messages and react to them.

This lets you make many-to-many communication networks like the one shown
below. Here, a LEGO hub measures a color and broadcasts it to all other boards
in the area that may be listening, which is two Arduino Nano ESP32s in this
case. They respond to the message by turning on the LED at the corresponding
color.

{% include youtube.html videoid="q0em83vuwvs" %}

A similar example is shown below, where a LEGO hub broadcasts tilt and roll
data, which is used by the Arduino Alvik robot to drive around.

{% include youtube.html videoid="L4FL35y8up0" %}

# Installing the `bleradio` module

The communication tools come pre-installed on the LEGO hubs running Pybricks.

If you want to use this technique with other MicroPython
boards, install the `bleradio` library first. If you have `mpremote`, just do:

{% include copy-code.html %}
```
mpremote mip install https://raw.githubusercontent.com/pybricks/micropython-bleradio/master/bleradio.py
```
Alternatively, download <a href="https://raw.githubusercontent.com/pybricks/micropython-bleradio/master/bleradio.py" download>
bleradio.py</a> and copy it to your board.


# What can you send?

Each hub can broadcast on one "channel" (0 through 255) and observe any number
of channels (each 0 through 255). The channel numbers are used to filter out
the messages you are interested in.

You can send signed integer values, floating point numbers, booleans, strings,
or bytes. Or a list/tuple of these objects.

For example, you can broadcast one of the following:

```python
data = 12345

data = "Hello, world!"

data = b"\x01\x02\x03"

data = (123, 3.14, True, "Hello World")
```

Boolean values are packed into one byte. All other types are packed into their
respective sizes plus one byte for the type.

Since advertisements payloads are limited to 31 bytes by the Bluetooth spec and
there are 5 bytes of overhead, the combined size of all type headers and values
is limited to 26 bytes.

When no data is observed, the observe method returns None. To stop
broadcasting, use broadcast(None).

The full specification is available in the [protocol](https://github.com/pybricks/technical-info/blob/master/pybricks-ble-broadcast-observe.md).

# Example programs

Here is a simple example program that shows how to use the `BLERadio` class.
This example shows how you can broadcast data on on a channel and listen to
data on other channels at the same time.

{% include copy-code.html %}
```python
from time import sleep_ms
from bleradio import BLERadio

# A board can broadcast small amounts of data on one channel. Here we broadcast
# on channel 5. This board will listen for other boards on channels 4 and 18.
radio = BLERadio(broadcast_channel=5, observe_channels=[4, 18])

# You can run a variant of this script on another board, and have it broadcast
# on channel 4 or 18, for example. This board will then receive it.

counter = 0

while True:

    # Data observed on channel 4, as broadcast by another board.
    # It gives None if no data is detected.
    observed = radio.observe(4)
    print(observed)

    # Broadcast some data on our channel, which is 5.
    radio.broadcast(["hello, world!", 3.14, counter])
    counter += 1
    sleep_ms(100)
```

You can make a variant of the program above and run it on a second board.
For example, you can make a program that observes the data on channel 5 and
prints it when it changes.

This example also shows the signal strength, which can be an additional piece
of information to help you roughly determine the distance between the boards.

{% include copy-code.html %}
```python
from bleradio import BLERadio

radio = BLERadio(observe_channels=[5])

old_data = None

while True:

    new_data = radio.observe(5)
    strength = radio.signal_strength(5)

    if new_data == old_data:
        continue

    print(strength, "dBm:", new_data)
    old_data = new_data
```

Check out the GitHub
[repository](https://github.com/pybricks/micropython-bleradio) for more
examples, details, and discussion.

# Mixing with LEGO Hubs

This communication technique is included in Pybricks by default. This means you
can use any [existing program](https://pybricks.com/project/hub-to-hub-communication/) for inspiration.

It does not matter if the LEGO hub uses a Python program or a block-based
program. Wireless communication works the same way in both cases.
