#import the Raspberry pinout library and time
from EmulatorGUI import GPIO
#import rpi.GPIO as GPIO
import threading
import tkinter

#won't have to write timeit.Timer every time
from threading import Timer

#clean all pinout settings
GPIO.cleanup()
 
#Mode of pinout numbering, BOARD or BCM available
GPIO.setmode(GPIO.BCM)
 
#List of output channels for airpumps set as output 0V
output_list = (5, 6, 12, 13, 19, 16, 26, 20, 21)

#NOTICE!!! Initial set to HIGH instead of LOW. Apparently the logic is somewhat inverted, and using initial LOW will enable
#out signal instead of disable it, making the relays close it's circuits instead of leaving them open.

GPIO.setup(5, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(6, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(19, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(26, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(20, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(21, GPIO.OUT, initial = GPIO.HIGH)

#General times for booze and soda

sodatime = 8.0
boozetime = 2.0


#Naming the outputs for simpler mixing

soda_1 = 5
soda_2 = 6
soda_3 = 12
soda_4 = 13
liquor_1 = 19
liquor_2 = 16
liquor_3 = 26
liquor_4 = 20
liquor_5 = 21

#tkinter gui 
from tkinter import *


#Timer for drink 1

def makeGrogg1():
    GPIO.output(soda_1, False)
    GPIO.output(liquor_1, False)
    sprit = Timer(1.9, turnOffBooze1)
    virke = Timer(8.5, turnOffSoda1)
    sprit.start()
    virke.start()
def turnOffBooze1():
    GPIO.output(liquor_1, True)
def turnOffSoda1():
    GPIO.output(soda_1, True)

#Timer for drink 2

def makeGrogg2():
    GPIO.output(soda_2, False)
    GPIO.output(liquor_2, False)
    sprit = Timer(1.9, turnOffBooze2)
    virke = Timer(8.5, turnOffSoda2)
    sprit.start()
    virke.start()
def turnOffBooze2():
    GPIO.output(liquor_2, True)
def turnOffSoda2():
    GPIO.output(soda_2, True)

#Timer for drink 3, booze only

def makeGrogg3():

    GPIO.output(liquor_3, False)
    sprit = Timer(1.9, turnOffBooze3)

    sprit.start()

def turnOffBooze3():
    GPIO.output(liquor_3, True)
def turnOffSoda3():

#Timer for drink 4, booze only

def makeGrogg4():
    GPIO.output(liquor_4, False)

    sprit = Timer(1.9, turnOffBooze4)

    sprit.start()
    virke.start()
def turnOffBooze4():
    GPIO.output(liquor_4, True)




mainframe = Tk()


mainframe.attributes("-fullscreen", True)
mainframe.title('Drink 5000')

labelheader = Label(mainframe, text = 'Skål')
labelheader.grid(row=0, column=1)
button1 = Button(mainframe, text = 'Rom o Cola', command = makeGrogg1, height = 8, width = 20)
button1.grid(row=1, column=0)
button2 = Button(mainframe, text = 'Gin o Tonic', command = makeGrogg2, height = 8, width = 20)
button2.grid(row=1, column=2)
button3 = Button(mainframe, text = 'Whiskey', command = makeGrogg3, height = 8, width = 20)
button3.grid(row=2, column=0)
button4 = Button(mainframe, text = 'Cognac', command = makeGrogg4, height = 8, width = 20)
button4.grid(row=2, column=2)
 
 
mainframe.mainloop()
