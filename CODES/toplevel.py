from tkinter import*

win = Tk()
win.title("Main Window")

def open_new_win():
    new_win = Toplevel(win)
    new_win.geometry("400x500")

    l1 = Label(new_win,text="NEW WINDOW",font="arial 20 bold")
    l1.pack()

b1 = Button(win,text="Open New Window",command=open_new_win)
b1.pack(padx=20,pady=20)

win.mainloop()