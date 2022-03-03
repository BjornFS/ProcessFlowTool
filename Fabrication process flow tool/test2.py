from tkinter import *

sl_value = 10
def width(e):
    x0, y0, x1, y1 = canvas.coords(rectangle) # get the coords of rect
    y1 = 3 * float(e)                         # calc new coords
    canvas.coords(rectangle, x0, y0, x1, y1)  # set new coords

root = Tk()
frame = Frame(root)
frame.pack()

slider = Scale(frame, from_=10 , to=100, orient = HORIZONTAL, bg="blue",command = width)
slider.pack()
canvas = Canvas(root,height=500,width=360)
canvas.pack()
rectangle = canvas.create_rectangle(20,50, 40,3*sl_value, fill="green")

root.mainloop()