from math import *
import tkinter

SCREEN_SIZE = 600, 600
alpha = 0
LENGTH = 100
n = 9
main = tkinter.Tk()
main.title("Rotating line")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


MN_coords = []
for i in range(n):
    MN_coords += xys(LENGTH * cos(2 * pi * i / n), LENGTH * sin(2 * pi * i / n))
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
MN = canvas.create_polygon(*MN_coords, fill='', outline='green')
canvas.pack()


def rotate():
    global alpha
    canvas.coords(MN, *MN_coords)
    alpha = (alpha + 1) % 360
    u = alpha
    MN_coords[:] = []
    for i in range(n):
        xa = LENGTH * cos((u + i * (360 / n)) * pi / 180)
        ya = LENGTH * sin((u + i * (360 / n)) * pi / 180)
        MN_coords[:] += xys(xa, ya)
    main.after(10, rotate)


rotate()
main.mainloop()