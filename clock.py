import math
import tkinter
import time

SCREEN_SIZE = 600, 600
alpha1 = 0
alpha2 = 0
alpha3 = 0
alpha4 = -60
LENGTH1 = 140
LENGTH2 = 120
LENGTH3 = 90
LENGTH4 = 140
main = tkinter.Tk()
main.title("Clock")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
line1_coords = [*xys(0, LENGTH1), *xys(0, 0)]
line1 = canvas.create_line(*line1_coords, width=3, fill='#9d0191')
line2_coords = [*xys(0, LENGTH2), *xys(0, 0)]
line2 = canvas.create_line(*line2_coords, width=5, fill='#fd3a69')
line3_coords = [*xys(0, LENGTH3), *xys(0, 0)]
line3 = canvas.create_line(*line3_coords, width=7, fill='#fecd1a')
circle_coords = [*xys(-150, 150), *xys(150, -150)]
canvas.create_oval(*circle_coords, width=3, outline="#120078")
canvas.pack()
label = tkinter.Label(font=("Helvetica", 28), fg="#120078")
label.pack()
i = 0
while i != 12:
    alpha4 = (alpha4 - 30)
    xa = LENGTH4 * math.cos(alpha4 * math.pi / 180)
    ya = LENGTH4 * math.sin(alpha4 * math.pi / 180)
    xa, ya = xys(-xa, -ya)
    l = canvas.create_text(xa, ya, text=str(i))
    i += 1


def rotate1():
    global alpha1
    canvas.coords(line1, *line1_coords)
    alpha1 = -(time.time() % 60) * 6 - 90
    xa = LENGTH1 * math.cos(alpha1 * math.pi / 180)
    ya = LENGTH1 * math.sin(alpha1 * math.pi / 180)
    line1_coords[:] = xys(-xa, -ya) + xys(0, 0)
    main.after(10, rotate1)


def rotate2():
    global alpha2
    canvas.coords(line2, *line2_coords)
    alpha2 = -(time.time() % 3600 / 10) - 90
    xa = LENGTH2 * math.cos(alpha2 * math.pi / 180)
    ya = LENGTH2 * math.sin(alpha2 * math.pi / 180)
    line2_coords[:] = xys(-xa, -ya) + xys(0, 0)
    main.after(10, rotate2)


def rotate3():
    global alpha3
    canvas.coords(line3, *line3_coords)
    alpha3 = -(time.time() % 43200 / 120) - 180
    xa = LENGTH3 * math.cos(alpha3 * math.pi / 180)
    ya = LENGTH3 * math.sin(alpha3 * math.pi / 180)
    line3_coords[:] = xys(-xa, -ya) + xys(0, 0)
    main.after(10, rotate3)


def update_clock():
    now = time.strftime("%H:%M:%S")
    label.configure(text=now)
    main.after(1000, update_clock)


update_clock()
rotate1()
rotate2()
rotate3()
main.mainloop()