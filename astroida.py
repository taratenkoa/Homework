from math import *
import tkinter

SCREEN_SIZE = 1900, 600
t = 0
A = 100
x0 = A
y0 = 0
x2 = A
y2 = 0
main = tkinter.Tk()
main.title("Rotating line")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.pack()


def rotate():
    global t
    global x2
    global y2
    t = t + pi / 30
    x0 = A * cos(t) ** 3
    y0 = A * sin(t) ** 3
    canvas.create_line(xys(x2, y2), xys(x0, y0), fill='black', width=1)
    x2 = x0
    y2 = y0
    if t <= 2 * pi:
        main.after(20, rotate)


rotate()
main.mainloop()