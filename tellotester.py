from djitellopy import Tello
import time

tello=Tello()
tello.connect()

for x in range (2):
    
    tello.takeoff()

    time.sleep(5)

    tello.land()
