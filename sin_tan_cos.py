import tkinter
import math


def move_to(x, y):
    graph_pos[1:] = x, y


def line_to(x, y, width=1, color='black'):
    graph_pos[0].create_line(graph_pos[1:], (x, y), width=width, fill=color)
    graph_pos[1:] = x, y


def xs(x):
    return SCREEN_SIZE[0] // 2 + x


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


def draw(event):
    if event.keycode == 83:
        canvas.delete("all")
        label.config(text="Синус")
        canvas.create_line((SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]))
        canvas.create_line((0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2))
        x = -SCREEN_SIZE[0] // 2
        k = 2 * math.pi / SCREEN_SIZE[0]
        move_to(xs(x), ys(50 * math.sin(x * k)))
        for x in range(-SCREEN_SIZE[0] // 2 - 1, SCREEN_SIZE[1] // 2 + 1):
            line_to(xs(x), ys(100 * math.sin(x * k)), color='blue', width=3)
    if event.keycode == 67:
        canvas.delete("all")
        label.config(text="Косинус")
        canvas.create_line((SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]))
        canvas.create_line((0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2))
        x = -SCREEN_SIZE[0] // 2
        k = 2 * math.pi / SCREEN_SIZE[0]
        move_to(xs(x), ys(50 * math.cos(x * k)))
        for x in range(-SCREEN_SIZE[0] // 2 - 1, SCREEN_SIZE[1] // 2 + 1):
            line_to(xs(x), ys(100 * math.cos(x * k)), color='blue', width=3)
    if event.keycode == 84:
        canvas.delete("all")
        label.config(text="Тангенс")
        canvas.create_line((SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]))
        canvas.create_line((0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2))
        x = -SCREEN_SIZE[0] // 2
        k = math.pi / SCREEN_SIZE[0]
        move_to(xs(x), ys(50 * math.tan(x * k)))
        for x in range(-SCREEN_SIZE[0] // 2 - 1, SCREEN_SIZE[1] // 2 + 1):
            line_to(xs(x), ys(100 * math.tan(x * k)), color='blue', width=3)


main = tkinter.Tk()
SCREEN_SIZE = [700, 700]
canvas = tkinter.Canvas(main, bg="white", height=SCREEN_SIZE[0], width=SCREEN_SIZE[1])
canvas.pack()
label = tkinter.Label(main, text="Функция")
canvas.create_line((SCREEN_SIZE[0] // 2, 0), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]))
canvas.create_line((0, SCREEN_SIZE[1] // 2), (SCREEN_SIZE[0], SCREEN_SIZE[1] // 2))
graph_pos = [canvas, 0, 0]
main.bind("<KeyPress>", draw)
label.pack()
main.mainloop()