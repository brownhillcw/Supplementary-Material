"""
@author Benjamin Bowring
@author Craig Brownhill

@data: 11/2017

Script for calculating a series of 10 distance measurements using one of the HC-SR04
ultrasonic range finders. 

Before each series of measurements the user is prompted to specify a file to write to and
the true  distance to the reflecting object. 

The measurements are then written to a text file for further analysy and printed to the terminal window.
"""

### Import packages to be used throughout script

import time
import os


### Create a new text file in the folder "NewSensorData" and prompt the user
### to name the file.

file = open("NewSensorData/" + input('Name text file: ') + ".txt", "w")

### Define function with sensor argument that will be called to return current distance
### of reflective surface from module.

def reading(sensor):

### Define GPIO pins TRIG & ECHO are connected to such that they can be defined
### in GPIO setup
    
    TRIG = 24
    ECHO = 23
    import time
    import RPi.GPIO as GPIO
    value = 0
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

### Function then returns distance

        return distance

### Setup arrays to store the measurements which can later be saved to the text file 

master = []
strMaster = ('')
inputRead = []


### Prompt the user to specify the distane of the object before taking the
### measurements and write this to the text file. 

inputRead.append(input('Initial reflector distance: '))
file.write(str(inputRead[-1]) + '\n')


### Continuous while loop allows results to be measured repetitively until script is cancelled

### While loop commences by calling the defined 'reading' function and correct argument

### A nested if loop then checks if 10 readings have occured and returns values until this condition is satisfied

while True:
    
    j=reading(0)
    print(j)

    master.append(j)
    file.write(str(j) + ' \n')
    if len(master) % 10 == 0:
        inputRead.append(input('Distance of reflector: '))
        file.write('\n' + str(inputRead[-1]) + '\n')


  
    
