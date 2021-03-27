import math
import tkinter

with open('mist.dat', "rt", encoding="utf-8") as file:
    L = [list(map(int, x.split())) for x in file.readlines()]

SCREEN_SIZE = 1900, 1000
angles = []
circle = []
for k in range(1, len(L)):
    angles += [[L[k][3]]]
    circle += [[L[k][0], L[k][1], L[k][2]]]

i = L[0][0]
j = 0
C = []
while j < i:
    if int(255 / i * j) > 15:
        C += ['#' + hex(int(255 / i * j))[2:] * 3]
    else:
        C += ['#' + ('0' + hex(int(255 / i * j))[2:]) * 3]
    j += 1

main = tkinter.Tk()
main.title("Windows")
S = []


def xys(x, y):
    return SCREEN_SIZE[0] // 2 + x, SCREEN_SIZE[1] // 2 - y


line_coords = []
for k in range(len(circle)):
    line_coords += [[*xys(circle[k][0] + circle[k][2] * math.cos(angles[k][0] * math.pi / 180),
                          circle[k][1] + circle[k][2] * math.sin(angles[k][0] * math.pi / 180)), *xys(
        circle[(k + 1) % len(circle)][0] + circle[(k + 1) % len(circle)][2] * math.cos(
            angles[(k + 1) % len(circle)][0] * math.pi / 180),
        circle[(k + 1) % len(circle)][1] + circle[(k + 1) % len(circle)][2] * math.sin(
            angles[(k + 1) % len(circle)][0] * math.pi / 180))]]
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
for k in range(len(line_coords)):
    S += [[canvas.create_line(*line_coords[k], width=3)]]
canvas.pack()


def rotate():
    global S
    global i
    global C
    for k in range(len(angles)):
        angles[k][0] = (angles[k][0] + L[k + 1][4]) % 360
    for k in range(len(S)):
        S[k] += [canvas.create_line([[*xys(circle[k][0] + circle[k][2] * math.cos(angles[k][0] * math.pi / 180),
                                           circle[k][1] + circle[k][2] * math.sin(angles[k][0] * math.pi / 180)), *xys(
            circle[(k + 1) % len(circle)][0] + circle[(k + 1) % len(circle)][2] * math.cos(
                angles[(k + 1) % len(circle)][0] * math.pi / 180),
            circle[(k + 1) % len(circle)][1] + circle[(k + 1) % len(circle)][2] * math.sin(
                angles[(k + 1) % len(circle)][0] * math.pi / 180))]], width=3)]
    for k in range(len(S)):
        if len(S[k]) > i:
            canvas.delete(S[k][0])
            S[k].pop(0)
        h = 0
        while h < len(S[k]):
            canvas.itemconfig(S[k][len(S[k]) - h - 1], fill=C[h])
            h += 1
    main.after(40, rotate)


rotate()
main.mainloop()
