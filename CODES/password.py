from tkinter import*

win = Tk()
win.geometry("500x500")

l1 = Label(win,text="PASSWORD")
l1.pack()

pentry = Entry(win,width=40)
pentry.pack()

l2 = Label(win,text="",fg="red")
l2.pack()

def clicked():
    l1 = pentry.get()
    passwordsize = len(l1)

    if passwordsize > 8:
        l2.config(text="SUCCESFUL")
    else:
        l2.config(text="ERROR : PASSWORD MUST OF 8 CHARCTER")


btn = Button(win,text="SUBMIT",font="arial 16 bold",command=clicked)
btn.pack()

win.mainloop()