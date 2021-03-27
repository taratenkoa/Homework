import math
import tkinter

SCREEN_SIZE = 1900, 600
alpha = 0
r = 50
d = 60
s = 1
R = 160
i = 1
while ((R - r) / r * i) % 1 > 1 / 10 ** 12:
    i += 1
x0 = 0
y0 = r - R
x2 = R - r + d
y2 = 0
main = tkinter.Tk()
main.title("Rotating line")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.create_oval(xys(R, R), xys(-R, -R), fill='', width=1)
krug_coords = [*xys(x0 - r, y0 + r), *xys(x0 + r, y0 - r)]
krug = canvas.create_oval(*krug_coords, fill='', width=1)
line_coords = [*xys(x0, y0), *xys(x0, y0 - d)]
line = canvas.create_line(*line_coords, fill='black', width=1)
canvas.pack()


def rotate():
    global alpha
    global x0
    global y0
    global x2
    global y2
    global krug
    canvas.coords(krug, *krug_coords)
    canvas.coords(line, *line_coords)
    alpha = alpha + math.pi / 30
    x0 = (R - r) * math.cos(alpha)
    y0 = (R - r) * math.sin(-alpha)
    krug_coords[:] = xys(x0 - r, y0 + r) + xys(x0 + r, y0 - r)
    xa = x0 + d * math.cos(alpha * R / r - alpha)
    ya = y0 + d * math.sin(alpha * R / r - alpha)
    canvas.create_line(xys(x2, y2), xys(xa, ya), fill='black', width=1)
    x2 = xa
    y2 = ya
    line_coords[:] = xys(x0, y0) + xys(xa, ya)
    if alpha <= 2 * math.pi * i:
        main.after(20, rotate)
    else:
        canvas.delete(krug)
        canvas.delete(line)


rotate()
main.mainloop()