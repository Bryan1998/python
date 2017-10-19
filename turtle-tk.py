import turtle
import tkinter as tk

def key(event):
	forward()
	backward()
	left()
	right()

def forward():
	t.forward(10)

def back():
	t.backward(10)

def left():
	t.left(17.5)

def right():
	t.right(17.5)

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()

root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('<Up>',forward)
root.bind('<Down>',backward)

t = turtle.RawTurtle(canvas)

tk.Button(master = root, text = "Forward 10px", command = forward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Back 10px", command = backward).pack(side = tk.LEFT)
tk.Button(master = root, text = "Left 17.5d", command = left).pack(side = tk.LEFT)
tk.Button(master = root, text = "Right 17.5d", command = right).pack(side = tk.LEFT)

root.mainloop()
