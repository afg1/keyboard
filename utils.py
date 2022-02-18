import time



def sleep(seconds):
    """
    Sleep, but using time.monotonic
    """
    now = time.monotonic()
    elapsed = time.monotonic() - now
    while elapsed < seconds:
        elapsed = time.monotonic() - now

