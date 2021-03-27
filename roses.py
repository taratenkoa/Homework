from math import *
import tkinter

SCREEN_SIZE = 1900, 600
alpha = 0
A = 100
k = 3 / 7
x0 = 0
y0 = 0
x2 = 0
y2 = 0
i = 1
while (k * i) % 1 > 1 / 10 ** 12:
    i += 1
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
    alpha = alpha + pi / 120
    r = A * sin(k * alpha)
    x0 = r * cos(alpha)
    y0 = r * sin(alpha)
    canvas.create_line(xys(x2, y2), xys(x0, y0), fill='black', width=1)
    x2 = x0
    y2 = y0
    if alpha <= 2 * i * pi:
        main.after(10, rotate)
