import math
import tkinter

SCREEN_SIZE = 1900, 600
alpha = -90
r = 50
d = 70
x0 = SCREEN_SIZE[0] / 2 * -1
y0 = r
s = 1
main = tkinter.Tk()
main.title("Rotating line")


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


point_coords = [*xys(x0 - s, y0 - r - s), *xys(x0 + s, y0 - r + s)]
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
point = canvas.create_oval(*point_coords, fill='black', width=1)
canvas.create_line(0, SCREEN_SIZE[1] // 2, SCREEN_SIZE[0], SCREEN_SIZE[1] // 2, fill='black', width=1)
krug_coords = [*xys(x0 - r, y0 + r), *xys(x0 + r, y0 - r)]
krug = canvas.create_oval(*krug_coords)
canvas.pack()


def rotate():
    global alpha
    global x0
    canvas.create_oval(*point_coords, fill='black', width=1)
    alpha = (alpha - 1) % 360
    canvas.coords(krug, *krug_coords)
    krug_coords[:] = xys(x0 - r, y0 + r) + xys(x0 + r, y0 - r)
    x0 = x0 + 1
    xa = x0 + d * math.cos(alpha * math.pi / 180)
    ya = y0 + d * math.sin(alpha * math.pi / 180)
    point_coords[:] = xys(xa - s, ya - s) + xys(xa + s, ya + s)
    main.after(10, rotate)


rotate()
main.mainloop()