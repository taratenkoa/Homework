import tkinter
n = int(input())
main = tkinter.Tk()
SCREEN_SIZE = [654, 902]
canvas = tkinter.Canvas(main, bg='white', height=SCREEN_SIZE[0], width=SCREEN_SIZE[1])
for i in range((SCREEN_SIZE[0] + n) // n):
    canvas.create_line(0, n * i, SCREEN_SIZE[1], n * i)
for i in range((SCREEN_SIZE[1] + n) // n + 1):
    canvas.create_line(n * i, 0, n * i, SCREEN_SIZE[0])
for i in range((SCREEN_SIZE[1] + n) // n * 2 + 1):
    canvas.create_line(n * i, 0, n * i - SCREEN_SIZE[0], SCREEN_SIZE[0])
for i in range(-((SCREEN_SIZE[1] + n) // n), (SCREEN_SIZE[1] + n) // n + 1):
    canvas.create_line(n * i, 0, n * i + SCREEN_SIZE[0], SCREEN_SIZE[0])
canvas.pack()
main.mainloop()