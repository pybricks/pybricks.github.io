---
title: "Installing Pybricks Code"
sidebar:
  nav: "install"
toc: true
---

<img src="/assets/images/home-code-2.png" />

## System requirements

- Device with Windows, Mac, Linux, ChromeOS or Android operating system.
- [Google Chrome] or [Microsoft Edge] web browser.
- Bluetooth adapter with Bluetooth Low Energy support.
- USB Type-A port (only required for flashing firmware on hubs with USB).


### Browser compatibility notes

- Other browsers such as Firefox and Safari do not support Web Bluetooth and
  therefore can't be used with Pybricks Code.
- Google Chrome for iOS does not support Web Bluetooth, so Pybricks Code can't
  currently be used on iOS.
- There are known issues with the Ubuntu `snap` versions of the Chromium browser.
  Some Pybricks Code features may not work.
- Other Chromium-based web-browser may or may not support Web Bluetooth. Notably,
  Opera, Vivaldi and Brave do not support Web Bluetooth and therefore won't work
  for Pybricks Code.
- Web Bluetooth is not officially supported on Linux and requires *Experimental
  Web Platform features* to be enabled. Copy and paste the following in the
  address bar, set it to *Enabled* and restart the browser. This is only
  needed on Linux, not any other OS.

      chrome://flags/#enable-experimental-web-platform-features

### Bluetooth compatibility notes

- Using other Bluetooth devices at the same time can cause interference
  resulting in errors in Pybricks Code, particularly Bluetooth keyboards/mice.
  Be sure to turn off any unused devices for the best experience.
- Many Bluetooth adapters on Windows have compatibility issues. We have had the
  best results with adapters that used the generic Microsoft Bluetooth drivers
  such as adapters that use Cambridge Silicon Radio (CSR 4.0) chips. You can
  help by reporting known working and not working adapters [here][win ble issue].
- Additional Bluetooth troubleshooting advice is available [here][ble trouble].


[Pybricks Code]: https://code.pybricks.com
[Google Chrome]: https://google.com/chrome
[Microsoft Edge]: https://microsoft.com/edge
[win ble issue]: https://github.com/pybricks/support/issues/921
[ble trouble]: https://github.com/pybricks/support/discussions/270


## Installation

Since Pybricks Code is a [progressive web app], it runs entirely in the web
browser and no installation is needed.

It is possible to "install" Pybricks Code as an app. This just means that a
shortcut is added to the start menu (or home screen depending on the OS) which
will launch the web page in a special window that doesn't include the browser
address bar so that it looks more like an app than a web page.

Since Pybricks Code is a [progressive web app] it can be used offline once the
page has fully loaded. You do not need to "install" as an app to use Pybricks
Code offline.

[progressive web app]: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
