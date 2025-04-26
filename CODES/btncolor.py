from tkinter import*

win = Tk()

w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry(f"{w}x{h}")

f1 = Frame(win,bg="black",height=500,width=500)
f1.place(x=500,y=150)

def chnagecolor(color):
    f2.config(bg=color)

f2 = Frame (f1,height=300,width=300,bg="white")
f2.place(x=100,y=30)

# def gray():
#     f2.destroy()
#     f3 = Frame (f1,height=300,width=300,bg="gray")
#     f3.place(x=100,y=30)
# def pink():
#     f2.destroy()
#     f4 = Frame (f1,height=300,width=300,bg="pink")
#     f4.place(x=100,y=30)
# def lightblue():
#     f2.destroy()
#     f5 = Frame (f1,height=300,width=300,bg="lightblue")
#     f5.place(x=100,y=30)
# def yellow():
#     f2.destroy()
#     f6 = Frame (f1,height=300,width=300,bg="yellow")
#     f6.place(x=100,y=30)


b1 = Button(f1,bg="gray",width=3,command=lambda:f2.config(bg="gray"))
b1.place(x=50,y=400)

b2 = Button(f1,bg="pink",width=3,command=lambda:f2.config(bg="pink"))
b2.place(x=140,y=400)

b3 = Button(f1,bg="lightblue",width=3,command=lambda:f2.config(bg="lightblue"))
b3.place(x=230,y=400)

b4 = Button(f1,bg="yellow",width=3,command = lambda:chnagecolor("yellow"))
b4.place(x=310,y=400)

def cadetblue():
    f2.destroy()
    f7 = Frame (f1,height=300,width=300,bg="cadetblue")
    f7.place(x=100,y=30)

b5 = Button(f1,bg="cadetblue",width=3,command=cadetblue)
b5.place(x=400,y=400)

win.mainloop()