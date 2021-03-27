import tkinter


def motion(event):
    label.configure(text=f"Mouse position: ({event.x}, {event.y})")


def press(event):
    if event.num == 1:
        L.append([event.x, event.y])
    elif event.num == 3 and len(L) != 0:
        L.pop(-1)
    canvas.delete("all")
    if len(L) > 1:
        canvas.create_polygon(*L, fill="white", outline="black")
    for elem in L:
        canvas.create_oval(elem[0]-10, elem[1] - 10, elem[0]+10, elem[1]+10)


SCREEN_SIZE = [500, 500]
L = list()
main = tkinter.Tk()
canvas = tkinter.Canvas(main, width=SCREEN_SIZE[0], height=SCREEN_SIZE[1], bg="white")
canvas.bind('<Motion>', motion)
canvas.bind('<Button>', press)
canvas.pack()
label = tkinter.Label(main, text="Mouse position (0, 0): ")
label.pack()
main.mainloop()