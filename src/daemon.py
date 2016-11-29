# IMPORTS

import sys
import signal
import time

import pins
import status
import encoder

# MAIN

run = True

def main():

    #
    # INITIALIZATION
    #

    # Set up signals for graceful termination.

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Set up modules.

    pins.init()
    status.init()

    #
    # LOOP
    #

    while run is True:
       newpos = encoder.getpos()

       if newpos is None: # Turn on the last LED to indicate transit or an error.
           newpos = 7

       status.states = dict.fromkeys(status.states, 0)
       status.states[status.leds[newpos]] = 1
       status.update()

       time.sleep(0.1)

    #
    # CLEANUP
    #

    status.destroy()
    pins.destroy()

    print("Quitting!")
    return 0

def signal_handler(signal, frame):
    """Catch system signals and terminate the program gracefully."""
    global run
    print("Signal triggered!")
    run = False 

# EXECUTION

if __name__ == '__main__':
    sys.exit(main())

