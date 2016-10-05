"""Module for handling GPIO pin setup and settings.

Uses RPi.GPIO
"""
import RPi.GPIO as GPIO

mode = GPIO.BCM # Numbering system

status_data = 17 # For status LED shift register.
status_clock = 27
status_latch = 4
display_data = 23
display_clock = 24
display_latch = 15
display_blank = 18
button_left = 22
button_right = 10
button_up = 9
button_down = 11
encoder_d1 = 25
encoder_d2 = 8
encoder_d3 = 7


outputs = [
    status_data, 
    status_clock, 
    status_latch, 
    display_data,
    display_clock,
    display_latch,
    display_blank
]

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
    GPIO.setwarnings(False)
    GPIO.setmode(mode)

    for x in outputs:
        GPIO.setup(x, GPIO.OUT)

    for x in inputs:
        GPIO.setup(x, GPIO.IN)

def destroy():
    """Clean up, stop using GPIO pins."""
    GPIO.cleanup()
