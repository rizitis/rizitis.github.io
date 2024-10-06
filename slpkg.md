---
layout: default
title: "slpkg setup"
---

### /etc/slpkg/repositories.toml

This is an example setup for Slackware-`current`:

```
[DEFAULT]
# This is the DEFAULT REPOSITORY.
# You can change it with one that you see below.
# Make sure you have enabled it before.
REPOSITORY = "slack"

[NEW_PACKAGES]
# Configure the repositories that you want new packages to be added
# when upgrading installed packages. Only useful for repositories that
# are fully installed on the system. Example ["slack", "gnome"].
# Normally you should see the new packages first to install.
REPOSITORIES = ["slack", "gnome"]

[REMOVE_PACKAGES]
# Configure the repositories that you want to remove installed packages
# that no longer exist in the repository. Only useful for repositories
# that are fully installed on the system. Example ["slack", "gnome"].
# WARNING: Always check which packages are going to remove before proceed.
REPOSITORIES = []

[SBO]
ENABLE = false
#MIRROR = "https://slackbuilds.org/slackbuilds/15.0/"
# Alternative, you can use the git repository.
 MIRROR = "https://github.com/SlackBuildsOrg/slackbuilds.git"

[PONCE]
ENABLE = true
#MIRROR = "https://cgit.ponce.cc/slackbuilds/plain/"
# Alternative, you can use the git repository.
MIRROR = "https://github.com/Ponce/slackbuilds.git"

[SLACK]
ENABLE = true
MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-current/"

[SLACK_EXTRA]
ENABLE = true
MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-current/extra/"

[SLACK_PATCHES]
ENABLE = false
MIRROR = "http://mirror.nl.leaseweb.net/slackware/slackware64-15.0/patches/"

[ALIEN]
ENABLE = true
MIRROR = "https://slackware.nl/people/alien/sbrepos/15.0/x86_64/"

[MULTILIB]
ENABLE = false
MIRROR = "https://slackware.nl/people/alien/multilib/15.0/"

[RESTRICTED]
ENABLE = true
MIRROR = "https://slackware.nl/people/alien/restricted_sbrepos/15.0/x86_64/"

[GNOME]
ENABLE = true
MIRROR = "https://reddoglinux.ddns.net/linux/gnome/46.x/x86_64/"

[MSB]
ENABLE = false
MIRROR = "https://slackware.uk/msb/15.0/1.28/x86_64/"

[CSB]
ENABLE = false
MIRROR = "https://slackware.uk/csb/15.0/x86_64/"

[CONRAID]
ENABLE = true
MIRROR = "https://slackers.it/repository/slackware64-current/"

[SLACKONLY]
ENABLE = false
MIRROR = "https://packages.slackonly.com/pub/packages/15.0-x86_64/"

[SALIX]
ENABLE = false
MIRROR = "https://repo.greeklug.gr/data/pub/linux/salix/x86_64/15.0/"

[SALIX_EXTRA]
ENABLE = false
MIRROR = "https://repo.greeklug.gr/data/pub/linux/salix/x86_64/extra-15.0/"

[SLACKEL]
ENABLE = false
MIRROR = "http://www.slackel.gr/repo/x86_64/current/"

[SLINT]
ENABLE = false
MIRROR = "https://slackware.uk/slint/x86_64/slint-15.0/"

[PPRKUT]
ENABLE = true
MIRROR = "https://repo.liwjatan.org/pprkut/current/x86_64/"

[COSMIC]
ENABLE = true
MIRROR = "https://reddoglinux.ddns.net/linux/cosmic/x86_64/"
TAG = "cosmic"
```

---

### /etc/slpkg/slpkg.toml

This example is for *hp omen laptop cpu 12700h*

