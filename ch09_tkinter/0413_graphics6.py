from tkinter import *
import tkinter.colorchooser as cc

window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()
color = cc.askcolor()

w.create_rectangle(50, 25, 200, 100, fill=color[1])
window.mainloop()
