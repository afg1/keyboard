from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import random
import utils

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)



## define functions to link up with keys. Use decorators to indicate type

@utils.launcher
def launch_vscode():
    """
    Requires powertoys on windows, or maping alt + space to launcher
    """
    keyboard.send(Keycode.CONTROL, Keycode.SPACE)
    keyboard.send(Keycode.DELETE)
    layout.write("Code")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)

@utils.launcher
def launch_terminal():
    keyboard.send(Keycode.CONTROL, Keycode.SPACE)
    keyboard.send(Keycode.DELETE)
    layout.write("Terminal")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)

@utils.macro
def run_update():
    keyboard.send(Keycode.CONTROL, Keycode.SPACE)
    keyboard.send(Keycode.DELETE)
    layout.write("Terminal")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)
    utils.sleep(0.2)
    layout.write("sudo apt update && sudo apt upgrade")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)

@utils.emergency_exit
def zoom_nuke():
    keyboard.send(Keycode.LEFT_ALT, Keycode.Q)

@utils.noop
def noop():
    print("This key does nothing!")


def run_linux(pmk, hardware):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    print(alphabet)

    keycodes = {
        "win": Keycode.WINDOWS}

    for letter in alphabet:
        keycodes[letter] = layout.keycodes(letter)[0]
        
    keymap = { k : noop for k in pmk.keys} 


    keymap[pmk.keys[0]] = launch_vscode
    keymap[pmk.keys[1]] = launch_terminal
    keymap[pmk.keys[2]] = run_update
    keymap[pmk.keys[3]] = zoom_nuke

    return keymap
