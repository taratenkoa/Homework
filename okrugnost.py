import tkinter
import random
n = int(input())
L = [[random.randint(200, 800), random.randint(200, 800)] for i in range(n)]
Ru = 10 ** 100
x0u = 0
y0u = 0
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        for k in range(j + 1, len(L)):
            s = 0
            x1, y1, x2, y2, x3, y3 = L[i][0], L[i][1], L[j][0], L[j][1], L[k][0], L[k][1]
            x0 = -(1 / 2) * (y1 * (x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2) + y2 * (-x1 ** 2 + x3 ** 2 - y1 ** 2 + y3 ** 2) + y3 * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2)) / (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            y0 = (1 / 2) * (x1 * (x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2) + x2 * (
                        -x1 ** 2 + x3 ** 2 - y1 ** 2 + y3 ** 2) + x3 * (x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2)) / (
                             x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

            R = float(str(((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5)[:12])
            for h in range(len(L)):
                a = float(str(((x0 - L[h][0]) ** 2 + (y0 - L[h][1]) ** 2) ** 0.5)[:12])
                if a > R:
                    s += 1
            if s == 0 and Ru > R:
                Ru = R
                x0u = x0
                y0u = y0
main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=1000, width=1000)
for i in L:
    canvas.create_oval((i[0] - 3, i[1] - 3), (i[0] + 3, i[1] + 3), fill='black', width=1)
canvas.create_oval((x0u - Ru, y0u + Ru), (x0u + Ru, y0u - Ru))
canvas.pack()
main.mainloop()