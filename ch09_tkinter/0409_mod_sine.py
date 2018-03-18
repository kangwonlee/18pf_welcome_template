import math
from tkinter import *

window = Tk()

angle_deg_range = range(0, 360 + 1)
angle_deg_list = list(angle_deg_range)

height = 200

a = height / 2
offset = height / 2 + 2

y = [a * math.sin(math.radians(angle_deg)) for angle_deg in angle_deg_range]

w = Canvas(window, width=max(angle_deg_list), height=height + 1)
w.pack()

x0 = angle_deg_list[0]
y0 = y[0]
for i in angle_deg_range[1:]:
    x1 = angle_deg_list[i]
    y1 = y[i]
    w.create_line(x0, offset - y0, x1, offset - y1)
    x0, y0 = x1, y1

mainloop()
