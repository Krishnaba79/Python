from tkinter import*
root = Tk()

root.geometry("1800x1700")

panded_win = PanedWindow(root,orient=HORIZONTAL)
panded_win.pack(fill=BOTH,expand=True)

# leftframe = Frame(panded_win,bg="pink",width=200,height=800)

whiteframe = Frame(panded_win,bg="white",width=200,height=400)
blackframe = Frame(panded_win,bg="black",width=200,height=400)

def  btnclicked():
    panded_win.forget(blackframe)
    pinkframe = Frame(panded_win,bg="pink",width=200,height=400)
    panded_win.add(pinkframe)

def jadu():
    # panded_win.forget(pinkframe)
    blueframe = Frame(panded_win,bg="blue",width=200,height=400)
    panded_win.add(blueframe)

btn = Button(panded_win,text="HOME",font="arial 20 bold",command=btnclicked)
btn.place(x=10,y=100)

btn1 = Button(panded_win,text="jadu",font="arial 20 bold",command=jadu)
btn1.place(x=10,y=200)

panded_win.add(whiteframe)
panded_win.add(blackframe)

root.mainloop()