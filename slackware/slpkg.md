# slpkg setup 

[![slpkg](https://gitlab.com/dslackw/slpkg/-/raw/site/docs/images/logo.png)](https://dslackw.gitlab.io/slpkg/)


### /etc/slpkg/repositories.toml
---
This is a slpkg example  setup for Slackware-**current**:

---


> [DEFAULT]
> REPOSITORY = "slack"
> 
> [NEW_PACKAGES]
> REPOSITORIES = ["gnome"]
> 
> [REMOVE_PACKAGES]
> REPOSITORIES = []
> [SBO]
> ENABLE = false
> 
> [PONCE]
> ENABLE = true
> MIRROR = "https://github.com/Ponce/slackbuilds.git"
> 
> [SLACK]
> ENABLE = true
> MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-current/"
> 
> [SLACK_EXTRA]
> ENABLE = true
> MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-current/extra/"
> 
> [SLACK_PATCHES]
> ENABLE = false
> MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-15.0/patches/"
> 
> [ALIEN]
> ENABLE = true
> MIRROR = "https://slackware.nl/people/alien/sbrepos/15.0/x86_64/"
> 
> [MULTILIB]
> ENABLE = false
> MIRROR = "https://slackware.nl/people/alien/multilib/15.0/"
> 
> [RESTRICTED]
> ENABLE = true
> MIRROR = "https://slackware.nl/people/alien/restricted_sbrepos/15.0/x86_64/"
> 
> [GNOME]
> ENABLE = true
> MIRROR = "https://reddoglinux.ddns.net/linux/gnome/46.x/x86_64/"
> 
> [MSB]
> ENABLE = false
> MIRROR = "https://slackware.uk/msb/15.0/1.28/x86_64/"
> 
> [CSB]
> ENABLE = false
> MIRROR = "https://slackware.uk/csb/15.0/x86_64/"
> 
> [CONRAID]
> ENABLE = true
> MIRROR = "https://slackers.it/repository/slackware64-current/"
> 
> [SLACKONLY]
> ENABLE = false
> MIRROR = "https://packages.slackonly.com/pub/packages/15.0-x86_64/"
> 
> [SALIX]
> ENABLE = false
> MIRROR = "https://repo.greeklug.gr/data/pub/linux/salix/x86_64/15.0/"
> 
> [SALIX_EXTRA]
> ENABLE = false
> MIRROR = "https://repo.greeklug.gr/data/pub/linux/salix/x86_64/extra-15.0/"
> 
> [SLACKEL]
> ENABLE = false
> MIRROR = "http://www.slackel.gr/repo/x86_64/current/"
> 
> [SLINT]
> ENABLE = false
> MIRROR = "https://slackware.uk/slint/x86_64/slint-15.0/"
> 
> [PPRKUT]
> ENABLE = true
> MIRROR = "https://repo.liwjatan.org/pprkut/current/x86_64/"
> 
> [COSMIC]
> ENABLE = true
> MIRROR = "https://reddoglinux.ddns.net/linux/cosmic/x86_64/"
> TAG = "cosmic"

---

### /etc/slpkg/slpkg.toml
---
This is my setup for `hp omen 16 cpu 12700h` 

---
>
> [CONFIGS] 
> OS_ARCH = "x86_64"
> 

> DOWNLOAD_ONLY_PATH = "/tmp/slpkg/"

> FILE_LIST_SUFFIX = ".pkgs"
> 
> PACKAGE_TYPE = [".tgz", ".txz"]
> 
> COLORS = true
> 
> MAKEFLAGS = "-j20"
> 
> GPG_VERIFICATION = false
> 
> CHECKSUM_MD5 = true
> 
> DIALOG = true
> 
> VIEW_MISSING_DEPS = true
> 
> PACKAGE_METHOD = false
> 
> DOWNGRADE_PACKAGES = false
> 
> DELETE_SOURCES = false
> 
> ASCII_CHARACTERS = true
> 
> ASK_QUESTION = true
> 
> KERNEL_VERSION = true
> 
> PARALLEL_DOWNLOADS = false
> 
> MAXIMUM_PARALLEL = 15
> 
> PROGRESS_BAR = false
> 
> PROGRESS_SPINNER = "spinner"
> 
> SPINNER_COLOR = "green"
> 
> BORDER_COLOR = "bold_green"
> 
> PROCESS_LOG = true
>
> INSTALLPKG = "upgradepkg --install-new"
> 
> REINSTALL = "upgradepkg --reinstall"
> 
> REMOVEPKG = "removepkg"
> 
> DOWNLOADER = "wget"
> 
> WGET_OPTIONS = "-c -q --progress=bar:force:noscroll --show-progress"
> 
> CURL_OPTIONS = ""
> 
> LFTP_GET_OPTIONS = "-c get -e"
> 
> LFTP_MIRROR_OPTIONS = "-c mirror --parallel=100 --only-newer --delete"
> 
> GIT_CLONE = "git clone --depth 1 "
> 
> URLLIB_RETRIES = false
> URLLIB_REDIRECT = false
> URLLIB_TIMEOUT = 3.0
> 
> PROXY_ADDRESS = ""
> PROXY_USERNAME = ""
> PROXY_PASSWORD = ""
>
---

##### slpkg commands
`man slpkg`

---

**TIPS**
1. `slpkg -u` updates or enabled repos.
2. `slpkg -U` upgrades installed packages **only** for the default repo. 
3. `slpkg -U -o repo_name` upgrade installed packages for specific repo.
4. `slpkg -s package_name` search for package or slackbuild only to default repo
5. `slpkg -s package_name -o '*'` search for in all repos
6. `slpkg -i package_name` build and install or install binary from default repo
7. `slpkg -i package_name -o repo_name` install from specific repo
8. `sudo slpkg -t package_name` list deps of package
9. `sudo slpkg -e package_name` list which packages dependes-on this package
10. ....

---