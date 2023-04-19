# made bu 0x3ff and a fast audi r8

import tkinter
import subprocess
import platform

from tkinter import *
from tkinter import Tk, font
from tkinter import Menu
from subprocess import Popen, PIPE

import time

from scripts import *


rootWin = Tk()
font.families()


# checkstatus = 1
# while checkstatus == 1:
#     devicestatus = deviceconnected()
# 
rootWin.title('tkRecovery (0x2be, a fast audi r8)')
rootWin.geometry('500x175')

# tk gui defined items


def openNewWindow():
    # Create a new window to display the device information
    infoWin = Toplevel(rootWin)
    infoWin.title("iDevice information")
    infoWin.geometry("250x175")

    # Add labels to the window for the device information
    label = Label(infoWin, text="iDevice information", font=('System', 16))
    label.pack()

    devicename = Label(infoWin, text="Device Name:", font=('System', 12))
    devicename.pack()
    devicenameval = Label(infoWin, text=get_device_name(), font=('System', 9))
    devicenameval.pack()

    model = Label(infoWin, text="iPhone model:", font=('System', 12))
    model.pack()
    modeln = Label(infoWin, text=get_device_model(), font=('System', 9))
    modeln.pack()

    serial = Label(infoWin, text="Serial Number:", font=('System', 12))
    serial.pack()
    serialn = Label(infoWin, text=get_device_serial_number(), font=('System', 9))
    serialn.pack()

    ios = Label(infoWin, text="iOS:", font=('System', 12))
    ios.pack()
    iosv = Label(infoWin, text=get_device_ios_version(), font=('System', 9))
    iosv.pack()

def get_device_name():
    cmd = ["ideviceinfo", "-k", "DeviceName"]
    return run_command(cmd).decode("utf-8").strip()

def get_device_model():
    cmd = ["ideviceinfo", "-k", "HardwareModel"]
    return run_command(cmd).decode("utf-8").strip()

def get_device_serial_number():
    cmd = ["ideviceinfo", "-k", "SerialNumber"]
    return run_command(cmd).decode("utf-8").strip()

def get_device_ios_version():
    cmd = ["ideviceinfo", "-k", "ProductVersion"]
    return run_command(cmd).decode("utf-8").strip()

def run_command(cmd):
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    output, error = proc.communicate()
    return output

def updatestatus():
    log.config(text=f'Status: {deviceconnected()}')
    rootWin.after(1000, updatestatus)

# tk gui
label = Label(rootWin, text="tkRecovery", font=('System', 24))
label.pack()
desc = Label(rootWin, text="Easy tool to make your iDevice enter/exit recovery.", font=('System', 13))
desc.pack()
desc2 = Label(rootWin, text="(Use it when restoring or jailbreaking your iDevice)", font=('System', 10))
desc2.pack()
log = Label(rootWin, text=f"Status: {deviceconnected()}", font=('System', 12))
log.pack()

EnterButton = Button(rootWin, text="Enter Recovery", command=enterrecovery)
EnterButton.pack()
ExitButton = Button(rootWin, text="Exit Recovery", command=exitrecovery)
ExitButton.pack()

menubar = Menu(rootWin)
rootWin.config(menu=menubar)

deviceinfo_menu = Menu(menubar)

deviceinfo_menu.add_command(
    label='Show iDevice information',
    command=openNewWindow
)


# cascade buttons

menubar.add_cascade(
    label="Tool",
    menu=deviceinfo_menu
)

updatestatus()
rootWin.mainloop()