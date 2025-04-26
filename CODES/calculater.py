from tkinter import*
window = Tk()

window.geometry("400x300")

l1 = Label(window,text="Enter your NUmber1 : ")
l1.grid(row=0,column=0)

Entry1 = Entry(window)
Entry1.grid(row=0,column=1)

l2 = Label(window,text="Enter your NUmber2 : ")
l2.grid(row=1,column=0)

Entry2 = Entry(window)
Entry2.grid(row=1,column=1)

def Addition():
    Number1 = Entry1.get()
    Number2 = Entry2.get()
    Sum = int(Number1) + int(Number2)
    print(Sum)
    Entry3.delete(0,END)
    Entry3.insert(0,Sum)
    # l3.config(text="Ans {}".format(Sum))

btn1 = Button(window,text="+",width=10,command=Addition)
btn1.grid(row=3,column=0)

def Subtraction():
    Number1 = Entry1.get()
    Number2 = Entry2.get()
    Sub = int(Number1) - int(Number2)
    print(Sub)
    Entry3.delete(0,END)
    Entry3.insert(0,Sub)
    # l3.config(text="Ans {}".format(Sub))

btn2 = Button(window,text="-",width=10,command=Subtraction)
btn2.grid(row=3,column=1)

def Multipul():
    Number1 = Entry1.get()
    Number2 = Entry2.get()
    Mul = int(Number1) * int(Number2)
    print(Mul)
    Entry3.delete(0,END)
    Entry3.insert(0,Mul)
    # l3.config(text="Ans {}".format(mul))

btn3 = Button(window,text="*",width=10,command=Multipul)
btn3.grid(row=4,column=0)

def Division():
    Number1 = Entry1.get()
    Number2 = Entry2.get()
    Div = int(Number1) / int(Number2)
    print(Div)
    Entry3.delete(0,END)
    Entry3.insert(0,Div)
    # l3.config(text="Ans {}".format(div))

btn4 = Button(window,text="/",width=10,command=Division)
btn4.grid(row=4,column=1)

l3 = Label(window,text="Result of the selected one : ")
l3.grid(row=5,column=0)

Entry3 = Entry(window)
Entry3.grid(row=5,column=1)

window.mainloop()
