#!/usr/bin/env python

"""Take a VM screenshot using the VirtualBox API"""

import win32com.client
from win32com.client import constants

def take_screenshot(vm_name, screenshot_path='screenshot.png'):
    """Create a VM Screenshot for a given VM"""

    vbox = win32com.client.Dispatch("VirtualBox.VirtualBox")
    session = win32com.client.Dispatch("VirtualBox.Session")

    machine = vbox.FindMachine(vm_name)

    machine.LockMachine(session, constants.LockType_Shared)

    display = session.Console.Display
    width, height, _, _, _, _ = display.GetScreenResolution(0)
    screenshot = display.TakeScreenShotToArray(0, width, height,
                                               constants.BitmapFormat_PNG)

    session.UnlockMachine()

    with open(screenshot_path, 'wb') as output_png:
        output_png.write(screenshot.tobytes())

if __name__ == '__main__':
    take_screenshot('example_vm')
