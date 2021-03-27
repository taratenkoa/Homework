import tkinter
L1 = [[3, 3], [101, 101], [203, 3], [301, 101], [403, 3], [501, 101], [603, 3], [701, 101]]
L2 = [[i[0] + 100, i[1] + 100] for i in L1]
L3 = [[i[0], i[1] + 200] for i in L1]
A = L1 + L2 + L3
K1 = [[i[0], i[1] + 400] for i in L2]
K2 = [[i[0], i[1] + 600] for i in L1]
K3 = [[i[0], i[1] + 600] for i in L2]
B = K1 + K2 + K3
main = tkinter.Tk()
canvas = tkinter.Canvas(main, bg='white', height=800, width=800)
for i in range(9):
    canvas.create_line(2, 100 * i + 2, 802, 100 * i + 2)
    canvas.create_line(100 * i + 2, 2, 100 * i + 2, 802)
    canvas.create_line(2, 801, 802, 801)
    canvas.create_line(801, 2, 801, 802)
for i in range(0, len(A), 2):
    canvas.create_oval((A[i][0], A[i][1]), (A[i + 1][0], A[i + 1][1]), fill='red', outline="black")
for i in range(0, len(B), 2):
    canvas.create_oval((B[i][0], B[i][1]), (B[i + 1][0], B[i + 1][1]), fill='blue', outline="black")
canvas.pack()
main.mainloop()