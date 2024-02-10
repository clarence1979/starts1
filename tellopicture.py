from djitellopy import Tello
import time

tello=Tello()
tello.connect()

#Take picture
tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

tello.land()
