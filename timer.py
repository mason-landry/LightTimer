import RPi.GPIO as GPIO
from common.relay import relay_close, relay_open 
import datetime
import time
import pickle

""" This program was written to control a custom light setup for a plant shelf. The program runs on a Raspberry
    Pi Zero W and does the following:
        1. It checks the time based on system clock using datetime
        2. If the current time is between a certain period, the lights will be turned on
        3. Otherwise the lights should remain off.
    
    Program written by:
    Mason Landry
    mason-landry@outlook.com
    09.03.2020
    """

# GPIO setup
channel = 4 # Use GPIO pin 4 on RPiZeroW
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# close relay on startup.
relay_close(channel)
state = 0   # Set initial state to be 0

if __name__ == '__main__':
    while (True):
        try:    
	    # Get sunrise & sunset values fom text files: 
            fp = open(r"/home/pi/times/sunrise.txt", "rb")
            sunrise = pickle.load(fp)
            fp.close()
            fp = open(r"/home/pi/times/sunset.txt", "rb")
            sunset = pickle.load(fp)
            fp.close()
            sunrise = datetime.time(int(sunrise[0]),int(sunrise[1]), int(sunrise[2]))
            sunset = datetime.time(int(sunset[0]),int(sunset[1]), int(sunset[2]))

            t = datetime.datetime.now().time()
            if state == 0:  #Lights are in state 'off'
                if t > sunrise and t < sunset:   #Lights should be on
                    state = 1    #Change state to 'on'
                    relay_open(channel)
                    print("Changing state to on")
                else:
                    continue    #Lights should remain off

            elif state == 1:    #Lights are in state 'on'
                if t < sunrise or t >= sunset:   #Lights should be off
                    state = 0    #Change state to 'off'
                    relay_close(channel)
                    print("Changing state to off")
                else:
                    continue #Lights should remain on
        except KeyboardInterrupt:
            GPIO.cleanup()
        
        time.sleep(5) #Wait 5 seconds
