import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry("720x480")
#mainWindow.resizable(0,0)
#mainWindow.attributes("-fullscreen", True)

#start top clock/info bar
clockTime = Label(mainWindow, text="10:21", font=("Verdana", 20)).grid(column=0, row=0)
weatherBrief = Label(mainWindow, text="partly cloudy", font=("Verdana", 20)).grid(column=6, row=0)

#start button section
clockbtn = PhotoImage(file="guiimages/clockbtn.png")
clockButton = Button(mainWindow, image=clockbtn).grid(column=0, row=1)
mapbtn = PhotoImage(file="guiimages/mapbtn.png")
mapButton = Button(mainWindow, image=mapbtn).grid(column=0, row=2)
weatherbtn = PhotoImage(file="guiimages/weatherbtn.png")
weatherButton = Button(mainWindow, image=weatherbtn).grid(column=0, row=3)
heartbtn = PhotoImage(file="guiimages/heartbtn.png")
heartButton = Button(mainWindow, image=heartbtn).grid(column=0, row=4)
blankbtn = PhotoImage(file="guiimages/blankbtn.png")
blankButton = Button(mainWindow, image=blankbtn).grid(column=0, row=5)


mainWindow.mainloop()
