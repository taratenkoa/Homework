from math import *
import tkinter

SCREEN_SIZE = 1900, 600
alpha = 0
A = 10
x0 = 0
y0 = 0
x2 = 0
y2 = 0
x1 = 0
y1 = 0
x3 = 0
y3 = 0
main = tkinter.Tk()
main.title("Rotating line")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.pack()


def rotate():
    global alpha
    global x2
    global y2
    global x3
    global y3
    alpha = alpha + pi / 30
    r = (A ** 2 * alpha) ** 0.5
    x0 = r * cos(alpha)
    y0 = r * sin(alpha)
    x1 = -r * cos(alpha)
    y1 = -r * sin(alpha)
    canvas.create_line(xys(x2, y2), xys(x0, y0), fill='black', width=1)
    canvas.create_line(xys(x3, y3), xys(x1, y1), fill='black', width=1)
    x2 = x0
    y2 = y0
    x3 = x1
    y3 = y1
    if alpha <= 10 * pi:
        main.after(20, rotate)


rotate()
main.mainloop()