from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware

from keyboard_windows import run_windows
from keyboard_linux import run_linux
from utils import sleep


from generic_kb import MacroBoard

def windows_splash(pmk):
    brightness = 255
    for i in range(255):
        pmk.keys[0].set_led(brightness,0,0)
        pmk.keys[1].set_led(brightness,0,0)
        pmk.keys[4].set_led(brightness,0,0)
        pmk.keys[5].set_led(brightness,0,0)

        pmk.keys[2].set_led(0,brightness,0)
        pmk.keys[3].set_led(0,brightness,0)
        pmk.keys[6].set_led(0,brightness,0)
        pmk.keys[7].set_led(0,brightness,0)

        pmk.keys[8].set_led(0,0,brightness)
        pmk.keys[9].set_led(0,0,brightness)
        pmk.keys[12].set_led(0,0,brightness)
        pmk.keys[13].set_led(0,0,brightness)

        pmk.keys[10].set_led(brightness,brightness,0)
        pmk.keys[11].set_led(brightness,brightness,0)
        pmk.keys[14].set_led(brightness,brightness,0)
        pmk.keys[15].set_led(brightness,brightness,0)
        brightness -= 5
        print(brightness)
        if brightness <= 0:
            break
        sleep(0.01)


def mac_splash(pmk):
    brightness = 255
    for i in range(100):
        pmk.keys[0].set_led(brightness,0,0)
        pmk.keys[1].set_led(brightness,0,0)
        pmk.keys[4].set_led(brightness,0,0)
        pmk.keys[5].set_led(brightness,0,0)

        pmk.keys[2].set_led(0,brightness,0)
        pmk.keys[3].set_led(0,brightness,0)
        pmk.keys[6].set_led(0,brightness,0)
        pmk.keys[7].set_led(0,brightness,0)

        pmk.keys[8].set_led(0,0,brightness)
        pmk.keys[9].set_led(0,0,brightness)
        pmk.keys[12].set_led(0,0,brightness)
        pmk.keys[13].set_led(0,0,brightness)

        pmk.keys[10].set_led(brightness,brightness,0)
        pmk.keys[11].set_led(brightness,brightness,0)
        pmk.keys[14].set_led(brightness,brightness,0)
        pmk.keys[15].set_led(brightness,brightness,0)
        brightness -= 10
        if brightness <= 0:
            break
        sleep(1)


def linux_splash(pmk):
    brightness = 255
    for i in range(100):
        pmk.keys[0].set_led(brightness,0,0)
        pmk.keys[3].set_led(brightness,0,0)
        pmk.keys[4].set_led(brightness,0,0)
        pmk.keys[7].set_led(brightness,0,0)

        pmk.keys[2].set_led(0,brightness,0)
        pmk.keys[3].set_led(0,brightness,0)
        pmk.keys[6].set_led(0,brightness,0)
        pmk.keys[7].set_led(0,brightness,0)

        pmk.keys[8].set_led(0,0,brightness)
        pmk.keys[9].set_led(0,0,brightness)
        pmk.keys[12].set_led(0,0,brightness)
        pmk.keys[13].set_led(0,0,brightness)

        pmk.keys[10].set_led(brightness,brightness,0)
        pmk.keys[11].set_led(brightness,brightness,0)
        pmk.keys[14].set_led(brightness,brightness,0)
        pmk.keys[15].set_led(brightness,brightness,0)
        brightness -= 10
        if brightness <= 0:
            break
        sleep(0.01)


hardware = Hardware()
pmk = PMK(hardware)

pmk.keys[0].set_led(255,0,0)
pmk.keys[1].set_led(0,255,0)
pmk.keys[2].set_led(0,0,255)

win = False
mac = False
lin = False

while True:
    pmk.update()
    if pmk.keys[0].pressed:
        print("Loading windows keymaps...")
        win = True
        windows_splash(pmk)
        break
    elif pmk.keys[1].pressed:
        print("Loading linux keymaps...")
        lin = True
        linux_splash(pmk)
        break
    elif pmk.keys[2].pressed:
        print("Loading mac keymaps...")
        mac = True
        mac_splash(pmk)
        break


if win:
    run_windows(pmk, hardware)
elif lin:
    keymap = run_linux(pmk, hardware)
    kb = MacroBoard()
    kb.assign_keys(keymap)
    kb.run(pmk)
    # run_linux(pmk, hardware)
elif mac:
    pass


