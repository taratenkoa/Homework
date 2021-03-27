import tkinter

SCREEN_SIZE = [1600, 800]
main = tkinter.Tk()
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.pack()
krug = canvas.create_oval((SCREEN_SIZE[0] / 2 - 50, SCREEN_SIZE[1] / 2 - 50), (SCREEN_SIZE[0] / 2 + 50, SCREEN_SIZE[1] / 2 + 50), fill='green', width=3, outline="black")
vx = 1
vy = 1


def rotate():
    global vx
    global vy
    L = canvas.coords(krug)
    if L[3] + vy > SCREEN_SIZE[1] or L[1] + vy < 0:
        vy *= -1
    if L[2] + vx > SCREEN_SIZE[0] or L[0] + vx < 0:
        vx *= -1
    canvas.move(krug, vx, vy)
    main.after(5, rotate)


rotate()
main.mainloop()