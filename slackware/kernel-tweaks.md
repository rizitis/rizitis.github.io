

## Linux Kernel

Slackware recently change it philosophy for linux kernel builds. <br>
R.I.P:
- huge-kernel
- initrd.gz

Welcome:
- dracut
- modules_build_in
- remove-orphaned-initrds
- kernel-backup

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

Everything you need is [HERE](https://github.com/rizitis/linux-zen)