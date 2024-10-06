# init

![ALT](./images/slackware_logo_med.png)

This is the Slackware init system for boot:

> runlevel 1 executes `/etc/rc.d/rc.S`. <br>
>runlevel 3 executes `/etc/rc.d/rc.S`, then `/etc/rc.d/rc.M`.<br>
 >runlevel 4 executes `/etc/rc.d/rc.S`, `/etc/rc.d/rc.M` and `/etc/rc.d/rc.4`. 
 >Shutting down executes `/etc/rc.d/rc.K`.
 
 There is also `/etc/rc.d/rc.local` and you can create an `/etc/rc.d/rc.local_shutdown` for specific scripts/services. <br>
 `ls -l /etc/rc.d/` will print in your terminal what rc.script are executable or not. Everything it not then simple do not start. <br>
 
 
 
 Slackware keep things simple stupids **(KISS)** and don't follow the complex madness of modern confusion philosophy. <br>
 So far is staying away from systemd (personal I hope for ever) but it can work with systemd, dinit , openrc or vera. <br>
 
 * [systemd](https://slackernet.ddns.net/slackware/slackware64-15.0/testing/source/systemd/x86_64/) for fun!
* [dinit](https://github.com/0xBOBF/dinit-slackware) for testing! (not 100% ready)
* [OpenRC](https://docs.slackware.com/howtos:general_admin:openrc) for enjoy!
* [vera](https://github.com/svarshavchik/vera) for the hack and the win! 

Vera is a very promise project ...