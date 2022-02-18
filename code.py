from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware

from keyboard_windows import run_windows

def windows_splash(pmk):
    brightness = 255
    for i in range(25):
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




hardware = Hardware()
pmk = PMK(hardware)

pmk.keys[0].set_led(255,0,0)
pmk.keys[1].set_led(0,255,0)
pmk.keys[2].set_led(0,0,255)


while True:
    pmk.update()
    if pmk.keys[0].pressed:
        print("Loading windows keymaps...")
        win = True
        windows_splash(pmk)
        break


if win:
    run_windows(pmk, hardware)



