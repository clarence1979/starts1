from djitellopy import Tello
import cv2
import time

tello = Tello()

tello.connect()
tello.takeoff()
print("Battery level is " + str(tello.get_battery())+"%")
print("Height is " + str(tello.get_height()) + "cm")

#print("Speed is " + str(tello.get_speed()))
tello.move_left(20)
tello.move_right(30)
time.sleep(2)
tello.streamon() #Take picture
frame_read=tello.get_frame_read() #Take picture
cv2.imwrite("picture.png", frame_read.frame) #Take picture
time.sleep(2)
tello.land()
print("Total flight time is: "+ str(tello.get_flight_time())+" seconds")
