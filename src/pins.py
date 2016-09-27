"""Settings for all input and output pins used by other modules.

Uses RPi.GPIO.
"""
import RPi.GPIO as GPIO
mode = GPIO.BCM # Numbering system

status_data = 16 # For status LED shift register.
status_clock = 20
status_latch = 21

outputs = [status_data, status_clock, status_latch]
