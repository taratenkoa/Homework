import tkinter
import random


def draw(event):
    print(event.keysym)
    if event.keysym == 'Up':
        L = canvas.coords(krug)
        if (L[1] + L[3]) / 2 - 10 < 0:
            L[1] += SCREEN_SIZE[1]
            L[3] += SCREEN_SIZE[1]
        else:
            L[1] -= 10
            L[3] -= 10
        canvas.coords(krug, *L)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == 'Down':
        L = canvas.coords(krug)
        if (L[1] + L[3]) / 2 + 10 > SCREEN_SIZE[1]:
            L[1] -= SCREEN_SIZE[1]
            L[3] -= SCREEN_SIZE[1]
        else:
            L[1] += 10
            L[3] += 10
        canvas.coords(krug, *L)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == 'Left':
        L = canvas.coords(krug)
        if (L[0] + L[2]) / 2 - 10 < 0:
            L[0] += SCREEN_SIZE[0]
            L[2] += SCREEN_SIZE[0]
        else:
            L[0] -= 10
            L[2] -= 10
        canvas.coords(krug, *L)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == 'Right':
        L = canvas.coords(krug)
        if (L[0] + L[2]) / 2 + 10 > SCREEN_SIZE[0]:
            L[0] -= SCREEN_SIZE[0]
            L[2] -= SCREEN_SIZE[0]
        else:
            L[0] += 10
            L[2] += 10
        canvas.coords(krug, *L)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == '1':
        s[0] = '#FF0000'
        canvas.itemconfig(krug, fill='#FF0000')
        L = canvas.coords(krug)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == '2':
        s[0] = '#0000FF'
        canvas.itemconfig(krug, fill='#0000FF')
        L = canvas.coords(krug)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == '3':
        s[0] = '#00FF00'
        canvas.itemconfig(krug, fill='#00FF00')
        L = canvas.coords(krug)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == 'c':
        c = '#'
        for _ in range(6):
            c += str(hex(random.randint(0, 15))[2:])
        s[0] = c
        canvas.itemconfig(krug, fill=c)
        L = canvas.coords(krug)
        label.config(text=f"{(L[0] + L[2]) / 2 - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - (L[1] + L[3]) / 2}, {s[0]}")
    elif event.keysym == 'p':
        x = random.randint(50, SCREEN_SIZE[0] - 50)
        y = random.randint(50, SCREEN_SIZE[1] - 50)
        canvas.coords(krug, x - 50, y - 50, x + 50, y + 50)
        label.config(text=f"{x - SCREEN_SIZE[0] / 2}, {SCREEN_SIZE[1] / 2 - y}, {s[0]}")


SCREEN_SIZE = [800, 800]
main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=SCREEN_SIZE[0], width=SCREEN_SIZE[1])
canvas.pack()
s = ['#FF0000']
label = tkinter.Label(main, text=f"{0.0}, {0.0}, {s[0]}")
label.pack()
krug = canvas.create_oval((SCREEN_SIZE[0] / 2 - 50, SCREEN_SIZE[0] / 2 - 50), (SCREEN_SIZE[0] / 2 + 50, SCREEN_SIZE[0] / 2 + 50), fill='#FF0000', width=3, outline="black")
main.bind("<KeyPress>", draw)
main.mainloop()