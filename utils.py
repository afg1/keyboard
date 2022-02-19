import time
# import functools


def sleep(seconds):
    """
    Sleep, but using time.monotonic
    """
    now = time.monotonic()
    elapsed = time.monotonic() - now
    while elapsed < seconds:
        elapsed = time.monotonic() - now


class launcher():
    def __init__(self, func):
        self.func = func
        self.is_launcher = True

    def __call__(self, *args, **kwargs):
        return self.func()



class emergency_exit():
    def __init__(self, func):
        self.func = func
        self.is_exit = True
    
    def __call__(self, *args, **kwargs):

        return self.func()
    

class macro():
    def __init__(self, func):
        self.func = func
        self.is_macro = True
    
    def __call__(self, *args, **kwargs):
        return self.func()
    
class noop():
    def __init__(self, func):
        self.func = func
        self.is_noop = True
    
    def __call__(self, *args, **kwargs):
        return self.func()
    