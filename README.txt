
@author: Benjamin Bowring
@author: Craig Brownhill
        
@date: 11/2017

No initial arguments are required when running any of the scripts.

------------------------------------------------------------------------------

@file: DistanceRead.py

When running the DistanceRead script a file name must be specified in the
terminal. This file will be save to a folder which should be specified in line
19 of the code. 

The terminal will then ask for the 'Initial reflector distance: ' which should
measured by the user using a metre stick. After taking calculating 10 distance
measurements the terminal will prompt the user 'Distance of reflector:' which
when entered will take a new series of 10 measurements. This process repeats
indefintely, allowing the user to take as many data series as desired. The
script must be exited manually.

The text file output from DistanceRead has the format:

<Initial Distance>
<Measurement 1>
<Measurement 2>
 .
 .
 .
<Measurement 10>

<New Distance>
<Measurement 1>
<Measurement 2>
 .
 .
 .
<Measurement 10>
.
.
.

------------------------------------------------------------------------------

Music will start playing when running both therodigit and LOOPPEDAL. 

@file: Therodigit.py

When running the thero script the pitch of the note can be changed by moving an
object in front of sensor two. The volume can be changed by moving an object
in front of sensor 1. The rate at which notes are played can be adjusted by
changing the duration of the sleep statement on line 216 of the code.

@file: LOOPPEDAL.py

When running the LOOPPEDAL script sensor 2 again controls the pitch of note
played. Sensor one controls the loop pedal. To record a sequence of notes
place your hand within 30cm of the sensor. When you have finished recording
simply remove your hand and the recorded sequence will play from the
beginning. Additional notes to create harmonies can still be played with
sensor 1 while the loop is running. The recorded loop will repeat once it
reaches the end. To record a new loop simply place your hand in front of
sensor 1 as before. If you wish to exit the programme at any point simply
play the note closest to sensor 2 three times in a row. 

------------------------------------------------------------------------------

Data analysis was performed with files requiring terminal prompting to 
specify storage location.

@file:

@file:

@file:

@file:
 


