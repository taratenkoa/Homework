import tkinter
import math
main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=600, width=600)
canvas.pack()
r = 100
A = set()
n = int(input('Количество лучей:'))
k = 1
A.add(1)
while True:
    if n % 2 == 0:
        k1 = (k + n / 2 - 1) % n
    else:
        k1 = (k + (n - 1) / 2) % n
    x = (200 + r * math.cos(2 * 3.14 * k / n), 200 + r * math.sin(2 * 3.14 * k / n))
    y = (200 + r * math.cos(2 * 3.14 * k1 / n), 200 + r * math.sin(2 * 3.14 * k1 / n))
    canvas.create_line(x, y, fill='red')
    k = k1
    A.add(k)
    if k == 1:
        break
if len(A) == n:
    main.mainloop()
else:
    print("Такую звезду нарисовать нельзя")