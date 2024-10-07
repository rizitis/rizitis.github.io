

## Linux Kernel

Slackware recently change it philosophy for linux kernel builds. <br>
R.I.P:
- huge-kernel
- initrd.gz

Welcome:
- dracut
- modules_build_in

And more good news or bad for some are here...<br>
As **heretics** what will provided here are some alternatives you might want...<br>

---

#### backup_custom kernel

![kernel](https://www.kernel.org/theme/images/logos/tux.png)

If you want a *traditional* builded backup kernel just in case... You can use [SBKS](./scripts/SBKS)<br>
*requires: yad*<br>
READ script first  and then add it in your $PATH, I have it in `/usr/local/bin` or just run it as root always... <br>  
It will build a backup kernel that slackpkg will not delete  when officially kernel upgrade comes in.

#### Tip

Build NVIDIA drivers in this backup kernel `sh NVIDIA-xxxx.sh`. Then boot in stock kernel and install only nvidia modules for stock kernel<br>
`sh NVIDIA-xxxx.sh -K`  <br>
This way if you are on current, always you will have nvidia drivers installed in your backup kernel and on first boot of new stock kernel only need to  command `sh NVIDIA-xxxx.sh -K` <br>

#### ZEN kernel

[Check](https://github.com/zen-kernel/zen-kernel/blob/6.11/main/Documentation/process/changes.rst) Current Minimal Requirements to build and run a zen kernel.<br>

**HOWTO Build zen kernel + Headers in Slackware** <br>

1. zen kernel should **NOT** builded in `/usr/src` or in `/tmp` and generally speaking go away from root `(/)` path.
2. Best place for zen job is someware in your regular user home `/home/$USER/x.d`
3. Here we install zen-headers too...
4. You can build NVIDIA-xxxx.sh in this zen kernel.

---

As **user** command:<br>

1. `mkdir -p "$HOME"/zenhacks/workdir`<br>
2. `git clone https://github.com/zen-kernel/zen-kernel.git "$HOME"/zenhacks/workdir --depth 1 `<br>
3. `zcat /proc/config.gz > "$HOME"/zenhacks/workdir/.config`
4. `cd "$HOME"/zenhacks/workdir`
5. `nano .config`

```
CONFIG_ANDROID=y
CONFIG_ANDROID_BINDER_IPC=y
CONFIG_ANDROID_BINDERFS=n
CONFIG_ANDROID_BINDER_DEVICES="binder,hwbinder,vndbinder" 
```
6. `make oldconfig`
7. `make -j$(getconf _NPROCESSORS_ONLN)`
8. `make all`
9. `pushd tools/bpf/resolve_btfids`
10. `make`
11. `popd`
9. `su -c "make modules_install"`
  - copy kernel version assume (6.11.2)
10. `version=6.11.2 && echo "$version"`
11. `su -c "rm -r /lib/modules/"$version"-zen+/build"`
12. `su -c "mkdir -p /lib/modules/"$version"-zen+/build"`
13. `su -c "cp -R include /lib/modules/"$version"-zen+/build"`
14. `su -c "mkdir -p  /lib/modules/"$version"-zen+/build/arch/x86"`
15. `su -c "cp -R arch/x86/include  /lib/modules/"$version"-zen+/build/arch/x86/"`
16. `su -c "mkdir -p  /lib/modules/"$version"-zen+/build/arch/x86/kernel"`
17. `su -c "cp -a arch/x86/kernel/asm-offsets.s /lib/modules/"$version"-zen+/build/arch/x86/kernel"`
18. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/drivers/md"`
19. `su -c "cp -a drivers/md/*.h /lib/modules/"$version"-zen+/build/drivers/md"`
20. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/net/mac80211"`
21. `su -c "cp -a net/mac80211/*.h /lib/modules/"$version"-zen+/build/net/mac80211/"`
22. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/drivers/media/i2c"`
23. `su -c "cp -a drivers/media/i2c/msp3400-driver.h /lib/modules/"$version"-zen+/build/drivers/media/i2c/"`
24. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/drivers/media/usb/dvb-usb"`
25. `su -c "cp -a drivers/media/usb/dvb-usb/*.h /lib/modules/"$version"-zen+/build/drivers/media/usb/dvb-usb"`
26. `su -c "mkdir -p  /lib/modules/"$version"-zen+/build/drivers/media/{dvb-frontends,tuners}"`
27. `su -c "cp -a drivers/media/dvb-frontends/*.h /lib/modules/"$version"-zen+/build/drivers/media/dvb-frontends"`
28. `su -c "cp -a drivers/media/tuners/*.h /lib/modules/"$version"-zen+/build/drivers/media/tuners"`
29. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/drivers/iio/common/hid-sensors "`
30. `su -c "cp -a drivers/iio/common/hid-sensors/*.h /lib/modules/"$version"-zen+/build/drivers/iio/common/hid-sensors"`
31. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/tools/objtool"`
32. `su -c "cp -R tools/objtool/objtool  /lib/modules/"$version"-zen+/build/tools/objtool"`
33. `su -c "mkdir -p /lib/modules/"$version"-zen+/build/tools/objtool/tools/bpf/resolve_btfids"`
34. `su -c "cp -a tools/bpf/resolve_btfids/resolve_btfids /lib/modules/"$version"-zen+/build/tools/objtool/tools/bpf/resolve_btfids"`
35. `su -c "cp -R scripts /lib/modules/"$version"-zen+/build/"`
36. `su -c "ln -srt /lib/modules/"$version"-zen+/build /lib/modules/"$version"-zen+/build/scripts/gdb/vmlinux-gdb.py"`
36. `su -c "cp -a .config Makefile Module.symvers System.map vmlinux /lib/modules/"$version"-zen+/build"`
37. `su -c "mkdir -p  /lib/modules/"$version"-zen+/build/kernel"`
38. `su -c "cp  kernel/Makefile /lib/modules/"$version"-zen+/build/kernel"`
39. `su -c "mkdir -p  /lib/modules/"$version"-zen+/build/arch/x86"`
40. `su -c "cp arch/x86/Makefile /lib/modules/"$version"-zen+/build/arch/x86"`
31. `su -c "find . -name 'Kconfig*' -exec install -Dm644 {} /lib/modules/"$version"-zen+/build/{} \;"`
32. `sleep get a coffe, get some rest...`
33. `su -c "cp arch/x86_64/boot/bzImage /boot/vmlinuz-"$version"-zen+"`
34. `su -c "cp System.map /boot/System.map-"$version"-zen+"`
35. `cd /boot`
36. `su -c "rm System.map"`
37. `su -c "ln -s System.map-"$version"-zen+  System.map"`
38. `su -c "/usr/share/mkinitrd/mkinitrd_command_generator.sh -k "$version"-zen+"`
 - copy output but remove the `-c` option and paste it terminal then hit enter.
 - example: `su -k "mkinitrd  -k 6.11.2-zen+ -f ext4 -r /dev/nvme0n1p2 -m xhci-pci:ohci-pci:ehci-pci:xhci-hcd:uhci-hcd:ehci-hcd:hid:usbhid:i2c-hid:hid_generic:hid-asus:hid-cherry:hid-logitech:hid-logitech-dj:hid-logitech-hidpp:hid-lenovo:hid-microsoft:hid_multitouch:ext4 -u -o /boot/initrd.gz"`
39. `su -c "grub-mkconfig -o /boot/grub/grub.cfg"`
40. `echo "Good luck"`


