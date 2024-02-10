import tkinter
import tkinter.messagebox
from djitellopy import Tello
import cv2
import time

tello = Tello()

tello.connect()

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# creating a function called takeoff1()
def takeoff1():    
    tello.takeoff()
    tkinter.messagebox.Message(title="Takeoff",message="Takeoff")
    print("Battery level is " + str(tello.get_battery())+"%")
    print("Height is " + str(tello.get_height()) + "cm")
    #print("Speed is " + str(tello.get_speed()))
def land1():    
    tello.land()
    print("Total flight time is: "+ str(tello.get_flight_time())+" seconds")
def left1():    
    tello.move_left(20)
def right1():    
    tello.move_right(20)
def takepic1():
    tello.streamon()
    frame_read=tello.get_frame_read()
    cv2.imwrite("picture.png", frame_read.frame)

tkinter.Label(window, text = "Tello Controls").pack()
tkinter.Button(window, text = "Takeoff", command = takeoff1).pack()
tkinter.Button(window, text = "Land!", command = land1).pack()
tkinter.Button(window, text = "Left", command = left1).pack()
tkinter.Button(window, text = "Right", command = right1).pack()
tkinter.Button(window, text = "Take Pic", command = takepic1).pack()

window.geometry('200x200+150+150')
window.minsize(150,150)
window.mainloop()
