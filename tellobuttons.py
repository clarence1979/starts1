import tkinter
import tkinter.messagebox
from djitellopy import Tello

#tello = Tello('192.168.86.72',8889)
#If tello not connected to wifi, delete the IP and the port

#tello.connect() #Uncomment when ready to fly

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# creating a function called takeoff1()
def takeoff1():    
    tello.takeoff()
    tkinter.messagebox.Message(title="Takeoff",message="Takeoff")
def land1():    
    tello.land()
def left1():    
    tello.move_left(100) #values 20-500cm
def right1():    
    tello.move_right(100)
def takepic1():
    #Take picture
    tello.streamon()
    frame_read = tello.get_frame_read()
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




