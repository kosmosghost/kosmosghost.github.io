You are going to need a few tools before you can install postmarketOS with full disk encryption on the oneplus6/t device:
1) Android tools for fastboot.
2) pmbootstrap - pip install pmbootstrap

Warning: I have not tried this with dual booting android.


Here is how I installed postmarketOS on my oneplus6t with FULL DISK ENCRYPTION:

```
fastboot erase dtbo
```

Warning: This will mess up android if you want to dual boot.

```
pmbootstrap init
```

Simply follow the prompts and select oneplus as the vendor, and enchilada if using the oneplus6 or fajita if using oneplus6t.


```
pmbootstrap install --fde --split --filesystem btrfs

```

I chose `--filesystem btrfs` for this because I like btrfs, and it's easier to install on the oneplus6/t devices with btrfs. You can ignore this if you chose the defaults, which is ext4. I will have instructions for btrfs and regular ext4 at the end of this tutorial.

```
pmbootstrap export
```

Again, just follow the prompts. pmbootstrap will create a link into /tmp/postmarketOS-export/.

```
fastboot erase boot
fastboot erase vendor
fastboot erase userdata
```

This is going to erase the bootloader on the boot slot. Erasing userdata will probably delete the data on your Android partition. This method only works when not dual booting.

When inside the postmarketOS-export directory run:
```
fastboot flash boot boot.img
fastboot flash vendor oneplus-fajita-boot.img
fastboot flash userdata oneplus-fajita-root.img
```

Once everything is flashed turn off the device. Reboot, and make sure that everything is working as it should. As of this writing postmarketOS does not correctly size the storage on your device. It is very important to boot the device, and then restart, before you resize the storage. 


Next download the jumpdrive enchilada/fajita boot imgage from [github](https://github.com/dreemurrs-embedded/Jumpdrive/releases) and run:
```
fastboot boot jumpdrive.img
```

The phone will boot into the jumpdrive os and show as a block device. In my case it was sda.

Run `cryptsetup open /dev/sdx fajita` and enter your password for unlocking the device.

In this very order run if you used btrfs for the filesystem:

```
cryptsetup resize fajita
btrfs resize max /dev/mapper/fajita
```

Or for ext4:
```
cryptsetup resize fajita

e2fsck -f /dev/mapper/fajita

resize2fs /dev/mapper/fajita
```

And now everything should be working!