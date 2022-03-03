import tkinter as tk
from tkinter import *


############    MATERIALS

# init rgb converter
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb   

### Dielectica
def Silicon_Nitride():
    global Silicon_Nitride
    StructSilicon_Nitride = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,40,255)), outline="")
    CurrentStructure.append(StructSilicon_Nitride)

def Silicon_Oxide():
    global Silicon_Oxide
    StructSilicon_Oxide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,200)), outline="")
    CurrentStructure.append(StructSilicon_Oxide)

def Titanium_Oxide():
    global Titanium_Oxide
    StructTitanium_Oxide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,150,150)), outline="")
    CurrentStructure.append(StructTitanium_Oxide)

def Aluminium_Oxide():
    global Aluminium_Oxide
    StructAluminium_Oxide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((150,150,170)), outline="")
    CurrentStructure.append(StructAluminium_Oxide)

def Bulk_Glass():
    global Bulk_Glass
    StructBulk_Glass = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,200,200)), outline="")
    CurrentStructure.append(StructBulk_Glass)


### Semiconductors
def Silicon():
    global Silicon
    StructSilicon = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,255)), outline="")
    CurrentStructure.append(StructSilicon)

def Indium_Phosphide():
    global Indium_Phosphide
    StructIndium_Phosphide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,255)), outline="")
    CurrentStructure.append(StructIndium_Phosphide)

def Gallium_Arsenide():
    global Gallium_Arsenide
    StructGallium_Arsenide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,255)), outline="")
    CurrentStructure.append(StructGallium_Arsenide)

def Indium_Gallium_Arsenide():
    global Indium_Gallium_Arsenide
    StructIndium_Gallium_Arsenide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,255)), outline="")
    CurrentStructure.append(StructIndium_Gallium_Arsenide)

def Aluminium_Gallium_Arsenide():
    global Aluminium_Gallium_Arsenide
    StructAluminium_Gallium_Arsenide = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((30,144,255)), outline="")
    CurrentStructure.append(StructAluminium_Gallium_Arsenide)

### Metals
def Aluminium():
    global Aluminium
    StructAluminium = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructAluminium)

def Chromium():
    global Chromium
    StructChromium = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructChromium)

def Titanium():
    global Titanium
    StructTitanium = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructTitanium)

def Gold():
    global Gold
    StructGold = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructGold)

def Platinium():
    global Platinium
    StructPlatinium = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructPlatinium)

def MagneticStack():
    global MagneticStack
    StructMagneticStack = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((135,134,129)), outline="")
    CurrentStructure.append(StructMagneticStack)

### Alloys

### Polymers
def Polymers():
    global Polymers
    StructPolymers = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((0,153,0)), outline="")
    CurrentStructure.append(StructPolymers)

def Photoresist_SU8():
    global Photoresist_SU8
    StructPhotoresist_SU8 = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((0,153,0)), outline="")
    CurrentStructure.append(Photoresist_SU8)

def Topas():
    global Topas
    StructTopas = can.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill=_from_rgb((0,153,0)), outline="")
    CurrentStructure.append(StructTopas)

#def Custom():                                                                              UNDER CONSTRUCTION - custom




############    MAIN

# inital position
[x0, y0, x1, y1] = [40, 100, 190, 125]
pos = [x0,y0,x1,y1]

# savestate
[x0new, y0new, x1new, y1new] = [x0, y0, x1, y1]
pos_new = [x0new, y0new, x1new, y1new]

# storing the current structure, so when pressing go next, it automatically transfers it
CurrentStructure = []

# Spacing specifications
Length_wafer = int(150)
Height_wafer = int(25)
Height_layer = int(10)
Size_gap = int(75)
Size_init = int(40)
#Height_custom = 0                                                                          UNDER CONSTRUCTION - custom
Size_GoNext = Length_wafer + Size_gap
Size_SkipLine = 150


def AddLayer(pos):
        #if pos[3] - pos[1] == Height_wafer:     # checking if wafer
    pos[3] = pos[1]
    pos[1] = pos[1] - Height_layer

        #elif pos[3] - pos[1] == Height_layer:   # checking if layer
            #pos[1] = 
        #else:
            #print("error while adding layer")
        
        #print(pos)

