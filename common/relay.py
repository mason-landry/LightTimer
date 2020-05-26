# relay.py
import RPi.GPIO as GPIO

# DEFINITIONS
def relay_close(pin):
    GPIO.output(pin, GPIO.HIGH)  # close relay

def relay_open(pin):
    GPIO.output(pin, GPIO.LOW)  # open relay