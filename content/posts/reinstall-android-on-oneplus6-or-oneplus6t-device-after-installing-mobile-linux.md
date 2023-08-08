---
title: "Reinstall Android on Oneplus6 or Oneplus6t Device After Installing Mobile Linux"
date: 2023-08-07T19:50:08-07:00
draft: true
---

Did you install a Mobile Linux Operating System onto your Oneplus6 or Oneplus6t device, and you want to go back to android? Well, you're in luck as it's a pretty straight forward process.

First, download the package from Oneplus. This can be done by going to [service.oneplus.com/us](https://service.oneplus.com/us). Scroll down to the image that says **Software Update** and then click on it. You will now be at a page that has a list of devices with links for firmware for the devices. Download the .zip file for your device.

Once you have downloaded the file unzip it. You will need an application called [payload-dumper-go](https://github.com/ssut/payload-dumper-go/releases) in order to unpack the firmware.


Use payload dumper to extract payload.bin

Enter into the directory and enter these commands into the terminal.

```
    fastboot -w
    fastboot flash aop_a aop.img
    fastboot flash aop_b aop.img
    fastboot flash bluetooth_a bluetooth.img
    fastboot flash bluetooth_b bluetooth.img
    fastboot flash boot_a boot.img
    fastboot flash boot_b boot.img
    fastboot flash dsp_a dsp.img
    fastboot flash dsp_b dsp.img
    fastboot flash dtbo_a dtbo.img
    fastboot flash dtbo_b dtbo.img
    fastboot flash modem_a modem.img
    fastboot flash modem_b modem.img
    fastboot flash oem_stanvbk oem_stanvbk.img
    fastboot flash qupfw_a qupfw.img
    fastboot flash qupfw_b qupfw.img
    fastboot flash storsec_a storsec.img
    fastboot flash storsec_b storsec.img
    fastboot flash system_a system.img
    fastboot flash system_b system.img
    fastboot flash vbmeta_a vbmeta.img
    fastboot flash vbmeta_b vbmeta.img
    fastboot flash vendor_a vendor.img
    fastboot flash vendor_b vendor.img
    fastboot flash LOGO_a LOGO.img
    fastboot flash LOGO_b LOGO.img
    fastboot reboot bootloader
```