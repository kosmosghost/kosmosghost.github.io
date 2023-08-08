---
title: "Installing PostmarketOS With Full Disk Encryption on Oneplus6 Oneplus6t Devices"
date: 2023-08-05T19:30:24-07:00
draft: false
---

Installing PostmarketOS on the Oneplus 6/6t devices is pretty easy, and you will have a linux operating system on your phone with full disk encryption. By following this short tutorial you can have a mobile linux operating system on your phone in no time, but this tutorial assumes you are using linux for doing the install. Before you start you are going to need a few tools:

1) Android tools for fastboot - On Fedora: `sudo dnf install android-tools`

2) pmbootstrap - On Fedora: `sudo dnf install pmbootstrap` or `pip3 install pmbootstrap`

Warning: The following will delete everything on the user partition of the device. Everything you have saved on your phone will be deleted. While you won't be able to ever get your data back, it is easy to reinstall android if you are unhappy running mobile linux on your device.

First, make sure your phone is fully upgraded. Then, unlock the boot loader. I followed the tutorial over at [gadgethacks](https://oneplus.gadgethacks.com/how-to/unlock-bootloader-your-oneplus-6-0185473/). Once the device is unlocked reboot into fastboot mode. On the Oneplus 6 hold the volume up and the power button at the same time. On the Oneplus6t hold both volume buttons and the power button at the same time. Once the phone has rebooted into fastboot, release the power button first, and then release the volume keys.

Next, plug your device into a usb cable and attach it to your computer. All the following commands will require superuser privileges. 

Verify that your computer can see the device:

```
sudo fastboot devices
```

#Insert Picture here.

If you see your device proceed to the next step. Otherwise remove the usb cable, reboot your phone into fastboot again, and then reattach. If that doesn't work try rebooting your computer and start again.

Unlock your device:

```
sudo fastboot oem unlock
```

The Oneplus6/6t devices have a dual slot for the kernel, and for some reason I could never get encryption working when booting from slot b, so make sure that the device will boot from slot a.

```
sudo fastboot set_active a
```

Erase the dtbo partition:

```
fastboot erase dtbo
```

Now let's build the image using the postmarketos.

```
pmbootstrap init
```

Simply follow the prompts and select oneplus as the vendor, and enchilada if using the oneplus6 or fajita if using oneplus6t. At this time I highly suggest using phosh for the shell. The current version of plasma mobile is still too buggy, crashes way to often, audio doesn't work, and video is "iffy".

Next build the system:

```
pmbootstrap install --fde --split --filesystem btrfs

```

I chose `--filesystem btrfs` for this because I like btrfs, and it's easier to install on the oneplus6/t devices with btrfs. You can ignore this if you want chose the default, which is ext4. I will have instructions for btrfs and regular ext4 at the end of this tutorial.

```
pmbootstrap export
```

Again, just follow the prompts. pmbootstrap will create a link into /tmp/postmarketOS-export/. Enter into the directory, `cd /tmp/postmarketOS-export/` After that just copy and paste the following commands into the terminal. This will erase the android operating system from your phone. While it is easy to reinstall android, the data you have stored such as pictures, and videos will be forever gone unless you have a backup.

```
sudo fastboot erase boot
sudo fastboot erase vendor
sudo fastboot erase userdata
```

If using the Oneplus6(enchilada) paste the following into your terminal:

```
sudo fastboot flash boot boot.img
sudo fastboot flash vendor oneplus-enchilada-boot.img
sudo fastboot flash userdata oneplus-enchilada-root.img
```

Or if flashing to the oneplus6t:


```
sudo fastboot flash boot boot.img
sudo fastboot flash vendor oneplus-fajita-boot.img
sudo fastboot flash userdata oneplus-fajita-root.img
```

Once everything is flashed turn off the device. Reboot, and make sure that everything is working as it should. As of this writing postmarketOS does not correctly size the storage on your device.

Because we installed postmarketOS with btrfs, we can easily resize the device once the device has booted. Open up the console on the phone, or while the phone is connected to usb ssh into the phone `ssh $USER@172.16.42.1` Replace $USER with the user name that you entered when you ran `pmbootstrap init`. Type in the following into the terminal:

```
sudo btrfs resize max /
```

If you opted to go with EXT4 instead of BTRFS then power on your phone and make sure it works. Then reboot into fastboot mode and connect to your computer with the usb cable. Download the jumpdrive enchilada/fajita boot image from [github](https://github.com/dreemurrs-embedded/Jumpdrive/releases) and for the Oneplus6 run on your computer:

```
sudo fastboot boot boot-oneplus-enchilada.img 
```

Oneplus6t:

```
sudo fastboot boot boot-oneplus-fajita.img
```

The phone will boot into the jumpdrive os and show as a block device when connected to your computer using a usb cable. Use `lsblk` to find the device. In my case it was sda.

#insert picture here

Run `cryptsetup open /dev/$SDX oneplus`, replacing $SDX with the appropriate device name(sda, sdb, sdc, etc) and enter your password for unlocking the device.

```
cryptsetup resize oneplus

e2fsck -f /dev/mapper/oneplus

resize2fs /dev/mapper/oneplus
```

Once everything is finished reboot your device and you should have a working Oneplus6/6t device running postmarketOS with full disk encryption.
