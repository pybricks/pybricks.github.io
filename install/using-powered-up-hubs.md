---
title: "Using LEGO Powered Up hubs with Pybricks firmware"
sidebar:
  nav: "install"
toc: true
---

The Pybricks firmware for Powered Up devices has been designed to behave similar
to the official LEGO firmware, however there are some differences.

## Status light

| | Pattern | Description |
|-|---------|-------------|
| ![blue 100ms, off 200ms, blue 100ms, off 2200ms](/assets/images/powered-up/status-light/advertising.gif) | Two short, blue blinks | Waiting for Bluetooth Low Energy connection (advertising) |
| ![orange 100ms, off 200ms, orange 100ms, off 2200ms](/assets/images/powered-up/status-light/advertising-low-battery.gif) | Two short, orange blinks | Waiting for Bluetooth Low Energy connection (advertising) and low battery |
| ![orange 300ms, off 400ms, orange 300ms, off 200ms, system 800ms, off 200ms](/assets/images/powered-up/status-light/low-battery.gif) | Two long, orange blinks | Low battery |
| ![solid blue](/assets/images/powered-up/status-light/connected.gif) | Solid blue | Connected with Bluetooth Low Energy, no program is running |
| ![breathing blue 2000ms cycle](/assets/images/powered-up/status-light/program-running.gif) | Breathing blue | Program is running (program may control the light) |
| ![light purple 500ms, off 100ms](/assets/images/powered-up/status-light/bootloader-advertising.gif) | Slow light purple blinks | Bootloader is waiting for Bluetooth Low Energy connection (advertising) |
| ![red 500ms, green 500ms, blue 500ms, off 100ms](/assets/images/powered-up/status-light/bootloader-connected.gif) | Alternating red, green, blue blinks | Bootloader is connected |
