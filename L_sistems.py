import math
import tkinter


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


def preobr(h, k):
    for i in range(k):
        a = h
        m = len(a) // 2
        h += "1"
        h += a[:m]
        if a[m] == "1":
            h += "0"
        else:
            h += "1"
        h += a[m + 1:]
    return h


def paint():
    global angle_1
    global x2
    global y2
    global a2
    global b2
    x = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180)
    y = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180)
    a2 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * 0.8
    b2 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * 0.8
    x2 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * koef_1
    y2 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * koef_1
    graph_pos[0].create_line(xys(*graph_pos[1:3]), xys(x2, y2))
    graph_pos[1] = x
    graph_pos[2] = y
    for elem in h:
        if elem == "1":
            graph_pos[3] += 90
        if elem == "0":
            graph_pos[3] -= 90
        a1 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * 0.2
        b1 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * 0.2
        if elem == "1":
            canvas.create_arc(xys(a2, b2), xys(a1, b1), style=tkinter.ARC, start=graph_pos[3] + 180)
        if elem == "0":
            canvas.create_arc(xys(a2, b2), xys(a1, b1), style=tkinter.ARC, start=graph_pos[3] + 90)
        a2 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * 0.8
        b2 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * 0.8
        x1 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * koef_2
        y1 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * koef_2
        x2 = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180) * koef_1
        y2 = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180) * koef_1
        x = graph_pos[1] + a * math.cos(graph_pos[3] * math.pi / 180)
        y = graph_pos[2] + a * math.sin(graph_pos[3] * math.pi / 180)
        graph_pos[0].create_line(xys(x2, y2), xys(x1, y1))
        graph_pos[1] = x
        graph_pos[2] = y
        All_x.append(x)
        All_y.append(y)


SCREEN_SIZE = (1000, 800)
main = tkinter.Tk()
main.title('mnn')
canvas = tkinter.Canvas(main, bg='white', width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
canvas.pack()
a = 1
koef_1 = 0.9
koef_2 = 0.1
All_x = list()
All_y = list()
graph_pos = [canvas, 0, 0, 0]
h = preobr("1", int(input()))
paint()
koef = min(SCREEN_SIZE[1]//(max(All_y)-min(All_y)), SCREEN_SIZE[0]//(max(All_x)-min(All_x)))
canvas.delete("all")
x = SCREEN_SIZE[0]//2-2 - max(All_x) * koef
y = SCREEN_SIZE[1]//2-2 - max(All_y) * koef
graph_pos = [canvas, x, y, 0]
a = koef
paint()
main.mainloop()