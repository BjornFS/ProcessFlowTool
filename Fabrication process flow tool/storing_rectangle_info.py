#Import the required library
from tkinter import*
from tkinter import ttk
#Create an instance of tkinter frame
win= Tk()
#Set the geometry
win.geometry("750x250")
#Define geometry of the window
win.geometry("750x250")
#Create CheckButtons
chk= ttk.Checkbutton(win, text="Python")
chk.pack()
chk.config(state=NORMAL)
print(chk.state())
win.mainloop()