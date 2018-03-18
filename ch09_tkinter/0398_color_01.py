from  tkinter import *

window = Tk()
button = Button(window, text="버튼을 클릭하세요")
button.pack()
button["fg"] = "#ff0000"
button["bg"] = "#00ff00"

window.mainloop()
