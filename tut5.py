from tkinter import *
root=Tk()
root.geometry()
root.wm_minsize(400,300)
root.title("Student Form")

f1 = Frame(root,borderwidth=8,bg="gray")
f1.pack(anchor="sw")

f2 = Frame(root,borderwidth=5,bg="gray")
f2.pack(anchor="sw")

l1=Label(f1,text="Name :",fg="blue")
l1.pack()

l2=Label(f2,text="Age :",fg="blue")
l2.pack()


root.mainloop()