---
title: "Using LEGO Powered Up hubs with Pybricks firmware"
---

With Pybricks now installed, we'll show you how the hub works.

## Turning the hub on and off

Click (press and release) the green button to turn the hub on.
Press and hold it for three seconds to turn it off.


## Understanding the hub status light

The status light helps you see what the hub is doing, and monitor status
information such as low battery.

### Normal operation

You'll see these light patterns most of the time. 

| | Pattern | Description |
|-|---------|-------------|
| ![blue 100ms, off 200ms, blue 100ms, off 2200ms](listening.png) | Two blue blinks | Waiting for a connection. |
| ![solid blue](connected.png) | Solid blue | Connected. No program is running. |
| ![breathing blue 2000ms cycle](program-running.png) | Fading blue | A program is running.|


### Warnings

These warning lights take priority over the normal light behavior.

| | Pattern | Description |
|-|---------|-------------|
| ![low-battery](low-battery.png) | Two long orange blinks | Low battery. |

### During installation

These patterns are only visible when installing or restoring the firmware.

| | Pattern | Description |
|-|---------|-------------|
| ![light purple 500ms, off 100ms](bootloader-listening.png) | Slow light-purple blinks | Waiting for update. |
| ![red 500ms, green 500ms, blue 500ms, off 100ms](bootloader-connected.png) | Red, green, and blue blinks | Updating. |
