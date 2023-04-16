# tkRecovery

tkRecovery is a work-in-progress macOS program written with python (tkinter) to enter and exit recovery mode on iOS devices with ease. This is designed to easily re-install iOS with Finder and/or help you with the jailbreak process.

# Usage

Connect your iDevice to your Mac and choose "Enter recovery" to start the process.
Once you want to exit from recovery, just click on "Exit recovery".

# Requirements

- Mac device
- MacPorts (for installation)
- libimobiledevice (for the tool to work)

# Installation

## MacOS installation
### MacPorts: 

To install tkRecovery, you first need to install Apple's Command Line Developer Tools with `xcode-select --install`
Then, install MacPorts for your version of the Mac operating system:
- [Ventura (13)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-13-Ventura.pkg)
- [Monterey (12)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-12-Monterey.pkg)
- [Big Sur (11)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-11-BigSur.pkg)
- [Catalina (10.15)](https://github.com/macports/macports-base/releases/download/v2.8.1/MacPorts-2.8.1-10.15-Catalina.pkg)
- [Older OS? See here.](https://www.macports.org/install.php#installing)

### libimobiledevice:

Now that you installed MacPorts, you are now able to install libimobiledevice (what makes the app enter/exit recovery). To start off, type `sudo port install libimobiledevice`. This will start the installation of libimobiledevice.

## Linux installation
### libimobiledevice

To install libimobiledevice on Linux, you will need to follow this:
Type these commands in the terminal:
- `sudo add-apt-repository ppa:pmcenery/ppa`
- `sudo apt-get update`
- `sudo apt-get install libimobiledevice`

If it says Package not found, do this:

- `sudo gedit /etc/apt/sources.list`

- Replace `deb http://ppa.launchpad.net/pmcenery/ppa/ubuntu precise main` and `deb-src http://ppa.launchpad.net/pmcenery/ppa/ubuntu precise main` by `deb http://ppa.launchpad.net/pmcenery/ppa/ubuntu maverick main`  and `deb-src http://ppa.launchpad.net/pmcenery/ppa/ubuntu maverick main`.

- Save the file.
- `sudo apt-get update`
- `sudo apt-get install libimobiledevice`

If that does not work manaully download the ppa files for maverick(links below)(these are packages for 32 bit)

- [Libgpod-common](https://launchpad.net/~pmcenery/+archive/ppa/+files/libgpod-common_0.8.0-1ubuntu1~maverick1_i386.deb)
- [Libgpod4](https://launchpad.net/~pmcenery/+archive/ppa/+files/libgpod4_0.8.0-1ubuntu1~maverick1_i386.deb)
- [Libimobiledevice1](https://launchpad.net/~pmcenery/+archive/ppa/+files/libimobiledevice1_1.0.6-1ubuntu1~maverick1_i386.deb)
- [Libplist1](https://launchpad.net/~pmcenery/+archive/ppa/+files/libplist1_1.4-1ubuntu1~maverick1_i386.deb)
- [libusbmuxd1](https://launchpad.net/~pmcenery/+archive/ppa/+files/libusbmuxd1_1.0.7-1ubuntu1~maverick1_i386.deb)
- [usbmuxd](https://launchpad.net/~pmcenery/+archive/ppa/+files/usbmuxd_1.0.7-1ubuntu1~maverick1_i386.deb)

If you did these steps correctly then libimobiledevice is installed!

### tkRecovery itself

There is already a prealpha of the GUI so you can try it out.
