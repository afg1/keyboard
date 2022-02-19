from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware

class MacroBoard:
    """
    Ths class is meant to implement a generic macro board class

    It takes a dictionary mapping keys to functions (must be actual pmk.keys instances) which
    have been decorated to indicate their type (launcher, macro etc)

    The decoration allows colour coding the buttons by what they do
    """
    def __init__(self):
        pass
        


    def assign_keys(self, key_dict):
        for key, func in key_dict.items():
            ## Handle key colours - based on attribute set in the decorator of the function
            ## we are attaching to this key
            if hasattr(func, "is_launcher"):
                key.set_led(0,128,0)
            elif hasattr(func, "is_exit"):
                key.set_led(128,0,0)
            elif hasattr(func, "is_macro"):
                key.set_led(0,0,128)
            elif hasattr(func, "is_noop"):
                key.set_led(0,0,0)

            ## Attach the function to the key now
            key.press_function = func

    def run(self, pmk):
        while True: 
            pmk.update()
