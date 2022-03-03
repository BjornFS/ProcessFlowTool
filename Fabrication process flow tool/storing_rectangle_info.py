from tkinter import Canvas
import tkinter

_width = 50
_height = 50
_size = 8

root = tkinter.Tk()
root.title("draw me a lovely matrix")
canv = Canvas(root, width=_width * _size, height=_height * _size)
rects = []

# B1-Motion activates every time the mouse is moved with button 1 held down
# See https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# We fill every item that the mouse comes in contact with while button 1 is held
# The tag tied to the item the event was called on, "current", points to the
#   item under the pointer when the button was pressed, i.e. the first box.
# Only the x and y properties change, so we configure the item closest to those.
def motion(event):
  canv.itemconfig(canv.find_closest(event.x, event.y), fill="#aaa")
canv.bind("<B1-Motion>", motion)

for i in range(_size):
    for j in range(_size):
        rects.append(canv.create_rectangle(_width * j, _height * i, _width * (j + 1), _height * (i + 1), fill="#fff", width=0))
        # don't need to bind anything to <Enter>
    print(rects[i])

canv.pack()
root.mainloop()