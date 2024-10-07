

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

If you want a *traditional* builded backup kernel just in case... you can use [SBKS](./scripts/SBKS)<br>
requires: yad.<br>
READ script and then add it in your $PATH, I have it in `/usr/local/bin` <br>  
It will build a backup kernel that slackpkg will not delete it when officially kernel upgrade come.

#### Tip

Build NVIDIA drivers in this backup kernel.  And then boot in stock kernel and install only modules to that kernel<br>
`sh NVIDIA-xxxx.sh -K`  <br>
This way if you are on current always you will have nvidia drivers installed in your backup kernel and on first boot of new stock kernel just `sh NVIDIA-xxxx.sh -K` <br>
`exit 0`
