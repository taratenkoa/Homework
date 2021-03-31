import tkinter
import math


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


def sat(rad_planet, ras_do_sput, rec, xc, yc):
    graph_pos[0] = xc
    graph_pos[1] = yc
    if rec == 0:
        for i in range(kol_vo_ver + 1):
            x = xc + rad_planet * math.cos(2 * math.pi * i / kol_vo_ver)
            y = yc + rad_planet * math.sin(2 * math.pi * i / kol_vo_ver)
            if graph_pos[0] != xc or graph_pos[1] != yc:
                canvas.create_line(xys(*graph_pos[:2]), xys(x,y))
            graph_pos[0] = x
            graph_pos[1] = y
    else:
        for j in range(kol_vo_sput + 1):
            x1 = xc + ras_do_sput * math.cos(2 * math.pi * j / kol_vo_sput)
            y1 = yc + ras_do_sput * math.sin(2 * math.pi * j / kol_vo_sput)
            sat(rad_planet * koef, ras_do_sput * koef, rec - 1, x1, y1)

        graph_pos[0] = xc
        graph_pos[1] = yc
        for i in range(kol_vo_ver + 1):
            x = xc + rad_planet * math.cos(2 * math.pi * i / kol_vo_ver)
            y = yc + rad_planet * math.sin(2 * math.pi * i / kol_vo_ver)
            if (graph_pos[0] != xc or graph_pos[1] != yc):
                canvas.create_line(xys(*graph_pos[:2]), xys(x, y))
            graph_pos[0] = x
            graph_pos[1] = y


def ocr(rad_planet, ras_do_sput, rec, xc, yc):
    if rec == 0:
        canvas. create_oval(xys(xc - rad_planet, yc - rad_planet), xys(xc + rad_planet, yc + rad_planet) )
    else:
        for j in range(kol_vo_sput + 1):
            x1 = xc + ras_do_sput * math.cos(2 * math.pi * j / kol_vo_sput)
            y1 = yc + ras_do_sput * math.sin(2 * math.pi * j / kol_vo_sput)
            ocr(rad_planet * koef, ras_do_sput * koef, rec - 1, x1, y1)
        graph_pos[0] = xc
        graph_pos[1] = yc
        canvas.create_oval(xys(xc - rad_planet, yc - rad_planet), xys(xc + rad_planet, yc + rad_planet))





SCREEN_SIZE = 1900, 600
graph_pos = [0, 0, 0]
kol_vo_ver = int(input())
kol_vo_sput = int(input())
rad_planet = int(input())
ras_do_sput = int(input())
koef = float(input())
rec = int(input())
main = tkinter.Tk()
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
if kol_vo_ver == 0:
    ocr(rad_planet, ras_do_sput, rec, 0, 0)
else:
    sat(rad_planet, ras_do_sput, rec, 0, 0)
canvas.pack()
main.mainloop()