```
[CONFIGS]

# OS architecture by default.
OS_ARCH = "x86_64"

# Where the packages download.
# This path works only with the command download.
DOWNLOAD_ONLY_PATH = "/tmp/slpkg/"

# File suffix for list packages.
# Change here if you are going to use '.sqf' files.
FILE_LIST_SUFFIX = ".pkgs"

# List of suffixes for binary packages.
PACKAGE_TYPE = [".tgz", ".txz"]

# Configs for displaying colorful menu. Default is true. [true/false]
COLORS = true

# Specify the number of jobs to run concurrently. Default is '-j4'.
MAKEFLAGS = "-j20"

# Set for GPG verification. Default is false.
# If you set true, you should update the repositories for GPG-KEY import.
GPG_VERIFICATION = false

# Set for checksum md5 verification. Default is true. [true/false]
CHECKSUM_MD5 = true

# Dialog is a program that will let you present a variety of questions or
# display messages using dialog boxes from a shell script.
# Default is true. [true/false]
DIALOG = true

# View missing dependencies as main packages from the repository.
# Some repositories include packages as dependencies,
# but not as main packages. Default is true. [true/false]
VIEW_MISSING_DEPS = true

# There are two different methods to choose when you want to upgrade
# your installed packages, "version" method and "package" method.
# With the "version" method (it is by default), it will compare
# the version and the build number of the packages following the
# semantic versioning, and with the "package" method it will compare
# for different package between installed and repository and this
# means it will suggest also downgrades if the installed package
# is newer than the repository package. Default is false. [true/false]
PACKAGE_METHOD = false

# This setting allows you to downgrade packages.
# It works if the package method it is false.
# Default is false. [true/false]
DOWNGRADE_PACKAGES = false

# Delete downloaded sources after build or install packages.
# Default is false. [true/false]
DELETE_SOURCES = false

# Choose ascii printable characters.
# If true, it uses the extended characters, otherwise the basic ones.
# Default is true. [true/false].
ASCII_CHARACTERS = true

# Set false to all the questions. If set false, option --yes will
# not work. Default is true. [true/false].
ASK_QUESTION = true

# This config removes the kernel version from some slackbuilds custom
# version build, like nvidia-kernel and virtualbox-kernel slackbuild packages.
# It helps to compare install and repository versions.
# Default is true. [true/false].
KERNEL_VERSION = true

# Download sources in parallel. Default is false. [true/false]
# Alternatively, you can use the option '--parallel'.
PARALLEL_DOWNLOADS = false

# Specifies number of concurrent download streams. Default is 5.
MAXIMUM_PARALLEL = 15

# If progress bar is true, it does not print the commands as they
# are executed. Default is false. [true/false]
PROGRESS_BAR = false

# There are 5 predefined spinners for the progress bar.
# Default is spinner. [spinner/pie/moon/line/pixel/ball/clock]
PROGRESS_SPINNER = "spinner"

# Choose color for the progress bar spinner.
# Default is white. [white/green/violet/yellow/blue/cyan/grey/red]
SPINNER_COLOR = "green"

# Choose color for the border box.
# Bold colors: [bold_green/bold_cyan/bold_yellow/bold_red/bold_blue]
# Colors: [white/green/cyan/yellow/red/blue]
# Default is bold_green.
BORDER_COLOR = "bold_green"

# Keep process log files on /var/log/slpkg/ folder.
# Default is true. [true/false]
PROCESS_LOG = true

# Slackware command for installation packages, instead, you can use
# 'installpkg'. Normally upgradepkg only upgrades packages that are
# already installed on the system, and will skip any packages that
# do not already have a version installed. If --install-new is specified,
# the behavior is modified to install new packages in addition to
# upgrading existing ones. See manpage of the upgradepkg.
INSTALLPKG = "upgradepkg --install-new"

# Slackware command to reinstall packages.
# Upgradepkg usually skips packages if the exact same package
# (matching name, version, arch, and build number) is already installed
# on the system. Use the --reinstall option if you want to upgrade all
# packages even if the same version is already installed.
REINSTALL = "upgradepkg --reinstall"

# Slackware command to remove packages.
# removepkg removes a previously installed Slackware package, while
# writing a progress report to the standard output. A package may be
# specified either by the full package name (as you'd see listed in
# /var/lib/pkgtools/packages/), or by the base package name.
# See manpage of the removepkg.
REMOVEPKG = "removepkg"

# You can choose a downloader among wget, wget2, curl and lftp.
# Default is wget. [wget/wget2/curl/lftp]
DOWNLOADER = "wget"

# Wget downloader options.
# -c, --continue: resume getting a partially-downloaded file.
# -q, Turn off Wget's output.
# --show-progress, Force wget to display the progress bar in any verbosity.
WGET_OPTIONS = "-c -q --progress=bar:force:noscroll --show-progress"

# Curl downloader options.
CURL_OPTIONS = ""

# Lftp donwloader options.
LFTP_GET_OPTIONS = "-c get -e"

# Lftp mirror options are used to synchronize with the SBo and
# Ponce repositories or for the local repositories.
LFTP_MIRROR_OPTIONS = "-c mirror --parallel=100 --only-newer --delete"

# Instead of the lftp command to synchronize the Slackbuilds repositories
# (sbo and ponce) you can use the git clone command, after you have also
# changed the mirror in the repositories.toml file.
GIT_CLONE = "git clone --depth 1 "

# Python urllib3 settings used for checking between two changelog files.
# Timeouts allow you to control how long (in seconds) requests are allowed
# to run before being aborted. In simple cases, you can specify a timeout
# as a float. By default, urllib3 will retry requests 3 times and follow
# up to 3 redirects. For more please visit:
# https://urllib3.readthedocs.io/en/stable/user-guide.html
URLLIB_RETRIES = false
URLLIB_REDIRECT = false
URLLIB_TIMEOUT = 3.0

# If you are going to use a proxy server, try to fill in these variables.
# Choose between http or socks proxy type.
# For a sock proxy, you need to install the PySocks package.
# https://urllib3.readthedocs.io/en/stable/advanced-usage.html#socks-proxies
PROXY_ADDRESS = ""
PROXY_USERNAME = ""
PROXY_PASSWORD = ""
```

`man slpkg` for commands ;) <br>
