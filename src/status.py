"""
Module for setting the states of status LEDs.

Uses PRi.GPIO, pins, time, atexit

leds[]: Names of each LED, ordered.
states{}: Names of each LED and its current desired state, unordered.

init(): initalizes everything.
update(p): Outputs current desired LED set state to hardware.
destroy(): Clean up.
"""

import RPi.GPIO as GPIO
import pins
import time
import atexit

leds = [ # LED names, in physical order.
    'pwr',
    'heartbeat',
    'rtc_ok',
    'ntp_ok',
    'net_ok',
    'alarm',
    'audio',
    'unused'
]

states = {} # Name and current desired value of each LED.

def init():
    """Initializes LED current state dict and GPIO interface based off settings in pins module."""
    GPIO.setwarnings(False)
    GPIO.setmode(pins.mode)

    for x in pins.outputs:
        GPIO.setup(x, GPIO.OUT)

    for led in leds: # Default all LED states to on.
        states[led] = 1

    atexit.register(destroy) # Make sure destroy() runs on exit. 

def update(p = 0.000001):
    """
    Output LED settings from states{} to shift register.

    Argument is time to wait in seconds between actions, 0.000001 by default.
    Pins module settings used for outputs.
    """

    data = pins.status_data
    clock = pins.status_clock
    latch = pins.status_latch

    for led in leds:
        time.sleep(p)
        GPIO.output(data, states[led]) # Set data
        time.sleep(p)
        GPIO.output(clock, 0) # Unset clock 
        time.sleep(p)
        GPIO.output(clock, 1) # Pulse clock
    time.sleep(p)
    GPIO.output(latch, 0) # Unset latch
    time.sleep(p)
    GPIO.output(latch, 1) # Pulse latch
    time.sleep(p)

def destroy():
    """Clean up, stop using GPIO pins."""
    print("Bye!")
    GPIO.cleanup()
