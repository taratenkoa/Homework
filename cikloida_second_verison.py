import math
import tkinter


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


def spirograph():
    global angle_1
    global d
    global graph_pos
    global a
    global pol
    y0 = 80
    x0 = -SCREEN_SIZE[0] // 2
    x0 = x0 + r * angle_1
    x = x0 + d * math.cos(angle_1)
    y = y0 + d * math.sin(angle_1)
    canvas.move(pol, r * 0.1, 0)
    if a == 0:
        a = 1
    else:
        graph_pos[0].create_line(xys(graph_pos[1], graph_pos[2]), xys(x, y))
    graph_pos[1] = x
    graph_pos[2] = y
    angle_1 += 0.1
    main.after(10, spirograph)


SCREEN_SIZE = (800, 600)

main = tkinter.Tk()
main.title('mnn')
canvas = tkinter.Canvas(main, bg='white', width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
canvas.create_line(0, SCREEN_SIZE[1] // 2, SCREEN_SIZE[0], SCREEN_SIZE[1] // 2)
canvas.pack()
pol = canvas.create_oval(-80, 140, 80, 300)
r = 80
r2 = 45
d = 80
angle_1 = 0
a = 0
graph_pos = [canvas, 0, 0]
spirograph()
main.mainloop()