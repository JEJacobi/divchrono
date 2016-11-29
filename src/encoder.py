"""
Module for reading the state of the encoder board.

Uses RPi.GPIO, pins
"""

import RPi.GPIO as GPIO
import pins

def getpos():
    """Return the current position of the encoder board, from 0-6, or None if in transit."""

    d1 = GPIO.input(pins.encoder_d1)
    d2 = GPIO.input(pins.encoder_d2)
    d3 = GPIO.input(pins.encoder_d3)

    if not d1 and d2 and d3:
        return 0
    elif d1 and not d2 and d3:
        return 1
    elif d1 and d2 and not d3:
        return 2
    elif not d1 and not d2 and d3:
        return 3
    elif not d1 and d2 and not d3:
        return 4
    elif d1 and not d2 and not d3:
        return 5
    elif not d1 and not d2 and not d3:
        return 6
    else:
        return None

