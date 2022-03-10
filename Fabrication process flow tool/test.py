from pickletools import read_decimalnl_short
import posix
from tabnanny import check
import tkinter as tk
from tkinter import *

[x0, y0, x1, y1] = [0, 50, 10, 100]
pos = [x0,y0,x1,y1]

def Etch_width(w):
    width = float(w)
    return width

def Etch_depth(d):
    depth = int(d)
    return depth

def Etch_amount(n):
    amount = int(n)
    return amount 

def aligned(): #### needs to be implemented
    a = 0
    return a

def Etch_anisotropic(amount, depth, width):

    # Amount Computations
    for i in range(amount):
        pos[0] = (i * 50) - amount # + offset (if aligned or not) has to be an input to the function. 150 is the wafer size
        pos[2] = pos[0] + 10 # 10 is the initial width, later to be adjusted by the width() function
    global gratings
    gratings = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill= 'white')

    # Depth Computations
    pos[3] = pos[3] - depth * 10 #Height_layer

    # Width Computations
    pos[0] = pos[0] * int(width)/2
    pos[2] = pos[2] * (-int(width))/2


root = Tk()
frame = Frame(root)
frame.pack()

width = Scale(frame, from_=0 , to=100, orient = HORIZONTAL, bg="blue",command = Etch_width)
height = Scale(frame, from_=0 , to=3, orient = HORIZONTAL, bg="yellow",command = Etch_depth)
spacing = Scale(frame, from_=0 , to=10, orient = HORIZONTAL, bg="pink",command = Etch_amount)

spacing.pack()
height.pack()
width.pack()

Align_struct = tk.Checkbutton(frame, text='Aligned', variable= IntVar, command = aligned)
Align_struct.pack()

Anis_Etch = tk.Checkbutton(frame, text='Anisopotropic Etch', variable=IntVar, command = Etch_anisotropic)
Anis_Etch.pack()

can = Canvas(root,height=500,width=360, bg = 'green')
can.pack()




root.mainloop()