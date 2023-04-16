# tkRecovery

tkRecovery is a work-in-progress macOS program written with python (tkinter) to enter and exit recovery mode on iOS devices with ease. This is designed to easily re-install iOS with Finder and/or help you with the jailbreak process.

# Usage

Connect your iDevice to your Mac and choose "Enter recovery" to start the process.
Once you want to exit from recovery, just click on "Exit recovery".

# Requirements

- Mac/Linux device
- Homebrew
- libimobiledevice

# Installation

## tk:

Since this GUI was made with tkinter, you will need to install tk. For this, you will need to install Homebrew from https://brew.sh/ and then execute `brew install python-tk` in the Terminal.

## MacOS installation
### libimobiledevice:

Now that you installed Homebrew, you are now able to install libimobiledevice (what makes the app enter/exit recovery). To start off, type `brew install libimobiledevice`. This will start the installation of libimobiledevice.

## Linux installation
### libimobiledevice:

To install libimobiledevice on Linux, follow steps here: https://libimobiledevice.org/#get-started

### tkRecovery itself:

There is already a prealpha of the GUI so you can try it out.
