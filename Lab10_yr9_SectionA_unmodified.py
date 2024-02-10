from djitellopy import Tello #Library to enable Tello to run
import cv2 #Library for taking photos and image recognition

#STUDENT TO WRITE ALL COMMENTS USING THE HASH NOTATION FOR THE REST OF THE CODE BELOW AND SUBMIT VIA SEQTA
#CODE NEEDS TO BE TESTED ON A DRONE. RECORD VIDEO OF SUCCESSFUL TESTING AND UPLOAD TO SEQTA.

import time

tello = Tello()
tello.connect()


time.sleep(2)
x=int(input("Enter the number of flips:\n"))
print("You have entered "+x+" number of flips")

for y in range (x):
       tello.flip(“f”)
