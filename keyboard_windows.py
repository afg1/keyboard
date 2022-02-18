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



def launch_vscode():
    """
Requires powertoys on windows, or maping alt + space to launcher
    """
    keyboard.send(Keycode.LEFT_ALT, Keycode.SPACE)
    keyboard.send(Keycode.DELETE)
    layout.write(".code")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)

def launch_wsl():
    keyboard.send(Keycode.LEFT_ALT, Keycode.SPACE)
    keyboard.send(Keycode.DELETE)
    layout.write(".ubuntu")
    # utils.sleep(0.1)
    # layout.write("cd\n")
    utils.sleep(0.1)
    keyboard.send(Keycode.ENTER)

def zoom_nuke():
    keyboard.send(Keycode.LEFT_ALT, Keycode.Q)

def run_windows(pmk, hardware):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    print(alphabet)

    keycodes = {
        "win": Keycode.WINDOWS}

    for letter in alphabet:
        keycodes[letter] = layout.keycodes(letter)[0]
        
        
    print(keycodes)

    keyboard.send(Keycode.LEFT_ALT, Keycode.SPACE)
    keyboard.send(Keycode.LEFT_ALT, Keycode.SPACE)


    ## Open keymap
    keymap = {"press":{}, "hold":{}}

    keymap["press"] = {
        0 : launch_vscode,
        1 : launch_wsl,
        3 : zoom_nuke
        }

    for key in pmk.keys:
        key.hold_time = 1
        
        @pmk.on_press(key)
        def press_keystrokes(key):
            print(type(key.number))
            keycode = keymap["press"][key.number]
            if isinstance(keycode, list):
                keyboard.send(*keycode)
            elif callable(keycode):
                keycode()
            else:
                layout.write(keycode)
            
        @pmk.on_hold(key)
        def hold_keystrokes(key):
            print(type(key.number))
            keycode = keymap["hold"][key.number]
            layout.write(keycode)


    while True:
        pmk.update()

