from pickletools import read_decimalnl_short
import posix
import tkinter as tk
from tkinter import *

[x0, y0, x1, y1] = [0, 50, 10, 100]
pos = [x0,y0,x1,y1]


def Etch():
    global Etch
    Etch = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill='grey', outline="")

sl_value = 3.63
def Etch_width(w):
    pos = can.coords(Etch)     
    pos[2] = sl_value * float(w)                    
    can.coords(Etch, pos[0], pos[1], pos[2], pos[3])
    return pos

def Etch_depth(d):
    pos = can.coords(Etch)
    pos[3] = int(d)
    can.coords(Etch, pos[0], pos[1], pos[2], pos[3])
    return pos

def Etch_spacing(s):
    pos = can.coords(Etch)
    for i in range(int(s)):
        pos[0] = pos[0] + 
        pos[2] = pos[2]
        can.coords(Etch, pos[0], pos[1], pos[2], pos[3])


root = Tk()
frame = Frame(root)
frame.pack()

width = Scale(frame, from_=0 , to=100, orient = HORIZONTAL, bg="blue",command = Etch_width)
width.pack()
height = Scale(frame, from_=0 , to=100, orient = HORIZONTAL, bg="yellow",command = Etch_depth)
height.pack()
spacing = Scale(frame, from_=0 , to=10, orient = HORIZONTAL, bg="pink",command = Etch_spacing)
spacing.pack()


btn_Etch = tk.Button(frame, text='Etch', width=20, command = Etch)
btn_Etch.pack()

can = Canvas(root,height=500,width=360, bg = 'green')
can.pack()




root.mainloop()