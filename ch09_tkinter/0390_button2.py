from tkinter import *

counter = 0


def callback():
    global counter
    counter += 1
    button["text"] = "버튼이 %d 번 클릭되었음!" % counter


window = Tk()
button = Button(window, text="클릭", command=callback)
button.pack(side=LEFT)

window.mainloop()