def GoNext(pos):                                                                            #NEEDS TO NOT BE HARDCODED
    print("------------")
    print(pos)
    # First row --> go right
    if pos[2] < 640 and pos[1] <= 200:
        # Shifting the x-coords to the right
        pos[0] = pos[0] + Size_GoNext
        pos[2] = pos[2] + Size_GoNext
        print("x : right")

        # Returning the y-coords to baseline
        pos[1] = 100
        pos[3] = 125
        print("y : baseline")
        print("------------")
        print(pos)

    # Go to new line
    elif pos[2] >= 640:
        # Returning the x-coords to baseline
        pos[0] = 40
        pos[2] = 190
        print("x : baseline")

        # Shifting the y-coords to new line
        pos[1] = pos[1] + Size_SkipLine
        pos[3] = pos[3] + Size_SkipLine
        print("y : new line")
        print("------------")
        print(pos)
    
    # Second row --> go right
    elif pos[2] < 640 and pos[1] <=350:
        # Shifting the x-coords to the right
        pos[0] = pos[0] + Size_GoNext
        pos[2] = pos[2] + Size_GoNext
        print("x : right")

        # Returning the y-coords to baseline
        pos[1] = 250
        pos[3] = 275
        print("y : baseline")
        print("------------")
        print(pos)
    
    # Third row --> go right
    elif pos[2] < 640 and pos[1] <=500:
        # Shifting the x-coords to the right
        pos[0] = pos[0] + Size_GoNext
        pos[2] = pos[2] + Size_GoNext
        print("x : right")

        # Returning the y-coords to baseline
        pos[1] = 400
        pos[3] = 425
        print("y : baseline")
        print("------------")
        print(pos)
    
    # Fourth row --> go right
    elif pos[2] < 640 and pos[1] <=650:
        # Shifting the x-coords to the right
        pos[0] = pos[0] + Size_GoNext
        pos[2] = pos[2] + Size_GoNext
        print("x : right")

        # Returning the y-coords to baseline
        pos[1] = 550
        pos[3] = 575
        print("y : baseline")
        print("------------")
        print(pos)

    # Fifth row --> go right
    elif pos[2] < 640 and pos[1] <= 800:
        # Shifting the x-coords to the right
        pos[0] = pos[0] + Size_GoNext
        pos[2] = pos[2] + Size_GoNext
        print("x : right")

        # Returning the y-coords to baseline
        pos[1] = 700
        pos[3] = 725
        print("y : baseline")
        print("------------")
        print(pos)


############    GUI


### general config
root = tk.Tk()
root.title('tool')
root.resizable(width=False, height=False)
root.geometry("1400x800")
#root.attributes('-fullscreen', True)
root.configure(bg='light grey')


### canvas config
can = tk.Canvas(root, bg='white', height = 1000, width=680)
can.grid(row = 0, column=0)


### Materials config - MASTER FRAME
frame_mats = LabelFrame(root, text = "Materials", padx = 5, pady= 5)
frame_mats.grid(row = 0 , column= 1, sticky = N)

# Materials - SUB FRAMES
# Dielectrica
frame_diel = LabelFrame(frame_mats, text = "Dielectrica", padx = 5, pady = 5)
frame_diel.grid(row = 0, column=1, sticky = N)

# Semiconductors
frame_SeCo = LabelFrame(frame_mats, text = "Semiconductors", padx = 5, pady = 5)
frame_SeCo.grid(row = 2, column=1, sticky = N)

# Metals
frame_Metals = LabelFrame(frame_mats, text = "Metals", padx = 5, pady = 5)
frame_Metals.grid(row = 3, column=1, sticky = N)

# Polymers
frame_Poly = LabelFrame(frame_mats, text = "Polymers", padx = 5, pady = 5)
frame_Poly.grid(row = 4, column=1, sticky = N)


