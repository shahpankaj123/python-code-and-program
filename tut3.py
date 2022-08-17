from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry()
root.wm_maxsize(900,500)
root.wm_minsize(900,500)

heading = Label(text="TINKU")
heading.pack()

photo = PhotoImage(file="scr.png")
tinku = Label(image=photo)
tinku.pack()
root.mainloop()