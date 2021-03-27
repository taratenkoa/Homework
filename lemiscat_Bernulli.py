from math import *
import tkinter

SCREEN_SIZE = 1900, 600
alpha = pi / 4
A = 200
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
    global r
    alpha = (alpha + pi / 120)
    if cos(2 * alpha) >= 0:
        r = A * 2 ** 0.5 * (cos(2 * alpha)) ** 0.5
        x0 = r * cos(alpha)
        y0 = r * sin(alpha)
        canvas.create_line(xys(x2, y2), xys(x0, y0), fill='black', width=1)
        x2 = x0
        y2 = y0
    if alpha <= 3 * pi:
        main.after(1, rotate)


rotate()
main.mainloop()