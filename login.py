from tkinter import *
from tkinter import messagebox
def login():
    username=data1.get()
    password=data2.get()
    if (username=="" and password==""):
        messagebox.showinfo("Error","empty not allowed")
    if(username=="Tinku" and password=="123"):
        messagebox.showinfo(""," login sucussfull !")
    else:
        messagebox.showinfo("Error","Incorrect username or password")

root=Tk()
root.title("Login")
root.minsize(height=250,width=300)
root.configure(bg="gray",bd=5)

global data1
global data2


Label(root,text="Username :").place(x=20,y=30)
Label(root,text="Password :").place(x=20,y=70)

data1=Entry(root,bd=5)
data1.place(x=100,y=30)

data2=Entry(root,bd=5)
data2.place(x=100,y=70)

Button(root,text="Login",command=login).place(x=170,y=110)




root.mainloop()