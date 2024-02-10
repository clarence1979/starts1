from djitellopy import Tello
import time
import cv2

tello=Tello() # or tello = Tello('192.168.86.72',8889) 
tello.connect()

time.sleep(5) #pauses for 5 seconds
tello.takeoff()
tello.move_forward(20) #moves forward for 20cm
tello.move_right(20)
tello.move_up(20) #accepts values 20-500cm

for x in range (3):       #does it 3 times
    tello.flip("f")  
tello.stop
time.sleep(5)
tello.move_backward(20)
tello.move_left(20)
tello.move_down(20) #accepts values 20-500cm
tello.land()
