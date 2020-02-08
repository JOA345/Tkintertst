#!/usr/bin/end python3
from tkinter import *

blank_window = Tk()
topFrame = Frame(blank_window)
topFrame.pack()
bottomFrame = Frame(blank_window)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="purple")
button4 = Button(bottomFrame, text="Button 4", fg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

blank_window.mainloop()