########################                    BUTTONS
# Dielectrica
btn_SiN = tk.Button(frame_diel, text='Silicon Nitride', width=20, command = Silicon_Nitride)
btn_SiO2 = tk.Button(frame_diel, text='Silicon Oxide', width=20, command = Silicon_Oxide)
btn_TiO2 = tk.Button(frame_diel, text='Titanium Oxide', width=20, command = Titanium_Oxide)
btn_AlO2 = tk.Button(frame_diel, text='Aluminium Oxide', width=20, command = Aluminium_Oxide)
btn_Glass = tk.Button(frame_diel, text='Bulk Glass', width=20, command = Bulk_Glass)

# Semiconductors
btn_Si = tk.Button(frame_SeCo, text='Silicon', width=20, command = Silicon)
btn_InP = tk.Button(frame_SeCo, text='Indium Phosphide', width=20, command= Indium_Phosphide)
btn_GaAs = tk.Button(frame_SeCo, text='Gallium Arsenide', width=20, command = Gallium_Arsenide)
btn_InGaAs = tk.Button(frame_SeCo, text='Indium Gallium Arsenide', width=20, command = Indium_Gallium_Arsenide)
btn_AlGaAs = tk.Button(frame_SeCo, text='Aluminium Gallium Arsenide', width=20, command = Aluminium_Gallium_Arsenide)

# Metals
btn_Al = tk.Button(frame_Metals, text='Aluminium', width=20, command = Aluminium)
btn_Cr = tk.Button(frame_Metals, text='Chromium', width=20, command = Chromium)
btn_Ti = tk.Button(frame_Metals, text='Titanium', width=20, command = Titanium)
btn_Au = tk.Button(frame_Metals, text='Gold', width=20, command = Gold)
btn_Pl = tk.Button(frame_Metals, text='Platinium', width=20, command = Platinium)
btn_MagS = tk.Button(frame_Metals, text='Magnetic Stack', width=20, command = MagneticStack)

# Alloys

# Polymers
btn_Pol = tk.Button(frame_Poly, text='Polymer', width=20, command = Polymers)
btn_PRSU8 = tk.Button(frame_Poly, text='Photoresist SU-8', width=20, command = Photoresist_SU8)
btn_Topas = tk.Button(frame_Poly, text='Topas', width=20, command = Topas)

btn_SiN.pack()
btn_SiO2.pack()
btn_TiO2.pack()
btn_AlO2.pack()
btn_Glass.pack()
btn_Si.pack()
btn_InP.pack()
btn_GaAs.pack()
btn_InGaAs.pack()
btn_AlGaAs.pack()
btn_Al.pack()
btn_Cr.pack()
btn_Ti.pack()
btn_Au.pack()
btn_Pl.pack()
btn_MagS.pack()
btn_Pol.pack()
btn_PRSU8.pack()
btn_Topas.pack()

# Custom Material
#frame_Custom = LabelFrame(frame_mats, text = "Custom Material", padx = 5, pady = 5)        UNDER CONSTRUCTION - custom
#frame_Custom.grid(row = 5, column=1, sticky = N)                                           UNDER CONSTRUCTION - custom


#Cmats = Entry(frame_Custom)                                                                UNDER CONSTRUCTION - custom
#CnameLabel = Label(frame_Custom, text = 'Material:')                                       UNDER CONSTRUCTION - custom
#CnameLabel.pack()                                                                          UNDER CONSTRUCTION - custom
#Cmats.pack()                                                                               UNDER CONSTRUCTION - custom
#CcolorLabel = Label(frame_Custom, text = 'Color:')                                         UNDER CONSTRUCTION - custom
#CcolorLabel.pack()                                                                         UNDER CONSTRUCTION - custom



# process config
frame_proc = LabelFrame(root, text = "Process", padx = 5, pady= 5)
frame_proc.grid(row = 0 , column= 2, sticky = N)

btn_Etch= tk.Button(frame_proc, text='etch', width=20) #, command = Etch
btn_Etch.pack()

btn_AddLayer = tk.Button(frame_proc, text = 'add layer', width = 20, command = lambda: AddLayer(pos))
btn_AddLayer.pack()

btn_GoNext = tk.Button(frame_proc, text = 'next', width = 20, command = lambda: GoNext(pos))
btn_GoNext.pack()


root.mainloop()