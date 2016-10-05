"""Module for setting the states of status LEDs.

Uses PRi.GPIO, pins, time

leds[]: Names of each LED, ordered.
states{}: Names of each LED and its current desired state, unordered.

init(): initalizes everything.
update(p): Outputs current desired LED set state to hardware.
"""

import RPi.GPIO as GPIO
import pins
import time

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
    """Initializes LED current state dict and sets LEDs to on by default."""
    for led in leds:
        states[led] = 1

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
