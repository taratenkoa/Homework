from math import *
import tkinter

SCREEN_SIZE = 1900, 600
alpha = 0
A = 100
x0 = 0
y0 = 0
x2 = 0
y2 = 0
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
    alpha = alpha + pi / 30
    r = 2 * A * (1 - cos(alpha))
    x0 = r * cos(alpha)
    y0 = r * sin(alpha)
    canvas.create_line(xys(x2, y2), xys(x0, y0), fill='black', width=1)
    x2 = x0
    y2 = y0
    if alpha <= 2 * pi:
        main.after(20, rotate)


rotate()
main.mainloop()
