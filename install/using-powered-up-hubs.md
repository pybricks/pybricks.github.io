---
title: "Using LEGO Powered Up hubs with Pybricks firmware"
sidebar:
  nav: "install"
toc: true
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
| ![blue 100ms, off 200ms, blue 100ms, off 2200ms](/assets/images/powered-up/status-light/advertising.gif) | Two short, blue blinks | Waiting for a connection. |
| ![solid blue](/assets/images/powered-up/status-light/connected.gif) | Solid blue | Connected. No program is running. |
| ![breathing blue 2000ms cycle](/assets/images/powered-up/status-light/program-running.gif) | Fading blue | A program is running.|



### Warnings

These warning lights take priority over the normal light behavior.

| | Pattern | Description |
|-|---------|-------------|
| ![orange 300ms, off 400ms, orange 300ms, off 200ms, system 800ms, off 200ms](/assets/images/powered-up/status-light/low-battery.gif) | Two long, orange blinks | Low battery |

### During installation

These patterns are only visible when installing or restoring the firmware.

| | Pattern | Description |
|-|---------|-------------|
| ![light purple 500ms, off 100ms](/assets/images/powered-up/status-light/bootloader-advertising.gif) | Slow light-purple blinks | Bootloader is waiting for a connection |
| ![red 500ms, green 500ms, blue 500ms, off 100ms](/assets/images/powered-up/status-light/bootloader-connected.gif) | Alternating red, green, blue blinks | Bootloader is connected |
