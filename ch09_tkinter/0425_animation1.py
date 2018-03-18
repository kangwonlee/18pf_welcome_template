from tkinter import *

window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill="green")


def move_right(event):
    canvas.move(id, 5, 0)


def move_left(event):
    canvas.move(id, -5, 0)


def move_up(event):
    canvas.move(id, 0, -5)


def move_down(event):
    canvas.move(id, 0, 5)


canvas.bind_all('<KeyPress-Right>', move_right)
canvas.bind_all('<KeyPress-Left>', move_left)
canvas.bind_all('<KeyPress-Up>', move_up)
canvas.bind_all('<KeyPress-Down>', move_down)

while True:
    window.update()
