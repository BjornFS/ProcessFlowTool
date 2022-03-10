from tkinter import *
import tkinter as tk

[x0,y0,x1,y1] = [20, 50, 40, 10]

def rectangle():
    global rectangle
    rectangle = canvas.create_rectangle([x0,y0,x1,y1], fill="green")

def remove():
    canvas.delete(rectangle)
    widthslid.set(10)
    heightslid.set(10)

def width(e):
    x0, y0, x1, y1 = canvas.coords(rectangle) # get the coords of rect
    x1 = float(e)                             # calc new coords
    canvas.coords(rectangle, x0, y0, x1, y1)  # set new coords

def height(h):
    x0, y0, x1, y1 = canvas.coords(rectangle)
    y1 = float(h) + 40
    canvas.coords(rectangle, x0,y0,x1,y1)


root = Tk()
frame = Frame(root)
frame.pack()

IntVar = tk.BooleanVar() 
IntVar.set(False)

create_rect = Button(frame, text='rect', command = rectangle)
create_rect.pack()
remove_rect = Button(frame, text='remove', command = remove)
remove_rect.pack()
widthslid = Scale(frame, from_=10 , to=100, orient = HORIZONTAL, bg="blue",command = width)
widthslid.pack()
heightslid = Scale(frame, from_=10 , to=100, orient = HORIZONTAL, bg="green",command = height)
heightslid.pack()
canvas = Canvas(root,height=500,width=360)
canvas.pack()

root.mainloop()