from tkinter import *
import time
import os
root=Tk()

root.wm_minsize(300,300)
root.wm_maxsize(300,300)

root.title("Power app")



f1=Frame(borderwidth=8,bg="blue")
f1.pack()

l2=Label(f1,pady=200,padx=200)
l2.pack()



def showndown():
    os.system("shutdown /s /t 1")
def sleep():
    time.sleep(15)
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")

b1=Button(root,text="showndown",fg="red",bg="green",command=showndown)
b1.place(x=100,y=50)

b2=Button(root,text="Sleep",fg="red",bg="green",command=sleep)
b2.place(x=100,y=100)

b3=Button(root,text="Restart",fg="red",bg="green",command=restart)
b3.place(x=100,y=150)

b4=Button(root,text="restart_time",fg="red",bg="green",command=restart_time)
b4.place(x=100,y=200)












root.mainloop()