# IMPORTS

import sys
import time

import pins
import status
import encoder

# MAIN

def main():
    pins.init()
    status.init()

    while True:
       newpos = encoder.getpos()

       if newpos is not None:
           status.states = dict.fromkeys(status.states, 0)
           status.states[status.leds[newpos]] = 1
           status.update()

       time.sleep(0.1)
       

# EXECUTION

if __name__ == '__main__':
    sys.exit(main())

