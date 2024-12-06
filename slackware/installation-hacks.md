# installation-hacks

### slackwareaarch64-current
For [aarch64/arm64](https://slackware.lngn.net/) <~ thats your heretic-place

---

**FOR PC/LAPTOPS**<br>
---

- History notes
  - Slackware Linux was first released before CD-ROMs became a standard in systems  and before fast Internet connections were cheap.<br>
  Because of this, the distribution was broken down into software sets. Each set contains a different group of programs.<br>
  This allowed for someone to get the Slackware Linux distribution quickly. For example, if you know you don't want the X Window System, just skip all of the X software set.<br>
  - Now days things are better, but for historical reasons Slackware kept the same structure.
  Any way a full Slackware installation is always the better and safe choise, but sometime we dont realy like or want or need it...<br>
  So **A**, **AP**, **F**, **L**, and **N** are for sure what **MUST** be installed for a very minimal installation of custom Slackware system<br>
  That not mean other sets are optionals but lets say you dont want emacs,howtos,KDE,xfce etc... <br>
  What Ι can say (but not suggest) is this: 
  - Every set has inside a `tagfile` if some day you think you need one more set but not all of it at least install<br> from `tagfile` everything has `:REC` and `:ADD` option. But even this its not a mandatory for example gcc is :OPT which is true,<br> in theory its not requitment for a Linux system but do you realy not need it? You know... 
  Again what i can say but not suggest is:
  - If you install everything is :REC and :ADD in tagfile(s) you will have a `custom` booting Slackware system 100%, **but** if you need to install something more or compile etc... you are on your `own` for deps resolution. 
  Presonally I always have a full Slackware installation.
  
  --- 
  
  **SETS**

| set |                                                   Description                                                           |
|-----|-------------------------------------------------------------------------------------------------------------------------|
| `A` | The base system. Contains enough software to get up and running and have a text editor and basic communications programs|
| `AP`| Various APplications that do not require the X Window System.                                                           |
| `D` | Program Development tools. Compilers, debuggers, interpreters, and man pages. It's all here.                            |
| `E` | GNU Emacs. Yes, Emacs is so big it requires its own series.                                                             |
| `F` | FAQs, HOWTOs, and other miscellaneous documentation.                                                                    |
| `K` | The source code for the Linux Kernel.                                                                                   |
|`KDE`| KDE-PLASMA The Qt widget library is also in this series, as KDE requires it to function.                                |
| `L` | System Libraries.                                                                                                       |
| `N` | Networking programs. Daemons, mail programs, telnet, news readers, and so on.                                           |
| `T` | teTeX document formatting system.                                                                                       |
|`TCL`| The Tool Command Language                                                                                               |
| `X` | The base X Window System X11, Wayland..                                                                                 |
|`XAP`| X APplications that are not part of a major desktop environment                                                         |
| `Υ` | Games (the BSD games collection, Sasteroids, Koules, and Lizards).                                                      |


Note that [volkerdi](https://www.linuxquestions.org/questions/showpost.php?p=5766773) the founder , owner, and maintainer of Slackware said:<br>
- Arguing about which series any particular package belongs in is even more pointless than having separate package series in the first place. Really, everything should just be dumped in one big package directory so that people don't get carried away with the idea that the divisions actually mean something.
- [Also](https://www.linuxquestions.org/questions/showpost.php?p=5856424), it's strange to keep fixating on which series a package belongs in, as if it's a dependency system or something.
- [AND](https://www.linuxquestions.org/questions/showpost.php?p=5920588)I'll change the status from OPT to REC at some point soon, though I'll note that none of those tags are any guarantee that dependencies in Slackware will actually be met. Only a full install is.<br>

Since libunistring is a rather large library I'm not inclined to add it to the aaa_elflibs package, especially since wget isn't part of the A series. And again, I'll note that these series divisions are largely legacy and shouldn't really be paid much attention.
---

**tagfile**<br>
**The old but true** [slackbook](https://slackbook.org/html/package-management-making-tags-and-tagfiles.html) explain better:<br>

The Slackware setup program handles installation of the software packages on your system. There are files that tell the setup program which packages must be installed, which ones are optional, and which ones are selected by default by the setup program.<br>

A tagfile is in the first software series directory and is called tagfile. It lists the packages in that particular disk set and their status. The status can be:


|Option| 	              Meaning                          |
|------|---------------------------------------------------|
| `ADD`|The package is required for proper system operation|
| `SKP`|The package will be automatically skipped          |
| `REC`|The package is not required, but recommended       |
| `OPT`|The package is optional                            |


One package per line. The original tagfiles for each software series are stored as tagfile.org. So if you mess up yours, you can restore the original one.<br>

Many administrators prefer writing their own tagfiles and starting the installer and selecting “full”. The setup program will read the tagfiles and perform the installation according to their contents.<br> If you use REC or OPT, a dialog box will be presented to the user asking whether or not they want a particular package.<br> Therefore, it is recommended that you stick with ADD and SKP when writing tagfiles for automated installs.
<br>
Just make sure your tagfiles are written to the same location as the originals. Or you can specify a custom tagfile path if you have custom tagfiles.

---

### TIPS

1. OK Slackware installation finish, time for your first reboot and for your first regular user.<br>
Assume you command `adduser` and now you are in `$user UID` prompt.<br>

![user UID](./images/userUID.png)


Why you just hit enter and use as User ID ('UID') [ defaults to next available ]:`?` <br>
98% of Linux systems has first user id 1000 and next one 1001... **why ?** <br>
Give to your first user id up to 10000 and if some day you create more users they will follow...him. <br>
If  a cracker target one Linux system, he know that 100{1,2,3} is user ID, lets make his life not so obviously... 
So, User ID ('UID') [ defaults to next available ]: `12000` (is a good example that crackers will not find it).<br>
**NOTE:** (Don't start users IDs up to `40000`) its not wrong but not good practice for busy systems... 

---

 2. Don't add user to sudoers group.<br>
You don't need sudo. You don't even need root, but that's a long story...(that's a blasphemy for most Slackers) <br>
Just download [xudo](https://rizitis.github.io/slackware/binaries/xudo) some ware in your $PATH and that's all.<br>
If your user  know root password can execute any command need root access. <br>
example: `xudo slackpkg update` , `xudo ./some.SlackBuild` etc...<br>
To make it even better you can rename xudo to what ever you like, assume wns (WhoNeedSudo) ;)<br>
So lets do it `mv /usr/bin/xudo /usr/bin/wns` <br>
Now your commands should be: `wns slackpkg upgrade-all` , `wnd ./some.SlackBuild` , `wns ls /root` etc... ;) <br>

**Conclusion:** cracker don't know your user ID and cant guess it because its not `100?`, also you are not in sudoers group, you don't have sudo enable and you can even disable root but that's not for now...
Note: that with xudo or what ever you name it, during command is executed you are not in full root mode (su -l) exactly, but for sure after xudo finish you are back in $USER $PATH ;).<br>
So you can use xudo for everything if it full root mode is not hard depend... <br>
Also xudo do not work with slpkg, slpkg must always used in full root mode:<br>
`su -`<br>
`slpkg $cmd`

---

### Types of Security issues

**Its very simple, they just want your system data**<br>

 
- Steel
- Corrupt
- Remove

**If target data cant be touched, next target is Applications**

- Apache server
- Database (SQL,Orcale etc)
- Any other applications

**Host is next target**


- File Coraptions
- Complite shutdown
- Process Managent(CPU RAM)

**Last target is hardware**

- Attack CPU, RAM, external connected devices
  - Disable, remove, corrupt them



---

#### LINUX

Now days things are very complicate. Linux systems are not KISS systems, and modern<br> philosophy is more close to windows boxes than old UNIX...<br>

*Thats why I dont like systemd:* <br>

1. Because log files must always be plain.txt files and not binaries files
  - So I can pipe them ... Not only for debug but mostly for security reasons...
If you can understand that then keep going here, else there is no reason loosing your time!

2. I dont like the way that distros configure systemd as a root commander and do things that kernel must do.

3. Also systems that are designed to be simple , with systemd using windows philosophy of interlocking depencencies,well thats the best way to break things.
  - So these systems or must have systemd or nothing! Really?

4. And one more question, who is now developing systemd?  hm...
  - How easy it is for developers to develop and modify systemd? <br>
 
 ---
 
 **PAM** <br>
 
   *Learn PAM, how it works and how you can modify things to connect your services/users etc...*
   - [x] Auth
   - [x] Account
   - [x] Password
   - [x] Session
   



>        ALSO:
>
>>   Requisite
>
>>   Required
>
>>   Sufficient
>
>>    optional
>


---

#### Investigate: 

`/lib64/security/` those modules and libs are speaking to system for get access<br>
Most module there are pre-build and come with your Linux system. But also new can be added there if needed.<br>
If this option was not included in PAM then we should rebuild pam every time new RSA token or other login method was out...<br>
I think `man pam_unix` is your friend...<br>

On the other hand all modules in `/lib64/security/` are encrypted so you cant find something, but what you can find is what modules your new installed package *call* (if so), *why* or *how*?.<br>
Then `man module_name` and **read** what this module do...<br>
Or are there any modules that you should add to your configuration...?<br>
    Remember pam is not only for logins but also for `/var/logs/` **read logs**... 

**Remember that first target is your data, in other words your information**

*You probably think now that I will say:*
- Dont install binaries
- Dont run AppImages
- Build your own packages..etc

    **I wont** `:D`<br>
    
    Again, now days things are very complicate, Linux systems are not KISS systems, <br>
    and modern philosophy is more close to windows boxes than old UNIX...<br>
I mean yeah, **dont install everything from everyware and dont run varius scripts** <br>
but... thats not the real problem, real problem is that we *lost the path*...
<br>

**Did I said that  log files must always be txt files and not binaries files?**<br>
- So I can pipe them
-  use them in other apps
- read them
- edit them
   -  Not only for debug but mostly for develop and security reasons now days...
For the same reason `/etc` is the most important directory in a Linux system.
So command: `egrep -v "bash|false" /etc/passwd` and `egrep -v "bash|nologin" /etc/passwd`
Read and understand wtf is going on with your services, apps etc...
Thats things are more or the same important like from were you build or install packages now days. <br>

**Privilege**
1. Who gets what?
2. Who can access what?
3. How can access ?


*Always access you system and login manually don't store passwd in plain txt files*<br>
*Encrypt disk is ok but that's only for boot, after that?*<br>

*Specify what files needed to have access your user(s), and what limits:*
  -  User accounts
  -  File Systems
  -  System access
  -  System conf files
  -  OS network

All above must have carefully and manually configuration, speaking for personal pc...
We had speak earlier how to give smart ID to your first user in your Linux. 
<br>

*Learn how to read:* `cat /etc/group`<br>

*Something useful to learn is how can edit* `/etc/security/faillock.conf` and `/etc/pam.d/system-auth` since `old pam_tally2` is not in Slackware.<br>

*But more useful would be to understand* `/etc/default/useradd` and modify it exactly for your user needs <br>

*I almost forgot, one very unknown file for "regular" linux users that you must focus and learn, that's* `/etc/login.defs`

Hack your Slackware, read and understand ALL these files you and should secure your users as needed because **Slackware** is  not only the best Linux distro, it is a learning machine...

---

- Linux system is secure by default and Slackware stable true never break, but you must do often your updates.
- Install slpkg and build packages from SlackBuilds.org
- Install a firewall, its very simple...
- Be careful with your browser. You are clever enough to know who need your data...Use open-source trusted browsers.
- Dont run localy AIs using their API and give them access to your files.
- Dont connect to unknown wifi networks.
- Build your own kernel with only what you need...
- Keep learning, every day you will learn something more... We all learning none is a teacher!
- Happy Slacking!!! 



 



 
