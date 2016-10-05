"""Module for handling GPIO pin setup and settings.

Uses RPi.GPIO
"""
import RPi.GPIO as GPIO

mode = GPIO.BCM # Numbering system

status_data = 16 # For status LED shift register.
status_clock = 20
status_latch = 21

outputs = [status_data, status_clock, status_latch]
inputs = []

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(mode)

    for x in outputs:
        GPIO.setup(x, GPIO.OUT)

    for x in inputs:
        GPIO.setup(x, GPIO.IN)

def destroy():
    """Clean up, stop using GPIO pins."""
    GPIO.cleanup()
