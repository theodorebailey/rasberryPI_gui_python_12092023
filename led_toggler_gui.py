# import 
import tkinter as tk
from tkinter import font
from gpiozero import LED
import RPi.GPIO as GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# hardware
led = LED(14)

# create our GUI = GRAPHICAL USER INTERFACE

# create tk interface to build gui in
win = tk.Tk()
win.title("LED Toggler")

# build font properties
myFont = font.Font(family = "Helvetica", size = 12, weight = "bold")

## EVENT FUNCTIONS
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"] = "Turn LED on"
    else:
        led.on()
        ledButton["text"] = "Turn LED off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()


### WIDGETS - two buttons
# where to go, where to place it, event function placed in constructor BUTTON function
ledButton = Button(win, text = "Turn LED On", font = myFont, command = ledToggle, bg = "bisque2", height = 1, width = 24)

ledButton.grid(row=0, column=1)

# change: text, colour, size
exitButton = Button(win, text = "exit", font = myFont, command = close, bg = "blue", height = 1, width = 6)

# suffix protocol of object
win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

# as project gets bigger we require this
# main loop will loop forever
win.mainloop()


