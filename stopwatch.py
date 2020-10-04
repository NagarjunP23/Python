#program for stopwatch


import os
import time
 
 #initialize to zero
second,minute,hours = 0,0,0

while(True):
    print(hours, ":",minute,":",second)
    time.sleep(1)       #sleep for one second to count exactly 1 second
    second+=1
    if(second == 60):
        second = 0
        minute+=1
    if(minute == 60):
        minute = 0
        hours+=1
    os.system('cls')