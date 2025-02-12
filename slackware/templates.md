---
layout: default
title: "SlackBuilds Template"
---

## SlackBuilds Template?

Well the correct answer for this question is **I Dont Know**...<br>
In theory there is none officially SlackBuild Template! <br>
Why?<br>
I think that it not needed the way distro introduce it self.<br>

![ALT](./images/slackware_whitelogo_med.png)

**Explain better**

Keep in mind these:<br>
1. Slackware is not providing a package manager like other distros. 
2. slackpkg is a collection of bash scripts which help root to update/upgrade **officially binaries** and patches, but not to build from source!
3. Although Slackware source and SlackBuilds are in public view, there is non official tool for building from source. Only manually way is possible. 
4. Every official Slackbuild has its own rulles and builds commands, because thats how PAT do the job. 


So official SlackBuild Template not needed and not exist. (I disagree but thats me...)<br>
What we have are several kind of unofficial SlackBuilds. Which will be listed here:

* [SBo](./scripts/SlackBuilds-Templates.tar.xz) Templates that use SlackBuilds.org 
* [Aliens SlackBuild Toolkit](https://alien.slackbook.org/AST/) Eric Hameleers (aka alienBOB)
* [slkbuild](https://github.com/gapan/slkbuild) arch-like wrapper script for easy slackware packaging
* [Martin Lefebvre](https://www.slackwiki.com/Different_Approach_To_Buildscripts) Different Approach To Buildscripts
* [AthOS](https://github.com/rizitis/PLASMA_WORLD) this is what i use for personal builds. Its totaly different for classic SlackBuild from first view but that not true...
* [Writing_A_SlackBuild_Script](https://www.slackwiki.com/Writing_A_SlackBuild_Script) How to write your own.

From above the most famous are SBo and alienBOB. Also slkbuild is used from SlaxOS,Slint and Slackel. And its more combative with slap-get package manager. 


---

### Tip

In case you really want to use a script (download,edit,build) from official SlackBuilds provided by distro, you can use the unofficial [slackpkg_build](./scripts/slackpkg_build.sh) script.<br>
It works with most of official SlackBuilds as long as a package.SlackBuild exist appstream.<br>
If a package provided from a different name SlackBuild will not work.<br>
By default it read your `/etc/slackpkg/mirrors` and download from this mirror what you ask.<br>

example: 
```
slackpkg_build emacs

                                                        
  ██████  ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ █     █░ ▄▄▄       ██▀███  ▓█████  
▒██    ▒ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀  
░ ▓██▄   ▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███    
 ▒   ██▒▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄  ░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄   
▒██████▒▒░██████▒▓█   ▓██▒▒ ▓███▀░▒██▒ █▄░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒ 
▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░ 
░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ 
░ ░  ░    ░ ░    ░   ▒   ░        ░ ░░ ░   ░   ░    ░   ▒     ░░   ░    ░    
  ░      ░  ░     ░  ░░ ░      ░  ░       ░          ░  ░   ░        ░  ░ 
                         ░                                             
                                                                        



--2024-10-07 16:02:14--  http://ftp.cc.uoc.gr/mirrors/linux/slackware/slackware64-current/source/FILE_LIST
Resolving ftp.cc.uoc.gr (ftp.cc.uoc.gr)... 2001:648:2c00:6c08::2, 147.52.159.50
Connecting to ftp.cc.uoc.gr (ftp.cc.uoc.gr)|2001:648:2c00:6c08::2|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 872948 (852K) [application/octet-stream]
Saving to: ‘/tmp/tmp.4SrKMwByWB/FILE_LIST’

/tmp/tmp.4SrKMwByWB/FILE_LIST                               100%

2024-10-07 16:02:14 (3.35 MB/s) - ‘/tmp/tmp.4SrKMwByWB/FILE_LIST’ saved [872948/872948]

Following dependencies required for emacs:
 at-spi2-atk is not installed.
 at-spi2-core is already installed.
 atk is already installed.
 brotli is already installed.
 cairo is already installed.
 dbus is already installed.
 elogind is already installed.
 fontconfig is already installed.
 freetype is already installed.
 fribidi is already installed.
 gdk-pixbuf2 is already installed.
 giflib is already installed.
 glib2 is already installed.
 gnutls is already installed.
 graphite2 is already installed.
 gtk+3 is already installed.
 harfbuzz is already installed.
 jansson is already installed.
 lcms2 is already installed.
 libICE is already installed.
 libSM is already installed.
 libX11 is already installed.
 libXau is already installed.
 libXcomposite is already installed.
 libXcursor is already installed.
 libXdamage is already installed.
 libXdmcp is already installed.
 libXext is already installed.
 libXfixes is already installed.
 libXft is already installed.
 libXi is already installed.
 libXinerama is already installed.
 libXpm is already installed.
 libXrandr is already installed.
 libXrender is already installed.
 libepoxy is already installed.
 libglvnd is already installed.
 librsvg is already installed.
 libunistring is already installed.
 libwebp is already installed.
 libxcb is already installed.
 libxkbcommon is already installed.
 libxml2 is already installed.
 nettle is already installed.
 p11-kit is already installed.
 pango is already installed.
 pixman is already installed.
 util-linux is already installed.
 wayland is already installed.
Do you want to continue? (y/n): y
Continuing...
Finding Remote Path for: emacs
=========================
Path: /e/emacs
=========================

Package Downloaded                                                                
===================
emacs has been successfully downloaded.
===================

Files in /tmp/slackpkg-build for package emacs:
===================
doinst.sh.gz  emacs-29.4.tar.xz  emacs-29.4.tar.xz.sig  emacs.SlackBuild  emacs.SlackBuild.regular-build  emacs.SlackBuild.with-native-compilation  slack-desc
===================

Important Information
===================
If emacs.SlackBuild is not visible, you can't build the package.
It might be part of a larger project that builds multiple files with one SlackBuild.
You can find more informations: http://ftp.cc.uoc.gr/mirrors/linux/slackware/slackware64-current/source/e/emacs
===================

Do you want to build or stop? (yes/no):

```

If you dont want to build , but first patch then:

```
Do you want to build or stop? (yes/no):no
Stopping the build progress.
You may continue in /tmp/slackpkg-build/emacs 

```

Or if you want to build-rebuild as is:

```
Do you want to build or stop? (yes/no):yes
...
Slackware package /tmp/emacs-29.4-x86_64-2.txz created.

Package 'emacs' built successfully.
Binary stored in /tmp/slackpkg-build/emacs, ready for installation.
 

```
---

### Captain-Slack

You might like it or find it helpful... <br>
[cptn](https://github.com/rizitis/captain-slack)


