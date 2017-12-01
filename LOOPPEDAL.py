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
            
        else:
            value = 9
            

        

        return value

    
    
        GPIO.cleanup()

    else:
        print("Incorrect usonic() fn")

### Repeat function but have only one value that segregates dependent on if surface is within
### preset distance.

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
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            signaloff = time.time()

        while GPIO.input(ECHO) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff

        distance = (timepassed*343) /2



        if 0 < distance < 0.3:
            value = 1
            
        else:
            value = 0
            

        return value

    
    
        GPIO.cleanup()

    else:
        print("Incorrect usonic() fn")

### For functionality as a loop pedal we must define a sequence of notes when prompted that is
### repeated on command.

### We do this by defining a master string that is reset and appended with notes when a loop
### is desired.

### For usage in terminal commands we also define a strMaster that can be searched as a list.



### All loops to be used are defined as either arrays or lists

master = []
loop = [0]
strMaster = ()

### The kArray defines whether the pedal is 'initiated'. When the loop is on, the value returned
### from the associated module is 'True' or 1. When the pedal is off, the notes
### repeat in the sequence they were initially recorded.

kArray = []
jArray = []

### Throughout the code we are looking for certain conditions to be met, these conditions are
### defined before commencement.

### kick corresponds to the end of recording a loop

### mastKick corresponds to an interactive quitting of the whole session following three notes
### being played in sequence

kick = [1,0]
mastKick = [1,1,1]

### i is the position in the recorded loop, it is defined as zero initially and will be stepped
### over when repeating the loop.

i=0


while True:

### Call the two defined functions to return the associated values for the two modules.

### A sleep time is called as problems in running the code were noticed at quick repetitive
### intervals, this could be due to limitations on the RPi.
 
    time.sleep(1.5)
    
    j=reading1(0)

    k =reading2(0)


### The current integer value corresponding to a note is appended to the module's associated array.

    jArray.append(j)

### The array is checked for the interactive sequence of notes required for quiting of function
### if met the code will quit

    if (jArray[-3:]) == mastKick:
        quit()

### If the interactive quit requirement is not met, the current status of the loop pedal is checked
### and appended to the module's array

    kArray.append(k)

### If the loop pedal is 'initiated' the current note is appeneded to the master array and
### played

    if kArray[-1] == 1:

        os.system('mpg321 -q Notes/{}.mp3 &'.format(str(j)))
        print('mpg321 -q Notes/{}.mp3 &'.format(str(j)))
        master.append(j)
        print('New Note: ' + str(j))
        print(master)

### If the loop pedal has just been released, the repeated loop is defined as the current sequence
### of notes in the master array and the first note is played. The master array is then deleted
### so it can be reinitiated when a new loop is defined.

    elif (kArray[-2:]) == kick:
        i=0
        loop = master[:]
        del master[:]
        
        os.system('mpg321 -q Notes/{}.mp3 &'.format(str(loop[i])))
        print('Final loop: ' + str(loop))
        print('First Note: ' + str(loop[i]))
        i+=1

### If the loop pedal remains released the next note is continually stepped over. This is done
### by incrementing the value of i, our position in the repeated loop.

### The functionality to play over the loop is included, however if the note is at maximum,
### corresponding to no input, a note is not played.

    else:

### If the code has reached the end of the recorded loop, we pass to the except and start the loop
### again with the same functionality.
        
        try:
            print(loop[i])
            os.system('mpg321 -q Notes/{}.mp3 &'.format(str(loop[i])))
            if j == 9:
                pass
            else:
                os.system('mpg321 -q Notes/{}.mp3 &'.format(str(j)))


        except:
            i=0
            print(loop[i])
            os.system('mpg321 -q Notes/{}.mp3 &'.format(str(loop[i])))
            if j == 9:
                pass
            else:
                os.system('mpg321 -q Notes/{}.mp3 &'.format(str(j)))

        i+=1
