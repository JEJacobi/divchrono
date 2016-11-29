"""
Module for handling GPIO pin setup and settings.

Uses RPi.GPIO
"""

import RPi.GPIO as GPIO

mode = GPIO.BCM    # GPIO addressing system. Use the BCM ports instead of IO numbers.

status_data = 17   # For status LED shift register.
status_clock = 27
status_latch = 4
display_data = 23  # For Nixie tube shift registers.
display_clock = 24
display_latch = 15
display_blank = 18 # Nixie tube PWM brightness control.

button_left = 22   # Case pushbuttons (active low).
button_right = 10
button_up = 9
button_down = 11
encoder_d1 = 25    # Encoded rotary switch data.
encoder_d2 = 8
encoder_d3 = 7

# Pins to configure as outputs:

outputs = [
    status_data, 
    status_clock, 
    status_latch, 
    display_data,
    display_clock,
    display_latch,
    display_blank
]

# Pins to configure as inputs:

inputs = [
    button_left,
    button_right,
    button_up,
    button_down,
    encoder_d1,
    encoder_d2,
    encoder_d3
]

def init():
    """Initalize GPIO, set up input and output pins."""

    # TODO: Log any warnings and raspi board information with GPIO.RPI_INFO.
    #       Also report current GPIO module version with GPIO.VERSION.

    GPIO.setwarnings(False)
    GPIO.setmode(mode)
    GPIO.setup(inputs, GPIO.IN)
    GPIO.setup(outputs, GPIO.OUT, initial=GPIO.LOW)

def destroy():
    """Clean up, stop using GPIO pins."""
    GPIO.cleanup()

