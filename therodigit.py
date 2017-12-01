"""
@author: Benjamin Bowring
@author: Craig Brownhill

@date: 11/2017

Script for running loop pedal application with two HC-SR04 transducer modules.
"""

### Import packages to be used throughout script

import time
import os
import numpy as np

### Define function with sensor argument that will be called to produce a value dependent
### on current distance from module that corresponds to notes pre-loaded on RPi

def reading1(sensor):

### Define GPIO pins TRIG & ECHO are connected to such that they can be defined
### in GPIO setup

    TRIG = 24
    ECHO = 23
    import time
    import RPi.GPIO as GPIO
    value = 0
    value2 = 0
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

### Function defined so that when called correctly will always operate, with exception otherwise
    
    if sensor == 0:

### TRIG pin defined as output and ECHO as input with GPIO package

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        
### TRIG is set to voltage high for 10us so as to trigger the 8 40kHz pulses

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

### ECHO is checked to be receiving no signal and a measurement of time is commenced.
### When a signal is received the ECHO input to the GPIO is high and an end time is defined
### so that a total time of travel can be calculated.

        while GPIO.input(ECHO) == 0:
            signaloff = time.time()

        while GPIO.input(ECHO) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff

### Considering double journey of pulse we can calculate the distance of the reflecting surface
### in air

        distance = (timepassed*343) /2

### A note is assigned to each step of distance and a value integer returned

        if 0 < distance < 0.125:
            value = 1

        elif 0.125 < distance < 0.25:
            value = 2

        elif 0.25 < distance < 0.375:    
            value = 3

        elif 0.375 < distance < 0.5:
            value = 4
            
        elif 0.5 < distance < 0.625:
            value = 5    

        elif 0.625 < distance < 0.75:
            value = 6
            
        elif 0.75 < distance < 0.875:
            value = 7

        elif 0.875 < distance < 1:   
            value = 8

        elif 1.125 < distance < 1.25:
            value = 9
            
        elif 1.25 < distance < 1.375:
            value = 10  

        elif 1.5 < distance < 1.625:
            value = 11
            
        else:
            value = 12
            

        return value

    
    
        GPIO.cleanup()

    else:
        print("Incorrect usonic() fn")

### Repeat function but returned value is a continuous function depending on the inverse of the distance.
### This returned value is assigned to the volume of the note played by the script

def reading2(sensor):

    TRIG = 10
    ECHO = 17
    import time
    import RPi.GPIO as GPIO
    value = 0
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    if sensor == 0:

        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)


        GPIO.output(TRIG, True)
        time.sleep(0.1)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            signaloff = time.time()

        while GPIO.input(ECHO) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff

        distance = (timepassed*343) /2

        value = int(round(10/distance))

        
        return value

    
    
        GPIO.cleanup()

    else:
        print("Incorrect usonic() fn")

### All loops to be used are defined as either arrays or lists

master = []
strMaster = ()

### Commence continual loop with interactive quit sequence if notes are played in correct order

while True:

### A sleep time is called as problems in running the code were noticed at quick repetitive
### intervals, this could be due to limitations on the RPi.

    time.sleep(0.5)

### Call the two defined functions to return the associated values for the two modules.
    
    j=reading1(0)
    k =reading2(0)

### Current selected note value is played with volume argument also included

    os.system('mpg321 -q -g {} Notes/{}.mp3 &'.format(k,j))

### Interactive quit requirement checks on each loop if condition is met, results in termination of script

    if ('1, 1, 1') in strMaster:
        quit()



  
    
