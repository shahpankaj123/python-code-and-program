from tkinter import *
root = Tk()

root.title("Calculator")
root.minsize(280,280)
root.maxsize(280,280)
root.configure(background="gray",borderwidth="5px")

eqn = ""

def show(value):
    global eqn
    eqn+=value
    result.config(text=eqn)

def clear():
    global eqn
    eqn=""
    result.config(text=eqn)

def output():
    global eqn
    out = ""
    if eqn !="":
        try:
            out = eval(eqn)
        except:
            out ="Error!!!"
            eqn=""
    result.config(text=out)



result = Label(root,width=25,height=2,text="",borderwidth=5,bg="black",fg="white")
result.pack()

button_1 = Button(root,text="C",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :clear()).place(x=10,y=50)
button_2 = Button(root,text="%",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("%")).place(x=75,y=50)
button_3 = Button(root,text="/",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("/")).place(x=140,y=50)
button_4 = Button(root,text="*",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("*")).place(x=200,y=50)

button_5 = Button(root,text="7",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("7")).place(x=10,y=100)
button_6 = Button(root,text="8",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("8")).place(x=75,y=100)
button_7 = Button(root,text="9",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("9")).place(x=140,y=100)
button_8 = Button(root,text="-",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("-")).place(x=200,y=100)

button_9 = Button(root,text="4",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("4")).place(x=10,y=150)
button_10 = Button(root,text="5",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("5")).place(x=75,y=150)
button_11 = Button(root,text="6",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("6")).place(x=140,y=150)
button_12 = Button(root,text="+",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("+")).place(x=200,y=150)

button_13 = Button(root,text="1",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("1")).place(x=10,y=200)
button_14 = Button(root,text="2",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("2")).place(x=75,y=200)
button_15 = Button(root,text="3",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :show("3")).place(x=140,y=200)
button_16 = Button(root,text="=",width=5,height=2,borderwidth=5,bg="black",fg="green",command=lambda :output()).place(x=200,y=200)


root.mainloop()